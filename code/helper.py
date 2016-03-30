import json
import pickle
import nltk.data, nltk.tag

def load_constants():
    global male_first_names,female_first_names,last_names,cities,other_features,number_as_words,word_ordinals, other_features_names, \
        tagger, adulterants, foods

    tagger = nltk.data.load(nltk.tag._POS_TAGGER)
    cities = pickle.load(open('../data/constants/cities.p','rb'))
    with open('../data/constants/male_first_names.json','rb') as outfile:
        male_first_names = set(json.load(outfile))
    with open('../data/constants/female_first_names.json','rb') as outfile:
        female_first_names = set(json.load(outfile))
    with open('../data/constants/last_names.json','rb') as outfile:
        last_names = set(json.load(outfile))
    with open('../data/constants/train_names.json','rb') as outfile:
        train_names = set(json.load(outfile))
    with open('../data/constants/number_as_words.json','rb') as outfile:
        number_as_words = set(json.load(outfile))
    with open('../data/constants/word_ordinals.json','rb') as outfile:
        word_ordinals = set(json.load(outfile))
    with open('../data/constants/adulterants.p','rb') as outfile:
        adulterants = set(pickle.load(outfile))
    with open('../data/constants/foods.p','rb') as outfile:
        foods = pickle.load(outfile)


    
    #IMP: adding train names to last names here. Comment below if you don't want this
    # last_names.update(train_names)

    other_features = [is_capital,is_digit,is_male_first_name,is_female_first_name,is_last_name,is_full_city,
    is_partial_city,contains_digit,is_short_word,is_long_word,is_number_word,is_ordinal_word,is_ordinal_num, is_adulterant]
    other_features_names = ['is_capital','is_digit','is_male_first_name','is_female_first_name','is_last_name','is_full_city',
    'is_partial_city','contains_digit','is_short_word','is_long_word','is_number_word','is_ordinal_word','is_ordinal_num']
    #other_features = []

 



# other features, return true or false
def is_capital(word):
    return word[0].isupper()

def is_adulterant(word):
    return word.lower() in adulterants

def is_food(word):
    return word.lower() in foods

def is_digit(word):
    return word.isdigit()

def is_male_first_name(word):
	return word.lower() in male_first_names

def is_female_first_name(word):
    return word.lower() in female_first_names

def is_last_name(word):
    return word.lower() in last_names

def is_full_city(word):
    return word in cities and "" in cities[word]

def is_partial_city(word):
    return word in cities and "" not in cities[word]

def contains_digit(word):
    return any(char.isdigit() for char in word)

def is_short_word(word):
    return len(word) < 4

def is_long_word(word):
    return len(word) > 8

def is_number_word(word):
    return word in number_as_words

def is_ordinal_word(word):
    return word in word_ordinals

def is_ordinal_num(word):
    return contains_digit(word) and (word.endswith('th') or word.endswith('nd') or word.endswith('st'))

def part_of_speech(word):
    return tagger.tag([word])[0][1]

def captilized(word):
    return word.istitle()

def getOtherFeatures(word):
    features = {}
    features["is_capital"] = is_capital(word)
    features["is_digit"] = is_digit(word)
    features["is_male_first_name"] = is_male_first_name(word)
    features["is_female_first_name"] = is_female_first_name(word)
    features["is_last_name"] = is_last_name(word)
    features["is_full_city"] = is_full_city(word)
    features["is_partial_city"] = is_partial_city(word)
    features["is_adulterants"] = is_adulterant(word)
    # features["is_food"] = is_food(word)
   # features["contains_digit"] = contains_digit(word)
    features["is_short_word"]= is_short_word(word)
    features["is_long_word"] = is_long_word(word)
    features["is_cap"] = captilized(word)
   # features["is_number_word"] = is_number_word(word)
   # features["is_ordinal_word"] = is_ordinal_word(word)
   # features["is_ordinal_num"] = is_ordinal_num(word)
   # features["POS_tag"] = part_of_speech(word)
    return features
