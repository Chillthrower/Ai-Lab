db = ["Croaks", "Eat Flies", "Shrimps", "Sings"]
kb = ["Frog", "Canary", "Green", "Yellow"]

def main():
    x = int(input("*-----Forward Chaining*\n1. Croaks \n2. Eat Flies \n3. Shrimps \n4. Sings\nSelect One: "))
    if x in (1, 2): 
        print(f"Chance Of Frog {db[x - 1]} Color Is 1. Green 2. Yellow")
    elif x in (3, 4): 
        print(f"Chance of Canary {db[x - 1]} Color Is 1. Green 2. Yellow")
    else: 
        return print("\n-------Invalid Option Select")

    k = int(input("Select Option: "))
    if (k == 1 and x in (1, 2)): 
        print(f"Yes, it is {kb[0]} And Color Is {kb[2]}")
    elif (k == 2 and x in (3, 4)): 
        print(f"Yes, it is {kb[1]} And Color Is {kb[3]}")
    else: print("\n---Invalid Knowledge Database")

if __name__ == "__main__": main()
