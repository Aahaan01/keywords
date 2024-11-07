name=input("Enter your name: ")

for i in name:
    print(i)
    if i=="a":
        print("A is found.")
        break
    else:
        print("A is not found.")