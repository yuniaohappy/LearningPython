# 4.10.1
spam = ['apples', 'bananas', 'tofu', 'cats']
res = ''
for i in range(len(spam)):
    if i == len(spam) - 2:
        res += spam[i] + ", and "
    else:
        res += spam[i] + ", "
print(res)


# 4.10.2
# grid = [['.', '.', '.', '.', '.', '.'],
#         ['.', 'O', 'O', '.', '.', '.'],
#         ['O', 'O', 'O', 'O', '.', '.'],
#         ['O', 'O', 'O', 'O', 'O', '.'],
#         ['.', 'O', 'O', 'O', 'O', 'O'],
#         ['O', 'O', 'O', 'O', 'O', '.'],
#         ['O', 'O', 'O', 'O', '.', '.'],
#         ['.', 'O', 'O', '.', '.', '.'],
#         ['.', '.', '.', '.', '.', '.']]
# for i in range(len(grid[0])):
#     for x in range(len(grid)):
#         print(grid[x][i], end='')
#     print()
