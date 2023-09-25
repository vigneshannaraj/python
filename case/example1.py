def grades(i):
    if i>=90:
        i='A+'
        return i
    elif i>=80:
        i='A'
        return i
    elif i>=70:
        i='B+'
        return i
    elif i>=60:
        i='B'
        return i
    elif i>=50:
        i='C'
        return i
    elif i>=40:
        i='E'
        return i
    else:
        i='F'
        return i

    

def gpa(i):
    if i=='A+':
        i=10
        return i
    elif i=='A':
        i=9
        return i
    elif i=='B+':
        i=8
        return i
    elif i=='B':
        i=7
        return i
    elif i=='C':
        i=6
        return i
    elif i=='E':
        i=5
        return i
    elif i=='F':
        i=0
        return i
    else:
        i=0
        return i
        
