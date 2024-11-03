db = ["Croaks", "Eat Flies"]
kb = ["Frog", "Canary"]
color = ["Green", "Yellow"]

def main():
    x = int(input("*-----Backward Chaining*\n X is \n1. Frog \n2. Canary\nSelect One: "))
    if x in (1, 2): print(f"Chance Of {'eating flies' if x == 1 else 'shrimping'}")
    else: return print("\n-------Invalid Option Select")

    k = int(input(f"\n X is {kb[x - 1]}\n1. Green \n2. Yellow\nSelect Option: "))
    if k in (1, 2): print(f"Yes, it is in {color[k - 1]} colour and will {db[x - 1]}")
    else: print("\n---Invalid Knowledge Database")

if __name__ == "__main__": main()
