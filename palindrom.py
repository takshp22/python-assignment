n= int(input("enter a N:"))
num_str=  str(n)
start=0
end=len(num_str)-1

while start < end:
    if num_str[start] != num_str[end]:
        print(n,"is not palindrom")
        break
    start +=1
    end -=1
else:
    print(n,"is palindrom")

