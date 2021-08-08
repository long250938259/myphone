import pymysql

# try:
con = pymysql.connect(host="192.168.174.128", user="root", password="123456", db="mydatabase", port=3306)
cursorl = con.cursor()
sql = "INSERT INTO test_you (name, phone) VALUES ('陈荟萃', '18281741826')"
cursorl.execute(sql)
con.commit()
