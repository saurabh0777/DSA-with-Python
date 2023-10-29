# create hashtable
dp = {}
def fibo(n):
    if n < 2:
        return 1

    else:
        if (n in dp ):
            return dp[n]
        else:
            dp[n] =fibo(n-1) + fibo(n-2)
            return dp[n]

for i in range(1,100):
    print("i value",i ,"fibo =",str(fibo(i)))


