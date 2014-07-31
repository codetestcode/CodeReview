#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created By Don Johnson <dj@codetestcode.io)

import re
import sys

PREFIX_EXP = '''((?:2|1)\\d{3}(?:-|\\/)(?:(?:0[1-9])|(?:1[0-2]))
	                (?:-|\\/)(?:(?:0[1-9])|(?:[1-2][0-9])|(?:3[0-1]))
	                (?:T|\\s)(?:(?:[0-1][0-9])|(?:2[0-3])):(?:[0-5][0-9]):
	                (?:[0-5][0-9])(,)(\\d\\d\\d)( )(\\[.*?\\])( )(
	            '''

SUFFIX_EXP = '))'

ERROR_DEF				= PREFIX_EXP + 'ERROR' + SUFFIX_EXP
WARN_DEF 				= PREFIX_EXP + 'WARN' + SUFFIX_EXP
INFO_DEF				= PREFIX_EXP + 'INFO' + SUFFIX_EXP
EIN_DEF					= '(EIN)(//d)(//d)(//d)(//d)'

CLI_OPTIONS = {'--ERROR':ERROR_DEF,'--WARN': WARN_DEF,'--INFO': INFO_DEF,'--EIN': INFO_DEF }

class LogUtil:

	def filter(self,pattern,status_color,file_location):
		self.pattern = pattern

		color_options = {	'info_color': "\\033[94m",'warn_color': '\\033[93m','error_color':'\\033[91m'}

		try:
			log_pattern = re.compile(pattern)
			seen = set()
			with open(file_location,'r') as log:
				for line in log:
					mo = log_pattern.search(line)
					if mo is not None:
						pattern_entry = mo.group()
						if pattern_entry not in seen:
							seen.add(pattern_entry)
							print(color_options[str(self.status_color)] + line)
		except Exception as e:
			print("An error has occured: {}".format(e))

def main():
	info_log_test = LogUtil()
	print(info_log_test.filter(INFO_DEF,'info_color','data/server.log'))
	

if __name__ == '__main__':
	main()
