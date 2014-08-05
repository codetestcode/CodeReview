#!/usr/bin/env python
#created by:Don Johnson
#email :dj@codetestcode.io


import re
import logging
from colorlog import ColoredFormatter


class LogSearch:

	def __init__(self): pass

	def init_logger(self):
		"""Initialize Logger format setting."""
		formatter = ColoredFormatter(
        "%(log_color)s%(levelname)-8s%(reset)s %(white)s%(message)s",
        datefmt=None,
        reset=True,
        log_colors={'DEBUG':'cyan','INFO':'green','WARNING':'yellow','ERROR':'red','CRITICAL':'red'}
    )
		logger = logging.getLogger('example')
		handler = logging.StreamHandler()
		handler.setFormatter(formatter)
		logger.addHandler(handler)
		logger.setLevel(logging.DEBUG)
		return logger

	def greplog(self, file_path,search_type=''):
		"""Usage: greplog(file_path,search_type) Valid search types: INFO, WARN, ERROR, DEBUG, CRITICAL"""
		reg_ex_prefix = '((?:2|1)\\d{3}(?:-|\\/)(?:(?:0[1-9])|(?:1[0-2]))(?:-|\\/)(?:(?:0[1-9])|(?:[1-2][0-9])|(?:3[0-1]))(?:T|\\s)(?:(?:[0-1][0-9])|(?:2[0-3])):(?:[0-5][0-9]):(?:[0-5][0-9])(,)(\\d\\d\\d)( )(\\[.*?\\])( )('
		reg_ex_suffix = '))'
		self.file_path = file_path
		self.search_type = search_type
		logger = self.init_logger()

		pattern = re.compile(reg_ex_prefix + search_type + reg_ex_suffix)
		seen = set()
		try:
			with open(file_path,'r') as log:
				for line in log:
					mo = pattern.search(line)
					if mo is not None:
						searchentry = mo.group()
						if searchentry not in seen:
							seen.add(searchentry)
							if search_type == 'INFO':
								logger.info(line)
							elif search_type == 'WARN':
								logger.warning(line)
							elif search_type == 'ERROR':
								logger.error(line)
							elif search_type == 'DEBUG':
								logger.debug(line)
							elif search_type == 'CRITICAL':
								logger.critical(line)
							else:
								logger.info(line)
		except Exception as e:
			print('Error Occured during  search {}'.format(e))






def test():
	testLogSearch = LogSearch()
	greplog_test_info = testLogSearch.greplog('data/server.log','INFO')
	greplog_test_warn = testLogSearch.greplog('data/server.log','WARN')
	greplog_test_error = testLogSearch.greplog('data/server.log','ERROR')
	greplog_test_critical = testLogSearch.greplog('data/server.log','CRITICAL')
	greplog_test_debug = testLogSearch.greplog('data/server.log','DEBUG')


if __name__ == '__main__':
	test()
