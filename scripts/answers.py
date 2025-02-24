# -*- coding: utf-8 -*-
import os
from constants import *

all_footer=("\\end{tabular}\n"
    "\\end{center}\n"
    "\\vfill\n"
    "\\end{document}")

os.chdir("../kengura%s/answers" % (year))
for gr, num in groupfull:
    all_header=("\\documentclass[12pt,a4paper,oneside]{book}\n"
		"\\pdfoutput=1\n"
		"\\input{../salygos/%s}\n"
		"\\begin{document}\n" 
        "\\chapter*{\\centering Atsakymai}\n"
		"\\thispagestyle{empty}\n"
		"\\vfill\n"
		"\\begin{center}\n"
		"\\begin{tabular}[h]{c c}\n"
		"Uždavinio  nr. & Atsakymas \\\\\n"
		"\hline\n" % (gr))
    group = gr[:1].upper()
    ats = open(gr + "_answers.tex", 'w')
    ats.write(all_header)
    for number in range(1, num+1):
      ats.write("%d & \\r%s%s\\\\\n\n" % (number, group, N2T[str(number)]))
      if 3*number == Prob_number[gr]:
          ats.write("\hline\n")
      if 3*number == 2*Prob_number[gr]:
          ats.write("\hline\n")
    ats.write(all_footer)
    ats.close()
    cmd = 'pdflatex %s_answers.tex' % gr
    os.system(cmd)
