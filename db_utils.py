import sqlite3

conn = sqlite3.connect("demodb.db")
c = conn.cursor()
c.execute(''' 
create table if not exists user(
          id integer primary key not null ,
          name text not null
          )

''')
conn.commit()
conn.close()

