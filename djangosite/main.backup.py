import pymysql

try:
    conn = pymysql.connect(host='localhost', port=3307, user='root', password='Technology30#', database='meteringdatabase', auth_plugin='mysql_native_password')
    c = conn.cursor()
    print('connection successful')

except:
    print('not connected')
