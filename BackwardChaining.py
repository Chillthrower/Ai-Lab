db = ["Croaks", "Eat Flies", "Shrimps", "Sings"]
kb = ["Frog", "Canary"]
cl = ["Green", "Yellow"]

def main():
    x = int(input("*-----Backward Chaining*\n X is\n1. Frog \n2. Canary\nSelect One: "))
    if x in (1, 2): 
        print(f"Chance of {db[x - 1]} Color Is 1. Green 2. Yellow")
    else: 
        return print("\n-------Invalid Option Select")

    k = int(input("Select Color: "))
    if (k == 1 and x == 1): 
        print(f"Yes, it is {kb[0]} And Color Is {cl[0]}")
    elif (k == 2 and x == 2): 
        print(f"Yes, it is {kb[1]} And Color Is {cl[1]}")
    else: 
        print("\n---Invalid Knowledge Database")

if __name__ == "__main__": 
    main()
