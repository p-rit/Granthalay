import sqlite3

def connect():
	conn = sqlite3.connect('book.db')
	cur = conn.cursor()
	cur.execute("CREATE TABLE IF NOT EXISTS book(id integer primary key ,title text, author text,year integer,isbn integer)")
	conn.commit()
	conn.close()

def insert(title,author,year,isbn):
	conn = sqlite3.connect("book.db")
	cur = conn.cursor()
	cur.execute("INSERT INTO book values(NULL,?,?,?,?)",(title,author,year,isbn))
	conn.commit()
	conn.close()

def view():
	conn = sqlite3.connect("book.db")
	cur = conn.cursor()
	cur.execute("SELECT * FROM  book")
	rows = cur.fetchall()
	conn.close()
	return rows

def search(author='',title='',year='',isbn=''):
	conn = sqlite3.connect("book.db")
	cur = conn.cursor()
	cur.execute("SELECT * FROM book where author=? or title=? or year=? or isbn=? ",(author,title,year,isbn))
	rows = cur.fetchall()
	conn.close()
	return rows

def delete(id):
	conn = sqlite3.connect("book.db")
	cur = conn.cursor()
	cur.execute("DELETE FROM book WHERE id =?",(id,))
	conn.commit()
	conn.close()

def update(id,author,title,year,isbn):
	conn = sqlite3.connect("book.db")
	cur = conn.cursor()
	cur.execute("UPDATE book SET author =?, title=? ,year=?,isbn=? WHERE id=?",(author,title,year,isbn,id))
	conn.commit()
	conn.close()



connect()
#insert('Wings of Fire','A P J Abdul Kalam',1998,123467878)
update(2,'author','title',2018,10937468)
print(view())