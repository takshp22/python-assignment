def test(a,b,c,*d,**e): # we can use when we dont know about the value enter in function
    print ("A",a,"B",b,"C",c,"D",d,"E",e)
    
test(1,2,3,4,5,6,7,8,9,x=10,b=20,c=30)
