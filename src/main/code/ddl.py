import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)),'config'))
import connection

import os.path

class dbconn:
    def __init__(self):
        """Connection with the database is established and the functions for table creation are invoked"""
        try:
            l_tables=['STUDENT_REFERENCE','placement_details','staff_details','calender_details','department_details','payment_details','degree','course_details','exam_details','grade_details','FactAcademics','FactAttendence','FactPayment','FactPlacement','FactStudent']
            mydb = connection.con()
            mycursor = mydb.cursor()
            del sys.path[:]
            for i in l_tables:
                sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'files', 'DDL', i + '.sql'))
            self.tablescreation(mydb,mycursor)
            del sys.path[:]
            for i in l_tables:
                sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'files', 'RECORDS', i + '.csv'))
            table_dict = dict(zip(l_tables, sys.path))
            self.tablesinsertion(mydb,mycursor,table_dict)
        except Exception as e:
            print(e)

    def tablescreation(self,mydb,mycursor):
        """TABLE CREATION"""
        try:
            for file_path in sys.path:
                sqlfile = open(file_path, 'r')
                sqlfile = sqlfile.read()
                command = sqlfile.split(';')[0]
                mycursor.execute(command)
                mydb.commit()
        except Exception as e:
            print(e)

    def tablesinsertion(self,mydb,mycursor,table_dict):
        try:
            for table_name, file_path in table_dict.items():
                with open(file_path, 'r') as read_file:
                    data = read_file.readlines()
                for row in data:
                    query = "INSERT INTO " + table_name + " VALUES " + "(" + row + ")"
                    mycursor.execute(query)
                    mydb.commit()

        except Exception as e:
            print(e)
bj=dbconn()