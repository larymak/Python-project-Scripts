# Python Logging Helper for Multiple Processes

## Description
This is a helper class that allows Python developers to log to a single log file from multiple processes easily.

## Examples
The following is an example code snippet in **main.py**, which provides two modes:

1. Running in Multiprocessing Pool:
```python
python3 main.py --is_pool yes
```

1. Running in Normal Multiprocessing:
```python
python3 main.py --is_pool no
```

The log file will be created in the log directory and named mulp.log.

* Log File Content
```
06-17 13:41:13 | sub | INFO | /projects/OTHERS/MultiprocessingLogger/main.py:19 | 26802 | c
06-17 13:41:13 | sub | INFO | /projects/OTHERS/MultiprocessingLogger/main.py:19 | 26803 | d
06-17 13:41:13 | sub | INFO | /projects/OTHERS/MultiprocessingLogger/main.py:19 | 26799 | a
06-17 13:41:13 | sub | INFO | /projects/OTHERS/MultiprocessingLogger/main.py:19 | 26804 | e
06-17 13:41:13 | sub | INFO | /projects/OTHERS/MultiprocessingLogger/main.py:19 | 26801 | b
```