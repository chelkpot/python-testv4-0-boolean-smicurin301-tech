# tasks/task6.py

def solve():
# Ниже пишите решение задачи
    a, b, c = map(int, input().split())
    # Сортируем стороны, чтобы найти наибольшую (гипотенузу)
    sides = sorted([a, b, c])
    print(sides[0]**2 + sides[1]**2 == sides[2]**2)
   
   
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()