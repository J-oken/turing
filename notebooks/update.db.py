#!/bin/env python3

import os, sys;

import glob;

import sqlite3;

import hashlib;

from simhash import Simhash;

import tokenizador as tkn;

###############################################################################
if __name__=="__main__":

   DBNAME ="./glwiki.db"
   SQLFILE="./glwiki.sql";

   with sqlite3.connect(DBNAME, isolation_level=None) as dbc:

        with open(SQLFILE,"rt") as fd:
             dds=fd.read();
             dbc.executescript(dds);
             dbc.commit();
             
        sources=[];
        
        for arg in sys.argv[1:]:
            if arg[:9]=="--source=":
               source=arg[9:];
               if os.path.isfile(source):
                  sources.append(source);
               if os.path.isdir(source):
                  for filename in glob.glob(os.path.join(source,"*.txt")):
                      sources.append(filename);

        for filename in sources:
        
            with open(filename,"rt") as fd:
                 url   = fd.readline().strip();
                 title = fd.readline().strip();
                 text  = fd.read().lower();
                 
                 m = hashlib.sha256();
                 m.update(text.encode("utf-8"));
                 n_hash=m.hexdigest();
                 
                 s_hash=str(Simhash(text).value);
                                  
                 cur=dbc.cursor();
                 #cur.execute("DELETE FROM pages WHERE url=? OR title=?;",(url,title));
                 cur.execute("INSERT INTO pages(url,title,nhash,shash) values (?,?,?,?);",(url,title,n_hash,s_hash));
                 page=cur.lastrowid;
                 
                 print(f"{title}", flush=True);
                                       
                 F=tkn.stats(text, sort=False);
                 
                 for (glyph,f) in F.items():
                     
                     cur.execute("SELECT token FROM tokens WHERE glyph=?;",(glyph,));
                     row=cur.fetchone();
                     if row==None:
                        cur.execute("INSERT INTO tokens(glyph) values (?);",(glyph,));
                        token=cur.lastrowid;
                     else:
                        token=row[0];
                     
                     cur.execute("INSERT INTO invidx (page,token,counter) VALUES (?,?,?);",(page,token,f));
                     
                 