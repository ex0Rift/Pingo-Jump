import pygame , colours , random , sys , copy , json

pygame.init()

screenWidth,screenHeight = 800 , 600
screen = pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption("Pingo Jump")

clock = pygame.time.Clock()
running = True

#variables
time = 0                    #The clock for tracking how much time passed
amountOfClouds = 7          #controls how many clouds are on screen
player_x,player_y = 200,500 #the player coordiantes
ground_x = 0                #the ground current pan position
fall_speed = 1.8            #sets default fall starting speed
jump_speed = 10             #sets default jump starting speed
onGround = False            #stops any gravity if touching ground
jump = 0                    #for controling jump time sets default.
movingleft = 0              #default for moving left animation
movingright = 0             #default for moving right anumation
activeClouds=[]             #defining list for clouds data
clouds = []                 #defining useable cloud list
levelStars = [0,0]          #defins the list where the quantity of stars you have for a level is stored
keybox = True               #determins whether or not to show the keybind turotial
isLevelChange = True        #activates part to increment what level it is currently
levelID = 0                 #This is what level is currently in use 
amountOfLevels = 2          #amount of levels in game
collected_coins = 0         #how many coins the player has
winTimer = 0                #defines the variable for the length of the win timer
winContinue = False         #determins weather the next screen after winning is ready to be shown
score = 0                   #final score each level determined by the amount of coins / least amoun of time
totalScore = 0              #The total score across multiple levels
totalCoins = 0              #The total amount of coins the player have, they can be spent
flag_x , flag_y = 610 , 210 #coordinates of the flag, starting pos as shown
flagTexture = ''            #define the variable for storing which state the flag is in
spikeBallAnimation = 0      #defines spikeball animation loop control
spikeBallFrame = ''         #defines which spikeball fram it is on
spikeBallSpeed = 11         #defines the speed of which the spikeballs will move
platformSpeed = 4           #defines the speed of the moving platforms
platformCollided = False    #stops other collsion if already on paltform
renderDebug = False         #determins whether or not the debug menu will be renderd
saving = 0                  #defines the saving timer for showing save icon
key_jump = pygame.K_UP      #keybind for the jump button
key_left = pygame.K_LEFT    #keybind for the walk left button
key_right = pygame.K_RIGHT  #keybind for the walk right button
current_pingo = 0           #the current pingo the player has selected
current_flag = 0            #the current flag the player has selected
displayed_flag = 0          #the flag being shown to the user in wardrobe
buttonCooldown = 0          #defines the variable that controls how many times a button can be pressed at once
buttonCooldownLength = 20   #defines the amount of frames the button will be disabled
fallAnimation = 0           #defines the fall animation timer
onGroundTimer = 0           #defines extra time ong ground is in place for improved edge jumping #not implemented
velocity = 10               #walking speed
keyPressed = False          #weather or not movment key was pressed

#This list is up here purly so it is defined before data is loaded
flags_purchase = [
    [0,True],
    [20,False],
    [50,False],
    [80,False]
]

#load saved data
with open("user_data/settings.json","r") as file:
    try:
        load = json.load(file)

        totalScore = load["score"]
        key_jump = load["jump"]
        key_left = load["left"]
        key_right =load["right"]
        renderDebug = load["save"]
        levelStars = load["stars"]
        current_pingo = load["pingo"]
        current_flag = load["flag"]
        totalCoins = load["coins"]
    except:
        pass

with open("user_data/purchases.json") as file:
    try:
        flags_purchase = json.load(file)
    except:
        pass

#text for in game
pixel_font = pygame.font.Font("fonts/upheavtt.ttf",40)
header_font = pygame.font.Font("fonts/buble.TTF",80)
subTitle_font = pygame.font.Font("fonts/buble.TTF",50)
smallText_font = pygame.font.Font("fonts/upheavtt.ttf",20)

signText_001 = pixel_font.render("Walk up to the wall!",True,colours.black)
signText_002 = pixel_font.render("trust me it wont hurt.",True,colours.black)
signText_003 = pixel_font.render("See...you rolled up that wall ",True,colours.black)
signText_004 = pixel_font.render("like a boss!", True, colours.black)
signText_005 = pixel_font.render("Watch out for spike balls...",True,colours.black)
signText_006 = pixel_font.render("They hurt quite alot!",True,colours.black)

#loads all the  image assets from imageLoading.py
from imageLoading import *

#generate masks
player_mask = pygame.mask.from_surface(player_sprite)
firstLevel_mask = pygame.mask.from_surface(firstLevel)
secondLevel_mask = pygame.mask.from_surface(secondLevel)
sign_mask = pygame.mask.from_surface(sign)
coin_mask = pygame.mask.from_surface(coin)
spikeBall_mask = pygame.mask.from_surface(spikeBall)
platform_mask = pygame.mask.from_surface(platform)

clouds.append(cloudone)
clouds.append(cloudtwo)
clouds.append(cloudthree)
clouds.append(cloudfour)
clouds.append(cloudfive)
clouds.append(cloudsix)


#first is level its on, second is x coord , third is y coord
coins=[
    [0,ground_x+2000,90],
    [0,ground_x+2060,90],
    [0,ground_x+2120,90],
    [0,ground_x+2180,90],
    [0,ground_x+1250,450],
    [0,ground_x+3050,40],
    [0,ground_x+3110,40],
    [0,ground_x+3170,40],
    [0,ground_x+3230,40],
    [0,ground_x+4200,115],
    [0,ground_x+4250,115],
    [0,ground_x+4300,115],
    [1,ground_x+1840,400],
    [1,ground_x+2200,50],
    [1,ground_x+2260,50],
    [1,ground_x+3500,240],
    [1,ground_x+3550,240],
    [1,ground_x+3600,240],
    [1,ground_x+3650,240],
    [1,ground_x+2580,300],
    [1,ground_x+2580,350],
    [1,ground_x+2580,400]
]

powerUps = [
    [0,ground_x+200,300]
]

#
# first is the level its on , second is x coord , third is y coord ,foruth is x far left, fith is final x far right , sixth is movment direction('pos' positve 'neg' negative)
#
spikeBalls = [
    [0,ground_x+4000,508,4000,4500,'pos'],
    [1,ground_x+300,490,300,850,'pos']
]

platforms = [
    [1, ground_x+2800,300,2800,3300,'pos'],
    [1,ground_x+4000,400,3600,4000,'neg']
]

levels = [
    [firstLevel,firstLevel_mask],
    [secondLevel,secondLevel_mask]
]

starPoints = [
    [500,2000,5000],
    [500,2000,4000]
]

exitGates=[
    [ground_x+4672,395],
    [ground_x+4672,395]
]

panoramas = [
    panorama,
    panorama_two
]


pingos = [
    [
        player_sprite,
        player_left,
        player_left_walk,
        player_right,
        player_right_walk,
        player_roll,
        player_fall,
        player_fall_two,
        pingoDefaultUI
    ],
    [
        player_sprite_gold,
        player_left_gold,
        player_left_walk_gold,
        player_right_gold,
        player_right_walk_gold,
        player_roll_gold,
        player_fall_gold,
        player_fall_two_gold,
        pingoGoldUI
    ]
]

flags = [
    [
        flag_default_one,
        flag_default_two
    ],
    [
        flag_red_one,
        flag_red_two
    ],
    [
        flag_blue_one,
        flag_blue_two
    ],
    [
        flag_green_one,
        flag_green_two
    ]
]

#
#Different game screens here
#

def MainMenu():
    global buttonCooldown
    text_title = header_font.render("Pingo Jump", True, colours.white)
    display_pingo = pygame.transform.scale(pingos[current_pingo][0],(128,128))
    margin = [120]
    buttonCooldown = buttonCooldownLength-15
    menu = True
    while menu:
        mouse_pos = pygame.mouse.get_pos()
        mouse_press = pygame.mouse.get_pressed()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                SaveGame()
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if (
                    event.key == pygame.K_RETURN or
                    event.key == pygame.K_SPACE
                    ):
                    menu = False
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit(0)
        
        screen.fill(colours.sky)

        screen.blit(text_title,(80,50))

        screen.blit(start_button,(margin[0]+125,300))

        screen.blit(levelSelectButton,(margin[0],380))

        screen.blit(setings_Button,(margin[0],300))

        screen.blit(display_pingo,(500,300))

        random_positions=[player_sprite,player_right,player_right_walk,player_left,player_left_walk,player_fall,player_sprite_gold]
        for i in range(0,screenWidth,64):
            r = random.choice(random_positions)
            screen.blit(r,(i,screenHeight-64))

        if buttonCooldown == 0:
            if margin[0]+125 < mouse_pos[0] < (margin[0]+125)+start_button.get_width() and 300 < mouse_pos[1] < 300+start_button.get_height():
                screen.blit(start_pressed,(margin[0]+122,298))
                if mouse_press[0]:
                    menu = False

            if margin[0] < mouse_pos[0] < margin[0]+levelSelectButton.get_width() and 380 < mouse_pos[1] < 380+levelSelectButton.get_height():
                screen.blit(levelSelectButton_Pressed,(margin[0],380))
                if mouse_press[0]:
                    LevelSelect()
                    menu = False

            if margin[0] < mouse_pos[0] < margin[0]+setings_Button.get_width() and 300 < mouse_pos[1] < 300+setings_Button.get_width():
                screen.blit(settingsButton_Pressed,(margin[0],300))
                if mouse_press[0]:
                    menu = False
                    Settings()

            if 500 < mouse_pos[0] < display_pingo.get_width()+500 and 300 < mouse_pos[1] < display_pingo.get_height()+300:
                pygame.draw.rect(screen,colours.sky,pygame.Rect(500,300,128,128))
                screen.blit(pingos[current_pingo][8],(500,300))
                if mouse_press[0]:
                    menu = False
                    Wardrobe()


        if buttonCooldown != 0:
            buttonCooldown -= 1

        pygame.display.flip()
        clock.tick(10)

def LevelSelect():
    global levelID , buttonCooldown , isLevelChange
    level_one_text = smallText_font.render("Level: 1",True,colours.white)
    level_two_text = smallText_font.render("level: 2",True,colours.white)
    winStar_select = pygame.transform.scale(winStar,(32,32))
    winStar_select_empty = pygame.transform.scale(empty_winStar,(32,32))
    levelRun = True
    selectedLevel = levelID
    while levelRun:
        mouse_Pos = pygame.mouse.get_pos()
        mouse_Pressed = pygame.mouse.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                SaveGame()
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    levelRun = False
                    MainMenu()

        screen.blit(levelSelectBackground,(0,0))

        #code for level one button
        if selectedLevel == 0:
            screen.blit(levelButton_selected,(112,84))
        else:screen.blit(levelButton,(112,84))
        screen.blit(level_one_text,(108,159))
        for i in range(3):
            if levelStars[0] >= i+1:
                screen.blit(winStar_select,((i*32)+95,181))
            else:screen.blit(winStar_select_empty,((i*32)+95,181))
        
        #code for level two button
        if levelStars[0] == 3:
            if selectedLevel == 1:
                screen.blit(levelButton_selected,(304,180))
            else:screen.blit(levelButton,(304,180))
        else:screen.blit(levelButton_disabled,(304,180))
        screen.blit(level_two_text,(290,256))
        for i in range(3):
            if levelStars[1] >= i+1:
                screen.blit(winStar_select,((i*32)+283,280))
            else:screen.blit(winStar_select_empty,((i*32)+283,280))

        #code for level three button
        screen.blit(levelButton_disabled,(428,72))

        screen.blit(backButton,(10,screenHeight-backButton.get_height()-5))
        screen.blit(start_button,(650,screenHeight-backButton.get_height()-5))
        #button pressing logic

        if 112 < mouse_Pos[0] < 112+levelButton.get_width() and 84 < mouse_Pos[1] < 84+levelButton.get_height():
            if selectedLevel != 0:screen.blit(levelButton_pressed,(112,84))
            if mouse_Pressed[0]:
                selectedLevel = 0

        if 304 < mouse_Pos[0] < 304+levelButton.get_width() and 180 < mouse_Pos[1] < 180+levelButton.get_height():
            if levelStars[0] == 3:  
                if selectedLevel != 1:screen.blit(levelButton_pressed,(304,180))
                if mouse_Pressed[0]:
                    selectedLevel = 1
        
        #operating buttons pressing logic

        if (screenHeight-backButton.get_height()-5) < mouse_Pos[1] < screenHeight-5:
            if 10 < mouse_Pos[0] < 10+backButton.get_width():
                screen.blit(backButton_Pressed,(10,screenHeight-backButton.get_height()-5))
                if mouse_Pressed[0]:
                    levelRun = False
                    MainMenu()
            if 650 < mouse_Pos[0] <650+start_button.get_width():
                screen.blit(start_pressed,(648,screenHeight-backButton.get_height()-8))
                if mouse_Pressed[0]:
                    levelRun = False
                    isLevelChange = True
                    levelID = selectedLevel

        #mini debug for this screen
        debug_text = pixel_font.render(f"x:{mouse_Pos[0]} y:{mouse_Pos[1]}",True,colours.red)
        screen.blit(debug_text,(0,0))

        pygame.display.flip()
        clock.tick(120)

def Settings():
    global key_jump , key_left , key_right
    settingsRun = True
    changingKey = ''
    margin = [80,350] #This is a new system im testing from commit 13. all uniform items like menus will have a margin for base placment. making things easier to code
    title_text = subTitle_font.render("Settings",True,colours.black)
    jumpSetting_text = pixel_font.render("Jump Key:",True,colours.white)
    jumpCurrentKey_text = pixel_font.render(f"{pygame.key.name(key_jump)}",True,colours.white)
    leftSetting_text = pixel_font.render("Left Key:",True,colours.white)
    leftCurrentKey_text = pixel_font.render(f"{pygame.key.name(key_left)}",True,colours.white)
    rightSetting_text = pixel_font.render("Right Key:",True,colours.white)
    rightCurrentKey_text = pixel_font.render(f"{pygame.key.name(key_right)}",True,colours.white)

    while settingsRun:
        mouse_Pos = pygame.mouse.get_pos()
        mouse_Pressed = pygame.mouse.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                SaveGame()
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    SaveGame()
                    MainMenu()

            if changingKey != '':
                if event.type == pygame.KEYDOWN:
                    if changingKey == 'jump':
                        key_jump = event.key
                        jumpCurrentKey_text = pixel_font.render(f"{pygame.key.name(key_jump)}",True,colours.white)
                        changingKey = ''
                    if changingKey == 'left':
                        key_left = event.key
                        leftCurrentKey_text = pixel_font.render(f"{pygame.key.name(key_left)}",True,colours.white)
                        changingKey = ''
                    if changingKey == 'right':
                        key_right = event.key
                        rightCurrentKey_text = pixel_font.render(f"{pygame.key.name(key_right)}",True,colours.white)
                        changingKey = ''

        screen.fill(colours.sky)
        screen.blit(topBar,(0,0))
        screen.blit(title_text,(250,18))
        screen.blit(backButton,(10,10))

        #keybind changing setting
        screen.blit(jumpSetting_text,(margin[0],150))
        screen.blit(inputBackground,(margin[1],140))
        screen.blit(jumpCurrentKey_text,(margin[1]+20,150))

        screen.blit(leftSetting_text,(margin[0],220))
        screen.blit(inputBackground,(margin[1],210))
        screen.blit(leftCurrentKey_text,(margin[1]+20,220))

        screen.blit(rightSetting_text,(margin[0],290))
        screen.blit(inputBackground,(margin[1],280))
        screen.blit(rightCurrentKey_text,(margin[1]+20,290))


        if 10 < mouse_Pos[0] < 10+backButton.get_width() and 10 < mouse_Pos[1] < 10+backButton.get_height():
            screen.blit(backButton_Pressed,(10,10))
            if mouse_Pressed[0]:
                SaveGame()
                MainMenu()
                settingsRun = False

        if margin[1] < mouse_Pos[0] < margin[1]+inputBackground.get_width():
            if 140 < mouse_Pos[1] < 140+inputBackground.get_height():
                if mouse_Pressed[0]:
                    changingKey = 'jump' 
            if 210 < mouse_Pos[1] < 210+inputBackground.get_height():
                if mouse_Pressed[0]:
                    changingKey = 'left'
            if 280 < mouse_Pos[1] < 280+inputBackground.get_height():
                if mouse_Pressed[0]:
                    changingKey = 'right'           

        pygame.display.flip()
        clock.tick(120)

def Wardrobe():
    global current_pingo , current_flag , buttonCooldown , display_flag , flags_purchase , totalCoins
    runWardrobe = True
    pingoChange = False
    displayed_flag = current_flag
    buttonCooldown = buttonCooldownLength
    y_margin = [200,400]
    wardrobeHeader_text = subTitle_font.render("Wardrobe",True,colours.black)
    changePingo_text = pixel_font.render("Change Pingo",True,colours.white)
    changeFlag_text = pixel_font.render("Change Flag",True,colours.white)
    coins_text = pixel_font.render(f"x{totalCoins}",True,colours.black)
    cost_text = pixel_font.render(f"x{flags_purchase[displayed_flag][0]}",True,colours.black)
    display_pingo = pygame.transform.scale(pingos[current_pingo][0],(128,128))

    while runWardrobe:
        mouse_Pos = pygame.mouse.get_pos()
        mouse_Pressed = pygame.mouse.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                SaveGame()
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    SaveGame()
                    runWardrobe = False
                    MainMenu()

        screen.fill(colours.sky)
        screen.blit(topBar,(0,0))
        screen.blit(wardrobeHeader_text,(250,18))
        screen.blit(backButton,(10,10))
        screen.blit(coins_text,((screenWidth-coins_text.get_width())-15,25))
        screen.blit(coin_icon,((screenWidth-coins_text.get_width())-coin_icon.get_width()-15,33))

        #drawing for the pingo changer

        screen.blit(display_pingo,(350,y_margin[0]-50))
        screen.blit(changePingo_text,(270,y_margin[0]-80))

        if current_pingo != 0:
            screen.blit(leftButton,(200,y_margin[0]))
        else: screen.blit(leftButton_disabled,(200,y_margin[0]))

        if current_pingo != len(pingos)-1:
            screen.blit(rightButton,(550,y_margin[0]))
        else: screen.blit(rightButton_disabled,(550,y_margin[0]))

        #drawing for the flag changer
        screen.blit(changeFlag_text,(270,y_margin[1]-80))
        
        screen.blit(flags[displayed_flag][0],(350,y_margin[1]))
        
        if not flags_purchase[displayed_flag][1]:
            screen.blit(lockIcon,(370,y_margin[1]))
            screen.blit(buyButton,(320,y_margin[1]+80))
            screen.blit(cost_text,(410,y_margin[1]+90))

        else: current_flag = displayed_flag

        

        if displayed_flag != 0:
            screen.blit(leftButton,(200,y_margin[1]))
        else: screen.blit(leftButton_disabled,(200,y_margin[1]))
        if displayed_flag != len(flags)-1:  
            screen.blit(rightButton,(550,y_margin[1]))
        else: screen.blit(rightButton_disabled,(550,y_margin[1]))

        #for the back button
        if 10 < mouse_Pos[0] < backButton.get_width()+10 and 10 < mouse_Pos[1] < backButton.get_height()+10:
            screen.blit(backButton_Pressed,(10,10))
            if mouse_Pressed[0]:
                runWardrobe = False
                MainMenu()

        #
        #purchasing buttons
        #
        if not flags_purchase[displayed_flag][1]:
            if 320 < mouse_Pos[0] < 320+buyButton.get_width() and y_margin[1]+90 < mouse_Pos[1] < (y_margin[1]+90)+buyButton.get_height():
                if mouse_Pressed[0]:
                    if totalCoins >= flags_purchase[displayed_flag][0]:
                        flags_purchase[displayed_flag][1] = True
                        totalCoins -= flags_purchase[displayed_flag][0]
                        coins_text = pixel_font.render(f"x{totalCoins}",True,colours.black)

        #
        #for player atrobute changing
        #
        if buttonCooldown == 0:
            if 200 < mouse_Pos[0] < leftButton.get_width()+200:
                #left button for pingo changing
                if y_margin[0] < mouse_Pos[1] < leftButton.get_height()+y_margin[0]:
                    if current_pingo != 0:
                        screen.blit(leftButton_pressed,(200,y_margin[0]))
                        if mouse_Pressed[0]:
                            current_pingo -= 1
                            buttonCooldown = buttonCooldownLength
                            pingoChange = True
                #left button for flag changing
                if y_margin[1] < mouse_Pos[1] < leftButton.get_height()+y_margin[1]:
                    if displayed_flag != 0:
                        screen.blit(leftButton_pressed,(200,y_margin[1]))
                        if mouse_Pressed[0]:
                            displayed_flag -=1
                            cost_text = pixel_font.render(f"x{flags_purchase[displayed_flag][0]}",True,colours.black)
                            buttonCooldown = buttonCooldownLength
                    
            if 550 < mouse_Pos[0] < rightButton.get_width()+550:
                #right button for pingo changing
                if y_margin[0] < mouse_Pos[1] < rightButton.get_height()+y_margin[0]:
                    if current_pingo != len(pingos)-1:
                        screen.blit(rightButton_pressed,(550,y_margin[0]))
                        if mouse_Pressed[0]:
                            current_pingo+= 1
                            buttonCooldown = buttonCooldownLength
                            pingoChange = True
                #right button for flag changing
                if y_margin[1] < mouse_Pos[1] < rightButton.get_height()+y_margin[1]:
                    if displayed_flag != len(flags)-1:
                        screen.blit(rightButton_pressed,(550,y_margin[1]))
                        if mouse_Pressed[0]:
                            displayed_flag += 1
                            cost_text = pixel_font.render(f"x{flags_purchase[displayed_flag][0]}",True,colours.black)
                            buttonCooldown = buttonCooldownLength

        if pingoChange:
            display_pingo = pygame.transform.scale(pingos[current_pingo][0],(128,128))
            pingoChange = False
        
        if buttonCooldown > 0:
            buttonCooldown -= 1
        pygame.display.flip()
        clock.tick(60)

def Dead():
    global isLevelChange
    font = pygame.font.Font("fonts/buble.TTF",100)
    secondfont = pygame.font.Font(None,30)
    textSurface = font.render("You died!",True,colours.black)
    dead = True
    y_margin = [400]
    while dead:
        mouse_Pos = pygame.mouse.get_pos()
        mouse_Pressed = pygame.mouse.get_pressed()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                SaveGame()
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    dead = False
                    isLevelChange = True
                    MainMenu()
                    
                if event.key == pygame.K_RETURN:
                    dead = False
                    isLevelChange = True
                    MainMenu()

        screen.blit(deathBackground,(38,150))
        screen.blit(textSurface,((screenWidth//2)-textSurface.get_width()//2,(screenHeight//2)-textSurface.get_height()))
        screen.blit(mainMenuButton,(70,y_margin[0]))
        screen.blit(levelSelectButton,(460,y_margin[0]))
        screen.blit(restartButton,(359,y_margin[0]-1))

        if y_margin[0] < mouse_Pos[1] < y_margin[0]+mainMenuButton.get_height():
            if 70 < mouse_Pos[0] < 70+mainMenuButton.get_width():
                screen.blit(mainMenuButton_pressed,(70,y_margin[0]))
                if mouse_Pressed[0]:
                    dead = False
                    isLevelChange = True
                    MainMenu()
            if 460 < mouse_Pos[0] < 460+levelSelectButton.get_width():
                screen.blit(levelSelectButton_Pressed,(460,y_margin[0]))
                if mouse_Pressed[0]:
                    dead = False
                    isLevelChange =True
                    LevelSelect()
            if 359 < mouse_Pos[0] < 359+restartButton.get_width():
                screen.blit(restartButton_pressed,(359,y_margin[0]-1))
                if mouse_Pressed[0]:
                    dead = False
                    isLevelChange = True
        
        pygame.display.flip()
        clock.tick(60)

def WinCon():
    global winTimer , flag_y , flagTexture , score , totalScore , collected_coins , time , saving , totalCoins
    
    
    if winTimer == 0:
        winTimer = 30
        #calculate score from coins and time and resets them
        score = (500*collected_coins)-time//2
        if score < 0:
            score = 0
        totalScore += score
        totalCoins += collected_coins
        SaveGame()
        saving = 60

    #flag animation
    if winTimer % 10 == 0:
        if flagTexture == flags[current_flag][0]:
            flagTexture = flags[current_flag][1]
        else:
            flagTexture = flags[current_flag][0]
    if flag_y > 95:
        flag_y -= 2

    #draw flag
    screen.blit(flagTexture,(flag_x,flag_y))
    
    #condition for continuing the win time or closing it
    if winTimer == 1:
        if winContinue:
            winTimer = 0
            return True
        else:
            winTimer = 120
            return False
    else:
        winTimer -= 1
        return False

def WinUI():
    global winContinue ,winTimer , isLevelChange , levelID , saving , levelStars
    winTime_text = pixel_font.render(f"Time: {formatted_time}",True,colours.black)
    winCoins_text = pixel_font.render(f"Coins: {collected_coins}",True,colours.black)
    winScore_text = pixel_font.render(f"Score: {score}",True,colours.black)

    screen.blit(winBackground,(15,15))

    screen.blit(winTime_text,(25,30))
    screen.blit(winCoins_text,(25,70))

    if score > starPoints[levelID][0]:    
        screen.blit(winStar,(60,150))
        if levelStars[levelID] < 1:
            levelStars[levelID] = 1
    else: screen.blit(empty_winStar,(60,150))
    if score > starPoints[levelID][1]:
        screen.blit(winStar,(140,150))
        if levelStars[levelID] < 2:
            levelStars[levelID] = 2
    else: screen.blit(empty_winStar,(140,150))
    if score > starPoints[levelID][2]:
        screen.blit(winStar,(220,150))
        if levelStars[levelID] < 3:
            levelStars[levelID] = 3
    else: screen.blit(empty_winStar,(220,150))

    screen.blit(winScore_text,(25,220))

    screen.blit(continueButton,(75,420))

    screen.blit(levelSelectButton,(40,500))

    if saving != 0:
        screen.blit(saveIcon,((screenWidth-saveIcon.get_width())-20,(screenHeight-saveIcon.get_height())-20))
        saving -=1

    #checking for button presses
    if not winContinue:
        if 75 < mouse_Pos[0] < 75+continueButton.get_width() and 420 < mouse_Pos[1] < 420+continueButton.get_height():
            screen.blit(continueButton_Pressed,(75,420))
            if mouse_Pressed[0]:
                winContinue = True
                winTimer = 1
                exitGates[levelID][0] = currentExit_x
                levelID += 1

    if 40 < mouse_Pos[0] < 40+levelSelectButton.get_width() and 500 < mouse_Pos[1] < 500+levelSelectButton.get_height():
        screen.blit(levelSelectButton_Pressed,(40,500))
        if mouse_Pressed[0]:
            winTimer = 0
            isLevelChange = True
            exitGates[levelID][0] = currentExit_x
            LevelSelect()

def DeBugUI():
    debug_font = pygame.font.Font("fonts/upheavtt.ttf",25)

    player_coords_text = debug_font.render(f"player: x:{player_x}, y:{player_y}",True,colours.red)
    level_coords_text = debug_font.render(f"ground: x:{ground_x-player_x}",True,colours.red)
    levelID_text = debug_font.render(f"Level_ID: {levelID}",True,colours.red)
    levelStars_text = debug_font.render(f"Stars: {levelStars}",True,colours.red)
    totalCoins_text = debug_font.render(f"Total_Coins: {totalCoins}",True,colours.red)

    screen.blit(player_coords_text,(0,0))
    screen.blit(level_coords_text,(0,18))
    screen.blit(levelID_text,(0,36))
    screen.blit(levelStars_text,(0,54))
    screen.blit(totalCoins_text,(0,72))

def SaveGame():
    data = {
        "score":totalScore,
        "coins":totalCoins,
        "jump":key_jump,
        "left":key_left,
        "right":key_right,
        "save":renderDebug,
        "stars":levelStars,
        "pingo":current_pingo,
        "flag":current_flag,
        }

    with open ("user_data/settings.json", "w") as file:
        json.dump(data, file)

    with open ("user_data/purchases.json","w") as file:
        json.dump(flags_purchase,file)

def CloudGen():
    cloud = random.choice(clouds)
    x = random.randint(0,screenWidth)
    y = random.randint(0,200)
    speed = random.uniform(0.03,0.2)
    return cloud , x , y , speed

for i in range(amountOfClouds):
    tempcloud ,tempX , tempY , tempspeed = CloudGen()
    activeClouds.append([tempcloud,tempX,tempY,tempspeed])


##RUNS MAIN MENU FIRST 
MainMenu()
##

current_sprite = player_sprite
while running:
    mouse_Pos = pygame.mouse.get_pos()
    mouse_Pressed = pygame.mouse.get_pressed()


    if isLevelChange:
        player_x = 200
        player_y = 400
        ground_x = 0
        score = 0
        time = 0
        collected_coins = 0
        currentExit_x = exitGates[levelID][0]
        coins_editable = copy.deepcopy(coins)
        platforms_editable = copy.deepcopy(platforms)
        spikeBalls_editable = copy.deepcopy(spikeBalls)
        winContinue = False
        isLevelChange = False
    
    past_player_x = player_x
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            SaveGame()
            pygame.quit()
            sys.exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isLevelChange = True
                LevelSelect()
            if event.key == pygame.K_0:
                renderDebug = not renderDebug

            if event.key == pygame.K_9:
                SaveGame()

    #movement keys, these are smoother beacuse they dont rely on the small wait
    keys = pygame.key.get_pressed() 

    if winTimer == 0:
        #movment controller for jumping
        if keys[key_jump]:
            keybox = False
            if current_sprite != pingos[current_pingo][5]:
                current_sprite = pingos[current_pingo][5]
            if onGround:
                jump = 25

        #movment controller for moving left
        if keys[key_left]:
            keybox = False
            if current_sprite != pingos[current_pingo][5]:
                if movingleft == 0:
                    movingleft = 20
                if movingleft > 10:
                    current_sprite = pingos[current_pingo][2]
                if 0 < movingleft <= 10:
                    current_sprite = pingos[current_pingo][1]
                movingleft -=1
            if player_x == 200:
                if ground_x <= -velocity:
                    ground_x+=velocity

                    
                    for i in coins_editable:
                        if i[0] == levelID:
                            i[1] += velocity

                    for i in spikeBalls_editable:
                        if i[0] == levelID:
                            i[1] += velocity

                    for i in platforms_editable:
                        if i[0] == levelID:
                            i[1] += velocity

                    exitGates[levelID][0] +=velocity
            else:
                player_x -=velocity
            
            keyPressed = True

        #movemnet controller for moving right
        if keys[key_right]:
            keybox = False
            if current_sprite != pingos[current_pingo][5]:
                if movingright == 0:
                    movingright = 20
                if movingright > 10:
                    current_sprite = pingos[current_pingo][4]
                if 0 < movingright <= 10:
                    current_sprite = pingos[current_pingo][3]
                movingright-=1
        
            if ground_x > -currentExit_x+360:
                ground_x-=velocity

                for i in coins_editable:
                        if i[0] == levelID:
                            i[1] -= velocity

                for i in spikeBalls_editable:
                    if i[0] == levelID:
                        i[1] -= velocity

                for i in platforms_editable:
                    if i[0] == levelID:
                        i[1] -= velocity

                exitGates[levelID][0] -=velocity
            else:
                if player_x <= 370:
                    player_x+=velocity
                else:
                    WinCon()

    #Makes the background
    screen.blit(background,(0,0))
    screen.blit(panoramas[levelID],(ground_x//12,280))

    #
    #This will only show at the start
    if keybox:
        screen.blit(keybox,(250,450))
    #
    

    for i in activeClouds:
        screen.blit(i[0],(i[1],i[2]))
        i[1]+=i[3]

        if i[1] > screenWidth:
            i[1] = 0 - i[0].get_width()



    #objects drawn on screen
    if levelID == 0:
        screen.blit(sign,(ground_x+850,500))
        screen.blit(sign,(ground_x+1900,500))
        screen.blit(sign,(ground_x+3900,500))

    screen.blit(levels[levelID][0],(ground_x,0))
    
    screen.blit(current_sprite,(player_x,player_y))

    screen.blit(exit_gate,(exitGates[levelID][0],exitGates[levelID][1]))

    #handling the coin rendering and collision in one for loop to save performance
    for j , i in enumerate(coins_editable):
        if i[0] == levelID:
            screen.blit(coin,(i[1],i[2]))

            coinOffset = (player_x - i[1],player_y - i[2])
            coinCollision = coin_mask.overlap(player_mask,coinOffset)
            if coinCollision:
                collected_coins+=1
                del coins_editable[j]

    #
    #moving platform code
    #
    for i in platforms_editable:
        if i[0] == levelID:

            #platform movement
            if i[5] == 'pos':
                if ground_x+i[4] >= i[1]:
                    i[1] += platformSpeed
                else:i[5] = 'neg'
            if i[5] == 'neg':
                if ground_x+i[3] <= i[1]:
                    i[1] -= platformSpeed
                else:i[5] = 'pos'
            
            screen.blit(platform,(i[1],i[2]))

        platformOffset = (player_x-i[1],player_y-i[2])
        platformCollision = platform_mask.overlap(player_mask,platformOffset)
        if platformCollision:
            if player_y+current_sprite.get_height() != i[2]:
                player_y = i[2]-current_sprite.get_height()
                current_sprite = pingos[current_pingo][0]
                onGround = True
                platformCollided = True
                fall_speed = 1.8
    #
    #Enemy Code here
    #
    if spikeBallAnimation == 0:
        spikeBallAnimation = 60

    if spikeBallAnimation % 10 == 0:
        if spikeBallFrame == spikeBall:
            spikeBallFrame = spikeBall_one
        else:
            spikeBallFrame = spikeBall
    spikeBallAnimation -= 1


    for i in spikeBalls_editable:
        if i[0] == levelID:

            #This handles the movemnt of spike balls
            if i[5] == 'pos':
                if ground_x+i[4] >= i[1]:
                    i[1] += spikeBallSpeed
                else:
                    i[5] = 'neg'
            if i[5] == 'neg':
                if ground_x+i[3] <= i[1]:
                    i[1] -= spikeBallSpeed
                else:
                    i[5] = 'pos'

            screen.blit(spikeBallFrame,(i[1],i[2]))

            spikeBallOffset = (player_x - i[1],player_y - i[2])
            spikeBallCollision = spikeBall_mask.overlap(player_mask,spikeBallOffset)
            if spikeBallCollision:
                isLevelChange =True
                exitGates[levelID][0] = currentExit_x
                Dead()

            


    #
    #  UI rendering -- over all the other elements
    #
    if winTimer == 0:
        formatted_time = f"{(time//60) // 60:02}:{(time//60) % 60:02}"

        clock_text = pixel_font.render(f"{formatted_time}",True,colours.black)
        coin_text = pixel_font.render(f"x{collected_coins}",True,colours.black)


        screen.blit(clock_text,((screenWidth-clock_text.get_width())-20,0))
        screen.blit(clock_icon,((screenWidth-clock_text.get_width())-50,8))
        screen.blit(coin_icon,((screenWidth-clock_text.get_width())-145,8))
        screen.blit(coin_text,(((screenWidth-clock_text.get_width())-coin_text.get_width())-70,0))

    #
    #Collisions handling
    #
    if levelID == 0:
        signOffset_first = (player_x - (ground_x+850),player_y - 500)
        signcollision_first = sign_mask.overlap(player_mask,signOffset_first)
        if signcollision_first:
            screen.blit(messageBox,(50,50))
            screen.blit(signText_001,(70,80))
            screen.blit(signText_002,(70,120))

        signOffset_second = (player_x - (ground_x+1900),player_y - 500)
        signcollision_second = sign_mask.overlap(player_mask,signOffset_second)
        if signcollision_second:
            screen.blit(messageBox,(50,50))
            screen.blit(signText_003,(70,80))
            screen.blit(signText_004,(70,120))
        
        signOffset_second = (player_x - (ground_x+3900),player_y - 500)
        signcollision_second = sign_mask.overlap(player_mask,signOffset_second)
        if signcollision_second:
            screen.blit(messageBox,(50,50))
            screen.blit(signText_005,(70,80))
            screen.blit(signText_006,(70,120))


    offset = (player_x - ground_x, player_y - 0)
    collision = levels[levelID][1].overlap(player_mask, offset)
    
    if collision:
        if player_y != ((collision[1] - player_mask.get_size()[1]) + 1):
            current_sprite = pingos[current_pingo][5]
        else:
            current_sprite = pingos[current_pingo][0]

        player_y = (collision[1] - player_mask.get_size()[1]) + 1
        onGround = True
        fall_speed = 1.8
    else:
        if not platformCollided:
            onGround = False
    #
    #Player gravity and jumping handler
    #
    if player_y+64 >= screenHeight:
        isLevelChange = True
        exitGates[levelID][0] = currentExit_x
        Dead()

    if jump != 0:
        onGround = False
        player_y -= jump_speed

        jump_speed -= 0.8
        jump -=1
    else:
        jump_speed = 25
    
    if not onGround:
        player_y += fall_speed
        fall_speed +=0.7

    if winTimer != 0:
        isLevelChange = WinCon()
        if not winContinue:
            WinUI()
    
    if winTimer == 0:
        time+=1

    if not onGround and jump == 0:
        if fallAnimation ==0:
            fallAnimation = 10
        if fallAnimation > 5:
            current_sprite = pingos[current_pingo][6]
        if fallAnimation < 5:
            current_sprite = pingos[current_pingo][7]
        fallAnimation -= 1
    else:
        fallAnimation = 0

    platformCollided = False
    #renders the debug UI over anything while in game loop
    if renderDebug:
        DeBugUI()


    pygame.display.flip()
    clock.tick(60)

pygame.quit()