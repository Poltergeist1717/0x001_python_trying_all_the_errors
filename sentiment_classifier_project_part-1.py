
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

def strip_punctuation(puncts):
    for punct in punctuation_chars:
        puncts = puncts.replace(punct, "")
    return puncts

def get_pos(words):
    text = strip_punctuation(words)
    text_2 = text.lower().split()
    count = 0
    for word in text_2:
        if word in positive_words:
            count += 1
    return count  

def get_neg(words):
    count = 0
    text = strip_punctuation(words)
    words = text.lower().split()
    for word in words:
        if word in negative_words:
            count += 1
    return count

def project_twitter_data_csv():
    with open ("project_twitter_data.csv", "r") as prj_twt_data:
        twitter_data_read = prj_twt_data.readlines()
        return twitter_data_read
            
def twitter_data_read_values():
    twitter_data_read = project_twitter_data_csv()
    values = []
    for line in twitter_data_read:
        value = line.strip().split(",")
        values.append(value)
    return values

def tweet_text_data_list():
    datas = twitter_data_read_values()
    tweet_text_list = []
    for data in datas:
        tweet_text_list.append(data[0]) 
    return tweet_text_list 

def retweet_count_data_list():
    datas = twitter_data_read_values()
    retweet_count_list = []
    for data in datas:
        retweet_count_list.append(data[1])
    return retweet_count_list

def reply_count_data_list():
    datas = twitter_data_read_values()
    reply_count = []
    for data in datas:
        reply_count.append(data[2]) 
    return reply_count 
       
def neg_sentiment_list():
    datas = tweet_text_data_list()
    negative_setmnt_list = []
    for data in datas[1:]:
        negative = get_neg(data)
        negative_setmnt_list.append(negative)
    return negative_setmnt_list

def pos_sentiment_list():
    datas = tweet_text_data_list()
    positive_setmnt_list = []
    for data in datas[1:]:
        positive = get_pos(data)
        positive_setmnt_list.append(positive)
    return positive_setmnt_list

def net_neg_sentiment_count():
    datas = neg_sentiment_list()
    count = 0
    for data in datas:
        count += data
    return count

def net_pos_sentiment_count():
    datas = pos_sentiment_list()
    count = 0
    for data in datas:
        count += data
    return count    

def neg_sentiment_count():
    datas = neg_sentiment_list()
    count = 0
    for data in datas:
        if data != 0:
            count += 1
    return count   
    
def pos_sentiment_count():
    datas = pos_sentiment_list()
    count = 0
    for data in datas:
        if data != 0:
            count += 1
    return count

def numb_retweet_count():
    datas = retweet_count_data_list()
    count = 0
    for data in datas:
        if data != 0:
            count += 1
    return count

def numb_reply_count():
    datas = reply_count_data_list()
    count = 0
    for data in datas:
        if data != 0:
            count += 1
    return count

def net_pos_neg_sentiment():
    net_negative = net_neg_sentiment_count()
    net_positive = net_pos_sentiment_count()
    
    if net_negative < net_positive:
        return net_positive
    elif net_positive < net_negative:
        return net_negative
    else:
        return 0


def sentiment_classifier():
    result_data = [["Number of Retweets", "Number of Replies", "Positive Score", "Negative Score", "Net Score"]]
    
    retweets = numb_retweet_count()
    replies = numb_reply_count()
    positive_score = pos_sentiment_count()
    negative_score = neg_sentiment_count()
    net_score = net_pos_neg_sentiment()
    
    result_data.append([retweets, replies, positive_score, negative_score, net_score])
    
    return result_data


with open ("resulting_data.csv", "w") as rslt_data:
    resulting_data_write = rslt_data.write(sentiment_classifier())
