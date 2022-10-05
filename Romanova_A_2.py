def flag_cz():
    for i in range(9):
        if i<=2:
            print(YELLOW + ' ' * 40 + END)
        elif i<=5:
            print(GREEN + ' ' * 40 + END)
        else:
            print(RED + ' ' * 40 + END)


def esc(code):
    return f'\u001b[{code}m'


def uzor_print():
    for i in range(7):
        first = '   ' * i + WHITE + ' ' * 4 + END + ' ' * (36 - 6 * i) + WHITE + ' ' * 4 + END
        second = '   ' * i + first
        print(first + second * 2)


def array_init(array_in, st):
    for i in range(10):
        for j in range(10):
            if j == 0:
                array_in[i][j] = round(st * (8 - i) + st, 1)
            if i == 9:
                array_in[i][j] = round(j, 1)
    return array_in


def array_fill(array_fi, res, st):
    for i in range(9):
        for k in range(10):
            if abs(array_fi[i][0] - res[9 - k]) < st:
                for j in range(9):
                    if 8 - j == k:
                        array_fi[i][j + 1] = 1
    return array_fi


def print_plot(plot):
    for i in range(9):
        line = ''
        for j in range(10):
            if j == 0:
                line += WHITE + str(plot[i][j])
            if plot[i][j] == 0:
                line += '  '
            elif plot[i][j] == 1:
                line += RED + '  ' + WHITE
        line += END
        print(line)
    print(WHITE + '0   1 2 3 4 5 6 7 8 9' + END)


def criteria(row):
    return int(row[5])


def procent(x, y):
    if x < y:
        return round(x / y * 100)
    else:
        return round(y / x * 100)


RED = esc(41)
GREEN = esc(42)
YELLOW = esc(43)
WHITE = esc(47)
END = esc(0)

array_plot = [[0 for col in range(10)] for row in range(10)]
result = [0 for i in range(10)]


flag_cz()


uzor_print()


for i in range(10):
    result[i] = abs(i)

step = round(abs((result[9] - result[0])) / 9, 1)

array_init(array_plot, step)
array_fill(array_plot, result, step)
print_plot(array_plot)


import csv

summ = 0
summ1 = 0
summ2 = 0
with open('books.csv') as csvfile:
    table = list(csv.reader(csvfile, delimiter=';'))
    table.pop(0)
    for row in table:
        summ += 1
        if int(row[5]) <= 12:
            summ2 += 1
        else:
            summ1 += 1

print('       0       10%       20%       30%       40%       50%       60%       70%       80%       90%       100%')
print('Другие ' + YELLOW + ' ' * procent(summ1, summ) + END, summ1, '(', procent(summ1, summ), '% )')
print('<=12   ' + GREEN + ' ' * procent(summ2, summ) + END, summ2, '(', procent(summ2, summ), '% )')
