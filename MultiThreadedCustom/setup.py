import MySQLdb
import sys

mysql_host=<hostname>
mysql_pass=<user>
mysql_user=<password>
mysql_port="3306"
mysql_db="information_schema"

db = MySQLdb.connect(host=mysql_host, user=mysql_user, passwd=mysql_pass, db=mysql_db)
cur = db.cursor()

#Creates 1500 databases, each have a table db_segments
for i in range(1,1501):
    try:
        sql="CREATE DATABASE IF NOT EXISTS db_"+str(i)
        print "Creating database db_"+str(i)
        cur.execute(sql)
        print "Creating table db_" + str(i)+".segments"
        sql="""CREATE TABLE sql here """
        cur.execute(sql)
    except MySQLdb.Error, e:
        print "Error %d: %s" % (e.args[0],e.args[1])
        sys.exit(1)
