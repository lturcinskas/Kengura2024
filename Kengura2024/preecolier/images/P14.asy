import geometry;
settings.outformat="pdf";
settings.pdfviewer="/usr/bin/evince";
size(80);

draw(box((0,0),(2,2)));
draw((0,0)--(2,2));
draw((2,0)--(0,2));
draw((1,0)--(1,2));
draw((2,1)--(0,1));
draw((2,1)--(1,0)--(0,1)--(1,2)--cycle);

real r=0.3;
filldraw(circle((0,0), r), mediumgray);
filldraw(circle((0,1), r), mediumgray);
filldraw(circle((0,2), r), mediumgray);
filldraw(circle((1,0), r), mediumgray);
filldraw(circle((1,1), r), mediumgray);
filldraw(circle((1,2), r), mediumgray);
filldraw(circle((2,0), r), mediumgray);
filldraw(circle((2,1), r), mediumgray);
filldraw(circle((2,2), r), mediumgray);



// Label nodes
label("4", (0, 0));
label("2", (1, 0));
label("10", (2, 0));
label("12", (0, 1));
label("1", (1, 1));
label("5", (2, 1));
label("3", (0, 2));
label("1", (1, 2));
label("7", (2, 2));