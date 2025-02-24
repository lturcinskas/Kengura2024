import geometry;
settings.outformat="pdf";
settings.pdfviewer="/usr/bin/evince";
size(60);

pair O = origin;
pair A = (10,10);
pair B = (10,0);
pair C = (0,10);
pair D = (8,10);
real[] isec = intersect(O--D,B--C);
pair E = point(O--D,isec[0]);

fill(O--E--C--cycle, mediumgray);
fill(D--E--B--cycle, mediumgray);
draw(O--D);
draw(B--C);
draw(D--B);
draw(box(O,A), linewidth(1pt));

label("$A$", (2,5));
label("$B$", (7,5));