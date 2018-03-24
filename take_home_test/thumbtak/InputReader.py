#!/usr/bin/env python
import sys
import Commands

class InputReader:
	""" This class reads input (file/command line till END encountered) """
	def read_input(self):
		""" Read inputs """
		line = raw_input()
		if Commands.END in line:
			sys.exit(0) 	
		else:
			#LOGGER.debug(line)
			return line

