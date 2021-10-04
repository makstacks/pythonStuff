# counter to keep track of strokes and score for golf
import csv


# asking user to define number of holes, default to 18 if no answer given
def start_round():
    num_holes = input("Enter number of holes: \n>")
    if num_holes == "0":
        print("Number of holes defaulted to 18.\n")
        num_holes = 18
    elif num_holes.isdigit():
        num_holes = int(num_holes)
    else:
        start_round()

    # initialising arrays to store all strokes and scores and pars for the pars
    pars = [0] * num_holes
    score = [0] * num_holes
    strokes = [0] * num_holes
    # calling get_pars function to obtain user selection for pars/ no pars
    pars = get_par_ind(num_holes)
    #saving out course name
    course = str(pars[-1])
    if course.isdigit() == False:
        print(course)
        course = "Par (" + course + ")"
    #saving out list with pars
        pars = pars[0][0:num_holes]
    p = len(pars)
    if p > num_holes:
        while p > num_holes:
            del pars[p-1]
            p -= 1
    total_par = sum(pars)
    # loop through each hole to be played and get user strokes for each
    for i in range(num_holes):
        strk = enter_strokes(i, pars)
        while not strk.isdigit():
            print("Not recognised. Try again.")
            strk = enter_strokes(i, pars)

        strokes[i] = int(strk)
        score[i] = strokes[i] - pars[i]
        total_strokes = sum(strokes)
        total_score = sum(score)
        # if no par entered then we don't display the score
        if pars[i] == 0:
            print("Total Strokes: " + str(total_strokes) + " through " + str(i + 1))
            print("")
        elif total_score < 0:
            print("Total Strokes: " + str(total_strokes) + " (" + str(total_score) + ") through " + str(i + 1))
            print("")
        else:
            print("Total Strokes: " + str(total_strokes) + " (+" + str(total_score) + ") through " + str(i + 1))
            print("")

    holes_list = []
    for j in range(1, num_holes + 1):
        holes_ins = j
        holes_list.append(holes_ins)
    # holes_list.insert("Hole")
    holes_list.insert(0, "Hole")

    strokes_list = []
    for k in range(1, num_holes + 1):
        strokes_ins = strokes[k - 1]
        strokes_list.append(strokes_ins)
    strokes_list.append(total_strokes)
    strokes_list.insert(0, "Strokes")

    pars_list = []
    for l in range(1, num_holes + 1):
        pars_ins = pars[l - 1]
        pars_list.append(pars_ins)
    pars_list.append(total_par)
    if course.isdigit() == False:
        pars_list.insert(0, course)
    else:
        pars_list.insert(0, "Par")

    score_list = []
    for m in range(1, num_holes + 1):
        score_ins = str(score[m - 1])
        tot_sc_str = str(total_score)
        if score[m - 1] > - 1:
            score_ins = "+" + score_ins
            tot_sc_str = "+" + tot_sc_str
        score_list.append(score_ins)
    score_list.append(tot_sc_str)
    score_list.insert(0, "Score")

    # compile the lists into one
    round_stats = []

    if sum(pars) > 0:
        round_stats.insert(0, score_list)
        round_stats.insert(0, strokes_list)
        round_stats.insert(0, pars_list)
        round_stats.insert(0, holes_list)
        header = ["Hole", "Par", "Strokes", "Score"]
    else:
        round_stats.insert(0, strokes_list)
        round_stats.insert(0, holes_list)
        header = ["Hole", "Strokes"]
#call function which asks whether user wants to save results and saves out csv file if so
    create_csv(round_stats)

def create_csv(round_stats):
    import csv
#let user select whether to save out their round and choose file name
    save_round_q = input("Save round? \n[y] Yes \n[n] No \n>")
    if save_round_q == "y" or save_round_q == "Y":
        csv_name = input("Enter file name: \n>")
        csv_rowlist = [round_stats]
        with open(csv_name + '.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerows(csv_rowlist)

            print("Bye, have a beautiful time")
    elif save_round_q == "n" or save_round_q == "N":
        print("Bye, have a beautiful time")
    else:
        create_csv(round_stats)


# letting user choose course/enter pars for the course or not
def get_par_ind(num_holes):
    user_par_ind = input("Enter pars? \n[y] Yes \n[n] No \n> ")
    if user_par_ind == "y" or user_par_ind == "Y":
        return get_pars(num_holes)
    elif user_par_ind == "n" or user_par_ind == "N":
        pars = [0] * num_holes
        return pars
    else:
        return get_par_ind(num_holes)


def get_pars(num_holes):
    # preset courses
    allerton = [4, 4, 4, 3, 4, 4, 4, 3, 3, 4, 4, 3, 4, 4, 4, 4, 3]
    bowring = [4, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 4, 4, 4, 4, 4]
    pebble_beach = [4, 4, 4, 4, 3, 5, 3, 4, 4, 4, 4, 3, 4, 5, 4, 4, 3, 5]
    paynes_valley = [4, 3, 4, 5, 3, 4, 4, 5, 4, 3, 4, 4, 5, 4, 4, 3, 4, 5, 3]
    # get response from user
    course = ""
    par_res = input(
        "Enter pars or select course: \n[e] Enter pars \n[a] Allerton Golf Course \n[b] Bowring Park \n[p] Pebble Beach Golf Links \n[v] Payne's Valley \n>")
    if par_res == "a" or par_res == "A":
        pars = allerton
        course = "Allerton"
        return pars, course
    elif par_res == "b" or par_res == "B":
        pars = bowring
        course = "Bowring"
        return pars, course
    elif par_res == "p" or par_res == "P" or par_res == "pb" or par_res == "PB":
        pars = pebble_beach
        course = "Pebble Beach"
        return pars, course
    elif par_res == "v" or par_res == "V" or par_res == "PV" or par_res == "pv":
        pars = paynes_valley
        course = "Payne's Valley"
        return pars, course
    elif par_res == "e" or par_res == "E":
        return enter_pars(num_holes)
    else:
        return get_pars(num_holes)



# let user enter pars for all holes
def enter_pars(num_holes):
    pars_entered = [0] * num_holes
    for j in range(num_holes):
        pars_entered[j] = int(input("Enter par for Hole " + str(j + 1) + ":\n> "))
    return pars_entered


# let user enter strokes for given hole
def enter_strokes(k, pars):
    hole_num = k + 1
    if pars[k] > 0:
        print("Hole " + str(hole_num) + ", Par " + str(pars[k]))
    else:
        print("Hole " + str(hole_num))

    stroke = input("Enter strokes: ")
    return stroke

start_round()
