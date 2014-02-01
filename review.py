from common import *
from models import *
from datetime import datetime

SCREEN_WIDTH = 50

def print_recipes():
	print "## All recipes:"
	print
	for recipe in Recipe.select():
		print '- [%s](import/%s)' % (recipe.name, recipe.image)


def process_unreviewed():
	today = datetime.today()

	for recipe in Recipe.select().where(Recipe.is_reviewed==False):
		if recipe.name: 
			print "Recipe name:", recipe
		else:
			print "Recipe file:", recipe.image
		answer = raw_input("name? ")
		if answer:
			recipe.name = answer
			recipe.is_reviewed = True
			recipe.update_date = today
			recipe.save()
	else:
		print "Nothing to review."

if __name__ == '__main__':
	print
	process_unreviewed()
	print
	print_recipes()