import sqlite3
from flask import Flask

app = Flask(__name__)

@app.route('/')
def ReturnList():	
	items = ""

	with sqlite3.connect('SharedList.db') as conn:
		c = conn.cursor()

		for row in c.execute('select * from items'):
			items = items + row[1] + ","

	if(items == ""):
		items = "nothing,"
		
	print items
	return items

@app.route('/rm/<name>')
def RemoveItem(name):
	with sqlite3.connect('SharedList.db') as conn:
		c = conn.cursor()
		print ("Removing item: " + name)
		c.execute('delete from items where name="' + name + '"')

	return 'removing item'

@app.route('/add/<name>')
def AddItem(name):
	with sqlite3.connect('SharedList.db') as conn:		
		c = conn.cursor()
		print ("Adding item: " + name)
		c.execute('insert into items (name) values ("' + name + '")')

	return 'adding item'

if __name__ == "__main__":
	app.run(host='192.168.2.109', port=5000, debug=False)
