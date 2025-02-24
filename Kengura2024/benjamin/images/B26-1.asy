import geometry;
settings.outformat="pdf";
settings.pdfviewer="/usr/bin/evince";
size(100);

real a=85;
real b=116;
real c=18;
real d=78;

pair A = (0,0);
pair B = (b,0);
pair C = (0,a);
pair D = (b,a);
pair Ee = (d,-c);
pair F = (b-d,c);
pair G = (d,a-c);
pair H = (b-d,a+c);

pair[] vertices = {A,B,C,D,Ee,F,G,H};

draw(A--Ee--G--C--cycle);
draw(Ee--B--D--H--C);
draw(D--G);
draw(A--F--B, dashed);
draw(F--H, dashed);

for (pair vertice : vertices) {
filldraw(circle(vertice, 10), lightgray);
}


label("$7$", D);
label("$8$", Ee);
label("$\textbf{?}$", A);
label("$6$", F);
