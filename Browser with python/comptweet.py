from selenium import webdriver
import datetime
# time for pausing between navigation
import time

def submit_assignment(username, password):
    # Using Chrome to access web
    try:
        driver = webdriver.Chrome(executable_path="C:\\Users\\hp\\OneDrive\\Desktop\\chromedriver_win32\\chromedriver.exe")
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
        i=0

        while i<100:
            x = datetime.datetime.now()
            x = str(x)
            x = x[:-7]
            tweetbox = driver.find_element_by_class_name('public-DraftStyleDefault-block')
            mt  = "Hello Twitter!!" + str(x)
            tweetbox.send_keys(mt)
            time.sleep(2)
            login = driver.find_element_by_xpath('//span[normalize-space()="Tweet"]')
            login.click()
            time.sleep(2)
            print(i, " done.")
            i=i+1
        return "Tweet DOne!"
    except Exception as e:
        print(e)
        return str(e)
if __name__ == "__main__":
	submit_assignment('#', '#')