coin = int(input("금액:"))
dan=50000
check=1
while(dan!=0):
    print(int(dan),end="원:")
    print(int(coin/dan),end="개")
    print()
    coin=coin%dan
    if check==1:
        dan=int(dan/5)
        check=0
    else:
        dan=int(dan/2)
        check=1
