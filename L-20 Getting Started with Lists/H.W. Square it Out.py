def square_and_separate(start, end):
    squares = [x**2 for x in range(start, end + 1)]
    os = []  # Odd squares
    es = []  # Even squares
    for x in squares:
        if x % 2 == 0:
            es.append(x)
        else:
            os.append(x)
    print("Odd Squares:", os)
    print("Even Squares:", es)
sr = int(input("Enter the start of the range: "))
er = int(input("Enter the end of the range: "))
square_and_separate(sr, er)
