from datetime import datetime
from users import *
import sys


questions = 1
artist_genre = ""
year = 0
month = 0
day = 0
while questions == 1:
    artist_date = input("When do you want to perform?\n")
    year = int(artist_date.split(',')[0])
    month = int(artist_date.split(',')[1])
    day = int(artist_date.split(',')[2])
    artist_genre = str(input("What is your genre?\n"))
    if 'Exit' == artist_date or 'Exit' == artist_genre:
        break
    print("Thank you for your input\n")
    questions = 0
artist_date = datetime(year, month, day)

print("\n")

match_list = []
match_dict = {}


for venue in venue_list:
    for show in venue["start"]:
        if (artist_date.year == show.year) and (artist_date.month == show.month) and artist_date.day == show.day:
            match_list.append(venue)

for venue in venue_list:
    for show in venue["start"]:
        list = []
        if (artist_date.year == show.year) and (artist_date.month == show.month) and artist_date.day == show.day:
            list.append(venue)
        if list != []:
            match_dict[show] = list

match_check = 0
#for venue in match_list:
for i in range(len(match_list)):
    if artist_genre in match_list[i]["genre"]:
        print("You have matched with " + match_list[i]["name"] + ": " + match_list[i]["description"])
        #print("You will be performing at ", end='')
        #print(match_dict[i])
        #print('start: ' + venue["start"])
        #print('end: ' + venue["end"])
        match_check = 1


for showtime in match_dict:
    print("You will be performing at ", end='')
    print(showtime)

if match_check == 0:
    print("Sorry, no venues fit your criteria.")
