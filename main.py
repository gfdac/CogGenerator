# /*[[[cog

# !/usr/bin/env python

import pymysql.cursors
import json, ast, sys, re


def converte(type):
    regex = re.compile('int')
    inteiro = regex.findall(type)

    regex = re.compile('double')
    duplo = regex.findall(type)

    regex = re.compile('float')
    floater = regex.findall(type)

    regex = re.compile('decimal')
    decimal = regex.findall(type)

    regex = re.compile('varchar')
    string = regex.findall(type)

    regex = re.compile('text')
    texto = regex.findall(type)

    if inteiro:
        return "int"
    if string:
        # if type == "varchar(255)":
        return "string"
    if texto:
        return "string"
    if duplo:
        return "double"
    if floater:
        return "float"
    if decimal:
        return "float"

    return type


# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             db='exchange',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

#
# try:
#     with connection.cursor() as cursor:
#
#
#
#         # Read a single record
#         sql = "SHOW COLUMNS FROM CompraVenda"
#         # sql = "SELECT `ID`, `Nome` FROM `Usuario` WHERE `ID`>%s"
#         cursor.execute(sql)
#         # cursor.execute(sql, ('0',))
#         # result = cursor.fetchone()
#         # result = cursor.fetchall()
#         # my_list = [str(result[x]) for x in range(len(result))]
#
#         while True:
#             row = cursor.fetchone()
#             if row == None:
#                 break
#
#             # json.dump(row, sys.stdout)
#
#
#             # cog.out("""
#             #
#             # /*
#             #     Campo %s
#             # */
#             # """ % row['Type'], dedent=True, trimblanklines=True)
#
#
#
#             cog.outl("")
#
#             cog.outl("/*")
#
#             cog.outl("Attributo %s" % row['Field'])
#             cog.outl("Tipo %s" % row['Type'])
#
#             for k, v in row.items():
#                 # print(k, 'corresponds to', v)
#                 cog.outl(unicode(k) + " = " + unicode(v))
#
#             cog.outl("*/")
#
#             # "Extra": "", "Default": null, "Field": "Status", "Key": "", "Null": "YES", "Type": "int(11)"
#
#             cog.outl("public " + converte(row['Type']) + " get%s();" % row['Field'])
#             cog.outl("public void set" + row['Field'] + "(" + converte(row['Type']) + ");")
#
#
#
#             # print map(lambda x: x.encode('ascii'), my_list)
#             # print [x.encode('ascii') for x in my_list]
#             # print type(my_list)(x.encode('ascii') for x in my_list)
#
#
# finally:
#     connection.close()
#
#
#


try:
    with connection.cursor() as cursortabela:




        # Read a single record
        sql = "SHOW TABLES FROM exchange"
        # sql = "SELECT `ID`, `Nome` FROM `Usuario` WHERE `ID`>%s"
        cursortabela.execute(sql)
        # cursor.execute(sql, ('0',))
        # result = cursor.fetchone()
        # result = cursor.fetchall()
        # my_list = [str(result[x]) for x in range(len(result))]

        while True:
            tabela = cursortabela.fetchone()
            if tabela == None:
                break

            # json.dump(row, sys.stdout)

            print(tabela['Tables_in_exchange'])


            for k, v in tabela.items():
                # print(k, 'corresponds to', v)
                # cog.outl(unicode(k) + " = " + unicode(v))
                # Read a single record
                sql = "SHOW COLUMNS FROM %s" %v
                # sql = "SELECT `ID`, `Nome` FROM `Usuario` WHERE `ID`>%s"

                try:
                    with connection.cursor() as cursor:
                        cursor.execute(sql)
                        # cursor.execute(sql, ('0',))
                        # result = cursor.fetchone()
                        # result = cursor.fetchall()
                        # my_list = [str(result[x]) for x in range(len(result))]

                        cog.out("""

                        /*
                            --------------------------------------------------------------
                            Tabela %s
                            --------------------------------------------------------------
                        */
                        """ % v, dedent=True, trimblanklines=True)


                        while True:
                            row = cursor.fetchone()
                            if row == None:
                                break

                            # json.dump(row, sys.stdout)


                            # cog.out("""
                            #
                            # /*
                            #     Campo %s
                            # */
                            # """ % row['Type'], dedent=True, trimblanklines=True)



                            cog.outl("")

                            cog.outl("/*")

                            cog.outl("Attributo %s" % row['Field'])
                            cog.outl("Tipo %s" % row['Type'])

                            for k, v in row.items():
                                # print(k, 'corresponds to', v)
                                cog.outl(unicode(k) + " = " + unicode(v))

                            cog.outl("*/")

                            # "Extra": "", "Default": null, "Field": "Status", "Key": "", "Null": "YES", "Type": "int(11)"

                            cog.outl("public " + converte(row['Type']) + " get%s();" % row['Field'])
                            cog.outl("public void set" + row['Field'] + "(" + converte(row['Type']) + ");")

                finally:
                    print("final")
                    #connection.close()




                # cog.out("""
            #
            # /*
            #     Campo %s
            # */
            # """ % row['Type'], dedent=True, trimblanklines=True)



            # cog.outl("")
            #
            # cog.outl("/*")
            #
            # cog.outl("Attributo %s" % row['Tables_in_exchange'])
            #
            # for k, v in row.items():
            #     # print(k, 'corresponds to', v)
            #     cog.outl(unicode(k) + " = " + unicode(v))
            #
            # cog.outl("*/")
            #
            # # "Extra": "", "Default": null, "Field": "Status", "Key": "", "Null": "YES", "Type": "int(11)"
            #
            # cog.outl("public " + converte(row['Tables_in_exchange']) + " get%s();" % row['Tables_in_exchange'])



            # print map(lambda x: x.encode('ascii'), my_list)
            # print [x.encode('ascii') for x in my_list]
            # print type(my_list)(x.encode('ascii') for x in my_list)


finally:
    connection.close()

# ]]]*/
# //[[[end]]]
