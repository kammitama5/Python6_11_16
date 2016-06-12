##Welcome message --> game begin

print 'Welcome to my game. This game is sweet.'
##ask the player for his name
player_name = raw_input('What\'s is your name: ')

## check/ask for player name and display it
if player_name == '':
	print'\n'
	print 'You entered an empty string!'
else:
	
	print 'Your name is {}'.format(player_name)

## check/ask for player age and display it
page =  raw_input('What is your age: ')
if page.isdigit():
	page = int(page)
	print 'Your age is {}'.format(page)
	print'\n'
else:
	print 'Not a real age'
	print'\n'

## functions for gamestuff values of dragon, mazes, dungeons or the single life
def do_dragons():
	print'\n'
	print 'Rahhhh dragons'
	print'\n'
	
def do_mazes():
	print'\n'
	print 'Wheee! you are in a maze!'
	print'\n'

def do_dungeons():
	print '\n'
	print 'You are in a dark and scary dungeon! Creeepy!!'
	print '\n'

def do_the_single_life():
	print '\n'
	print 'You are probably a lonely virgin. Good luck with that!'
	print '\n'
	
## list gamestuff var and ask them to choose
gamestuff = ['dragons','dungeons','mazes','the single life']	


while True:
	print 'What shall we do?'
	for item in gamestuff:
		print '* {}'.format(item)

## choose gamestuff, call a function or else not an answer (or exit to quit)	
	choice = raw_input('>>>')
	if choice.lower() in ['exit','quit']:
		print 'You have chosen to quit.'
		break;
	elif choice == 'dragons':
		do_dragons()
	elif choice == 'mazes':
		do_mazes()
	elif choice == 'dungeons':
		do_dungeons()
	elif choice == 'the single life':
		do_the_single_life()
	elif choice not in gamestuff:
		print 'come on now. That is not a choice.'
	else:
		print 'you chose "{}"'.format(choice)
	