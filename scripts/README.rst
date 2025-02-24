Jums reikės
===========

- Kengūros oficialių tex ir paveikslėlių failų, kurie būna patalpinami į
  kengūros vidinę svetainę prieš Kalėdas.

- Šios programinės įrangos (2014 metų sąrašas, OS - Mint Debian)
  dos2unix, convmv, python2.7, asymptote, inkscape, git, epstopdf, iconv, 
  texlive, texlive-lang-lithuanian, texlive-lang-polish, texlive-lang-cyrillic,
  texlive-fonts-extra texlive-latex-extra  lmodern

- Lenkiškų ir baltarusiškų sąlygų, lietuviškų vertimų.

Pirmas žingsnis - automatinis gėris
===================================
  
- Oficialūs tex ir paveiksliukų failai yra viename kataloge. Pavadiname jį
  official ir paveiksliukus sukeliame į subkatalogą images (2022 metais nedariau paveiksliukų perkėlimo į images, tai skriptas parašytas tiems folderių pavadinimams, kokie buvo 2022).
  
- Iš ankstesnių metų nukopijuojame folderį other

- folderyje scripts randame failą 'constants.py' ir pakeičiame metus (year) į konkurso metus.

- Paleidžiame iš scripts folderio failą parser.py su python2.7. Jis:
    - sukuria katalogus kiekvienai grupei, į jas nukopijuoja oficialių sąlygų failą (vėliau nenaudojamas).
    - į kiekvienos grupės images folderį sukopijuoja paveiksliukus
        - Skriptas įterpiamų paveikslėlių dydį nustato pagal pdf failo bounding box.
            Jei oficialus paveikslėlis turi tik .png versiją, skriptas pats iš jo padaro .pdf versiją
            naudodamas komandą convert -quality 100 sample.png sample.pdf
    - išparsina oficialias sąlygas, surašo sąlygų failus į folderį salygos
    - sukuria angliškų sąlygų maketą.
	
(ko nedaro: kažkaip kitaip elgiasi su paveiksliukais, netvarko sąlygų failo eilučių pabaigų(?), Kaip yra su bounding_box magija ir .png vertimu į .pdf?)
(- Išmetami lauk netikę paveikslėlių formatai. Aš nenaudoju .crd, .eps, .pst) !šito neatlieka
(- Visi failai pervadinami mažosiomis raidėmis: convmv --lower * --notest)

- Sekmės atveju, parser.py kiekvienai grupei sugeneruoja failus benjamin.tex (folderyje sąlygos) ir benjamin_enX.tex. Pastarąjį reikia pervadinti
  ištrinant X.

- benjamin_en.tex turėtų iš karto kompiliuotis, į rezultatą labai dėmesio
  kreipti kol kas neverta.

Antras žingsnis - sąlygų kopijavimas
====================================

Bent keli oficialūs uždaviniai dažniausiai būna pakeičiami, tad verta pradėti
nuo galutinio uždavinių rinkinio suderinimo. Tą geriausia pildant
benjamin_problems.tex ir benjamin_answers.tex:

- Atsidaromas su gedit ar pluma benjamin_problems.tex failas. Į jį kopijuojami
  vertimai (naudojant middle click, prašom už hint'ą) ir kartu pakeičiamos
  kelios angliškos sąlygos kitomis. Jei keičiant anglišką sąlygą keičiasi ir
  uždavinio vaizdavimo tipas (su paveikslėliu -> be paveikslėlio), atitinkamai
  pakeičiamas ir benjamin_en.tex failas.

- Lenkai savo sąlygas yra užkodavę Windows-1250, tad reikia konvertuoti
        iconv -f WINDOWS-1250 -t utf8 b_2014.tex > ub_2014.tex

- Baltarusiai savo sąlygas atsiunčia wordu (lol), tad reikia atidžiai kopijuoti,
  nes formulės nesikopijuoja.

Trečias žingsnis - pirmasis iliustracijų perpiešimas
====================================================

Jau pačioje pradžioje būna aišku, kurias iliustracijas reikia perdaryti. (Pvz.
2014 perdariau ar pataisiau 9 preecolier, 9 ecolier, 5 benjamin, 6 cadet, 6
junior ir 5 student iliustracijas, maždaug 2/3 visų.) Dažniausiai reikia
nupiešti naują nuo nulio (dėl vieningo stiliaus, ypač geometrija su asy), bet
kartais pavyksta pataisyti ir turimą. Keli hint'ai:

- Kataloge templates yra .tex, .asy ir inkscape šablonai. Tex automatiškai
  kompiliuosis į pdf, asy reikia kompiliuoti su vėliava -f pdf, inkscape reikia
  exportinti į pdf. Kuo daugiau pdf, tuo mažiau galvos skausmo. BET, su git
  kartais išsaugojus į pdf spausdina juodą blob'ą. Tuomet reikia naudoti .png.
  Jis renderinasi ekrane lievai, bet spausdinasi gerai.

- Naujus piešinėlius geriausia vadinti prasmingai, pavyzdžiui p27.pdf. Jei
  daromi keturkalbiai paveikslėliai, juos reikia vadinti p27EN.pdf, p27LT.pdf ir
  t.t., tuomet make_all.py sėkmingai pakeis pavaidinimus.

- Naudojant .png ir darant nuo nulio, geriau nepagailėti pixelių ir scalinti jau
  po to su tex'u. Gaunasi daug gražiau, nei iš karto daryti finalinį dydį.

- Spalvotus .svg paverst į grayscale:
    inkscape -f inputfile.svg --verb EditSelectAll --verb org.inkscape.color.desaturate.noprefs --verb FileSave --verb FileQuit

-Spalvotus .pdf paverst į grayscale:
    gs -sOutputFile=output.pdf -sDEVICE=pdfwrite -sColorConversionStrategy=Gray -dProcessColorModel=/DeviceGray -dCompatibilityLevel=1.4 -dAutoRotatePage=/None -dNOPAUSE -dBATCH input.pdf 

-Spalvotus .png paverst į grayscale:
    convert -type Grayscale input-picture.png output-picture.png

Ketvirtas žingsnis - maketavimas
================================

Turint anglišką sąlygų rinkinį ir paveikslėlius galima maketuoti
benjamin_en.tex. Įrankiai ir triukai:

- ktext ir kpic turi versijas be \vfill gale: ktextnofill, kpicnofill

- kpic turi parametrą [laužtiniuose skliausteliuose], kuris paveikslėlį kilnoja
  aukštyn žemyn. Pirmasis {parametras} yra paveikslėlio pavadinimas, {antrasis}
  jo plotis (tuo pačiu ir nustato, kiek pločio palikti tekstui), {trečiasis}
  scale (scalin'a viską automatiškai, labai patogu naudoti). 

- kvoid naudojamas, kai atsakymai netelpa teksto ertmėje dėl didelio kpic
  paveikslėlio. Tada jie išimami iš kpic ir su kvoid įdedami apačioje

- Tarpai tarp uždavinių ir bet ko kito reguliuomi su \vspace{10pt} ir ypač su
  \vspace{-5pt}. Vietos dažniausiai trūksta, tad neigiami tarpai yra lobis.

- Jei reikia priversti uždavinius likti viename lape, jie dedami į \vbox{}, bet
  jis sumažina viršutinę paraštę. Geriausia jį naudoti pradžiai, kad pažiūrėti,
  kur ką galima sugrūsti, o sėkmingai sugrūdus, nuimti.

- Sunkiausias triukas - jei paveikslėlis kreivas, ir reikia užleisti tekstą ant
  jo dalies, arba jei paveikslėlis žemas ir ilgas, ir reikia pakišti tekstą po
  juo, naudojamas \parshape, kuris dedamas į minipage. 2014 metais šitas
  naudojama ecolier 19 uždavinyje, pažiūrėkite, kaip atrodo. Hint - kai tekstas
  yra parshape, o parshepas minipage, viskas veikia gana neįprastai (pvz. kpic
  dydžio parametras) tad gali būti sunku suprasti, kodėl kažkas nedaro kažko.

- Baigus maketuoti benjamin_en.tex, iš scripts folderio paleidžiamas script'as
  makeall.py su parametru benjamin. Jis sugeneruoja failus
  benjamin_lt\ru\pl\allX.tex bei failą bejamin_all_with_answers.tex. Pastarąjį
  sukompiliavus galima siųsti pirmai redakcijai. Pirmuosius reikia pervadinti
  ištrinant X ir pakoreguoti maketą. Paprastai po pirmų redakcijų gali nemažai
  pasikeisti maketas.

Penktas žingsnis - didžiosios korekcijos
========================================

- Perpiešiamos reikiamos iliustracijos.
  
- Koreguojamas sąlygų ir atsakymų tekstas failuose benjamin.tex

Trečias žingsnis - baigiamosios kritinės korekcijos
===================================================

- Taisomos sąlygos, taisomos sąlygos, taisomos sąlygos. Paskutinę sekundę kas
  nors sugalvoja kokią radikalią nesąmonę, tada vykdoma radikali nesąmonė ir
  pridaroma naujų klaidų.
  
- Suvedami atsakymai. Atsakymų failus generuoja answers.py ir answers_csv.py

- Prireikus visus maketus kompiliuoja compile_all.py

- Dar gali būt patogu turėti visų maketų kopijas viename kataloge, jas galima
  sukurti su hard_links.py

Algoritmo išdėstymas laike
==========================

Sausio 4 savaitė
----------------
	Visi išverčia visas sąlygas ir susiunčia/suneša man. Juozas surašo sąlygas ranka. Marytė surašo į word'o failą.

Vasario 1 savaitė
-----------------
	Suvedu visus tekstus, padarau visus maketus (pirmas žingsnis)

Vasario 2 savaitė
-----------------
	Juozas ir visi redaguoja kalbą, taisomi paveikslėliai (antras žingsnis)

Vasario 3 savaitė
-----------------
	Kritinis dvigubas peržiūrėjimas ir persprendimas (trečias žingsnis)
	
Kažkada prieš konkursą
-----------------
    Surašomi atsakymai, spaustuvėj patikrinami maketai.
    
Kažkada po konkurso
-----------------
    Visi surašo sprendimus, susiunčia man, daromi paveiksliukai, redaguojama kalba.
	

Atsitiktinės pastabos
=====================

Raidžių bounding box dydis 120pt
Teksto ilgis (parshape'ui) apie 378pt
Asymptotė padaro truputį per didelius piešinius (šrifto dydis), tad jos
generuotus pdf reikia įdėti su .9 ar .85 scale'u.
