import random
import time
Game = True
#nates code
def gameMenu():
     ans=True
     while ans:
        print('  1.Play The Game ','\n',' 2.Instructions ','\n',' 3.Exit/Quit')
        print('Please only type in a number!')
        print('What would you like to do? ')
        ans=input('')
        if ans=='1':
             name = input('What is your name? ')
             print('Hello ', name, '. Let\'s play Top Trumps!')
             game()
        elif ans=='2':
             print('\n',' Okay then. ')
             instructions()
             askQuestion = input('do you want to play the game now?')
             if askQuestion == 'yes':
                 name = input('What is your name? ')
                 print('Hello ', name, '. Let\'s play Top Trumps!')
                 game()
             elif askQuestion == 'y':
                 name = input('What is your name? ')
                 print('Hello ', name, '. Let\'s play Top Trumps!')
                 game()
             else:
                 print('oh......i\'m sorry......il let you go away...')
                 
        elif ans=='3':
             print('\n',' Goodbye') 
             ans = False
        else:
             print('\n' ,'Please Enter an Option Shown')
             gameMenu()

def instructions():
    listInstruction = print(''' '\n' Here are the Instructions for the game:
              1.You have five top trump cards, as does the computer
              2.List the category you want to pick
              3.If the category you picked has more points than the computer's,
                then you get a point.
              4.there are 9 rounds and whoever has the most points by the end, Wins!
              ''')

def game():
     q=('james',10,29,20)
     w=('william',11,28,21)
     e=('etheridge',12,27,26)
     r=('roland',13,26,23)
     t=('tom',11,25,24)
     y=('yves',15,24,25)
     u= ('uderzo',16, 22,26)
     i= ('inigo', 17,23,27)
     o= ('oliver', 18,  21, 28)
     p= ('preston', 19, 20, 29)
     a= ('aston', 20, 29, 19)
     s= ('sylvester', 11, 18, 15)
     d= ('david', 22, 17, 17)
     f= ('fernando', 23, 16, 16)
     g= ('goscini',24,15,15)
     h= ('harry',25,14,14)
     j= ('jill',26,13,18)
     k= ('kill',15,12,16)
     l= ('lill',28,11,11)
     z= ('zoolander',29,10,10)
     deck = [q,w,e,r,t,y,u,i,o,p,a,s,d,f,g,h,j,k,l,z]
     random.shuffle(deck)

#aiDeck
     aiDeck = []
     for i in range(0,10):
         aideckTemp = random.choice(deck)
         aiDeck.append(aideckTemp)

#userDeck
     userDeck = []
     for i in range (0,10):
         userdeckTemp = random.choice(deck)
         userDeck.append(userdeckTemp)
        
     print('the stats go as so:','\n','Name of your caracter, his power rating, his agility rating, his magic rating')
     print ('\n','your deck contains: ')
     for i in userDeck:
         print(i,'\n')
         time.sleep( 0.05)

#these are the ai points and the user points
     userScore = 0
     aiScore = 0
     number = 0
     card = 0
    
#this while loop make sure you play again. and the end will happen once you get the ai's cards.

     while card!= 9:
#these are the stats of the cards
         userPower = userDeck[card][1]
         userAgility = userDeck[card][2]
         userMagic = userDeck[card][3]
         aiPower = aiDeck[card][1]
         aiAgility = aiDeck[card][2]
         aiMagic = aiDeck[card][3]
         print('\n','Your card is: ', userDeck[card])
         print('please type in all lowercase the actual word!')
         userstatTemp = input('which stat do you wish to compare? Power, Agility or Magic?  ')
         if userstatTemp == 'power':
             print('your card is: ',userDeck[card])
             print('His card is: ',aiDeck[card])
             if int(userPower) > int(aiPower):
                 print('You Won! you have a higher power stat than the computer!','\n')
                 print('your stat was ',userPower,'while his was ',aiPower,'!')
                 userScore = userScore + 1
                 card = card + 1
                
             elif int(userPower) < int(aiPower):
                 print('Oh no!!! You lost...the computer had a higher power stat than you!','\n')
                 print('your stat was ',userPower,'while his was ',aiPower,'!')
                 aiScore = aiScore + 1
                 card = card + 1
                 
             else:
                 print('Uh Oh...you and the computer seem to have come to a draw!','\n')
                 print('There is only one thing to do! continue. draws do not count as points.')
                 card = card + 1
                       
         elif userstatTemp == 'agility':
             print('your card is: ',userDeck[card])
             print('His card is: ',aiDeck[card])
             if int(userAgility) > int(aiAgility):
                 print('You Won! you have a higher power stat than the computer!','\n')
                 print('your stat was ',userAgility,'while his was ',aiAgility,'!')
                 userScore = userScore + 1
                 card = card + 1
                 
             elif int(userAgility) < int(aiAgility):
                 print('Oh no!!! You lost...the computer had a higher power stat than you!','\n')
                 print('your stat was ',userAgility,'while his was ',aiAgility,'!')
                 aiScore = aiScore + 1
                 card = card + 1
                 
             else:
                 print('Uh Oh...you and the computer seem to have come to a draw!','\n')
                 print('There is only one thing to do! continue. draws do not count as points.')
                 card = card + 1
             
             
         elif userstatTemp == 'magic':
             print('your card is: ',userDeck[card])
             print('His card is: ',aiDeck[card])
             if int(userMagic) > int(aiMagic):
                 print('You Won! you have a higher power stat than the computer!','\n')
                 print('your stat was ',userMagic,'while his was ',aiMagic,'!')
                 userScore = userScore + 1
                 card = card + 1
                
             elif int(userMagic) < int(aiMagic):
                 print('Oh no!!! You lost...the computer had a higher power stat than you!','\n')
                 print('your stat was ',userMagic,'while his was ',aiMagic,'!')
                 aiScore = aiScore + 1
                 card = card + 1
                 
             else:
                 print('Uh Oh...you and the computer seem to have come to a draw!','\n')
                 print('There is only one thing to do! continue. draws do not count as points.')
                 card = card + 1
         else:
                 print('WHO SAID YOU COULD PICK THAT! try again pls')

     if userScore > aiScore:
         print('OhMyGosh You won by ',userScore - aiScore,' points!')
         
     elif userScore < aiScore:
         print('I\'m so sorry about this but you have lost! You have been defeated by the AI by ', aiScore - userScore,' points!','\n')


def main():
     gameMenu()
     instructions()
     cards()
     game(cards)
    

main()
