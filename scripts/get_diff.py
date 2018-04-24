import sys


prefix = sys.argv[1]
src = sys.argv[2]
trg = sys.argv[3]

with open(prefix + '.' + src) as f_src, open(prefix + '.' + trg) as f_trg:
    for sline, tline in zip(f_src, f_trg):
        sline = sline.strip()
        tline = tline.strip()
        if sline != tline:
            print(sline+'\t'+tline)
