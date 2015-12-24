import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()
# cursor.execute('CREATE TABLE user (id VARCHAR(20) PRIMARY KEY, name VARCHAR(20))')
# cursor.execute('INSERT INTO user (id, name) VALUES (\'1\', \'Chen\')')
# print('count changed %d' % cursor.rowcount)
cursor.execute('SELECT * FROM user')
values = cursor.fetchall()
print(values)
cursor.close()
# conn.commit()
conn.close()
