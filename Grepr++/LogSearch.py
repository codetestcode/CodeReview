import re
import logging
from colorlog import ColoredFormatter


class LogSearch:

	def __init__(self): pass

	def search(self, file_path,search_type):

		self.file_path = file_path
		self.search_type = search_type
