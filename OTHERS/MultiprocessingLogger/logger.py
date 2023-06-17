import logging
import logging.handlers
import multiprocessing
import os
import sys

from pathlib import Path

class MultiProcesses_Logging_Helper:

    def __init__(self) -> None:
        self.queue = multiprocessing.Manager().Queue(-1)
        
        self.process = multiprocessing.get_context('fork').Process(
            target=self._process_target,
        )
        self.process.start()
        self.redirect_main_process_log_to_queue()

    def get_log_file_path(self) -> str:
        # TODO: make this configurable
        log_file_dir = os.path.join(Path(__file__).parent, 'logs')
        Path(log_file_dir).mkdir(parents=True, exist_ok=True)
        log_file_path = os.path.join(log_file_dir, 'multip.log')
        return log_file_path

    def redirect_main_process_log_to_queue(self):

        main_process_id = os.getpid()

        def filter(record: logging.LogRecord):
            if record.process == main_process_id:
                self.queue.put_nowait(record)
            return None

        root = logging.getLogger()
        root.setLevel(logging.INFO)

        handler = logging.Handler()
        handler.addFilter(filter)
        root.addHandler(handler)

    def init_logger_configure(self):
        
        root = logging.getLogger()
        root.setLevel(logging.INFO)

        # TODO: make this configurable
        file_handler = logging.handlers.RotatingFileHandler(
            self.get_log_file_path(),
            mode='w',
            # maxBytes=5000,
            # backupCount=0,
            encoding='utf-8'
        )
        file_handler.setLevel(logging.INFO)
        file_handler_formatter = logging.Formatter(
            fmt='%(asctime)s | %(name)s | %(levelname)s | %(pathname)s:%(lineno)d | %(process)d | %(message)s',
            datefmt="%m-%d %H:%M:%S"
        )
        file_handler.setFormatter(file_handler_formatter)
        root.addHandler(file_handler)

        std_handler = logging.StreamHandler(sys.stdout)
        std_handler.setLevel(logging.DEBUG)
        std_handler_formatter = logging.Formatter(
            fmt='%(asctime)s | %(name)s | %(levelname)s | %(pathname)s:%(lineno)d | %(process)d | %(message)s',
            datefmt="%m-%d %H:%M:%S"
        )
        std_handler.setFormatter(std_handler_formatter)
        root.addHandler(std_handler)

    def _process_target(self):
        self.init_logger_configure()
        while True:
            record: logging.LogRecord = self.queue.get()
            if record is None:
                break
            logger = logging.getLogger(record.name)
            logger.handle(record)

    def close(self):
        self.process.join(timeout=0)
        self.process.terminate()
