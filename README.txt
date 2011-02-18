== Sark Notes ==
= Douglas Greiman =

I. Installing 4D ODBC Drivers to connect to the Embark database

1. Find the folder "4D2004DriverFiles"

   This is derived from the official "ODBC Driver 2004.7" from 4D Inc,
   with hand-crafted registry entries to work on Windows 7 64 bit.
   
   Right click on "Install 4D ODBC Driver for Windows 7 64 bit.reg" and
   choose "Merge"

   Copy the 5 files starting with "4DOD..." to the 
   c:\Windows\SysWOW64 directory.

   Start the 32bit ODBC Administrator interface
   C:\Windows\SysWOW64\odbcad32.exe

   On "User DSN" tab, click "Add...".  
   Ignore error message about CTL3D32.DLL -- I haven't figured out how to fix this yet.
   
   xxx DID NOT WORK xxx
   xxxx Register 32bit CTL3D32.DLL by opening command prompt in 
   xxxx   C:\Windows\SysWOW64 and typing
   xxxx   C:\Windows\SysWOW64\regsvr32.exe C:\Windows\SysWOW64\CTL3D32.DLL
   xxxxxxxxxxxxxxxxxxxx
   xxxx   Copy C:\Windows\SysWOW64\CTL3D32.DLL to C:\Windows\System32\CTL3D32.DLL
   xxxxxxxxxxxxxxxxxxxx

   Set "Data Source Name" to "EmbARK Server"
   Set "Network Path" to whatever connects to the server.  Click "Test data source ..."
   "User name" and "Password" are blank.

   Copy latest Embark Datafiles to local machine.  Start Embark Server on local machine.

   Install "ODBC Explorer 1.2.4 Trial" on local machine.

   Error message on Table "OBJECT_1": 

   [Simba][Simba ODBC Driver][Codebase File Library]
   SQLState: S1000
   Native error code: -9583

   xxx DID NOT WORK xxx
   xxxx Tried various settings of APILevel, SQLLevel, DriverODBCVer
   xxxxxxxxxxxxxxxxxxxx

2. Interlude to install Pyton 2.7 and pyodbc

   Download and install Windows 32-bit Python 2.7.x to C:\Python27

   Download and install pyodbc for 32-bit Python 2.7.x

3. Run Python utility to dump Embark database

   Edit EmbarkDBDump.conf to set output directory

   Run
       python EmbarkDBDump.py
   
4. 4D ODBC Driver/PyODBC Programming Notes
   
   A) In SELECT statements, column names should be double quoted, i.e.
      SELECT "_Object_1_ID" FROM OBJECTS_1

   B) In SELECT statements, LIMIT X is not allowed

   C) The maximum number of columns that can be in a single SELECT is,
      by empirical testing, 79 or less.  More than that crashes the
      process.  Probably should use somewhat less than 79 to give
      a buffer against other unknown limits.

5. A list of characters encountered in the Embark Database

   CP1252 Code Page?

   Table Name:		Hex code:      Intended character (a guess):
   _FM_FIELDS		\x92	       U+2019 --> '
   _FM_FIELDS		\x93	       U+201C --> "
   _FM_FIELDS		\x94	       U+201D --> "
   _FM_FIELDS		\r	       Mistake (omit)
   _FM_FIELDS		\x01	       Newline ?
   _FM_FIELDS		\xe0	       U+00E1 == á
   _FM_FIELDS		\xa5	       U+00A5 == ¥
   _FM_FIELDS		\xe8	       U+00E8 == è
   _MENU_ITEMS		\x85	       U+2026 == …   
