from example1 import grades
class student:

    def create(self):
        #n=int(input('how many students you want to create'))
        #if n<=0:
            #return
        for i in range(3):
            self.name=str(input('enter student name'))
            self.mark=int(input('enter student mark'))
            self.attendance=int(input('enter student attendance'))
            if self.attendance>100 or self.attendance<0:
                print('100 is the max attendance')
                break
            name_s.append(self.name)
            mark_s.append(self.mark)
            attendance_s.append(self.attendance)

    def convert(self):
        for i in mark_s:
            empty_m.append(grades(i))
            
    def atten(self):
        for i in attendance_s:
            if (i<75):
                i='RA'
                empty_a.append(i)
            else:
                empty_a.append(str(i)+'%')

    def display(self):
        for i in name_s:
            position=name_s.index(i)
            print('\n',i,'\t',empty_m[position],'\t',empty_a[position])

    def show(self):
        a=input('\nenter search name')
        if a in name_s:
            b=name_s.index(a)
            print('\n',a,'\t',empty_m[b],'\t',empty_a[b])
        elif a not in name_s:
            print(a,'is not there')
    
name_s=[]
mark_s=[]
attendance_s=[]

empty_m=[]
empty_a=[]

call=student()

call.create()
call.convert()
call.atten()
call.display()
call.show()



    
            
        
            



    
        
