import pandas as pd
import json


import dupicates_in_string
from string_and_list_opperations import *
from link_extraction import working_with
from link_extraction import final_links_list
links = final_links_list

# from Text_Input_Window import string
# links = string
# links = string.split(", ")

#import the file dropdown menu to select whether your working with drivers, gliders or karts
from dropdown_menu import selection as working_with

start = 0

# To have a different values written to final file...
# when appropriate and to write to the right file
if working_with == 'Drivers':
    class_name = 'race_tool'
    first_best_setname = '_3items'
    second_best_setname = '_2items'
    final_file = "C:/Users/jkruz/Desktop/Test/Webscraper/Mario_Kart_Tour_drivers2.py"

elif working_with == 'Karts':
    class_name = 'race_tool'
    first_best_setname = '_TWO_x_Bonus_Points'
    second_best_setname = '_ONEoFIVE_x_Bonus_Points'
    final_file = "C:/Users/jkruz/Desktop/Test/Webscraper/Mario_Kart_Tour_karts2.py"

elif working_with == 'Gliders':
    class_name = 'race_tool'
    first_best_setname = '_3x_Combo_Boost'
    second_best_setname = '_2x_Combo_Boost'
    final_file = "C:/Users/jkruz/Desktop/Test/Webscraper/Mario_Kart_Tour_gliders2.py"

final_string = ('import weakref\n\nclass ' + class_name +':\n\t_instances = set()\n\n\tdef __init__(self, name, rarity, three_items = {}, two_items = {}, lv3_courses = {}, lv6_courses = {}):\n\t\tself.name = name\n\t\tself.rarity = rarity\n\t\tself._instances.add(weakref.ref(self))\n\t\tself.three_items = three_items\n\t\tself.two_items = two_items\n\t\tself.lv3_courses = lv3_courses\n\t\tself.lv6_courses = lv6_courses\n\t@classmethod\n\tdef getinstances(cls):\n\t\tdead = set()\n\t\tfor ref in cls._instances:\n\t\t\tobj = ref()\n\t\t\tif obj is not None:\n\t\t\t\tyield obj\n\t\t\telse:\n\t\t\t\tdead.add(ref)\n\t\tcls._instances -= dead\n\n')


def webscraper():
    dfs = pd.read_html(webpage)

    # To filter out all text after the word "Skill Level"
    string = (str(dfs))
    string = pre_filter(string,'Skill Level')

    ###find text between "Rarity and "...," aka badstring
    badstring = string.split("Rarity")[1].split("...,")[0]
    string = string.replace(badstring, '')

    # Find the item's rarity level (ie. high-end, super or normal)

    rarity = first_letter_filter(badstring)
    rarity = pre_filter(rarity,',')

    # Filter out badstring

    string = string.replace('Rarity...', '')
    string = string.replace(',', '')

    # Make string easier to parse

    string = space_removal(string, 30)

    string = first_letter_filter(string)

    # split string into a string for character names and another for their courses
    char_name = pre_filter(string, '\n')
    courses_name = string.split('\n', 2)[-1] #deletes the first 2 lines

    # modify char_name(s) so they can be processed by a python program
    bad_chars = ['(', ')', ' ', '-']
    char_name = bad_chars_removal(bad_chars,char_name,'_')

    bad_chars = ['\'', '.', '\"']
    char_name = bad_chars_removal(bad_chars, char_name, '')

    char_name = first_letter_filter(char_name)
    char_name = dupicates_in_string.duplicate_be_gone(char_name)
    char_name = str(char_name)

    # Filter out results before the first course name

    courses_name = list(courses_name.split("\n"))

    start = 0
    while start < len(courses_name):
        if 'Columns' in courses_name[start]:
            pass
        elif 'Index' in courses_name[start]:
            pass
        elif 'DataFrame' in courses_name[start]:
            pass
        elif len(courses_name[start]) <= 2:
            pass
        else:
            break
        start+=1

    courses_name = courses_name[start:]

    courses_name = '\n'.join([str(elem) for elem in courses_name])

    # eliminate unneeded numbers and "NaN"
    bad_chars = ['\n0', '\n1', '\n2', '\n3', '\n4', '\n5', '\n6', '\n7', '\n8','\n9','\nNaN']

    courses_name = bad_chars_removal(bad_chars,courses_name,'\n')

    # eliminate other unhelpful characters
    courses_name = courses_name.replace('?', '')
    courses_name = courses_name.replace('�','e')

    # differentiate 3 and 2 item characters
    course_item = courses_name.find('\n\n\n')
    course_2item = (courses_name[course_item:])
    course_3item = (courses_name[:course_item])

    # convert to a list
    course_3item = list(course_3item.split("\n"))
    course_2item = list(course_2item.split("\n"))

    # remove elements from the list shorter than 4 characters
    course_3item = list(filter(lambda x: len(x) >= 4, course_3item))
    course_2item = list(filter(lambda x: len(x) >= 4, course_2item))


    # search through 3 item list for courses that are infact 2 item courses at lower levels

    Lv_courses = str_list_filter(' (Lv', course_3item, 'keep')
    lv_courses = str_list_filter(' (lv', course_3item, 'keep')
    lv_courses = Lv_courses+lv_courses

    lv3_courses = []
    lv6_courses = []

    def list_sort(set_o_words):
        start = len(set_o_words) - 1
        set_o_words_list = list(set_o_words)
        while start > 0:
            if set_o_words_list[start] == '3':
                nonlocal lv3_courses
                lv3_courses.append(set_o_words)
                break
            if set_o_words_list[start] == '6':
                # set_o_words = str(set_o_words)
                nonlocal lv6_courses
                lv6_courses.append(set_o_words)
                break
            else:
                start -= 1

    start = 0
    while start < len(lv_courses):
        list_sort(lv_courses[start])
        start += 1


    # Remove (Lv courses from course_3item

    course_3item = str_list_filter(' (Lv', course_3item, 'remove')
    course_3item = str_list_filter(' (lv', course_3item, 'remove')

    # Remove ' (lv' and ' (Lv' from all items in lv3_courses and lv6_courses

    start = 0
    while start < len(lv3_courses):
        new_string = lv3_courses[start]
        new_string = pre_filter(new_string,' (')
        lv3_courses[start] = new_string
        # print(new_string)
        start = start + 1

    start = 0
    while start < len(lv6_courses):
        new_string = lv6_courses[start]
        new_string = pre_filter(new_string,' (')
        lv6_courses[start] = new_string
        # print(new_string)
        start = start + 1

    # Formating final writing that will be put in the file

    course_3item = str(course_3item)
    course_2item = str(course_2item)

    global class_name
    global first_best_setname
    global second_best_setname
    global final_string

    final_string = final_string + ('\n' + "#" + char_name + '\n# '+ webpage + "\n\n")
    final_string = final_string + char_name + first_best_setname \
                   + " = " + course_3item + "\n\n" \
                   + char_name + second_best_setname + " = " + str(course_2item) + "\n\n" \
                   + char_name + '_lv3_courses = '+ str(lv3_courses)+ "\n\n" \
                   + char_name + '_lv6_courses = '+ str(lv6_courses)+'\n\n'

    final_string = final_string + (char_name + " = " + class_name + "(\'" + char_name + "\', " + '\'' + rarity + '\', '  + char_name + first_best_setname + ', '
           + char_name + second_best_setname + ', ' + char_name + '_lv3_courses, ' + char_name + '_lv6_courses'
                                   ")\n\n")

    print(char_name)
    print(webpage)

    return final_string

# to cycle through, getting info from the links specified

start = 0
while start < len(links):
    webpage = (links[start])
    start += 1
    try:
        webscraper()
    except IndexError:
        print('passing')

# Try writing into specified program, except: just printing it all below
try:
    file = open(final_file,"w")
    cont = file.write(final_string)
    file.close()

except PermissionError:
    print(final_string)