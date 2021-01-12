def mutate_string(string, position, character):
    l=list(string)
    for i in range(len(l)):
        l[position]=character
    str1=""
    for i in l:
        str1+=i
    return str1

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
