import pyautogui,time
# ft=open('json.txt','r+')
time.sleep(2)
s="Kya bhai ready ho na ,bhai kuch nahi padhe hai."
for i in s:
    pyautogui.keyDown(i)
pyautogui.keyDown('enter')
