import os
from constants import groupfull, year

for gr, num in groupfull:
    os.chdir("../kengura%s/%s" % (year, gr))
    cmd = 'pdflatex %s_all_with_answers.tex' % gr
    os.system(cmd)
    cmd = 'ln -f build/%s_all_with_answers.pdf %s_all_with_answers.pdf' % (gr, gr)
    os.system(cmd)
    cmd = 'ln -f build/%s_all_with_answers.pdf ../pdf/%s_all_with_answers.pdf' % (gr, gr)
    os.system(cmd)
    os.chdir("../")
