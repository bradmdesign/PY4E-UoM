import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (email TEXT, count INTEGER)')

fname = input('Enter File Name: ')
if (len(fname)<1): 
    fname = 'mbox-short.txt'

fh = open(fname)

for line in fh:
    if not line.startswith('From: '):  #This is a great line of code, remember it. If it doesn't start with this, skip it.
        continue
    pieces = line.split()
    email=pieces[1]
    cur.execute('SELECT count FROM Counts WHERE email = ?', (email,))
    row = cur.fetchone() #All information found in the database that fetches the above info
    if row is None:
        cur.execute('''INSERT INTO Counts (email, count) VALUES (?, 1)''', (email,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?', (email,))
    conn.commit()

# https://www.sqlite.org/lang_select.html 
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 5'

for row in cur.execute(sqlstr):
    print(row[0],row[1]) #In the explainer video he converted to str but I didn't see it as necessary so I removed.

cur.close()