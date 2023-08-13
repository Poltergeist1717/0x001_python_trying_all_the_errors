"""
Finally, copy in your previous functions and
write code that opens the file project_twitter_data.csv
which has the fake generated twitter data (the text of a tweet,
the number of retweets of that tweet, and the number of replies to that tweet).
Your task is to build a sentiment classifier, which will detect how positive or
negative each tweet is. Copy the code from the code windows above,
and put that in the top of this code window.
Now, you will write code to create a csv file called resulting_data.csv,
which contains the Number of Retweets, Number of Replies, Positive Score
(which is how many happy words are in the tweet),
Negative Score (which is how many angry words are in the tweet),
and the Net Score (how positive or negative the text is overall)
for each tweet. The file should have those headers in that order.
Remember that there is another component to this project.
You will upload the csv file to Excel or Google Sheets
and produce a graph of the Net Score vs Number of Retweets.
Check Coursera for that portion of the assignment,
if you’re accessing this textbook from Coursera.
"""






projectTwitterData = open("project_twitter_data.csv", 'r')
resultingData = open("resulting_data.csv","w")

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def strip_punctuation(string):
    for i in punctuation_chars:
        string = string.replace(i, "")
    return string

def get_pos(string):
    count_positive = 0
    #Convert all the words to lower case and get rid of punctuation
    string = strip_punctuation(string)
    string = string.lower()
    new_lst = string.split(" ")
    #Count positive words
    for word in new_lst:
        if word in positive_words:
            count_positive += 1
    return count_positive

def get_neg(string):
    count_negative = 0
    #Convert all the words to lower case and get rid of punctuation
    string = strip_punctuation(string)
    string = string.lower()
    new_lst = string.split(" ")
    #Count negative words
    for word in new_lst:
        if word in negative_words:
            count_negative += 1
    return count_negative



def writeDataInFile(resultingData):
    resultingData.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
    resultingData.write("\n")
    
    lines = projectTwitterData.readlines()
    header = lines[0]
    
    for word in lines[1:]:
        lst = word.strip().split(',')
        resultingData.write("{}, {}, {}, {}, {}".format(lst[1], lst[2], get_pos(lst[0]), get_neg(lst[0]), (get_pos(lst[0])-get_neg(lst[0]))))    
        resultingData.write("\n")

        

writeDataInFile(resultingData)
projectTwitterData.close()
resultingData.close()
