#
import pyautogui, os

os.chdir("C:\\GitRepo")

def clickimg(img):
    box = pyautogui.locateOnScreen(img)
    if box:
        pyautogui.click(box.left + (box.width)/2, box.top + (box.height)/2)
        return True
    
    return False

def navigatetoFriendList():
    if not clickimg("homeicon1.png"):
        clickimg("homeicon2.png")

    if not clickimg("friendsicon1.png"):
        clickimg("friendsicon2.png")

    if not clickimg("All1.png"):
        clickimg("All2.png")

win = pyautogui.getWindowsWithTitle('Discord')
win[0].activate()

navigatetoFriendList()

receiverList = ["person1.png"]

for person in receiverList:

    if clickimg(person):
        pyautogui.write("MessageToSend")
        #pyautogui.write(["enter"])

        navigatetoFriendList()

