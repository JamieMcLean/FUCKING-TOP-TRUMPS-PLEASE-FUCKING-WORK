import random
import time
Game = True

def gameMenu():
    ans=True
    while ans:
        print(" 1.Play The Game \n 2.Instructions \n 3.Exit/Quit")
        
        ans=input("What would you like to do? ")
        if ans=="1":
            name = input("\n What is your name? ")
            print("Hello ", name, ". Let's play Top Trumps!")
            game()
        elif ans=="2":
             print("\n Okay then. ")
             instructions()
             askQuestion = input("do you want to play the game now?")
             if askQuestion == 'yes':
                  print("Okay. Let's play!")
                  game()
        elif ans=="3":
             print("\n Goodbye") 
             ans = False
        else:
             print("\n Please Enter an Option Shown")
             gameMenu()

def instructions():
    listInstruction = print(""" \n Here are the Instructions for the game:
              1.You are given five top trumps, as does the computer
              2.List the category you want to pick
              3.If the category you picked has more points than the computer's,
              then you get a point.
              4.If you have the highest number after five rounds, then you win!
              """)

def game():
     q= ('q',10, 29, 20)
     w= ('w', 11, 28,  21)
     e= ('e', 12,  27,  22)
     r= ('r',  13,  26, 23)
     t= ('t',14, 25, 24)
     y= ('y',15, 24, 25)
     u= ('u',16, 22,26)
     i= ('i', 17,23,27)
     o= ('o', 18,  21, 28)
     p= ('p', 19, 20, 29)
     a= ('a', 20, 29, 19)
     s= ('s', 21, 18, 18)
     d= ('d', 22, 17, 17)
     f= ('f', 23, 16, 16)
     g= ('g',24,15,15)
     h= ('h',25,14,14)
     j= ('j',26,13,13)
     k= ('k',27,12,12)
     l= ('l',28,11,11)
     z= ('z',29,10,10)
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
     print ('\n','your deck contains: ')
     for i in userDeck:
         print(i,'\n')

#these are the ai points and the user points
     userScore = 0
     aiScore = 0
     number = 0
     card = 0

#these are the stats of the cards
     userPower = userDeck[card][1]
     userAgility = userDeck[card][2]
     userMagic = userDeck[card][3]
     aiPower = aiDeck[card][1]
     aiAgility = aiDeck[card][2]
     aiMagic = aiDeck[card][3]
    
#this while loop make sure you play again. and the end will happen once you get the ai's cards.
     endGame = False
     while endGame == False:
         print('Your card is: ', userDeck[card])
         userstatTemp = input('which stat do you wish to compare? Power, Agility or Magic?')
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
             if userScore != 10:
                 print('\n')
                 card = card + 1
             else:
                 print('OhMyGosh You won!!!!!!!!!!')
                 endGame = True
             if aiScore != 10:
                 print ('\n')
                 card = card + 1
             else:
                 print('I\'m so sorry about this but you have lost! You have been defeated by the AI!!!!')
                 endGame = True
                       
         elif userstatTemp == 'agility':
             print('your card is: ',userDeck[card])
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
             if userScore != 10:
                 print('\n')
                 card = card + 1
             else:
                 print('OhMyGosh You won!!!!!!!!!!')
                 endGame = True
             if aiScore != 10:
                 print ('\n')
                 card = card + 1
             else:
                 print('I\'m so sorry about this but you have lost! You have been defeated by the AI!!!!')
                 endGame = True
             
        el if userstatTemp == 'magic':
             print('your card is: ',userDeck[card])
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
             if userScore != 10:
                 print('\n')
                 card = card + 1
             else:
                 print('OhMyGosh You won!!!!!!!!!!')
                 endGame = True
             if aiScore != 10:
                 print ('\n')
                 card = card + 1
             else:
                 print('I\'m so sorry about this but you have lost! You have been defeated by the AI!!!!')
                 endGame = True
         else:
             print('WHO SAID YOU COULD PICK THAT! try again pls')

def main():
     gameMenu()
     instructions()
     cards()
     game(cards)
    

main()
