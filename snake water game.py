import random
width=140
print("\n\n")
print("SNAKE WATER GAME".center(width,'-'))
no_of_times=int(input("Enter the number of times you want to play the game: ")) #input no of turns
print("Press S for SNAKE \nPress W for WATER \nPress G for GUN\n")
choices_list=['S','W','G']
score_user=0             #initial scores
score_comp=0
for i in range(no_of_times):
    user=input("Enter your choice: ")
    comp_ch=random.choice(choices_list)

    if user==comp_ch:
        print(f"Computer chooses {comp_ch} and You chose {user}")
        print("Tie\n")

    elif user=='S' and comp_ch=='W':
        score_user=score_user+1
        print(f"Computer chooses {comp_ch} and You chose {user}")
        print(f"Your score = {score_user}")
        print(f"Computer score= {score_comp}\n")
    
    elif user=='S' and comp_ch=='G':
        score_comp=score_comp+1
        print(f"Computer chooses {comp_ch} and You chose {user}")
        print(f"Your score = {score_user}")
        print(f"Computer score= {score_comp}\n")

    elif user=='W' and comp_ch=='S':
        score_comp=score_comp+1
        print(f"Computer chooses {comp_ch} and You chose {user}")
        print(f"Your score = {score_user}")
        print(f"Computer score= {score_comp}\n")

    elif user=='W' and comp_ch=='G':
        score_user=score_user+1
        print(f"Computer chooses {comp_ch} and You chose {user}")
        print(f"Your score = {score_user}")
        print(f"Computer score= {score_comp}\n")

    elif user=='G' and comp_ch=='S':
        score_user=score_user+1
        print(f"Computer chooses {comp_ch} and You chose {user}")
        print(f"Your score = {score_user}")
        print(f"Computer score= {score_comp}\n")

    elif user=='G' and comp_ch=='W':
        score_comp=score_comp+1
        print(f"Computer chooses {comp_ch} and You chose {user}")
        print(f"Your score = {score_user}")
        print(f"Computer score= {score_comp}\n")

    print(f"You are left with {no_of_times-i-1} chances\n")

print(f"Your score is {score_user}")
print(f"Computer's score is {score_comp}\n")

if score_user>score_comp:
    print("CONGRATULATIONS! You Won!!")

elif score_comp>score_user:
    print("Oops, You Lost!")

else:
    print("Match Draw")

print("GAME OVER".center(100,'-'))






    





        

