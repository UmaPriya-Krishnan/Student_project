import mysql.connector
import sys,os.path
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)),'config'))
import devconfig

def con():
    obj=devconfig.DevConfig()
    host, user, pwd, db = obj.connect_db("dev")
    mydb = mysql.connector.connect(host=host, user=user, password=pwd, database=db)
    #print(host, user, pwd, db)
    return mydb
con()