import cv2
import numpy as np
import pyautogui
import time
import subprocess

# Paths to template images
templates = {
    #images
    "start": ("./images/start.png", None),
    "close1": ("./images/close1.png", None),
    "close2": ("./images/close2.png", None),
    "return": ("./images/return.png", None),
    "reward1": ("./images/reward1.png", None),
    "monthlysignin": ("./images/monthlysignin.png", None),
    "dailytasks": ("./images/dailytasks.png", None),
    "chest1": ("./images/chest1.png", None),
    "fountain": ("./images/fountain.png", None),
    "make-a-wish": ("./images/make-a-wish.png", None),
    "barracks": ("./images/barracks.png", None),
    "train1": ("./images/train1.png", None),
    "mail": ("./images/mail.png", None),
    
    #elfprivelage
    "lv0": ("./images/elfprivelage/lv0.png", None),
    "chest1": ("./images/elfprivelage/chest1.png", None),
    "return2": ("./images/elfprivelage/return2.png", None),
    
    #dailytaks
    "go": ("./images/dailytasks/go.png", None),
    "portcargo": ("./images/dailytasks/portcargo.png", None),
    "fountain-of-fate": ("./images/dailytasks/fountain-of-fate.png", None),
    "infantry-training": ("./images/dailytasks/infantry-training.png", None),
    "chest2": ("./images/dailytasks/chest2.png", None),
    "chest3": ("./images/dailytasks/chest3.png", None),
    "claim3": ("./images/dailytasks/claim3.png", None),
    
    #portcargo
    "available": ("./images/portcargo/available.png", None),
    "monthlysignin": ("./images/portcargo/monthlysignin.png", None),
    "signin": ("./images/portcargo/signin.png", None),
    "dailyoffer": ("./images/portcargo/dailyoffer.png", None),
    
    #barracks
    "train2": ("./images/barracks/train2.png", None),
    "num1450": ("./images/barracks/num1450.png", None),
    "switch-left": ("./images/barracks/switch-left.png", None),
    "speedup1": ("./images/barracks/speedup1.png", None),
    "quickspeed1": ("./images/barracks/quickspeed1.png", None),
    "use1": ("./images/barracks/use1.png", None),
    "claim1": ("./images/barracks/claim1.png", None),
    
    #fountain
    "grain": ("./images/fountain/grain.png", None),
    "wood": ("./images/fountain/wood.png", None),
    "iron": ("./images/fountain/iron.png", None),
    "silver": ("./images/fountain/silver.png", None),
    "stone": ("./images/fountain/stone.png", None),
    
    #mail
    "system": ("./images/mail/system.png", None),
    "allread": ("./images/mail/allread.png", None),
    "claim2": ("./images/mail/claim2.png", None),
    
}

# Step 1: Restart ADB using 'adb_restart.bat'
subprocess.run(["adb kill start.bat"])

# Step 3: Run 'run_game.bat' to launch the game
subprocess.run(["run game.bat"])

# Step 2: Initialize ADB (assuming adb is in the current directory)
adb_path = "./adb"  # Adjust if adb is located elsewhere
subprocess.run([adb_path, "start-server"])
subprocess.run([adb_path, "connect", "127.0.0.1:62001"])  # Replace with the actual device address


# Step 4: Load templates and dimensions
for name, (path, _) in templates.items():
    template = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    if template is None:
        print(f"{name}.png not found. Check the file path.")
        exit()
    templates[name] = (template, template.shape[::-1])

# Wait for the game to load
time.sleep(50)

# Capture the screen and search for a template
def find_and_click(name):
    template, (w, h) = templates[name]
    i = 0
    while i < 10:
        screen = cv2.cvtColor(np.array(pyautogui.screenshot()), cv2.COLOR_RGB2GRAY)
        result = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
        locations = np.where(result >= 0.8)
        
        if locations[0].size > 0:
            # Calculate center and click
            x, y = locations[1][0] + w // 2, locations[0][0] + h // 2
            pyautogui.click(x, y)
            print(f"{name}.png found and clicked at ({x}, {y})")
            return True
        else:
            i += 1
            print(f"{name}.png not found, rechecking... (attempt {i})")
            time.sleep(0.5)  # Optional delay to prevent too frequent screen checks

    # If 99 attempts are made without finding the image, return False
    print(f"{name}.png not found after {i} attempts.")
    return False


#Start Game
find_and_click("start")
time.sleep(2)
find_and_click("close1")
time.sleep(2)
find_and_click("return")
time.sleep(2)
find_and_click("close2")
time.sleep(2)


#elfclaim
find_and_click("lv0")
time.sleep(2)
find_and_click("chest1")
time.sleep(2)
find_and_click("return2")
time.sleep(2)


#Daily tasks
find_and_click("dailytasks")
time.sleep(2)  


#port cargo
find_and_click("portcargo")
find_and_click("go")
time.sleep(2)
find_and_click("monthlysignin")
find_and_click("signin")
time.sleep(2)
find_and_click("dailyoffer")
find_and_click("available")
time.sleep(60)
find_and_click("available")
time.sleep(120)
find_and_click("available")
time.sleep(120)
find_and_click("available")
time.sleep(180)
find_and_click("available")
time.sleep(240)
find_and_click("return")
time.sleep(2)


#fountain task
find_and_click("dailytasks")
time.sleep(2)
find_and_click("fountain-of-fate")
find_and_click("go")
time.sleep(2)
find_and_click("fountain")
time.sleep(2)
find_and_click("make-a-wish")
time.sleep(2)
for i in range(3):
    find_and_click("stone")
    time.sleep(2)
for i in range(3):
    find_and_click("iron")
    time.sleep(2)
for i in range(2):
    find_and_click("wood")
    time.sleep(2)
for i in range(2):
    find_and_click("grain")
    time.sleep(2)
for i in range(2):
    find_and_click("silver")
    time.sleep(2)
find_and_click("return")
time.sleep(2)


#infantry-training
find_and_click("dailytasks")
time.sleep(2)
find_and_click("infantry-training")
find_and_click("go")
time.sleep(2)
find_and_click("barracks")
time.sleep(2)
find_and_click("train1")
time.sleep(2)
find_and_click("switch-left")
find_and_click("num1450")
time.sleep(2)
pyautogui.press('delete')
pyautogui.press('delete')
pyautogui.press('delete')
pyautogui.press('delete')
pyautogui.press('delete')
time.sleep(2)
pyautogui.write('50')
time.sleep(2)
pyautogui.press('enter')
find_and_click("train2")
find_and_click("speedup1")
find_and_click("quickspeed1")
find_and_click("use1")
find_and_click("claim1")
find_and_click("return")
time.sleep(2)


#Deathmatch


#cavalary Training


#Archer Training


#Warmachine Training


#kill Monster


#Collect chestrewards
find_and_click("dailytasks")
find_and_click("chest2")
find_and_click("claim3")
find_and_click("chest3")
find_and_click("claim3")
time.sleep(2)
find_and_click("return")
time.sleep(2)


#mail
find_and_click("mail")
find_and_click("system")
find_and_click("allread")
find_and_click("claim2")
for i in range(2):
    find_and_click("return")
    