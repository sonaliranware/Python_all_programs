#Project : KBC game 

import random;
import sys;
#method for displaying the welcome screen
def oscreen():
  for a in range(65):
    print('*',end='')
  print("""\nW E L C O M E       T O       T H E      K B C      G A M E""")
  for b in range(65):
    print('*',end='')
  
def display_question(rn):
  print('\n') 
  for x in range (8):
    for j in range(65):
      print('-',end='') 
    print('\n') 
    i=rn 
    print(questions[i])   
    for k in range(65):
      print('-',end='')      
    print("\n")
    print(choices[i][0:choices[i].index('2')],end='')
    print("\t\t\t"+choices[i][choices[i].index('2'):choices[i].index('3')])
    print("\n"+choices[i][choices[i].index('3'):choices[i].index('4')],end='');
    print("\t\t\t"+choices[i][choices[i].index('4'):len(choices[i])])
    print("YOUR TIME STARTS NOW....")
    print("\n\n\n")
    ua=0
    ua=int(input("Enter your answer or if you are not sure---> Enter digit 9 for using a lifeline\n"))
    return ua
def display_lifelines(i):
  global ll5050, llhint, ll2guesses, llchangeq, rnum,lifelinectr
  llua=0

  if (lifelinectr>0):
    print("You have "+str(lifelinectr)+" lifelines left!")
    print("They are :")
    if ll5050:
      print("(A)50-50")
    if (llhint):
      print("(B)Give a Hint")
    if (ll2guesses):
      print("(C)2 guesses")
    if (llchangeq):
      print("(D)Change the question")
                
    
    llchoice=input("\nWhich lifeline do you want to use ? ")
                    
    if (llchoice[0]=='A' or llchoice[0]=='a'):
      if answer[i]==1:
        print(choices[i][0:choices[i].index('2')],end='')
        print("\t\t\t"+choices[i][choices[i].index('2'):choices[i].index('3')])
      elif answer[i]==2:
        print("\t\t\t"+choices[i][choices[i].index('2'):choices[i].index('3')])
        print("\n"+choices[i][choices[i].index('3'):choices[i].index('4')],end='');
      elif answer[i]==3:
        print("\n"+choices[i][choices[i].index('3'):choices[i].index('4')],end='');
        print("\t\t\t"+choices[i][choices[i].index('4'):len(choices[i])])
      else:
        print("\t\t\t"+choices[i][choices[i].index('2'):choices[i].index('3')])
        print("\t\t\t"+choices[i][choices[i].index('4'):len(choices[i])])
      llua=int(input("\nEnter your answer"))
      ll5050=False #setting lifeline indicator to false to show that it has been used
                        
                    
    if (llchoice[0]=='B' or llchoice[0]=='b'):
      print(hints[i])
      llua=int(input("\nEnter your answer"))
      llhint=False;
                    
    if (llchoice[0]=='C' or llchoice[0]=='c'):
      for d in range(2):
        llua=int(input("\nEnter your answer"))
        if llua != answer[i]:
          print('\nWrong!..You get one more guess')
          continue
      ll2guesses=False
                    
    if (llchoice[0]=='D' or llchoice[0]=='d'):
      while True: #to ensure that same question not repeated    
        rnum=random.randint(1,10)
        if  rnum not in usedquestions:
          break
      usedquestions.append(rnum)
      llua=display_question(rnum)
      llchangeq=False
                    
               
    lifelinectr-=1
                
  else:
    print("\nSorry....no more lifelines left")
    llua=int(input("\n\nEnter your answer"))
    print('\n\n\n')
  
  return llua


prizeamt=["1000.00","2000.00","3000.00","5000.00","10,000.00","20,000.00","40,000.00","80,000.00","1,60,000.00","3,20,000.00","6,40,000.00","12,50,000.00","25 Lakhs","50 Lakhs","1 Crore","7  Crores"]


    
llchoice="" # variable to accept the choice of lifeline
   
prize="" #for storing prize money amount won by player


usedquestions=[]
            
    
    

  #list for storing questions
questions = {1:"What is a custard apple called in Hindi?",2:"What is the name of the Sardar Patel statue inaugurated on 31st October?",3:"How many players are there in a basketball team?",4:'Who was the first Indian woman to win a medal in the Olympics?',5:'With which metal does oxygen combine to form rust?',6:'\'To be or not to be that is the question........... \' this famous quotation is attributed to ___',7:'Who is considered the \'Father of Indian Films\'?',8:'The fastest animal on four legs is the cheetah. How fast can it run?',9:'Which of these measures is the shortest in length?',10:'Question 4) Which of these is a board game which can normally be played by only two opponents at a time?'}
      
#list for storing choices for each question(4 choices per question
choices=["dummy choices entry to fix indexing","1.Seb 2.Sitaphal 3.Aam 4.Ramphal","1.Statue of Liberty 2.Statue of Equality 3.Statue of Fraternity 4.Statue of Unity","1.Four players 2.Five players 3.Six players 4.Eight players","1.P.T.Usha 2.Karnam Malleshwari 3.P.V.Sindhu 4.Kunjarani Devi","1.Iron 2.Platinum 3.Gold 4.Silver","1.Bernard Shaw 2.Rabindra Nath Tagore 3.Abraham Lincoln 4.William Shakespeare","1.Prithviraj Kapoor 2.Dada Saheb Phalke 3.Raj Kapoor 4.Amitabh Bachchan","1.400 km/hr 2.40 km/hr 3.110 km/hr 4.200 km/hr","1.Half-mile 2.Half foot 3.Half Yard 4.Half Metre","1.Snakes and ladders 2.Chess 3.Ludo 4.Monopoly"]

hints=["dummy choices entry to fix indexing","It also contains a girl\'s name","United we stand ....","Half of a dozen","Longest name also","Least expensive","Shake it up","There is a film award by his name","Between 100 and 200","A foot is the smallest","Hari and Suma were playing chess"]

#list to store the correct answers
answer=[0,2,4,3,2,1,4,2,3,2,2]   
rnum=0

ll5050=True  #50-50 lifeline indicator variable which is set to false after the lifeline is used by the player
llhint=True #hint lifeline indicator    
ll2guesses=True #2 guesses lifeline indicator 
llchangeq=True #change the question lifeline indicator 

oscreen()
choice = 0
useranswer=0 #variable for accepting users answer to question, also used for selecting a lifeline or  quitting the game
lifelinectr=4 #counter to keep track of lifelines used, initially 4 lifelines given

z=0 #variable to traverse prizeamt list from the start
for q in range(8):
  while True: #to ensure that same question not repeated    
    rnum=random.randint(1,10)
    if  rnum not in usedquestions:
      break
  usedquestions.append(rnum)
  

  useranswer=display_question(rnum)
  if (useranswer==9):
    useranswer=display_lifelines(rnum)
  if (useranswer==answer[rnum]):
    print("Yippee...its right")
    prize=prizeamt[z]
    z+=1
    print("You have won Rs."+prize)
  else :
    print("Sorry...wrong answer...GAME OVER...press any key to exit")
    print("You have won Rs."+prize)
    sys.exit('Terminating the game')
    
    
    input("\n\n\n\t\tPress Enter for next question")
    
