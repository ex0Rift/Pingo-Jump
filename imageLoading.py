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

#------ PLAYER
player_left = pygame.image.load("assets/player/default/facing_left.png")
player_left = pygame.transform.scale(player_left,(64,64))

player_left_walk = pygame.image.load("assets/player/default/facing_left_walk.png")
player_left_walk = pygame.transform.scale(player_left_walk,(64,64))

player_right = pygame.image.load("assets/player/default/facing_right.png")
player_right = pygame.transform.scale(player_right,(64,64))

player_right_walk = pygame.image.load("assets/player/default/facing_right_walk.png")
player_right_walk = pygame.transform.scale(player_right_walk,(64,64))

player_sprite = pygame.image.load("assets/player/default/sprite.png")
player_sprite = pygame.transform.scale(player_sprite,(64,64))

player_roll = pygame.image.load('assets/player/default/rolling.png')
player_roll = pygame.transform.scale(player_roll,(64,64))

player_sprite_gold = pygame.image.load("assets/player/gold/spriteGold.png")
player_sprite_gold = pygame.transform.scale(player_sprite_gold,(64,64))

player_left_gold = pygame.image.load("assets/player/gold/leftspriteGold.png")
player_left_gold = pygame.transform.scale(player_left_gold,(64,64))

player_left_walk_gold = pygame.image.load("assets/player/gold/facing_left_walkGold.png")
player_left_walk_gold = pygame.transform.scale(player_left_walk_gold,(64,64))

player_right_gold = pygame.image.load("assets/player/gold/rightspriteGold.png")
player_right_gold = pygame.transform.scale(player_right_gold,(64,64))

player_right_walk_gold = pygame.image.load("assets/player/gold/facing_right_walkGold.png")
player_right_walk_gold = pygame.transform.scale(player_right_walk_gold,(64,64))

player_roll_gold = pygame.image.load("assets/player/gold/ballSpriteGold.png")
player_roll_gold = pygame.transform.scale(player_roll_gold,(64,64))



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

spikeBall = pygame.image.load("assets/level_objects/spikeBall.png")
spikeBall = pygame.transform.scale(spikeBall,(64,64))

spikeBall_one = pygame.image.load("assets/level_objects/spikeBall_one.png")
spikeBall_one = pygame.transform.scale(spikeBall_one,(64,64))

#-----Flags
flag_default_one = pygame.image.load("assets/flags/flagOne.png")
flag_default_one = pygame.transform.scale(flag_default_one,(32*4,16*4))

flag_default_two = pygame.image.load("assets/flags/flagTwo.png")
flag_default_two = pygame.transform.scale(flag_default_two,(32*4,16*4))

flag_red_one = pygame.image.load("assets/flags/flagOne_red.png")
flag_red_one = pygame.transform.scale(flag_red_one,(32*4,16*4))

flag_red_two = pygame.image.load("assets/flags/flagTwo_red.png")
flag_red_two = pygame.transform.scale(flag_red_two,(32*4,16*4))

flag_blue_one = pygame.image.load("assets/flags/flagOne_blue.png")
flag_blue_one = pygame.transform.scale(flag_blue_one,(32*4,16*4))

flag_blue_two = pygame.image.load("assets/flags/flagTwo_blue.png")
flag_blue_two = pygame.transform.scale(flag_blue_two,(32*4,16*4))

flag_green_one = pygame.image.load("assets/flags/flagOne_green.png")
flag_green_one = pygame.transform.scale(flag_green_one,(32*4,16*4))

flag_green_two = pygame.image.load("assets/flags/flagTwo_green.png")
flag_green_two = pygame.transform.scale(flag_green_two,(32*4,16*4))


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

saveIcon = pygame.image.load("assets/UI/saveIcon.png")
saveIcon = pygame.transform.scale(saveIcon,(64,64))

lockIcon = pygame.image.load("assets/UI/lockIcon.png")
lockIcon = pygame.transform.scale(lockIcon,(64,64))

leftButton = pygame.image.load("assets/UI/leftButton.png")
leftButton = pygame.transform.scale(leftButton,(37*2,35*2))

leftButton_pressed = pygame.image.load("assets/UI/leftButtonPressed.png")
leftButton_pressed = pygame.transform.scale(leftButton_pressed,(37*2,35*2))

leftButton_disabled = pygame.image.load("assets/UI/leftButtonDisabled.png")
leftButton_disabled = pygame.transform.scale(leftButton_disabled,(37*2,35*2))

rightButton_disabled = pygame.image.load("assets/UI/rightButtonDisabled.png")
rightButton_disabled = pygame.transform.scale(rightButton_disabled,(37*2,35*2))

rightButton = pygame.image.load("assets/UI/rightButton.png")
rightButton = pygame.transform.scale(rightButton,(37*2,35*2))

rightButton_pressed = pygame.image.load("assets/UI/rightButtonPressed.png")
rightButton_pressed = pygame.transform.scale(rightButton_pressed,(37*2,35*2))

pingoDefaultUI = pygame.image.load("assets/UI/pingoDefaultUI.png")
pingoDefaultUI = pygame.transform.scale(pingoDefaultUI,(128,128))

pingoGoldUI = pygame.image.load("assets/UI/pingoGoldUI.png")
pingoGoldUI = pygame.transform.scale(pingoGoldUI,(128,128))

buyButton = pygame.image.load("assets/UI/buyButton.png")
buyButton = pygame.transform.scale(buyButton,(86*2,32*2))

#-----levels
firstLevel = pygame.image.load("assets/levels/firstlevel.png")
firstLevel = pygame.transform.scale(firstLevel,(5120,600))

secondLevel = pygame.image.load("assets/levels/secondLevel.png")
secondLevel = pygame.transform.scale(secondLevel,(5120,600))


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