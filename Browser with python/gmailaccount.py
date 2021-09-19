from selenium import webdriver
import time
def submit_assignment(username, password):
    # Using Chrome to access web
    try:
        driver = webdriver.Chrome(executable_path="C:\\Users\\hp\\OneDrive\\Desktop\\chromedriver_win32\\chromedriver.exe")
        # Open the website
        driver.get('https://accounts.google.com/signup/v2/webcreateaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ltmpl=default&dsh=S219112200%3A1631875662549610&biz=false&flowName=GlifWebSignIn&flowEntry=SignUp')

        # Locate id and password
        firstName = driver.find_element_by_id('firstName')
        lastName = driver.find_element_by_id('lastName')
        email = driver.find_element_by_id('username')
        pass_box = driver.find_element_by_name('Passwd')
        pass_box2 = driver.find_element_by_name('ConfirmPasswd')
        # print(pass_box)
        # pass_box = driver.find_element_by_name('session[Passwd]')
        # pass_box2 = driver.find_element_by_name('session[ConfirmPasswd]')
        
        
        # Send login information
        firstName.send_keys("Preyansh")
        lastName.send_keys("Prerit")
        email.send_keys("Preyanshpreritprepre2021")
        pass_box.send_keys('Preyanshpreritprepre2021@1902802742384')
        pass_box2.send_keys('Preyanshpreritprepre2021@1902802742384')
        time.sleep(5)
        next = driver.find_element_by_xpath('//span[normalize-space()="Next"]')
        next.click()
        time.sleep(5)
        # time.sleep(5)
        # i=0

        # while i<100:
        #     x = datetime.datetime.now()
        #     x = str(x)
        #     x = x[:-7]
        #     tweetbox = driver.find_element_by_class_name('public-DraftStyleDefault-block')
        #     mt  = "Hello Twitter!!" + str(x)
        #     tweetbox.send_keys(mt)
        #     time.sleep(2)
        #     login = driver.find_element_by_xpath('//span[normalize-space()="Tweet"]')
        #     login.click()
        #     time.sleep(2)
        #     print(i, " done.")
        #     i=i+1
        # return "Tweet DOne!"
    except Exception as e:
        print(e)
        return str(e)
if __name__ == "__main__":
	submit_assignment('#', '#')