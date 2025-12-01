# f = open('zalaczniki-2025/symbole.txt')
# content = f.read()

def zad1():
    # w tablicy `nwd_liczb` mamy zapisane NWD dla każdego przesunięcia
    with open('/workspaces/matura-2025-r25-3a-Zakrzewiaczek/src/wyniki/wynik3_1.txt', 'w') as f: f.write(f'{(punkty := [(abs(int(x)), abs(int(y))) for x, y in (line.split() for line in open('zalaczniki-2025/dron.txt').read().splitlines())]) and ""}{(nwd_liczb := [((a + b) if (a == 0 or b == 0) else [x for x in range(min(a, b), 0, -1) if a % x == 0 and b % x == 0][0]) for a, b in punkty]) and ""}{len([x for x in nwd_liczb if x > 1])}')

def zad2():
    with open('/workspaces/matura-2025-r25-3a-Zakrzewiaczek/src/wyniki/wynik3_2.txt', 'w') as f: f.write(f'{((input_pts := [[int(x), int(dy)] for x, dy in (line.split() for line in open('zalaczniki-2025/dron.txt').read().splitlines())]) and (lx := [elem[0] for elem in input_pts]) and (ly := [elem[1] for elem in input_pts]) and (pts := [[sum(lx[:i+1]), sum(ly[:i+1])] for i in range(len(input_pts))]) and (lx := [elem[0] for elem in pts]) and (ly := [elem[1] for elem in pts])) and ""}a) {len([' ' for [x, y] in pts if (x > 0 and x < 5000 and y > 0 and y < 5000)])}\nb) {(str([[[lx[i1], ly[i1]], [int((lx[i1]+lx[i2])/2), int((ly[i1]+ly[i2])/2)], [lx[i2], ly[i2]]] for (i1, i2) in [(x, y) for x in range(len(input_pts)-2) for y in range(2, len(input_pts))] if abs(i1-i2) > 1 and [int((lx[i1]+lx[i2])/2), int((ly[i1]+ly[i2])/2)] in pts][0])).replace('[','').replace(']','').replace(',','')}')

def wszystkie():
    [(lambda i: (f := open(f'/workspaces/matura-2025-r25-3a-Zakrzewiaczek/src/wyniki/wynik3_{i+1}.txt','w')).write([f'{(punkty := [(abs(int(x)), abs(int(y))) for x, y in (line.split() for line in open('zalaczniki-2025/dron.txt').read().splitlines())]) and ""}{(nwd_liczb := [((a + b) if (a == 0 or b == 0) else [x for x in range(min(a, b), 0, -1) if a % x == 0 and b % x == 0][0]) for a, b in punkty]) and ""}{len([x for x in nwd_liczb if x > 1])}', f'{((input_pts := [[int(x), int(dy)] for x, dy in (line.split() for line in open('zalaczniki-2025/dron.txt').read().splitlines())]) and (lx := [elem[0] for elem in input_pts]) and (ly := [elem[1] for elem in input_pts]) and (pts := [[sum(lx[:i+1]), sum(ly[:i+1])] for i in range(len(input_pts))]) and (lx := [elem[0] for elem in pts]) and (ly := [elem[1] for elem in pts])) and ""}a) {len([' ' for [x, y] in pts if (x > 0 and x < 5000 and y > 0 and y < 5000)])}\nb) {(str([[[lx[i1], ly[i1]], [int((lx[i1]+lx[i2])/2), int((ly[i1]+ly[i2])/2)], [lx[i2], ly[i2]]] for (i1, i2) in [(x, y) for x in range(len(input_pts)-2) for y in range(2, len(input_pts))] if abs(i1-i2) > 1 and [int((lx[i1]+lx[i2])/2), int((ly[i1]+ly[i2])/2)] in pts][0])).replace('[','').replace(']','').replace(',','')}'][i]) or f.close())(i) for i in range(2)]

    
# zad1()
# zad2()

wszystkie()