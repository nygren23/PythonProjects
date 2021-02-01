import requests
import sys
from bs4 import BeautifulSoup # pip install bs4 to work
import datetime
import smtplib

# scraping tool
# returns game information based on url parameter
def find_game(url):
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser', from_encoding="latin-1")

    # find title
    # catches any non-ascii characters in titles
    # so the output can be printed to the console
    # or written to a file
    title = soup.find('title').text
    title = title.encode("ascii", errors="ignore").decode()

    # find and parse price
    final_price_str = soup.find('span', attrs={'data-qa':'mfeCtaMain#offer0#finalPrice'}).text[1:]
    final_price_float = float(final_price_str)

    # find original price (0 if does not exist)
    orig_price_str = soup.find('span', attrs={'data-qa':'mfeCtaMain#offer0#originalPrice'})
    if(orig_price_str is None):
        orig_price_float = 0
    else:
        orig_price_str = orig_price_str.text[1:]
        orig_price_float = float(orig_price_str)
    return [title, final_price_float, orig_price_float]


# prints the game based on the url
# and the info returned from find_game()
def transcribe_game(url):
    game = find_game(url)
    
    title = game[0]
    final_price = game[1]
    orig_price = game[2]


    # change prints to str appends
    message = ("Title: " + title + "\n")
    if(orig_price == 0):
        message += ("Price: $" + str(final_price) + " (No Discount)\n")
    else:
        message += ("Original Price: $" + str(orig_price) + "\n")
        message += ("New Price: $" + str(final_price) + "\n")
        message += ("Discount Amount: -$" + str(round(orig_price - final_price, 2)) + "0\n")
    message += "---------------------------------------\n"

    return message

#
# main
#

# URLs to scrape for discounts!
urls = [ 
"https://store.playstation.com/en-us/product/UP3639-CUSA16364_00-0000000000000001",
"https://store.playstation.com/en-us/product/UP0101-CUSA17688_00-YGOLOTDLEXXXXXXX",
"https://store.playstation.com/en-us/product/UP0774-CUSA04917_00-00000000FURISCEA",
"https://store.playstation.com/en-us/product/UP1822-CUSA13632_00-HOLLOWKNIGHT18US",
"https://store.playstation.com/en-us/product/UP4040-CUSA24170_00-GHOSTRUNNER00000",
"https://store.playstation.com/en-us/product/UP1980-CUSA10507_00-REMNANT000000001",
"https://store.playstation.com/en-us/product/UP0002-CUSA12125_00-SPYROTRILOGY0001",
"https://store.playstation.com/en-us/product/UP9000-CUSA07820_00-THELASTOFUSPART2",
"https://store.playstation.com/en-us/product/UP9000-CUSA00552_00-THELASTOFUS00000",
"https://store.playstation.com/en-us/product/UP0700-CUSA05929_00-LITTLENIGHTMARES",
"https://store.playstation.com/en-us/product/UP2344-CUSA13637_00-MDKRTGAMES4BATIM"
]

# set up server

server = smtplib.SMTP("smtp.gmail.com", 587)
server.ehlo()
server.starttls()
server.ehlo()


username = 'blakeraymond777@gmail.com'
with open('C:/Users/blake/OneDrive/Desktop/Code_Building/pythonprojects/password.txt', 'r') as f:
    password = f.read()

server.login(username, password)


# setup email header
date = datetime.datetime.now().strftime("%m/%d/%Y")
msg = str(date + "\n---------------------------------------\n\n")
 
# print all games from the url list
for u in urls:
    msg += transcribe_game(u)

server.sendmail(username, username, msg)

server.quit()
