************************************************************************
 EmbarkDBCopy.py
 Author: Douglas Greiman

 This program dumps the structure and data of an Embark database
 into a single file in sqlite3 format.

 This code is quick, dirty, and probably should not be used by anyone.

************************************************************************

I. Install 4D ODBC Drivers to connect to the Embark database

2. Install Pyton 2.7 (64 bit) and pyodbc

3. Run Python utility to dump Embark database

   Edit EmbarkDBDump.conf to set output directory

   $ python EmbarkDBDump.py
