#!/usr/bin/env python

from subprocess import call

def main():
	"""
	A simple shell. Just a frontent for deafult shell.
	"""
	try:	
		while True:
			ins = raw_input("% ")
			call(ins, shell=True)
	except EOFError:
		print ("^D")


if __name__ == "__main__":
	main()
