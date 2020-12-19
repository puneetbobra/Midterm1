#q2.py
##use nested loops to draw a pattern
rows = 30
for a in range(rows):
    for b in range(a+1):
        if a == 0 and b == 0:
            print('#',end ='')
        if b == 0 or b == a:
            print('#', end='')
        else:
            print(' ', end='')
    print('')

#End