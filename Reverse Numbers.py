def main():
    tc = int(input())
    while tc > 0 :
        tc -= 1
        number = int(input())
        revs_number = int(0)
        while (number > 0):
            revs_number = (revs_number * 10) + number % 10
            number = number // 10
        print(revs_number)
    return 0

if __name__ == '__main__':
    main()