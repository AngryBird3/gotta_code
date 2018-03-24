#!/usr/bin/env python
class Logger:
	DEBUG = 0
	INFO = 1
	WARNING = 2
	ERROR = 3
	CRITICAL = 4
	def __init__(self, level=ERROR):
		self.level = level

	def debug(function, *msg):
		if self.level <= DEBUG:
			print "[DEBUG: %s] %s" %(function, ''.join(str(x) for x in msg))



'''

	def set_debugger(self):
		""" set logging """
		global LOGGER
		try:
			import logging
			LOGGER = logging.getLogger('CommandParser')
			FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
			logging.basicConfig(level=logging.DEBUG, format=FORMAT)
		except ImportError:
			import Logger
			LOGGER = Logger(Logger.DEBUG)	
'''	
