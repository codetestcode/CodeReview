import sys
import re

LOG_LOC = 'data/server.log'
PREFIX_EXPR     = '((?:2|1)\\d{3}(?:-|\\/)(?:(?:0[1-9])|(?:1[0-2]))' +
	              '(?:-|\\/)(?:(?:0[1-9])|(?:[1-2][0-9])|(?:3[0-1]))' + 
	              '(?:T|\\s)(?:(?:[0-1][0-9])|(?:2[0-3])):(?:[0-5][0-9]):(?:[0-5][0-9])(,)(\\d\\d\\d)( )(\\[.*?\\])( )('
	SUFFIX_EXPR = '))'
ERROR_DEF       = PREFIX_EXPR + 'ERROR'+ SUFFIX_EXPR
WARN_DEF        = PREFIX_EXPR + 'WARN' + SUFFIX_EXPR
INFO_DEF        = PREFIX_EXPR + 'INFO'+ SUFFIX_EXPR
ERROR_DEF       = PREFIX_EXPR + 'ERROR'+ SUFFIX_EXPR
EIN_DEF         = '(EIN)(\\d)(\\d)(\\d)(\\d)'
EXCEPTION_DEF=''#TODO: Define a  REGEX to accurately detect  stack exceptions.


{ '--EXC',  PREFIX_EXPR + 'ERROR'+ SUFFIX_EXPR, '\033[91m'}
{ '--WARN', PREFIX_EXPR + 'WARN'+ SUFFIX_EXPR,  '\033[93m'}
{ '--EXC', PREFIX_EXPR + 'INFO'+ SUFFIX_EXPR, '\033[91m'}
{ '--EXC', PREFIX_EXPR + 'INFO'+ SUFFIX_EXPR, '\033[91m'}


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARN = '\033[93m'
    ERROR = '\033[91m'

    def colorTest(self):
			print(self.HEADER + "HEADER TEST")
			print(self.OKBLUE + "OKBLUE TEST")
			print(self.OKGREEN + "OKGREEN TEST")
			print(self.WARNING + "WARNING TEST")
			print(self.ERROR + "HEADER TEST")


def filterError():
	pattern = re.compile(ERROR_DEF)
	seen = set()

	with open(LOG_LOC,'r') as log:
		for line in log:
			mo = pattern.search(line)
			if mo is not None:
				errorentry = mo.group()
				if errorentry not in seen:
					seen.add(errorentry)
					redcolor = bcolors()
					print(redcolor.ERROR + line)


def filterWarnings():
	pattern = re.compile(WARN_DEF)
	seen = set()

	with open(LOG_LOC,'r') as log:
		for line in log:
			mo = pattern.search(line)
			if mo is not None:
				warnentry = mo.group()
				if warnentry not in seen:
					seen.add(warnentry)
					yellowcolor = bcolors()
					print(yellowcolor.WARN + line)

def filterInfo():
	pattern = re.compile(INFO_DEF)
	seen = set()

	with open(LOG_LOC,'r') as log:
		for line in log:
			mo = pattern.search(line)
			if mo is not None:
				infoentry = mo.group()
				if infoentry not in seen:
					seen.add(infoentry)
					greencolor = bcolors()
					print(greencolor.OKGREEN + line)

def filterEIN():
	pattern = re.compile(EIN_DEF)
	seen = set()

	with open(LOG_LOC,'r') as log:
		for line in log:
			mo = pattern.search(line)
			if mo is not None:
				einentry = mo.group()
				if einentry not in seen:
					seen.add(einentry)
					bluecolor = bcolors()
					print(bluecolor.OKBLUE + line)


def filter(expression, colorTest):
	pattern = re.compile(expression)
	seen = set()

	with open(LOG_LOC,'r') as log:
		for line in log:
			mo = pattern.search(line)
			if mo is not None:
				entry = mo.group()
				if entry not in seen:
					seen.add(entry)
					print(color + line)


def about():
	pylogo = '''



          777..777777777777$+
         .77    7777777777$$$
         .777 .7777777777$$$$
         .7777777777777$$$$$$
         ..........:77$$$$$$$
  .77777777777777777$$$$$$$$$.=======.
 777777777777777777$$$$$$$$$$.========
7777777777777777$$$$$$$$$$$$$.=========
77777777777777$$$$$$$$$$$$$$$.=========
777777777777$$$$$$$$$$$$$$$$ :========+.
77777777777$$$$$$$$$$$$$$+..=========++~
777777777$$..~=====================+++++
77777777$~.~~~~=~=================+++++.
777777$$$.~~~===================+++++++.
77777$$$$.~~==================++++++++:
 7$$$$$$$.==================++++++++++.
 .,$$$$$$.================++++++++++~.
         .=========~.........
         .=============++++++
         .===========+++..+++
         .==========+++.  .++
          ,=======++++++,,++,
          ..=====+++++++++=.

PYTHON ZEN:
-----------------------------------------
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!

	'''
	print(pylogo)



def main():
	if sys.argv[1] == '--Errors':
		filterError()
	elif sys.argv[1] == '--Info':
		filterInfo()
	elif sys.argv[1] == '--Warnings':
		filterWarnings()
	elif sys.argv[1] == '--EIN':
		filterEIN()
	elif sys.argv[1] == '--EXC':
		filter(EXCEPTION_DEF, '\033[91m')
	elif sys.argv[1] == '--about':
		about()
	else
		print ("You've entered an invalid argument")
		print("="*30)
		print("""Usage:
searchLog --Errors outputs log error entries.
searchLog --Warnings outputs log Warning entries.
searchLog --Info outputs log info entries. 
searchLog --EIN outputs failed jobs.
searchLog --EXC outputs Exceptions.
searchLog --about
			    """
			            )


if __name__ == '__main__':
	main()


