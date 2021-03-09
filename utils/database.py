import sqlite3

DATABASE_PATH = "database.sqlite3"


class Database:
	conn = sqlite3.connect(DATABASE_PATH)

	@staticmethod
	def cursor():
		return Database.conn.cursor()

	@staticmethod
	def commit():
		Database.conn.commit()
