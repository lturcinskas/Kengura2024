import geometry;
settings.outformat="pdf";
settings.pdfviewer="/usr/bin/evince";
size(60);

int rows = 3;
int cols = 3;
string[][] n = {
{"1","1","3"},
{"3","4","3"},
{"2","4","2"}
};


real hexagonSize = 1;
real dx = 1.5;
real dy = sqrt(3)/2;


for (int row = 0; row < rows; ++row) {
    for (int col = 0; col < cols; ++col) {
        pair center = (col*dx+row*1.5, col*dy-row*sqrt(3)/2);
        //-row*sqrt(3)/2,row*1.5
        filldraw(shift(center)*polygon(6), gray(0.75));
        label(n[row][col], center);
    }
}