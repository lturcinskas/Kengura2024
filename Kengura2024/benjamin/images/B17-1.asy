import geometry;
settings.outformat="pdf";
settings.pdfviewer="/usr/bin/evince";
size(80);

int rows = 4;
int cols = 4;
string[] n = {"1","3","2","2"};
string[][] n = {
{"1","3","2","2"},
{"2","3","4","2"},
{"4","4","3","3"},
{"1","3","2","0"}
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