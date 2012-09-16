************************************************************************
 EmbarkDBCopy.py
 Author: Douglas Greiman

 This program dumps the structure and data of an Embark database
 into a single file in sqlite3 format.
************************************************************************

I. Installing 4D ODBC Drivers to connect to the Embark database

1. Find the folder "4D v11 SQL Release 9 Custom"

   Run the file "4D ODBC Driver.exe"

2. Interlude to install Pyton 2.7 and pyodbc

   Download and install Windows 32-bit Python 2.7.x to C:\Python27

   Download and install pyodbc for 32-bit Python 2.7.x

3. Run Python utility to dump Embark database

   Edit EmbarkDBDump.conf to set output directory

   Run
       python EmbarkDBDump.py
   
4. 4D ODBC Driver/PyODBC Programming Notes [*Not verified for 4D v11]
   
   A) In SELECT statements, column names should be double quoted, i.e.
      SELECT "_Object_1_ID" FROM OBJECTS_1

   B) In SELECT statements, LIMIT X is not allowed

   C) The maximum number of columns that can be in a single SELECT is,
      by empirical testing, 79 or less.  More than that crashes the
      process.  Probably should use somewhat less than 79 to give
      a buffer against other unknown limits.

5. As of 4D v11, we hope that all text fields are UTF-8
