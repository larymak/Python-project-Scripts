import argparse
import logging
import logging.handlers
import multiprocessing
from functools import partial
from logger import MultiProcesses_Logging_Helper


def process_target(queue: multiprocessing.Queue, input: str):
    # add queue handler at the beginning of the process
    sub_logger = logging.getLogger('sub')
    sub_logger.setLevel(logging.INFO)
    queue_handler = logging.handlers.QueueHandler(queue)

    # this process may be reused multiple times (when multiprocessing pool) 
    if len(sub_logger.handlers) == 0 or not isinstance(sub_logger.handlers[0], logging.handlers.QueueHandler):
        sub_logger.addHandler(queue_handler)

    sub_logger.info(input)


def main(is_pool: bool):
    logger_helper = MultiProcesses_Logging_Helper()

    if is_pool:
        print("run in multiprocessing pool")
        pool = multiprocessing.Pool(2)
        inputs = [i for i in ["a", "b", "c", "d", "e"]]
        pool.map(partial(process_target, logger_helper.queue), inputs)
        logger_helper.queue.put_nowait(None)
        pool.close()
        pool.join()
    else:    
        print("run in multiprocessing")
        workers = []
        for i in ["a", "b", "c", "d", "e"]:
            worker = multiprocessing.get_context('fork').Process(target=process_target,
                                                args=(logger_helper.queue, i))
            workers.append(worker)
            worker.start()
        for w in workers:
            w.join()
        logger_helper.queue.put_nowait(None)

    logger_helper.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-p', '--is_pool', help='is run in multiprocessing pool mode', default=True, type=lambda x: (str(x).lower() in ['true','1', 'yes', 'y', 'True']))
    args = parser.parse_args()
    main(args.is_pool)
