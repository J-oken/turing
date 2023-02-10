#!/bin/env python3

import os, sys;

if __name__=="__main__":
	for i, arg in enumerate(sys.argv):
		if i==0: continue
		fd=open(arg, "rt");
		for line in sys.stdin:
			line=line.upper();
			print(line, file=sys.stdout);
