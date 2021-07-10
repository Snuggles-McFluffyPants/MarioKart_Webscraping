"""
Note: This program outputs links_list_string which
is a final variable containing all the links in a string format

final_links_list is another final output that comes in list form
"""

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from tkinter import *

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

#filter out unhelpful results
final_links_list = \
    str_list_filter('https://game8.co/games/mariokarttour/archives/',final_links_list,'keep')
final_links_list = \
    str_list_filter('comment',final_links_list,'remove')

# Make links_list_string itterable
links_list_string = str(final_links_list)
links_list_string = links_list_string.replace('\'', '')

bad_chars = ['[', ']']
links_list_string = \
    bad_chars_removal(bad_chars, links_list_string,'')


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

if __name__ == "__main__":
    text_window(links_list_string)

