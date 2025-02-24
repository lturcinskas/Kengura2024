# -*- coding: utf-8 -*-
import os
import re
from utils import groupfull, year, N2T, get_bracketed


os.chdir("../Kengura%s/answers" % (year))
ats = open("atsakymai.csv", 'w')

for gr, num in groupfull:
    prob = open("../salygos/%s.tex" % gr, 'r')
    text = prob.read()
    group = gr[:1].upper()
    ats.write(gr)
    for number in range(1, num+1):
        cm = "\\r%s%s" % (group, N2T[str(number)])
        letter = get_bracketed(text[text.find(cm):])[0]
        ats.write(","+letter)
    for number in range(num+1, 31):
        ats.write(",")
    ats.write("\n")

# expert
answers = open("expert_answers.tex", 'r')
text = answers.read()
pattern = r'\d+\s+&\s+([A-E])\\'
matches = re.findall(pattern, text)
ats.write("expert,")
ats.write(",".join(matches))

ats.close()

