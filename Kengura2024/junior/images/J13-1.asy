import geometry;
settings.outformat="pdf";
settings.pdfviewer="/usr/bin/evince";
size(6cm);

pair O = origin;
fill(circle(O,4));
fill(circle(O,3), gray);
fill(circle(O,0.98), white);

real r = 11.2;

fill(circle((r,0),4));
fill(circle((r,-1),3), gray);
fill(circle((r,3),0.98), white);