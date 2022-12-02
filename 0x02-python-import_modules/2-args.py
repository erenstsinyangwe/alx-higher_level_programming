#!/usr/bin/python3
if __name__ == "__main__":
	import sys
	arg_count = len(sys.argv)
	if arg_count == 1:
		print("0 arguments.")
	if arg_count > 1:
		count = len(sys.argv) - 1
		print("{} argument:".format(count))
		index = 1
		while index <= count:
			argument = sys.argv[index]
			print("{}: {}".format(index, argument))
			index += 1
