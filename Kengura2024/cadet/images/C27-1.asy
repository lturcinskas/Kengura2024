import geometry;
settings.outformat="pdf";
settings.pdfviewer="/usr/bin/evince";
size(140);

real l = 0.7pt;

// Draw grid lines
for (int i = 0; i < 5; ++i) {
    draw((i, -0.4)--(i, 3.4), linewidth(0.6pt)+gray(0.5));
}

for (int j = 0; j < 4; ++j) {
    draw((-0.4, j)--(4.4, j), linewidth(0.6pt)+gray(0.5));
}

// Draw lines
draw((1,3)--(0,0)--(3,3)--(4,0)--cycle, linewidth(l));
draw((1,3)--(2,0)--(3,3), linewidth(l));


line l1 = line((0,0), (1,3));
line l2 = line((0,0), (3,3));
line l3 = line((2,0), (1,3));
line l4 = line((2,0), (3,3));
line l5 = line((4,0), (1,3));
line l6 = line((4,0), (3,3));

markangle(Label("$\alpha$", align=SSW), l2, l1, linewidth(2.1l));
markangle(Label("$\beta$", align=S), l4, l3, linewidth(2.1l));
markangle(Label("$\gamma$", align=SSE), l6, l5, linewidth(2.1l));



