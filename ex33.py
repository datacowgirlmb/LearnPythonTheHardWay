def num_loop(max_number):
    # max_number=6
    i = 0
    numbers = []

    while i < max_number:
        print(f"At the top i is {i}")
        numbers.append(i)
        
        i = i + 1
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")
        
    print("The numbers: ")

    for num in numbers:
        print(num)
        
num_loop(6)