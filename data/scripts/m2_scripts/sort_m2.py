#!/usr/bin/python


import sys
from operator import itemgetter
import argparse


def write_to_m2(wlines, fwrite):
	for line in wlines:
		fwrite.write(line+'\n')
	fwrite.write('\n')

def collect_lines(filename, outfilename, min_annots=0, out_remaining=False):
	sent_lines = []
	dataset_lines = []
	lcount = 0
	fwrite = open(outfilename,'w')
	fremwrite = open(outfilename + '.rem', 'w')
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

	for lines in dataset_lines:
		if len(lines) == 0:
			print line
	sortedset = sorted(dataset_lines, key=lambda x: (len(x), -len(x[0].split())))
	for lines in sortedset:
		if len(lines) - 1 >= min_annots :	# len(lines) = sentence + annots
			write_to_m2(lines, fwrite)
		elif out_remaining == True:
			write_to_m2(lines, fremwrite)
	fwrite.close()
	fremwrite.close()

parser = argparse.ArgumentParser()
parser.add_argument('-i','--input_m2', dest="input_m2", required=True, help="Path to input m2 file")
parser.add_argument('-o','--output_m2', dest="output_m2", required=True, help="Path to output m2 file")
parser.add_argument('-m','--min_annots', type=int, dest="min_annots", help="Keep only lines with >= min. no. of annotations")
parser.add_argument('--output-remaining-lines', action='store_true', dest="out_remaining", help="Output remaiining lines")
args = parser.parse_args()

#filename = sys.argv[1]
#outfilename = sys.argv[2]
collect_lines(args.input_m2, args.output_m2, args.min_annots,args.out_remaining)


