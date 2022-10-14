def palindrome(s: str)-> bool:
    l = len(s) // 2
    m = len(s) - 1
    f = 0
    for i in range(l):
        if s[i] != s[m - i]:
            break
    else:
        f = 1

    return True if f else False

if __name__ == '__main__':
    inputs = input()
    while inputs.isspace() or len(inputs) == 0:
        inputs = input()

    print('input str', inputs, 'is palindrome?', palindrome(inputs))
