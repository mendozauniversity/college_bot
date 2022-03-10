# college_bot
DISCLAIMER - Try this on your own accord, I'm not responsible for anything that happens. If you are using GMail, it limits you to 500 emails per day, this is why the counter iterates 500 times on the python bot. I made 4 emails and just made the iterator go from 0-499, 500 - 999, 1000 - 1499, 1500 - 1716 i.e. update the x and i values respectively). After each set of 500 emails, log out and log into the next email you're using. If you need to stop the program once it's started, move your cursor to the upper-left corner of the leftmost monitor, it's a built in failsafe for pyautogui. It takes quite a while for the bot to write out and send every email.

Follow these steps:
• Step 1: Follow instructions on TikTok to download python and pyautogui, links can be found here:
	• https://www.python.org/downloads/
	• https://pyautogui.readthedocs.io/en/latest/install.html
	
• Step 2: Download .CSV and .py files from GitHub (click on the file on the main github branch, click raw, right click and click save as, change the file extension from .txt to .py or .csv (collegeemailer and position need .py, collegenames and collegeemails need .csv), make save all files in one folder on your PC. 

• Step 3: Press the Windows key, type IDLE and press enter. Open position.py and collegeemailer.py (File > Open > (location of collegeemailer.py and position.py) and open both .py files)

• Step 4: Run position.py (Run > Run Module > move mouse to compose button) to get the (x,y) coordinates for the compose button. The format is (x = x_coord, y = y_coord) (for example (x = 1230, y = 540)) Fill in the (x,y) in pytautogui.click() section.

• Step 5: Change the following values to your information respectively: ENTER_NAME (x2), ENTER_HIGHSCHOOL, ENTER_STATE, ENTER_ADDRESS. (If you don't add your address in the email you're much less likely to get stuff from the colleges.)

• Step 6: Run college_emailer.py (Run > Run Module) click into the window gmail is on and sit back and watch!
	
