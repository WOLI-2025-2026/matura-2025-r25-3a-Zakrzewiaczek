# Jakub Zakrzewski

f = open("zalaczniki-2025/symbole.txt")
content = f.read()

def zad1():
    print([elem for elem in content.split('\n') if (elem[::-1] == elem and elem != '')])

def zad2():
    tablica = [list(elem) for elem in content.split('\n')]
    print(f"{len(wynik := [(y+1, x+1) for y in range(1, len(tablica) - 2) for x in range(1, len(tablica[0]) - 1) if len(set(tablica[b][a] for a, b in [(x-1,y-1),(x,y-1),(x+1,y-1),(x-1,y),(x,y),(x+1,y),(x-1,y+1),(x,y+1),(x+1,y+1)])) == 1])} {' '.join(f'{x} {y}' for x, y in wynik)}")

def zad3():
    print(f"{(output := max([(int(elem.replace('o','0').replace('+','1').replace('*','2'), 3), elem) for elem in content.split('\n') if elem.strip()], key=lambda x: x[0]))[0]} {output[1]}")

def zad4():
    def to_base3(n: int) -> str:
        if n == 0:
            return "0"
        digits = []
        while n:
            digits.append(str(n % 3))
            n //= 3
        return ''.join(reversed(digits))
    print(f"{(output := sum([int(elem.replace('o','0').replace('+','1').replace('*','2'), 3) for elem in content.split('\n') if elem.strip()]))} {to_base3(output).replace('0','o').replace('1','+').replace('2','*')}")

zad1()
zad2()
zad3()
zad4()