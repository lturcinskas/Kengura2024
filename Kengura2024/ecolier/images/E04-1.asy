import geometry;
settings.outformat="pdf";
settings.pdfviewer="/usr/bin/evince";
size(110);

real R = 1;

draw(circle((0,0), 1));

for (int na = 1; na <= 11; ++na) {
    real angle = 285 - na * 360 / 11;
    pair point = R * dir(angle);
    
    label("$" + string(na) + "$", point, point);
    dot(point);
    
    if (na == 1 || na == 4 || na == 7) {
    real j = na+3;
    real anglej = 285 - j * 360 / 11;
    pair pointj = R * dir(anglej);
    path p = point -- pointj;
    draw(subpath(p,0.1,0.9), Arrow);
    } else {}
}

//draw((1*dir(),0) -- (4,0), Arrow);
//draw((4,0) -- (7,0), Arrow);
