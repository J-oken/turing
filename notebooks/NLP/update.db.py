#!/bin/env python3

import os, sys;

import glob;

import sqlite3;

import tokenizador as tkn;

import hashlib;

################################
if __name__ == "__main__":

    DBNAME="./glwiki.db"
    SQLFILE="./glwiki.sql"
    
    with sqlite3.connect(DBNAME, isolation_level=None) as dbc:

        with open(SQLFILE, 'rt') as fd:
            dds = fd.read();
            dbc.executescript(dds);
            dbc.commit();

        sources=[];

        for arg in sys.argv[1:]:
            if arg[:9]=="--source--":
                source=arg[9:];
                if os.path.isfile(source):
                    sources.append(source);
                if os.path.isdir(source):
                    for filename in glob.glob(os.path.join(source, '*.txt')):
                        sources.append(filename);
        for filename in sources:
                                                        
            with open(filename,"rt") as fd:
                url  = fd.readline().strip();
                title= fd.readline().strip();
                test = fd.read().lower();
                                                           
                m = hashlib.sha256();
                m.update(text.encode("utf-8"));
                n_hash=m.hexdigest();
                                                        
                s_hash=str(Simhash(text).value)
                cur=dbc.cursor();
                #cur.execute("DELETE FROM pages WHERE url=?
                cur ejecute