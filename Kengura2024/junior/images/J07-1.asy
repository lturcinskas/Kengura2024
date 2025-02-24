import geometry;
settings.outformat="pdf";
settings.pdfviewer="/usr/bin/evince";
size(4cm);

filldraw((0,0)--(4,0)--(4,4)--(0,4)--cycle, gray(0.6));
filldraw(circle((1,3),1), white);
filldraw(circle((3,3),1), white);
filldraw(circle((1,1),1), white);
filldraw(circle((3,1),1), white);

path quarterCircle(pair center, real r, real start, real end)
{
    return shift(center)*scale(r)*arc((0,0),1,start,end);
}

filldraw(quarterCircle((1,1),1,0,90)--quarterCircle((1,3),1,-90,0)--
         quarterCircle((3,3),1,-180,-90)--quarterCircle((3,1),1,-270,-180)--cycle, black);
