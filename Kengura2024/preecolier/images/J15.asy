import geometry;
settings.outformat="pdf";
settings.pdfviewer="/usr/bin/evince";
size(80);

real a = 2;
real b = 3;
real c = 6;
real s = a+b+c;
pair O = (0,0);
pair A = (s,0);
pair B = rotate(60)*A;


draw(O--A--B--cycle);




// Label nodes
label("4", (0, 0));
