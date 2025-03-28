#Create a function to find the frequency count of an element in that list.
def freq_count(lst,num):
    count=0
    for i in lst:
        if(i==num):
            count=count+1
    return count
    
def main():
    Input_lst=[]
    size=int(input("enter size of list: "))
    print("enter values")
    for i in range(size):
        values=int(input())
        Input_lst.append(values)
    print("input values=", Input_lst)

    num=int(input("enter  nunber to find frequency: "))
    result=freq_count(Input_lst,num)
    print(f"frequency of {num} in list {Input_lst}= {result}")


if __name__=="__main__":
    main()
        
    