#!/usr/bin/env python
import InputReader
import Execute

if __name__ == '__main__':	
	reader = InputReader.InputReader()
	execute = Execute.Execute()
	while True:
		raw_command = reader.read_input()	
		execute.parse_n_execute(raw_command)
