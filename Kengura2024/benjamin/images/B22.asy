import geometry;
settings.outformat="pdf";
settings.pdfviewer="/usr/bin/evince";
size(150);

real r = 0.45;
//real arrowScaleFactor = 1.4;
//real arrowSizeFactor = 1.5;

// Draw rectangles
draw((0,0)--(10,0)--(10,4)--(0,4)--cycle);
draw((10,0)--(16,0)--(16,8)--(10,8)--cycle);
draw((0,4)--(5,4)--(5,13)--(0,13)--cycle);
filldraw((5,4)--(10,4)--(10,8)--(5,8)--cycle, lightgray);

// Label areas
label("$40$ cm$^2$", (5,2));
label("$48$ cm$^2$", (13,4));
label(rotate(90)*"$45$ cm$^2$", (2.5,8.5));
label("\large\textbf{?}", (7.5,6));

// Draw axes with ticks and labels
draw((0,-r)--(16,-r), arrow=Arrows(TeXHead), L=Label("$16$ cm", position=MidPoint));
draw((-r,0)--(-r,13), arrow=Arrows(TeXHead), L=Label("$13$ cm", position=MidPoint, W));
draw((0,13+r)--(5,13+r), arrow=Arrows(TeXHead), L=Label("$5$ cm", position=MidPoint, N));
