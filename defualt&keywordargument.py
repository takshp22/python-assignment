def test(a=40,b=30,c=20,d=10):   # default argument
    print("A",a,"B",b,"C",c,"D",d)

test(1,2,3,4)
test(1,2,3)
test(1,2)
test(1)
test()
test(b=100,d=200)#keyword argument
