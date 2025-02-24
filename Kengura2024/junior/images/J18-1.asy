settings.outformat="pdf";
settings.pdfviewer="/usr/bin/evince";
size(105);
//unitsize(3.5mm);
real dotsize = 0.75;
real g = 0.55;

pair A = (0, 3);
pair B = (3, 9);
pair C = (6, 9);
pair D = (9, 3);
pair Ee = (3, 0);
pair F = (6, 0);
pair G = (0, 6);
pair H = (3, 6);
pair I = (6, 6);
pair J = (9, 6);
pair K = (6, 3);
pair L = (3, 3);

draw(A--D--J--G--cycle);
draw(Ee--F--C--B--cycle);


filldraw(circle(B, dotsize), gray(g));
filldraw(circle(C, dotsize), gray(g));
filldraw(circle(K, dotsize), white);
filldraw(circle(H, dotsize), white);
filldraw(circle(I, dotsize), white);
filldraw(circle(J, dotsize), gray(g));
filldraw(circle(G, dotsize), gray(g));
filldraw(circle(L, dotsize), white);
filldraw(circle(A, dotsize), gray(g));
filldraw(circle(D, dotsize), gray(g));
filldraw(circle(Ee, dotsize), gray(g));
filldraw(circle(F, dotsize), gray(g));


label("$10$", (B + I)/2);
label("$4$", (G + L)/2);
label("$12$", (H + K)/2);
label("$6$", (I + D)/2);
label("$24$", (L + F)/2);
