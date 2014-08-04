import re
import logging
from colorlog import ColoredFormatter


class LogSearch:

	def __init__(self): pass

	def search(self, file_path,search_type):
		reg_ex_prefix = '((?:2|1)\\d{3}(?:-|\\/)(?:(?:0[1-9])|(?:1[0-2]))(?:-|\\/)(?:(?:0[1-9])|(?:[1-2][0-9])|(?:3[0-1]))(?:T|\\s)(?:(?:[0-1][0-9])|(?:2[0-3])):(?:[0-5][0-9]):(?:[0-5][0-9])(,)(\\d\\d\\d)( )(\\[.*?\\])( )('
		reg_ex_suffix = '))'
		self.file_path = file_path
		self.search_type = search_type

