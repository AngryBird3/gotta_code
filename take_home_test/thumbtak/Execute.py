#!/usr/bin/env python
import Commands
import Database
class Execute:
	""" Parse Raw command and issue execute """
	def __init__(self):
		self.db = Database.Database()

	def parse_n_execute(self, raw_command):
		""" Parse commands from raw input """
		#split into words
		command = raw_command.split()
		if command[0] not in Commands.KNOWN_COMMANDS:
			#Unknown command, ignore				
			return
		# Execute the command
		self.execute_command(command)	

	def execute_command(self, command):
		""" Execute command on database """
		#Call the function based on argument
		if command[0] == Commands.BEGIN:
			self.db.begin()
		elif command[0] == Commands.COMMIT: 	
			self.db.commit()
		elif command[0] == Commands.ROLLBACK:
			self.db.rollback()
		elif command[0] == Commands.SET:
			self.db.set_c(command[1], command[2]) 
		elif command[0] == Commands.GET:
			self.db.get(command[1])
		elif command[0] == Commands.UNSET:
			self.db.unset(command[1])
		elif command[0] == Commands.NUMEQUALTO:
			self.db.num_equal_to(command[1]) 
