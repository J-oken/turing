CREATE TABLE IF NOT EXISTS pages(page   INTEGER PRIMARY KEY,
                                 url    TEXT NOT NULL,
                                 title  TEXT NOT NULL,
                                 nhash  TEXT NOT NULL,
                                 shash  TEXT NOT NULL,
                                 
                                 UNIQUE (url)   ON CONFLICT FAIL,
                                 UNIQUE (title) ON CONFLICT FAIL
                                );
                                                                                  
CREATE TABLE IF NOT EXISTS tokens(token   INTEGER PRIMARY KEY,
                                  glyph   TEXT NOT NULL,
                                       
                                  UNIQUE (glyph) ON CONFLICT FAIL
                                  
                                 );
                                                        
CREATE TABLE IF NOT EXISTS invidx(page    INTEGER NOT NULL,
                                  token   INTEGER NOT NULL,
                                  counter INTEGER DEFAULT 0,
                                                         
                                  PRIMARY KEY (page,token),
                                                           
                                  FOREIGN KEY (page)  REFERENCES pages  (page)  ON DELETE CASCADE,
                                  FOREIGN KEY (token) REFERENCES tokens (token) ON DELETE CASCADE
                                  
                                 ) WITHOUT ROWID;
                    
CREATE INDEX IF NOT EXISTS invidx_page_idx  ON invidx (page );

CREATE INDEX IF NOT EXISTS invidx_token_idx ON invidx (token);

PRAGMA synchronous = NORMAL;
PRAGMA journal_mode = WAL;
PRAGMA foreign_keys = ON;
PRAGMA cache_size = -32000;
