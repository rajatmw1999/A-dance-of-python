Note: You will need python 3 installed on your system

# How to Setup the automation python script on your local machine.

Follow the steps below for windows:

1. Open a command line tool inside the test script folder
2. RUN >>       py -m venv env
3. RUN >>       .\env\Scripts\activate
4. RUN >>       pip install -r requirements.txt
5. RUN >>       py script.py

# How to add new test cases in the script

1. Open the data.xlsx file that is present inside the test script folder
2. Add a new row at the end and fill in the details for name of test case and test case serial no
3. In the data column, add your payload that you want to pass to the API
4. Save the xlsx file

Now, sit back and have a coffee. Your test results will be ready in some time.


To-do: Include expected 'MSG' or 'Status Code' from csv and in code