import geometry;
settings.outformat="pdf";
settings.pdfviewer="/usr/bin/evince";
size(60);

// Draw grid
draw((0,0)--(2,0));
draw((0,1)--(2,1));
draw((0,2)--(2,2));
draw((0,0)--(0,2));
draw((1,0)--(1,2));
draw((2,0)--(2,2));

// Label nodes
label("6", (2.5, 1.5));
label("8", (2.5, 0.5));
label("4", (0.5, -0.5));
label("12", (1.5, -0.5));
