import os
from constants import year, groupfull
import datetime

for gr, num in groupfull[:1]:
    os.chdir("../kengura%s/%s" % (year, gr))
    out_path = "../pdf/"
    date = datetime.datetime.now()
    cmd = f"pdflatex {gr}_en.tex -synctex=1 - interaction=nonstopmode -output-directory='{out_path}{gr}_en_{date}.pdf'"
    # cmd = f'pdflatex {gr}_en.tex ../pdf/{gr}_en_{date}.pdf'
    print(cmd)
    # os.system(cmd)
    # cmd = 'pdflatex %s_lt.tex' % gr
    # os.system(cmd)
    # cmd = 'pdflatex %s_ru.tex' % gr
    # os.system(cmd)
    # cmd = 'pdflatex %s_pl.tex' % gr
    # os.system(cmd)
    #cmd = 'pdf2ps build/%s_en.pdf' % gr
    #os.system(cmd)
    #cmd = 'pdf2ps build/%s_lt.pdf' % gr
    #os.system(cmd)
    #cmd = 'pdf2ps build/%s_ru.pdf' % gr
    #os.system(cmd)
    #cmd = 'pdf2ps build/%s_pl.pdf' % gr
    #os.system(cmd)
    os.chdir("../")
