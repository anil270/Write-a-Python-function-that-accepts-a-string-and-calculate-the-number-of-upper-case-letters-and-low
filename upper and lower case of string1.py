def upperlower():
    n = input("Enter the String :")
    count = 0
    count1 = 0
    for i in n:
        if (i.isupper())==True:
            count+=1
        elif (i.islower())==True:
            count1+=1
    print('No. of Upper case characters :',count)
    print('No. of Lower case Characters :',count1)
upperlower()