#counter to keep track of strokes and score for golf
#asking user to define number of holes
num_holes = int(input("Enter number of holes: "))
#initialising arrays to store all strokes and scores and pars for the pars
score = [0] * num_holes
strokes = [0] * num_holes
pars = [0] * num_holes
total_strokes = 0
total_score = 0


allerton = [4, 4, 4, 3, 4, 4, 4, 3, 3, 4, 4, 3, 4, 4, 4, 4, 3]
bowring = [4, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 4, 4, 4, 4, 4]
#pars = allerton

course_par = sum(pars)

#setting up indicator for user to decide whether to enter pars for the course or not
user_par_ind = input("Enter pars? [Y/N]: ")

#while loop to continue prompting an answer if user doesnt enter y or n
while user_par_ind != "n" and user_par_ind != "N" and user_par_ind != "Y" and user_par_ind != "y":
    print("Not recognised, try again")
    user_par_ind = input("Enter pars? [Y/N]: ")
    print("")

#let user enter pars for each hole
if user_par_ind == "Y" or user_par_ind == "y":
    for x in range(0, num_holes):
        pars[x] = int(input("Par for Hole "+ str(x+1) + ": "))

print("")

i = 0
#while loop to track users strokes and calculate score
while i < num_holes:

    hole_num = i + 1
    print("Hole " + str(hole_num))

    strokes[i] = int(input("Enter strokes for Hole " + str(hole_num) + ": "))
    score[i] = strokes[i] - pars[i]
    total_strokes = sum(strokes)
    total_score = sum(score)
    #if no par entered then we don't display the score
    if pars[i] == 0:
        print("Total Strokes: " + str(total_strokes))

    if total_score > 0 and pars[i] != 0:
        print("Total Strokes: " + str(total_strokes) + " (+" + str(total_score) + ")")

    if total_score < 1 and pars[i] != 0:
        print("Total Strokes: " + str(total_strokes) + " (" + str(total_score) + ")")

    print("")
    i = i + 1
