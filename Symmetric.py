if __name__ == "__main__":
    M = int(input())
    A = set(map(int, input().split(" ")))
    N = int(input())
    B = set(map(int, input().split(" ")))
    for num in sorted(list((A | B) - (A & B))):
        print(num)
