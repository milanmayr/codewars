# https://www.codewars.com/kata/51c8e37cee245da6b40000bd/python

def solution(string,markers):
    lines = string.split('\n')
    stripped_lines = []
    for line in lines:
        stripped_line = line
        for marker in markers:
            if marker in stripped_line:
                stripped_line = stripped_line[0:line.find(marker)].strip(' ')
        stripped_lines.append(stripped_line)
    return '\n'.join(stripped_lines)

solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])