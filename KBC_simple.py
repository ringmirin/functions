def kbc_simple():
        name=["who is the new FC?","who is the T&p?","who is the IT?"]
        option=[["Worrin","Swathi","Ramchanpy","Honmi"],["Manori","Ashma","Rinki","Pretty"],["Narani","Sushma",
           "Deepti","Nikita"]]
        ans=[3,1,4]
        i=0
        j=0
        while i<len(name) and j<len(option):
                print("Q",i+1,name[i])
                k=0
                while k<len(option[i]):
                        print(k+1,option[j][k])
                        k+=1
        
                answer=int(input("enter your ans: "))
                if answer==ans[i]:
                        print("right")
                else:
                        print("wrong")
                i+=1
                j+=1
kbc_simple()



