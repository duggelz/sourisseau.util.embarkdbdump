#!/usr/bin/python2.7
#
# Douglas Greiman
# January 12, 2011
#
# Export all the data from an Embark server using the 4D 2004.7
# ODBC driver.
#
#
# Empirical Stuff:
#   Result of running embark_cursor.getTypeInfo():
#   v9.5.1
#     000 (u'BOOLEAN', -7, 5, None, None, None, 2, 0, 2, 1, 0, 0, u'BOOLEAN', 0, 0, -7, 0, 10, 10)
#     001 (u'TEXT', 1, 256, u"'", u"'", None, 2, 1, 1, 0, 0, 0, u'TEXT', 0, 0, 1, 0, 10, 10)
#     002 (u'TEXT', -8, 256, u"'", u"'", None, 2, 1, 1, 0, 0, 0, u'TEXT', 0, 0, -8, 0, 10, 10)
#     003 (u'BYTE', -6, 4, None, None, None, 2, 0, 2, 0, 0, 1, u'BYTE', 0, 0, -6, 0, 10, 10)
#     004 (u'INT16', 5, 6, None, None, None, 2, 0, 2, 0, 0, 1, u'INT16', 0, 0, 5, 0, 10, 10)
#     005 (u'INT32', 4, 11, None, None, None, 2, 0, 2, 0, 0, 1, u'INT32', 0, 0, 4, 0, 10, 10)
#     006 (u'UUID', -11, 32, None, None, None, 2, 0, 2, 0, 0, 1, u'UUID', 0, 0, -11, 0, 10, 10)
#     007 (u'INT64', -5, 20, None, None, None, 2, 0, 2, 0, 0, 1, u'INT64', 0, 0, -5, 0, 10, 10)
#     008 (u'REAL', 7, 7, None, None, None, 2, 0, 2, 0, 0, 0, u'REAL', 0, 0, 7, 0, 10, 10)
#     009 (u'DOUBLE PRECISION', 8, 15, None, None, None, 2, 0, 2, 0, 0, 0, u'DOUBLE PRECISION', 0, 0, 8, 0, 10, 10)
#     010 (u'DOUBLE PRECISION', 2, 10, None, None, None, 2, 0, 2, 0, 0, 0, u'DOUBLE PRECISION', 0, 0, 2, 0, 10, 10)
#     011 (u'BINARY', -2, 0, None, None, None, 2, 0, 2, 1, 0, 0, u'BINARY', 0, 0, -2, 0, 10, 10)
#     012 (u'TIMESTAMP', 91, 10, None, None, None, 2, 0, 2, 1, 0, 0, u'TIMESTAMP', 0, 0, 9, 1, 10, 10)
#     013 (u'DURATION', 92, 8, None, None, None, 2, 0, 2, 1, 0, 0, u'DURATION', 0, 0, 92, 0, 10, 10)
#     014 (u'TIMESTAMP', 93, 19, None, None, None, 2, 0, 2, 1, 0, 0, u'TIMESTAMP', 0, 0, 9, 3, 10, 10)
#     015 (u'DURATION', 110, 10, None, None, None, 2, 0, 2, 1, 0, 0, u'DURATION', 0, 0, 9, 2, 10, 10)
#    .description
#     000 ('type_name', <type 'unicode'>, None, 256, 256, 0, True)
#     001 ('data_type', <type 'int'>, None, 2, 2, 0, True)
#     002 ('column_size', <type 'int'>, None, 4, 4, 0, True)
#     003 ('literal_prefix', <type 'unicode'>, None, 256, 256, 0, True)
#     004 ('literal_suffix', <type 'unicode'>, None, 256, 256, 0, True)
#     005 ('create_params', <type 'unicode'>, None, 256, 256, 0, True)
#     006 ('nullable', <type 'int'>, None, 2, 2, 0, True)
#     007 ('case_sensitive', <type 'int'>, None, 2, 2, 0, True)
#     008 ('searchable', <type 'int'>, None, 2, 2, 0, True)
#     009 ('unsigned_attribute', <type 'int'>, None, 2, 2, 0, True)
#     010 ('fixed_prec_scale', <type 'int'>, None, 2, 2, 0, True)
#     011 ('auto_unique_value', <type 'int'>, None, 2, 2, 0, True)
#     012 ('local_type_name', <type 'unicode'>, None, 256, 256, 0, True)
#     013 ('minimum_scale', <type 'int'>, None, 2, 2, 0, True)
#     014 ('maximum_scale', <type 'int'>, None, 2, 2, 0, True)
#     015 ('sql_data_type', <type 'int'>, None, 2, 2, 0, True)
#     016 ('sql_datetime_sub', <type 'int'>, None, 2, 2, 0, True)
#     017 ('num_prec_radix', <type 'int'>, None, 4, 4, 0, True)
#     018 ('interval_precision', <type 'int'>, None, 2, 2, 0, True)
#
#   v8
#     (u'BOOLEAN', -7, 5, None, None, None, 2, 0, 2, 1, 0, 0, u'BOOLEAN', 0, 0, -7, 0, 10, 10)
#     (u'TEXT', 1, 256, u"'", u"'", None, 2, 1, 1, 0, 0, 0, u'TEXT', 0, 0, 1, 0, 10, 10)
#     (u'TEXT', -8, 256, u"'", u"'", None, 2, 1, 1, 0, 0, 0, u'TEXT', 0, 0, -8, 0, 10, 10)
#     (u'BYTE', -6, 4, None, None, None, 2, 0, 2, 0, 0, 1, u'BYTE', 0, 0, -6, 0, 10, 10)
#     (u'INT16', 5, 6, None, None, None, 2, 0, 2, 0, 0, 1, u'INT16', 0, 0, 5, 0, 10, 10)
#     (u'INT32', 4, 11, None, None, None, 2, 0, 2, 0, 0, 1, u'INT32', 0, 0, 4, 0, 10, 10)
#     (u'UUID', -11, 32, None, None, None, 2, 0, 2, 0, 0, 1, u'UUID', 0, 0, -11, 0, 10, 10)
#     (u'INT64', -25, 20, None, None, None, 2, 0, 2, 0, 0, 1, u'INT64', 0, 0, -25, 0, 10, 10)
#     (u'REAL', 7, 7, None, None, None, 2, 0, 2, 0, 0, 0, u'REAL', 0, 0, 7, 0, 10, 10)
#     (u'DOUBLE PRECISION', 8, 15, None, None, None, 2, 0, 2, 0, 0, 0, u'DOUBLE PRECISION', 0, 0, 8, 0, 10, 10)
#     (u'DOUBLE PRECISION', 2, 10, None, None, None, 2, 0, 2, 0, 0, 0, u'DOUBLE PRECISION', 0, 0, 2, 0, 10, 10)
#     (u'BINARY', -2, 0, None, None, None, 2, 0, 2, 1, 0, 0, u'BINARY', 0, 0, -2, 0, 10, 10)
#     (u'TIMESTAMP', 91, 10, None, None, None, 2, 0, 2, 1, 0, 0, u'TIMESTAMP', 0, 0, 9, 1, 10, 10)
#     (u'DURATION', 92, 8, None, None, None, 2, 0, 2, 1, 0, 0, u'DURATION', 0, 0, 92, 0, 10, 10)
#     (u'TIMESTAMP', 93, 19, None, None, None, 2, 0, 2, 1, 0, 0, u'TIMESTAMP', 0, 0, 9, 3, 10, 10)
#     (u'DURATION', 110, 10, None, None, None, 2, 0, 2, 1, 0, 0, u'DURATION', 0, 0, 9, 2, 10, 10)
#
#   .description
#     ('type_name', <type 'unicode'>, None, 256, 256, 0, True)
#     ('data_type', <type 'int'>, None, 2, 2, 0, True)
#     ('column_size', <type 'int'>, None, 4, 4, 0, True)
#     ('literal_prefix', <type 'unicode'>, None, 256, 256, 0, True)
#     ('literal_suffix', <type 'unicode'>, None, 256, 256, 0, True)
#     ('create_params', <type 'unicode'>, None, 256, 256, 0, True)
#     ('nullable', <type 'int'>, None, 2, 2, 0, True)
#     ('case_sensitive', <type 'int'>, None, 2, 2, 0, True)
#     ('searchable', <type 'int'>, None, 2, 2, 0, True)
#     ('unsigned_attribute', <type 'int'>, None, 2, 2, 0, True)
#     ('fixed_prec_scale', <type 'int'>, None, 2, 2, 0, True)
#     ('auto_unique_value', <type 'int'>, None, 2, 2, 0, True)
#     ('local_type_name', <type 'unicode'>, None, 256, 256, 0, True)
#     ('minimum_scale', <type 'int'>, None, 2, 2, 0, True)
#     ('maximum_scale', <type 'int'>, None, 2, 2, 0, True)
#     ('sql_data_type', <type 'int'>, None, 2, 2, 0, True)
#     ('sql_datetime_sub', <type 'int'>, None, 2, 2, 0, True)
#     ('num_prec_radix', <type 'int'>, None, 4, 4, 0, True)
#     ('interval_precision', <type 'int'>, None, 2, 2, 0, True)
#
#   v7
#     ('BOOLEAN', -7, 1, None, None, None, 1, 0, 2, None, 0, None, 'BOOLEAN', 0, 0)
#     ('BOOLEAN', -6, 3, None, None, None, 1, 0, 2, 0, 0, 0, 'BOOLEAN', 0, 0)
#     ('BLOB', -4, 2147483647, "'", "'", None, 1, 0, 0, None, 0, None, 'BLOB', None, None)
#     ('TEXT', -1, 65500, "'", "'", None, 1, 1, 3, None, 0, None, 'TEXT', None, None)
#     ('STRING', 1, 256, "'", "'", None, 1, 1, 3, None, 0, None, 'STRING', None, None)
#     ('REAL', 3, 8, None, None, None, 1, 0, 2, 0, 0, 0, 'REAL', 0, 10)
#     ('LONGINT', 4, 10, None, None, None, 1, 0, 2, 0, 0, 0, 'LONGINT', 0, 0)
#     ('INTEGER', 5, 5, None, None, None, 1, 0, 2, 0, 0, 0, 'INTEGER', 0, 0)
#     ('UNKNOWN', 6, 15, None, None, None, 1, 0, 2, None, 0, None, 'UNKNOWN', None, None)
#     ('REAL', 8, 15, None, None, None, 1, 0, 2, 0, 0, 0, 'REAL', None, None)
#     ('DATE', 9, 10, "'", "'", None, 1, 0, 3, None, 0, None, 'DATE', None, None)
#     ('TIME', 10, 8, "'", "'", None, 1, 0, 3, None, 0, None, 'TIME', None, None)
#     ('STRING', 12, 255, "'", "'", None, 1, 1, 3, None, 0, None, 'STRING', None, None)
#   .description():
#     ('type_name', <type 'str'>, None, 128, 128, 0, False),
#     ('data_type', <type 'int'>, None, 5, 5, 0, False),
#     ('precision', <type 'int'>, None, 10, 10, 0, True),
#     ('literal_prefix', <type 'str'>, None, 128, 128, 0, True),
#     ('literal_suffix', <type 'str'>, None, 128, 128, 0, True),
#     ('create_params', <type 'str'>, None, 128, 128, 0, True),
#     ('nullable', <type 'int'>, None, 5, 5, 0, False),
#     ('case_sensitive', <type 'int'>, None, 5, 5, 0, False),
#     ('searchable', <type 'int'>, None, 5, 5, 0, False),
#     ('unsigned_attribute', <type 'int'>, None, 5, 5, 0, True),
#     ('money', <type 'int'>, None, 5, 5, 0, False),
#     ('auto_increment', <type 'int'>, None, 5, 5, 0, True),
#     ('local_type_name', <type 'str'>, None, 128, 128, 0, True),
#     ('minimum_scale', <type 'int'>, None, 10, 10, 0, True),
#     ('maximum_scale', <type 'int'>, None, 10, 10, 0, True))
#
#   Result of running embark_cursor.tables():
#   v8
#     ('table_cat', <type 'unicode'>, None, 256, 256, 0, True),
#     ('table_schem', <type 'unicode'>, None, 256, 256, 0, True),
#     ('table_name', <type 'unicode'>, None, 256, 256, 0, True),
#     ('table_type', <type 'unicode'>, None, 256, 256, 0, True),
#     ('remarks', <type 'unicode'>, None, 256, 256, 0, True)]
#
#     E.g. (None, None, u'_Debug', u'TABLE', None)
#   v7
#     ('table_qualifier', <type 'str'>, None, 128, 128, 0, True),
#     ('table_owner', <type 'str'>, None, 128, 128, 0, True),
#     ('table_name', <type 'str'>, None, 128, 128, 0, True),
#     ('table_type', <type 'str'>, None, 128, 128, 0, True),
#     ('remarks', <type 'str'>, None, 254, 254, 0, True))
#
#     1. table_cat: The catalog name.
#     2. table_schem: The schema name.
#     3. table_name: The table name.
#     4. table_type: One of TABLE, VIEW, SYSTEM TABLE, GLOBAL TEMPORARY, LOCAL TEMPORARY, ALIAS, SYNONYM, or a data source-specific type name.
#     5. remarks: A description of the table.
#
#     E.g. ('C:\\USERS\\DUGGELZ\\DESKTOP\\4D ODBC DRIVER FOR WINDOWS 7 64BIT', None, '_AAT_OTHERTERMS', 'TABLE', None)
#
#   Result of running embark_cursor.columns():
#     ('table_qualifier', <type 'str'>, None, 128, 128, 0, True),
#     ('table_owner', <type 'str'>, None, 128, 128, 0, True),
#     ('table_name', <type 'str'>, None, 128, 128, 0, False),
#     ('column_name', <type 'str'>, None, 128, 128, 0, False),
#     ('data_type', <type 'int'>, None, 5, 5, 0, False),
#     ('type_name', <type 'str'>, None, 128, 128, 0, False),
#     ('precision', <type 'int'>, None, 10, 10, 0, True),
#     ('length', <type 'int'>, None, 10, 10, 0, True),
#     ('scale', <type 'int'>, None, 5, 5, 0, True),
#     ('radix', <type 'int'>, None, 5, 5, 0, True),
#     ('nullable', <type 'int'>, None, 5, 5, 0, False),
#     ('remarks', <type 'str'>, None, 254, 254, 0, True))
#
#     E.g. ('C:\\USERS\\DUGGELZ\\DESKTOP\\4D ODBC DRIVER FOR WINDOWS 7 64BIT', None, '_AAT_OTHERTERMS', '_New_DK_ID', 12, 'STRING', 4, 4, None, None, 1, None)
#
# Various broken things:
#   x _Mod_History should have 1756 records but we retrieve 0
#   x _User_Groups should have 2 records but we retrieve 0
#
# TODO:
#   * Retry CopyTable if child process fails for any reason
#
# Done:
#   x Only rename fields that need to be renamed, like "Values"
#   x Command line processing
#   x Investigate os.chdir() inheritance on windows subprocesses
#   x Dump and log file rotation (delete all but X newest files)
#   x Read from config file

import datetime
import itertools
import collections
import os
import pprint
import time
import re
import sys
import subprocess
import string
import json
import traceback

import pyodbc
import sqlite3


# Work around IDLE bug
if "__file__" not in globals():
    __file__ = sys.argv[0]
#

# 4D crashes if various tables and/or columns are accessed.  We skip
# those and hope the data isn't too important.
TABLE_BLACKLIST = (
    # Error ('HY000', '[HY000] [Simba][Simba ODBC Driver]Non unique column reference: _unused. (0) (SQLExecDirectW)')
    #'_CHOICELISTDEFS',

    # Crashes
##    '_Blobs',

    # Crashes
##    '_Previews',

    # Crashes
    '_ThumbNails',

    )

COLUMN_BLACKLIST = (
    # Truncate
    ('_Arrays4Files', 'Arrays_1D'),

    # Crash in both v7 and v8
    ('_Blobs', 'theBlob'),

    # Has two columns with the same name
    ('_ChoiceListDefs', '_unused'),

    # Truncated
    ('_ChoiceListDefs', '_Parent_Value'),
    ('_ChoiceListDefs', 'ValuesData'),
    ('_ChoiceListDefs', 'CreateStamp'),

    # Illegal column name
    ('_ChoiceListDefs', 'Values'),

    # Truncates results
##    ('_FM_Fields', 'Field_Help'),

    # Truncates results
##    ('_Mod_History', 'Modifications'),

    # v9.5.1 sqlite3.InterfaceError: Error binding parameter 5 - probably unsupported type
    ('Portfolios', 'PortPict'),

    # Crash in both v7 and v8
    ('_Previews', 'Picture'),

    # 0 results
    ('_User_Groups', 'Access'),

    # 0 results
    ('_User_Groups', 'AccessFldIDs'),

    # Crash
    ('_UTILITY', 'ContainsField'),
    # Crash
    ('_UTILITY', 'PageNames'),

    # v9.5.1 sqlite3.InterfaceError: Error binding parameter 81 - probably unsupported type.
    ('_UTILITY', 'Delay')

    # Truncates results
##    ('Artist_Maker', 'Biography'),

    # Truncates results
##    ('Keywords', 'Notes'),

    # Truncates results
##    ('Objects_1', 'Info_Page_Comm'),
##    ('Objects_1', 'User_Text_1'),

    # Truncates results
##    ('Object_Notes', 'Text'),

    # pyodbc.Error: ('ODBC data type -25 is not supported.  Cannot read column WORDS.', 'HY000')
##    ('_Contains', 'Words'),
##    ('_Contains_Words', 'id_added_by_converter'),
##    ('Objects_1', '_Object_Keyword'),
##    ('Objects_1__Object_Keyword', 'id_added_by_converter'),
    )

# These columns have string fields that are too long(?) and
# cause the driver to return few or no results.
COLUMN_LIMIT_LEN = (
    ('_FM_Fields', 'Field_Help'),
    ('_Mod_History', 'Modifications'),
    ('Artist_Maker', 'Biography'),
    ('Keywords', 'Notes'),
    ('Object_Notes', 'Text'),
    ('Objects_1', 'User_Text_1'),
    ('Objects_1', 'Info_Page_Comm'),
)

# This table has rows that, if fetched, cause 4D to truncate the
# results and/or crash.  We use an alternate method to fetch what we
# can.
TABLE_FETCH_BY_KEY = {
    #'OBJECT_NOTES': '_Object_ID',
    #'OBJECTS_1': '_Objects_1_ID',
}

TABLE_SHARDING = {
    #'OBJECTS_1': 2,
}

# 4D crashes if you SELECT more than this many columns
# The actual limit is 79ish, but we are conservative here.
#_4D_MAX_SELECT_COLUMNS = 64
#_4D_MAX_SELECT_COLUMNS = 32
#_4D_MAX_SELECT_COLUMNS = 16
_4D_MAX_SELECT_COLUMNS = 4
#_4D_ENCODING = 'cp1252'
_4D_ENCODING = 'utf-8'
#_4D_DSN = 'DRIVER={4D 2004 Server 32bit Driver};SERVER=TCP/IP:EmbARK	SLICK;'
#_4D_DSN = 'DRIVER={4D 2004 Server 32bit Driver};SERVER=TCP/IP:EmbARK    localhost;'
#_4D_DSN = 'DRIVER={4D v11 ODBC Driver};SERVER=localhost;PORT=19812;UID=Administrator'
#_4D_DSN = 'DRIVER={4D v12 ODBC Driver};SERVER=localhost;PORT=19812;UID=Administrator'
_4D_DSN = 'DSN=4D;SERVER=localhost;PORT=19812;UID=Administrator'

# Return codes aren't working.  I don't know why.  So use magic strings
COPY_TABLE_SUCCESS_MAGIC = 'CopyTable Success QQZZ1'
## COPY_ALL_SUCCESS_MAGIC = 'CopyAll Success QQZZ2'

# Class used to hold schema information
ColumnSpec = collections.namedtuple('ColumnSpec', ('in_name', 'out_name', 'out_type', 'out_def', 'select_name'))

# Keep this many days of old dumps
KEEP_DAYS = 28

def DisableErrorPopup():
    """Popup blocker.

    Bleah Windows.  We spawn subprocesses but when they crash, they
    pop up a window to the user (who may not exist or be logged in),
    and halt all further processing, along with hogging file and
    database handles.  This disables the popup.
    
    From http://blogs.msdn.com/b/oldnewthing/archive/2004/07/27/198410.aspx
    
    DWORD dwMode = SetErrorMode(SEM_NOGPFAULTERRORBOX);
    SetErrorMode(dwMode | SEM_NOGPFAULTERRORBOX);
    """
    import ctypes
    # Enums from MSDN
    SEM_FAILCRITICALERRORS     = 0x0001
    SEM_NOGPFAULTERRORBOX      = 0x0002
    SEM_NOALIGNMENTFAULTEXCEPT = 0x0004
    SEM_NOOPENFILEERRORBOX     = 0x8000
    dwMode = ctypes.windll.kernel32.SetErrorMode(
        SEM_FAILCRITICALERRORS|
        SEM_NOGPFAULTERRORBOX|
        SEM_NOALIGNMENTFAULTEXCEPT|
        SEM_NOOPENFILEERRORBOX
        )
#


def Convert(type, value):
    """Convert string from cp1252 to unicode

    type: SQL typename
    value: Any value

    Returns new value
    """
#    if value is not None and type == 'TEXT':
#        return value.decode(_4D_ENCODING)
#    else:
#        return value
#    #
    # Assume already utf-8
    return value
#


def OpenEmbarkConn():
    """Open connection to Embark Server"""

    # Disable connection pooling
    pyodbc.pooling=False

    print "Opening embark connection"
    embark_conn = pyodbc.connect(_4D_DSN, autocommit=False)
    print "Opened"

    # This crashes the process intermittently so we are force to do
    # character conversion manually
    ## embark_conn.add_output_converter(pyodbc.SQL_CHAR, convert_cp1252_to_unicode)
    ## embark_conn.add_output_converter(pyodbc.SQL_LONGVARCHAR, convert_cp1252_to_unicode)
    ## embark_conn.add_output_converter(pyodbc.SQL_VARCHAR, convert_cp1252_to_unicode)

    embark_cursor = embark_conn.cursor()
    print "Cursor created"

    return embark_conn, embark_cursor
#


def CreateSQLiteFile(sqlite3_db_fn):
    """Create an SQLite database."""

    # We just open and close it.  This will check that the file is
    # writable and create an empty database.
    assert not os.path.exists(sqlite3_db_fn)
    conn, cursor = OpenSQLiteConn(sqlite3_db_fn)
    cursor.close()
    conn.commit()
    conn.close()
#


def FinalizeSQLiteFile(tmp_sqlite3_db_fn, final_sqlite3_db_fn):
    """Move an sqlite database to its permanent filename."""

    assert not os.path.exists(final_sqlite3_db_fn)
    # This isn't atomic on Windows fyi
    os.rename(tmp_sqlite3_db_fn, final_sqlite3_db_fn)
#


def OpenSQLiteConn(sqlite3_fn):
    """Open connection to sqlite database
    
    sqlite3_fn: Filename of database

    Returns (connection, cursor)
    """

    # pysqlite handles datetime.date and datetime.datetime but not datetime.time
    def adapt_time(t):
        """Convert datetime.time to ISO string format"""
        return t.strftime('%H:%M:%S')
    #
    sqlite3.register_adapter(datetime.time, adapt_time)

    print "Opening sqlite3 file"
    sqlite3_conn = sqlite3.connect(sqlite3_fn, detect_types=sqlite3.PARSE_DECLTYPES)
    sqlite3_cursor = sqlite3_conn.cursor()

    return sqlite3_conn, sqlite3_cursor
#


def GetColumnSpecs(in_cursor, in_table_name):
    """Read a table's schema from a database

    in_cursor: Cursor to the database
    in_table_name: string

    returns a list of ColumnSpec(in_name, out_name, out_type, out_def)
    """

    print "Getting columns"
    column_specs = []
    in_cursor.columns(table=in_table_name)
    for idx, row in enumerate(in_cursor):
        # Validate column names
        print row
        #for idx, (desc, val) in enumerate(zip(row.cursor_description, row)):
        #    print "[%d] %s='%s'" % (idx, desc[0], val)
        ##
        in_name = row.column_name
        out_name = in_name
        match = re.match('^[a-zA-Z_0-9 ]+$', in_name)
        assert match, row

        # Some columns cause a crash when they are SELECTed.  Skip them
        blacklisted_lowered = [(t.lower(), c.lower()) for t,c in COLUMN_BLACKLIST]
        if (in_table_name.lower(), in_name.lower()) in blacklisted_lowered:
            print "Skipping blacklisted column %s %s" % (in_table_name, in_name)
            continue
        #

        # 4D allows column names starting with digits, and column
        # names that are the same as SQL keywords, embedded
        # spaces, and who knows what else.  So mangle column
        # names as needed.
        ## out_name = '_' + out_name.replace(' ', '_')
        out_name = out_name.replace(' ', '_')
        if out_name[0] not in string.ascii_letters:
            out_name = '_' + out_name
        #

        # Handle each recognized type
        select_name = '"%s"' % in_name
        if row.type_name in ('STRING', 'TEXT', 'CLOB'):
            #assert row.column_size == row.buffer_length, { t[0]: value for (t, value) in zip(row.cursor_description, row) }
            out_type = 'TEXT'
        elif row.type_name in ('INT16', 'INT32'):
            # Avoid "ODBC data type -25 is not supported.  Cannot read column"
            # TODO Cast to some other type
            #assert row.data_type != -25, row
            out_type = 'INTEGER'
        elif row.type_name in ('INT64'):
            # Apparently the driver can't handle 64 bit ints, so we truncate
            # them all to 32 bits.  The error is
            # Avoid "ODBC data type -25 is not supported.  Cannot read column"
            #assert row.data_type == -25, row
            #select_name = 'CAST("%s" AS INT) AS "%s"' % (in_name, in_name)
            out_type = 'INTEGER'
        elif row.type_name in ('REAL',):
            assert 1 < row.buffer_length <= 8, row
            #assert row.num_prec_radix == 10, { t[0]: value for (t, value) in zip(row.cursor_description, row) }
            assert row.decimal_digits in (0, None), row
            out_type = 'REAL'
        elif row.type_name == 'BOOLEAN':
            #assert row.buffer_length == 1, row
            #assert row.num_prec_radix == 2, row
            out_type = 'INTEGER'
        elif row.type_name in ('UNKNOWN', 'BLOB'):
            out_type = 'BLOB'
        elif row.type_name == 'TIMESTAMP':
            assert row.sql_datetime_sub in (1,3), { t[0]: value for (t, value) in zip(row.cursor_description, row) } # SQL_CODE_DATE
            out_type = 'DATE'
        elif row.type_name == 'INTERVAL':
            assert row.sql_datetime_sub == 2 # SQL_CODE_TIME
            out_type = 'TIME'
        else:
            assert False, { t[0]: value for (t, value) in zip(row.cursor_description, row) }
        #

        # Pure Hack
        if (in_table_name, in_name) in COLUMN_LIMIT_LEN:
            column_max_len = 510
            select_name = '''SUBSTRING("%s", 0, %d)''' % (in_name, column_max_len)
        #
        
        # Assemble SQLite CREATE TABLE spec
        out_def = '%s %s%s' % (
            out_name, out_type, 
            ' NOT NULL' if not row.nullable else ''
            )

        column_specs.append(ColumnSpec(in_name, out_name, out_type, out_def, select_name))
    #
    return column_specs
#


def GetTableRowCount(cursor, table_name):
    """Read the number of data rows in a table

    in_cursor: Cursor to the database
    in_table_name: string

    returns integer number of columns
    """

    print "Getting row count for %s" % table_name
    # SELECT COUNT(*) doesn't work, gives ODBC error, don't know why
    select_stmt = '''SELECT CAST(COUNT(*) AS int) FROM %s''' % table_name
    print select_stmt
    time.sleep(.01) # Let Embark/4D settle a little

    cursor.execute(select_stmt)
    #rows = cursor.fetchall()
    #row_count = rows[0][0]
    #print rows
    row = cursor.fetchone()
    row_count = row[0]
    # 4D v11 ODBC returns None instead of 0 for empty tables
    if row_count is None:
        row_count = 0
    #
    print "Row count is %d" % row_count
    return row_count
#

def WriteTable(out_conn, out_cursor, out_table_name, column_specs,
               out_data, shard, num_shards):
    """Create a table and write a list of rows to it.

    out_conn: Connection to destination database
    out_cursor: Open cursor to destination
    out_table_name: string
    column_specs: As per GetColumnSpecs
    out_data: List of rows, each row is a list of column values
    """

    # ... create table
    if shard == 0:
        create_table_defs = ',\n    '.join([c.out_def for c in column_specs])
        create_table_stmt = '''CREATE TABLE %s (\n    %s\n)''' % (
            out_table_name, create_table_defs)
        print create_table_stmt

        # Create table at destination
        print "Creating table %s" % out_table_name
        out_cursor.execute(create_table_stmt)
        #print out_cursor.fetchall()
    #

    # assemble insert statement
    insert_names = ', '.join([c.out_name for c in column_specs])
    insert_values = ', '.join(['?'] * len(column_specs))
    insert_stmt = '''INSERT INTO %s (%s) VALUES (%s)''' % (
        out_table_name, insert_names, insert_values)
    print insert_stmt

    # Insert data into destination
    print "Inserting data (%d rows)" % len(out_data)
    out_cursor.executemany(insert_stmt, out_data)
    #print out_cursor.fetchall()

    # Commit
    out_conn.commit()
    print "committed"
#


def ReadTableData(in_cursor, in_table_name, column_specs, expected_row_count):
    """Read all the data in a table and return a list of rows.

    Returns a list of rows, each row is a list of column values.
    """

    select_stmts = AssembleSelects(in_table_name, column_specs)
    data_sets = RunSelects(in_cursor, select_stmts, remove_last_field=True, 
                           expected_row_count=expected_row_count)
    out_data = StitchData(data_sets, column_specs)

    return out_data
#


def AssembleSelects(in_table_name, column_specs, max_columns=None):
    """Generate a list of select statements.

    The 4D ODBC driver crashes if we access too many columns.
    So we have to assemble multiple select statements and hope
    the database doesn't change underneath us.

    The driver doesn't return rows if all the values as null,
    so we add ", 1" to the list of columns returned for
    each select so that there is at least one non-null value
    per row.  The CAST() is required to avoid an ODBC error.
    """
    if max_columns is None:
        max_columns = _4D_MAX_SELECT_COLUMNS
    select_stmts = []
    num_selects = ((len(column_specs)-1) // max_columns) + 1
    assert num_selects > 0, column_specs
    for select_idx in range(num_selects):
        start = select_idx * max_columns
        stop = start + max_columns
        select_column_specs = column_specs[start:stop]

        select_defs = ', '.join([c.select_name 
                                 for c in select_column_specs])
        select_stmt = '''SELECT %s , CAST(1 AS int) FROM "%s"''' % (
            select_defs, in_table_name)
        select_stmts.append((select_stmt, select_column_specs))
    #
    print "%d select statements:" % len(select_stmts)
    print select_stmts
    return select_stmts
#


def RunSelects(in_cursor, select_stmts, args=[], quiet=False, remove_last_field=True, expected_row_count=None):
    """Run a series of select statements.

    The statements are assumed (hoped, really) to return different
    columns of the same rows in the same row order.

    Returns a list of the result of each select statement.
    """
    data_sets = []
    for select_stmt, select_column_specs in select_stmts:
        if not quiet:
            print "Running %s" % select_stmt
        #
        sys.stdout.flush()
        time.sleep(.01) # Let Embark/4D settle a little

        in_cursor.execute(select_stmt, *args)
        if 0:
            # This doesn't work because the character encoding crashes
            data = in_cursor.fetchall()
        else:
            data = []
            for row_idx, row in enumerate(in_cursor):
                # Print progress
                if row_idx % 10 == 0:
                    if not quiet:
                        print "Row %d" % row_idx
                    #
                #

                # Character encoding conversion
                #types = [c.out_type for c in select_column_specs]
                #converted_row = map(Convert, types, row)
                converted_row = list(row)
                if remove_last_field:
                    converted_row = converted_row[:-1]
                #
                assert len(converted_row) == len(select_column_specs), (
                    len(converted_row), len(select_column_specs))
                data.append(converted_row)
            #
        #
        if not quiet:
            print "Returned %d partial rows" % len(data)
        #
        if expected_row_count is not None:
            assert len(data) == expected_row_count, (
                len(data), expected_row_count, select_stmt)
        #
        data_sets.append(data)
    #

    return data_sets
#


def ReadTableDataByKey(in_cursor, in_table_name, column_specs,
                       shard, num_shards):
    """For whatever reason, 4D just doesn't return all the rows for
    some tables.  So we fetch a list of all the key values (hoping
    the list is complete), then fetch each row individually.

    Except, the table doesn't always have a unique primary key.  So we
    use a non-unique key that may fetch more than one row.

    Returns a list of rows, each row is a list of column values.
    """
    
    key_name = TABLE_FETCH_BY_KEY[in_table_name]

    # Get complete (hopefully) list of keys
    key_select = '''SELECT "%s" FROM "%s"''' % (
        key_name, in_table_name)
    key_values = []
    for row in in_cursor.execute(key_select):
        assert len(row) == 1, (key_name, row)
        key_value = row[0]
        if key_value not in key_values:
            key_values.append(key_value)
        #
    #
    print "Found %d keys" % len(key_values)

    select_stmts = AssembleSelects(in_table_name, column_specs, max_columns=1000)

    # Add a where clause and run each select once per unique key value
    sorted_key_values = sorted(key_values)
    active_key_values = key_values[shard::num_shards]
    all_rows = []
    for key_value in active_key_values:
        where = ' WHERE "%s"=?' % key_name
        new_select_stmts = [(stmt + where, specs)
                            for stmt, specs in select_stmts]

        try:
            # Fetch data from source
            data_sets = RunSelects(in_cursor, new_select_stmts, 
                                   args=[key_value], quiet=True,
                                   remove_last_field=True,
                                   expected_row_count=None)

            # Look for bad rows
            bad = False
            if len(data_sets[0]) == 0:
                bad = True
            #
            for set_idx in range(len(data_sets)):
                if len(data_sets[set_idx]) != len(data_sets[0]):
                    bad = True
                    break
                #
            #
            if bad:
                print "Skipping bad row with key %s: %s" % (key_value, data_sets)
                continue
            #

            this_rows = StitchData(data_sets, column_specs)
            assert len(this_rows) >= 1, (data_sets, this_rows, key_name, key_value)
            all_rows.extend(this_rows)
        except pyodbc.Error, e:
            print "Exception raised while running selects for key '%s'" % key_value
            print str(e)
            traceback.print_exc()
        #
    #

    return all_rows
#


def StitchData(data_sets, column_specs):
    """Merge different columns together into a single set of rows.

    We might have to fetch a table multiple times, fetching only a
    subset of the columns each time.  This merges the data together
    into a single set of rows with all columns.

    E.g. 
       data_sets = [
       [
       [ 1,  2,  3],
       [11, 12, 13],
       ], 
       [
       [ 4,  5],
       [14, 15],
       ]
       ]
       Returns [
          [ 1,  2,  3,  4,  5],
          [11, 12, 13, 14, 15]
          ]
    """
    # Each select should return the same number of rows
    for set_idx in range(len(data_sets)):
        assert len(data_sets[set_idx]) == len(data_sets[0]), (set_idx, len(data_sets[set_idx]), len(data_sets[0]))
    #

    # Stitch data from different statements together.  First rotate
    # data 90 degrees so it's a list of rows, each row is a list of
    # lists
    flipped_data = zip(*data_sets)

    # Flatten each row from list of list to just list of values
    out_data = [list(itertools.chain(*row)) for row in flipped_data]

    # Sanity check
    assert len(out_data) == len(data_sets[0])
    for row_idx in range(len(out_data)):
        assert len(out_data[row_idx]) == len(column_specs)
    #

    return out_data
#

assert StitchData([
        [
        [ 1,  2,  3],
        [11, 12, 13],
        ],
        [
        [ 4,  5],
        [14, 15],
        ]
        ], [0]*5) == [
    [ 1,  2,  3,  4,  5],
    [11, 12, 13, 14, 15]
    ]


def CopyTableWithConns(in_conn, in_cursor, out_conn, out_cursor, 
                       in_table_name, shard, num_shards):
    """Copy the schema and contents of an SQL table from one db to another

    in_conn: Connection to source database
    in_cursor: Open cursor to source
    out_conn: Connection to destination database
    out_cursor: Open cursor to destination
    in_table_name: As from pyodbc.Cursor.tables()
    """

    # Validate table names
    match = re.match('^[a-zA-Z_][a-zA-Z_0-9]*$', in_table_name)
    assert match, in_table_name
    out_table_name = in_table_name

    # Get columns of this table
    column_specs = GetColumnSpecs(in_cursor, in_table_name)

    # Get number of rows in this table
    expected_row_count = GetTableRowCount(in_cursor, in_table_name)

    # Read data
    if in_table_name in TABLE_FETCH_BY_KEY:
        print "Fetching table %s by key" % in_table_name
        out_data = ReadTableDataByKey(in_cursor, in_table_name,
                                      column_specs, shard, num_shards)
    else:
        out_data = ReadTableData(in_cursor, in_table_name, column_specs,
                                 expected_row_count)
        # Check that table is not truncated
        assert len(out_data) == expected_row_count, (len(out_data), expected_row_count)
    #

    # Write data
    WriteTable(out_conn, out_cursor, out_table_name, column_specs,
               out_data, shard, num_shards)

    print COPY_TABLE_SUCCESS_MAGIC
#


def CopyAll(tmp_sqlite3_db_fn, final_sqlite3_db_fn):
    """Copy an entire database from one connection to another."""

    print "Starting CopyAll at %s" % time.asctime()

    embark_conn, embark_cursor = OpenEmbarkConn()

    # Get list of tables in source
    try:
        table_names = []
        for row in embark_cursor.tables():
            table_names.append(row.table_name)
        #
    finally:
        embark_conn.close()
        embark_conn = None
    #
    print "Found %d tables in source" % len(table_names)
    table_names.sort()
        
    # Create sqlite3 destination
    CreateSQLiteFile(tmp_sqlite3_db_fn)

    # Copy each table
    errors = []
    for table_name in table_names:
        if table_name in TABLE_BLACKLIST:
            print "Skipping blacklisted table %s" % table_name
            continue
        #

        num_shards = TABLE_SHARDING.get(table_name, 1)
        for shard in range(num_shards):
            error = SpawnCopyTable(table_name, tmp_sqlite3_db_fn,
                                   shard, num_shards)
            if error:
                print "Doh! (%s)" % table_name
                print error
                errors.append((table_name, error))
                break
            #
        #
    #

    if errors:
        print "CopyAll had %d errors:\n%s" % (len(errors), errors)
        # Leave the sqlite database under the temporary name to
        # indicate errors.
    else:
        print "No errors in CopyAll."
        FinalizeSQLiteFile(tmp_sqlite3_db_fn, final_sqlite3_db_fn)
    #

    print "Finished CopyAll at %s" % time.asctime()
#


def CopyTable(table_name, sqlite3_fn, shard, num_shards):
    """Open connections and copy a single table from Embark to sqlite"""
    print "Enter CopyTable(%s)" % table_name
    embark_conn, embark_cursor = OpenEmbarkConn()
    try:
        sqlite3_conn, sqlite3_cursor = OpenSQLiteConn(sqlite3_fn)
        try:
            CopyTableWithConns(embark_conn, embark_cursor,
                               sqlite3_conn, sqlite3_cursor, table_name,
                               shard, num_shards)
        finally:
            sqlite3_conn.close()
            sqlite3_conn = None
        #
    finally:
        embark_conn.close()
        embark_conn = None
    #
    print "Exit CopyTable(%s)" % table_name
#
        

def SpawnCopyTable(table_name, sqlite3_fn, shard, num_shards):
    """Spawn a child process to copy a single database table.

    We don't use the process exit code because it doesn't seem to be
    set reliably on Windows.  Instead we print and look for magic
    strings to indicate success or failure.
    """

    print "Spawning CopyTable(%s)" % table_name
    time.sleep(.1)
    sys.stdout.flush()
    #this_file = "DumpEmbarkDatabaseVia4DODBC.py"
    this_file = sys.argv[0]
    #args = "python.exe %s copytable %s %s" % (this_file, table_name, sqlite3_fn)
    args = ("python.exe", this_file, "copytable", table_name, sqlite3_fn,
            str(shard), str(num_shards))
    stdoutdata = None
    stderrdata = None
    popen = subprocess.Popen(args, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE, 
                             universal_newlines=True)
    stdoutdata, stderrdata = popen.communicate()
    sys.stdout.flush()
    if stdoutdata:
        print "== Child stdout =="
        print stdoutdata,
        print "== End Child stdout =="
    #
    if stderrdata:
        print "== Child stderr =="
        print stderrdata,
        print "== End Child stderr =="
    #
    returncode = popen.returncode
    #returncode = subprocess.call(args)
    #print "returncode=%d" % returncode # This seems like a random number

    if stderrdata:
        return stderrdata
    #

    if not COPY_TABLE_SUCCESS_MAGIC in stdoutdata:
        return "Didn't see success marker"
    #

    return None # Success
#


def FindUnusedFilenames(output_dir, output_root_name):
    """Decide which filename to use for output and log files."""

    # Start with date based filename
    today = datetime.date.today()
    base_fn = os.path.join(output_dir, output_root_name)
    base_fn += '_' + today.strftime('%Y-%m-%d')

    # Possibly append .1, .2, ... to get a unique name
    exts = ['.sqlite.tmp', '.sqlite', '.log']
    suffix = 0
    while suffix < 1000:
        suffix_str = ('.%d' % suffix) if suffix > 0 else ''
        fn = base_fn + suffix_str
        for ext in exts:
            if os.path.exists(fn + ext):
                suffix += 1
                break # Try another higher suffix
            #
        else:
            break # This suffix works
    else:
        raise AssertionError("Too many dump files, exiting.")
    #
    assert fn

    final_sqlite3_db_fn = fn + '.sqlite'
    tmp_sqlite3_db_fn = fn + '.sqlite.tmp'
    log_fn = fn + '.log'

    return (tmp_sqlite3_db_fn, final_sqlite3_db_fn, log_fn)
#


def CleanupOldDumps(output_dir, output_root_name):
    """Delete old dump files.

    Keep last N days, as well as the first dump of each month,
    as well as the very first and last dumps.
    """

    # Get a list of all dumps
    tmp_list = [] # List of filenames
    dump_list = [] # List of (filename, mtime)
    for fn in os.listdir(output_dir):
        if fn.endswith('.sqlite.tmp'):
            # Always delete tmp files
            tmp_list.append(fn)
        elif (fn.endswith('.sqlite') and
              fn.startswith(output_root_name + '_')):
            # Get last modified time
            fn = os.path.join(output_dir, fn)
            mtime = os.stat(fn).st_mtime
            #print mtime
            dump_list.append((fn, mtime))
        #
    #

    # If no dumps found, something is wrong.
    print "Found %d dump files" % len(dump_list)
    assert dump_list

    # Sort from oldest to newest
    dump_list.sort(lambda x, y: cmp(x[1],y[1]) or cmp(x[0],y[0]))

    # Get age of newest (should be seconds old)
    newest_mtime = dump_list[-1][1]
    print "Newest dump is %s" % dump_list[-1][0]

    # Keep track of which months we've seen a dump for
    months_seen = set() # Set of (year, month)

    # Decide which to delete
    del_list = [] # List of dumps to delete
    for fn, mtime in dump_list[1:-1]: # Ignore newest and oldest
        #print fn
        #print mtime
        # Find age in days
        age = newest_mtime - mtime
        delta = datetime.timedelta(seconds=age)
        assert delta.total_seconds() >= 0
        print "Age of %s is %s" % (fn, delta)
        #print delta.days
        # Old?
        if delta.days > KEEP_DAYS:
            # Have we seen a dump for this month?
            dt = datetime.datetime.fromtimestamp(mtime)
            key = (dt.year, dt.month)
            if key in months_seen:
                del_list.append(fn)
            else:
                months_seen.add(key)
            #
        #
    #

    keep_count = len(dump_list) - len(del_list)
    assert keep_count > 0
    print "Cleaning up %d tmp files and %d old dumps, keeping %d" % (
        len(tmp_list), len(del_list), keep_count)
    #print tmp_list
    #print del_list
    #print dump_list
    for fn in tmp_list: # fn is relative
        print "Deleting %s" % fn
        #os.remove(fn)
        os.rename(os.path.join(output_dir, fn),
                  os.path.join(output_dir, 'old', fn))
        pass
    #
    for fn in del_list: # fn is absolute
        print "Deleting %s" % fn
        #os.remove(fn)
        old_fn = os.path.join(output_dir, 'old', os.path.basename(fn))
        os.rename(fn, old_fn)
        pass
    #
#           


def usage():
    msg = """\
Usage: %s [copytable <tablename> <sqlite_filename>]\
""" % sys.argv[0]
    print >> sys.stderr, msg
    sys.exit(1)
#


def main():
    if len(sys.argv) == 1: # CopyAll
        # Read config file (in JSON format)
        config_dir = os.path.dirname(__file__) or os.getcwd()
        config_fn = os.path.join(config_dir, "EmbarkDBDump.conf")
        with open(config_fn, 'rb') as config_f:
            config = json.load(config_f)
        #
        output_dir = config.get("OUTPUT_DIR", os.getcwd())
        assert output_dir
        output_root_name = config.get("OUTPUT_ROOT_NAME", 'embark_dump')
        assert output_root_name

        # Validate config options
        #print "Output dir is %s" % output_dir
        if not os.path.isdir(output_dir):
            raise AssertionError("Not a directory: %s" % output_dir)
        #
        
        tmp_sqlite3_db_fn, final_sqlite3_db_fn, log_fn = FindUnusedFilenames(
            output_dir, output_root_name)

        # Redirect stdout, stderr to log file
        log_f = open(log_fn, 'wb+')
        sys.stdout = log_f
        sys.stderr = log_f

        CopyAll(tmp_sqlite3_db_fn, final_sqlite3_db_fn)

        CleanupOldDumps(output_dir, output_root_name)
    elif len(sys.argv) == 6 and sys.argv[1] == 'copytable':
        tablename = sys.argv[2]
        sqlite3_db_fn = sys.argv[3]
        shard = int(sys.argv[4], 10)
        num_shards = int(sys.argv[5], 10)
        CopyTable(tablename, sqlite3_db_fn, shard, num_shards)
    else:
        usage()
    #
#

# Random test code
if 0:
    embark_conn, embark_cursor = OpenEmbarkConn()
    s = '''
SELECT "_Object_ID", "Field_Name", "Text", "Web_Access", "Mod_Date", "Mod_Time", "Mod_User", "Record_Date", "Record_Time", "Record_User", "_Not_Used7", "_Not_Used8", "_Not_Used9", "_Not_Used10", "_Not_Used11" FROM "OBJECT_NOTES" WHERE "_Object_ID"<>5222 AND "_Object_ID"<>509 AND "_Object_ID"<>510 AND "_Object_ID"<>511
'''

    s = '''SELECT * FROM "_User_Groups"'''
    s = '''SELECT "_unused5", "_unused6" FROM "_User_Groups"'''
    s = '''SELECT "_Group_ID", "Name", "Menus_Pg4" FROM "_User_Groups"'''
    s = '''SELECT "AccessFldIDs" FROM "_User_Groups"'''
    s = '''SELECT "_Object_Keyword" FROM "Objects_1"'''
    #s = '''SELECT "_Width", "_Depth", "Duration", "Info_Page_Comm" FROM "Objects_1"'''
    #s = '''SELECT "_Width", "_Depth", "Duration" FROM "Objects_1"'''
    s = '''SELECT "User_Num_2", "User_Num_3", "InActive", "User_Text_1" FROM "Objects_1"'''
    s = '''SELECT "User_Text_1", "_AccNumSort1", "_AccNumSort2", "Artist_Dates" , CAST(1 AS int) FROM "Objects_1"'''
    s = '''SELECT SUBSTRING("User_Text_1", 0, 510) FROM Objects_1'''
    embark_cursor.execute(s)
    #print len(embark_cursor.fetchall())
    #stopstop
    for row_idx, row in enumerate(embark_cursor.getTypeInfo()):
        print "%03d %s" % (row_idx, row)
    embark_cursor.getTypeInfo()
    for row_idx, row in enumerate(embark_cursor.description):
        print "%03d %s" % (row_idx, row)
    #for row_idx, row in enumerate(embark_cursor.tables()):
    #for row_idx, row in enumerate(embark_cursor.columns()):
    #for row_idx, row in enumerate(embark_cursor.execute(s)):
        print "%03d %s" % (row_idx, row)
        #print row_idx
    #print "Found %d rows" % (embark_cursor.rowcount)
    stopstop
#

if __name__ == '__main__':
    DisableErrorPopup()
    main()
#
