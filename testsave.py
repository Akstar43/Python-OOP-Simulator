from save import Save
save = Save()
save.loadsave()
userinput = int(input("Enter count"))
if userinput == save.loadsave():
    print("Hello")
else: 
    print("Not working")

