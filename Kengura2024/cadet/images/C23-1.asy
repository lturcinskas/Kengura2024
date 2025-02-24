import geometry;
settings.outformat="pdf";
settings.pdfviewer="/usr/bin/evince";
size(200);

pair O = origin;
pair A = (36,10);

draw(box(O,A));
draw(arc((10,0),10,0,180));
draw(arc((25,0),5,0,180));
draw(arc((33,0),3,0,180));

arrowbar ar = ArcArrows();
draw((0,-1) -- (36,-1), arrow=ar,
	 L=Label("$36\ \textup{cm}$", position=MidPoint, S));
draw((25,5) -- (25,10), arrow=ar,
L=rotate(90)*Label("$5\ \textup{cm}$", position=MidPoint));
draw((33,3) -- (33,10), arrow=ar,
L=rotate(90)*Label("$7\ \textup{cm}$", position=MidPoint));