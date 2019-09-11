import sqlite3
import json

conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

#Basic setup
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT UNIQUE
);

CREATE TABLE Course (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE
);

CREATE TABLE Member (
    course_id INTEGER,
    user_id INTEGER,
    role INTEGER,
    PRIMARY KEY(user_id, course_id)
)

''')

fname = input("Input file name: ")
if (len(fname) < 1 ):
    fname = 'roster_data_sample.json'



str_data = open(fname).read()
#print(str_data)
#print("That was str_data, here's json_data:")
json_data = json.loads(str_data)
#print(json_data)

for entry in json_data:

    name = entry[0]
    title = entry[1]

    print((name, title))

    cur.execute('INSERT OR IGNORE INTO User(name) VALUES ( ? )', (name, ))
    cur.execute('SELECT id FROM User WHERE name = ? ', (name, ))
    user_id = cur.fetchone()[0]

    cur.execute('INSERT OR IGNORE INTO Course(title) VALUES ( ? )', (title, ))
    cur.execute('SELECT id FROM Course WHERE title = ? ', (title, ))
    course_id = cur.fetchone()[0]

    cur.execute('INSERT OR REPLACE INTO Member (user_id, course_id) VALUES (?, ?)', (user_id, course_id))

    conn.commit()
