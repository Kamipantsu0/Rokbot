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
    "fountain": ("./images/fountain.png", None),
    "make-a-wish": ("./images/make-a-wish.png", None),
    "barracks": ("./images/barracks.png", None),
    "train1": ("./images/train1.png", None),
    "target-range": ("./images/target-range.png", None),
    "elvish-gardens": ("./images/elvish-gardens.png", None),
    "deathmatch1": ("./images/deathmatch1.png", None),
    "dragonschallenge": ("./images/dragonschallenge.png", None),
    "siege-works": ("./images/siege-works.png", None),
    "stables": ("./images/stables.png", None),
    "returnofthelord": ("./images/returnofthelord.png", None),
    "claimall": ("./images/claimall.png", None),
    "mail": ("./images/mail.png", None),
    "bag": ("./images/bag.png", None),
    "outside": ("./images/outside.png", None),
    "hallofheroes": ("./images/hallofheroes.png", None),
    "hero-summons2": ("./images/hero-summons2.png", None),
    "skill-shop": ("./images/skill-shop.png", None),
    "heroes": ("./images/heroes.png", None),
    "bank": ("./images/bank.png", None),
    
    
    
    #bank
    "taptodeposit": ("./images/bank/taptodeposit.png", None),
    "deposit": ("./images/bank/deposit.png", None),
    "suspend": ("./images/bank/suspend.png", None),
    "confirm1": ("./images/bank/confirm1.png", None),
    
    
    #elfprivelage
    "lv0": ("./images/elfprivelage/lv0.png", None),
    "chest": ("./images/elfprivelage/chest.png", None),
    "return2": ("./images/elfprivelage/return2.png", None),
    
    
    
    #deathmatch
    "challenge": ("./images/deathmatch/challenge.png", None),
    "challenge2": ("./images/deathmatch/challenge2.png", None),
    "challenge3": ("./images/deathmatch/challenge3.png", None),
    "ok": ("./images/deathmatch/ok.png", None),
    "back": ("./images/deathmatch/back.png", None),
    "close": ("./images/deathmatch/close.png", None),
    "chest4": ("./images/deathmatch/chest4.png", None),
    "claim4": ("./images/deathmatch/claim4.png", None),
    "return3": ("./images/deathmatch/return3.png", None),
    
    
    
    #dragonschallenge
    "quick-mode1": ("./images/dragonschallenge/quick-mode1.png", None),
    "battle1": ("./images/dragonschallenge/battle1.png", None),
    "thefallows1": ("./images/dragonschallenge/thefallows1.png", None),
    "thefallows7": ("./images/dragonschallenge/thefallows7.png", None),
    "thefallows8": ("./images/dragonschallenge/thefallows8.png", None),
    "thefallows9": ("./images/dragonschallenge/thefallows9.png", None),
    "thefallows10": ("./images/dragonschallenge/thefallows10.png", None),
    "thefallows11": ("./images/dragonschallenge/thefallows11.png", None),
    "thefallows12": ("./images/dragonschallenge/thefallows12.png", None),
    "thefallows13": ("./images/dragonschallenge/thefallows13.png", None),
    "thefallows14": ("./images/dragonschallenge/thefallows14.png", None),
    "thefallows15": ("./images/dragonschallenge/thefallows15.png", None),
    "thefallows16": ("./images/dragonschallenge/thefallows16.png", None),
    "thefallows17": ("./images/dragonschallenge/thefallows17.png", None),
    "thefallows18": ("./images/dragonschallenge/thefallows18.png", None),
    "thefallows19": ("./images/dragonschallenge/thefallows19.png", None),
    "thefallows20": ("./images/dragonschallenge/thefallows20.png", None),
    "thefallows21": ("./images/dragonschallenge/thefallows21.png", None),
    "thefallows22": ("./images/dragonschallenge/thefallows22.png", None),
    "thefallows23": ("./images/dragonschallenge/thefallows23.png", None),
    "thefallows24": ("./images/dragonschallenge/thefallows24.png", None),
    "thefallows25": ("./images/dragonschallenge/thefallows25.png", None),
    "thefallows26": ("./images/dragonschallenge/thefallows26.png", None),
    "thefallows27": ("./images/dragonschallenge/thefallows27.png", None),
    "thefallows28": ("./images/dragonschallenge/thefallows28.png", None),
    "thefallows29": ("./images/dragonschallenge/thefallows29.png", None),
    "thefallows30": ("./images/dragonschallenge/thefallows30.png", None),
    
    "attack1": ("./images/dragonschallenge/attack1.png", None),
    "rafe": ("./images/dragonschallenge/rafe.png", None),
    "recommend1": ("./images/dragonschallenge/recommend1.png", None),
    "ok2": ("./images/dragonschallenge/ok2.png", None),
    "dispatch": ("./images/dragonschallenge/dispatch.png", None),
    "attack2": ("./images/dragonschallenge/attack2.png", None),
    "treasure1": ("./images/dragonschallenge/treasure1.png", None),
    "treasure2": ("./images/dragonschallenge/treasure2.png", None),
    "claim5": ("./images/dragonschallenge/claim5.png", None),
    
    
    
    #dailytaks
    "go": ("./images/dailytasks/go.png", None),
    "deathmatch": ("./images/dailytasks/deathmatch.png", None),
    "portcargo": ("./images/dailytasks/portcargo.png", None),
    "fountain-of-fate": ("./images/dailytasks/fountain-of-fate.png", None),
    "infantry-training": ("./images/dailytasks/infantry-training.png", None),
    "archer-training": ("./images/dailytasks/archer-training.png", None),
    "warmachine-training": ("./images/dailytasks/warmachine-training.png", None),
    "cavalry-training": ("./images/dailytasks/cavalry-training.png", None),
    "kill-monsters": ("./images/dailytasks/kill-monsters.png", None),
    "dragons-challenge": ("./images/dailytasks/dragons-challenge.png", None),
    "grain-collection": ("./images/dailytasks/grain-collection.png", None),
    "lumber-collection": ("./images/dailytasks/lumber-collection.png", None),
    "lumber-boost": ("./images/dailytasks/lumber-boost.png", None),
    "farm-boost": ("./images/dailytasks/farm-boost.png", None),
    "silver-boost": ("./images/dailytasks/silver-boost.png", None),
    "hero-summons": ("./images/dailytasks/hero-summons.png", None),
    "heros-skill": ("./images/dailytasks/heros-skill.png", None),
    "drunken-wizard": ("./images/dailytasks/drunken-wizard.png", None),
    "knowledge-potion": ("./images/dailytasks/knowledge-potion.png", None),
    "bank-deposit": ("./images/dailytasks/bank-deposit.png", None),
    "chest2": ("./images/dailytasks/chest2.png", None),
    "chest3": ("./images/dailytasks/chest3.png", None),
    "bronze-chest": ("./images/dailytasks/bronze-chest.png", None),
    "silver-chest": ("./images/dailytasks/silver-chest.png", None),
    "gold-chest": ("./images/dailytasks/gold-chest.png", None),
    "claim3": ("./images/dailytasks/claim3.png", None),
    
    
    
    #portcargo
    "available": ("./images/portcargo/available.png", None),
    "monthlysignin": ("./images/portcargo/monthlysignin.png", None),
    "signin": ("./images/portcargo/signin.png", None),
    "dailyoffer": ("./images/portcargo/dailyoffer.png", None),
    
    
    
    #troopstrain
    "train2": ("./images/troopstrain/train2.png", None),
    "reset": ("./images/troopstrain/reset.png", None),
    "iron1": ("./images/troopstrain/iron1.png", None),
    "minus": ("./images/troopstrain/minus.png", None),
    "switch-left": ("./images/troopstrain/switch-left.png", None),
    "speedup1": ("./images/troopstrain/speedup1.png", None),
    "quickspeed1": ("./images/troopstrain/quickspeed1.png", None),
    "use1": ("./images/troopstrain/use1.png", None),
    "claim1": ("./images/troopstrain/claim1.png", None),
    
    
    
    #fountain
    "grain": ("./images/fountain/grain.png", None),
    "wood": ("./images/fountain/wood.png", None),
    "iron": ("./images/fountain/iron.png", None),
    "silver": ("./images/fountain/silver.png", None),
    "stone": ("./images/fountain/stone.png", None),
    
    
    
    #herosummons
    "superb-summon": ("./images/herosummons/superb-summon.png", None),
    "superb-freesummon": ("./images/herosummons/superb-freesummon.png", None),
    "elite-summon": ("./images/herosummons/elite-summon.png", None),
    "elite-freesummon": ("./images/herosummons/elite-freesummon.png", None),
    "summon1timesuperb": ("./images/herosummons/summon1timesuperb.png", None),
    "summon1timeelite": ("./images/herosummons/summon1timeelite.png", None),
    
    
    #herosummons
    "exchange-slot": ("./images/skillshop/exchange-slot.png", None),
    "exchangesilver": ("./images/skillshop/exchangesilver.png", None),
    "plus": ("./images/skillshop/plus.png", None),
    "paysilver": ("./images/skillshop/paysilver.png", None),
    
    
    #map
    "searchtool": ("./images/map/searchtool.png", None),
    "monsterslot": ("./images/map/monsterslot.png", None),
    "lumberslot": ("./images/map/lumberslot.png", None),
    "farmslot": ("./images/map/farmslot.png", None),
    "lumbermillfarm": ("./images/map/lumbermillfarm.png", None),
    "grainfarm": ("./images/map/grainfarm.png", None),
    "collect1": ("./images/map/collect1.png", None),
    "go2": ("./images/map/go2.png", None),
    "activatevipstatus": ("./images/map/activatevipstatus.png", None),
    "activatevip": ("./images/map/activatevip.png", None),
    "use": ("./images/map/use.png", None),
    "dispatch2": ("./images/map/dispatch2.png", None),
    "autoslay": ("./images/map/autoslay.png", None),
    "go3": ("./images/map/go3.png", None),
    "start2": ("./images/map/start2.png", None),
    "mycastle": ("./images/map/mycastle.png", None),
    "collecting": ("./images/map/collecting.png", None),
    "back2": ("./images/map/back2.png", None),
    
    
    
    #bag
    "others": ("./images/bag/others.png", None),
    "lumberboost": ("./images/bag/lumberboost.png", None),
    "grainboost": ("./images/bag/grainboost.png", None),
    "silverboost": ("./images/bag/silverboost.png", None),
    "use3": ("./images/bag/use3.png", None),
    
    
    #heroes
    "zantar": ("./images/heroes/zantar.png", None),
    "upgrade1": ("./images/heroes/upgrade1.png", None),
    "orangepotion": ("./images/heroes/orangepotion.png", None),
    "return4": ("./images/heroes/return4.png", None),
    
    
    #mail
    "system": ("./images/mail/system.png", None),
    "events": ("./images/mail/events.png", None),
    "allread": ("./images/mail/allread.png", None),
    "claim2": ("./images/mail/claim2.png", None),
    
}


# Step 1: Run 'run_game.bat' to launch the game
subprocess.run(["run game.bat"])


# Step 2: Load templates and dimensions
for name, (path, _) in templates.items():
    template = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    if template is None:
        print(f"{name}.png not found. Check the file path.")
        exit()
    templates[name] = (template, template.shape[::-1])


# Capture the screen and search for a template
def find_and_click(name):
    template, (w, h) = templates[name]
    i = 0
    while i < 5:
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


def start():
    # Wait for the game to load
    time.sleep(50)
    #Start Game
    if find_and_click("start"):
        time.sleep(30)
        find_and_click("close1")
        time.sleep(4)
        find_and_click("return")
        time.sleep(4)
        find_and_click("close2")
        time.sleep(4)
    else:
        start()


def claimrewards():
    if find_and_click("returnofthelord"):
        time.sleep(2)
        find_and_click("claimall")
        time.sleep(2)
        find_and_click("return")


def elfclaim():
    time.sleep(2)
    if find_and_click("lv0"):
        time.sleep(3)
        find_and_click("chest")
        time.sleep(3)
        find_and_click("return2")
        time.sleep(3)


def Deathmatch():
    find_and_click("dailytasks")
    time.sleep(3)  
    if find_and_click("deathmatch"):
        find_and_click("go")
        time.sleep(3)
        find_and_click("elvish-gardens")
        time.sleep(1)
        x, y = pyautogui.position()
        pyautogui.click(x , y + 20)
        time.sleep(2)
        for i in range(5): 
            find_and_click("deathmatch1")
            time.sleep(3)
            find_and_click("challenge")
            time.sleep(3)
            find_and_click("challenge2")
            time.sleep(4)
            find_and_click("challenge3")
            time.sleep(4)
            find_and_click("ok")
            time.sleep(4)
            find_and_click("back")
        time.sleep(2)
        find_and_click("close")
        for i in range(4):
            time.sleep(2)
            find_and_click("chest4")
            find_and_click("claim4")
            pyautogui.click(y=100, button='left')
    find_and_click("return3")
    time.sleep(1)
    find_and_click("return")
        
    
def portcargo():
    find_and_click("dailytasks")
    time.sleep(3)  
    if find_and_click("portcargo"):
        find_and_click("go")
        time.sleep(3)
        if find_and_click("monthlysignin"):
            time.sleep(3)
            find_and_click("signin")
            time.sleep(3)
            find_and_click("dailyoffer")
            time.sleep(3)
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
        find_and_click("available")
        time.sleep(3)
    find_and_click("return")
    time.sleep(3)


def fountaintask():
    find_and_click("dailytasks")
    time.sleep(3)
    if find_and_click("fountain-of-fate"):
        find_and_click("go")
        time.sleep(3)
        find_and_click("fountain")
        time.sleep(2)
        x, y = pyautogui.position()
        pyautogui.click(x , y + 20)
        time.sleep(1)
        find_and_click("make-a-wish")
        time.sleep(3)
        for i in range(3):
            find_and_click("stone")
            time.sleep(1)
        for i in range(3):
            find_and_click("iron")
            time.sleep(1)
        for i in range(2):
            find_and_click("wood")
            time.sleep(1)
        for i in range(2):
            find_and_click("grain")
            time.sleep(1)
        for i in range(2):
            find_and_click("silver")
            time.sleep(1)
        time.sleep(1)
    find_and_click("return")
    time.sleep(3)


def infantrytraining():
    find_and_click("dailytasks")
    time.sleep(3)
    if find_and_click("infantry-training"):
        find_and_click("go")
        time.sleep(3)
        find_and_click("barracks")
        time.sleep(3)
        find_and_click("train1")
        time.sleep(3)
        find_and_click("switch-left")
        x, y = pyautogui.position()
        time.sleep(1)
        for i in range(3391):
            pyautogui.click(x + 25 ,y + 225)
        time.sleep(1)
        find_and_click("train2")
        find_and_click("speedup1")
        find_and_click("quickspeed1")
        find_and_click("use1")
        find_and_click("claim1")
    find_and_click("return")
    time.sleep(3)


def archertraining():
    find_and_click("dailytasks")
    time.sleep(3)
    if find_and_click("archer-training"):
        find_and_click("go")
        time.sleep(3)
        find_and_click("target-range")
        find_and_click("train1")
        time.sleep(3)
        find_and_click("switch-left")
        x, y = pyautogui.position()
        time.sleep(1)
        for i in range(3234):
            pyautogui.click(x + 25 ,y + 225)
        time.sleep(1)
        find_and_click("train2")
        find_and_click("speedup1")
        find_and_click("quickspeed1")
        find_and_click("use1")
        find_and_click("claim1")
    find_and_click("return")
    time.sleep(3)


def warmachinetraining():
    find_and_click("dailytasks")
    time.sleep(3)
    if find_and_click("warmachine-training"):
        find_and_click("go")
        find_and_click("siege-works")
        find_and_click("train1")
        time.sleep(3)
        find_and_click("switch-left")
        x, y = pyautogui.position()
        time.sleep(1)
        for i in range(6271):
            pyautogui.click(x + 25 ,y + 225)
        time.sleep(1)
        find_and_click("train2")
        find_and_click("speedup1")
        find_and_click("quickspeed1")
        find_and_click("use1")
        find_and_click("claim1")
    find_and_click("return")
    time.sleep(3)


def cavalarytraining():
    find_and_click("dailytasks")
    time.sleep(3)
    if find_and_click("cavalry-training"):
        find_and_click("go")
        find_and_click("stables")
        find_and_click("train1")
        time.sleep(3)
        find_and_click("switch-left")
        x, y = pyautogui.position()
        time.sleep(1)
        for i in range(3226):
            pyautogui.click(x + 25 ,y + 225)
        time.sleep(1)
        find_and_click("train2")
        find_and_click("speedup1")
        find_and_click("quickspeed1")
        find_and_click("use1")
        find_and_click("claim1")
    find_and_click("return")
    time.sleep(3)


def killmonster():
    find_and_click("dailytasks")
    time.sleep(3)
    if find_and_click("kill-monsters"):
        find_and_click("go")
        time.sleep(3)
        find_and_click("searchtool")
        time.sleep(3)
        find_and_click("monsterslot")
        time.sleep(3)
        find_and_click("go2")
        time.sleep(3)
        find_and_click("activatevipstatus")
        time.sleep(3)
        find_and_click("activatevip")
        time.sleep(3)
        for i in range(2):
            find_and_click("use")
            time.sleep(2)
        time.sleep(3)
        for i in range(2):
            find_and_click("return")
        time.sleep(2)
        find_and_click("autoslay")
        time.sleep(2)
        find_and_click("go3")
        time.sleep(2)
        find_and_click("start2")
        time.sleep(2)
        find_and_click("mycastle")
        time.sleep(2)
    find_and_click("return")
    time.sleep(2)
        

def lumberboost():
    find_and_click("dailytasks")
    time.sleep(6)
    if find_and_click("lumber-boost"):
        find_and_click("go")
        time.sleep(3)
        find_and_click("bag")
        time.sleep(2)
        find_and_click("others")
        time.sleep(1)
        find_and_click("lumberboost")
        time.sleep(1)
        find_and_click("use3")
        time.sleep(1)
        find_and_click("ok")
        time.sleep(1)
    find_and_click("return")
    time.sleep(1)
    
    
def grainboost():
    find_and_click("dailytasks")
    time.sleep(3)
    if find_and_click("farm-boost"):
        find_and_click("go")
        time.sleep(3)
        find_and_click("bag")
        time.sleep(2)
        find_and_click("others")
        time.sleep(1)
        find_and_click("grainboost")
        time.sleep(1)
        find_and_click("use3")
        time.sleep(1)
        find_and_click("ok")
        time.sleep(1)
    find_and_click("return")
    time.sleep(1)
    
    
def silverboost():
    find_and_click("dailytasks")
    time.sleep(3)
    if find_and_click("silver-boost"):
        find_and_click("go")
        time.sleep(3)
        find_and_click("bag")
        time.sleep(2)
        find_and_click("others")
        time.sleep(1)
        find_and_click("silverboost")
        time.sleep(1)
        find_and_click("use3")
        time.sleep(1)
        find_and_click("ok")
        time.sleep(1)
    find_and_click("return")
    time.sleep(1)
    

def lumbercollection():
    find_and_click("dailytasks")
    time.sleep(3)
    find_and_click("lumber-collection")
    find_and_click("go")
    time.sleep(5)
    find_and_click("searchtool")
    time.sleep(3)
    find_and_click("lumberslot")
    time.sleep(3)
    find_and_click("go2")
    time.sleep(3)
    if find_and_click("activatevipstatus"):
        time.sleep(3)
        find_and_click("activatevip")
        time.sleep(3)
        for i in range(2):
            find_and_click("use")
            time.sleep(2)
        time.sleep(3)
        for i in range(2):
            find_and_click("return")
    time.sleep(2)
    
    def lumberdispatch():
        find_and_click("go2")
        time.sleep(3)
        find_and_click("lumbermillfarm")
        time.sleep(2)
        if find_and_click("collect1"):
            time.sleep(2)
            find_and_click("dispatch2")
            time.sleep(2)
        else:
            lumberdispatch()
                   
    lumberdispatch()


def graincollection():
    find_and_click("dailytasks")
    time.sleep(3)
    find_and_click("grain-collection")
    find_and_click("go")
    time.sleep(3)
    find_and_click("searchtool")
    time.sleep(3)
    find_and_click("farmslot")
    time.sleep(3)
    find_and_click("go2")
    time.sleep(3)
    if find_and_click("activatevipstatus"):
        time.sleep(3)
        find_and_click("activatevip")
        time.sleep(3)
        for i in range(2):
            find_and_click("use")
            time.sleep(2)
        time.sleep(3)
        for i in range(2):
            find_and_click("return")
    time.sleep(2)
    
    def graindispatch():
        find_and_click("go2")
        time.sleep(3)
        find_and_click("grainfarm")
        time.sleep(2)
        if find_and_click("collect1"):
            time.sleep(2)
            find_and_click("dispatch2")
            time.sleep(2)
        else:
            graindispatch()
            
    graindispatch() 


def herosummons():
    find_and_click("dailytasks")
    time.sleep(3)  
    if find_and_click("hero-summons"):
        find_and_click("go")
        time.sleep(3)
        find_and_click("hallofheroes")
        time.sleep(1)
        find_and_click("hero-summons2")
        time.sleep(3)
        
        def superbsummon():
            find_and_click("superb-summon")
            time.sleep(2)
            for i in range(2):
                if find_and_click("superb-freesummon") or find_and_click("summon1timesuperb"):
                    time.sleep(4)
                    pyautogui.click(x=100, button='left')
                    time.sleep(2)
                else:
                    superbsummon()
        def elitesummon():
            find_and_click("elite-summon")
            time.sleep(2)
            for i in range(3):
                if find_and_click("elite-freesummon") or find_and_click("summon1timeelite"):
                    time.sleep(4)
                    pyautogui.click(x=100, button='left')
                    time.sleep(2)
                else:
                    elitesummon()
                    
        superbsummon()
        elitesummon()            
    find_and_click("return")
    time.sleep(2)
           

def heroskills():
    find_and_click("dailytasks")
    time.sleep(3)  
    if find_and_click("heros-skill"):
        find_and_click("go")
        time.sleep(3)
        find_and_click("hallofheroes")
        time.sleep(1)
        find_and_click("skill-shop")
        time.sleep(3)
        find_and_click("exchange-slot")
        time.sleep(2)
        find_and_click("exchangesilver")
        x, y = pyautogui.position()
        pyautogui.click(x + 350 ,y)
        time.sleep(1)
        find_and_click("plus")
        find_and_click("paysilver")
        time.sleep(2)
        find_and_click("ok")
        time.sleep(2)
    find_and_click("return")
    time.sleep(2)

    
def dragonschallenge():
    if find_and_click("dailytasks"):
        time.sleep(3)
        find_and_click("dragons-challenge")
        find_and_click("go")
        time.sleep(3)
        find_and_click("elvish-gardens")
        time.sleep(1)
        x, y = pyautogui.position()
        pyautogui.click(x , y + 20)
        time.sleep(1)
        find_and_click("dragonschallenge")
    time.sleep(2)
    
    for i in range(28):
        
        def atkdragonschallenge():    
            if find_and_click("attack1"):
                time.sleep(1)
                find_and_click("rafe")
                time.sleep(1)
                find_and_click("recommend1")
                time.sleep(1)
                find_and_click("ok2")
                time.sleep(1)
                find_and_click("dispatch")
                time.sleep(1)
                find_and_click("attack2")
                time.sleep(0.5)
                find_and_click("return")
                find_and_click("battle1")
                time.sleep(1)
        
        find_and_click("battle1")
        time.sleep(1)
        
        
        if find_and_click("treasure1") or find_and_click("treasure2"):
            time.sleep(1)
            find_and_click("claim5")
            time.sleep(1)
            pyautogui.click(y=100, button='left')
            time.sleep(1)
                
        if find_and_click("thefallows7"):
            time.sleep(1)
            x, y = pyautogui.position()
            pyautogui.click(x + 35, y + 80)
            time.sleep(1)
            atkdragonschallenge()
            
        if find_and_click("thefallows8"):
            time.sleep(1)
            x, y = pyautogui.position()
            pyautogui.click(x + 35, y + 80)
            time.sleep(1)
            atkdragonschallenge()
            
        if find_and_click("thefallows9"):
            time.sleep(1)
            x, y = pyautogui.position()
            pyautogui.click(x + 35, y + 80)
            time.sleep(1)
            atkdragonschallenge()
            
        if find_and_click("thefallows10"):
            time.sleep(1)
            x, y = pyautogui.position()
            pyautogui.click(x + 35, y + 80)
            time.sleep(1)
            atkdragonschallenge()
         
        if find_and_click("thefallows11"):
            time.sleep(1)
            x, y = pyautogui.position()
            pyautogui.click(x + 35, y + 80)
            time.sleep(1)
            atkdragonschallenge()
            
        if find_and_click("thefallows12"):
            time.sleep(1)
            x, y = pyautogui.position()
            pyautogui.click(x + 35, y + 80)
            time.sleep(1)
            atkdragonschallenge()
            
        if find_and_click("thefallows13"):
            time.sleep(1)
            x, y = pyautogui.position()
            pyautogui.click(x + 35, y + 80)
            time.sleep(1)
            atkdragonschallenge()
            
        if find_and_click("thefallows14"):
            time.sleep(1)
            x, y = pyautogui.position()
            pyautogui.click(x + 35, y + 80)
            time.sleep(1)
            atkdragonschallenge()
            
        if find_and_click("thefallows15"):
            time.sleep(1)
            x, y = pyautogui.position()
            pyautogui.click(x + 35, y + 80)
            time.sleep(1)
            atkdragonschallenge()
            
        if find_and_click("thefallows16"):
            time.sleep(1)
            x, y = pyautogui.position()
            pyautogui.click(x + 35, y + 80)
            time.sleep(1)
            atkdragonschallenge()
            
        if find_and_click("thefallows17"):
            time.sleep(1)
            x, y = pyautogui.position()
            pyautogui.click(x + 35, y + 80)
            time.sleep(1)
            atkdragonschallenge()
            
        if find_and_click("thefallows18"):
            time.sleep(1)
            x, y = pyautogui.position()
            pyautogui.click(x + 35, y + 80)
            time.sleep(1)
            atkdragonschallenge()
            
        if find_and_click("thefallows19"):
            time.sleep(1)
            x, y = pyautogui.position()
            pyautogui.click(x + 35, y + 80)
            time.sleep(1)
            atkdragonschallenge()
            
        if find_and_click("thefallows20"):
            time.sleep(1)
            x, y = pyautogui.position()
            pyautogui.click(x + 35, y + 80)
            time.sleep(1)
            atkdragonschallenge()
            
        if find_and_click("thefallows21"):
            time.sleep(1)
            x, y = pyautogui.position()
            pyautogui.click(x + 35, y + 80)
            time.sleep(1)
            atkdragonschallenge()
            
        if find_and_click("thefallows22"):
            time.sleep(1)
            x, y = pyautogui.position()
            pyautogui.click(x + 35, y + 80)
            time.sleep(1)
            atkdragonschallenge()
            
        if find_and_click("thefallows23"):
            time.sleep(1)
            x, y = pyautogui.position()
            pyautogui.click(x + 35, y + 80)
            time.sleep(1)
            atkdragonschallenge()
            
        if find_and_click("thefallows24"):
            time.sleep(1)
            x, y = pyautogui.position()
            pyautogui.click(x + 35, y + 80)
            time.sleep(1)
            atkdragonschallenge()
            
        if find_and_click("thefallows25"):
            time.sleep(1)
            x, y = pyautogui.position()
            pyautogui.click(x + 35, y + 80)
            time.sleep(1)
            atkdragonschallenge()
            
        if find_and_click("thefallows26"):
            time.sleep(1)
            x, y = pyautogui.position()
            pyautogui.click(x + 35, y + 80)
            time.sleep(1)
            atkdragonschallenge()
            
        if find_and_click("thefallows27"):
            time.sleep(1)
            x, y = pyautogui.position()
            pyautogui.click(x + 35, y + 80)
            time.sleep(1)
            atkdragonschallenge()
            
        if find_and_click("thefallows28"):
            time.sleep(1)
            x, y = pyautogui.position()
            pyautogui.click(x + 35, y + 80)
            time.sleep(1)
            atkdragonschallenge()
            
        if find_and_click("thefallows29"):
            time.sleep(1)
            x, y = pyautogui.position()
            pyautogui.click(x + 35, y + 80)
            time.sleep(1)
            atkdragonschallenge()
            
        if find_and_click("thefallows30"):
            time.sleep(1)
            x, y = pyautogui.position()
            pyautogui.click(x + 35, y + 80)
            time.sleep(1)
            atkdragonschallenge()
                

def dragonschallenge2():
    find_and_click("dailytasks")
    time.sleep(3)
    if find_and_click("dragons-challenge"):
        find_and_click("go")
        time.sleep(3)
        find_and_click("elvish-gardens")
        time.sleep(1)
        x, y = pyautogui.position()
        pyautogui.click(x , y + 20)
        time.sleep(1)
        find_and_click("dragonschallenge")
        time.sleep(2)
        find_and_click("quick-mode1")
        time.sleep(2)
        find_and_click("ok")
        time.sleep(2)
    find_and_click("return")
    time.sleep(2)
    

def knowledgepotion():
    find_and_click("dailytasks")
    time.sleep(3)
    if find_and_click("knowledge-potion"):
        find_and_click("go")
        time.sleep(3)
        find_and_click("heroes")
        time.sleep(2)
        find_and_click("zantar")
        time.sleep(1)
        find_and_click("upgrade1")
        time.sleep(1)
        for i in range(2):
            find_and_click("orangepotion")
        find_and_click("return4")
        time.sleep(1)
    find_and_click("return")
    time.sleep(2)
        

def bankdeposit():
    find_and_click("dailytasks")
    time.sleep(3)
    if find_and_click("bank-deposit"):
        find_and_click("go")
        time.sleep(6)
        find_and_click("bank")
        time.sleep(2)
        find_and_click("taptodeposit")
        time.sleep(1)
        find_and_click("deposit")
        time.sleep(1)
        find_and_click("suspend")
        time.sleep(1)
        find_and_click("confirm1")
        time.sleep(1)
    for i in range(2):
        find_and_click("return")
    time.sleep(2)
        
          
def collectchestrewards():
    find_and_click("outside")
    time.sleep(4)
    if find_and_click("collecting") or find_and_click("back2"):
        time.sleep(2)
        collectchestrewards()
    else:
        find_and_click("dailytasks")
        time.sleep(3)
        for i in range(3):
            find_and_click("chest2")
            time.sleep(2)
            find_and_click("claim3")
            time.sleep(2)
            pyautogui.click(y=100, button='left')
            time.sleep(2)
            find_and_click("chest3")
            time.sleep(2)
            find_and_click("claim3")
            time.sleep(2)
            pyautogui.click(y=100, button='left')
            time.sleep(2)
        find_and_click("bronze-chest")
        time.sleep(2)
        find_and_click("claim3")
        time.sleep(2)
        pyautogui.click(y=100, button='left')
        time.sleep(2)
        find_and_click("silver-chest")
        time.sleep(2)
        find_and_click("claim3")
        time.sleep(2)
        pyautogui.click(y=100, button='left')
        time.sleep(2)
        find_and_click("gold-chest")
        time.sleep(2)
        find_and_click("claim3")
        time.sleep(2)
        pyautogui.click(y=100, button='left')
        time.sleep(2)
        find_and_click("return")
        time.sleep(3)


def mail():
    if find_and_click("mail"):
        time.sleep(3)
        find_and_click("system")
        time.sleep(3)
        find_and_click("allread")
        time.sleep(3)
        find_and_click("claim2")
        time.sleep(3)
        find_and_click("return")
        time.sleep(2)
        find_and_click("events")
        time.sleep(3)
        find_and_click("allread")
        time.sleep(3)
        find_and_click("claim2")
        time.sleep(3)
    for i in range(2):
        find_and_click("return")
    
    
    
#start()
#claimrewards()
#elfclaim()

## Those are dailytasks:

#Deathmatch()
#portcargo()
#fountaintask()
infantrytraining()
archertraining()
cavalarytraining()
warmachinetraining()
killmonster()
lumbercollection()
graincollection()
dragonschallenge2()
##dragonschallenge() ==> original but will not be used
grainboost()
lumberboost()
silverboost()
herosummons()
heroskills()
knowledgepotion() 
bankdeposit()


collectchestrewards()
mail()
