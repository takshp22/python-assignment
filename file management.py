print("************************************************")
file=open("Tops1.txt","w")
file.write("this is file management demo using python.")
fie.close()
print("file written succesfully")
print("************************************************")


file=open("Tops1.txt","r")
print(file.read())
file.close()
print("************************************************")


file=open("Tops1.txt","a")
file.write("\nthis file is now appended")
file.close()
print("file appended successfully")
print("************************************************")


file=open("tops.txt","w+")
file.write("this is w+ operation is python.")
print("current file position",file.tell())
file.seek(0)
print(file)
print("************************************************")
