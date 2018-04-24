#!/usr/bin/python
import sys, nltk

while 1:
	line = sys.stdin.readline()
	if not line:
		break
	line = line.decode('utf8')
	print ' '.join(nltk.word_tokenize(line.strip())).encode('utf8')
