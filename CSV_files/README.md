# Reading and Writing a CSV File
* There are various ways to read a CSV file that uses either the CSV module or the pandas library.

- csv Module: The CSV module is one of the modules in Python which provides classes for reading and     writing tabular information in CSV file format.

- pandas Library: The pandas library is one of the open-source Python libraries that provide high-performance, convenient data structures and data analysis tools and techniques for Python programming.

* **Read using csv.DictReader() class:** the CSV file is first opened using the open() method then it is read by using the DictReader class of csv module which works like a regular reader but maps the information in the CSV file into a dictionary. The very first line of the file consists of dictionary keys. 

* There are various classes provide by csv  module for writting to csv:
- using csv.writer class
- using csv.DictWritter class

* **Write using cvs.DictWritter() class**: this class returns a writer object which maps directories onto output rows.


* **Write using pandas module**:You can save your Pandas DataFrame as a CSV file with .to_csv(data)
  