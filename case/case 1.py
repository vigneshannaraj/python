name=input('whats your name?')
print('\nBINGO','\nguess the right number 1-10 to win jackpot')
import random
class play:
    def __init__(self):
        self.win=0
        self.n=0
        
    def mode(x):
        m_ode=input('\nselect mode \neasy \nmedium \nhard')
        if m_ode=='easy':
            x.n=5
        elif m_ode=='medium':
            x.n=3
        elif m_ode=='hard':
            x.n=1
        else:
            x.n=3

    def game(x):
        ram=random.randint(1,10)
        while x.n>0:
            w=0
            print('\nyou have',x.n,'chance LEFT')
            x.n=x.n-1
            a=int(input('\nwhats the number?'))
            if a==ram:
                print('\nthats it',name,'won JACKPOT')
                w=w+1
                break
            elif a>ram:
                print('\nthats a NO','\nguess LOWER')
            elif a<ram:
                print('\nthats a NO','\nguess HIGHER')
        if w==0:
            print('\n',name,'LOST the game')
        else:
            x.win=x.win+w
            
    def show(x):
        print('\ntotal WIN=',x.win)
            
call=play()

class main:
    def again(x):
        call.mode()
        call.game()
        count=1
        while True:
            b=input('\ndo you want to PLAY again? \npress yes/no')
            if b=='yes':
                count=count+1
                call.mode()
                call.game()
            else:
                call.show()
                print('\ntotal play=',count)
                break

obj=main()
obj.again()
        

                

      


