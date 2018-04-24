#!/usr/bin/python


import sys
from operator import itemgetter
import random
import argparse

random.seed(1234)

def read_from_m2(filename):

	dataset_lines = []
	sent_lines = []

	with open(filename) as f:
		lcount = 0
		for line in f:
			line = line.strip()
			if line.startswith('S'):
				lcount += 1
				#if lcount > int(numlines):
				#	break
				if lcount > 1:
					dataset_lines.append(sent_lines)
				sent_lines = [line]
			if line.startswith('A'):
				sent_lines.append(line)
		dataset_lines.append(sent_lines)
	return dataset_lines

def write_to_m2(wlines, fwrite):
	for line in wlines:
		fwrite.write(line+'\n')
	fwrite.write('\n')


def get_chunks(l, n):
   	nlines = len(l)/n
	chunks = [l[i:i + nlines] for i in range(0, len(l)-len(l)%nlines, nlines)]
	rem = len(l)%nlines
	if rem > 0:
		chunks[-1] += l[-rem:]
	return chunks

def split_lines(filename, outprefix, numparts, shuffle=False):

	# Read from input m2 file
	dataset_lines = read_from_m2(filename)

	if args.shuffle == True:
		random.shuffle(dataset_lines)

	data_chunks = get_chunks(dataset_lines, numparts)

	fwrites = []
	for i in xrange(numparts):
		fwrites.append(open(outprefix+"."+str(i+1)+".m2",'w'))
	for i in xrange(numparts):
		for lines in data_chunks[i]:
			write_to_m2(lines, fwrites[i])
		fwrites[i].close()

def get_lines(filename, outprefix, numlines,  shuffle=False):

	# Read from input m2 file
	dataset_lines = read_from_m2(filename)

	if args.shuffle == True:
		random.shuffle(dataset_lines)

	# Writing the num. of lines to the m2 file
	fwrite = open(outprefix+"."+str(numlines)+".m2",'w')
	# Writing to output file
	for lines in dataset_lines[:numlines]:
		write_to_m2(lines, fwrite)
	fwrite.close()

	remaining_numlines = len(dataset_lines) - numlines
	# Writing the num. of lines to the remaining m2 file
	fwrite = open(outprefix+"."+str(remaining_numlines)+".m2",'w')
	for lines in dataset_lines[:numlines]:
		write_to_m2(lines, fwrite)
	fwrite.close()

	if numlines <= len(dataset_lines):
		fwrite = open(outprefix+"."+str(remaining_numlines)+".m2",'w')
		for lines in dataset_lines[numlines:]:
			write_to_m2(lines, fwrite)
		fwrite.close()

parser = argparse.ArgumentParser()
parser.add_argument('-i','--input_m2', dest="input_m2", required=True, help="Path to input m2 file")
parser.add_argument('-o','--output_m2_prefix', dest="output_m2_prefix", required=True, help="Path to output m2 file")
parser.add_argument('-s','--shuffle', dest="shuffle", action='store_true', help="Shuffle the m2 file before splitting")
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-l','--num_lines', type=int, dest="num_lines", help="Number of lines to extract")
group.add_argument('-n','--num_parts', type=int, dest="num_parts", help="Number of parts to split m2 file into")
args = parser.parse_args()

if args.num_lines:
	get_lines(args.input_m2, args.output_m2_prefix, args.num_lines, args.shuffle)
elif args.num_parts:
	split_lines(args.input_m2, args.output_m2_prefix, args.num_parts, args.shuffle)

