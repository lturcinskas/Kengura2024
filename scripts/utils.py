import os
from constants import *

def bboxfinder(filename, source_path, output_path):
    # try:
    #     f = open(source_path+filename+'.pdf')
    #     cmd = 'cp %s/%s.pdf ./%s/%s.pdf' %(source_path, filename, output_path, filename)
    #     os.system(cmd)
    #     print ("found ", filename)
    # except IOError:
    #     print ('I will convert', filename)
    #     cmd = 'convert -quality 100 %s/%s.png ./%s/%s.pdf' %(source_path, filename, output_path, filename)
    #     os.system(cmd)
    #     filen = output_path + filename + '.pdf'
    #     path = os.getcwd() + '/' + filen
    #     f = open(path,'r')

    # for line in f:
    return 100
        # start = max( line.find('MediaBox'), line.find('BBox') )
        # if start > -1:
        #     dimensions, _ = get_bracketed(line[start:], '[', ']')
        #     return int(dimensions.split()[2].split('.')[0])+1

def get_bracketed(string, op='{', cl='}'):
    if string[0] != op:
        start = string.find(op)
        #print "Loosing" + string[:start+1],
        string = string[start+1:]
    else:
        string = string[1:]

    if cl not in string:
        print("Aborting, misformatted string:")
        print(string)
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
    
def parse_problem(problem, source_path, output_path, side_pics):
    number, problem = get_bracketed(problem)
    # print("number", number)
    # print("problem", problem)
    # problem = problem.split('\Problem')[1]
    number = number.split()[0]
    print("problem",problem)
    _, problem = get_bracketed(problem)
    print("problem",problem)
    _, problem = get_bracketed(problem)
    print("problem", problem)
    _, problem = get_bracketed(problem)
    print("problem", problem)
    _, problem = get_bracketed(problem)
    print("problem", problem)
    _, problem = get_bracketed(problem)
    print("problem", problem)
    text, problem = get_bracketed(problem)
    print("text", text)
    print("problem", problem)
    a1, problem = get_bracketed(problem)
    a2, problem = get_bracketed(problem)
    a3, problem = get_bracketed(problem)
    a4, problem = get_bracketed(problem)
    a5, problem = get_bracketed(problem)
    answer, problem = get_bracketed(problem)

    images, text = get_images(text)
    try:
        images.append(side_pics[number])
    except KeyError:
        pass
    for a in (a1, a2, a3, a4, a5):
        imgs, txt = get_images(a)
        widths = [bboxfinder(img, source_path, output_path) for img in imgs]
    widths = [bboxfinder(image, source_path, output_path) for image in images]
    answers = '{' + '}{'.join((a1, a2, a3, a4, a5)) + '}'
    text = ' '.join(text.split())

    return (number, text, answers, answer, images, widths)

def form_header(group, number):
    cnt = ("%%%s%s" % (group, number))
    spacer = "="#*(1 - int(number)/10)
    return cnt+spacer+30*"="+'['+int(number)*'='+(30-int(number))*'.'+']'+30*"="+spacer+cnt+"\n"

def form_problems(raw_data, group):
    print(raw_data)
    number, text, _, _, _, _ = raw_data
    head = form_header(group, number)
    number = N2T[number]
    en = "\def\\%s%sEN{%s}\n" % (group, number, text)
    lt = "\def\\%s%sLT{}\n" % (group, number)
    pl = "\def\\%s%sPL{}\n" % (group, number)
    ru = "\def\\%s%sRU{}\n" % (group, number)

    return head + en + lt + pl + ru + '\n'

def form_answers(raw_data, group):
    number, _, answers, answer, _, _ = raw_data
    #head = form_header(group, number)
    number = N2T[number]

    #guess if answer is language specific
    answer = "\def\\r%s%s{%s}\n" % (group, number, answer)
    if all(x not in answers for x in 'abcdefghijklmnoprstuvwxyz') or "includegraphics" in answers:
        return answer + "\def\\a%s%s{\\answer%s}\n\n" % (group, number, answers)
    else:
        en = "\def\\a%s%sEN{\\answer%s}\n" % (group, number, answers)
        lt = "\def\\a%s%sLT{\\answer{}{}{}{}{}}\n" % (group, number)
        pl = "\def\\a%s%sPL{\\answer{}{}{}{}{}}\n" % (group, number)
        ru = "\def\\a%s%sRU{\\answer{}{}{}{}{}}\n" % (group, number)
        return answer + en + lt + pl + ru + '\n'

def form_en(raw_data,group):
    number, _, answers, _, images, widths = raw_data
    WIDE_IMAGE = 200

    #guess if answer is language specific
    if all(x not in answers for x in 'abcdefghijklmnoprstuvwxyz') or "includegraphics" in answers:
        answers = "\\a%s%s" % (group, N2T[number])
    else:
        answers = "\\a%s%sEN" % (group, N2T[number])

    text = "\\%s%sEN" % (group, N2T[number])

    #case no image
    if not images:
        return "\ktext{%s}{%s\\newline%s}\n" % (number, text, answers)
    #case one normal image
    elif len(images) == 1 and widths[0] < WIDE_IMAGE:
        return "\kpic{%s}{%s\\newline%s}{%s}{%spt}{1}\n" % (number, text, answers, images[0], str(widths[0])) 
    #case one long image
    elif len(images) == 1 and widths[0] >= WIDE_IMAGE:
        return ("\ktext{%s}{\n"
                "%s\n"
                "\\vspace{-5pt}\n"
                "\\begin{center} \\includegraphics[scale=1]{%s} \\end{center}\n"
                "\\vspace{-5pt}\n"
                "%s}\n") % (number, text, images[0], answers)
    #case more than one image
    else:
        return ("\kpic{%s}{%s\\newline%s}{%s}{%spt}{1}\n"
                "%%plociai%s\n") % (number, text, answers, images[0],
                                    str(widths[0]),str(widths)) 
    return

def get_images(text):
    new = ""
    images = []
    while '\\includegraphics' in text:
        start = text.find('\\includegraphics')
        new += text[:start]
        text = text[start:]
        o_br = text.find('{')
        c_br = text.find('}')
        images.append(text[o_br+1: c_br])
        text = text[c_br+1:]
    print(text)
    new += text
    return images, new
    
def get_problems(text):
    problems = []
    while get_first_token(text):
        token = get_first_token(text)
        piece, text, number = separate_first_piece(text, token)
        if token != '\\kvoid':
            problems.append([number, piece])
        else:
            problems[-1][1] = problems[-1][1] + piece
            print(problems[-1])
    return problems


def get_first_token(text):
    tex = text.find("\\ktext")
    pic = text.find("\\kpic")
    void = text.find("\\kvoid")
    if tex + pic + void == -3:
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
        pro += '{' + a + '}'
        if i == 0:
            nr = a
    return token + pro, text, nr

import re

text = """\problemID{3}{20199}{Uzbekistan}%
\problemRating{B}{3}{L}%
\Problem{Problem text}
{a1}{a2}{a3}{a4}{a5}
{right_answer}{0}
{Solution text} to problem, a1, a2, a3, a4, a5, right_answer in python
"""

def parse_problem2(text):
    # Extracting problem ID, rating, and problem statement
    problem_id_match = re.search(r'\\problemID{(\d+)}{(\d+)}{([^}]+)}', text)
    rating_match = re.search(r'\\problemRating{([^}]+)}{(\d+)}{([^}]+)}', text)
    problem_text_match = re.search(r'\\Problem{([^}]+)}\n{([^}]+)}{([^}]+)}{([^}]+)}{([^}]+)}{([^}]+)}\n{([^}]+)}{(\d+)}', text)
    print(problem_id_match, rating_match, problem_text_match)
    print(asg)

    if problem_id_match and rating_match and problem_text_match:
        problem_id = problem_id_match.group(1)
        contest_id = problem_id_match.group(2)
        country = problem_id_match.group(3)

        difficulty = rating_match.group(1)
        points = rating_match.group(2)
        division = rating_match.group(3)

        problem_text = problem_text_match.group(1)
        a1, a2, a3, a4, a5 = problem_text_match.group(2, 3, 4, 5, 6)
        right_answer = problem_text_match.group(7)

        print(f"Problem ID: {problem_id}")
        print(f"Contest ID: {contest_id}")
        print(f"Country: {country}")
        print(f"Difficulty: {difficulty}")
        print(f"Points: {points}")
        print(f"Division: {division}")
        print(f"Problem Text: {problem_text}")
        print(f"a1: {a1}, a2: {a2}, a3: {a3}, a4: {a4}, a5: {a5}")
        print(f"Right Answer: {right_answer}")
    else:
        print("Could not extract information.")
