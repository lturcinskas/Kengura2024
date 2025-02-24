from utils import N2T, groups, year
from utils import get_bracketed


def change_number(line, i):
    start = line.find('{')
    end = line.find('}')
    new = line[:start+1]+str(i+1)+line[end:]   
    return new 

   
def get_answers(prob, group):
    problem = "\\r" + prob
    f = open("../Kengura%s/salygos/%s.tex" % (year, group), 'r')
    all_f = f.read()
    start = all_f.find(problem)
    answer = get_bracketed(all_f[start-1:])[0]
    return answer


f = open("../Kengura%s/expert/problems.txt" % year, 'r')
Problems = []
for line in f:
    Problems.append(line[0]+N2T[line[1:-1]])
    #Answers.append('a'+line[0]+N2T[line[1:-1]])
f.close()
print(Problems)

inputs = []
grpath = "\\graphicspath{ "
for k in groups.keys():
    inputs.append('\\input{../salygos/%s}\n' % groups[k])
    grpath += '{../%s/images/}' % groups[k]
grpath += '}\n'


Languages = ['lt']
Answers = []
for lang in Languages:

    header=("\\documentclass[10pt,a4paper,oneside]{memoir}\n"
               "\\pdfoutput=1\n"
               "\\usepackage{../other/kengura}\n"+
               grpath+
               "".join(inputs)+
               "\\begin{document}\n"
               "\\greeting{%s}{7}\n"
               "\\vspace{10pt}\n"
               "\\newline" % lang) 
    footer = ("%%Put us somewhere\n"
                "\\pointslt{3}\n"
                "\\pointslt{4}\n"
                "\\pointslt{5}\n"
                "\\greeting{lt}{7}\n"
                "\\goodbye\n"
                "\\end{document}\n")

    expert = open('ekspertas_%s.tex' % lang, 'w')  # TODO: change directory from scripts
    expert.write(header)
    for i in range(len(Problems)):
        group = groups[Problems[i][0]]
        f = open('../Kengura%s/%s/%s_%s.tex' % (year, group, group, lang))
        for line in f:
            if line.find(Problems[i]) > 0:
                if line.find('\\'+Problems[i]) > 0: 
                    line = change_number(line, i)
                    #find_images(Problems[i], group)
                expert.write(line)
               # expert.write('\n \\bigskip\n')
        f.close()
        if lang == "lt":
            Answers.append(get_answers(Problems[i], group))
    expert.write(footer)

an_header=("\\documentclass[12pt,a4paper,oneside]{book}\n"
		"\\pdfoutput=1\n"
		"\\begin{document}\n" 
		"\\pagestyle{empty}\n"
		"\\chapter*{\centering Ekspertas}\n"
		"\\begin{center}\n"
		"\\vfill\n"
		"\\begin{tabular}[h]{c c}\n"
		"Nr. & Atsakymas\\\\\n"
		"\hline\n")
an_footer=("\\end{tabular}\n"
    "\\end{center}\n"
    "\\vfill\n"
    "\\end{document}")
ats = open("../Kengura%s/expert/ekspertas_atsakymai.tex" % year, 'w')  # TODO: change directory to answers
ats.write(an_header)
for i in range(len(Answers)):
    ats.write("%d & %s\\\\\n" % (i+1, Answers[i]))
ats.write(an_footer)
ats.close()
