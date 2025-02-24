import geometry;
settings.outformat="pdf";
settings.pdfviewer="/usr/bin/evince";
size(100);

real a = 2;
real b = 3;
real c = 6;
real s = a+b+c;
pair B = (0,0);
pair C = (s,0);
pair A = rotate(60)*C;
pair P = rotate(60)*(c,0)+(a,0);
pair CP = rotate(60)*(c,0);
pair BP = rotate(60)*(c+b,0)+(a,0);
pair AP = (a+c,0);


draw(C--A--B--cycle);
draw(CP--P--AP);
draw(BP--P);


// Label nodes
label("$P$", P, E);
label("$A$", A, N);
label("$B$", B, SW);
label("$C$", C, SE);

label("$2$", CP--P, (0,-0.5));
label("$6$", AP--P, (0.5,0));
label("$3$", BP--P, (-0.5,0.2));