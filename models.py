from datetime import datetime
from peewee import *
database = SqliteDatabase('debug.db')#:memory:')  # Create a database instance.


class Book(Model):
	name = CharField()

	class Meta:
		database = database # this model uses the in-memory database we just created


class Recipe(Model):
    name = CharField(default='')
    image = CharField()
    addition_date = DateField(default=datetime.now)
    update_date = DateField(default=datetime.now)
    book = ForeignKeyField(Book, null=True, related_name="recipes")
    is_reviewed = BooleanField(default=False)
    #tags = 
    #ingridients = 


    class Meta:
		database = database # this model uses the in-memory database we just created


if __name__ == '__main__':
	Recipe.drop_table()
	Recipe.create_table()
	Book.drop_table()
	Book.create_table()