num_holes = int(input("Enter number of holes: "))
total_shots = 0
total_score = 0
score = [0] * num_holes
shots = [0] * num_holes

allerton = [4, 4, 4, 3, 4, 4, 4, 3, 3, 4, 4, 3, 4, 4, 4, 4, 3]
bowring = [4, 3, 4, 4, 4, 4, 4, 4, 4]
course = allerton
course_par = sum(allerton)

i = 0

while i < num_holes:
    hole_num = i + 1
    print("Hole " + str(hole_num))

    shots[i] = int(input("Enter shots for Hole " + str(hole_num) + ": "))
    score[i] = shots[i] - course[i]
    total_shots = sum(shots)
    total_score = sum(score)
    if total_score > 0:
        print("Total Shots: " + str(total_shots) + " (" + "+" + str(total_score) + ")" )
    if total_score < 1:
        print("Total Shots: " + str(total_shots) + " (" + str(total_score) + ")" )

    print("")

    i = i + 1


