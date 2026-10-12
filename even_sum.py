n=int(input("Ente a number :"))
total=0
count=0
for i in range(1,n+1):
    if i%2==0:
        total=total+i
        count=count+1
print(f"sum of even num:{total}")
print(f"number of even number:{count}")
