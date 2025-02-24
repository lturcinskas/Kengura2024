import geometry;
settings.outformat="pdf";
settings.pdfviewer="/usr/bin/evince";
size(90);

real b = 13;
real a = 9;
real c = (b*b-a*a)/a;
//real d = sqrt((a+b)*(a+b)+c*c);

draw((0,0)--(2a+b+c,0));
draw(box((0,0), (b,b)));
draw(box((0,b), (a,b+a)));
draw((a,b+a)--(a+c,0)--(a+c+a+b,c)--(a+a+b,a+b+c)--cycle);
draw(box((a+b+a+c,0), (a+b+a+c+c,c)));

label("$b$",(0,b/2), W);
label("$a$",(0,b+a/2), W);
label("$c$",(2a+b+2c,c/2), E);