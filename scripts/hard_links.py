import datetime
import os
from utils import groupfull, year

for gr, num in groupfull:
    for lng in ('en', 'lt', 'pl', 'ru'):
        #cmd = 'ln -f ./kengura%s/%s/build/%s_%s.pdf %s/%s_%s.pdf' % (year, gr, gr, lng, gr, gr, lng)
        date = datetime.date.today()
        cmd = 'ln -f ../kengura%s/out/%s_%s.pdf ../kengura%s/pdf/%s_%s_%s.pdf' % (year, gr, lng, year, gr, lng, date)
        #cmd = 'ln -f %s/%s_%s.pdf ../../../pdf/%s_%s.pdf' % (gr, gr, lng, gr, lng)
        os.system(cmd)
        #cmd = 'cp %s/%s_%s.ps ps/%s_%s.ps' % (gr, gr, lng, gr, lng)
        #os.system(cmd)
    #cmd = 'ln -f %s/%s_en.pdf pdf/%s_en.pdf' % (gr,gr, gr)
    #os.system(cmd)
    #cmd = 'ln -f %s/%s_lt.pdf pdf/%s_lt.pdf' % (gr,gr, gr)
    #os.system(cmd)
    #cmd = 'ln -f %s/%s_ru.pdf pdf/%s_ru.pdf' % (gr,gr, gr)
    #os.system(cmd)
    #cmd = 'ln -f %s/%s_pl.pdf pdf/%s_pl.pdf' % (gr,gr, gr)
    #os.system(cmd)
