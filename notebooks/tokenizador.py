#/bin/env python3

import os, sys;

import unicodedata as UD;

if __name__=="__main__":
    source=sys.stdin;
    tokens={}
    symbols={}
    
    s=0;
    t="";
    for line in source:
        
        for c in line:
        
            cat=UD.category(c)
        
            if s==0:
                    
                if cat[0]=="L":
                    t=c;
                    s=1;
                else:
                    if c not in symbols: symboss[c] =1;
                    else:		 symbols[c]+=1
                    s=0;
                    
            elif s==1:
                if cat[0]=="L":
                    s=1;
                    t=t+c;
                else:
                    print("CHECKPOINT-2",t);
                    if t not in tokens:   tokens[t] =1
                    else:		  tokens[t]+=1
                    if c not in symbols: symbols[c] =1
                    else:		 symbols[c]+=1
                    print(c);
                    s=0;
                    
                    
    with open("tokens.txt","wt") as fd:
        for key,value in sorted(token.items(),key=lambda item:
            print(f"{value:<10 {key}", file=fd);
                    
    with open("symbols.txt","wt") as fd:
        for key,value in sorted(symbols.items(),key=lambda item:
            print(f"{value:<10 {key}", file=fd); 
                           