# this function filters out from a string (set_o_words) anything
# that comes
# ====== BEFORE ======
# another specified string or letter (cur_letter)
def post_filter(set_o_words, cur_letter):
    index = set_o_words.find(cur_letter)
    set_o_words = (set_o_words[index:])
    return set_o_words

# this function filters out from a string (set_o_words) anything
# that comes
# ===== AFTER =======
# another specified string or letter (cur_letter)
def pre_filter(set_o_words, cur_letter):
    index = set_o_words.find(cur_letter)
    set_o_words = (set_o_words[:index])
    return set_o_words

# convert sets of spaces into new lines
def space_removal(set_o_words, x):
    while x >= 2:
        space = (" ")
        spaces = (space * x)
        set_o_words = set_o_words.replace(spaces, '\n')
        x = x - 1
    return set_o_words

def first_letter_filter(set_o_words):
    string_len = len(set_o_words)
    list(set_o_words)
    start = 0
    while start < string_len:
        cur_letter = (str(set_o_words[start]))
        sstring = str(cur_letter.isalpha())
        if sstring == 'True':
            break
        start += 1
    index = set_o_words.find(cur_letter)
    set_o_words = (set_o_words[index:])
    return set_o_words

## This function filters a list of strings for items
# without/without a certain group of characters in them
def str_list_filter(badstring, mylist, keep):
    if keep == 'keep':
        # list of strings with badstring
        newlist = [x for x in mylist if badstring in x]

    if keep == 'remove':
        # list of strings without badstring
        newlist = [x for x in mylist if badstring not in x]
    return(newlist)

# This function replaces characters (called bad_chars)
# in a string (set_o_words) with other characters (new_chars)
def bad_chars_removal(bad_chars, set_o_words, new_chars):
    start = 0
    while start < len(bad_chars):
        set_o_words = \
            set_o_words.replace(bad_chars[start],new_chars)
        start +=1
    return set_o_words

# string = bad_chars_removal(bad_chars_list,string,'')