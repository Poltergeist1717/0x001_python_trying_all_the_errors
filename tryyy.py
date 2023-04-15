def print_questions():
    print ("There are only 20 questions per subject.\nThere are 4 options per question.\nPick the correct answer from the options.\n")
    print ("Which Subject are you starting with?")
    print("A. Mathematics\nB. English Language\nC. Current Affairs?")
    subject_answer_input = input ("Enter A, B, Or C: ")

    if subject_answer_input == "A":
        print ("\t\tMATHEMATICS\n")
        print ("Question 1\n")
        with open ("C:\Programming Projects\Grader\Mathematics Questions\\mth_qst1.txt", "r") as math_question:
            read_math_question_1 = math_question.read()
            print (read_math_question_1)
            print ("A. 900\nB. 800\nC. 700\nD. 400")
            answer_input = input ("Enter A, B, Or C: ")
            check_answer_input(answer_input)
        #print_total_score()
            
    elif subject_answer_input == "B":
        print ("ENGLISH LANGUAGE")
        print ("Question 1\n")
        with open ("C:\\Programming Projects\\Grader\\Eng Lang Questions\\eng_lang_qst1.txt", "r") as eng_question:
            read_eng_question_1 = eng_question.read()
            print (read_eng_question_1)
            print ("A. 900\nB. 800\nC. 700\nD. 400")
            answer_input = check_answer_input(answer_input)
            
    elif subject_answer_input == "C":
        print ("CRRENT AFFAIRS")
        print ("Question 1\n")
        with open ("C:\\Programming Projects\\Grader\\Current Affairs Questions\\Curr_affrs_qst1.txt", "r") as curr_affrs_question:
            read_curr_affrs_question_1 = curr_affrs_question.read()
            print (read_curr_affrs_question_1)
            print ("A. 900\nB. 800\nC. 700\nD. 400")
            answer_input = check_answer_input(answer_input)
    else:
        print ("Invalid input!\nPlease enter A, B, C or D in capital letter.\n")
        print_questions()

def reg_scores(answer_input):
    subject_answer_indx = 1
    answer_score = 0
    with open ("C:\\Programming Projects\\Grader\\Mathematics Answers\\mth_answr1.txt", "r") as answers:
        read_answers = answers.read()
        answer_data = read_answers.split(".")
        if answer_input in answer_data[subject_answer_indx]:
            answer_score += 5
        else:
            answer_score += 0
            return
    subject_answer_indx += 2
    with open ("", "w") as write_scores_registery:
        write_scores_record = scores_registery.write(answer_score)
    
def print_total_score():
    with open ("", "r") as read_scores_registry:
        read_scores_record = read_scores_registry.read()
        print (read_scores_record)


    
def check_answer_input(answer_input):
    if answer_input in ("A", "B", "C", "D"):
        reg_scores(answer_input)
    else:
        print ("Your answer can only be A, B, C or D in capital letter.")
        answer_input = input ("Enter A, B, Or C: ")

def close():
    x = input ("Enter 0 to exit: ")
    if x == 0:
        print ("You have exited program!")
        return 0

def main ():
    print_questions()
    return close()

main()




    
