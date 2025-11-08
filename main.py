import pygame , colours , random , sys , copy


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
keybox = True               #determins whether or not to show the keybind turotial
isLevelChange = True        #activates part to increment what level it is currently
levelID = 0                 #This is what level is currently in use 
amountOfLevels = 1          #amount of levels in game
collected_coins = 0         #how many coins the player has
winTimer = 0                #defines the variable for the length of the win timer
winContinue = False         #determins weather the next screen after winning is ready to be shown
score = 0                   #final score each level determined by the amount of coins / least amoun of time
totalScore = 0              #The total score across multiple levels
flag_x , flag_y = 610 , 210 #coordinates of the flag, starting pos as shown
flagTexture = ''            #define the variable for storing which state the flag is in
spikeBallAnimation = 0      #defines spikeball animation loop control
spikeBallFrame = ''         #defines which spikeball fram it is on
spikeBallSpeed = 11         #defines the speed of which the spikeballs will move
key_jump = pygame.K_UP      #keybind for the jump button
key_left = pygame.K_LEFT    #keybind for the walk left button
key_right = pygame.K_RIGHT  #keybind for the walk right button


#text for in game
pixel_font = pygame.font.Font("fonts/upheavtt.ttf",40)
header_font = pygame.font.Font("fonts/buble.TTF",80)
subTitle_font = pygame.font.Font("fonts/buble.TTF",50)
signText_001 = pixel_font.render("Walk up to the wall!",True,colours.black)
signText_002 = pixel_font.render("trust me it wont hurt.",True,colours.black)
signText_003 = pixel_font.render("See...you rolled up that wall ",True,colours.black)
signText_004 = pixel_font.render("like a boss!", True, colours.black)
signText_005 = pixel_font.render("Watch out for spike balls...",True,colours.black)
signText_006 = pixel_font.render("They hurt quite alot!",True,colours.black)


#loading sprites
player_left = pygame.image.load("facing_left.png")
player_left = pygame.transform.scale(player_left,(64,64))

player_left_walk = pygame.image.load("facing_left_walk.png")
player_left_walk = pygame.transform.scale(player_left_walk,(64,64))

player_right = pygame.image.load("facing_right.png")
player_right = pygame.transform.scale(player_right,(64,64))

player_right_walk = pygame.image.load("facing_right_walk.png")
player_right_walk = pygame.transform.scale(player_right_walk,(64,64))

player_sprite = pygame.image.load("sprite.png")
player_sprite = pygame.transform.scale(player_sprite,(64,64))

player_roll = pygame.image.load('rolling.png')
player_roll = pygame.transform.scale(player_roll,(64,64))

ground = pygame.image.load("place.png")
ground = pygame.transform.scale(ground,(16*80,screenHeight))

panorama = pygame.image.load("panorama.png")
panorama = pygame.transform.scale(panorama,(256*5,64*5))

background = pygame.image.load("background.png").convert()
background = pygame.transform.scale(background,(screenWidth,screenHeight))

exit_gate = pygame.image.load("exitGate.png")
exit_gate = pygame.transform.scale(exit_gate,(22*4,42*4))

sign = pygame.image.load("sign.png")
sign = pygame.transform.scale(sign,(64,64))

messageBox = pygame.image.load("messageBox.png")
messageBox = pygame.transform.scale(messageBox,(screenWidth-100,150))

keybox = pygame.image.load("keybox.png")
keybox = pygame.transform.scale(keybox,(128*3,32*3))

coin = pygame.image.load("coin.png")
coin = pygame.transform.scale(coin,(64,64))

flagOne = pygame.image.load("flagOne.png")
flagOne = pygame.transform.scale(flagOne,(32*4,16*4))

flagTwo = pygame.image.load("flagTwo.png")
flagTwo = pygame.transform.scale(flagTwo,(32*4,16*4))

spikeBall = pygame.image.load("spikeBall.png")
spikeBall = pygame.transform.scale(spikeBall,(64,64))

spikeBall_one = pygame.image.load("spikeBall_one.png")
spikeBall_one = pygame.transform.scale(spikeBall_one,(64,64))


#-----UI

clock_icon = pygame.image.load("UI/clock.png")
clock_icon = pygame.transform.scale(clock_icon,(24,24))

coin_icon = pygame.image.load("UI/coinUI.png")
coin_icon = pygame.transform.scale(coin_icon,(24,24))

start_button = pygame.image.load("UI/startButton.png")
start_button = pygame.transform.scale(start_button,(64*2,32*2))

start_pressed = pygame.image.load("UI/StartPressed.png")
start_pressed = pygame.transform.scale(start_pressed,(64*2.3,32*2.5))

winBackground = pygame.image.load("UI/winBackground.png")
winBackground = pygame.transform.scale(winBackground,(174*1.8,383*1.5))

winStar = pygame.image.load("UI/star.png")
winStar = pygame.transform.scale(winStar,(64,64))

empty_winStar = pygame.image.load("UI/emptyStar.png")
empty_winStar = pygame.transform.scale(empty_winStar,(64,64))

continueButton = pygame.image.load("UI/continueButton.png")
continueButton = pygame.transform.scale(continueButton,(96*2,32*2))

continueButton_Pressed = pygame.image.load("UI/continueButton_Pressed.png")
continueButton_Pressed = pygame.transform.scale(continueButton_Pressed,(96*2,32*2))

levelCard = pygame.image.load("UI/levelCard.png")
levelCard = pygame.transform.scale(levelCard,(screenWidth-50,25*6))

levelSelectButton = pygame.image.load("UI/levelSelectButton.png")
levelSelectButton = pygame.transform.scale(levelSelectButton,(133*2,32*2.2))

levelSelectButton_Pressed = pygame.image.load("UI/levelSelectButton_Pressed.png")
levelSelectButton_Pressed = pygame.transform.scale(levelSelectButton_Pressed,(133*2,32*2.2))

backButton = pygame.image.load("UI/backButton.png")
backButton = pygame.transform.scale(backButton,(67*2,35*2))

backButton_Pressed = pygame.image.load("UI/backButton_Pressed.png")
backButton_Pressed = pygame.transform.scale(backButton_Pressed,(67*2,35*2))

setings_Button = pygame.image.load("UI/settingsButton.png")
setings_Button = pygame.transform.scale(setings_Button,(37*2,35*2))

settingsButton_Pressed = pygame.image.load("UI/settingsButton_pressed.png")
settingsButton_Pressed = pygame.transform.scale(settingsButton_Pressed,(37*2,35*2))

inputBackground = pygame.image.load("UI/inputBackground.png")
inputBackground = pygame.transform.scale(inputBackground,(87*2,35*2))

topBar = pygame.image.load("UI/topBar.png")
topBar = pygame.transform.scale(topBar,(screenWidth,15*6))

#-----levels
firstLevel = pygame.image.load("levels/firstlevel.png")
firstLevel = pygame.transform.scale(firstLevel,(5120,600))


#-----clouds
cloudone = pygame.image.load("clouds/cloudone.png")
cloudone = pygame.transform.scale(cloudone,(64*3,32*3))

cloudtwo = pygame.image.load("clouds/cloudtwo.png")
cloudtwo = pygame.transform.scale(cloudtwo,(64*3,32*3))

cloudthree = pygame.image.load("clouds/cloudthree.png")
cloudthree = pygame.transform.scale(cloudthree,(64*3,32*3))

cloudfour = pygame.image.load("clouds/cloudfour.png")
cloudfour = pygame.transform.scale(cloudfour,(64*3,32*3))

cloudfive = pygame.image.load("clouds/cloudfive.png")
cloudfive = pygame.transform.scale(cloudfive,(64*3,32*3))

cloudsix = pygame.image.load("clouds/cloudsix.png")
cloudsix = pygame.transform.scale(cloudsix,(64*3,32*3))

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
    [0,ground_x+4300,115]

]

# first is the level its on , second is x coord , third is y coord ,foruth is x far left, fith is final x far right , sixth is movment direction('pos' positve 'neg' negative)
spikeBalls = [
    [0,ground_x+4000,508,4000,4500,'pos']
]


starPoints = [
    [500,2000,5000]
]

exitGates=[
    [ground_x+4672,395]
]

#generate masks
player_mask = pygame.mask.from_surface(player_sprite)
ground_mask = pygame.mask.from_surface(firstLevel)
sign_mask = pygame.mask.from_surface(sign)
coin_mask = pygame.mask.from_surface(coin)
spikeBall_mask = pygame.mask.from_surface(spikeBall)

#
#Different game screens here
#
def MainMenu():
    text_title = header_font.render("Pingo Jump", True, colours.white)

    menu = True
    while menu:
        mouse_pos = pygame.mouse.get_pos()
        mouse_press = pygame.mouse.get_pressed()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
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

        screen.blit(start_button,(390,300))

        screen.blit(levelSelectButton,(265,380))

        screen.blit(setings_Button,(265,300))

        random_positions=[player_sprite,player_right,player_right_walk,player_left,player_left_walk]
        for i in range(0,screenWidth,64):
            r = random.choice(random_positions)
            screen.blit(r,(i,screenHeight-64))

        if 390 < mouse_pos[0] < 390+start_button.get_width() and 300 < mouse_pos[1] < 300+start_button.get_height():
            screen.blit(start_pressed,(384,298))
            if mouse_press[0]:
                menu = False

        if 265 < mouse_pos[0] < 265+levelSelectButton.get_width() and 380 < mouse_pos[1] < 380+levelSelectButton.get_height():
            screen.blit(levelSelectButton_Pressed,(265,380))
            if mouse_press[0]:
                LevelSelect()
                menu = False

        if 265 < mouse_pos[0] < 265+setings_Button.get_width() and 300 < mouse_pos[1] < 300+setings_Button.get_width():
            screen.blit(settingsButton_Pressed,(265,300))
            if mouse_press[0]:
                menu = False
                Settings()



        pygame.display.flip()
        clock.tick(10)

def LevelSelect():
    global levelID
    levelRun = True
    card_font = pygame.font.Font("fonts/upheavtt.ttf",80)
    score_text = card_font.render(f"Score: {totalScore}",True,colours.black)
    while levelRun:
        mouse_Pos = pygame.mouse.get_pos()
        mouse_Pressed = pygame.mouse.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    levelRun = False
                    MainMenu()

        screen.fill(colours.sky)

        screen.blit(topBar,(0,0))

        screen.blit(backButton,(25,10))
        screen.blit(score_text,(screenWidth-score_text.get_width()-20,5))
        

        for i in range(0,amountOfLevels):
            level_text = card_font.render(f"Level {i}",True,colours.black)
            screen.blit(levelCard,(25,i*(levelCard.get_height()+25)+95))
            screen.blit(level_text,(60,(i*(levelCard.get_height()+25)+95)+40))

            if 25 < mouse_Pos[0] < 25+levelCard.get_width() and (i*(levelCard.get_height()+25)+95) < mouse_Pos[1] < (i*(levelCard.get_height()+25)+95)+levelCard.get_height():
                if mouse_Pressed[0]:
                    levelID = i
                    levelRun = False

        if 25 < mouse_Pos[0] < 25+backButton.get_width() and 10 < mouse_Pos[1] < 10+backButton.get_height():
                screen.blit(backButton_Pressed,(25,10))
                if mouse_Pressed[0]:
                    MainMenu()
                    levelRun = False



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
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
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

def Dead():
    font = pygame.font.Font("fonts/buble.TTF",100)
    secondfont = pygame.font.Font(None,30)
    textSurface = font.render("You died!",True,colours.white)
    quitText = secondfont.render("Quit",True,colours.black)
    dead = True
    while dead:
        mouse_Pos = pygame.mouse.get_pos()
        mouse_Pressed = pygame.mouse.get_pressed()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    dead = False
                    MainMenu()
                if event.key == pygame.K_RETURN:
                    dead = False
                    MainMenu()
        screen.fill(colours.black)

        screen.blit(textSurface,((screenWidth//2)-textSurface.get_width()//2,(screenHeight//2)-textSurface.get_height()))

        pygame.draw.rect(screen,colours.red,pygame.Rect((screenWidth//2)-80,(screenHeight//2)+100,100,50))

        screen.blit(quitText,((screenWidth//2)-50,(screenHeight//2)+115))

        if mouse_Pressed[0]:
            if (screenWidth//2)-80 < mouse_Pos[0] < (screenWidth//2)+20 and (screenHeight//2)+100 < mouse_Pos[1] < (screenHeight//2)+150:
                dead = False
                MainMenu()
                

        pygame.display.flip()
        clock.tick(60)

def WinCon():
    global winTimer , flag_y , flagTexture , score , totalScore , collected_coins , time
    
    
    if winTimer == 0:
        winTimer = 30
        #calculate score from coins and time and resets them
        score = (500*collected_coins)-time//2
        totalScore += score
        collected_coins = 0
        time = 0
        if score < 0:
            score = 0

    #flag animation
    if winTimer % 10 == 0:
        if flagTexture == flagOne:
            flagTexture = flagTwo
        else:
            flagTexture = flagOne
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
    global winContinue ,winTimer , isLevelChange , levelID
    winTime_text = pixel_font.render(f"Time: {formatted_time}",True,colours.black)
    winCoins_text = pixel_font.render(f"Coins: {collected_coins}",True,colours.black)
    winScore_text = pixel_font.render(f"Score: {score}",True,colours.black)

    screen.blit(winBackground,(15,15))

    screen.blit(winTime_text,(25,30))
    screen.blit(winCoins_text,(25,70))

    if score > starPoints[levelID][0]:    
        screen.blit(winStar,(60,150))
    else: screen.blit(empty_winStar,(60,150))
    if score > starPoints[levelID][1]:
        screen.blit(winStar,(140,150))
    else: screen.blit(empty_winStar,(140,150))
    if score > starPoints[levelID][2]:
        screen.blit(winStar,(220,150))
    else: screen.blit(empty_winStar,(220,150))

    screen.blit(winScore_text,(25,220))

    screen.blit(continueButton,(75,420))

    screen.blit(levelSelectButton,(40,500))

    #checking for button presses
    if 75 < mouse_Pos[0] < 75+continueButton.get_width() and 420 < mouse_Pos[1] < 420+continueButton.get_height():
        screen.blit(continueButton_Pressed,(75,420))
        if mouse_Pressed[0]:
            winContinue = True
            exitGates[levelID][0] = currentExit_x
            levelID += 1

    if 40 < mouse_Pos[0] < 40+levelSelectButton.get_width() and 500 < mouse_Pos[1] < 500+levelSelectButton.get_height():
        screen.blit(levelSelectButton_Pressed,(40,500))
        if mouse_Pressed[0]:
            winTimer = 0
            isLevelChange = True
            exitGates[levelID][0] = currentExit_x
            LevelSelect()

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
#Settings() #DEBUG PURPOSES------------------------------------------------------<<<<
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
        currentExit_x = exitGates[levelID][0]
        coins_editable = copy.deepcopy(coins)
        spikeBalls_editable = copy.deepcopy(spikeBalls)
        winContinue = False
        isLevelChange = False
    
    past_player_x = player_x
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                LevelSelect()

    #movement keys, these are smoother beacuse they dont rely on the small wait
    keys = pygame.key.get_pressed()
    if winTimer == 0:

        #movment controller for jumping
        if keys[key_jump]:
            keybox = False
            if current_sprite != player_roll:
                current_sprite = player_roll
            if onGround:
                jump = 25

        #movment controller for moving left
        if keys[key_left]:
            keybox = False
            if current_sprite != player_roll:
                if movingleft == 0:
                    movingleft = 20
                if movingleft > 10:
                    current_sprite = player_left_walk
                if 0 < movingleft <= 10:
                    current_sprite = player_left
                movingleft -=1
            if player_x == 200:
                if ground_x <= -10:
                    ground_x+=10

                    
                    for i in coins_editable:
                        if i[0] == levelID:
                            i[1] += 10

                    for i in spikeBalls_editable:
                        if i[0] == levelID:
                            i[1] += 10

                    exitGates[levelID][0] +=10
            else:
                player_x -=10

        #movemnet controller for moving right
        if keys[key_right]:
            keybox = False
            if current_sprite != player_roll:
                if movingright == 0:
                    movingright = 20
                if movingright > 10:
                    current_sprite = player_right_walk
                if 0 < movingright <= 10:
                    current_sprite = player_right
                movingright-=1
        
            if ground_x > -currentExit_x+360:
                ground_x-=10

                for i in coins_editable:
                        if i[0] == levelID:
                            i[1] -= 10

                for i in spikeBalls_editable:
                    if i[0] == levelID:
                        i[1] -= 10

                exitGates[levelID][0] -=10
            else:
                if player_x <= 370:
                    player_x+=10
                else:
                    WinCon()

    #Makes the background
    screen.blit(background,(0,0))
    screen.blit(panorama,(ground_x//12,280))

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

    screen.blit(sign,(ground_x+850,500))

    screen.blit(sign,(ground_x+1900,500))

    screen.blit(sign,(ground_x+3900,500))

    screen.blit(firstLevel,(ground_x,0))
    
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
    collision = ground_mask.overlap(player_mask, offset)
    
    if collision:
        if player_y != ((collision[1] - player_mask.get_size()[1]) + 1):
            current_sprite = player_roll
        else:
            current_sprite = player_sprite

        player_y = (collision[1] - player_mask.get_size()[1]) + 1
        onGround = True
        fall_speed = 1.8
    else:
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
        WinUI()
    
    if winTimer == 0:
        time+=1
    pygame.display.flip()
    clock.tick(60)

pygame.quit()