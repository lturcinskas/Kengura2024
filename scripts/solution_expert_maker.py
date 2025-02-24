import fileinput 
import os
from constants import year, N2T, groups, problems

PARTICIPANTS = 37500
DATE = "kovo 15"

def get_problems(text):
    problems = []
    #print(text)
    while get_first_token(text):
        token = get_first_token(text)
        piece, text, number = separate_first_piece(text, token)
        if token != '\\kvoid':
            problems.append([number,piece])
        else:
            problems[-1][1] = problems[-1][1]+ piece
            print(problems[-1])
    return problems

def get_first_token(text):
    tex = text.find("\\ktext")
    pic = text.find("\\kpic")
    void = text.find("\\kvoid")
    if tex+pic+void == -3:
        return None
    else:
        l = [(score(tex), '\\ktext'), (score(pic), '\\kpic'), (score(void), '\\kvoid')]
        return min(l)[1]

def score(number):
    if number == -1:
        return 10000
    else:
        return number

def separate_first_piece(text, token):
    start = text.find(token)
    text = text[start:]
    pro = ""
    cycles = {"\\ktext": 2, "\\kpic": 5, "\\kvoid": 1}
    for i in range(cycles[token]):
        a, text = get_bracketed(text)
        pro += '{'+a+'}'
        if i == 0:
            number =  a
    return token+pro, text, number


def get_bracketed(string, op = '{', cl = '}'):
    if string[0] != op:
        start = string.find(op)
        #print "Loosing" + string[:start+1],
        string = string[start+1:]
    else:
        string = string[1:]

    if cl not in string:
        print("Aborting, misformatted string")
        return 

    level = 1
    position = 0
    while level > 0:
        if string[position] == op:
            level += 1
        if string[position] == cl:
            level -= 1
        position += 1
    return string[:position-1], string[position:]

#Expert
input_f = open("../kengura%d/expert/ekspertas.tex" %(year))
answers_f = open("../kengura%d/expert/problems.txt" %(year))
#answers_f = open("../kengura%d/expert.tex" %(year))
output_f = open("spExXXX.tex", 'w')


header=("\\documentclass[12pt,a4paper, openany]{memoir}\n"
          "\\pdfoutput=1\n"
          "\\usepackage{sprendimai}\n"
          "\\input{../kengura%d/preecolier}\n"
          "\\input{../kengura%d/ecolier}\n"
          "\\input{../kengura%d/benjamin}\n"
          "\\input{../kengura%d/cadet}\n"
          "\\input{../kengura%d/junior}\n"
          "\\input{../kengura%d/student}\n"
          "\\graphicspath{{../kengura%d/preecolier/images/}{./images/}\n"
          "{../kengura%d/ecolier/images/}\n"
          "{../kengura%d/benjamin/images/}\n"
          "{../kengura%d/cadet/images/}\n"
          "{../kengura%d/junior/images/}\n"
          "{../kengura%d/student/images/}}\n"
          "\\begin{document}\n"
          "%%\\includepdf[fitpaper=true]{cover/coverEx}\n"
          "\\titlepage{}{} %% Autorius, redaktorius\n"
          "\\tableofcontents*\n"
          "\\pratarmeE\n"
          "\\setlength{\parindent}{0pt} \setlength{\parskip}{0pt}\n"
          "%%\\cftaddtitleline{toc}{chapter}{Geriausiųjų sąrašas}{6}\n"
          "%%\\bestof{Ex}{.95} %% Grupė, klasė, trumpinys, spacing\n"
          "\\chapter[Sąlygos]{%d m. \emph{Eksperto} užduočių sąlygos}\n"
          "\\thispagestyle{empty}\n") % (year,year,year,year,year,year, year,year,year,year,year,year, year) 

footer = ("\\end{document}")
middle = ("\\chapter[Užduočių sprendimai]{\emph{Eksperto} užduočių sprendimai}\n")

output_f.write(header)
all_input = input_f.read()
all_answers = answers_f.read().split('\n')
Problems = get_problems(all_input)

output_f.write("\n\\pointslt{3}\n\n")
for i in range(0, 30):
    if (i) == 10:
        output_f.write("\\bigskip\n\n\\pointslt{4}\n\n")
    if (i) == 20:
        output_f.write("\\bigskip\n\n\\pointslt{5}\n\n")
    num, s = Problems[i]
    output_f.write('\\bigskip\n' + s + '\n')
output_f.write(middle)
for i in range(0, 30):
    gr = all_answers[i][0]
    num = all_answers[i][1:]
    input_s = open("sp%s.tex" % gr, 'r')
    solutions = input_s.read()
    start_s = solutions.find("\chapter[Užduočių sprendimai]")
    start = solutions.find("\s{%s}" % num, start_s)+3+len(num)
    if num == str(problems[gr]):
        end = solutions.find("\\includepdf{../kengura", start)
    else:
        end = solutions.find("\s{", start)
    input_s.close()
    #print("\s{" + str(i+1) + "}" + solutions[start:end])
    output_f.write("\s{" + str(i+1) + solutions[start:end])

output_f.write("\\vfill\n\\includepdf{../kengura%s/%s_answers}\n" % (year, groups[gr]))

output_f.write("\\vfill\n\\includepdf{../kengura%s/expert/expert_answers}\n" % (year))
output_f.write(footer)
input_f.close()
output_f.close()
