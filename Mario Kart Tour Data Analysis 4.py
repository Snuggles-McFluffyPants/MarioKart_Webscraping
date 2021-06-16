from gui_select_from_list import tkinter_stuff as tkinter_stuff2
from tkinter import *
from dropdown_menu import *

''' 
================================
List of owned Characters is here
================================
'''
if selection == 'Drivers':
    from Mario_Kart_Tour_drivers2 import *
    owned_chars = ['High-End --- Baby_Peach__Cherub_', 'High-End --- Dry_Bowser', 'High-End --- Dry_Bowser__Gold_', 'High-End --- Gold_Koopa__Freerunning_', 'High-End --- Ice_Mario', 'High-End --- Mario__Hakama_', 'High-End --- Metal_Mario', 'High-End --- Pauline', 'High-End --- Pauline__Rose_', 'High-End --- Peachette', 'High-End --- Rosalina__Swimwear_', 'High-End --- Toad__Party_Time_', 'High-End --- Wario__Cowboy_', 'Normal --- Baby_Daisy', 'Normal --- Baby_Luigi', 'Normal --- Baby_Mario', 'Normal --- Baby_Peach', 'Normal --- Baby_Rosalina', 'Normal --- Dry_Bones', 'Normal --- Iggy', 'Normal --- Koopa_Troopa', 'Normal --- Larry', 'Normal --- Lemmy', 'Normal --- Ludwig', 'Normal --- Morton', 'Normal --- Roy', 'Normal --- Shy_Guy', 'Normal --- Wendy', 'Super --- Birdo__Light_Blue_', 'Super --- Birdo__Yellow_', 'Super --- Black_Shy_Guy', 'Super --- Boomerang_Bro', 'Super --- Bowser', 'Super --- Bowser_Jr', 'Super --- Daisy', 'Super --- Diddy_Kong', 'Super --- Donkey_Kong', 'Super --- Fire_Bro', 'Super --- Hammer_Bro', 'Super --- Ice_Bro', 'Super --- King_Boo', 'Super --- Lakitu', 'Super --- Luigi', 'Super --- Mario', 'Super --- Monty_Mole', 'Super --- Peach', 'Super --- Pink_Shy_Guy', 'Super --- Red_Koopa__Freerunning_', 'Super --- Red_Yoshi', 'Super --- Rosalina', 'Super --- Toad', 'Super --- Toad__Pit_Crew_', 'Super --- Toadette', 'Super --- Waluigi', 'Super --- Wario', 'Super --- Yoshi']
    lv3_chars = ['High-End --- Gold_Koopa__Freerunning_', 'High-End --- Metal_Mario', 'Normal --- Baby_Mario', 'Normal --- Dry_Bones', 'Normal --- Koopa_Troopa', 'Normal --- Lemmy', 'Normal --- Ludwig', 'Normal --- Morton', 'Normal --- Roy', 'Super --- Bowser', 'Super --- Luigi', 'Super --- Peach', 'Super --- Red_Koopa__Freerunning_', 'Super --- Red_Yoshi']
    lv6_chars = []
    # owned_chars = []
    # lv3_chars = []
elif selection == 'Karts':
    from Mario_Kart_Tour_karts2 import *
    owned_chars = ['High-End --- Apple_Kart_', 'High-End --- B_Dasher_', 'High-End --- Badwagon_', 'High-End --- Banana_Master_', 'High-End --- Bruiser_', 'High-End --- Bumble_V_', 'High-End --- Cact_X', 'High-End --- Circuit_Special_', 'High-End --- Dark_Buggy_', 'High-End --- Dozer_Dasher_', 'High-End --- Gold_Cheep_Charger_', 'High-End --- Gold_Cheep_Snorkel_', 'High-End --- Head_Honcho_', 'High-End --- Ice_blue_Poltergust_', 'High-End --- Macharon_', 'High-End --- P_Wing', 'High-End --- Pink_Wing_', 'High-End --- Pirate_Sushi_Racer_', 'High-End --- Red_B_Dasher_', 'High-End --- Rose_Taxi_', 'High-End --- Snow_Skimmer_', 'High-End --- Sushi_Racer_', 'High-End --- Wild_Wing_', 'Normal --- Biddybuggy_', 'Normal --- Birthday_Girl_', 'Normal --- Birthday_Girl_Rosalina_', 'Normal --- Bullet_Blaster_', 'Normal --- Bulls_Eye_Banzai_', 'Normal --- Cheep_Charger_', 'Normal --- Green_Cheep_Charger_', 'Normal --- Green_Kiddie_Kart_', 'Normal --- Koopa_Dasher_', 'Normal --- Landship_', 'Normal --- Mushmellow_', 'Normal --- Pipe_Buggy_', 'Normal --- Pipe_Frame_', 'Normal --- Red_Kiddie_Kart_', 'Super --- Barrel_Train_', 'Super --- Blue_Seven_', 'Super --- Cloud_9_', 'Super --- Dark_Clown_', 'Super --- DK_Jumbo_', 'Super --- Egg_1_', 'Super --- Koopa_Clown_', 'Super --- Light_blue_Turbo_Birdo_', 'Super --- Mach_8_', 'Super --- Para_Wing_', 'Super --- Poltergust_4000_', 'Super --- Rambi_Rider_', 'Super --- Red_Turbo_Yoshi_', 'Super --- Royale_', 'Super --- Soda_Jet_', 'Super --- Streamliner_', 'Super --- Super_Blooper_', 'Super --- Turbo_Birdo_', 'Super --- Turbo_Yoshi_', 'Super --- Zucchini_']
    lv3_chars = ['High-End --- Cact_X', 'Normal --- Birthday_Girl_', 'Normal --- Bullet_Blaster_', 'Normal --- Green_Kiddie_Kart_', 'Normal --- Koopa_Dasher_', 'Normal --- Mushmellow_', 'Normal --- Pipe_Buggy_', 'Normal --- Pipe_Frame_', 'Normal --- Red_Kiddie_Kart_', 'Super --- Barrel_Train_', 'Super --- Blue_Seven_', 'Super --- Cloud_9_', 'Super --- Koopa_Clown_', 'Super --- Mach_8_', 'Super --- Para_Wing_', 'Super --- Soda_Jet_', 'Super --- Streamliner_']
    lv6_chars = []
elif selection == 'Gliders':
    from Mario_Kart_Tour_gliders2 import *
    owned_chars = ['High-End --- Butterfly_Sunset_', 'High-End --- Cheep_Cheep_Mask_', 'High-End --- Cloud_Glider_', 'High-End --- Crimson_Crane_', 'High-End --- Full_Flight_', 'High-End --- Gold_Glider_', 'High-End --- Gold_Swooper_', 'High-End --- Great_Sail_', 'High-End --- Heart_Balloons_', 'High-End --- Luma_Parafoil_', 'High-End --- Pink_Gold_Paper_Glider_', 'High-End --- Purple_Oilpaper_Umbrella_', 'High-End --- Rainy_Balloons_', 'High-End --- Silver_and_Gold_Hearts_', 'High-End --- Silver_Starchute_', 'High-End --- Star_Spangled_Glider_', 'High-End --- Starchute_', 'High-End --- Sweetheart_Glider_', 'High-End --- Swooper_', 'High-End --- Tropical_Glider_', 'Normal --- BBIA_Parafoil_', 'Normal --- Droplet_Glider_', 'Normal --- Minion_Paper_Glider_', 'Normal --- Paper_Glider_', 'Normal --- Parachute_', 'Normal --- Parafoil_', 'Normal --- Piranha_Plant_Parafoil_', 'Normal --- Piston_Glider_', 'Normal --- Super_Glider_', 'Super --- BaNaNa_Parafoil_', 'Super --- Bit_Jumping_Mario_8_Bit_Jumping_Mario1', 'Super --- Block__Block1', 'Super --- Blue_Flower_Glider_', 'Super --- Bob_omb_Parafoil_', 'Super --- Cucumber_', 'Super --- Eggshell_Glider_', 'Super --- Flower_Glider_', 'Super --- Lightning_Oilpaper_', 'Super --- Oilpaper_Umbrella_', 'Super --- Peach_Parasol_', 'Super --- Pink_Flower_Glider_', 'Super --- Shell_Parachute_', 'Super --- Waluigi_Wing_', 'Super --- Wario_Wing_']
    lv3_chars = ['Super --- Block__', 'High-End --- Crimson_Crane_', 'Normal --- BBIA_Parafoil_', 'Normal --- Droplet_Glider_', 'Normal --- Minion_Paper_Glider_', 'Normal --- Paper_Glider_', 'Normal --- Parachute_', 'Normal --- Parafoil_', 'Normal --- Piranha_Plant_Parafoil_', 'Normal --- Piston_Glider_', 'Normal --- Super_Glider_', 'Super --- BaNaNa_Parafoil_', 'Super --- Block__Block1', 'Super --- Blue_Flower_Glider_', 'Super --- Bob_omb_Parafoil_', 'Super --- Eggshell_Glider_', 'Super --- Lightning_Oilpaper_', 'Super --- Pink_Flower_Glider_', 'Super --- Shell_Parachute_', 'Super --- Wario_Wing_']
    lv6_chars = []
    # owned_chars =  [] #['Normal --- Minion_Paper_Glider_', 'Normal --- Paper_Glider_']
    # lv3_chars = []
# Change character names for easier read-ability
for obj in race_tool.getinstances():
    obj.name = obj.rarity + ' --- ' + obj.name

char_list = []

# make char_list have all character names in it
for obj in race_tool.getinstances():
    char_list.append(obj.name)

# Sort char_list items to make it easier to read
char_list = sorted(char_list, key=str.lower)

# Adds one race_tool's 2 item courses and 3 item courses to two_item_courses and three_item_courses
# optional class_var's are:
#           'three_items', 'two_items', 'lv3_courses' 'lv6_courses'

two_item_courses = []  # a list of course with a race_tool that gets 2 items
three_item_courses = []  # a list of courses with a race_tool that gets 3 items

# Function to take a class attribute and append them to a list
def class_attr_to_list(char_name,
                 class_var = 'three_items',
                 listToAddTo = three_item_courses):
    # find class instance with name selected
    for obj in race_tool.getinstances():
        if obj.name == char_name:
            char_name = obj
            class_attr = (getattr(char_name,class_var))

            # Get class attribute and add it to the specified list
            for item in class_attr:
                if item not in three_item_courses:
                    if isinstance(listToAddTo, list):
                        listToAddTo.append(item)
                    if isinstance(listToAddTo, set):
                        listToAddTo.add(item)

# Initial tkinter window for entering already owned characters
owned_chars = tkinter_stuff2('Enter in Your Characters',char_list,owned_chars)
# Sort owned_chars by alphabetic order to make it easier to read
owned_chars = sorted(owned_chars, key=str.lower)

# Initial tkinter window for entering already owned characters
lv3_chars = tkinter_stuff2('Enter in Level 3 Characters',owned_chars,lv3_chars)
# Sort lv3_chars by alphabetic order to make it easier to read
lv3_chars = sorted(lv3_chars, key=str.lower)

# Initial tkinter window for entering already owned characters
lv6_chars = tkinter_stuff2('Enter in Level 6 Characters',lv3_chars, lv6_chars)

# =================
# Adds owned characters two and three item courses to correct list
# =================
def item_courses_list_creation():
    global three_item_courses
    global two_item_courses
    global owned_chars
    # Add in owned characters two and three item courses
    for item in owned_chars:
        class_attr_to_list(item, 'three_items', three_item_courses)
        class_attr_to_list(item, 'two_items', two_item_courses)
    # Add three item courses form characters being level 3 or higher
    for item in lv3_chars:
        class_attr_to_list(item, 'lv3_courses', three_item_courses)
    # Add three item courses form characters being level 3 or higher
    for item in lv6_chars:
        class_attr_to_list(item, 'lv6_courses', three_item_courses)

    # redefine three and two item courses lists
    three_item_courses = set(three_item_courses)
    two_item_courses = set(two_item_courses)
    two_item_courses = two_item_courses - three_item_courses

    return three_item_courses, two_item_courses

three_item_courses = []
two_item_courses = []
three_item_courses, two_item_courses = item_courses_list_creation()

# Gui to select which characters to evaluate
evaluating_chars = tkinter_stuff2('Enter in Items to Evaluate',char_list,owned_chars)

# =================
# Evaluate which characters to upgrade
# =================

upgrade_to_lv3 = []
upgrade_to_lv6 = []

for char in char_list:
    temp_list = []
    class_attr_to_list(char, class_var='lv3_courses', listToAddTo=temp_list)
    for item in temp_list:
        if item in three_item_courses:
            temp_list.remove(item)
    if len(temp_list) > 0:
        char_and_courses = [char ,temp_list]
        upgrade_to_lv3.append(char_and_courses)

    temp_list = []
    class_attr_to_list(char, class_var='lv6_courses', listToAddTo=temp_list)
    for item in temp_list:
        if item in three_item_courses:
            temp_list.remove(item)
    if len(temp_list) > 0:
        char_and_courses = [char,temp_list]
        upgrade_to_lv6.append(char_and_courses)


# for obj in race_tool.getinstances():
#     if obj in char_list:
#     chars_lv3_courses = getattr(obj, 'lv3_courses')
#     for item in chars_lv3_courses:
#         if item in three_item_courses:
#             three_item_courses.remove(item)
#     if len(chars_lv3_courses) > 0:
#         char_and_courses = [obj,chars_lv3_courses]
#         upgrade_to_lv3.append(char_and_courses)
#
#
#     chars_lv6_courses = getattr(obj, 'lv6_courses')
#     for item in chars_lv6_courses:
#         if item in three_item_courses:
#             three_item_courses.remove(item)
#     if len(chars_lv3_courses) > 0:
#         char_and_courses = [obj,chars_lv6_courses]
#         upgrade_to_lv6.append(char_and_courses)

print('\n\nGained at lv3\n\n\n')
upgrade_to_lv3 = str(upgrade_to_lv3)
upgrade_to_lv3 = upgrade_to_lv3.replace('[','\n[')
print(upgrade_to_lv3)
print('\n\nGained at lv6\n\n\n')
upgrade_to_lv6 = str(upgrade_to_lv6)
upgrade_to_lv6 = upgrade_to_lv6.replace('[','\n[')
print(upgrade_to_lv6)


# =================
# Evaluate 3_item and 2_item courses gained with character
# =================

eval_owned_chars = []
eval_not_owned_chars = []

for item in evaluating_chars:
    if item in owned_chars:
        eval_owned_chars.append(item)
    else:
        eval_not_owned_chars.append(item)



def item_evaluation(char_name, final_list):
    # for obj in race_tool.getinstances():
    #     if obj.name == selection:
    global three_item_courses
    global two_item_courses
    global upgrade_to_lv3
    global upgrade_to_lv6
    for obj in race_tool.getinstances():
        if obj.name == char_name:
            char_name = obj
            three_x_courses = set(getattr(char_name, 'three_items'))
            three_x_courses = (three_x_courses - three_item_courses)

            two_x_courses = set(getattr(char_name, 'two_items'))
            two_x_courses = (two_x_courses - two_item_courses)
            two_x_courses = (two_x_courses - three_item_courses)

            three_from_one = three_x_courses - two_item_courses
            three_from_two = three_x_courses - three_from_one

            char_value = float(len(three_from_one))*2.4 + \
                         float(len(three_from_two)) *1.4 + \
                         float(len(two_x_courses))

            gained_at_lv3 =[]
            char_lv3_courses = getattr(char_name, 'lv3_courses')
            for item in char_lv3_courses:
                if item not in three_item_courses:
                    gained_at_lv3.append(item)

            gained_at_lv6 =[]
            char_lv6_courses = getattr(char_name, 'lv6_courses')
            for item in char_lv6_courses:
                if item not in three_item_courses:
                    gained_at_lv6.append(item)

            final_string = '\n\n' + (str(obj.name) + '\n')
            final_string = final_string + '-----------------------------------'

            final_string = final_string +('\n\t3 items from 1:')
            final_string = final_string +('\n\t\t'+ str(three_from_one))
            final_string = final_string +('\n\t\t'+ str(len(three_from_one)))

            final_string = final_string +('\n\t3 items from 2:')
            final_string = final_string +('\n\t\t'+ str(three_from_two))
            final_string = final_string +('\n\t\t'+ str(len(three_from_two)))

            final_string = final_string +('\n\t2 items:')
            final_string = final_string +('\n\t\t'+ str(two_x_courses))
            final_string = final_string +('\n\t\t'+ str(len(two_x_courses)))

            final_string = final_string + ('\n\tChar Value = ' + str(char_value)+ '\n')

            final_string = final_string +('\n\tCourses gained at Lv3:')
            final_string = final_string +('\t\t'+ str(gained_at_lv3))

            final_string = final_string +('\n\tCourses gained at Lv6:')
            final_string = final_string +('\t\t'+ str(gained_at_lv6))

            final_list.append(final_string)

attr_owned_chars = []
attr_not_owned_chars = []

for item in eval_not_owned_chars:
    item_evaluation(item,attr_not_owned_chars)

for item in eval_owned_chars:
    # Removing character form owned_char and lv3 and 6_char lists as needed
    if item in owned_chars:
        owned_chars.remove(item)
    # print('\nOwned Chars = ', owned_chars)

    lv3_chars_add_back = 'no'
    if item in lv3_chars:
        lv3_chars.remove(item)
        lv3_chars_add_back = 'yes'

    lv6_chars_add_back = 'no'
    if item in lv6_chars:
        lv6_chars.remove(item)
        lv6_chars_add_back = 'yes'

    # look at 2 and 3 item courses without the character
    three_item_courses = []
    two_item_courses = []
    three_item_courses, two_item_courses = item_courses_list_creation()

    # print('three_item_courses = ',three_item_courses)
    # print('two_item_courses = ', two_item_courses)

    # Evaluating an the characters value
    item_evaluation(item,attr_owned_chars)

    # Adding character back to the required lists
    owned_chars.append(item)
    if lv3_chars_add_back == 'yes':
        lv3_chars.append(item)
    if lv6_chars_add_back == 'yes':
        lv6_chars.append(item)

# =================
# Modifying final output string
# =================

# modify attr_not_owned_chars and attr_owned_chars to be usable strings
attr_not_owned_chars = '\n'.join([str(elem) for elem in attr_not_owned_chars])
attr_owned_chars = '\n'.join([str(elem) for elem in attr_owned_chars])




# Calculate amount of courses with 3,2 and 1 items given chars owned

def final_stats():
    # create a the list all_courses which contains every course in it
    all_courses = set()
    for item in char_list:
        class_attr_to_list(item, class_var='three_items',
                           listToAddTo= all_courses)
        class_attr_to_list(item, class_var='two_items',
                           listToAddTo= all_courses)

    print(all_courses)

    # redo adding all owned characters 3 and 2 item courses to
    # the correct list
    three_item_courses = set()
    two_item_courses = set()
    three_item_courses, two_item_courses = item_courses_list_creation()

    # Sort out how many courses only have 1 item
    one_item_courses = len(all_courses) \
                       - len(three_item_courses) \
                       - len(two_item_courses)

    num = one_item_courses \
          + len(two_item_courses) \
          + len(three_item_courses)

    len_all_courses = str(len(all_courses))
    len_three_item_courses = str(len(three_item_courses))
    len_two_item_courses = str(len(two_item_courses))
    len_one_item_courses = str(one_item_courses)

    # Add the amount of courses with 3, 2 and 1 item to the output string
    output_string = 'Amount of Courses:' + len_all_courses
    output_string = output_string + '\n\nAmount of 3 Item Courses:' + len_three_item_courses
    output_string = output_string + '\nAmount of 2 Item Courses:' + len_two_item_courses
    output_string = output_string + '\nAmount of 1 Item Courses:' + len_one_item_courses
    output_string = output_string + '\n'

    # # Print the amount of courses with 3, 2 and 1 item
    # print('Amount of Courses:', len(all_courses))
    # print('Amount of 3 Item Courses:', len(three_item_courses))
    # print('Amount of 2 Item Courses:', len(two_item_courses))
    # print('Amount of 1 Item Courses:', one_item_courses)

    # Find the percent of courses with 3, 2 and 1 item

    three_item_percent = 100 * (len(three_item_courses) / len(all_courses))
    two_item_percent = 100 * (len(two_item_courses) / len(all_courses))
    one_item_percent = 100 * (one_item_courses / len(all_courses))

    three_item_percent = list(str(three_item_percent))
    three_item_percent = ''.join(three_item_percent[:6])
    two_item_percent = list(str(two_item_percent))
    two_item_percent = ''.join(two_item_percent[:6])
    one_item_percent = list(str(one_item_percent))
    one_item_percent = ''.join(one_item_percent[:6])

    # Check that the percent of courses with 3,2, and 1 item = 100
    # percent_check = three_item_percent \
    #                 + two_item_percent \
    #                 + one_item_percent
    # percent_check = list(str(percent_check))
    # percent_check = ''.join(percent_check[:6])

    output_string = output_string \
                    + '\nPercent of Courses with 3 items:   %' \
                    + three_item_percent
    output_string = output_string \
                    + '\nPercent of Courses with 2 items:   %' \
                    + two_item_percent
    output_string = output_string \
                    + '\nPercent of Courses with 1 items:   %' \
                    + one_item_percent

    output_string = output_string + '\n\n'

    return output_string

# putting together the final output string

final_string = final_stats()
final_string = final_string + 'owned_chars = ' + str(owned_chars)
final_string = final_string + '\n\n' + 'lv3_chars = ' + str(lv3_chars)
final_string = final_string + '\n\n' + 'lv6_chars = ' + str(lv6_chars) + '\n\n\n'

final_string = final_string + '\n' + attr_not_owned_chars

final_string = final_string + '\n\n\n=============================\nowned_chars\n=============================\n'


final_string = final_string + attr_owned_chars

# =================
# Final tkinter Gui text output
# =================

def text_window(string):
    master = Tk()

    w = Text(master, height=30, borderwidth=0)
    w.insert(1.0, string)
    w.pack()

    w.configure(state="disabled")

    # if tkinter is 8.5 or above you'll want the selection background
    # to appear like it does when the widget is activated
    # comment this out for older versions of Tkinter
    w.configure(inactiveselectbackground=w.cget("selectbackground"))

    mainloop()

text_window(final_string)

