nterms=int(input("Enter number of terms:"))
n1=0
n2=1
count=0
if nterms<0:
    print("Please enter a positive number")
elif nterms==1:
    print("Fibonacci series upto",nterms,":")
    print(n1)
else:
    print("Fibonacci series:")
    while count<nterms:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1
