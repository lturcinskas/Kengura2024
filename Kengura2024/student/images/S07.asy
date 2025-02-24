import geometry;
settings.outformat="pdf";
settings.pdfviewer="/usr/bin/evince";
size(80);

real xmin = 2.1, xmax = -2;
real ymin = 2.1, ymax = -2;
real t = 0.2;
path xtick = (0,t) -- (0,-t);
path ytick = (t,0) -- (-t,0);

//draw((-2,-1)--(1,2), linewidth(1pt)); //1
//draw((-1,2)--(2,-1), linewidth(1pt)); //2
//draw((-2,1)--(1,-2), linewidth(1pt)); //3
draw((-1,-2)--(2,1), linewidth(1pt)); //4
//draw((2,-2)--(-2,2), linewidth(1pt)); //5

arrowbar axisarrow = Arrow(TeXHead, 1.7);
Label xlabel = Label("$x$", position=EndPoint, S);
draw((xmin,0) -- (xmax,0), arrow=axisarrow, L=xlabel);
Label ylabel = Label("$y$", position=EndPoint, W);
Label onelabel = Label("$1$", position=EndPoint);
draw((0,ymin) -- (0,ymax), arrow = axisarrow, L=ylabel);
label("$O$",(0,0),SW); //1,2,4
//label("$O$",(0,0),NE); //3,5

draw(shift(-1,0)*xtick, L=onelabel);
draw(shift(1,0)*xtick);
draw(shift(0,-1)*ytick, L=Label("$1$", position=EndPoint, (-0.5,-0.1)));
draw(shift(0,1)*ytick);