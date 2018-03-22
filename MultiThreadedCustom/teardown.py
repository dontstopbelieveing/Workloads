import MySQLdb
import sys

mysql_host=""
mysql_pass=""
mysql_user=""
mysql_port="3306"
mysql_db="information_schema"

db=MySQLdb.connect(host=mysql_host,user=mysql_user,passwd=mysql_pass,db=mysql_db)
cur=db.cursor()

for i in range(1,1501):
    try:
        sql="DROP DATABASE IF EXISTS db_"+str(i)
        cur.execute(sql)
    except MySQLdb.Error, e:
        print "Error %d: %s" % (e.args[0],e.args[1])
        sys.exit(1)
