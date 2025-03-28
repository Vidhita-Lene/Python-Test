#Create a function to find the count of odd numbers from that list.

def odd(lst):
    odd_num=[]
    for i in lst:
        if(i%2!=0):
            odd_num.append(i)
    return odd_num

def main():
    Input_lst=[]
    size=int(input("enter size of list: "))
    print("enter values")
    for i in range(size):
        values=int(input())
        Input_lst.append(values)
    print("input values=", Input_lst)

    result=odd(Input_lst)
    print("list of odd number= ",result)

if __name__=="__main__":
    main()

