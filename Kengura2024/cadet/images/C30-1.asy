import geometry;
settings.outformat="pdf";
settings.pdfviewer="/usr/bin/evince";
size(80);

real a = 10;
real b = 4;
pair A = origin;
pair B = (a,0);
pair Ee = (0,b);
pair C = (a,b);
pair D = (a/2,9);

fill((a/5,0)--(a/5,6)--(2a/5,8)--(2a/5,0)--cycle, gray(0.75));
fill((2a/5,0)--(2a/5,8)--D--(3a/5,8)--(3a/5,0)--cycle, gray(0.2));

draw(A--B--C--D--Ee--cycle);
draw((a/5,0)--(a/5,6));
draw((2a/5,0)--(2a/5,8));
draw((4a/5,0)--(4a/5,6));
draw((3a/5,0)--(3a/5,8));

label("$A$", A, SW);
label("$B$", B, SE);
label("$C$", C, E);
label("$D$", D, N);
label("$E$", Ee, W);