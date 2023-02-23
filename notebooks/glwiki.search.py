#!/bin/env python3

import os, sys, math;

import sqlite3;

from fractions import Fraction;

class  COLOR:
       Black     = "\u001b[30m"
       Red       = "\u001b[31m"
       Green     = "\u001b[32m"
       Yellow    = "\u001b[33m"
       Blue      = "\u001b[34m"
       Magenta   = "\u001b[35m"
       Cyan      = "\u001b[36m"
       White     = "\u001b[37m"
       Bold      = "\u001b[1m"
       Reset     = "\u001b[0m"
       Bold      = '\033[1m'
       Underline = '\033[4m'
       Clearline = "\033[K"

#------------------------------------------------------------------------------
def token_id(dbc, glyph):
    cur=dbc.cursor();
    r=cur.execute("SELECT token FROM tokens WHERE glyph=?;",(glyph,));
    row=r.fetchone();
    if row: return row[0];
    else:   return 0;

#------------------------------------------------------------------------------
def pages_of_token(dbc, token, details=False):
    if details:
       P=[];
       C=[];
       cur=dbc.cursor();
       r=cur.execute("SELECT page,counter FROM invidx WHERE token=?;",(token,));
       for row in r.fetchall():
           page   =row[0];
           counter=row[1];
           if page not in P:
              P.append(row[0]);
              C.append(row[1]);
           else:
              i=P.index(page);
              C[i]+=counter;
       return P,C;
    else:
       cur=dbc.cursor();
       r=cur.execute("SELECT COUNT(*) FROM invidx WHERE token=?;",(token,));
       row=r.fetchone();
       assert row!=None;
       return row[0];
       
#------------------------------------------------------------------------------
def page_data(dbc, page):
    r=cur.execute("SELECT url,title FROM pages WHERE page=?;",(page,));
    row=r.fetchone();
    if row: return row[0],row[1];
    else:   return None,  None  ;

#------------------------------------------------------------------------------
def page_max(dbc, page):
    cur=dbc.cursor();
    r=cur.execute("SELECT MAX(counter) FROM invidx WHERE page=?;",(page,));
    row=r.fetchone();
    assert row!=None;
    return row[0];

###############################################################################
if __name__=="__main__":
   
   DBNAME ="./glwiki.db"

   with sqlite3.connect(DBNAME, isolation_level=None) as dbc:

        P_TOTAL=None;
        
        cur=dbc.cursor();
        
        cur.execute("SELECT COUNT(*) FROM pages;");
        row=cur.fetchone();
        assert row!=None, f"No he podido recuperar el total de páginas en la base de datos";
        P_TOTAL=row[0];
        
        print(f"Número total de páginas indexadas: {COLOR.Red}{P_TOTAL}{COLOR.Reset}.");
        
        while True:
              prompt=input(COLOR.Yellow+"?> "+COLOR.Reset) .strip() .lower();
                     
              if prompt:
                 # TODO esto tenemos que rellenarlo entre todos
                 pass;
                 
              else:
                 break;

                    
                    
#pending!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
tf_idf={k:v for k,v in sorted(tf_idf.items(), key=lamda x:x[1], reverse=True)
        if v!=0};
#imprimir las 10 primeras paginas
for i, page in enumerate(tf_idf):
    score=tf_idf[page];
    url,title=page_data(dbc,page);
    print(f"{COLOR.Magenta}[{score}]{COLOR.Red}{title}{Color.Reset}");
    print(f"{COLOR.Bue}{url}{COLOR.Reset}");
    if i>10: break;