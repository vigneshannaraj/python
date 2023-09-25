class telephone:
    def __init__(self,storage):
        self.storage=storage
        
    def contact(a):
        a.storage=storage
        n=int(input('\nhow many contact you want to create'))
        if n<=0:
            return
        for i in range(n):
            a.name=str(input('\nenter name'))
            alpha=a.name.isalnum()
            #print(alpha)
            if alpha==False:
                print('name cannot contain special character')
                break
            a.phone=int(input('enter phone number'))
            digit=0
            check=a.phone
            while check>0:
                digit=digit+1
                check=check//10
            if digit!=10:
                print('\nphone number must be 10 digit')
                return 
            a.storage[a.name]=a.phone

    def show(c):
        for i,j in c.storage.items():
            print(i,j)

    def delete(d):
        #d.storage=storage
        x=str(input('\nenter contact name to delete'))
        del d.storage[x]

    def update(e):
        e.name=str(input('\nenter name'))
        alpha=e.name.isalpha()
        #print(alpha)
        if alpha==False:
            print('name cannot contain special character')
            return
        e.phone=int(input('enter phone number'))
        digit=0
        check=e.phone
        while check>0:
            digit=digit+1
            check=check//10
        if digit!=10:
            print('\nphone number must be 10 digit')
            return 
        e.storage[e.name]=e.phone

storage=dict(())
call=telephone(storage)



class main:
    while True:
        print('\npress 0 to exit \npress 1 to create contact \npress 2 to update contact \npress 3 to delete contact')
        action=int(input())
        if action==0:
            break
        elif action==1:
            call.contact()
            call.show()
        elif action==2:
            call.update()
            call.show()
        elif action==3:
            call.delete()
            call.show()
        else:
            print('\nenter valid option')

obj=main()

