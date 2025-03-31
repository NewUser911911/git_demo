while True:
    s = input()
    if '+' in s:
        args = s.split('+')
        a, b = int(args[0]), int(args[1])
        print(a + b)
    elif '-' in s:
        args = s.split('-')
        a, b = int(args[0]), int(args[1])
        print(a - b)
    elif '/' in s:
        args = s.split('/')
        a, b = int(args[0]), int(args[1])
        print(a / b)
    elif '*' in s:
        args = s.split('*')
        a, b = int(args[0]), int(args[1])
        print(a * b)
    else:
        break
        