while True:
    s = input('Enter something : ')
    if s == 'quit':
        break
    if len(s) <3:
        print('Too Small')
        continue
    print('Input is of sufficient length')