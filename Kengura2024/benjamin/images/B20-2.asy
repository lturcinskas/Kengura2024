import geometry;
settings.outformat="pdf";
settings.pdfviewer="/usr/bin/evince";
size(90);

int size = 14;
int circleRadius = 1;

// Draw circles
for (int i = 1; i <= size; i += 4) {
    for (int j = 1; j <= size; j += 4) {
        draw(circle((i, j), circleRadius));
    }
}

// Fill a circle
filldraw(circle((1, 1), circleRadius), gray(0.65));

// Labels and arrows
label("$3$", (9, 9));
label("$<$", (7, 9));
label(rotate(90)*"$<$", (9, 7));
label("$>$", (11, 9));
label(rotate(270)*"$<$", (9, 11));
label(rotate(90)*"$<$", (13, 7));
