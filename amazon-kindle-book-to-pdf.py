# This program create a screenshot of a amazon kindle book 
# from a browser, beacause it cannot be downloaded.
# Required : pip install pyautogui

import pyautogui
pyautogui.PAUSE = 2.5
# pic = pyautogui.screenshot()

# pic.save('Screenshot.png')

pyautogui.click(x=1700, y=200)

for num in range(1,50):
    im = pyautogui.screenshot(region=(200,130,1500,900))
    im.save('Page' + str(num) + '.png')
    pyautogui.click(x=1700, y=200)



