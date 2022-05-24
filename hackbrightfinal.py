def welcome_message():
  print("Welcome to Did you You Know? A trivia game about Black Female Composers in the Diaspora")

print("-------------------")
welcome_message()

name = input("What is your name?")
print(f"Welcome {name}")
answer=input('Are you ready to play the Quiz ? (type Yes or No):  ')


score=0
total_questions=6


if answer.title()=='Yes':

    answer=input('Question 1: Julia Perry was taught by which famous French female pianist and composer?  ')
  
    if answer.title()== 'Nadia Boulanger':
       score +=1
       print('You are correct!')
       
    else:
       print('Sorry, incorrect answer')
     


    answer=input('Who wrote the opera "Halelujah" inspired by Dr. Martin Luther King?')                                                                                                                                                                                                                                                                                         
  
    if answer.title()== 'Eva Jessye':
       score +=1
       print("That's right! Way to go!")
   
    else:
       print('Sorry, wrong answer')
    
    answer=input('Question 3: This UK Composer was nominated for  BBC Young Composer of the year in 2012  ')
   
    if answer.title()== 'Cassie Kinoshi':
       score +=1 
       print('Super! Correct!')
     
    else:
       print('That is incorrect, try again')
            
    answer=input("Question 4: This Cuban pianist/composer started playing piano at 4 years old and is known for her opera 'Scourge of Haycinths'  ")

    if answer.title()== 'Tania Leon':
       score+=1
       print('Wow! You are doing great!')
   
    else:
       print(' Sorry that is not correct')

             
    answer=input('Question 5: This Atlanta, Gerogia legendary pianist compose "Black Christ of the Andes" played with jazz giants, Thelonius Monk and Art Blakey  ')
    if answer.title()== 'Mary Lou Williams':
       score +=1
       print('Amazing job!')

    else:
       print('Ooo, so close! Great effort!')

    answer=input('Question 6: This world renowned vocal composer from Nigeria also has a PhD in Digital Forensics!')
    if answer.title()=='Edewede Oriwoh':
       score+=1
       print('Awesome work! Congratulations!')
    else:
       print('Oops.Wrong answer')
             
print(f'Thanks for playing {name}! You answered {score} correctly!')
final_score =(score/total_questions)*100
print('Your final score is: ',final_score)
print('Thanks for playing and hope to play again soon!Hope to play again soon!')
                 
        
    





