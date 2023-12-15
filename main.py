import csv

from icecream import ic


asc = []
arr = []

with open('to_parse.csv') as par:
    par = csv.reader(par)
    for line in par:
        asc.append([line[0].split('\t')[0], line[0].split('\t')[2]])


with open('list.csv') as file:
    file = csv.reader(file)
    for line in file:
        for word in line:
            arr.append(word)

"""Part 1"""

res = 0
x = 0
z = 0
#
# for word in arr:
#     for letter in word:
#         for y in range(len(asc)):
#             if asc[y][1] == letter:
#                 z = int(asc[y][0])
#         x += z
#         x *= 17
#         x %= 256
#     res += x
#     x = 0
#     ic(res)


"""Part2 """

h = {}

for word in arr:
    moved = False
    for letter in word:
        if letter == '-':
            box = word.split('-')[0]
            for l in box:
                for y in range(len(asc)):
                    if asc[y][1] == l:
                        x = ((x + int(asc[y][0])) * 17) % 256
            if x in h.keys():
                for arr in range(len(h[x])):
                    if h[x][arr][0] == word.split('-')[0]:
                        h[x].pop(arr)
                        break
        if letter == '=':
            box = word.split('=')[0]
            for l in box:
                for y in range(len(asc)):
                    if asc[y][1] == l:
                        x = ((x + int(asc[y][0])) * 17) % 256
            if x in h.keys():
                for arr in range(len(h[x])):
                    if h[x][arr][0] == word.split('=')[0]:
                        h[x][arr] = word.split('=')
                        moved = True
                if moved is False:
                    h[x].append(word.split('='))
            else:
                h[x] = [word.split('=')]
        x = 0

result = 0

for i in h:
    for arr in range(len(h[i])):
        res += (i + 1) * (arr + 1) * int(h[i][arr][1])

ic(res)
