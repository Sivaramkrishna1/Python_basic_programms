

def differ(n):
    r=range(1,n+1)
    print(sum(r)**2 - sum(i*i for i in r) )
differ(int(input('')))

# sum(r)**2  returns square of the sum of the N natural numbers.
# sum(i*i for i in r)  returns sum of the square of the N natural numbers.