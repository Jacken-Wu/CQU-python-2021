def main():
    s1 = input()
    s2 = input()
    print(is_rotation(s1,s2))

def is_rotation(s1, s2):
    if s1 == s2:
        return True
    if len(s1) == len(s2):
        for i in range(len(s1)):
            if s1[:i] == s2[-i:] and s1[i:] == s2[:-i]:
                return True
    return False


main()

