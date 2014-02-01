from datetime import datetime
from peewee import *
database = SqliteDatabase('debug.db')#:memory:')  # Create a database instance.


class Book(Model):
	name = CharField()

	class Meta:
		database = database # this model uses the in-memory database we just created


class Recipe(Model):
    name = CharField()
    image = CharField()
    addition_date = DateField(default=datetime.now)
    book = ForeignKeyField(Book, null=True, related_name="recipes")
    is_reviewed = BooleanField(default=False)

    class Meta:
		database = database # this model uses the in-memory database we just created


if __name__ == '__main__':
	Recipe.create_table()
	Book.create_table()