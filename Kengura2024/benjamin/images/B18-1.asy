import geometry;
settings.outformat="pdf";
settings.pdfviewer="/usr/bin/evince";
size(80);

import graph;

real[] angles = {210, 270, 330};

pair[] centers = {(2.5, 0), (5.0, 0), (7.5, 0)};

void drawFilledCircles(pair center) {
for (int i = 0; i < 3; ++i) {
filldraw(circle(rotate(angles[i])*center, 1), white);
}
}


void drawCircles() {
for (pair center : centers) {
drawFilledCircles(center);
}
}

void main() {
for (real angle: angles){
	draw((0,0)--rotate(angle)*(7.5,0), linewidth(1.5pt));
}
drawCircles();
filldraw(circle((0,0), 1), white);
label("?", (0,0));
}


main();