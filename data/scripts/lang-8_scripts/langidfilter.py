#!/usr/bin/python
#written by Peter Phandi

def extract_corrections(file):
  """Search for sentences and corrections from Lang-8 HTML"""
  #import json
  import os.path
  import langid
  fname = os.path.basename(file)
  if not os.path.isfile(file):
    return

  import re
  re_sentences   = re.compile(r'.*",\["(.*)"\],\[\[.*')
  re_corrections = re.compile(r'.*\],\[\[(.*)\]\]\]')

  sentences           = "[]"
  corrections         = "[]"
  language	      = ""
  for line in open(file, 'r'):
    line = line.rstrip()
    journal_id = line.split(',')[0][2:-1]
    author_id = line.split(',')[1][1:-1]
    language = line.split(',')[3][1:-1]
    m = re_sentences.match(line)
    if m:
      sentences = re.split('","',m.group(1))
    m = re_corrections.match(line)
    if m:
      corrections = re.split('\],\[',m.group(1))
      if len(sentences) != len (corrections) : continue
      empty = False
      for x in range(0,len(corrections)):
        if len(corrections[x])>0 : break
        if x == len(corrections)-1 : empty = True
      if empty : continue
      for x in range(0,len(corrections)):
	lang, prob = langid.classify(sentences[x])
        if lang!='en' : continue
        if len(corrections[x])>0 :
          corrections[x] = corrections[x][1:-1]
        if corrections[x] == '':
          print journal_id+'\t'+author_id+'\t'+language+'\t'+sentences[x]+'\t'+sentences[x]
        else:
          for corr in re.split('","',corrections[x]) :
            lang, prob = langid.classify(corr)
            if lang!='en' : continue
            if len(corr.split(" ,.")) - len(sentences[x].split(" ,.")) > 5 : continue
            else :
              print journal_id+'\t'+author_id+'\t'+language+'\t'+sentences[x]+'\t'+corr

def main():
  """Read Base64 encoded string and output decoded string"""
  import sys

  if len(sys.argv) < 2:
    print >>sys.stderr, "Usage: %s file1 file2 ..." % (sys.argv[0])
    sys.exit(-1)
  for file in sys.argv[1:]:
    extract_corrections(file)

main()
