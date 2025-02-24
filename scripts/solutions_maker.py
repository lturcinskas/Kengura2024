#!/usr/bin/python
# -*- coding: UTF-8 -*-

import fileinput 
import os
from constants import N2T, groups, translations, translations_o, kclass, time, problems, answers
from utils import get_bracketed

YEAR = 2024
PARTICIPANTS = 30300
DATE = "kovo 21"

def get_problems(text):
    problems = []
    while get_first_token(text):
        token = get_first_token(text)
        piece, text, number = separate_first_piece(text, token)
        if token != '\\kvoid':
            problems.append([number,piece])
        else:
            problems[-1][1] = problems[-1][1] + '\n' + piece
            print (problems[-1])
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
    number = 0
    for i in range(cycles[token]):
        a, text = get_bracketed(text)
        pro += '{'+a+'}'
        if i == 0:
            number = a
    return token+pro, text, number


def find_right_answer(st, text):
    sta = "r" + st
    start_f = text.find(sta)
    start = text[start_f:].find("{")
    a_letter = text[start+start_f+1:start+start_f+2]
    try:
        n = answers[a_letter]
    except KeyError:
        print(gr)
        print(st)
        print(sta)
        print(start_f)
        print(text[start+start_f+1:start+start_f+30])
        gr2 = text[start+start_f+3]
        answers_f2 = open("../Kengura%d/salygos/%s.tex" %(YEAR, groups[gr2]))
        text2 = answers_f2.read()
        answers_f2.close()
        st2 = text[start+start_f+3:start+start_f+text[start+start_f:].find("}")]
        return find_right_answer(st2, text2)
    sta = "a" + st
    start_f = text.find(sta)
    if text.find(sta+"LT")>0:
        start_f = text.find(sta+"LT")
    start = text[start_f:].find("{")
    start_f = start_f+start+1
    if text[start_f:start_f+9] == '\\granswer':
        if text[start_f+9] == '[':
            scale = text[start_f+10:start_f+text[start_f:].find(']')]
        else:
            scale = '1'
        pic_an_op = '\\includegraphics[scale = %s]{' % (scale)
        pic_an_cl = '}'
    else:
        pic_an_op = ''
        pic_an_cl = ''
    rest = text[start_f:]
    for j in range(n):
        answer, rest = get_bracketed(rest)
    return a_letter, pic_an_op + answer + pic_an_cl


for gr in groups.keys():
    input_f = open("../Kengura%d/%s/%s_lt.tex" %(YEAR, groups[gr], groups[gr]))
    answers_f = open("../Kengura%d/salygos/%s.tex" %(YEAR, groups[gr]))
    output_f = open("../Kengura%d/sprendimai/sp%sXXX.tex" % (YEAR, gr), 'w')


    header=("\\documentclass[12pt,a4paper, openany]{memoir}\n"
              "\\pdfoutput=1\n"
              "\\usepackage{../other/sprendimai}\n"
              "\\input{../salygos/%s}\n"
              "\\graphicspath{{../%s/images/}{../%s/images/build/}{./images/}{../other}}\n"
              "\\begin{document}\n"
              "%%\\includepdf[fitpaper=true]{cover/cover%s}\n"
              "\\titlepageS{%s}{}{%d}%%{} %% Autorius, redaktorius\n"
              "\\tableofcontents*\n"
              "\\pratarme{%d}{%s}{%s}{%s}{%s}{%d} %% Dalyvių sk, trukmė, data, klasė, grupė, metai\n"
              "\\setlength{\parindent}{0pt} \setlength{\parskip}{0pt}\n"
              "%%\\cftaddtitleline{toc}{chapter}{Geriausiųjų sąrašas}{6}\n"
              "%%\\bestof{\emph{%s}}{%s}{%s1}{.95} %% Grupė, klasė, trumpinys, spacing\n"
              "%%\\bestof{\emph{%s}}{%s}{%s2}{.95} %% Grupė, klasė, trumpinys, spacing\n"
              "%%\\kortele\n"
              "\\chapter[Sąlygos]{%d m. \emph{%s} užduočių sąlygos}\n"
              "\\thispagestyle{empty}\n") % (groups[gr], groups[gr], groups[gr],
                      gr, translations[gr], YEAR, PARTICIPANTS, time[gr], DATE, kclass[gr],
                      translations_o[gr], YEAR, translations[gr],
                      kclass[gr].split("--")[0], gr, translations[gr],
                      kclass[gr].split("--")[1], gr,  YEAR, translations_o[gr]) 

    footer = ("\\end{document}")
    middle = ("\\chapter[Užduočių sprendimai]{\emph{%s} užduočių sprendimai}\n") % translations_o[gr]

    output_f.write(header)
    all_input = input_f.read()
    all_answers = answers_f.read()
    Problems = get_problems(all_input)
    output_f.write("\n\\pointslt{3}\n\n")
    for i in range(1, problems[gr]+1):
        if (i-1)/problems[gr] == 1/3:
            output_f.write("\\bigskip\n\n\\pointslt{4}\n\n")
        if (i-1)/problems[gr] == 2/3:
            output_f.write("\\bigskip\n\n\\pointslt{5}\n\n")
        for num, s in Problems:
            if int(num)==i:
                output_f.write('\\bigskip\n' + s + '\n') 
    output_f.write(middle)
    for i in range(1, problems[gr]+1):
        st = gr +N2T[str(i)]
        an_letter, an = find_right_answer(st, all_answers)
        output_f.write("\\s{%d}{\\textbf{%s}}{%s}\n" % (i, an_letter, an) )
        output_f.write("\\stext{!}{}\n\n")
    
    output_f.write("\\vfill\n\\addcontentsline{toc}{chapter}{Atsakymai}\n\\includepdf{../answers/%s_answers}\n" % (groups[gr]))
    output_f.write(footer)
    input_f.close()
    output_f.close()
