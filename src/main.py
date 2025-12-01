# f = open('zalaczniki-2025/symbole.txt')
# content = f.read()

def zad1():
    # w tablicy `nwd_liczb` mamy zapisane NWD dla każdego przesunięcia
    with open('/workspaces/matura-2025-r25-3a-Zakrzewiaczek/src/wyniki/wynik3_1.txt', 'w') as f: f.write(f'{(punkty := [(abs(int(x)), abs(int(y))) for x, y in (line.split() for line in open('zalaczniki-2025/dron.txt').read().splitlines())]) and ""}{(nwd_liczb := [((a + b) if (a == 0 or b == 0) else [x for x in range(min(a, b), 0, -1) if a % x == 0 and b % x == 0][0]) for a, b in punkty]) and ""}{len([x for x in nwd_liczb if x > 1])}')

def zad2():
    input_pts = [(int(x), int(dy)) for x, dy in (line.split() for line in open('zalaczniki-2025/dron.txt').read().splitlines())]
    (lx, ldy) = zip(*input_pts)
    pts = [(sum(lx[:i+1]), sum(ldy[:i+1])) for i in range(len(input_pts))]
    # print(len([' ' for x, y in pts if (x > 0 and x < 5000 and y > 0 and y < 5000)]))


    tablica = [1, 2, 3, 4, 5, 6]

    print([])


# def wszystkie():
    
# zad1()
zad2()

# wszystkie()