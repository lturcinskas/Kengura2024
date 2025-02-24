import os
import sys
from constants import *
from utils import get_problems


if len(sys.argv) > 1:
    groupfull = sys.argv[1]
    os.chdir("../Kengura%s/%s" % (year, groupfull))
else:
    groupfull = (os.getcwd().split('/'))[-1]

try:
    en = open(groupfull + "_en.tex", 'r')
except IOError:
    en = open(groupfull + "_en.tex", 'r')

# Do easy ones
lt = open(groupfull + "_lt.texX", 'w')
ru = open(groupfull + "_ru.texX", 'w')
pl = open(groupfull + "_pl.texX", 'w')

text = en.read()
text_lt = text[:]
text_ru = text[:]
text_pl = text[:]

text_lt = text_lt.replace("EN", "LT")
text_lt = text_lt.replace("pointsen", "pointslt")
text_lt = text_lt.replace("greeting{en}", "greeting{lt}")

text_ru = text_ru.replace("EN", "RU")
text_ru = text_ru.replace("pointsen", "pointsru")
text_ru = text_ru.replace("greeting{en}", "greeting{ru}")

text_pl = text_pl.replace("EN", "PL")
text_pl = text_pl.replace("pointsen", "pointspl")
text_pl = text_pl.replace("greeting{en}", "greeting{pl}")

ru.write(text_ru)
pl.write(text_pl)
lt.write(text_lt)

lt.close()
ru.close()
pl.close()

# Do hard one
# _all = open(groupfull + "_all.tex", 'w') #Jei reiketu versijos be atsakymu
_all_a = open(groupfull + "_all_with_answers.tex", 'w')

group = groupfull[:1].upper()

all_header = ("\\documentclass[10pt,a4paper,oneside]{memoir}\n"
              "\\pdfoutput=1\n"
              "\\usepackage{../other/kengura}\n"
              "\\input{../salygos/%s}\n"
              "\\begin{document}\n") % groupfull

all_footer = "\\end{document}"

# _all.write(all_header)
_all_a.write(all_header)

problems = get_problems(text)
# print(problems)
for i in range(1, Prob_number[groupfull] + 1):
    for number, problem in problems:
        print(number, problem)
        if str(i) == number:
            _all_a.write("\\vbox{\n"
                         "\\hspace{2cm} Atsakymas: \\r%s%s "
                         "\\hfill \\textbf{%s %s}\n\n"
                         "%s\n\n\\bigskip"
                         "%s\n\n\\bigskip"
                         "%s\n\n\\bigskip"
                         "%s\n\n\\bigskip"
                         "}\n\\newpage\n" % (group, N2T[number],
                                             EN2LT[groupfull].upper(), year,
                                             problem,
                                             problem.replace("EN", "LT"),
                                             problem.replace("EN", "PL"),
                                             problem.replace("EN", "RU")))
    # _all.write("\\vbox{\n"
    #           "%s\n\n\\bigskip"
    #           "%s\n\n\\bigskip"
    #           "%s\n\n\\bigskip"
    #           "%s\n\n\\bigskip"
    #           "}\n\\newpage\n" % (problem, 
    #                    problem.replace("EN", "LT"),
    #                    problem.replace("EN", "PL"), 
    #                    problem.replace("EN", "RU")) )

# _all.write(all_footer)
_all_a.write(all_footer)

_all_a.close()
