word=input("Enter the word for search !:")
with open("filep1.txt") as f:
    contant = f.read()
    if word in contant:
        print("Is present !")
    else:print("Not present !")

