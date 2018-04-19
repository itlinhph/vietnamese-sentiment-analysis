import re
import nltk
import emoji
import yaml
from pyvi import ViTokenizer


def remove_special_text(tweet):
    tokens = re.sub(r'(http\S+)|(@\S+)|RT|\#|!|:|\.|,', ' ', tweet)
    
    return tokens


def load_dictionary(filename):
    vndict = {}
    dict_file = open(filename, 'r').read().split('\n')
    for line in dict_file:
        if line == "":
            continue
        line = line.split('\t')
        score = [int(line[1]), int(line[2])]
        vndict[line[0].strip()] = score
    return vndict

def load_boost_word(filename):
    boost_word = {}
    boost_file = open(filename, 'r').read().split('\n')
    for line in boost_file:
        if line == "":
            continue
        word, score = line.partition("\t")[::2]
        # print(word, score)
        boost_word[word.strip()] = int(score)
    return boost_word

def boost_word_score(i, tokens):
    
    listword = []

    if i < len(tokens)-1:
        after_word = tokens[i+1]
        listword.append(after_word)
        if i< len(tokens) -2:
            after_word2 = tokens[i+2]
            listword.append(after_word2)
    if i>0:
        prev_word = tokens[i-1]
        listword.append(prev_word)
        if i>1:
            prev_word2 = tokens[i-2]
            listword.append(prev_word2)
    
    list_score = []
    for word in listword:
        if word in boost_dict:
            list_score.append(boost_dict[word])
    score = sum(list_score)
    if score == 0:
        score = 1 
    
    return score

def evalue_score(tokens):
    pos_score = 0
    neg_score = 0
    for i,word in enumerate(tokens):
        if word in vndict:
            pos_score += (vndict[word][0] * boost_word_score(i, tokens) )
            neg_score += (vndict[word][1] * boost_word_score(i, tokens))
            # print(word, boost_word_score(i, tokens), "Pos: ", pos_score, "Neg: ", neg_score)
    
    return pos_score , neg_score

def pre_process(tweet):

    tweet = ViTokenizer.tokenize(tweet)             # Tokenizer Vietnamese
    tokens = remove_special_text(tweet)             # Remove special text
    tokens = emoji.demojize(tokens)                 # Convert emojition to text
    tokens = tokens.lower()                         # To lowercase
    tokens = tokens.split()                         # Tokenize tweet
    
    return tokens

def process_dataset(input_file, output_file):
    
    data = open(input_file, 'r').read().split('\n')
    print("input length:",len(data))
    id = 1
    str_file = "ID\tPositive_score\tNegative_score\tContent\n"

    for tweet in data:
        tokens = pre_process(tweet)
        tweet = tweet.replace("\n", " ")

        #Evalue score:
        pos_score, neg_score = evalue_score(tokens)
        
        str_file += str(id) + "\t"+ str(pos_score) +"\t" + str(neg_score) + "\t" + tweet + "\n"
        id+=1

    #write data
    text_file = open(output_file, "w")
    text_file.write(str_file)
    text_file.close()


#Load file:
vndict = load_dictionary("dictionary/vndict.txt")               # Main dictinary
emoji_dict = load_dictionary("dictionary/emoji-dict.txt")   # Emoji dictionary
boost_dict = load_boost_word('dictionary/boost-words.txt')  # Boost dictionary

# Update dictionary with emoji score:
vndict.update(emoji_dict)

process_dataset('input/dataset.txt', 'output/output.txt')

# tweet = "mẹ kiếp em ghét writing vcl :) trời má bth 120 rặn mệt vl giờ 160 chữ"
# tokens = pre_process(tweet)
# pos, neg = evalue_score(tokens)
# print(tokens)
# print("pos:", pos, "neg: ", neg)
