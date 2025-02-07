# Problem: Lists - https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true

if __name__ == '__main__':
    N = int(input())
    l = []
    for i in range(N):
        args = input().split()
        if args[0] == "print":
            print(l)
        elif args[0] == "append":
            l.append(int(args[1]))
        elif args[0] == "sort":
            l.sort()
        elif args[0] == "pop":
            l.pop()
        elif args[0] == "reverse":
            l.reverse()
        elif args[0] == "insert":
            l.insert(int(args[1]), int(args[2]))
        else :
            l.remove(int(args[1]))