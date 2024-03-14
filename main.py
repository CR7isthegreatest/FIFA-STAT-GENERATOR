print("#########  #######  #########     #           #######  ########      #      ########      #########  ########  ##    #                   ")
print("#             #     #           #  #          ##          #        #   #       #          #          #         # #   #                   ")
print("#######       #     #######    ######           ##        #       #######      #          #  #####   #######   #  #  #                   ")
print("#             #     #         #      #            ##      #      #       #     #          #      #   #         #   # #                   ")
print("#          #######  #        #        #      #######      #     #         #    #          ########   #######   #    ##                   ")






# Methods

def check_float(prompt):
    while True:
        try:
            user_input = float(input(prompt))
            return user_input
        except:
            print("ERROR! Please enter a number!")

def check_int(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            return user_input
        except:
            print("ERROR! Please enter a whole number!")



# welcoming and name



while True:
    name = input("Enter your name to begin\n").capitalize()

    if name != "":
        print("Sup {}".format(name))
        break
    print("ERROR PLEASE ENTER A NAME!")

print("----Welcome to Fifa Stat Generator----")
print("Fifa Stat Gen is a game that is designed to give you an overal football ability rating")
print("and rate you on your other aspects of the game passing, shooting ect. and then gives you")
print("a football legend who is similar to your stats.")


# passing and shooting



shooting = 0
passing = 0
while True:

    positioning = input("Please enter what position you play out of the following: W,ST,CM,CB,GK\n").upper()

    if positioning == "ST":

        shooting = shooting + 90
        break


    elif positioning == "W":

        shooting = shooting + 80
        break



    elif positioning == "CM":

        shooting = shooting + 60
        break


    elif positioning == "CB":

        shooting = shooting + 40
        break

    elif positioning == "GK":

        shooting = 55
        break

    else:
        print("ERROR: That is not a valid input")

# heading

heading = 0

while True:

    height = check_float("Please enter how tall you are in cm:\n")
    if height > 500:
        print("Brother In Christ you are not over 5m tall")
        continue

    if height <= 0:
        print("Brother In Christ you are not Logan")
        continue

    if height >= 185:

        heading = 99
        break

    elif height > 175:

        heading = 80
        break

    elif height > 165:

        heading = 70
        break

    elif height >= 155:

        heading = 55
        break

    elif height < 155:

        heading = 40
        break

    else:

        print("ERROR: Pleas enter a valid input with only numbers.")

# dribbling

dribbling = 0

while True:

    foot_size = check_float("Please enter your shoe size in UK:\n")

    if foot_size > 500:
        print("Brother In Christ you are not logans mum")
        continue

    if foot_size <= 0:
        print("Brother In Christ you are not Logan")
        continue

    if foot_size >= 14:

        dribbling = 55
        break

    elif foot_size > 11:

        dribbling = 60
        break

    elif foot_size > 9:

        dribbling = 70
        break

    elif foot_size > 8:

        dribbling = 80
        break

    elif foot_size <= 7:

        dribbling = 99
        shooting = shooting + 9
        break

    else:
        print("ERROR: Pleas enter a valid input with only numbers.")

# speed

speed = 0

while True:

    sprint_time = check_int("Please enter your 100m sprint time:\n")
    if sprint_time > 500:
        print("Brother In Christ you are not Logan")
        continue

    if sprint_time <= 1:
        print("Brother In Christ you are not Aaron")
        continue

    if sprint_time <= 10:

        speed = 99
        break

    elif sprint_time <= 12:

        speed = 80
        break

    elif sprint_time <= 14:

        speed = 70
        break

    elif sprint_time <= 16:

        speed = 60
        break

    elif sprint_time >= 17:

        speed = 50
        break

    else:
        print("ERROR: Please enter a valid input.")

# passing

passing = 0

while True:
    friends = check_int("Please enter how many friends you have:\n")
    if friends > 500:
        print("Brother In Christ you are not Aaron")
        continue

    if friends <= 0:
        print("Brother In Christ you are not Logan")
        continue

    if friends >= 14:

        passing = 99
        break

    elif friends >= 10:

        passing = 80
        break

    elif friends >= 9:

        passing = 70
        break

    elif friends >= 6:

        passing = 60
        break

    elif friends < 6:

        passing = 55
        break
    else:

        print("Please enter a number")

# calculating the overall rating

overall_rating = heading + shooting + dribbling + passing + speed

overall_rating = overall_rating / 5

print("These are your ratings {}:".format(name))

print("Shooting: {}".format(shooting))
print("Heading: {}".format(heading))
print("Dribbling: {}".format(dribbling))
print("Speed: {}".format(speed))
print("Passing: {}".format(passing))
print("Overall: {}".format(round(overall_rating)))


# Lists
footballer_names = ["Haaland", "Lionel Messi", "Sergio Ramos", "Kevin De Bruyne", "Harry Maguire", "Cristiano Roanldo"]
print("Your footballer legend is:")

while True:
    if overall_rating >= 90:
        print(footballer_names[5])
        break

    if shooting >= 80:
        print(footballer_names[0])
        break

    if dribbling >= 80:
        print(footballer_names[1])
        break

    if heading >= 80:
        print(footballer_names[2])
        break

    if passing >= 80:
        print(footballer_names[3])
        break

    else:
        print(footballer_names[4])
        break

