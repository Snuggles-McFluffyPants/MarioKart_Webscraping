"""
Note: This program outputs links_list_string which
is a final variable containing all the links in a string format

final_links_list is another final output that comes in list form
"""

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from string_and_list_opperations import *


# import the file dropdown menu to select whether your working with drivers, gliders or karts
from dropdown_menu import selection as working_with

driver_links=['https://game8.co/games/mariokarttour/archives/270420',
             'https://game8.co/games/mariokarttour/archives/270419',
             'https://game8.co/games/mariokarttour/archives/270418']

kart_links = ['https://game8.co/games/mariokarttour/archives/270423',
               'https://game8.co/games/mariokarttour/archives/270422',
               'https://game8.co/games/mariokarttour/archives/270421']

glider_links = ['https://game8.co/games/mariokarttour/archives/270427', \
               'https://game8.co/games/mariokarttour/archives/270426', \
               'https://game8.co/games/mariokarttour/archives/270425']

if working_with == 'Drivers':
    original_websites = driver_links
elif working_with == 'Karts':
    original_websites = kart_links
elif working_with == 'Gliders':
    original_websites = glider_links

final_links_list = []

# Get a list of links on a webpage and add them to final_links_list
def extraction(webpage):
    # Get a list of links on a webpage
    req = Request(webpage)
    html_page = urlopen(req)

    soup = BeautifulSoup(html_page, "lxml")

    links = []
    for link in soup.findAll('a'):
        links.append(link.get('href'))

    # #Filter out results that come before the string m.me
    # start = 0
    # done = 'False'
    # while done == 'False' and start < len(links):
    #     if '#hl_3' in links[start]:
    #         done = 'True'
    #     start+=1
    #
    # links = links[start:-1]
    #
    # links = links[0:(start-1)]
    # seperator = ', '
    # links = seperator.join(links)

    global final_links_list
    final_links_list = final_links_list + links
    return final_links_list

# Repeat extraction function for the necessary websites
start = 0
while start < len(original_websites):
    extraction(original_websites[start])
    start+=1


final_links_list = [x for x in final_links_list if x is not None]

final_links_list = list(filter(lambda x: len(x) >= 40, final_links_list))


# # Remove unneeded characters from final_links list
# bad_chars = ['hl_4,', ',', ' ', '#,','#']
#
# final_links_list = \
#     bad_chars_removal(bad_chars, final_links_list,'')
#
# # Changes in final_links_list string to make it itterable
#
# final_links_list = final_links_list.replace('https://game8.co/games/','/games/')
# final_links_list = final_links_list.replace('/games/',', https://game8.co/games/')
# final_links_list = final_links_list.replace('https:', ', https:')
#
# final_links_list = first_letter_filter(final_links_list)
#
#
#
# #convert final_links_list into a list
# final_links_list = final_links_list.split(", ")



#filter out unhelpful results
final_links_list = \
    str_list_filter('https://game8.co/games/mariokarttour/archives/',final_links_list,'keep')
# final_links_list = \
#     str_list_filter('javascript',final_links_list,'remove')
final_links_list = \
    str_list_filter('comment',final_links_list,'remove')

# print(final_links_list)

# Make links_list_string itterable
links_list_string = str(final_links_list)
links_list_string = links_list_string.replace('\'', '')

bad_chars = ['[', ']']
links_list_string = \
    bad_chars_removal(bad_chars, links_list_string,'')

from tkinter import *

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

# text_window(links_list_string)

