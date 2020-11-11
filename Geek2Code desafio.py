
def diamonds(n):
    for i in range(1, n + 1):

        print('\n', i, '.', sep='')
        lines = 2*i - 1

        for l in range(1 - i, i):
            line = abs(l)* ' ' + '#'

            if len(line) <= lines // 2:
                line += (lines // 2 - len(line))*' '
                line += ' ' + line[::-1]
            else:
                line += (lines - len(line))*' '

            print(line)

n = int(input('n = '))
diamonds(n)