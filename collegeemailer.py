import csv
import pyautogui
import time

time.sleep(2)

with open('collegeemails.csv', newline='') as csvfile:
    emails = list(csv.reader(csvfile))

with open('collegenames.csv', newline='') as csvfile:
    names = list(csv.reader(csvfile))
    
x = 0 #startine
i = 499 #endline
while x <= i:
    time.sleep(1)
    pyautogui.click(x=3936, y=162) #click on compose
    time.sleep(0.3)
    pyautogui.write(emails[x][0]) #write name into receipient field
    time.sleep(0.3)
    pyautogui.press('enter')
    pyautogui.press('tab') #tab to subject line
    time.sleep(0.3)
    pyautogui.write("Attending ") #Writing on subject line
    pyautogui.write(names[x][0]) #Writing on subject line
    pyautogui.write(" in the Fall") #Writing on subject line
    time.sleep(0.3)
    pyautogui.press('tab') #tab to email body
    time.sleep(0.3)
    pyautogui.write("Hi there, my name is ENTER_NAME and I am currently a senior at ENTER_HIGHSCHOOL in ENTER_STATE. I am planning on attending ") #Writing on email body
    pyautogui.write(names[x][0]) #Writing on email body
    pyautogui.write(" in the fall of 2022. I toured your campus and it just feels like the perfect fit for me. I'm sure you get a lot of these requests, but I was wondering if there is any chance I could receive a pennant, flag, shirt or really anything you guys are able to offer me! I would love to start representing my school pride as early as possible. If you guys are able to help me out, my address is ENTER_ADDRESS I am looking forward to being a student and getting my collegiate career started!") #Writing on email body
    time.sleep(0.3)
    pyautogui.press('enter') #paragraph break
    time.sleep(0.3)
    pyautogui.press('enter') #paragraph break
    time.sleep(0.3)
    pyautogui.write("All the best, ENTER_NAME.") #Writing on email body
    pyautogui.hotkey('ctrl', 'enter') #hotkey send email
    x = x + 1
