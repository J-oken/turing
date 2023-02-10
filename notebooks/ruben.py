

A=["La","casa","de","la","pradera","fue","una","serie","bonita","pero","muy","antigua"];
B=["De","pequeño","me","gustaba","la","rubia","de","la","casa","de","la","pradera"];

A=set([x.upper() for x in A]);
B=set([x.upper() for x in B]);

pd = len(A.intersection(B))/len(A.union(B));

print(pd);
