# Step 1
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

def strip_punctuation(word):
    New_word=""  
    print("Current Word is: ", word)
    for alpha in word:
        if alpha not in punctuation_chars:
            New_word = New_word + alpha
    return New_word

# Step 2
# list of positive words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())
            
def get_pos(string):
    string_Lower = string.lower()
    string_punc_removed = strip_punctuation(string_Lower)
    print("Punctuation Removed: ", string_punc_removed)
    splitted_string = string_punc_removed.split()
    print("Splitted String: ",splitted_string)
    
    pos_count = 0
    for word in splitted_string:
        if word in positive_words:
            pos_count += 1
    return pos_count


# Step 3
negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())


def get_neg(string):
    string_lower = string.lower()
    string_No_punc = strip_punctuation(string_lower)
    splitted_string = string_No_punc.split()
    
    neg_word = 0
    for word in splitted_string:
        if word in negative_words:
            neg_word += 1
    return neg_word


# Step 4