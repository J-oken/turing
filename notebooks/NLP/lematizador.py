#!/bin/env python3

import sys, os;

import stanza;

if __name__ == "__main__":

   tokens={};

   stanza.download("gl");
   nlp=stanza.Pipeline(lang="gl", processors="tokenize,mwt,pos,lemma");

   for line in sys.stdin:
       doc=nlp(line);
       words=[word.lemma.upper() for sent in doc.sentences for word in sent.words];
       for word in words:
           if word not in tokens: tokens[word] =1;
           else:                  tokens[word]+=1;


   with open("tokens.txt","wt") as fd:
       for key, value in sorted(tokens.items(),key=lambda item: item[1], reverse=True):
           print(f"{value:<10} {key}", file=fd);

