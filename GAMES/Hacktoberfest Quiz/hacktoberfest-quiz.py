print('Welcome to the Hacktoberfest 2022 Quiz')
answer=input('Are you ready to play the Quiz ? (yes/no) :')
score=0
total_questions=3
 
if answer.lower()=='yes':
    answer=input('Question 1: What programming language was this quiz created in?')
    if answer.lower()=='python':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
 
 
    answer=input('Question 2: Is one of the values of Hacktoberfest 2022 "EVERYONE IS WELCOME" ? ')
    if answer.lower()=='yes':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
 
    answer=input('Question 3: Does Hacktoberfest end on December 31?')
    if answer.lower()=='no':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
 
print('Thankyou for Playing the Hacktoberfest quiz game, you attempted',score,"questions correctly!")
mark=(score/total_questions)*100
print('Marks obtained:',mark)
print('BYE!')
