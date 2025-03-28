#. Create a function to find maximum number in the given list.
def max_num(lst):
    max=lst[0]
    for num in lst:
        if(num>max):
            max=num
    return max

def main():
    Input_lst=[]
    size=int(input("enter size of list: "))
    print("enter values")
    for i in range(size):
        values=int(input())
        Input_lst.append(values)
    print("input values=", Input_lst)

    result=max_num(Input_lst)
    print(f"maximum number in{Input_lst}=",result)


if __name__=="__main__":
    main()