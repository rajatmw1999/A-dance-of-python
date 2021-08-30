from os import write
from selenium import webdriver

# time for pausing between navigation
import time
from selenium.webdriver.chrome.options import Options  

chrome_options = Options()
chrome_options.add_argument("--headless") 

def get_quote():
    today_quote = None
    myquotesfile = open('quotes.txt','r', encoding="utf8")
    all_quotes = myquotesfile.readlines()
    write_back = ""
    for x in all_quotes:
        x = x[:-1]
    i=1
    while i<len(all_quotes):
        write_back = write_back + all_quotes[i]
        i=i+1
    today_quote = all_quotes[0]
    myquotesfile.close()
    myquotesfile = open('quotes.txt','w',encoding="utf8")
    myquotesfile.write(write_back)
    myquotesfile.close()
    # print(today_quote.count())
    return today_quote
    

def submit_assignment(username, password):
    # Using Chrome to access web
    driver = webdriver.Chrome(executable_path="C:\\Users\\hp\\OneDrive\\Desktop\\chromedriver_win32\\chromedriver.exe", chrome_options=chrome_options)
    time.sleep(5)

    # Open the website
    driver.get('https://twitter.com/login')
    time.sleep(5)

    # Locate id and password
    id_box = driver.find_element_by_name('session[username_or_email]')
    pass_box = driver.find_element_by_name('session[password]')

    # Send login information
    id_box.send_keys(username)
    pass_box.send_keys(password)

    login = driver.find_element_by_xpath('//span[normalize-space()="Log in"]')
    login.click()

    time.sleep(5)
    
    tweetbox = driver.find_element_by_class_name('public-DraftStyleDefault-block')

    my_next_tweet = get_quote()
    if len(my_next_tweet) < 258:
        my_next_tweet = my_next_tweet + '\n' + '#motivation #success '
    elif len(my_next_tweet) < 280:
        pass
    elif len(my_next_tweet) >= 280:
        my_next_tweet = get_quote()
    
    print(my_next_tweet)

    tweetbox.send_keys(my_next_tweet)

    time.sleep(5)

    login = driver.find_element_by_xpath('//span[normalize-space()="Tweet"]')
    time.sleep(5)
    login.click()

    time.sleep(5)
    return

if __name__ == "__main__":
	submit_assignment('rajatupadhyay3', '#')
    # get_quote()