import geometry;
settings.outformat="pdf";
settings.pdfviewer="/usr/bin/evince";
size(69);

//defaultpen(linewidth(0.7pt)+linejoin(1));

filldraw((0,0)--(10,0)--(10,10)--(0,10)--cycle, mediumgray);

filldraw((0,0)--(1.5,0)--(1.5,1.5)--(0,1.5)--cycle, white);
filldraw((4,0)--(10,0)--(10,6)--(4,6)--cycle, white);
filldraw((0,7.5)--(2.5,7.5)--(2.5,10)--(0,10)--cycle, white);
filldraw((7,7)--(10,7)--(10,10)--(7,10)--cycle, white);

label("$1$", (1.5,0.75), E);
label("$6$", (4,3), NW);
label("$2$", (2.5,8.75), E);
label("$3$", (7,8.5), W);
