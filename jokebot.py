import csv
import argparse
import sys
import time
import requests

def deliver_joke(prompt, punchline):
# prints the prompt, waits two seconds, then prints the punchline.
    print(prompt)
    time.sleep(2)
    print(punchline)
    return

def get_user_input():
# gets user input, and returns True if "next" or False if "quit".
    print('Enter "next" to hear another joke, or enter "quit" to exit.')
    choice = input()
    if (choice != "next") and (choice != "quit"):
        print("Not a valid input. Input 'next' for another joke, or 'quit' to stop.")
        choice = get_user_input()
    elif choice == "next":
        return True
    else:
        return False

def read_jokes(file):
# reads jokes from csv and returns them in a list with the format [[prompt, punchline]].
    joke_list = []
    with open(file, newline='') as jokes:
        jokereader = csv.reader(jokes, delimiter=',')
        for row in jokereader:
            try:
                joke_list.append([row[0], row[1]])
            # in case the csv passed in has 0 or 1 columns    
            except IndexError:
                print('Joke list does not provide both a prompt and a punchline!')
    return joke_list       

def get_jokes():
# gets jokes from r/dadjokes by parsing a JSON, if a joke csv is not given. Jokes are only chosen if
# the title begins with 'Why', 'How', or 'What', and are sfw.

    # headers arg gets rid of too many requests error
    r = requests.get('https://www.reddit.com/r/dadjokes.json', headers = {'User-agent': 'your bot 0.1'})
    joke_list = []
    query_words = ['Why', 'How', 'What']

    for post in r.json()['data']['children']:
        post_data = post['data']
        if (post_data['over_18'] == True) or (post_data['selftext'] == "") or (post_data['title'].partition(' ')[0] not in query_words):
            continue
        else:
            joke_list.append([post_data['title'], post_data['selftext']])

    return joke_list

# gets the csv file from the command line, else it defaults to getting from reddit.
parser = argparse.ArgumentParser()
parser.add_argument("-f", '--filename', type=str, default = 'reddit', help = 'No joke file given.')
args = parser.parse_args()

if args.filename == 'reddit':
    jokes = get_jokes()
else:
    jokes = read_jokes(args.filename)

# In the case no jokes are in jokelist from either empty csv or no jokes from reddit meet our conditions.
if jokes == None:
    if args.filename == 'reddit'
        print('No jokes from reddit meet criteria!')
    else: 
        print('Joke list is empty!')
    sys.exit(0)

# iterate over all jokes and continue based on user input, if out of jokes, then stop.
for i , joke in enumerate(jokes):
    deliver_joke(joke[0],joke[1])
    option = get_user_input()
    if option == True:
        if i == len(jokes)-1:
            print('Out of jokes!')
        continue
    else:
        sys.exit(0)
