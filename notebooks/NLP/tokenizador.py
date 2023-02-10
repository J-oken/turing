#!/bin/env python3

import os, sys;
import unicodedata as UD;

#----------------------------------------------
def tokenizer(text:str):
	#funcion para tokenizar un texto (p.ej. una linea)
	s=0;
	t="";

	for c in text:

		cat=UD.category(c);

		if	s==0:
			if cat[0]=='L':
				t=c;
				s=1;
			else:
				s=0;
		elif s==1:
			if cat[0]=='L':
				s=1;
				t=t+c;
			else:
				yield t;
				t="";
				s=0;

	if t: yield t;
###################################################
def stats(text:str, rt={}, sort=False):

	if text:
		for token in tokenizer(text):
			if token not in rt: rt[token]=0;
			rt[token]+=1;
	if sort:
		rt={k:v for k,v in sorted(rt.items(), key=lambda item: item[1], reverse=True)};

	return rt;
#################################################
if __name__=="__main__":

        F={};

        for line in sys.stdin:
                F=stats(line.lower(),F);

        F=stats(None, rt=F, sort=True);

        for (token,f) in F.items():
                print(token, f);

