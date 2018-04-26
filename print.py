# !/usr/bin/env python
import pymysql.cursors
import json, ast, sys


def PrintFields(database, table):
    """ Connects to the table specified by the user and prints out its fields in HTML format used by Ben's wiki. """
    host = 'localhost'
    user = 'user'
    password = 'password'
    conn = pymysql.connect(host='localhost',
                           user='root',
                           password='root',
                           db=database,
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)

    mysql = conn.cursor()
    sql = """ SHOW COLUMNS FROM %s """ % table
    mysql.execute(sql)
    fields = mysql.fetchall()
    print '<table border="0"><tr><th>order</th><th>name</th><th>type</th><th>description</th></tr>'
    print '<tbody>'
    counter = 0
    for field in fields:
        counter = counter + 1
        # print(field)
        # json.dump(field, sys.stdout)
        name = field['Field']
        type = field['Type']
        print '<tr><td>' + str(counter) + '</td><td>' + name + '</td><td>' + type + '</td><td></td></tr>'
    print '</tbody>'
    print '</table>'
    mysql.close()
    conn.close()


users_database = sys.argv[1]
users_table = sys.argv[2]
print "Wikified HTML for " + users_database + "." + users_table
print "========================"
PrintFields(users_database, users_table)