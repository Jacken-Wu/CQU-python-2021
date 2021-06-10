<<<<<<< HEAD
def main():
    total_count = int(input())
    calculate_days(total_count)
=======
def main():
    total_count = int(input())
    calculate_days(total_count)
>>>>>>> 91c5edef37c527a60ab0cadc28e08bc788a52119
def calculate_days(num):
    day = 0
    while num > 0:
        num -= num // 2 + 2
        day += 1
    print(day)
<<<<<<< HEAD

main()
=======

main()
>>>>>>> 91c5edef37c527a60ab0cadc28e08bc788a52119


