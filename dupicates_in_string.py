# this program is made to remove the second half of a string if it's identical to the first

string = 'Blue Badwagon Blue Badwagon'

def duplicate_be_gone(set_o_words):
    first_segment = (set_o_words[0:(len(set_o_words)//2)-1])
    # print(first_segment)
    set_o_words_scan = set_o_words.count(first_segment)

    if set_o_words_scan>1:
        # Python code to demonstrate
        # to find nth occurrence of substring

        occurrence = 2

        # Finding nth occurrence of substring
        val = -1
        for i in range(0, occurrence):
            val = set_o_words.find(first_segment, val + 1)

        set_o_words = set_o_words[0:val]
    return set_o_words

string = duplicate_be_gone(string)
# Printing nth occurrence
# print(string)
