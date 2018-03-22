import threading
import MySQLdb
import sys
import random

def run_insert(db):
    """thread worker function"""
    cnx = db.cursor()
    #10 inserts per connection 
    sql="""INSERT INTO .. """
    for i in range(11):
        try:
            cnx.execute(sql)
            db.commit()
        except MySQLdb.Error, e:
            print "insert failed - Error %d: %s" % (e.args[0],e.args[1])



def init_thread():
    backgrounds=[]
    for db in connections:
        t=threading.Thread(target=run_insert(db))
        backgrounds.append(t)
        t.start()

def cleanup(connections):
    print 1
    for db in connections:
        db.close()


def main():
    try:
        init_thread()
    except:
        print "failed to initialize thread"
    sys.exit(0)

if __name__=="__main__":
    mysql_host=""
    mysql_pass=""
    mysql_user=""
    mysql_port=3306
    mysql_db="information_schema"
    THREADS=250

    #Launch 250 connections 
    connections=[]
    for thread in range(THREADS):
        try:
            mysql_db="db_"+str(random.randint(1,1500))
            connection=MySQLdb.connect(host=mysql_host,user=mysql_user,passwd=mysql_pass,db=mysql_db,port=mysql_port)
            connection.autcommit=True
            connections.append(connection)
        except MySQLdb.Error, e:
            print "Error %d: %s" % (e.args[0],e.args[1])
            sys.exit(1)
    main()
    cleanup(connections)
