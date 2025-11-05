# Jakub Zakrzewski

f = open("zalaczniki-2025/symbole.txt")
content = f.read()

def zad1():
    print([elem for elem in content.split('\n') if (elem[::-1] == elem and elem != '')])

def zad2():
    print(f"{str((tablica := [list(elem) for elem in content.split('\n')])[0:0]).replace('[]', '')}{len(wynik := [(y+1, x+1) for y in range(1, len(tablica) - 2) for x in range(1, len(tablica[0]) - 1) if len(set(tablica[b][a] for a, b in [(x-1,y-1),(x,y-1),(x+1,y-1),(x-1,y),(x,y),(x+1,y),(x-1,y+1),(x,y+1),(x+1,y+1)])) == 1])} {' '.join(f'{x} {y}' for x, y in wynik)}")

def zad3():
    print(f"{(output := max([(int(elem.replace('o','0').replace('+','1').replace('*','2'), 3), elem) for elem in content.split('\n') if elem.strip()], key=lambda x: x[0]))[0]} {output[1]}")

def zad4():
    print(f"{str((to_base3 := lambda n: '' if n == 0 else to_base3(n // 3) + str(n % 3)))[0].replace('<', '')}{(output := sum([int(elem.replace('o','0').replace('+','1').replace('*','2'), 3) for elem in content.split('\n') if elem.strip()]))} {to_base3(output).replace('0','o').replace('1','+').replace('2','*')}")


zad1()
zad2()
zad3()
zad4()