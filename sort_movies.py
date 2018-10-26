#!/usr/bin/env python3


mov_lst = ['The Shape of You', 'a Beautiful Mind', 'A Beautiful Mind', 'Argo', 'a cats', 'a dogs', 'hello', 'The Something']


for i in range(len(mov_lst)):
    if mov_lst[i].split()[0] in ['A', 'The', 'a', 'the']:
        index = mov_lst[i].find(' ')
        if index == -1:
            pass
        else:
            mov_lst[i] = mov_lst[i][index+1:] + ' ' + mov_lst[i][:index]
mov_lst.sort()
for i in range(len(mov_lst)):
    if mov_lst[i].split()[-1] in ['A', 'The', 'a', 'the']:
        index = mov_lst[i].rfind(' ')
        if index == -1:
            pass
        else:
            mov_lst[i] = mov_lst[i][index+1:] + ' ' + mov_lst[i][:index]
print(mov_lst)
