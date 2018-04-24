#!/usr/bin/python

# Script to shuffle sentences in an M2 file
#Author: shamil.cm@gmail.com

import sys
from operator import itemgetter
from random import shuffle

def write_to_m2(wlines, fwrite):
	for line in wlines:
		fwrite.write(line+'\n')
	fwrite.write('\n')

def shuffle_lines(filename, outfilename):
	sent_lines = []
	dataset_lines = []
	lcount = 0
	fwrite = open(outfilename,'w')
	with open(filename) as f:
		lcount = 0
		for line in f:
			line = line.strip()
			if line.startswith('S'):
				lcount += 1
				if lcount > 1:
					dataset_lines.append(sent_lines)
				sent_lines = [line]
			if line.startswith('A'):
				sent_lines.append(line)
		dataset_lines.append(sent_lines)

	shuffle(dataset_lines)
	for lines in dataset_lines:
		write_to_m2(lines, fwrite)
	fwrite.close()



filename = sys.argv[1]
outfilename = sys.argv[2]
shuffle_lines(filename, outfilename)


