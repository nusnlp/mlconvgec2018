#!/usr/bin/python

# This script extracts for a particular l1 and l2

import argparse
import os
import sys

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input_file", dest="input_file", required=True, help="Lang8 file to be processed, in decoded format")
parser.add_argument("-o", "--output_dir", dest="output_dir", required=True, help="Path to output directory")
parser.add_argument("-l1","--native_language", dest="l1", help="Extract only for this native language")
parser.add_argument("-l2","--learning_language", dest="l2", required=True, help="Extract only for this learning language")
parser.add_argument("-split", dest="split_out", action="store_true", help="Enable this flag if output is to be split to different native languages")
args = parser.parse_args()

count = 0

if not os.path.exists(args.output_dir):
	os.makedirs(args.output_dir)

if args.l1 is None:
	l1dict = dict()
	f_combined_out=open(args.output_dir+"/" + os.path.basename(args.input_file) + ".processed",'w')
else:
	if args.l2 is None:
		print >> sys.stderr, "L2 should also be specfied"
		sys.exit()
	f_out = open(args.output_dir + "/" + os.path.basename(args.input_file) + "." + "processed.l1_" + args.l1,'w')
	#f_rest = open(args.output_dir + "/" + args.input_file + "." + "processed.l1_" + args.l1,'w')

with open(args.input_file) as f:
	for line in f:
		l2= line.split(',')[2][1:-1]
		l1= line.split(',')[3][1:-1]
		# If Learning Language is Specified and Learning Language = Required Learning Language
		if args.l2 is not None and args.l2 == l2:
			if args.l1 is None:
				if args.split_out:
					if l1dict.has_key(l1): # To check if the native language file has been opened
						f_out = l1dict[l1]
						f_out.write(line)
					else:
						f_out = open(args.output_dir + "/" + os.path.basename(args.input_file) + "." + "processed.l1_" + l1,'w')
						l1dict[l1] = f_out
						f_out.write(line)
				else:
					f_combined_out.write(line)
			# If Native Language is specified write that only.
			else:
				if args.l1 == l1:
					f_out.write(line)
		# If no language is specified or only L1 is specified
		elif args.l2 is None:
			f_combined_out.write(line)
if args.l1 is not None:
	f_out.close()

if args.l1 is None and args.split_out == True:
	for l1, f_out in l1dict.iteritems():
		f_out.close()

