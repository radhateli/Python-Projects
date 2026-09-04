
print("\n" + "-" * 45)
print("            RADHA MINI QUIZ")
print("-" * 45)

print("\nWelcome to my mini quiz game")


# Ask the player if they want to play

play = input("\nAre you interested in the game? (yes/no): ")

if play.lower() != "yes":

    print("\n" + "-" * 45)
    print("Okay, Maybe next time...")
    print("-" * 45)
    quit()

else:

    print("\n" + "-" * 45)
    print("           LET'S PLAY :) ")
    print("-" * 45)

    score = 0

    # Question 1

    print("\n[Question 1]")

    Q1 = input("Do you know Radha ?? ")

    if Q1.lower() == "yes":
        print("Niceee :)")
        score += 1

    elif Q1.lower() == "ha":
        print("Bahut hi badiyaa :)")
        score += 1

    else:
        print("GO... and firstly know Radha, then continue the game :( ")


    # Question 2

    print("\n[Question 2]")

    Q2 = input("Is Radha's friend? ")

    if Q2.lower() == "yes":
        print("You're Lucky because you have sapphire :)")
        score += 1

    else:
        print("So why are you playing the game? :(")


    # Question 3

    print("\n[Question 3]")

    Q3 = input("Are you both together? ")

    if Q3.lower() == "yes":
        print("Then I'm sure you have a nice day :)")
        score += 1

    else:
        print("So... why are you using her laptop? :( ")


    # Final Score

percentage = (score / 3) * 100

print("\n" + "-" * 45)
print("                FINAL RESULT")
print("-" * 45)

print(f"Correct Answers : {score}/3")
print(f"Percentage      : {percentage:.2f}%")

print("\n" + "-" * 45)

if score == 3:
    print("Perfect Score, You know Radha very well :)")

elif score == 2:
    print("Good Job, You know Radha quite well :)")

elif score == 1:
    print("Not bad, You need to know Radha better :)")

else:
    print("You definitely need to know Radha better :)")

print("-" * 45)
print("\nThanks for playing :)")
print("=" * 45)