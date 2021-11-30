import sqlite3
def testTask2():
 con = sqlite3.connect('sqlite/Countries.db')
 cur = con.cursor()
 assert len(list(cur.execute("SELECT * FROM Countries WHERE Population/Area < 50 AND Country !='USA'")))==0 and len(list(cur.execute("SELECT * FROM Countries WHERE Population/Area < 50 AND Country =='USA'")))!=0
