import pygame

#
#This file is for pingo jump
#it loads every image asset from here so the main file isnt so long and organised
#
#
#
#

screenWidth,screenHeight = 800 , 600

#loading sprites
player_left = pygame.image.load("assets/player/facing_left.png")
player_left = pygame.transform.scale(player_left,(64,64))

player_left_walk = pygame.image.load("assets/player/facing_left_walk.png")
player_left_walk = pygame.transform.scale(player_left_walk,(64,64))

player_right = pygame.image.load("assets/player/facing_right.png")
player_right = pygame.transform.scale(player_right,(64,64))

player_right_walk = pygame.image.load("assets/player/facing_right_walk.png")
player_right_walk = pygame.transform.scale(player_right_walk,(64,64))

player_sprite = pygame.image.load("assets/player/sprite.png")
player_sprite = pygame.transform.scale(player_sprite,(64,64))

player_roll = pygame.image.load('assets/player/rolling.png')
player_roll = pygame.transform.scale(player_roll,(64,64))

panorama = pygame.image.load("assets/background/panorama.png")
panorama = pygame.transform.scale(panorama,(256*5,64*5))

background = pygame.image.load("assets/background/background.png").convert()
background = pygame.transform.scale(background,(screenWidth,screenHeight))

exit_gate = pygame.image.load("assets/level_objects/exitGate.png")
exit_gate = pygame.transform.scale(exit_gate,(22*4,42*4))

sign = pygame.image.load("assets/level_objects/sign.png")
sign = pygame.transform.scale(sign,(64,64))

coin = pygame.image.load("assets/level_objects/coin.png")
coin = pygame.transform.scale(coin,(64,64))

flagOne = pygame.image.load("assets/flags/flagOne.png")
flagOne = pygame.transform.scale(flagOne,(32*4,16*4))

flagTwo = pygame.image.load("assets/flags/flagTwo.png")
flagTwo = pygame.transform.scale(flagTwo,(32*4,16*4))

spikeBall = pygame.image.load("assets/level_objects/spikeBall.png")
spikeBall = pygame.transform.scale(spikeBall,(64,64))

spikeBall_one = pygame.image.load("assets/level_objects/spikeBall_one.png")
spikeBall_one = pygame.transform.scale(spikeBall_one,(64,64))


#-----UI

keybox = pygame.image.load("assets/UI/keybox.png")
keybox = pygame.transform.scale(keybox,(128*3,32*3))

messageBox = pygame.image.load("assets/UI/messageBox.png")
messageBox = pygame.transform.scale(messageBox,(screenWidth-100,150))

clock_icon = pygame.image.load("assets/UI/clock.png")
clock_icon = pygame.transform.scale(clock_icon,(24,24))

coin_icon = pygame.image.load("assets/UI/coinUI.png")
coin_icon = pygame.transform.scale(coin_icon,(24,24))

start_button = pygame.image.load("assets/UI/startButton.png")
start_button = pygame.transform.scale(start_button,(64*2,32*2))

start_pressed = pygame.image.load("assets/UI/StartPressed.png")
start_pressed = pygame.transform.scale(start_pressed,(64*2.3,32*2.5))

winBackground = pygame.image.load("assets/UI/winBackground.png")
winBackground = pygame.transform.scale(winBackground,(174*1.8,383*1.5))

winStar = pygame.image.load("assets/UI/star.png")
winStar = pygame.transform.scale(winStar,(64,64))

empty_winStar = pygame.image.load("assets/UI/emptyStar.png")
empty_winStar = pygame.transform.scale(empty_winStar,(64,64))

continueButton = pygame.image.load("assets/UI/continueButton.png")
continueButton = pygame.transform.scale(continueButton,(96*2,32*2))

continueButton_Pressed = pygame.image.load("assets/UI/continueButton_Pressed.png")
continueButton_Pressed = pygame.transform.scale(continueButton_Pressed,(96*2,32*2))

levelCard = pygame.image.load("assets/UI/levelCard.png")
levelCard = pygame.transform.scale(levelCard,(screenWidth-50,25*6))

levelSelectButton = pygame.image.load("assets/UI/levelSelectButton.png")
levelSelectButton = pygame.transform.scale(levelSelectButton,(133*2,32*2.2))

levelSelectButton_Pressed = pygame.image.load("assets/UI/levelSelectButton_Pressed.png")
levelSelectButton_Pressed = pygame.transform.scale(levelSelectButton_Pressed,(133*2,32*2.2))

backButton = pygame.image.load("assets/UI/backButton.png")
backButton = pygame.transform.scale(backButton,(67*2,35*2))

backButton_Pressed = pygame.image.load("assets/UI/backButton_Pressed.png")
backButton_Pressed = pygame.transform.scale(backButton_Pressed,(67*2,35*2))

setings_Button = pygame.image.load("assets/UI/settingsButton.png")
setings_Button = pygame.transform.scale(setings_Button,(37*2,35*2))

settingsButton_Pressed = pygame.image.load("assets/UI/settingsButton_pressed.png")
settingsButton_Pressed = pygame.transform.scale(settingsButton_Pressed,(37*2,35*2))

inputBackground = pygame.image.load("assets/UI/inputBackground.png")
inputBackground = pygame.transform.scale(inputBackground,(87*2,35*2))

topBar = pygame.image.load("assets/UI/topBar.png")
topBar = pygame.transform.scale(topBar,(screenWidth,15*6))

#-----levels
firstLevel = pygame.image.load("assets/levels/firstlevel.png")
firstLevel = pygame.transform.scale(firstLevel,(5120,600))


#-----clouds
cloudone = pygame.image.load("assets/clouds/cloudone.png")
cloudone = pygame.transform.scale(cloudone,(64*3,32*3))

cloudtwo = pygame.image.load("assets/clouds/cloudtwo.png")
cloudtwo = pygame.transform.scale(cloudtwo,(64*3,32*3))

cloudthree = pygame.image.load("assets/clouds/cloudthree.png")
cloudthree = pygame.transform.scale(cloudthree,(64*3,32*3))

cloudfour = pygame.image.load("assets/clouds/cloudfour.png")
cloudfour = pygame.transform.scale(cloudfour,(64*3,32*3))

cloudfive = pygame.image.load("assets/clouds/cloudfive.png")
cloudfive = pygame.transform.scale(cloudfive,(64*3,32*3))

cloudsix = pygame.image.load("assets/clouds/cloudsix.png")
cloudsix = pygame.transform.scale(cloudsix,(64*3,32*3))