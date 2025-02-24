import geometry;
settings.outformat="pdf";
settings.pdfviewer="/usr/bin/evince";
size(150);

real linewidth = 0.7pt;

// Draw polygon
//filldraw((-0.2,0)..(-0.5,-0.5)..(-2,-1)..(2,-1)..(0.5,-0.5)..(0.2,0), gray(0.4));
filldraw((-0.2,0)--(-0.5,-0.6)--(-1.5,-0.8)--(-1.5,-1)--(1.5,-1)..(1.5,-0.8)--(0.5,-0.6)--(0.2,0)..cycle, gray(0.4));
//filldraw((-0.2,0)--(-0.5,-0.5)..(-1.5,-0.9)..(-1.5,-1.1)--(1.5,-1.1)..(1.5,-0.9)..(0.5,-0.5)..(0.2,0)..cycle, gray(0.4));

// Draw line
draw((-2.5,0.5)--(2.5,-0.5), linewidth(2.1pt));//, LineCap(1));

// Draw shapes at (-3,0.5)
filldraw(shift((-2.5,0.5))*circle((0,0.2), 0.2), gray(0.75));
filldraw(shift((-2.5,0.5))*ellipse((0,0.55), 1.7, 0.3), gray(0.75));

// Draw shapes at (3,-0.5)
filldraw(shift((2.5,-0.5))*circle((0,0.2), 0.2), gray(0.75));
filldraw(shift((2.5,-0.5))*ellipse((0,0.55), 1.7, 0.3), gray(0.75));

// Draw subshapes at (3,-0.15)
filldraw(shift((2.2,-0.15))*(((0,0)--(1.2,0)--(1.2,0.8)--(0,0.8)--cycle)^^((1.2,0)--(1.5,0.3)--(1.5,1.1)--(1.2,0.8)--cycle)^^
                           ((0,0.8)--(1.2,0.8)--(1.5,1.1)--(0.3,1.1)--cycle)),
        gray(0.9));

label(scale(0.78)*"$445\,\textup{g}$", (2.78,0.25));//, (0.5,0.3), UnFill);
