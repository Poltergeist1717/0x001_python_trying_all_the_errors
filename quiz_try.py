def print_questions():
    print ("There are only 20 questions per subject.\nThere are 4 options per question.\nPick the correct answer from the options.\n")
    print ("Which Subject are you starting with?")
    print ("A. Mathematics\nB. English Language\nC. Current Affairs?")
    subject_answer_input = input ("Enter A, B, Or C: ")


    if subject_answer_input == "A":
        print ("\t\tMATHEMATICS\n")
        question_files()
            
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
        print ("Invalid input!\nPlease enter A, B, or C in capital letter.\n")
        print_questions()

def question_files():
    import os

    qst_numb_count = 0

    question_files_list = []
    x = 0

    path = "C:\Programming Projects\Grader\Mathematics Questions"
    questions_folder = os.listdir(path)

    for files in questions_folder:
        #print (files)
        question_files_list.append(files)

    #print (y)

    for data in range (0, len(question_files_list) + 1):
        data = "mth_qst({}).txt".format(x)
        if data in question_files_list:

            #Assigns names of question_files to varaible question_files_names
            question_files_names = data
            #Prints the question number 
            print ("Question {}\n".format(qst_numb_count))
            with open ("C:\Programming Projects\Grader\Mathematics Questions\{}".format(question_files_names), "r") as anything:
                sup = anything.read()
                print (sup)
                print ("A. 900\nB. 800\nC. 700\nD. 400")
                answer_input = input ("Enter A, B, C Or D: ")
                check_answer_input(answer_input)
                print ("\n")

        x += 1
        qst_numb_count += 1


    """
    This function checks answer_input if it's correct
    by reading the file where the answers are stored
    This function also keeps record of the user's score
    by increasing the score by 5 for each correct answer
    Calls write_print_total_score function to register and print scores
    """
    
def reg_scores(answer_input):
    answer_score = 0
    subject_answer_indx = 1
    with open ("C:\\Programming Projects\\Grader\\Mathematics Answers\\mth_answr1.txt", "r") as answers:
        read_answers = answers.read()
        answer_data = read_answers.split(".")
        for data in answer_data:
            data_index = answer_data[subject_answer_indx]
            if answer_input == data_index:
                answer_score += 5
            else:
                answer_score += 0
                break

    subject_answer_indx += 2
    write_and_print_score(answer_score)

    """
    This function writes the user's score to a file
    Prints the registered scores
    """

def write_and_print_score(answer_score):
    with open ("C:\\Programming Projects\\Grader\\Mathematics Answers\\score_registry.txt", "w") as write_scores_registry:
        write_scores_record = write_scores_registry.write(str(answer_score))
        
    with open ("C:\\Programming Projects\\Grader\\Mathematics Answers\\score_registry.txt", "r") as read_scores_registry:
        read_scores_record = read_scores_registry.read()
        print ("Your final score for this subject is: ", read_scores_record)

    """
    This function checks answers
    Calls reg_scores function to register scores
    
    """
def check_answer_input(answer_input):
    if answer_input in ["A", "B", "C", "D"]:
        reg_scores(answer_input)
    else:
        print ("Your answer can only be A, B, C or D in capital letter.")
        answer_input = input ("Enter A, B, C Or D: ")

    """
    This function closes or restart progam
    Takes input from user to either close or restart program
    """

def close():
    print ("Enter 0 to quit 0r 1 to continue.")
    x = input ("Enter: ")
    try:
        if x == "1":
            print_questions()
        elif x == "0":
            print ("You have exited program!")
            return None
        else:
            print ("Inavlid input!")
            close()
    except:
        print ("Invalid input")
        close()
    return 0

def main ():
    print_questions()
    return close()

main()
