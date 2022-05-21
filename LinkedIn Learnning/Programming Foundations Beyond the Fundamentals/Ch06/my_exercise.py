# app to interact with user
# rt stands for reading files 
# wt stands for writing files

from turtle import update


mainFile = open("mainFile.txt", "rt")
updatedFile = open("updateMainFile.txt", "wt")
print("updating start")
New = 0
for new in mainFile:
    New += int(new)
#Remove space at the end of a string using strip() or rstrip() in python 
    print(new.rstrip(), file= updatedFile)

print("\nNewUpdate:" + str(New), file=updatedFile)

updatedFile.close()
print("updating complete")

# #########
