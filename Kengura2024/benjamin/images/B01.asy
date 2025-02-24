import geometry;
settings.outformat="pdf";
settings.pdfviewer="/usr/bin/evince";
size(50);

filldraw(box((1,0), (9,3)), white); //02 03 04 06

//filldraw(box((2,0), (5,5)), lightgray); //01 02
//filldraw(box((3,0), (4,7)), darkgray); //01 02
//filldraw(box((7,0), (8,5)), gray); //01 02

filldraw(box((6,0), (7,7)), darkgray); //03 06
filldraw(box((5,0), (8,5)), lightgray); //03-06
//filldraw(box((6,0), (7,7)), darkgray); //04 05
//filldraw(box((2,0), (3,5)), gray); //03-05
filldraw(box((2,0), (3,7)), gray); //06

//filldraw(box((1,0), (9,3)), white); //01 05