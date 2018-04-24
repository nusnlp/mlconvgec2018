#!/usr/bin/python

import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("-i","--input_file", dest="input_path", required="True", help="Path to input file" )
parser.add_argument("-o","--output_prefix", dest="output_prefix", required="True", help="Output prefix" )
parser.add_argument("-d","--output_dir", dest="output_dir", required="True", help="Path to output_directory" )
parser.add_argument("-l1","--split_by_l1", dest="split_by_l1", action="store_true", help="Enable this flag to split by L1")
args = parser.parse_args()

if not os.path.exists(args.output_dir):
    os.makedirs(args.output_dir)

l1_dict = dict()
if args.split_by_l1 == False:
    out_path_prefix = args.output_dir + "/" + args.output_prefix
    src_path = out_path_prefix + ".src"
    trg_path = out_path_prefix + ".trg"
    f_src, f_trg = open(src_path,'w'), open(trg_path,'w')

with open(args.input_path) as f:
    for line in f:
        line = line.strip()
        pieces = line.split('\t')
        if len(pieces) < 5:
            continue
        l1 = pieces[2].replace(" ", "-")
        src_sent = pieces[3]
        trg_sent = pieces[4]
        if args.split_by_l1 == True:
            if l1 not in l1_dict:
                out_path_prefix = args.output_dir + "/" + args.output_prefix + "." + l1
                src_path = out_path_prefix + ".src"
                trg_path = out_path_prefix + ".trg"
                l1_dict[l1] = open(src_path,'w'), open(trg_path,'w')
            f_src, f_trg = l1_dict[l1]
            f_src.write(src_sent + '\n')
            f_trg.write(trg_sent + '\n')
        else:
            f_src.write(src_sent + '\n')
            f_trg.write(trg_sent + '\n')

if args.split_by_l1 == False:
    f_src.close()
    f_trg.close()
else:
    for l1, fp in l1_dict.iteritems():
        fp[0].close() # src file pointer
        fp[1].close() # trg file pointer

