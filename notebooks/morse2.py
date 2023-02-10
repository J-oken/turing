import os, sys

_dmorse={
    'A': '.-', 'Á': '.-',
    'B': '-...',
    'C': '-.-.',
    'CH': '----',
    'D': '-..',
    'E': '.', 'É': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..', 'Í': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'Ñ': '--.--',
    'O': '---', 'Ó': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-', 'Ú': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '.': '.-.-.-',
    ',': '--..--',
    '?': '..--..',
    '"': '· − · · − ·',
    "/": '· − − − − ·'
}

def cmorse(c):
        if c in _dmorse:
                return _dmorse[c]
        else:
                if c==" ": return " ";
                if c=="\n": return "\n";
                return f"<unk,{c}>";
def morse(c):
        m=cmorse(c);
        print(f" {m}", end='', file=sys.stdout);
        return;

def decode(line):
        rt=[]
        l=line.strip().split();
        for c in l:
            for c in _dmorse:
                if e==_dmorse[c]:
                       rt.append(e);
                break;
        return rt;


if __name__=="__main__":
   source=sys.stdin;
   action=c;
        
    for i,arg in enumerate(sys.argv):
        if i==0: continue;
        if arg[:10+1]=="--filename=":
           filename=arg[11:];
           assert os.path.isfile(filename) and os.path.exists(filename);
           sorce=open(filename,"rt");
        if arg=="--to-ascii":
           action="d";

        for line in source:
            if action=="c":
                line=line.upper();
                s=0;
                for i,c in enumerate(line):
                        if s==0:
                                if c=='C':
                                        s==1
                                else:
                                        morse(c)
                                        s==0
                        elif s==1:
                                if c=='H':
                                        morse('CH')
                                        s=0
                                else:
                                        morse('C')
                                        morse(c)
                                        s=0
            else:
              assert action=="d";
              l=decode(line);
              for e in l: print(f"{e]", end='');
              print("");
        if source!=sys.stdin
	   source.close()
