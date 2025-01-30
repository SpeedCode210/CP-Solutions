# Problem: Split string and Join - https://www.hackerrank.com/challenges/python-string-split-and-join/problem?isFullScreen=true



def split_and_join(line):
    res = ""
    for i in range(0,len(line)):
        if line[i] == ' ':
            res = res + '-'
        else:
            res = res + line[i]
    return res

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)