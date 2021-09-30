#counter to keep track of strokes and score for golf
#asking user to define number of holes, default to 18 if no answer given
def start_round():
    num_holes = input("Enter number of holes: ")
    if num_holes == "0":
        print("Number of holes defaulted to 18.\n")
        num_holes = 18
    elif num_holes.isdigit():
        num_holes = int(num_holes)
    else:
        start_round()

    #initialising arrays to store all strokes and scores and pars for the pars
    pars = [0] * num_holes
    score = [0] * num_holes
    strokes = [0] * num_holes

    pars = get_par_ind(num_holes)

    for i in range(num_holes):
        strk = enter_strokes(i, pars)
        while not strk.isdigit():
            print("Not recognised. Try again.")
            strk = enter_strokes(i, pars)

        strokes[i] = int(strk)
        score[i] = strokes[i] - pars[i]
        total_strokes = sum(strokes)
        total_score = sum(score)
        #if no par entered then we don't display the score
        if pars[i] == 0:
            print("Total Strokes: " + str(total_strokes) + " through " + str(i+1))
        elif total_score < 0:
            print("Total Strokes: " + str(total_strokes) + " (" + str(total_score) + ") through "  + str(i+1))
        else:
            print("Total Strokes: " + str(total_strokes) + " (+" + str(total_score) + ") through "  + str(i+1))



#letting user choose course/enter pars for the course or not
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
#preset courses
    allerton = [4, 4, 4, 3, 4, 4, 4, 3, 3, 4, 4, 3, 4, 4, 4, 4, 3]
    bowring = [4, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 4, 4, 4, 4, 4]
    pebble_beach = [4, 4, 4, 4, 3, 5, 3, 4, 4, 4, 4, 3, 4, 5, 4, 4, 3, 5]
#get response from user
    par_res = input("Enter pars or select course: \n[e] Enter pars \n[a] Allerton Golf Course \n[b] Bowring Park \n[p] Pebble Beach Golf Links\n> ")
    if par_res == "a" or par_res == "A":
        pars = allerton
        return pars
    elif par_res == "b" or par_res == "B":
        pars = bowring
        return pars
    elif par_res == "p" or par_res == "P" or par_res == "pb" or par_res == "PB":
        pars = pebble_beach
        return pars
    elif par_res == "e" or par_res == "E":
        return enter_pars(num_holes)
    else:
        return get_pars(num_holes)

#let user enter pars for all holes
def enter_pars(num_holes):
    pars_entered = [0] * num_holes
    for j in range(num_holes):
        pars_entered[j] = int(input("Enter par for Hole " + str(j + 1) + ":\n> "))
    return pars_entered

#let user enter strokes for given hole
def enter_strokes(k, pars):
    hole_num = k + 1
    if pars[k] > 0:
        print("Hole " + str(hole_num) + ", Par " + str(pars[k]))
    else:
        print("Hole " + str(hole_num))
    stroke = input("Enter strokes: ")
    return stroke

start_round()
