import sqlite3


def create(cursor):
    cursor.execute("DROP TABLE IF EXISTS users")
    cursor.execute("""CREATE TABLE users (username, password, phone_email, year_of_birth, sex, disability, 
    doctor_email, family_email)""")
    cursor.execute("DROP TABLE IF EXISTS results")
    cursor.execute("""CREATE TABLE results (username, phone_email, date, result)""")


def insert(cursor):
    cursor.execute('INSERT INTO users VALUES(?,?,?,?,?,?,?,?)', ('Grażyna', 'password', 'grazyna@gmail.com', 1950, 'K', 1,
                                                               'mojneurolog@gmail.com', 'ukochanywnuczek@gmail.com'))
    results = [('Grażyna', 'grazyna@gmail.com', '2019-01-12', 12), ('Grażyna', 'grazyna@gmail.com', '2019-02-12', 17),
               ('Grażyna', 'grazyna@gmail.com', '2019-03-12', 25), ('Grażyna', 'grazyna@gmail.com', '2019-04-12', 18),
               ('Grażyna', 'grazyna@gmail.com', '2019-05-12', 23)]
    cursor.executemany('INSERT INTO results VALUES(?,?,?,?)', results)


def select(cursor):
    sql = "SELECT * FROM users"
    recs = cursor.execute(sql)
    for row in recs:
        print(row)

    sql = "SELECT * FROM results"
    recs = cursor.execute(sql)
    for row in recs:
        print(row)


db_path = './sqlite/app_database.db'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()
create(cursor)
insert(cursor)
conn.commit()
select(cursor)
cursor.close()
