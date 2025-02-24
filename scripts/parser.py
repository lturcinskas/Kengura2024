import os
import fileinput
from utils import *
from constants import *

cmd = 'cd ../kengura%s/official && convmv --lower * --notest' % (year)
os.system(cmd)
cmd = 'cd ../kengura%s/official/sources-tex && convmv --lower * --notest' % (year)
os.system(cmd)
#for gr in groupfull_dict:
#    Gr = gr.capitalize()
#    cmd = 'cd ../kengura%s/official/%s && convmv --lower * --notest' % (year, Gr)
#    os.system(cmd)

cmd = 'mkdir ../kengura%s/salygos' % (year)
os.system(cmd)

#for gr in ['student']:
for gr, num in groupfull:
    probs_fn = '%s-finalized.tex' % (gr)
    cmd = 'mkdir ../kengura%s/%s' % (year, gr)
    os.system(cmd)
    cmd = 'cp ../kengura%s/official/sources-tex/%s ../kengura%s/%s/' % (year, probs_fn, year, gr)
    os.system(cmd)
    cmd = 'mkdir ../kengura%s/%s/images' % (year, gr)
    os.system(cmd)
    
    #read the official kengura file and separate out the problems
    #megalist = list(fileinput.input())
    f = open("../kengura%s/%s/%s" % (year, gr, probs_fn), "r")
    megalist = f.read().split('\n')
    #side pics
    side_pics = dict()
    for i in megalist:
        if i.startswith('\\NSidePictureEPS'):
            pic, rest = get_bracketed(i)
            rest, _ = get_bracketed(rest+'}')
            num, _ = get_bracketed(rest)
            side_pics[num] = pic
    megastring = ' '.join(megalist)
    probs = megastring.split('\\begin{document}')[1].split('\problemID')[1:]

    #get the group
    #groupfull = (os.getcwd().split('/'))[-1]
    group = gr[:1].upper()

    en_header=("\\documentclass[10pt,a4paper,twocolumn,landscape,oneside]{memoir}\n"
               "\\pdfoutput=1\n"
               "\\usepackage{../other/kengura}\n"
               "\\input{../salygos/%s}\n" #problems and answers
               "\\begin{document}\n"
               "\\greeting{en}{%d}\n"
                "\\pointsen{3}\n") % (gr, groupnumber[group])

    en_footer =("%%Put us somewhere\n"
                "\\goodbye\n"
                "\\pointsen{4}\n"
                "\\pointsen{5}\n"
                "\\end{document}\n") 

    problems_and_answers = open("../kengura%s/salygos/%s.tex" % (year, gr), 'w') #problems and answers
    en = open("../kengura%s/%s/" % (year, gr) + gr + "_enX.tex", 'w')

    #writeout headers
    en.write(en_header)

    #parse, format and writeout each problem
    for problem in probs:
        raw_content = parse_problem(problem, '../kengura%s/official/graphics-%s/' % (year, gr), '../kengura%s/%s/images/' % (year, gr), side_pics)

        problems_string = form_problems(raw_content, group)
        answers_string = form_answers(raw_content, group)
        en_string = form_en(raw_content, group)

        problems_and_answers.write(problems_string+answers_string)
        en.write(en_string)

    #writeout footers
    en.write(en_footer)
    en.close()
