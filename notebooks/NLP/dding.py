#!/bin/env python3

import os, sys;

def dnumber(line:str):
        s=0;
        n="";
        for c in line:
                if s==0:
                   if c.isdigit():
                      s=1;
                      n=c;
                   else:
                      s=0;
                """
                elif s==1:
			if c.isdigit():
				n+=c;
				s=1;
			elif c==".":
				s=2;
			else:
				print(n);
				s=0;
                elif s==2:
			if c.isdigit():
				n+='.' + c;
				s=3;
			else:
				print(n);
				s=0;
                elif s==3:
			if c.isdigit():
				s=3;
				n+=c
			elif c=="e":
				s=4;
			else:
				print(n);
				s=0;
                elif s==4:
                        if c.isdigit():
                                n+= "e" + c;
                                s=5;
                        else:
                                print(n);
                                s=0;
                elif s==5:
                	if c.isdigit():
                                s=5;
                                n+=c;
                    	else:
                              	print(n);
				s=0;
                """
######################################################################

if __name__=="__main__":
	for line in sys.stdin:
		dnumber(line.strip());
