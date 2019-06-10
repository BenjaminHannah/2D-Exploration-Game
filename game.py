#4/6/2019
import pygame, os, sys, random
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()
pygame.init()
os.environ['SDL_VIDEO_WINDOW_POS'] = str(50) + "," + str(50)

screen = pygame.display.set_mode((1280,720),pygame.DOUBLEBUF) #Standard

#screen = pygame.display.set_mode((1780,920),pygame.DOUBLEBUF) #Tile_Map Editor
#screen2 = pygame.surface((1780,920),pygame.DOUBLEBUF)

font = pygame.font.SysFont('impact', 15)
clock = pygame.time.Clock()

gameState = 0

#Map Editor
selectedTile = 0
worldx = 32
worldy = 0

FloorLevel = 1

#
oneTime = True
darknessCounter = 0
##
slashSound = pygame.mixer.Sound('slash001.wav')

#Load Images#
heartImage = pygame.image.load('hudImages/heart.png').convert_alpha()

ItemPick = 0
ItemBoxSword = pygame.image.load('hudImages/ItemBoxSword.png').convert_alpha()
ItemBoxFishing = pygame.image.load('hudImages/ItemBoxFishing.png').convert_alpha()

darkness000 = pygame.image.load('darkness000.png').convert_alpha()
darkness001 = pygame.image.load('darkness001.png').convert_alpha()
darkness002 = pygame.image.load('darkness002.png').convert_alpha()

StartMenu = pygame.image.load('StartMenu.png').convert_alpha()

################################UNDERGROUND

tile_underground1_0 = pygame.image.load('tileImages/Tile (0).png').convert_alpha()
tile_underground1_1 = pygame.image.load('tileImages/Tile (1).png').convert_alpha()
tile_underground1_2 = pygame.image.load('tileImages/Tile (2).png').convert_alpha()
tile_underground1_3 = pygame.image.load('tileImages/Tile (3).png').convert_alpha()
tile_underground1_4 = pygame.image.load('tileImages/Tile (4).png').convert_alpha()
tile_underground1_5 = pygame.image.load('tileImages/Tile (5).png').convert_alpha()
tile_underground1_6 = pygame.image.load('tileImages/Tile (6).png').convert_alpha()
tile_underground1_7 = pygame.image.load('tileImages/Tile (7).png').convert_alpha()
tile_underground1_8 = pygame.image.load('tileImages/Tile (8).png').convert_alpha()
tile_underground1_9 = pygame.image.load('tileImages/Tile (9).png').convert_alpha()

tile_underground1_10 = pygame.image.load('tileImages/Tile (10).png').convert_alpha()
tile_underground1_11 = pygame.image.load('tileImages/Tile (11).png').convert_alpha()
tile_underground1_12 = pygame.image.load('tileImages/Tile (12).png').convert_alpha()
tile_underground1_13 = pygame.image.load('tileImages/Tile (13).png').convert_alpha()
tile_underground1_14 = pygame.image.load('tileImages/Tile (14).png').convert_alpha()
tile_underground1_15 = pygame.image.load('tileImages/Tile (15).png').convert_alpha()
tile_underground1_16 = pygame.image.load('tileImages/Tile (16).png').convert_alpha()
tile_underground1_17 = pygame.image.load('tileImages/Tile (17).png').convert_alpha()
tile_underground1_18 = pygame.image.load('tileImages/Tile (18).png').convert_alpha()
tile_underground1_19 = pygame.image.load('tileImages/Tile (19).png').convert_alpha()

tile_underground1_20 = pygame.image.load('tileImages/Tile (20).png').convert_alpha()
tile_underground1_21 = pygame.image.load('tileImages/Tile (21).png').convert_alpha()
tile_underground1_22 = pygame.image.load('tileImages/Tile (22).png').convert_alpha()
tile_underground1_23 = pygame.image.load('tileImages/Tile (23).png').convert_alpha()
tile_underground1_24 = pygame.image.load('tileImages/Tile (24).png').convert_alpha()
tile_underground1_25 = pygame.image.load('tileImages/Tile (25).png').convert_alpha()
tile_underground1_26 = pygame.image.load('tileImages/Tile (26).png').convert_alpha()
tile_underground1_27 = pygame.image.load('tileImages/Tile (27).png').convert_alpha()
tile_underground1_28 = pygame.image.load('tileImages/Tile (28).png').convert_alpha()
tile_underground1_29 = pygame.image.load('tileImages/Tile (29).png').convert_alpha()

tile_underground1_30 = pygame.image.load('tileImages/Tile (30).png').convert_alpha()
tile_underground1_31 = pygame.image.load('tileImages/Tile (31).png').convert_alpha()
tile_underground1_32 = pygame.image.load('tileImages/Tile (32).png').convert_alpha()
tile_underground1_33 = pygame.image.load('tileImages/Tile (33).png').convert_alpha()
tile_underground1_34 = pygame.image.load('tileImages/Tile (34).png').convert_alpha()
tile_underground1_35 = pygame.image.load('tileImages/Tile (35).png').convert_alpha()
tile_underground1_36 = pygame.image.load('tileImages/Tile (36).png').convert_alpha()
tile_underground1_37 = pygame.image.load('tileImages/Tile (37).png').convert_alpha()
tile_underground1_38 = pygame.image.load('tileImages/Tile (38).png').convert_alpha()
tile_underground1_39 = pygame.image.load('tileImages/Tile (39).png').convert_alpha()

tile_underground1_40 = pygame.image.load('tileImages/Tile (40).png').convert_alpha()
tile_underground1_41 = pygame.image.load('tileImages/Tile (41).png').convert_alpha()
tile_underground1_42 = pygame.image.load('tileImages/Tile (42).png').convert_alpha()
tile_underground1_43 = pygame.image.load('tileImages/Tile (43).png').convert_alpha()
tile_underground1_44 = pygame.image.load('tileImages/Tile (44).png').convert_alpha()
tile_underground1_45 = pygame.image.load('tileImages/Tile (45).png').convert_alpha()
tile_underground1_46 = pygame.image.load('tileImages/Tile (46).png').convert_alpha()
tile_underground1_47 = pygame.image.load('tileImages/Tile (47).png').convert_alpha()
tile_underground1_48 = pygame.image.load('tileImages/Tile (48).png').convert_alpha()
tile_underground1_49 = pygame.image.load('tileImages/Tile (49).png').convert_alpha()

tile_underground1_50 = pygame.image.load('tileImages/Tile (50).png').convert_alpha()
tile_underground1_51 = pygame.image.load('tileImages/Tile (51).png').convert_alpha()
tile_underground1_52 = pygame.image.load('tileImages/Tile (52).png').convert_alpha()
tile_underground1_53 = pygame.image.load('tileImages/Tile (53).png').convert_alpha()
tile_underground1_54 = pygame.image.load('tileImages/Tile (54).png').convert_alpha()
tile_underground1_55 = pygame.image.load('tileImages/Tile (55).png').convert_alpha()
tile_underground1_56 = pygame.image.load('tileImages/Tile (56).png').convert_alpha()
tile_underground1_57 = pygame.image.load('tileImages/Tile (57).png').convert_alpha()
tile_underground1_58 = pygame.image.load('tileImages/Tile (58).png').convert_alpha()
tile_underground1_59 = pygame.image.load('tileImages/Tile (59).png').convert_alpha()

tile_underground1_60 = pygame.image.load('tileImages/Tile (60).png').convert_alpha()
tile_underground1_61 = pygame.image.load('tileImages/Tile (61).png').convert_alpha()
tile_underground1_62 = pygame.image.load('tileImages/Tile (62).png').convert_alpha()
tile_underground1_63 = pygame.image.load('tileImages/Tile (63).png').convert_alpha()
tile_underground1_64 = pygame.image.load('tileImages/Tile (64).png').convert_alpha()
tile_underground1_65 = pygame.image.load('tileImages/Tile (65).png').convert_alpha()
tile_underground1_66 = pygame.image.load('tileImages/Tile (66).png').convert_alpha()
tile_underground1_67 = pygame.image.load('tileImages/Tile (67).png').convert_alpha()
tile_underground1_68 = pygame.image.load('tileImages/Tile (68).png').convert_alpha()
tile_underground1_69 = pygame.image.load('tileImages/Tile (69).png').convert_alpha()

tile_underground1_70 = pygame.image.load('tileImages/Tile (70).png').convert_alpha()
tile_underground1_71 = pygame.image.load('tileImages/Tile (71).png').convert_alpha()
tile_underground1_72 = pygame.image.load('tileImages/Tile (72).png').convert_alpha()
tile_underground1_73 = pygame.image.load('tileImages/Tile (73).png').convert_alpha()
tile_underground1_74 = pygame.image.load('tileImages/Tile (74).png').convert_alpha()
tile_underground1_75 = pygame.image.load('tileImages/Tile (75).png').convert_alpha()
tile_underground1_76 = pygame.image.load('tileImages/Tile (76).png').convert_alpha()
tile_underground1_77 = pygame.image.load('tileImages/Tile (77).png').convert_alpha()
tile_underground1_78 = pygame.image.load('tileImages/Tile (78).png').convert_alpha()
tile_underground1_79 = pygame.image.load('tileImages/Tile (79).png').convert_alpha()

tile_underground1_80 = pygame.image.load('tileImages/Tile (80).png').convert_alpha()
tile_underground1_81 = pygame.image.load('tileImages/Tile (81).png').convert_alpha()
tile_underground1_82 = pygame.image.load('tileImages/Tile (82).png').convert_alpha()
tile_underground1_83 = pygame.image.load('tileImages/Tile (83).png').convert_alpha()

tile_underground1_84 = pygame.image.load('tileImages/Tile (84).png').convert_alpha()#passage top
tile_underground1_85 = pygame.image.load('tileImages/Tile (85).png').convert_alpha()#passage
tile_underground1_86 = pygame.image.load('tileImages/Tile (86).png').convert_alpha()

tile_underground1_87 = pygame.image.load('tileImages/Tile (87).png').convert_alpha() #unique tile for underlay of transparent walls

################################OVERWORLD

tile_overworld1_1 = pygame.image.load('tileImages/GreenOverworld/Tile (1).png').convert_alpha()#tile_87
tile_overworld1_2 = pygame.image.load('tileImages/GreenOverworld/Tile (2).png').convert_alpha()
tile_overworld1_3 = pygame.image.load('tileImages/GreenOverworld/Tile (3).png').convert_alpha()
tile_overworld1_4 = pygame.image.load('tileImages/GreenOverworld/Tile (4).png').convert_alpha()
tile_overworld1_5 = pygame.image.load('tileImages/GreenOverworld/Tile (5).png').convert_alpha()#tile_91
tile_overworld1_6 = pygame.image.load('tileImages/GreenOverworld/Tile (6).png').convert_alpha()
tile_overworld1_7 = pygame.image.load('tileImages/GreenOverworld/Tile (7).png').convert_alpha()
tile_overworld1_8 = pygame.image.load('tileImages/GreenOverworld/Tile (8).png').convert_alpha()
tile_overworld1_9 = pygame.image.load('tileImages/GreenOverworld/Tile (9).png').convert_alpha()
tile_overworld1_10 = pygame.image.load('tileImages/GreenOverworld/Tile (10).png').convert_alpha()
tile_overworld1_11 = pygame.image.load('tileImages/GreenOverworld/Tile (11).png').convert_alpha()#tile_97

tile_overworld1_50 = pygame.image.load('tileImages/GreenOverworld/Tile (50).png').convert_alpha()
tile_overworld1_51 = pygame.image.load('tileImages/GreenOverworld/Tile (51).png').convert_alpha()
tile_overworld1_52 = pygame.image.load('tileImages/GreenOverworld/Tile (52).png').convert_alpha()#tile_100
tile_overworld1_53 = pygame.image.load('tileImages/GreenOverworld/Tile (53).png').convert_alpha()
tile_overworld1_54 = pygame.image.load('tileImages/GreenOverworld/Tile (54).png').convert_alpha()
tile_overworld1_55 = pygame.image.load('tileImages/GreenOverworld/Tile (55).png').convert_alpha()
tile_overworld1_56 = pygame.image.load('tileImages/GreenOverworld/Tile (56).png').convert_alpha()
tile_overworld1_57 = pygame.image.load('tileImages/GreenOverworld/Tile (57).png').convert_alpha()
tile_overworld1_58 = pygame.image.load('tileImages/GreenOverworld/Tile (58).png').convert_alpha()
tile_overworld1_59 = pygame.image.load('tileImages/GreenOverworld/Tile (59).png').convert_alpha()
tile_overworld1_60 = pygame.image.load('tileImages/GreenOverworld/Tile (60).png').convert_alpha()
tile_overworld1_61 = pygame.image.load('tileImages/GreenOverworld/Tile (61).png').convert_alpha()
tile_overworld1_62 = pygame.image.load('tileImages/GreenOverworld/Tile (62).png').convert_alpha()#tile_110
tile_overworld1_63 = pygame.image.load('tileImages/GreenOverworld/Tile (63).png').convert_alpha()
tile_overworld1_64 = pygame.image.load('tileImages/GreenOverworld/Tile (64).png').convert_alpha()
tile_overworld1_65 = pygame.image.load('tileImages/GreenOverworld/Tile (65).png').convert_alpha()
tile_overworld1_66 = pygame.image.load('tileImages/GreenOverworld/Tile (66).png').convert_alpha()
tile_overworld1_67 = pygame.image.load('tileImages/GreenOverworld/Tile (67).png').convert_alpha()
tile_overworld1_68 = pygame.image.load('tileImages/GreenOverworld/Tile (68).png').convert_alpha()
tile_overworld1_69 = pygame.image.load('tileImages/GreenOverworld/Tile (69).png').convert_alpha()
tile_overworld1_70 = pygame.image.load('tileImages/GreenOverworld/Tile (70).png').convert_alpha()
tile_overworld1_71 = pygame.image.load('tileImages/GreenOverworld/Tile (71).png').convert_alpha()
tile_overworld1_72 = pygame.image.load('tileImages/GreenOverworld/Tile (72).png').convert_alpha()#tile_120
tile_overworld1_73 = pygame.image.load('tileImages/GreenOverworld/Tile (73).png').convert_alpha()

################################PLAYER

#PLAYER

Player_Shadow_000 = pygame.image.load('playerImages/Player_Shadow_000.png').convert_alpha()

frontIdle_000 = pygame.image.load('playerImages/Front - Idle_000.png').convert_alpha()
frontIdle_001 = pygame.image.load('playerImages/Front - Idle_001.png').convert_alpha()
frontIdle_002 = pygame.image.load('playerImages/Front - Idle_002.png').convert_alpha()
frontIdle_003 = pygame.image.load('playerImages/Front - Idle_003.png').convert_alpha()
frontIdle_004 = pygame.image.load('playerImages/Front - Idle_004.png').convert_alpha()
frontIdle_005 = pygame.image.load('playerImages/Front - Idle_005.png').convert_alpha()
frontIdle_006 = pygame.image.load('playerImages/Front - Idle_006.png').convert_alpha()
frontIdle_007 = pygame.image.load('playerImages/Front - Idle_007.png').convert_alpha()
frontIdle_008 = pygame.image.load('playerImages/Front - Idle_008.png').convert_alpha()
frontIdle_009 = pygame.image.load('playerImages/Front - Idle_009.png').convert_alpha()
frontIdle_010 = pygame.image.load('playerImages/Front - Idle_010.png').convert_alpha()
frontIdle_011 = pygame.image.load('playerImages/Front - Idle_011.png').convert_alpha()
frontIdle_012 = pygame.image.load('playerImages/Front - Idle_012.png').convert_alpha()
frontIdle_013 = pygame.image.load('playerImages/Front - Idle_013.png').convert_alpha()
frontIdle_014 = pygame.image.load('playerImages/Front - Idle_014.png').convert_alpha()
frontIdle_015 = pygame.image.load('playerImages/Front - Idle_015.png').convert_alpha()
frontIdle_016 = pygame.image.load('playerImages/Front - Idle_016.png').convert_alpha()
frontIdle_017 = pygame.image.load('playerImages/Front - Idle_017.png').convert_alpha()

frontIdleBlinking_000 = pygame.image.load('playerImages/Front - Idle Blinking_000.png').convert_alpha()
frontIdleBlinking_001 = pygame.image.load('playerImages/Front - Idle Blinking_001.png').convert_alpha()
frontIdleBlinking_002 = pygame.image.load('playerImages/Front - Idle Blinking_002.png').convert_alpha()
frontIdleBlinking_003 = pygame.image.load('playerImages/Front - Idle Blinking_003.png').convert_alpha()
frontIdleBlinking_004 = pygame.image.load('playerImages/Front - Idle Blinking_004.png').convert_alpha()
frontIdleBlinking_005 = pygame.image.load('playerImages/Front - Idle Blinking_005.png').convert_alpha()
frontIdleBlinking_006 = pygame.image.load('playerImages/Front - Idle Blinking_006.png').convert_alpha()
frontIdleBlinking_007 = pygame.image.load('playerImages/Front - Idle Blinking_007.png').convert_alpha()
frontIdleBlinking_008 = pygame.image.load('playerImages/Front - Idle Blinking_008.png').convert_alpha()
frontIdleBlinking_009 = pygame.image.load('playerImages/Front - Idle Blinking_009.png').convert_alpha()
frontIdleBlinking_010 = pygame.image.load('playerImages/Front - Idle Blinking_010.png').convert_alpha()
frontIdleBlinking_011 = pygame.image.load('playerImages/Front - Idle Blinking_011.png').convert_alpha()
frontIdleBlinking_012 = pygame.image.load('playerImages/Front - Idle Blinking_012.png').convert_alpha()
frontIdleBlinking_013 = pygame.image.load('playerImages/Front - Idle Blinking_013.png').convert_alpha()
frontIdleBlinking_014 = pygame.image.load('playerImages/Front - Idle Blinking_014.png').convert_alpha()
frontIdleBlinking_015 = pygame.image.load('playerImages/Front - Idle Blinking_015.png').convert_alpha()
frontIdleBlinking_016 = pygame.image.load('playerImages/Front - Idle Blinking_016.png').convert_alpha()
frontIdleBlinking_017 = pygame.image.load('playerImages/Front - Idle Blinking_017.png').convert_alpha()

frontWalking_000 = pygame.image.load('playerImages/Front - Walking_000.png').convert_alpha()
frontWalking_001 = pygame.image.load('playerImages/Front - Walking_001.png').convert_alpha()
frontWalking_002 = pygame.image.load('playerImages/Front - Walking_002.png').convert_alpha()
frontWalking_003 = pygame.image.load('playerImages/Front - Walking_003.png').convert_alpha()
frontWalking_004 = pygame.image.load('playerImages/Front - Walking_004.png').convert_alpha()
frontWalking_005 = pygame.image.load('playerImages/Front - Walking_005.png').convert_alpha()
frontWalking_006 = pygame.image.load('playerImages/Front - Walking_006.png').convert_alpha()
frontWalking_007 = pygame.image.load('playerImages/Front - Walking_007.png').convert_alpha()
frontWalking_008 = pygame.image.load('playerImages/Front - Walking_008.png').convert_alpha()
frontWalking_009 = pygame.image.load('playerImages/Front - Walking_009.png').convert_alpha()
frontWalking_010 = pygame.image.load('playerImages/Front - Walking_010.png').convert_alpha()
frontWalking_011 = pygame.image.load('playerImages/Front - Walking_011.png').convert_alpha()
frontWalking_012 = pygame.image.load('playerImages/Front - Walking_012.png').convert_alpha()
frontWalking_013 = pygame.image.load('playerImages/Front - Walking_013.png').convert_alpha()
frontWalking_014 = pygame.image.load('playerImages/Front - Walking_014.png').convert_alpha()
frontWalking_015 = pygame.image.load('playerImages/Front - Walking_015.png').convert_alpha()
frontWalking_016 = pygame.image.load('playerImages/Front - Walking_016.png').convert_alpha()
frontWalking_017 = pygame.image.load('playerImages/Front - Walking_017.png').convert_alpha()

frontSlashing_000 = pygame.image.load('playerImages/Front - Slashing_000.png').convert_alpha()
frontSlashing_001 = pygame.image.load('playerImages/Front - Slashing_001.png').convert_alpha()
frontSlashing_002 = pygame.image.load('playerImages/Front - Slashing_002.png').convert_alpha()
frontSlashing_003 = pygame.image.load('playerImages/Front - Slashing_003.png').convert_alpha()
frontSlashing_004 = pygame.image.load('playerImages/Front - Slashing_004.png').convert_alpha()
frontSlashing_005 = pygame.image.load('playerImages/Front - Slashing_005.png').convert_alpha()
frontSlashing_006 = pygame.image.load('playerImages/Front - Slashing_006.png').convert_alpha()
frontSlashing_007 = pygame.image.load('playerImages/Front - Slashing_007.png').convert_alpha()
frontSlashing_008 = pygame.image.load('playerImages/Front - Slashing_008.png').convert_alpha()

rightIdle_000 = pygame.image.load('playerImages/Right - Idle_000.png').convert_alpha()
rightIdle_001 = pygame.image.load('playerImages/Right - Idle_001.png').convert_alpha()
rightIdle_002 = pygame.image.load('playerImages/Right - Idle_002.png').convert_alpha()
rightIdle_003 = pygame.image.load('playerImages/Right - Idle_003.png').convert_alpha()
rightIdle_004 = pygame.image.load('playerImages/Right - Idle_004.png').convert_alpha()
rightIdle_005 = pygame.image.load('playerImages/Right - Idle_005.png').convert_alpha()
rightIdle_006 = pygame.image.load('playerImages/Right - Idle_006.png').convert_alpha()
rightIdle_007 = pygame.image.load('playerImages/Right - Idle_007.png').convert_alpha()
rightIdle_008 = pygame.image.load('playerImages/Right - Idle_008.png').convert_alpha()
rightIdle_009 = pygame.image.load('playerImages/Right - Idle_009.png').convert_alpha()
rightIdle_010 = pygame.image.load('playerImages/Right - Idle_010.png').convert_alpha()
rightIdle_011 = pygame.image.load('playerImages/Right - Idle_011.png').convert_alpha()
rightIdle_012 = pygame.image.load('playerImages/Right - Idle_012.png').convert_alpha()
rightIdle_013 = pygame.image.load('playerImages/Right - Idle_013.png').convert_alpha()
rightIdle_014 = pygame.image.load('playerImages/Right - Idle_014.png').convert_alpha()
rightIdle_015 = pygame.image.load('playerImages/Right - Idle_015.png').convert_alpha()
rightIdle_016 = pygame.image.load('playerImages/Right - Idle_016.png').convert_alpha()
rightIdle_017 = pygame.image.load('playerImages/Right - Idle_017.png').convert_alpha()

rightIdleBlinking_000 = pygame.image.load('playerImages/Right - Idle Blinking_000.png').convert_alpha()
rightIdleBlinking_001 = pygame.image.load('playerImages/Right - Idle Blinking_001.png').convert_alpha()
rightIdleBlinking_002 = pygame.image.load('playerImages/Right - Idle Blinking_002.png').convert_alpha()
rightIdleBlinking_003 = pygame.image.load('playerImages/Right - Idle Blinking_003.png').convert_alpha()
rightIdleBlinking_004 = pygame.image.load('playerImages/Right - Idle Blinking_004.png').convert_alpha()
rightIdleBlinking_005 = pygame.image.load('playerImages/Right - Idle Blinking_005.png').convert_alpha()
rightIdleBlinking_006 = pygame.image.load('playerImages/Right - Idle Blinking_006.png').convert_alpha()
rightIdleBlinking_007 = pygame.image.load('playerImages/Right - Idle Blinking_007.png').convert_alpha()
rightIdleBlinking_008 = pygame.image.load('playerImages/Right - Idle Blinking_008.png').convert_alpha()
rightIdleBlinking_009 = pygame.image.load('playerImages/Right - Idle Blinking_009.png').convert_alpha()
rightIdleBlinking_010 = pygame.image.load('playerImages/Right - Idle Blinking_010.png').convert_alpha()
rightIdleBlinking_011 = pygame.image.load('playerImages/Right - Idle Blinking_011.png').convert_alpha()
rightIdleBlinking_012 = pygame.image.load('playerImages/Right - Idle Blinking_012.png').convert_alpha()
rightIdleBlinking_013 = pygame.image.load('playerImages/Right - Idle Blinking_013.png').convert_alpha()
rightIdleBlinking_014 = pygame.image.load('playerImages/Right - Idle Blinking_014.png').convert_alpha()
rightIdleBlinking_015 = pygame.image.load('playerImages/Right - Idle Blinking_015.png').convert_alpha()
rightIdleBlinking_016 = pygame.image.load('playerImages/Right - Idle Blinking_016.png').convert_alpha()
rightIdleBlinking_017 = pygame.image.load('playerImages/Right - Idle Blinking_017.png').convert_alpha()

rightWalking_000 = pygame.image.load('playerImages/Right - Walking_000.png').convert_alpha()
rightWalking_001 = pygame.image.load('playerImages/Right - Walking_001.png').convert_alpha()
rightWalking_002 = pygame.image.load('playerImages/Right - Walking_002.png').convert_alpha()
rightWalking_003 = pygame.image.load('playerImages/Right - Walking_003.png').convert_alpha()
rightWalking_004 = pygame.image.load('playerImages/Right - Walking_004.png').convert_alpha()
rightWalking_005 = pygame.image.load('playerImages/Right - Walking_005.png').convert_alpha()
rightWalking_006 = pygame.image.load('playerImages/Right - Walking_006.png').convert_alpha()
rightWalking_007 = pygame.image.load('playerImages/Right - Walking_007.png').convert_alpha()
rightWalking_008 = pygame.image.load('playerImages/Right - Walking_008.png').convert_alpha()
rightWalking_009 = pygame.image.load('playerImages/Right - Walking_009.png').convert_alpha()
rightWalking_010 = pygame.image.load('playerImages/Right - Walking_010.png').convert_alpha()
rightWalking_011 = pygame.image.load('playerImages/Right - Walking_011.png').convert_alpha()
rightWalking_012 = pygame.image.load('playerImages/Right - Walking_012.png').convert_alpha()
rightWalking_013 = pygame.image.load('playerImages/Right - Walking_013.png').convert_alpha()
rightWalking_014 = pygame.image.load('playerImages/Right - Walking_014.png').convert_alpha()
rightWalking_015 = pygame.image.load('playerImages/Right - Walking_015.png').convert_alpha()
rightWalking_016 = pygame.image.load('playerImages/Right - Walking_016.png').convert_alpha()
rightWalking_017 = pygame.image.load('playerImages/Right - Walking_017.png').convert_alpha()

rightSlashing_000 = pygame.image.load('playerImages/Right - Slashing_000.png').convert_alpha()
rightSlashing_001 = pygame.image.load('playerImages/Right - Slashing_001.png').convert_alpha()
rightSlashing_002 = pygame.image.load('playerImages/Right - Slashing_002.png').convert_alpha()
rightSlashing_003 = pygame.image.load('playerImages/Right - Slashing_003.png').convert_alpha()
rightSlashing_004 = pygame.image.load('playerImages/Right - Slashing_004.png').convert_alpha()
rightSlashing_005 = pygame.image.load('playerImages/Right - Slashing_005.png').convert_alpha()
rightSlashing_006 = pygame.image.load('playerImages/Right - Slashing_006.png').convert_alpha()
rightSlashing_007 = pygame.image.load('playerImages/Right - Slashing_007.png').convert_alpha()
rightSlashing_008 = pygame.image.load('playerImages/Right - Slashing_008.png').convert_alpha()

backIdle_000 = pygame.image.load('playerImages/Back - Idle_000.png').convert_alpha()
backIdle_001 = pygame.image.load('playerImages/Back - Idle_001.png').convert_alpha()
backIdle_002 = pygame.image.load('playerImages/Back - Idle_002.png').convert_alpha()
backIdle_003 = pygame.image.load('playerImages/Back - Idle_003.png').convert_alpha()
backIdle_004 = pygame.image.load('playerImages/Back - Idle_004.png').convert_alpha()
backIdle_005 = pygame.image.load('playerImages/Back - Idle_005.png').convert_alpha()
backIdle_006 = pygame.image.load('playerImages/Back - Idle_006.png').convert_alpha()
backIdle_007 = pygame.image.load('playerImages/Back - Idle_007.png').convert_alpha()
backIdle_008 = pygame.image.load('playerImages/Back - Idle_008.png').convert_alpha()
backIdle_009 = pygame.image.load('playerImages/Back - Idle_009.png').convert_alpha()
backIdle_010 = pygame.image.load('playerImages/Back - Idle_010.png').convert_alpha()
backIdle_011 = pygame.image.load('playerImages/Back - Idle_011.png').convert_alpha()
backIdle_012 = pygame.image.load('playerImages/Back - Idle_012.png').convert_alpha()
backIdle_013 = pygame.image.load('playerImages/Back - Idle_013.png').convert_alpha()
backIdle_014 = pygame.image.load('playerImages/Back - Idle_014.png').convert_alpha()
backIdle_015 = pygame.image.load('playerImages/Back - Idle_015.png').convert_alpha()
backIdle_016 = pygame.image.load('playerImages/Back - Idle_016.png').convert_alpha()
backIdle_017 = pygame.image.load('playerImages/Back - Idle_017.png').convert_alpha()

backWalking_000 = pygame.image.load('playerImages/Back - Walking_000.png').convert_alpha()
backWalking_001 = pygame.image.load('playerImages/Back - Walking_001.png').convert_alpha()
backWalking_002 = pygame.image.load('playerImages/Back - Walking_002.png').convert_alpha()
backWalking_003 = pygame.image.load('playerImages/Back - Walking_003.png').convert_alpha()
backWalking_004 = pygame.image.load('playerImages/Back - Walking_004.png').convert_alpha()
backWalking_005 = pygame.image.load('playerImages/Back - Walking_005.png').convert_alpha()
backWalking_006 = pygame.image.load('playerImages/Back - Walking_006.png').convert_alpha()
backWalking_007 = pygame.image.load('playerImages/Back - Walking_007.png').convert_alpha()
backWalking_008 = pygame.image.load('playerImages/Back - Walking_008.png').convert_alpha()
backWalking_009 = pygame.image.load('playerImages/Back - Walking_009.png').convert_alpha()
backWalking_010 = pygame.image.load('playerImages/Back - Walking_010.png').convert_alpha()
backWalking_011 = pygame.image.load('playerImages/Back - Walking_011.png').convert_alpha()
backWalking_012 = pygame.image.load('playerImages/Back - Walking_012.png').convert_alpha()
backWalking_013 = pygame.image.load('playerImages/Back - Walking_013.png').convert_alpha()
backWalking_014 = pygame.image.load('playerImages/Back - Walking_014.png').convert_alpha()
backWalking_015 = pygame.image.load('playerImages/Back - Walking_015.png').convert_alpha()
backWalking_016 = pygame.image.load('playerImages/Back - Walking_016.png').convert_alpha()
backWalking_017 = pygame.image.load('playerImages/Back - Walking_017.png').convert_alpha()

backSlashing_000 = pygame.image.load('playerImages/Back - Slashing_000.png').convert_alpha()
backSlashing_001 = pygame.image.load('playerImages/Back - Slashing_001.png').convert_alpha()
backSlashing_002 = pygame.image.load('playerImages/Back - Slashing_002.png').convert_alpha()
backSlashing_003 = pygame.image.load('playerImages/Back - Slashing_003.png').convert_alpha()
backSlashing_004 = pygame.image.load('playerImages/Back - Slashing_004.png').convert_alpha()
backSlashing_005 = pygame.image.load('playerImages/Back - Slashing_005.png').convert_alpha()
backSlashing_006 = pygame.image.load('playerImages/Back - Slashing_006.png').convert_alpha()
backSlashing_007 = pygame.image.load('playerImages/Back - Slashing_007.png').convert_alpha()
backSlashing_008 = pygame.image.load('playerImages/Back - Slashing_008.png').convert_alpha()

leftIdle_000 = pygame.image.load('playerImages/Left - Idle_000.png').convert_alpha()
leftIdle_001 = pygame.image.load('playerImages/Left - Idle_001.png').convert_alpha()
leftIdle_002 = pygame.image.load('playerImages/Left - Idle_002.png').convert_alpha()
leftIdle_003 = pygame.image.load('playerImages/Left - Idle_003.png').convert_alpha()
leftIdle_004 = pygame.image.load('playerImages/Left - Idle_004.png').convert_alpha()
leftIdle_005 = pygame.image.load('playerImages/Left - Idle_005.png').convert_alpha()
leftIdle_006 = pygame.image.load('playerImages/Left - Idle_006.png').convert_alpha()
leftIdle_007 = pygame.image.load('playerImages/Left - Idle_007.png').convert_alpha()
leftIdle_008 = pygame.image.load('playerImages/Left - Idle_008.png').convert_alpha()
leftIdle_009 = pygame.image.load('playerImages/Left - Idle_009.png').convert_alpha()
leftIdle_010 = pygame.image.load('playerImages/Left - Idle_010.png').convert_alpha()
leftIdle_011 = pygame.image.load('playerImages/Left - Idle_011.png').convert_alpha()
leftIdle_012 = pygame.image.load('playerImages/Left - Idle_012.png').convert_alpha()
leftIdle_013 = pygame.image.load('playerImages/Left - Idle_013.png').convert_alpha()
leftIdle_014 = pygame.image.load('playerImages/Left - Idle_014.png').convert_alpha()
leftIdle_015 = pygame.image.load('playerImages/Left - Idle_015.png').convert_alpha()
leftIdle_016 = pygame.image.load('playerImages/Left - Idle_016.png').convert_alpha()
leftIdle_017 = pygame.image.load('playerImages/Left - Idle_017.png').convert_alpha()

leftIdleBlinking_000 = pygame.image.load('playerImages/Left - Idle Blinking_000.png').convert_alpha()
leftIdleBlinking_001 = pygame.image.load('playerImages/Left - Idle Blinking_001.png').convert_alpha()
leftIdleBlinking_002 = pygame.image.load('playerImages/Left - Idle Blinking_002.png').convert_alpha()
leftIdleBlinking_003 = pygame.image.load('playerImages/Left - Idle Blinking_003.png').convert_alpha()
leftIdleBlinking_004 = pygame.image.load('playerImages/Left - Idle Blinking_004.png').convert_alpha()
leftIdleBlinking_005 = pygame.image.load('playerImages/Left - Idle Blinking_005.png').convert_alpha()
leftIdleBlinking_006 = pygame.image.load('playerImages/Left - Idle Blinking_006.png').convert_alpha()
leftIdleBlinking_007 = pygame.image.load('playerImages/Left - Idle Blinking_007.png').convert_alpha()
leftIdleBlinking_008 = pygame.image.load('playerImages/Left - Idle Blinking_008.png').convert_alpha()
leftIdleBlinking_009 = pygame.image.load('playerImages/Left - Idle Blinking_009.png').convert_alpha()
leftIdleBlinking_010 = pygame.image.load('playerImages/Left - Idle Blinking_010.png').convert_alpha()
leftIdleBlinking_011 = pygame.image.load('playerImages/Left - Idle Blinking_011.png').convert_alpha()
leftIdleBlinking_012 = pygame.image.load('playerImages/Left - Idle Blinking_012.png').convert_alpha()
leftIdleBlinking_013 = pygame.image.load('playerImages/Left - Idle Blinking_013.png').convert_alpha()
leftIdleBlinking_014 = pygame.image.load('playerImages/Left - Idle Blinking_014.png').convert_alpha()
leftIdleBlinking_015 = pygame.image.load('playerImages/Left - Idle Blinking_015.png').convert_alpha()
leftIdleBlinking_016 = pygame.image.load('playerImages/Left - Idle Blinking_016.png').convert_alpha()
leftIdleBlinking_017 = pygame.image.load('playerImages/Left - Idle Blinking_017.png').convert_alpha()

leftWalking_000 = pygame.image.load('playerImages/Left - Walking_000.png').convert_alpha()
leftWalking_001 = pygame.image.load('playerImages/Left - Walking_001.png').convert_alpha()
leftWalking_002 = pygame.image.load('playerImages/Left - Walking_002.png').convert_alpha()
leftWalking_003 = pygame.image.load('playerImages/Left - Walking_003.png').convert_alpha()
leftWalking_004 = pygame.image.load('playerImages/Left - Walking_004.png').convert_alpha()
leftWalking_005 = pygame.image.load('playerImages/Left - Walking_005.png').convert_alpha()
leftWalking_006 = pygame.image.load('playerImages/Left - Walking_006.png').convert_alpha()
leftWalking_007 = pygame.image.load('playerImages/Left - Walking_007.png').convert_alpha()
leftWalking_008 = pygame.image.load('playerImages/Left - Walking_008.png').convert_alpha()
leftWalking_009 = pygame.image.load('playerImages/Left - Walking_009.png').convert_alpha()
leftWalking_010 = pygame.image.load('playerImages/Left - Walking_010.png').convert_alpha()
leftWalking_011 = pygame.image.load('playerImages/Left - Walking_011.png').convert_alpha()
leftWalking_012 = pygame.image.load('playerImages/Left - Walking_012.png').convert_alpha()
leftWalking_013 = pygame.image.load('playerImages/Left - Walking_013.png').convert_alpha()
leftWalking_014 = pygame.image.load('playerImages/Left - Walking_014.png').convert_alpha()
leftWalking_015 = pygame.image.load('playerImages/Left - Walking_015.png').convert_alpha()
leftWalking_016 = pygame.image.load('playerImages/Left - Walking_016.png').convert_alpha()
leftWalking_017 = pygame.image.load('playerImages/Left - Walking_017.png').convert_alpha()

leftSlashing_000 = pygame.image.load('playerImages/Left - Slashing_000.png').convert_alpha()
leftSlashing_001 = pygame.image.load('playerImages/Left - Slashing_001.png').convert_alpha()
leftSlashing_002 = pygame.image.load('playerImages/Left - Slashing_002.png').convert_alpha()
leftSlashing_003 = pygame.image.load('playerImages/Left - Slashing_003.png').convert_alpha()
leftSlashing_004 = pygame.image.load('playerImages/Left - Slashing_004.png').convert_alpha()
leftSlashing_005 = pygame.image.load('playerImages/Left - Slashing_005.png').convert_alpha()
leftSlashing_006 = pygame.image.load('playerImages/Left - Slashing_006.png').convert_alpha()
leftSlashing_007 = pygame.image.load('playerImages/Left - Slashing_007.png').convert_alpha()
leftSlashing_008 = pygame.image.load('playerImages/Left - Slashing_008.png').convert_alpha()

frontFishing_000 = pygame.image.load('playerImages/Front - Fishing_000.png').convert_alpha()
fishingLine_000 = pygame.image.load('hudImages/fishingLine_000.png').convert_alpha()
##########################################################################################

SfrontIdle_000 = pygame.image.load('playerImages2/Front - Idle_000.png').convert_alpha()
SfrontIdle_001 = pygame.image.load('playerImages2/Front - Idle_001.png').convert_alpha()
SfrontIdle_002 = pygame.image.load('playerImages2/Front - Idle_002.png').convert_alpha()
SfrontIdle_003 = pygame.image.load('playerImages2/Front - Idle_003.png').convert_alpha()
SfrontIdle_004 = pygame.image.load('playerImages2/Front - Idle_004.png').convert_alpha()
SfrontIdle_005 = pygame.image.load('playerImages2/Front - Idle_005.png').convert_alpha()
SfrontIdle_006 = pygame.image.load('playerImages2/Front - Idle_006.png').convert_alpha()
SfrontIdle_007 = pygame.image.load('playerImages2/Front - Idle_007.png').convert_alpha()
SfrontIdle_008 = pygame.image.load('playerImages2/Front - Idle_008.png').convert_alpha()
SfrontIdle_009 = pygame.image.load('playerImages2/Front - Idle_009.png').convert_alpha()
SfrontIdle_010 = pygame.image.load('playerImages2/Front - Idle_010.png').convert_alpha()
SfrontIdle_011 = pygame.image.load('playerImages2/Front - Idle_011.png').convert_alpha()
SfrontIdle_012 = pygame.image.load('playerImages2/Front - Idle_012.png').convert_alpha()
SfrontIdle_013 = pygame.image.load('playerImages2/Front - Idle_013.png').convert_alpha()
SfrontIdle_014 = pygame.image.load('playerImages2/Front - Idle_014.png').convert_alpha()
SfrontIdle_015 = pygame.image.load('playerImages2/Front - Idle_015.png').convert_alpha()
SfrontIdle_016 = pygame.image.load('playerImages2/Front - Idle_016.png').convert_alpha()
SfrontIdle_017 = pygame.image.load('playerImages2/Front - Idle_017.png').convert_alpha()

SfrontIdleBlinking_000 = pygame.image.load('playerImages2/Front - Idle Blinking_000.png').convert_alpha()
SfrontIdleBlinking_001 = pygame.image.load('playerImages2/Front - Idle Blinking_001.png').convert_alpha()
SfrontIdleBlinking_002 = pygame.image.load('playerImages2/Front - Idle Blinking_002.png').convert_alpha()
SfrontIdleBlinking_003 = pygame.image.load('playerImages2/Front - Idle Blinking_003.png').convert_alpha()
SfrontIdleBlinking_004 = pygame.image.load('playerImages2/Front - Idle Blinking_004.png').convert_alpha()
SfrontIdleBlinking_005 = pygame.image.load('playerImages2/Front - Idle Blinking_005.png').convert_alpha()
SfrontIdleBlinking_006 = pygame.image.load('playerImages2/Front - Idle Blinking_006.png').convert_alpha()
SfrontIdleBlinking_007 = pygame.image.load('playerImages2/Front - Idle Blinking_007.png').convert_alpha()
SfrontIdleBlinking_008 = pygame.image.load('playerImages2/Front - Idle Blinking_008.png').convert_alpha()
SfrontIdleBlinking_009 = pygame.image.load('playerImages2/Front - Idle Blinking_009.png').convert_alpha()
SfrontIdleBlinking_010 = pygame.image.load('playerImages2/Front - Idle Blinking_010.png').convert_alpha()
SfrontIdleBlinking_011 = pygame.image.load('playerImages2/Front - Idle Blinking_011.png').convert_alpha()
SfrontIdleBlinking_012 = pygame.image.load('playerImages2/Front - Idle Blinking_012.png').convert_alpha()
SfrontIdleBlinking_013 = pygame.image.load('playerImages2/Front - Idle Blinking_013.png').convert_alpha()
SfrontIdleBlinking_014 = pygame.image.load('playerImages2/Front - Idle Blinking_014.png').convert_alpha()
SfrontIdleBlinking_015 = pygame.image.load('playerImages2/Front - Idle Blinking_015.png').convert_alpha()
SfrontIdleBlinking_016 = pygame.image.load('playerImages2/Front - Idle Blinking_016.png').convert_alpha()
SfrontIdleBlinking_017 = pygame.image.load('playerImages2/Front - Idle Blinking_017.png').convert_alpha()

SfrontWalking_000 = pygame.image.load('playerImages2/Front - Walking_000.png').convert_alpha()
SfrontWalking_001 = pygame.image.load('playerImages2/Front - Walking_001.png').convert_alpha()
SfrontWalking_002 = pygame.image.load('playerImages2/Front - Walking_002.png').convert_alpha()
SfrontWalking_003 = pygame.image.load('playerImages2/Front - Walking_003.png').convert_alpha()
SfrontWalking_004 = pygame.image.load('playerImages2/Front - Walking_004.png').convert_alpha()
SfrontWalking_005 = pygame.image.load('playerImages2/Front - Walking_005.png').convert_alpha()
SfrontWalking_006 = pygame.image.load('playerImages2/Front - Walking_006.png').convert_alpha()
SfrontWalking_007 = pygame.image.load('playerImages2/Front - Walking_007.png').convert_alpha()
SfrontWalking_008 = pygame.image.load('playerImages2/Front - Walking_008.png').convert_alpha()
SfrontWalking_009 = pygame.image.load('playerImages2/Front - Walking_009.png').convert_alpha()
SfrontWalking_010 = pygame.image.load('playerImages2/Front - Walking_010.png').convert_alpha()
SfrontWalking_011 = pygame.image.load('playerImages2/Front - Walking_011.png').convert_alpha()
SfrontWalking_012 = pygame.image.load('playerImages2/Front - Walking_012.png').convert_alpha()
SfrontWalking_013 = pygame.image.load('playerImages2/Front - Walking_013.png').convert_alpha()
SfrontWalking_014 = pygame.image.load('playerImages2/Front - Walking_014.png').convert_alpha()
SfrontWalking_015 = pygame.image.load('playerImages2/Front - Walking_015.png').convert_alpha()
SfrontWalking_016 = pygame.image.load('playerImages2/Front - Walking_016.png').convert_alpha()
SfrontWalking_017 = pygame.image.load('playerImages2/Front - Walking_017.png').convert_alpha()

SfrontSlashing_000 = pygame.image.load('playerImages2/Front - Slashing_000.png').convert_alpha()
SfrontSlashing_001 = pygame.image.load('playerImages2/Front - Slashing_001.png').convert_alpha()
SfrontSlashing_002 = pygame.image.load('playerImages2/Front - Slashing_002.png').convert_alpha()
SfrontSlashing_003 = pygame.image.load('playerImages2/Front - Slashing_003.png').convert_alpha()
SfrontSlashing_004 = pygame.image.load('playerImages2/Front - Slashing_004.png').convert_alpha()
SfrontSlashing_005 = pygame.image.load('playerImages2/Front - Slashing_005.png').convert_alpha()
SfrontSlashing_006 = pygame.image.load('playerImages2/Front - Slashing_006.png').convert_alpha()
SfrontSlashing_007 = pygame.image.load('playerImages2/Front - Slashing_007.png').convert_alpha()
SfrontSlashing_008 = pygame.image.load('playerImages2/Front - Slashing_008.png').convert_alpha()

SrightIdle_000 = pygame.image.load('playerImages2/Right - Idle_000.png').convert_alpha()
SrightIdle_001 = pygame.image.load('playerImages2/Right - Idle_001.png').convert_alpha()
SrightIdle_002 = pygame.image.load('playerImages2/Right - Idle_002.png').convert_alpha()
SrightIdle_003 = pygame.image.load('playerImages2/Right - Idle_003.png').convert_alpha()
SrightIdle_004 = pygame.image.load('playerImages2/Right - Idle_004.png').convert_alpha()
SrightIdle_005 = pygame.image.load('playerImages2/Right - Idle_005.png').convert_alpha()
SrightIdle_006 = pygame.image.load('playerImages2/Right - Idle_006.png').convert_alpha()
SrightIdle_007 = pygame.image.load('playerImages2/Right - Idle_007.png').convert_alpha()
SrightIdle_008 = pygame.image.load('playerImages2/Right - Idle_008.png').convert_alpha()
SrightIdle_009 = pygame.image.load('playerImages2/Right - Idle_009.png').convert_alpha()
SrightIdle_010 = pygame.image.load('playerImages2/Right - Idle_010.png').convert_alpha()
SrightIdle_011 = pygame.image.load('playerImages2/Right - Idle_011.png').convert_alpha()
SrightIdle_012 = pygame.image.load('playerImages2/Right - Idle_012.png').convert_alpha()
SrightIdle_013 = pygame.image.load('playerImages2/Right - Idle_013.png').convert_alpha()
SrightIdle_014 = pygame.image.load('playerImages2/Right - Idle_014.png').convert_alpha()
SrightIdle_015 = pygame.image.load('playerImages2/Right - Idle_015.png').convert_alpha()
SrightIdle_016 = pygame.image.load('playerImages2/Right - Idle_016.png').convert_alpha()
SrightIdle_017 = pygame.image.load('playerImages2/Right - Idle_017.png').convert_alpha()

SrightIdleBlinking_000 = pygame.image.load('playerImages2/Right - Idle Blinking_000.png').convert_alpha()
SrightIdleBlinking_001 = pygame.image.load('playerImages2/Right - Idle Blinking_001.png').convert_alpha()
SrightIdleBlinking_002 = pygame.image.load('playerImages2/Right - Idle Blinking_002.png').convert_alpha()
SrightIdleBlinking_003 = pygame.image.load('playerImages2/Right - Idle Blinking_003.png').convert_alpha()
SrightIdleBlinking_004 = pygame.image.load('playerImages2/Right - Idle Blinking_004.png').convert_alpha()
SrightIdleBlinking_005 = pygame.image.load('playerImages2/Right - Idle Blinking_005.png').convert_alpha()
SrightIdleBlinking_006 = pygame.image.load('playerImages2/Right - Idle Blinking_006.png').convert_alpha()
SrightIdleBlinking_007 = pygame.image.load('playerImages2/Right - Idle Blinking_007.png').convert_alpha()
SrightIdleBlinking_008 = pygame.image.load('playerImages2/Right - Idle Blinking_008.png').convert_alpha()
SrightIdleBlinking_009 = pygame.image.load('playerImages2/Right - Idle Blinking_009.png').convert_alpha()
SrightIdleBlinking_010 = pygame.image.load('playerImages2/Right - Idle Blinking_010.png').convert_alpha()
SrightIdleBlinking_011 = pygame.image.load('playerImages2/Right - Idle Blinking_011.png').convert_alpha()
SrightIdleBlinking_012 = pygame.image.load('playerImages2/Right - Idle Blinking_012.png').convert_alpha()
SrightIdleBlinking_013 = pygame.image.load('playerImages2/Right - Idle Blinking_013.png').convert_alpha()
SrightIdleBlinking_014 = pygame.image.load('playerImages2/Right - Idle Blinking_014.png').convert_alpha()
SrightIdleBlinking_015 = pygame.image.load('playerImages2/Right - Idle Blinking_015.png').convert_alpha()
SrightIdleBlinking_016 = pygame.image.load('playerImages2/Right - Idle Blinking_016.png').convert_alpha()
SrightIdleBlinking_017 = pygame.image.load('playerImages2/Right - Idle Blinking_017.png').convert_alpha()

SrightWalking_000 = pygame.image.load('playerImages2/Right - Walking_000.png').convert_alpha()
SrightWalking_001 = pygame.image.load('playerImages2/Right - Walking_001.png').convert_alpha()
SrightWalking_002 = pygame.image.load('playerImages2/Right - Walking_002.png').convert_alpha()
SrightWalking_003 = pygame.image.load('playerImages2/Right - Walking_003.png').convert_alpha()
SrightWalking_004 = pygame.image.load('playerImages2/Right - Walking_004.png').convert_alpha()
SrightWalking_005 = pygame.image.load('playerImages2/Right - Walking_005.png').convert_alpha()
SrightWalking_006 = pygame.image.load('playerImages2/Right - Walking_006.png').convert_alpha()
SrightWalking_007 = pygame.image.load('playerImages2/Right - Walking_007.png').convert_alpha()
SrightWalking_008 = pygame.image.load('playerImages2/Right - Walking_008.png').convert_alpha()
SrightWalking_009 = pygame.image.load('playerImages2/Right - Walking_009.png').convert_alpha()
SrightWalking_010 = pygame.image.load('playerImages2/Right - Walking_010.png').convert_alpha()
SrightWalking_011 = pygame.image.load('playerImages2/Right - Walking_011.png').convert_alpha()
SrightWalking_012 = pygame.image.load('playerImages2/Right - Walking_012.png').convert_alpha()
SrightWalking_013 = pygame.image.load('playerImages2/Right - Walking_013.png').convert_alpha()
SrightWalking_014 = pygame.image.load('playerImages2/Right - Walking_014.png').convert_alpha()
SrightWalking_015 = pygame.image.load('playerImages2/Right - Walking_015.png').convert_alpha()
SrightWalking_016 = pygame.image.load('playerImages2/Right - Walking_016.png').convert_alpha()
SrightWalking_017 = pygame.image.load('playerImages2/Right - Walking_017.png').convert_alpha()

SrightSlashing_000 = pygame.image.load('playerImages2/Right - Slashing_000.png').convert_alpha()
SrightSlashing_001 = pygame.image.load('playerImages2/Right - Slashing_001.png').convert_alpha()
SrightSlashing_002 = pygame.image.load('playerImages2/Right - Slashing_002.png').convert_alpha()
SrightSlashing_003 = pygame.image.load('playerImages2/Right - Slashing_003.png').convert_alpha()
SrightSlashing_004 = pygame.image.load('playerImages2/Right - Slashing_004.png').convert_alpha()
SrightSlashing_005 = pygame.image.load('playerImages2/Right - Slashing_005.png').convert_alpha()
SrightSlashing_006 = pygame.image.load('playerImages2/Right - Slashing_006.png').convert_alpha()
SrightSlashing_007 = pygame.image.load('playerImages2/Right - Slashing_007.png').convert_alpha()
SrightSlashing_008 = pygame.image.load('playerImages2/Right - Slashing_008.png').convert_alpha()

SbackIdle_000 = pygame.image.load('playerImages2/Back - Idle_000.png').convert_alpha()
SbackIdle_001 = pygame.image.load('playerImages2/Back - Idle_001.png').convert_alpha()
SbackIdle_002 = pygame.image.load('playerImages2/Back - Idle_002.png').convert_alpha()
SbackIdle_003 = pygame.image.load('playerImages2/Back - Idle_003.png').convert_alpha()
SbackIdle_004 = pygame.image.load('playerImages2/Back - Idle_004.png').convert_alpha()
SbackIdle_005 = pygame.image.load('playerImages2/Back - Idle_005.png').convert_alpha()
SbackIdle_006 = pygame.image.load('playerImages2/Back - Idle_006.png').convert_alpha()
SbackIdle_007 = pygame.image.load('playerImages2/Back - Idle_007.png').convert_alpha()
SbackIdle_008 = pygame.image.load('playerImages2/Back - Idle_008.png').convert_alpha()
SbackIdle_009 = pygame.image.load('playerImages2/Back - Idle_009.png').convert_alpha()
SbackIdle_010 = pygame.image.load('playerImages2/Back - Idle_010.png').convert_alpha()
SbackIdle_011 = pygame.image.load('playerImages2/Back - Idle_011.png').convert_alpha()
SbackIdle_012 = pygame.image.load('playerImages2/Back - Idle_012.png').convert_alpha()
SbackIdle_013 = pygame.image.load('playerImages2/Back - Idle_013.png').convert_alpha()
SbackIdle_014 = pygame.image.load('playerImages2/Back - Idle_014.png').convert_alpha()
SbackIdle_015 = pygame.image.load('playerImages2/Back - Idle_015.png').convert_alpha()
SbackIdle_016 = pygame.image.load('playerImages2/Back - Idle_016.png').convert_alpha()
SbackIdle_017 = pygame.image.load('playerImages2/Back - Idle_017.png').convert_alpha()

SbackWalking_000 = pygame.image.load('playerImages2/Back - Walking_000.png').convert_alpha()
SbackWalking_001 = pygame.image.load('playerImages2/Back - Walking_001.png').convert_alpha()
SbackWalking_002 = pygame.image.load('playerImages2/Back - Walking_002.png').convert_alpha()
SbackWalking_003 = pygame.image.load('playerImages2/Back - Walking_003.png').convert_alpha()
SbackWalking_004 = pygame.image.load('playerImages2/Back - Walking_004.png').convert_alpha()
SbackWalking_005 = pygame.image.load('playerImages2/Back - Walking_005.png').convert_alpha()
SbackWalking_006 = pygame.image.load('playerImages2/Back - Walking_006.png').convert_alpha()
SbackWalking_007 = pygame.image.load('playerImages2/Back - Walking_007.png').convert_alpha()
SbackWalking_008 = pygame.image.load('playerImages2/Back - Walking_008.png').convert_alpha()
SbackWalking_009 = pygame.image.load('playerImages2/Back - Walking_009.png').convert_alpha()
SbackWalking_010 = pygame.image.load('playerImages2/Back - Walking_010.png').convert_alpha()
SbackWalking_011 = pygame.image.load('playerImages2/Back - Walking_011.png').convert_alpha()
SbackWalking_012 = pygame.image.load('playerImages2/Back - Walking_012.png').convert_alpha()
SbackWalking_013 = pygame.image.load('playerImages2/Back - Walking_013.png').convert_alpha()
SbackWalking_014 = pygame.image.load('playerImages2/Back - Walking_014.png').convert_alpha()
SbackWalking_015 = pygame.image.load('playerImages2/Back - Walking_015.png').convert_alpha()
SbackWalking_016 = pygame.image.load('playerImages2/Back - Walking_016.png').convert_alpha()
SbackWalking_017 = pygame.image.load('playerImages2/Back - Walking_017.png').convert_alpha()

SbackSlashing_000 = pygame.image.load('playerImages2/Back - Slashing_000.png').convert_alpha()
SbackSlashing_001 = pygame.image.load('playerImages2/Back - Slashing_001.png').convert_alpha()
SbackSlashing_002 = pygame.image.load('playerImages2/Back - Slashing_002.png').convert_alpha()
SbackSlashing_003 = pygame.image.load('playerImages2/Back - Slashing_003.png').convert_alpha()
SbackSlashing_004 = pygame.image.load('playerImages2/Back - Slashing_004.png').convert_alpha()
SbackSlashing_005 = pygame.image.load('playerImages2/Back - Slashing_005.png').convert_alpha()
SbackSlashing_006 = pygame.image.load('playerImages2/Back - Slashing_006.png').convert_alpha()
SbackSlashing_007 = pygame.image.load('playerImages2/Back - Slashing_007.png').convert_alpha()
SbackSlashing_008 = pygame.image.load('playerImages2/Back - Slashing_008.png').convert_alpha()

SleftIdle_000 = pygame.image.load('playerImages2/Left - Idle_000.png').convert_alpha()
SleftIdle_001 = pygame.image.load('playerImages2/Left - Idle_001.png').convert_alpha()
SleftIdle_002 = pygame.image.load('playerImages2/Left - Idle_002.png').convert_alpha()
SleftIdle_003 = pygame.image.load('playerImages2/Left - Idle_003.png').convert_alpha()
SleftIdle_004 = pygame.image.load('playerImages2/Left - Idle_004.png').convert_alpha()
SleftIdle_005 = pygame.image.load('playerImages2/Left - Idle_005.png').convert_alpha()
SleftIdle_006 = pygame.image.load('playerImages2/Left - Idle_006.png').convert_alpha()
SleftIdle_007 = pygame.image.load('playerImages2/Left - Idle_007.png').convert_alpha()
SleftIdle_008 = pygame.image.load('playerImages2/Left - Idle_008.png').convert_alpha()
SleftIdle_009 = pygame.image.load('playerImages2/Left - Idle_009.png').convert_alpha()
SleftIdle_010 = pygame.image.load('playerImages2/Left - Idle_010.png').convert_alpha()
SleftIdle_011 = pygame.image.load('playerImages2/Left - Idle_011.png').convert_alpha()
SleftIdle_012 = pygame.image.load('playerImages2/Left - Idle_012.png').convert_alpha()
SleftIdle_013 = pygame.image.load('playerImages2/Left - Idle_013.png').convert_alpha()
SleftIdle_014 = pygame.image.load('playerImages2/Left - Idle_014.png').convert_alpha()
SleftIdle_015 = pygame.image.load('playerImages2/Left - Idle_015.png').convert_alpha()
SleftIdle_016 = pygame.image.load('playerImages2/Left - Idle_016.png').convert_alpha()
SleftIdle_017 = pygame.image.load('playerImages2/Left - Idle_017.png').convert_alpha()

SleftIdleBlinking_000 = pygame.image.load('playerImages2/Left - Idle Blinking_000.png').convert_alpha()
SleftIdleBlinking_001 = pygame.image.load('playerImages2/Left - Idle Blinking_001.png').convert_alpha()
SleftIdleBlinking_002 = pygame.image.load('playerImages2/Left - Idle Blinking_002.png').convert_alpha()
SleftIdleBlinking_003 = pygame.image.load('playerImages2/Left - Idle Blinking_003.png').convert_alpha()
SleftIdleBlinking_004 = pygame.image.load('playerImages2/Left - Idle Blinking_004.png').convert_alpha()
SleftIdleBlinking_005 = pygame.image.load('playerImages2/Left - Idle Blinking_005.png').convert_alpha()
SleftIdleBlinking_006 = pygame.image.load('playerImages2/Left - Idle Blinking_006.png').convert_alpha()
SleftIdleBlinking_007 = pygame.image.load('playerImages2/Left - Idle Blinking_007.png').convert_alpha()
SleftIdleBlinking_008 = pygame.image.load('playerImages2/Left - Idle Blinking_008.png').convert_alpha()
SleftIdleBlinking_009 = pygame.image.load('playerImages2/Left - Idle Blinking_009.png').convert_alpha()
SleftIdleBlinking_010 = pygame.image.load('playerImages2/Left - Idle Blinking_010.png').convert_alpha()
SleftIdleBlinking_011 = pygame.image.load('playerImages2/Left - Idle Blinking_011.png').convert_alpha()
SleftIdleBlinking_012 = pygame.image.load('playerImages2/Left - Idle Blinking_012.png').convert_alpha()
SleftIdleBlinking_013 = pygame.image.load('playerImages2/Left - Idle Blinking_013.png').convert_alpha()
SleftIdleBlinking_014 = pygame.image.load('playerImages2/Left - Idle Blinking_014.png').convert_alpha()
SleftIdleBlinking_015 = pygame.image.load('playerImages2/Left - Idle Blinking_015.png').convert_alpha()
SleftIdleBlinking_016 = pygame.image.load('playerImages2/Left - Idle Blinking_016.png').convert_alpha()
SleftIdleBlinking_017 = pygame.image.load('playerImages2/Left - Idle Blinking_017.png').convert_alpha()

SleftWalking_000 = pygame.image.load('playerImages2/Left - Walking_000.png').convert_alpha()
SleftWalking_001 = pygame.image.load('playerImages2/Left - Walking_001.png').convert_alpha()
SleftWalking_002 = pygame.image.load('playerImages2/Left - Walking_002.png').convert_alpha()
SleftWalking_003 = pygame.image.load('playerImages2/Left - Walking_003.png').convert_alpha()
SleftWalking_004 = pygame.image.load('playerImages2/Left - Walking_004.png').convert_alpha()
SleftWalking_005 = pygame.image.load('playerImages2/Left - Walking_005.png').convert_alpha()
SleftWalking_006 = pygame.image.load('playerImages2/Left - Walking_006.png').convert_alpha()
SleftWalking_007 = pygame.image.load('playerImages2/Left - Walking_007.png').convert_alpha()
SleftWalking_008 = pygame.image.load('playerImages2/Left - Walking_008.png').convert_alpha()
SleftWalking_009 = pygame.image.load('playerImages2/Left - Walking_009.png').convert_alpha()
SleftWalking_010 = pygame.image.load('playerImages2/Left - Walking_010.png').convert_alpha()
SleftWalking_011 = pygame.image.load('playerImages2/Left - Walking_011.png').convert_alpha()
SleftWalking_012 = pygame.image.load('playerImages2/Left - Walking_012.png').convert_alpha()
SleftWalking_013 = pygame.image.load('playerImages2/Left - Walking_013.png').convert_alpha()
SleftWalking_014 = pygame.image.load('playerImages2/Left - Walking_014.png').convert_alpha()
SleftWalking_015 = pygame.image.load('playerImages2/Left - Walking_015.png').convert_alpha()
SleftWalking_016 = pygame.image.load('playerImages2/Left - Walking_016.png').convert_alpha()
SleftWalking_017 = pygame.image.load('playerImages2/Left - Walking_017.png').convert_alpha()

SleftSlashing_000 = pygame.image.load('playerImages2/Left - Slashing_000.png').convert_alpha()
SleftSlashing_001 = pygame.image.load('playerImages2/Left - Slashing_001.png').convert_alpha()
SleftSlashing_002 = pygame.image.load('playerImages2/Left - Slashing_002.png').convert_alpha()
SleftSlashing_003 = pygame.image.load('playerImages2/Left - Slashing_003.png').convert_alpha()
SleftSlashing_004 = pygame.image.load('playerImages2/Left - Slashing_004.png').convert_alpha()
SleftSlashing_005 = pygame.image.load('playerImages2/Left - Slashing_005.png').convert_alpha()
SleftSlashing_006 = pygame.image.load('playerImages2/Left - Slashing_006.png').convert_alpha()
SleftSlashing_007 = pygame.image.load('playerImages2/Left - Slashing_007.png').convert_alpha()
SleftSlashing_008 = pygame.image.load('playerImages2/Left - Slashing_008.png').convert_alpha()
##########################################################################################

##########################################################################################
class Player:
    def __init__(self):

        self.visible = True
        self.animateCounter = 0
        self.animate = 0
        self.direction = 0
        self.attackDelay = 10

        self.walkCounter = 0
        self.attackCounter = 0

        self.x = (64 * 9)
        self.y = 64 * 4
        self.Tile = int(((self.x + 64) /64) + (((self.y + 64)/ 64) * 20)) #23
        self.attackedTile = -1 #out of map

        self.rightBorder = [19,39,59,79,99,119,139,159,179,199,219]
        self.leftBorder =  [0,20,40,60,80,100,120,140,160,180,200]
        self.backBorder =  [20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39]
        #self.frontBorder = [200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219]
        self.frontBorder = []#this is so that you can exit down

        self.blinkCounter = 0
        self.blinking = False
         
        self.fishing = False
        self.fishing_cast = False

    def teleport(self,tile):
        global worldx
        global worldy

        self.Tile = tile

        self.visible = False
        self.teleport_destination_down = ((int((tile * 1) / 20)) * 64) - (64 * 6)
        self.teleport_destination_up = ((int(tile / 20)) * 64) -256

        if self.direction == 0: #s
                worldy = ((int((tile * 1) / 20)) * 64) - (64 * 6)
                worldx = (((tile % 20) * 64) + 32) - 640
                self.Tile = self.Tile - 20

                worldy = self.teleport_destination_down * 2

                for i in range(int(100)): #screen move animation
                    worldy = worldy - (self.teleport_destination_down / 100)
                    screen.fill((40,37,34))
                    drawMap()
                    pygame.display.update()

                self.visible = True

        elif self.direction == 2: #w
                worldy = ((int(tile / 20)) * 64) -256
                worldx = (((tile % 20) * 64) + 32) - 640
                self.Tile = self.Tile + 20

                worldy = self.teleport_destination_up * 2

                for i in range(int(100)): #screen move animation
                    worldy = worldy - (self.teleport_destination_up / 100)
                    screen.fill((40,37,34))
                    drawMap()
                    pygame.display.update()
                
                self.visible = True

    def draw(self):
        #
        #@self change the way that you do "blinking"
        #Blinking can borrow frames from the regular images and then SWITCH a few frames instead of doing all 17
        #

        if self.visible == True:
            #print(self.Tile, self.attackedTile)
            screen.blit(Player_Shadow_000,(self.x,self.y))#shadow

            if self.fishing_cast == True:
                    screen.blit(frontFishing_000,(self.x,self.y))

            elif self.direction == 0: #Front

                if self.animate == 0: #front Idle
                    if self.blinking == False:#front Idle
                        if int(self.animateCounter) == 0: screen.blit(frontIdle_000,(self.x,self.y))
                        elif int(self.animateCounter) == 1: screen.blit(frontIdle_001,(self.x,self.y))
                        elif int(self.animateCounter) == 2: screen.blit(frontIdle_002,(self.x,self.y))
                        elif int(self.animateCounter) == 3: screen.blit(frontIdle_003,(self.x,self.y))
                        elif int(self.animateCounter) == 4: screen.blit(frontIdle_004,(self.x,self.y))
                        elif int(self.animateCounter) == 5: screen.blit(frontIdle_005,(self.x,self.y))
                        elif int(self.animateCounter) == 6: screen.blit(frontIdle_006,(self.x,self.y))
                        elif int(self.animateCounter) == 7: screen.blit(frontIdle_007,(self.x,self.y))
                        elif int(self.animateCounter) == 8: screen.blit(frontIdle_008,(self.x,self.y))
                        elif int(self.animateCounter) == 9: screen.blit(frontIdle_009,(self.x,self.y))
                        elif int(self.animateCounter) == 10: screen.blit(frontIdle_010,(self.x,self.y))
                        elif int(self.animateCounter) == 11: screen.blit(frontIdle_011,(self.x,self.y))
                        elif int(self.animateCounter) == 12: screen.blit(frontIdle_012,(self.x,self.y))
                        elif int(self.animateCounter) == 13: screen.blit(frontIdle_013,(self.x,self.y))
                        elif int(self.animateCounter) == 14: screen.blit(frontIdle_014,(self.x,self.y))
                        elif int(self.animateCounter) == 15: screen.blit(frontIdle_015,(self.x,self.y))
                        elif int(self.animateCounter) == 16: screen.blit(frontIdle_016,(self.x,self.y))
               
                        elif int(self.animateCounter) == 17:
                                screen.blit(frontIdle_017,(self.x,self.y)) 
                                self.blinkCounter += 1

                                if self.blinkCounter == 10:
                                    self.blinking = True
                
                    elif self.blinking == True:#front IdleBlinking
                
                        if int(self.animateCounter) == 0: screen.blit(frontIdleBlinking_000,(self.x,self.y))
                        elif int(self.animateCounter) == 1: screen.blit(frontIdleBlinking_001,(self.x,self.y))
                        elif int(self.animateCounter) == 2: screen.blit(frontIdleBlinking_002,(self.x,self.y))
                        elif int(self.animateCounter) == 3: screen.blit(frontIdleBlinking_003,(self.x,self.y))
                        elif int(self.animateCounter) == 4: screen.blit(frontIdleBlinking_004,(self.x,self.y))
                        elif int(self.animateCounter) == 5: screen.blit(frontIdleBlinking_005,(self.x,self.y))
                        elif int(self.animateCounter) == 6: screen.blit(frontIdleBlinking_006,(self.x,self.y))
                        elif int(self.animateCounter) == 7: screen.blit(frontIdleBlinking_007,(self.x,self.y))
                        elif int(self.animateCounter) == 8: screen.blit(frontIdleBlinking_008,(self.x,self.y))
                        elif int(self.animateCounter) == 9: screen.blit(frontIdleBlinking_009,(self.x,self.y))
                        elif int(self.animateCounter) == 10: screen.blit(frontIdleBlinking_010,(self.x,self.y))
                        elif int(self.animateCounter) == 11: screen.blit(frontIdleBlinking_011,(self.x,self.y))
                        elif int(self.animateCounter) == 12: screen.blit(frontIdleBlinking_012,(self.x,self.y))
                        elif int(self.animateCounter) == 13: screen.blit(frontIdleBlinking_013,(self.x,self.y))
                        elif int(self.animateCounter) == 14: screen.blit(frontIdleBlinking_014,(self.x,self.y))
                        elif int(self.animateCounter) == 15: screen.blit(frontIdleBlinking_015,(self.x,self.y))
                        elif int(self.animateCounter) == 16: screen.blit(frontIdleBlinking_016,(self.x,self.y))
                        elif int(self.animateCounter) == 17:
                            screen.blit(frontIdleBlinking_017,(self.x,self.y))
                            self.blinkCounter = 0
                            self.blinking = False

                elif self.animate == 1: #front Walking
                    if int(self.animateCounter) == 0: screen.blit(frontWalking_000,(self.x,self.y))
                    elif int(self.animateCounter) == 1: screen.blit(frontWalking_001,(self.x,self.y))
                    elif int(self.animateCounter) == 2: screen.blit(frontWalking_002,(self.x,self.y))
                    elif int(self.animateCounter) == 3: screen.blit(frontWalking_003,(self.x,self.y))
                    elif int(self.animateCounter) == 4: screen.blit(frontWalking_004,(self.x,self.y))
                    elif int(self.animateCounter) == 5: screen.blit(frontWalking_005,(self.x,self.y))
                    elif int(self.animateCounter) == 6: screen.blit(frontWalking_006,(self.x,self.y))
                    elif int(self.animateCounter) == 7: screen.blit(frontWalking_007,(self.x,self.y))
                    elif int(self.animateCounter) == 8: screen.blit(frontWalking_008,(self.x,self.y))
                    elif int(self.animateCounter) == 9: screen.blit(frontWalking_009,(self.x,self.y))
                    elif int(self.animateCounter) == 10: screen.blit(frontWalking_010,(self.x,self.y))
                    elif int(self.animateCounter) == 11: screen.blit(frontWalking_011,(self.x,self.y))
                    elif int(self.animateCounter) == 12: screen.blit(frontWalking_012,(self.x,self.y))
                    elif int(self.animateCounter) == 13: screen.blit(frontWalking_013,(self.x,self.y))
                    elif int(self.animateCounter) == 14: screen.blit(frontWalking_014,(self.x,self.y))
                    elif int(self.animateCounter) == 15: screen.blit(frontWalking_015,(self.x,self.y))
                    elif int(self.animateCounter) == 16: screen.blit(frontWalking_016,(self.x,self.y))
                    elif int(self.animateCounter) == 17: screen.blit(frontWalking_017,(self.x,self.y))

                elif self.animate == 2:#front Attack
                    if int(self.animateCounter) == 0: screen.blit(frontSlashing_000,(self.x,self.y))
                    elif int(self.animateCounter) == 1: screen.blit(frontSlashing_001,(self.x,self.y))
                    elif int(self.animateCounter) == 2: screen.blit(frontSlashing_002,(self.x,self.y))
                    elif int(self.animateCounter) == 3: screen.blit(frontSlashing_003,(self.x,self.y))
                    elif int(self.animateCounter) == 4: screen.blit(frontSlashing_004,(self.x,self.y))
                    elif int(self.animateCounter) == 5: screen.blit(frontSlashing_005,(self.x,self.y))
                    elif int(self.animateCounter) == 6: screen.blit(frontSlashing_006,(self.x,self.y))
                    elif int(self.animateCounter) == 7: screen.blit(frontSlashing_007,(self.x,self.y))
                    elif int(self.animateCounter) == 8: screen.blit(frontSlashing_008,(self.x,self.y))

                    if self.Tile not in self.frontBorder:
                        self.attackedTile = self.Tile + 20
    

            elif self.direction == 1: #Right

                if self.animate == 0: #right Idle
                    if self.blinking == False:
                        if int(self.animateCounter) == 0: screen.blit(rightIdle_000,(self.x,self.y))
                        elif int(self.animateCounter) == 1: screen.blit(rightIdle_001,(self.x,self.y))
                        elif int(self.animateCounter) == 2: screen.blit(rightIdle_002,(self.x,self.y))
                        elif int(self.animateCounter) == 3: screen.blit(rightIdle_003,(self.x,self.y))
                        elif int(self.animateCounter) == 4: screen.blit(rightIdle_004,(self.x,self.y))
                        elif int(self.animateCounter) == 5: screen.blit(rightIdle_005,(self.x,self.y))
                        elif int(self.animateCounter) == 6: screen.blit(rightIdle_006,(self.x,self.y))
                        elif int(self.animateCounter) == 7: screen.blit(rightIdle_007,(self.x,self.y))
                        elif int(self.animateCounter) == 8: screen.blit(rightIdle_008,(self.x,self.y))
                        elif int(self.animateCounter) == 9: screen.blit(rightIdle_009,(self.x,self.y))
                        elif int(self.animateCounter) == 10: screen.blit(rightIdle_010,(self.x,self.y))
                        elif int(self.animateCounter) == 11: screen.blit(rightIdle_011,(self.x,self.y))
                        elif int(self.animateCounter) == 12: screen.blit(rightIdle_012,(self.x,self.y))
                        elif int(self.animateCounter) == 13: screen.blit(rightIdle_013,(self.x,self.y))
                        elif int(self.animateCounter) == 14: screen.blit(rightIdle_014,(self.x,self.y))
                        elif int(self.animateCounter) == 15: screen.blit(rightIdle_015,(self.x,self.y))
                        elif int(self.animateCounter) == 16: screen.blit(rightIdle_016,(self.x,self.y))
                    
                        elif int(self.animateCounter) == 17: #switch to blinking
                            screen.blit(rightIdle_017,(self.x,self.y)) 
                            self.blinkCounter += 1

                            if self.blinkCounter == 10:
                                self.blinking = True
                
                    elif self.blinking == True:#right IdleBlinking
                
                        if int(self.animateCounter) == 0: screen.blit(rightIdleBlinking_000,(self.x,self.y))
                        elif int(self.animateCounter) == 1: screen.blit(rightIdleBlinking_001,(self.x,self.y))
                        elif int(self.animateCounter) == 2: screen.blit(rightIdleBlinking_002,(self.x,self.y))
                        elif int(self.animateCounter) == 3: screen.blit(rightIdleBlinking_003,(self.x,self.y))
                        elif int(self.animateCounter) == 4: screen.blit(rightIdleBlinking_004,(self.x,self.y))
                        elif int(self.animateCounter) == 5: screen.blit(rightIdleBlinking_005,(self.x,self.y))
                        elif int(self.animateCounter) == 6: screen.blit(rightIdleBlinking_006,(self.x,self.y))
                        elif int(self.animateCounter) == 7: screen.blit(rightIdleBlinking_007,(self.x,self.y))
                        elif int(self.animateCounter) == 8: screen.blit(rightIdleBlinking_008,(self.x,self.y))
                        elif int(self.animateCounter) == 9: screen.blit(rightIdleBlinking_009,(self.x,self.y))
                        elif int(self.animateCounter) == 10: screen.blit(rightIdleBlinking_010,(self.x,self.y))
                        elif int(self.animateCounter) == 11: screen.blit(rightIdleBlinking_011,(self.x,self.y))
                        elif int(self.animateCounter) == 12: screen.blit(rightIdleBlinking_012,(self.x,self.y))
                        elif int(self.animateCounter) == 13: screen.blit(rightIdleBlinking_013,(self.x,self.y))
                        elif int(self.animateCounter) == 14: screen.blit(rightIdleBlinking_014,(self.x,self.y))
                        elif int(self.animateCounter) == 15: screen.blit(rightIdleBlinking_015,(self.x,self.y))
                        elif int(self.animateCounter) == 16: screen.blit(rightIdleBlinking_016,(self.x,self.y))
                        elif int(self.animateCounter) == 17:
                            screen.blit(rightIdleBlinking_017,(self.x,self.y))
                            self.blinkCounter = 0
                            self.blinking = False
                

                elif self.animate == 1: #right Walking
                    if int(self.animateCounter) == 0: screen.blit(rightWalking_000,(self.x,self.y))
                    elif int(self.animateCounter) == 1: screen.blit(rightWalking_001,(self.x,self.y))
                    elif int(self.animateCounter) == 2: screen.blit(rightWalking_002,(self.x,self.y))
                    elif int(self.animateCounter) == 3: screen.blit(rightWalking_003,(self.x,self.y))
                    elif int(self.animateCounter) == 4: screen.blit(rightWalking_004,(self.x,self.y))
                    elif int(self.animateCounter) == 5: screen.blit(rightWalking_005,(self.x,self.y))
                    elif int(self.animateCounter) == 6: screen.blit(rightWalking_006,(self.x,self.y))
                    elif int(self.animateCounter) == 7: screen.blit(rightWalking_007,(self.x,self.y))
                    elif int(self.animateCounter) == 8: screen.blit(rightWalking_008,(self.x,self.y))
                    elif int(self.animateCounter) == 9: screen.blit(rightWalking_009,(self.x,self.y))
                    elif int(self.animateCounter) == 10: screen.blit(rightWalking_010,(self.x,self.y))
                    elif int(self.animateCounter) == 11: screen.blit(rightWalking_011,(self.x,self.y))
                    elif int(self.animateCounter) == 12: screen.blit(rightWalking_012,(self.x,self.y))
                    elif int(self.animateCounter) == 13: screen.blit(rightWalking_013,(self.x,self.y))
                    elif int(self.animateCounter) == 14: screen.blit(rightWalking_014,(self.x,self.y))
                    elif int(self.animateCounter) == 15: screen.blit(rightWalking_015,(self.x,self.y))
                    elif int(self.animateCounter) == 16: screen.blit(rightWalking_016,(self.x,self.y))
                    elif int(self.animateCounter) == 17: screen.blit(rightWalking_017,(self.x,self.y))

                elif self.animate == 2:#right Attack
                    if int(self.animateCounter) == 0: screen.blit(rightSlashing_000,(self.x,self.y))
                    elif int(self.animateCounter) == 1: screen.blit(rightSlashing_001,(self.x,self.y))
                    elif int(self.animateCounter) == 2: screen.blit(rightSlashing_002,(self.x,self.y))
                    elif int(self.animateCounter) == 3: screen.blit(rightSlashing_003,(self.x,self.y))
                    elif int(self.animateCounter) == 4: screen.blit(rightSlashing_004,(self.x,self.y))
                    elif int(self.animateCounter) == 5: screen.blit(rightSlashing_005,(self.x,self.y))
                    elif int(self.animateCounter) == 6: screen.blit(rightSlashing_006,(self.x,self.y))
                    elif int(self.animateCounter) == 7: screen.blit(rightSlashing_007,(self.x,self.y))
                    elif int(self.animateCounter) == 8: screen.blit(rightSlashing_008,(self.x,self.y))

                    if self.Tile not in self.rightBorder:
                        self.attackedTile = self.Tile + 1

            elif self.direction == 2: #Back

                if self.animate == 0:#back Idle
                    if int(self.animateCounter) == 0: screen.blit(backIdle_000,(self.x,self.y))
                    elif int(self.animateCounter) == 1: screen.blit(backIdle_001,(self.x,self.y))
                    elif int(self.animateCounter) == 2: screen.blit(backIdle_002,(self.x,self.y))
                    elif int(self.animateCounter) == 3: screen.blit(backIdle_003,(self.x,self.y))
                    elif int(self.animateCounter) == 4: screen.blit(backIdle_004,(self.x,self.y))
                    elif int(self.animateCounter) == 5: screen.blit(backIdle_005,(self.x,self.y))
                    elif int(self.animateCounter) == 6: screen.blit(backIdle_006,(self.x,self.y))
                    elif int(self.animateCounter) == 7: screen.blit(backIdle_007,(self.x,self.y))
                    elif int(self.animateCounter) == 8: screen.blit(backIdle_008,(self.x,self.y))
                    elif int(self.animateCounter) == 9: screen.blit(backIdle_009,(self.x,self.y))
                    elif int(self.animateCounter) == 10: screen.blit(backIdle_010,(self.x,self.y))
                    elif int(self.animateCounter) == 11: screen.blit(backIdle_011,(self.x,self.y))
                    elif int(self.animateCounter) == 12: screen.blit(backIdle_012,(self.x,self.y))
                    elif int(self.animateCounter) == 13: screen.blit(backIdle_013,(self.x,self.y))
                    elif int(self.animateCounter) == 14: screen.blit(backIdle_014,(self.x,self.y))
                    elif int(self.animateCounter) == 15: screen.blit(backIdle_015,(self.x,self.y))
                    elif int(self.animateCounter) == 16: screen.blit(backIdle_016,(self.x,self.y))
                    elif int(self.animateCounter) == 17: screen.blit(backIdle_017,(self.x,self.y))


                elif self.animate == 1:#back Walking
                    if int(self.animateCounter) == 0: screen.blit(backWalking_000,(self.x,self.y))
                    elif int(self.animateCounter) == 1: screen.blit(backWalking_001,(self.x,self.y))
                    elif int(self.animateCounter) == 2: screen.blit(backWalking_002,(self.x,self.y))
                    elif int(self.animateCounter) == 3: screen.blit(backWalking_003,(self.x,self.y))
                    elif int(self.animateCounter) == 4: screen.blit(backWalking_004,(self.x,self.y))
                    elif int(self.animateCounter) == 5: screen.blit(backWalking_005,(self.x,self.y))
                    elif int(self.animateCounter) == 6: screen.blit(backWalking_006,(self.x,self.y))
                    elif int(self.animateCounter) == 7: screen.blit(backWalking_007,(self.x,self.y))
                    elif int(self.animateCounter) == 8: screen.blit(backWalking_008,(self.x,self.y))
                    elif int(self.animateCounter) == 9: screen.blit(backWalking_009,(self.x,self.y))
                    elif int(self.animateCounter) == 10: screen.blit(backWalking_010,(self.x,self.y))
                    elif int(self.animateCounter) == 11: screen.blit(backWalking_011,(self.x,self.y))
                    elif int(self.animateCounter) == 12: screen.blit(backWalking_012,(self.x,self.y))
                    elif int(self.animateCounter) == 13: screen.blit(backWalking_013,(self.x,self.y))
                    elif int(self.animateCounter) == 14: screen.blit(backWalking_014,(self.x,self.y))
                    elif int(self.animateCounter) == 15: screen.blit(backWalking_015,(self.x,self.y))
                    elif int(self.animateCounter) == 16: screen.blit(backWalking_016,(self.x,self.y))
                    elif int(self.animateCounter) == 17: screen.blit(backWalking_017,(self.x,self.y))

                elif self.animate == 2:#back Attack
                    if int(self.animateCounter) == 0: screen.blit(backSlashing_000,(self.x,self.y))
                    elif int(self.animateCounter) == 1: screen.blit(backSlashing_001,(self.x,self.y))
                    elif int(self.animateCounter) == 2: screen.blit(backSlashing_002,(self.x,self.y))
                    elif int(self.animateCounter) == 3: screen.blit(backSlashing_003,(self.x,self.y))
                    elif int(self.animateCounter) == 4: screen.blit(backSlashing_004,(self.x,self.y))
                    elif int(self.animateCounter) == 5: screen.blit(backSlashing_005,(self.x,self.y))
                    elif int(self.animateCounter) == 6: screen.blit(backSlashing_006,(self.x,self.y))
                    elif int(self.animateCounter) == 7: screen.blit(backSlashing_007,(self.x,self.y))
                    elif int(self.animateCounter) == 8: screen.blit(backSlashing_008,(self.x,self.y))
                
                    if self.Tile not in self.backBorder:
                        self.attackedTile = self.Tile - 20

            elif self.direction == 3: #Left

                if self.animate == 0: #left Idle
                    if self.blinking == False:#left IdleBlinking
                        if int(self.animateCounter) == 0: screen.blit(leftIdle_000,(self.x,self.y))
                        elif int(self.animateCounter) == 1: screen.blit(leftIdle_001,(self.x,self.y))
                        elif int(self.animateCounter) == 2: screen.blit(leftIdle_002,(self.x,self.y))
                        elif int(self.animateCounter) == 3: screen.blit(leftIdle_003,(self.x,self.y))
                        elif int(self.animateCounter) == 4: screen.blit(leftIdle_004,(self.x,self.y))
                        elif int(self.animateCounter) == 5: screen.blit(leftIdle_005,(self.x,self.y))
                        elif int(self.animateCounter) == 6: screen.blit(leftIdle_006,(self.x,self.y))
                        elif int(self.animateCounter) == 7: screen.blit(leftIdle_007,(self.x,self.y))
                        elif int(self.animateCounter) == 8: screen.blit(leftIdle_008,(self.x,self.y))
                        elif int(self.animateCounter) == 9: screen.blit(leftIdle_009,(self.x,self.y))
                        elif int(self.animateCounter) == 10: screen.blit(leftIdle_010,(self.x,self.y))
                        elif int(self.animateCounter) == 11: screen.blit(leftIdle_011,(self.x,self.y))
                        elif int(self.animateCounter) == 12: screen.blit(leftIdle_012,(self.x,self.y))
                        elif int(self.animateCounter) == 13: screen.blit(leftIdle_013,(self.x,self.y))
                        elif int(self.animateCounter) == 14: screen.blit(leftIdle_014,(self.x,self.y))
                        elif int(self.animateCounter) == 15: screen.blit(leftIdle_015,(self.x,self.y))
                        elif int(self.animateCounter) == 16: screen.blit(leftIdle_016,(self.x,self.y))
                        elif int(self.animateCounter) == 17: #switch to blinking
                                screen.blit(leftIdle_017,(self.x,self.y)) 
                                self.blinkCounter += 1

                                if self.blinkCounter == 10:
                                    self.blinking = True
                
                    elif self.blinking == True:#left IdleBlinking
                
                        if int(self.animateCounter) == 0: screen.blit(leftIdleBlinking_000,(self.x,self.y))
                        elif int(self.animateCounter) == 1: screen.blit(leftIdleBlinking_001,(self.x,self.y))
                        elif int(self.animateCounter) == 2: screen.blit(leftIdleBlinking_002,(self.x,self.y))
                        elif int(self.animateCounter) == 3: screen.blit(leftIdleBlinking_003,(self.x,self.y))
                        elif int(self.animateCounter) == 4: screen.blit(leftIdleBlinking_004,(self.x,self.y))
                        elif int(self.animateCounter) == 5: screen.blit(leftIdleBlinking_005,(self.x,self.y))
                        elif int(self.animateCounter) == 6: screen.blit(leftIdleBlinking_006,(self.x,self.y))
                        elif int(self.animateCounter) == 7: screen.blit(leftIdleBlinking_007,(self.x,self.y))
                        elif int(self.animateCounter) == 8: screen.blit(leftIdleBlinking_008,(self.x,self.y))
                        elif int(self.animateCounter) == 9: screen.blit(leftIdleBlinking_009,(self.x,self.y))
                        elif int(self.animateCounter) == 10: screen.blit(leftIdleBlinking_010,(self.x,self.y))
                        elif int(self.animateCounter) == 11: screen.blit(leftIdleBlinking_011,(self.x,self.y))
                        elif int(self.animateCounter) == 12: screen.blit(leftIdleBlinking_012,(self.x,self.y))
                        elif int(self.animateCounter) == 13: screen.blit(leftIdleBlinking_013,(self.x,self.y))
                        elif int(self.animateCounter) == 14: screen.blit(leftIdleBlinking_014,(self.x,self.y))
                        elif int(self.animateCounter) == 15: screen.blit(leftIdleBlinking_015,(self.x,self.y))
                        elif int(self.animateCounter) == 16: screen.blit(leftIdleBlinking_016,(self.x,self.y))
                        elif int(self.animateCounter) == 17:
                            screen.blit(leftIdleBlinking_017,(self.x,self.y))
                            self.blinkCounter = 0
                            self.blinking = False
                

                elif self.animate == 1: #left Walking
                    if int(self.animateCounter) == 0: screen.blit(leftWalking_000,(self.x,self.y))
                    elif int(self.animateCounter) == 1: screen.blit(leftWalking_001,(self.x,self.y))
                    elif int(self.animateCounter) == 2: screen.blit(leftWalking_002,(self.x,self.y))
                    elif int(self.animateCounter) == 3: screen.blit(leftWalking_003,(self.x,self.y))
                    elif int(self.animateCounter) == 4: screen.blit(leftWalking_004,(self.x,self.y))
                    elif int(self.animateCounter) == 5: screen.blit(leftWalking_005,(self.x,self.y))
                    elif int(self.animateCounter) == 6: screen.blit(leftWalking_006,(self.x,self.y))
                    elif int(self.animateCounter) == 7: screen.blit(leftWalking_007,(self.x,self.y))
                    elif int(self.animateCounter) == 8: screen.blit(leftWalking_008,(self.x,self.y))
                    elif int(self.animateCounter) == 9: screen.blit(leftWalking_009,(self.x,self.y))
                    elif int(self.animateCounter) == 10: screen.blit(leftWalking_010,(self.x,self.y))
                    elif int(self.animateCounter) == 11: screen.blit(leftWalking_011,(self.x,self.y))
                    elif int(self.animateCounter) == 12: screen.blit(leftWalking_012,(self.x,self.y))
                    elif int(self.animateCounter) == 13: screen.blit(leftWalking_013,(self.x,self.y))
                    elif int(self.animateCounter) == 14: screen.blit(leftWalking_014,(self.x,self.y))
                    elif int(self.animateCounter) == 15: screen.blit(leftWalking_015,(self.x,self.y))
                    elif int(self.animateCounter) == 16: screen.blit(leftWalking_016,(self.x,self.y))
                    elif int(self.animateCounter) == 17: screen.blit(leftWalking_017,(self.x,self.y))

                elif self.animate == 2:#left Attack
                    if int(self.animateCounter) == 0: screen.blit(leftSlashing_000,(self.x,self.y))
                    elif int(self.animateCounter) == 1: screen.blit(leftSlashing_001,(self.x,self.y))
                    elif int(self.animateCounter) == 2: screen.blit(leftSlashing_002,(self.x,self.y))
                    elif int(self.animateCounter) == 3: screen.blit(leftSlashing_003,(self.x,self.y))
                    elif int(self.animateCounter) == 4: screen.blit(leftSlashing_004,(self.x,self.y))
                    elif int(self.animateCounter) == 5: screen.blit(leftSlashing_005,(self.x,self.y))
                    elif int(self.animateCounter) == 6: screen.blit(leftSlashing_006,(self.x,self.y))
                    elif int(self.animateCounter) == 7: screen.blit(leftSlashing_007,(self.x,self.y))
                    elif int(self.animateCounter) == 8: screen.blit(leftSlashing_008,(self.x,self.y))

                    if self.Tile not in self.leftBorder:
                        self.attackedTile = self.Tile - 1


    def movement(self):
        safeTiles = [13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,33,34,35,36,37,38,80,81,82,83,85,87]
    
        if pressed[pygame.K_s] and self.walkCounter == 0 and self.attackCounter == 0 and not pressed[pygame.K_w] and not pressed[pygame.K_a] and not pressed[pygame.K_d]:
            self.direction = 0
            if map[self.Tile + 20] in safeTiles and self.Tile not in self.frontBorder:
                self.walkCounter = 17

                if map[self.Tile + 20] == 85:
                    teleport(self.Tile)

        if pressed[pygame.K_d] and self.walkCounter == 0 and self.attackCounter == 0 and not pressed[pygame.K_a] and not pressed[pygame.K_s] and not pressed[pygame.K_w]:
            self.direction = 1
            if map[self.Tile + 1] in safeTiles and self.Tile not in self.rightBorder:
                self.walkCounter = 17

                if map[self.Tile + 1] == 85:
                    teleport(self.Tile)

        if pressed[pygame.K_w] and self.walkCounter == 0 and self.attackCounter == 0 and not pressed[pygame.K_s] and not pressed[pygame.K_a] and not pressed[pygame.K_d]:
            self.direction = 2
            if map[self.Tile - 20] in safeTiles and self.Tile not in self.backBorder:
                self.walkCounter = 17

                if map[self.Tile - 20] == 85:
                    teleport(self.Tile)

        if pressed[pygame.K_a] and self.walkCounter == 0 and self.attackCounter == 0 and not pressed[pygame.K_d] and not pressed[pygame.K_s] and not pressed[pygame.K_w]:
            self.direction = 3
            if map[self.Tile - 1] in safeTiles and self.Tile not in self.leftBorder:
                self.walkCounter = 17

                if map[self.Tile - 1] == 85:
                    teleport(self.Tile)

###############################################
    
        elif pressed[pygame.K_SPACE] and self.walkCounter == 0 and self.attackCounter == 0 and self.attackDelay == 0 and self.fishing == True: #fishing
            if self.fishing_cast == True:
                self.fishing_cast = False
                pygame.time.delay(150)################### not good practice. (remove later)

            elif self.fishing_cast == False:
                self.fishing_cast = True
                pygame.time.delay(150)################### not good practice. (remove later)
                
        elif pressed[pygame.K_SPACE] and self.walkCounter == 0 and self.attackCounter == 0 and self.attackDelay == 0: #attack
            self.animateCounter = 0
            self.attackCounter = 4
            self.attackDelay = 7

        #Face different Directions
        elif pressed[pygame.K_DOWN] and self.walkCounter == 0 and self.attackCounter == 0:
            self.direction = 0
        elif pressed[pygame.K_RIGHT] and self.walkCounter == 0 and self.attackCounter == 0:
            self.direction = 1
        elif pressed[pygame.K_UP] and self.walkCounter == 0 and self.attackCounter == 0:
            self.direction = 2
        elif pressed[pygame.K_LEFT] and self.walkCounter == 0 and self.attackCounter == 0:
            self.direction = 3

        elif pressed[pygame.K_e] and self.walkCounter == 0 and self.attackCounter == 0 and self.fishing_cast == False:
            global ItemPick
            if ItemPick == 0: #slash
                ItemPick = 1
                self.fishing = True
                pygame.time.delay(150)###################not good practice. (remove later)

            elif ItemPick == 1: #fish
                ItemPick = 0
                self.fishing = False
                pygame.time.delay(150)###################not good practice. (remove later)


        if self.walkCounter > 0 and self.walkCounter <= 16:
            self.animate = 1
            global worldx
            global worldy
            if self.direction == 0: worldy = worldy + 4
            elif self.direction == 1: worldx = worldx + 4
            elif self.direction == 2: worldy = worldy - 4
            elif self.direction == 3: worldx = worldx - 4

            self.walkCounter = self.walkCounter - 1
            if self.walkCounter == 0:
                #self.Tile = int(((self.x - 32 + 64) /64) + (((self.y + 64)/ 64) * 20))
                if self.direction == 0: self.Tile = self.Tile + 20 #s
                elif self.direction == 1: self.Tile = self.Tile + 1 #d
                elif self.direction == 2: self.Tile = self.Tile - 20 #w
                elif self.direction == 3: self.Tile = self.Tile - 1 #a
                self.animate = 0

                global gameState
                gameState = 1

        if self.walkCounter == 17:
            self.animateCounter = 0
            self.walkCounter = 16


        if self.walkCounter == 0 and pressed[pygame.K_d] == False and pressed[pygame.K_a] == False and pressed[pygame.K_w] == False and pressed[pygame.K_s] == False:
            self.animate = 0

        if self.attackCounter == 4: #play slash sound.
            #slashSound.play()
            pass

        if self.attackCounter > 0:
            self.animate = 2
            self.attackCounter = self.attackCounter - 1
            if self.attackCounter == 0:
                self.animate = 0
                self.attackedTile = -1

                gameState = 1

        elif self.attackDelay > 0:
            self.attackDelay = self.attackDelay - 1

    def animateObject(self):
        self.animateCounter += 1

        if self.animateCounter == 18:
            self.animateCounter = 0

    def getAttack(self):
        return self.attackedTile

    def getFishing_cast(self):
        return self.fishing_cast

    def getY(self):
        #return int(self.y / 64)
        #return int((self.y + 55)/ 64)
        return int(self.Tile / 20)

    def getPos(self):
        return self.x, self.y
        

class Skeleton:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y

        self.alive = 1

        self.animateCounter = 0
        self.animate = 0
        self.direction = direction
        self.attackDelay = 15

        self.walkCounter = 0
        self.attackCounter = 0

        self.damagedTimer = 0

        self.Tile = int(((self.x + 64) /64) + (((self.y + 64)/ 64) * 20))

        self.rightBorder = [19,39,59,79,99,119,139,159,179,199,219]
        self.leftBorder =  [0,20,40,60,80,100,120,140,160,180,200]
        self.backBorder =  [20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39]
        self.frontBorder = [200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219]

        self.blinkCounter = 0
        self.blinking = False

        self.BasicAI = random.randint(1,4)

    def draw(self):
        if self.alive == 1:
            #print(self.Tile, self.attackedTile)
            screen.blit(Player_Shadow_000,(self.x - worldx,self.y -worldy))#shadow

            if self.direction == 0: #Front

                if self.animate == 0: #front Idle
                    if self.blinking == False:#front Idle
                        if int(self.animateCounter) == 0: screen.blit(SfrontIdle_000,(self.x - worldx,self.y - worldy))
                        elif int(self.animateCounter) == 1: screen.blit(SfrontIdle_001,(self.x - worldx,self.y - worldy))
                        elif int(self.animateCounter) == 2: screen.blit(SfrontIdle_002,(self.x - worldx,self.y - worldy))
                        elif int(self.animateCounter) == 3: screen.blit(SfrontIdle_003,(self.x - worldx,self.y - worldy))
                        elif int(self.animateCounter) == 4: screen.blit(SfrontIdle_004,(self.x - worldx,self.y - worldy))
                        elif int(self.animateCounter) == 5: screen.blit(SfrontIdle_005,(self.x - worldx,self.y - worldy))
                        elif int(self.animateCounter) == 6: screen.blit(SfrontIdle_006,(self.x - worldx,self.y - worldy))
                        elif int(self.animateCounter) == 7: screen.blit(SfrontIdle_007,(self.x - worldx,self.y - worldy))
                        elif int(self.animateCounter) == 8: screen.blit(SfrontIdle_008,(self.x - worldx,self.y - worldy))
                        elif int(self.animateCounter) == 9: screen.blit(SfrontIdle_009,(self.x - worldx,self.y - worldy))
                        elif int(self.animateCounter) == 10: screen.blit(SfrontIdle_010,(self.x - worldx,self.y - worldy))
                        elif int(self.animateCounter) == 11: screen.blit(SfrontIdle_011,(self.x - worldx,self.y - worldy))
                        elif int(self.animateCounter) == 12: screen.blit(SfrontIdle_012,(self.x - worldx,self.y - worldy))
                        elif int(self.animateCounter) == 13: screen.blit(SfrontIdle_013,(self.x - worldx,self.y - worldy))
                        elif int(self.animateCounter) == 14: screen.blit(SfrontIdle_014,(self.x - worldx,self.y - worldy))
                        elif int(self.animateCounter) == 15: screen.blit(SfrontIdle_015,(self.x - worldx,self.y - worldy))
                        elif int(self.animateCounter) == 16: screen.blit(SfrontIdle_016,(self.x - worldx,self.y - worldy))
               
                        elif int(self.animateCounter) == 17:
                                screen.blit(SfrontIdle_017,(self.x - worldx,self.y - worldy)) 
                                self.blinkCounter += 1

                                if self.blinkCounter == 10:
                                    self.blinking = True
                
                    elif self.blinking == True:#front IdleBlinking
                
                        if int(self.animateCounter) == 0: screen.blit(SfrontIdleBlinking_000,(self.x - worldx, self.y - worldy))
                        elif int(self.animateCounter) == 1: screen.blit(SfrontIdleBlinking_001,(self.x - worldx, self.y - worldy))
                        elif int(self.animateCounter) == 2: screen.blit(SfrontIdleBlinking_002,(self.x - worldx, self.y - worldy))
                        elif int(self.animateCounter) == 3: screen.blit(SfrontIdleBlinking_003,(self.x - worldx, self.y - worldy))
                        elif int(self.animateCounter) == 4: screen.blit(SfrontIdleBlinking_004,(self.x - worldx, self.y - worldy))
                        elif int(self.animateCounter) == 5: screen.blit(SfrontIdleBlinking_005,(self.x - worldx, self.y - worldy))
                        elif int(self.animateCounter) == 6: screen.blit(SfrontIdleBlinking_006,(self.x - worldx, self.y - worldy))
                        elif int(self.animateCounter) == 7: screen.blit(SfrontIdleBlinking_007,(self.x - worldx, self.y - worldy))
                        elif int(self.animateCounter) == 8: screen.blit(SfrontIdleBlinking_008,(self.x - worldx, self.y - worldy))
                        elif int(self.animateCounter) == 9: screen.blit(SfrontIdleBlinking_009,(self.x - worldx, self.y - worldy))
                        elif int(self.animateCounter) == 10: screen.blit(SfrontIdleBlinking_010,(self.x - worldx, self.y - worldy))
                        elif int(self.animateCounter) == 11: screen.blit(SfrontIdleBlinking_011,(self.x - worldx, self.y - worldy))
                        elif int(self.animateCounter) == 12: screen.blit(SfrontIdleBlinking_012,(self.x - worldx, self.y - worldy))
                        elif int(self.animateCounter) == 13: screen.blit(SfrontIdleBlinking_013,(self.x - worldx, self.y - worldy))
                        elif int(self.animateCounter) == 14: screen.blit(SfrontIdleBlinking_014,(self.x - worldx, self.y - worldy))
                        elif int(self.animateCounter) == 15: screen.blit(SfrontIdleBlinking_015,(self.x - worldx, self.y - worldy))
                        elif int(self.animateCounter) == 16: screen.blit(SfrontIdleBlinking_016,(self.x - worldx, self.y - worldy))
                        elif int(self.animateCounter) == 17:
                            screen.blit(SfrontIdleBlinking_017,(self.x - worldx, self.y - worldy))
                            self.blinkCounter = 0
                            self.blinking = False

                elif self.animate == 1: #front Walking
                    if int(self.animateCounter) == 0: screen.blit(SfrontWalking_000,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 1: screen.blit(SfrontWalking_001,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 2: screen.blit(SfrontWalking_002,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 3: screen.blit(SfrontWalking_003,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 4: screen.blit(SfrontWalking_004,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 5: screen.blit(SfrontWalking_005,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 6: screen.blit(SfrontWalking_006,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 7: screen.blit(SfrontWalking_007,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 8: screen.blit(SfrontWalking_008,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 9: screen.blit(SfrontWalking_009,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 10: screen.blit(SfrontWalking_010,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 11: screen.blit(SfrontWalking_011,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 12: screen.blit(SfrontWalking_012,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 13: screen.blit(SfrontWalking_013,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 14: screen.blit(SfrontWalking_014,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 15: screen.blit(SfrontWalking_015,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 16: screen.blit(SfrontWalking_016,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 17: screen.blit(SfrontWalking_017,(self.x - worldx, self.y - worldy))

                elif self.animate == 2:#front Attack
                    if int(self.animateCounter) == 0: screen.blit(SfrontSlashing_000,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 1: screen.blit(SfrontSlashing_001,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 2: screen.blit(SfrontSlashing_002,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 3: screen.blit(SfrontSlashing_003,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 4: screen.blit(SfrontSlashing_004,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 5: screen.blit(SfrontSlashing_005,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 6: screen.blit(SfrontSlashing_006,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 7: screen.blit(SfrontSlashing_007,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 8: screen.blit(SfrontSlashing_008,(self.x - worldx, self.y - worldy))

                    if self.Tile not in self.frontBorder:
                        self.attackedTile = self.Tile + 20
    

            elif self.direction == 1: #Right

                if self.animate == 0: #right Idle
                    if self.blinking == False:
                        if int(self.animateCounter) == 0: screen.blit(SrightIdle_000,(self.x - worldx, self.y - worldy))
                        elif int(self.animateCounter) == 1: screen.blit(SrightIdle_001,(self.x - worldx, self.y - worldy))
                        elif int(self.animateCounter) == 2: screen.blit(SrightIdle_002,(self.x - worldx, self.y - worldy))
                        elif int(self.animateCounter) == 3: screen.blit(SrightIdle_003,(self.x - worldx, self.y - worldy))
                        elif int(self.animateCounter) == 4: screen.blit(SrightIdle_004,(self.x - worldx, self.y - worldy))
                        elif int(self.animateCounter) == 5: screen.blit(SrightIdle_005,(self.x - worldx, self.y - worldy))
                        elif int(self.animateCounter) == 6: screen.blit(SrightIdle_006,(self.x - worldx, self.y - worldy))
                        elif int(self.animateCounter) == 7: screen.blit(SrightIdle_007,(self.x - worldx, self.y - worldy))
                        elif int(self.animateCounter) == 8: screen.blit(SrightIdle_008,(self.x - worldx, self.y - worldy))
                        elif int(self.animateCounter) == 9: screen.blit(SrightIdle_009,(self.x - worldx, self.y - worldy))
                        elif int(self.animateCounter) == 10: screen.blit(SrightIdle_010,(self.x - worldx, self.y - worldy))
                        elif int(self.animateCounter) == 11: screen.blit(SrightIdle_011,(self.x - worldx, self.y - worldy))
                        elif int(self.animateCounter) == 12: screen.blit(SrightIdle_012,(self.x - worldx, self.y - worldy))
                        elif int(self.animateCounter) == 13: screen.blit(SrightIdle_013,(self.x - worldx, self.y - worldy))
                        elif int(self.animateCounter) == 14: screen.blit(SrightIdle_014,(self.x - worldx, self.y - worldy))
                        elif int(self.animateCounter) == 15: screen.blit(SrightIdle_015,(self.x - worldx, self.y - worldy))
                        elif int(self.animateCounter) == 16: screen.blit(SrightIdle_016,(self.x - worldx, self.y - worldy))
                    
                        elif int(self.animateCounter) == 17: #switch to blinking
                            screen.blit(SrightIdle_017,(self.x - worldx, self.y - worldy)) 
                            self.blinkCounter += 1

                            if self.blinkCounter == 10:
                                self.blinking = True
                
                    elif self.blinking == True:#right IdleBlinking
                
                        if int(self.animateCounter) == 0: screen.blit(SrightIdleBlinking_000,(self.x - worldx, self.y - worldy))
                        elif int(self.animateCounter) == 1: screen.blit(SrightIdleBlinking_001,(self.x - worldx, self.y - worldy))
                        elif int(self.animateCounter) == 2: screen.blit(SrightIdleBlinking_002,(self.x - worldx, self.y - worldy))
                        elif int(self.animateCounter) == 3: screen.blit(SrightIdleBlinking_003,(self.x - worldx, self.y - worldy))
                        elif int(self.animateCounter) == 4: screen.blit(SrightIdleBlinking_004,(self.x - worldx, self.y - worldy))
                        elif int(self.animateCounter) == 5: screen.blit(SrightIdleBlinking_005,(self.x - worldx, self.y - worldy))
                        elif int(self.animateCounter) == 6: screen.blit(SrightIdleBlinking_006,(self.x - worldx, self.y - worldy))
                        elif int(self.animateCounter) == 7: screen.blit(SrightIdleBlinking_007,(self.x - worldx, self.y - worldy))
                        elif int(self.animateCounter) == 8: screen.blit(SrightIdleBlinking_008,(self.x - worldx, self.y - worldy))
                        elif int(self.animateCounter) == 9: screen.blit(SrightIdleBlinking_009,(self.x - worldx, self.y - worldy))
                        elif int(self.animateCounter) == 10: screen.blit(SrightIdleBlinking_010,(self.x - worldx, self.y - worldy))
                        elif int(self.animateCounter) == 11: screen.blit(SrightIdleBlinking_011,(self.x - worldx, self.y - worldy))
                        elif int(self.animateCounter) == 12: screen.blit(SrightIdleBlinking_012,(self.x - worldx, self.y - worldy))
                        elif int(self.animateCounter) == 13: screen.blit(SrightIdleBlinking_013,(self.x - worldx, self.y - worldy))
                        elif int(self.animateCounter) == 14: screen.blit(SrightIdleBlinking_014,(self.x - worldx, self.y - worldy))
                        elif int(self.animateCounter) == 15: screen.blit(SrightIdleBlinking_015,(self.x - worldx, self.y - worldy))
                        elif int(self.animateCounter) == 16: screen.blit(SrightIdleBlinking_016,(self.x - worldx, self.y - worldy))
                        elif int(self.animateCounter) == 17:
                            screen.blit(SrightIdleBlinking_017,(self.x - worldx, self.y - worldy))
                            self.blinkCounter = 0
                            self.blinking = False
                

                elif self.animate == 1: #right Walking
                    if int(self.animateCounter) == 0: screen.blit(SrightWalking_000,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 1: screen.blit(SrightWalking_001,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 2: screen.blit(SrightWalking_002,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 3: screen.blit(SrightWalking_003,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 4: screen.blit(SrightWalking_004,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 5: screen.blit(SrightWalking_005,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 6: screen.blit(SrightWalking_006,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 7: screen.blit(SrightWalking_007,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 8: screen.blit(SrightWalking_008,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 9: screen.blit(SrightWalking_009,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 10: screen.blit(SrightWalking_010,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 11: screen.blit(SrightWalking_011,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 12: screen.blit(SrightWalking_012,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 13: screen.blit(SrightWalking_013,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 14: screen.blit(SrightWalking_014,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 15: screen.blit(SrightWalking_015,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 16: screen.blit(SrightWalking_016,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 17: screen.blit(SrightWalking_017,(self.x - worldx, self.y - worldy))

                elif self.animate == 2:#right Attack
                    if int(self.animateCounter) == 0: screen.blit(SrightSlashing_000,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 1: screen.blit(SrightSlashing_001,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 2: screen.blit(SrightSlashing_002,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 3: screen.blit(SrightSlashing_003,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 4: screen.blit(SrightSlashing_004,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 5: screen.blit(SrightSlashing_005,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 6: screen.blit(SrightSlashing_006,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 7: screen.blit(SrightSlashing_007,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 8: screen.blit(SrightSlashing_008,(self.x - worldx, self.y - worldy))

                    if self.Tile not in self.rightBorder:
                        self.attackedTile = self.Tile + 1

            elif self.direction == 2: #Back

                if self.animate == 0:#back Idle
                    if int(self.animateCounter) == 0: screen.blit(SbackIdle_000,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 1: screen.blit(SbackIdle_001,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 2: screen.blit(SbackIdle_002,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 3: screen.blit(SbackIdle_003,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 4: screen.blit(SbackIdle_004,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 5: screen.blit(SbackIdle_005,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 6: screen.blit(SbackIdle_006,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 7: screen.blit(SbackIdle_007,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 8: screen.blit(SbackIdle_008,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 9: screen.blit(SbackIdle_009,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 10: screen.blit(SbackIdle_010,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 11: screen.blit(SbackIdle_011,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 12: screen.blit(SbackIdle_012,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 13: screen.blit(SbackIdle_013,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 14: screen.blit(SbackIdle_014,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 15: screen.blit(SbackIdle_015,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 16: screen.blit(SbackIdle_016,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 17: screen.blit(SbackIdle_017,(self.x - worldx, self.y - worldy))


                elif self.animate == 1:#back Walking
                    if int(self.animateCounter) == 0: screen.blit(SbackWalking_000,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 1: screen.blit(SbackWalking_001,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 2: screen.blit(SbackWalking_002,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 3: screen.blit(SbackWalking_003,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 4: screen.blit(SbackWalking_004,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 5: screen.blit(SbackWalking_005,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 6: screen.blit(SbackWalking_006,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 7: screen.blit(SbackWalking_007,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 8: screen.blit(SbackWalking_008,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 9: screen.blit(SbackWalking_009,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 10: screen.blit(SbackWalking_010,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 11: screen.blit(SbackWalking_011,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 12: screen.blit(SbackWalking_012,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 13: screen.blit(SbackWalking_013,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 14: screen.blit(SbackWalking_014,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 15: screen.blit(SbackWalking_015,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 16: screen.blit(SbackWalking_016,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 17: screen.blit(SbackWalking_017,(self.x - worldx, self.y - worldy))

                elif self.animate == 2:#back Attack
                    if int(self.animateCounter) == 0: screen.blit(SbackSlashing_000,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 1: screen.blit(SbackSlashing_001,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 2: screen.blit(SbackSlashing_002,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 3: screen.blit(SbackSlashing_003,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 4: screen.blit(SbackSlashing_004,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 5: screen.blit(SbackSlashing_005,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 6: screen.blit(SbackSlashing_006,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 7: screen.blit(SbackSlashing_007,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 8: screen.blit(SbackSlashing_008,(self.x - worldx, self.y - worldy))
                
                    if self.Tile not in self.backBorder:
                        self.attackedTile = self.Tile - 20

            elif self.direction == 3: #Left

                if self.animate == 0: #left Idle
                    if self.blinking == False:#left IdleBlinking
                        if int(self.animateCounter) == 0: screen.blit(SleftIdle_000,(self.x - worldx, self.y - worldy))
                        elif int(self.animateCounter) == 1: screen.blit(SleftIdle_001,(self.x - worldx, self.y - worldy))
                        elif int(self.animateCounter) == 2: screen.blit(SleftIdle_002,(self.x - worldx, self.y - worldy))
                        elif int(self.animateCounter) == 3: screen.blit(SleftIdle_003,(self.x - worldx, self.y - worldy))
                        elif int(self.animateCounter) == 4: screen.blit(SleftIdle_004,(self.x - worldx, self.y - worldy))
                        elif int(self.animateCounter) == 5: screen.blit(SleftIdle_005,(self.x - worldx, self.y - worldy))
                        elif int(self.animateCounter) == 6: screen.blit(SleftIdle_006,(self.x - worldx, self.y - worldy))
                        elif int(self.animateCounter) == 7: screen.blit(SleftIdle_007,(self.x - worldx, self.y - worldy))
                        elif int(self.animateCounter) == 8: screen.blit(SleftIdle_008,(self.x - worldx, self.y - worldy))
                        elif int(self.animateCounter) == 9: screen.blit(SleftIdle_009,(self.x - worldx, self.y - worldy))
                        elif int(self.animateCounter) == 10: screen.blit(SleftIdle_010,(self.x - worldx, self.y - worldy))
                        elif int(self.animateCounter) == 11: screen.blit(SleftIdle_011,(self.x - worldx, self.y - worldy))
                        elif int(self.animateCounter) == 12: screen.blit(SleftIdle_012,(self.x - worldx, self.y - worldy))
                        elif int(self.animateCounter) == 13: screen.blit(SleftIdle_013,(self.x - worldx, self.y - worldy))
                        elif int(self.animateCounter) == 14: screen.blit(SleftIdle_014,(self.x - worldx, self.y - worldy))
                        elif int(self.animateCounter) == 15: screen.blit(SleftIdle_015,(self.x - worldx, self.y - worldy))
                        elif int(self.animateCounter) == 16: screen.blit(SleftIdle_016,(self.x - worldx, self.y - worldy))
                        elif int(self.animateCounter) == 17: #switch to blinking
                                screen.blit(SleftIdle_017,(self.x - worldx, self.y - worldy)) 
                                self.blinkCounter += 1

                                if self.blinkCounter == 10:
                                    self.blinking = True
                
                    elif self.blinking == True:#left IdleBlinking
                
                        if int(self.animateCounter) == 0: screen.blit(SleftIdleBlinking_000,(self.x - worldx, self.y - worldy))
                        elif int(self.animateCounter) == 1: screen.blit(SleftIdleBlinking_001,(self.x - worldx, self.y - worldy))
                        elif int(self.animateCounter) == 2: screen.blit(SleftIdleBlinking_002,(self.x - worldx, self.y - worldy))
                        elif int(self.animateCounter) == 3: screen.blit(SleftIdleBlinking_003,(self.x - worldx, self.y - worldy))
                        elif int(self.animateCounter) == 4: screen.blit(SleftIdleBlinking_004,(self.x - worldx, self.y - worldy))
                        elif int(self.animateCounter) == 5: screen.blit(SleftIdleBlinking_005,(self.x - worldx, self.y - worldy))
                        elif int(self.animateCounter) == 6: screen.blit(SleftIdleBlinking_006,(self.x - worldx, self.y - worldy))
                        elif int(self.animateCounter) == 7: screen.blit(SleftIdleBlinking_007,(self.x - worldx, self.y - worldy))
                        elif int(self.animateCounter) == 8: screen.blit(SleftIdleBlinking_008,(self.x - worldx, self.y - worldy))
                        elif int(self.animateCounter) == 9: screen.blit(SleftIdleBlinking_009,(self.x - worldx, self.y - worldy))
                        elif int(self.animateCounter) == 10: screen.blit(SleftIdleBlinking_010,(self.x - worldx, self.y - worldy))
                        elif int(self.animateCounter) == 11: screen.blit(SleftIdleBlinking_011,(self.x - worldx, self.y - worldy))
                        elif int(self.animateCounter) == 12: screen.blit(SleftIdleBlinking_012,(self.x - worldx, self.y - worldy))
                        elif int(self.animateCounter) == 13: screen.blit(SleftIdleBlinking_013,(self.x - worldx, self.y - worldy))
                        elif int(self.animateCounter) == 14: screen.blit(SleftIdleBlinking_014,(self.x - worldx, self.y - worldy))
                        elif int(self.animateCounter) == 15: screen.blit(SleftIdleBlinking_015,(self.x - worldx, self.y - worldy))
                        elif int(self.animateCounter) == 16: screen.blit(SleftIdleBlinking_016,(self.x - worldx, self.y - worldy))
                        elif int(self.animateCounter) == 17:
                            screen.blit(SleftIdleBlinking_017,(self.x - worldx, self.y - worldy))
                            self.blinkCounter = 0
                            self.blinking = False
                

                elif self.animate == 1: #left Walking
                    if int(self.animateCounter) == 0: screen.blit(SleftWalking_000,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 1: screen.blit(SleftWalking_001,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 2: screen.blit(SleftWalking_002,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 3: screen.blit(SleftWalking_003,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 4: screen.blit(SleftWalking_004,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 5: screen.blit(SleftWalking_005,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 6: screen.blit(SleftWalking_006,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 7: screen.blit(SleftWalking_007,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 8: screen.blit(SleftWalking_008,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 9: screen.blit(SleftWalking_009,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 10: screen.blit(SleftWalking_010,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 11: screen.blit(SleftWalking_011,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 12: screen.blit(SleftWalking_012,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 13: screen.blit(SleftWalking_013,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 14: screen.blit(SleftWalking_014,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 15: screen.blit(SleftWalking_015,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 16: screen.blit(SleftWalking_016,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 17: screen.blit(SleftWalking_017,(self.x - worldx, self.y - worldy))

                elif self.animate == 2:#left Attack
                    if int(self.animateCounter) == 0: screen.blit(SleftSlashing_000,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 1: screen.blit(SleftSlashing_001,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 2: screen.blit(SleftSlashing_002,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 3: screen.blit(SleftSlashing_003,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 4: screen.blit(SleftSlashing_004,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 5: screen.blit(SleftSlashing_005,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 6: screen.blit(SleftSlashing_006,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 7: screen.blit(SleftSlashing_007,(self.x - worldx, self.y - worldy))
                    elif int(self.animateCounter) == 8: screen.blit(SleftSlashing_008,(self.x - worldx, self.y - worldy))

                    if self.Tile not in self.leftBorder:
                        self.attackedTile = self.Tile - 1
              
    def movement(self):
        if self.alive == 1:
            safeTiles = [13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,33,34,35,36,37,38,80,81,82,83,87]

             #1-8 = actions
            #Left, Right, Up, Down#
            #Walk 1, Walk 3, Walk 3, Walk 4#

    #        if pressed[pygame.K_SPACE]  and self.walkCounter == 0 and self.attackCounter == 0 and self.attackDelay == 0: #attack
    #            self.animateCounter = 0
    #            self.attackCounter = 8
    #            self.attackDelay = 15
            if self.BasicAI <= 8:
                if self.BasicAI == 1 and self.walkCounter == 0 and self.attackCounter == 0:
                    self.direction = 0
                    if map[self.Tile + 20] in safeTiles and self.Tile not in self.frontBorder:
                        self.walkCounter = 16
                        self.Tile += 20

                elif self.BasicAI == 2 and self.walkCounter == 0 and self.attackCounter == 0:
                    self.direction = 1
                    if map[self.Tile + 1] in safeTiles and self.Tile not in self.rightBorder:
                        self.walkCounter = 16
                        self.Tile += 1

                elif self.BasicAI == 3 and self.walkCounter == 0 and self.attackCounter == 0:
                    self.direction = 2
                    if map[self.Tile - 20] in safeTiles and self.Tile not in self.backBorder:
                        self.walkCounter = 16
                        self.Tile -= 20

                elif self.BasicAI == 4 and self.walkCounter == 0 and self.attackCounter == 0:
                    self.direction = 3
                    if map[self.Tile - 1] in safeTiles and self.Tile not in self.leftBorder:
                        self.walkCounter = 16
                        self.Tile -= 1

            if self.walkCounter > 0:
                self.animate = 1
                if self.direction == 0: self.y = self.y + 4
                elif self.direction == 1: self.x = self.x + 4
                elif self.direction == 2: self.y = self.y - 4
                elif self.direction == 3: self.x = self.x - 4

                self.walkCounter = self.walkCounter - 1

                if self.walkCounter == 0: #maybe beef up this statement to check for "if moving" to clean up walk animation
                    self.animate = 0

                    self.BasicAI = random.randint(1,4)

                    global gameState
                    gameState = 0

            if self.attackCounter == 8: #play slash sound.
                slashSound.play()

            if self.attackCounter > 0:
                self.animate = 2
                self.attackCounter = self.attackCounter - 1
                if self.attackCounter == 0:
                    self.animate = 0
                    self.attackedTile = -1
            elif self.attackDelay > 0:
                self.attackDelay = self.attackDelay - 1

    def animateObject(self):
        if self.alive == 1:
            self.animateCounter += .5

            if int(self.animateCounter) == 18:
                self.animateCounter = 0

            if self.damagedTimer > 0:
                self.damagedTimer -= 1

    def checkDamage(self,playerAttack):
        if self.alive == 1:
            if self.Tile == playerAttack:
                if self.damagedTimer == 0: 
                    self.alive = 0
                    self.damagedTimer = 15
                    #print ("died")

    def checkAlive(self):
        return self.alive
    
    def getY(self):
        #return int(self.y / 64)
        #return int((self.y + 55)/ 64)
        return int(self.Tile / 20)

        #print(playerAttack, self.Tile)
##########################################################################################




###########################################
newTile = 0

map = [
51,51,51,51,51,51,51,58,56,54,56,59,51,51,51,51,51,52,21,21,
51,51,51,51,51,51,51,52,7,84,7,50,51,51,51,51,51,52,21,21,
51,51,51,51,51,51,51,52,11,85,11,50,51,51,51,51,51,60,48,49,
51,51,51,51,51,51,51,52,15,16,15,50,51,51,51,51,51,51,51,60,
51,51,51,51,51,51,51,52,21,21,21,50,51,51,51,51,51,51,51,51,
54,54,54,59,51,51,51,52,21,21,21,50,51,51,51,51,51,51,51,51,
6,6,6,50,51,51,51,52,21,21,21,53,54,54,59,51,51,51,51,51,
10,10,10,50,51,51,51,52,21,21,21,8,84,8,50,51,51,51,51,51,
16,16,16,50,51,51,51,52,21,21,21,12,85,12,50,51,51,51,51,51,
21,21,21,53,59,51,51,52,21,21,21,16,16,16,50,51,51,51,51,51,
21,21,21,6,53,59,51,60,48,48,48,48,48,48,61,51,51,51,51,51,
21,21,21,16,6,50,51,51,51,51,51,51,51,51,51,51,51,51,51,51,
]

map1 = [
51,51,51,51,51,51,51,58,56,54,56,59,51,51,51,51,51,52,21,21,
51,51,51,51,51,51,51,52,7,84,7,50,51,51,51,51,51,52,21,21,
51,51,51,51,51,51,51,52,11,85,11,50,51,51,51,51,51,60,48,49,
51,51,51,51,51,51,51,52,15,16,15,50,51,51,51,51,51,51,51,60,
51,51,51,51,51,51,51,52,21,21,21,50,51,51,51,51,51,51,51,51,
54,54,54,59,51,51,51,52,21,21,21,50,51,51,51,51,51,51,51,51,
6,6,6,50,51,51,51,52,21,21,21,53,54,54,59,51,51,51,51,51,
10,10,10,50,51,51,51,52,21,21,21,8,84,8,50,51,51,51,51,51,
16,16,16,50,51,51,51,52,21,21,21,12,85,12,50,51,51,51,51,51,
21,21,21,53,59,51,51,52,21,21,21,16,16,16,50,51,51,51,51,51,
21,21,21,6,53,59,51,60,48,48,48,48,48,48,61,51,51,51,51,51,
21,21,21,16,6,50,51,51,51,51,51,51,51,51,51,51,51,51,51,51,
]

map2 = [
51,51,51,58,54,56,54,56,54,56,54,56,54,59,51,51,51,51,51,51,
51,51,51,52,6,7,6,7,5,7,6,7,6,50,51,51,51,51,51,51,
51,51,51,52,9,11,9,11,9,11,9,11,9,50,51,51,51,51,51,51,
51,51,51,52,16,15,16,15,16,15,16,15,16,50,51,51,51,51,51,51,
51,51,51,52,21,21,21,21,21,21,21,21,21,50,51,51,51,51,51,51,
51,51,51,52,21,21,21,21,21,21,21,21,21,50,51,51,51,51,51,51,
51,51,51,52,21,21,21,21,21,21,21,21,21,50,51,51,51,51,51,51,
51,51,51,52,21,21,21,21,21,21,21,21,21,50,51,51,51,51,51,51,
51,51,51,52,21,21,21,21,21,21,21,21,21,50,51,51,51,51,51,51,
51,51,51,52,21,21,21,21,21,21,21,21,21,50,51,51,51,51,51,51,
51,51,51,60,48,48,48,49,21,47,48,48,48,61,51,51,51,51,51,51,
51,51,51,51,51,51,51,52,85,50,51,51,51,51,51,51,51,51,51,51,
]

map3 = [
51,51,51,51,51,51,58,54,54,54,54,54,54,54,59,51,51,51,51,51,
51,51,58,54,54,54,55,5,5,5,5,5,5,5,50,51,51,51,51,51,
51,51,52,7,84,7,5,10,10,10,10,10,10,10,50,51,51,51,51,51,
51,51,52,11,85,11,10,16,16,16,14,16,16,16,50,51,51,51,51,51,
51,51,52,15,13,15,16,24,26,26,26,26,27,26,50,51,51,51,51,51,
51,51,52,21,21,21,21,29,31,31,31,31,31,31,50,51,51,51,51,51,
51,51,52,22,21,21,21,29,44,44,44,44,44,44,50,51,51,51,51,51,
51,51,52,21,21,21,21,29,44,44,44,44,44,44,50,51,51,51,51,51,
51,51,60,49,85,47,48,48,48,48,48,48,48,48,61,51,51,51,51,51,
51,51,51,60,48,61,51,51,51,51,51,51,51,51,51,51,51,51,51,51,
51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,
51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,
]

map4 = [ #under construction...
58,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,59,
52,5,5,5,7,43,7,5,5,5,5,5,7,44,7,8,5,8,8,50,
52,9,9,9,11,43,11,9,9,9,9,9,11,44,11,12,12,9,9,50,
52,16,16,16,15,16,15,16,16,16,16,16,15,16,15,16,16,16,16,50,
52,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,53,
52,21,21,24,26,26,26,26,26,21,26,26,26,26,26,26,26,26,26,70,
52,21,21,29,30,31,31,31,31,21,31,31,31,31,31,31,31,31,31,31,
52,21,21,29,42,44,44,44,21,21,21,44,21,21,21,44,21,21,21,44,
52,21,21,29,42,44,44,44,21,21,21,26,21,21,21,26,21,21,21,44,
52,21,21,29,42,44,44,44,26,26,26,32,26,26,26,32,26,26,26,44,
52,21,21,29,42,44,44,44,32,32,32,44,32,32,32,44,32,32,32,44,
52,21,21,29,42,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,    
]

    #Draw Methods
def draw_Tile(i,layer,type):
    counter = i
    counter2 = layer

    i = map[i + (layer * 20)]

    global worldx
    global worldy

    if type == 0:

        if i == 51: #Added for optimization
            #screen.blit(tile_underground1_51,(counter * 64 - worldx, counter2 * 64 - worldy))
            pass

        elif i == 21: #ADDED FOR OPTIMIZATION
            screen.blit(tile_underground1_21,(counter * 64 - worldx, counter2 * 64 - worldy))

        elif i == 0:
            screen.blit(tile_underground1_0,(counter * 64 - worldx, counter2 * 64 - worldy))
        elif i == 1:
            screen.blit(tile_underground1_1,(counter * 64 - worldx, counter2 * 64 - worldy)) #overlay_tile
            #screen.blit(tile_underground1_87,(counter * 64, counter2 * 64))#87 is a unique tile used for the underlay of transparent walls.
            #screen.blit(tile_underground1_21,(counter * 64, counter2 * 64))
        elif i == 2:
            screen.blit(tile_underground1_2,(counter * 64 - worldx, counter2 * 64 - worldy)) #overlay_tile
            #screen.blit(tile_underground1_87,(counter * 64, counter2 * 64))#87 is a unique tile used for the underlay of transparent walls.
            #screen.blit(tile_underground1_21,(counter * 64, counter2 * 64))
        elif i == 3:
            screen.blit(tile_underground1_3,(counter * 64 - worldx, counter2 * 64 - worldy)) #overlay_tile
            #screen.blit(tile_underground1_87,(counter * 64, counter2 * 64))#87 is a unique tile used for the underlay of transparent walls.
            #screen.blit(tile_underground1_21,(counter * 64, counter2 * 64))
        elif i == 4:
            screen.blit(tile_underground1_4,(counter * 64 - worldx, counter2 * 64 - worldy)) #overlay_tile
            #screen.blit(tile_underground1_87,(counter * 64, counter2 * 64))#87 is a unique tile used for the underlay of transparent walls.
        elif i == 5:
            screen.blit(tile_underground1_5,(counter * 64 - worldx, counter2 * 64 - worldy))
        elif i == 6:
            screen.blit(tile_underground1_6,(counter * 64 - worldx, counter2 * 64 - worldy))
        elif i == 7:
            screen.blit(tile_underground1_7,(counter * 64 - worldx, counter2 * 64 - worldy))
        elif i == 8:
            screen.blit(tile_underground1_8,(counter * 64 - worldx, counter2 * 64 - worldy))
        elif i == 9:
            screen.blit(tile_underground1_9,(counter * 64 - worldx, counter2 * 64 - worldy))

        elif i == 10:
            screen.blit(tile_underground1_10,(counter * 64 - worldx, counter2 * 64 - worldy))
        elif i == 11:
            screen.blit(tile_underground1_11,(counter * 64 - worldx, counter2 * 64 - worldy))
        elif i == 12:
            screen.blit(tile_underground1_12,(counter * 64 - worldx, counter2 * 64 - worldy))
        elif i == 13:
            screen.blit(tile_underground1_13,(counter * 64 - worldx, counter2 * 64 - worldy))
        elif i == 14:
            screen.blit(tile_underground1_14,(counter * 64 - worldx, counter2 * 64 - worldy))
        elif i == 15:
            screen.blit(tile_underground1_15,(counter * 64 - worldx, counter2 * 64 - worldy))
        elif i == 16:
            screen.blit(tile_underground1_16,(counter * 64 - worldx, counter2 * 64 - worldy))
        elif i == 17:
            screen.blit(tile_underground1_17,(counter * 64 - worldx, counter2 * 64 - worldy))
        elif i == 18:
            screen.blit(tile_underground1_18,(counter * 64 - worldx, counter2 * 64 - worldy))
        elif i == 19:
            screen.blit(tile_underground1_19,(counter * 64 - worldx, counter2 * 64 - worldy))


        elif i == 20:
            screen.blit(tile_underground1_20,(counter * 64 - worldx, counter2 * 64 - worldy))
        elif i == 21:
            screen.blit(tile_underground1_21,(counter * 64 - worldx, counter2 * 64 - worldy))
        elif i == 22:
            screen.blit(tile_underground1_22,(counter * 64 - worldx, counter2 * 64 - worldy))
        elif i == 23:
            screen.blit(tile_underground1_23,(counter * 64 - worldx, counter2 * 64 - worldy))
        elif i == 24:
            screen.blit(tile_underground1_24,(counter * 64 - worldx, counter2 * 64 - worldy))
        elif i == 25:
            screen.blit(tile_underground1_25,(counter * 64 - worldx, counter2 * 64 - worldy))
        elif i == 26:
            screen.blit(tile_underground1_26,(counter * 64 - worldx, counter2 * 64 - worldy))
        elif i == 27:
            screen.blit(tile_underground1_27,(counter * 64 - worldx, counter2 * 64 - worldy))
        elif i == 28:
            screen.blit(tile_underground1_28,(counter * 64 - worldx, counter2 * 64 - worldy))
        elif i == 29:
            screen.blit(tile_underground1_29,(counter * 64 - worldx, counter2 * 64 - worldy))
            
        elif i == 30:
            screen.blit(tile_underground1_30,(counter * 64 - worldx, counter2 * 64 - worldy))
        elif i == 31:
            screen.blit(tile_underground1_31,(counter * 64 - worldx, counter2 * 64 - worldy))
        elif i == 32:
            screen.blit(tile_underground1_32,(counter * 64 - worldx, counter2 * 64 - worldy))
        elif i == 33:
            screen.blit(tile_underground1_33,(counter * 64 - worldx, counter2 * 64 - worldy))
        elif i == 34:
            screen.blit(tile_underground1_34,(counter * 64 - worldx, counter2 * 64 - worldy))
        elif i == 35:
            screen.blit(tile_underground1_35,(counter * 64 - worldx, counter2 * 64 - worldy))
        elif i == 36:
            screen.blit(tile_underground1_36,(counter * 64 - worldx, counter2 * 64 - worldy))
        elif i == 37:
            screen.blit(tile_underground1_37,(counter * 64 - worldx, counter2 * 64 - worldy))
        elif i == 38:
            screen.blit(tile_underground1_38,(counter * 64 - worldx, counter2 * 64 - worldy))
        elif i == 39:
            screen.blit(tile_underground1_39,(counter * 64 - worldx, counter2 * 64 - worldy))
            
        elif i == 40:
            screen.blit(tile_underground1_40,(counter * 64 - worldx, counter2 * 64 - worldy))
        elif i == 41:
            screen.blit(tile_underground1_41,(counter * 64 - worldx, counter2 * 64 - worldy))
        elif i == 42:
            screen.blit(tile_underground1_42,(counter * 64 - worldx, counter2 * 64 - worldy))
        elif i == 43:
            screen.blit(tile_underground1_43,(counter * 64 - worldx, counter2 * 64 - worldy))
        elif i == 44:
            screen.blit(tile_underground1_44,(counter * 64 - worldx, counter2 * 64 - worldy))
        elif i == 45:
            screen.blit(tile_underground1_45,(counter * 64 - worldx, counter2 * 64 - worldy))
        elif i == 46:
            screen.blit(tile_underground1_46,(counter * 64 - worldx, counter2 * 64 - worldy))
        elif i == 47:
            screen.blit(tile_underground1_47,(counter * 64 - worldx, counter2 * 64 - worldy)) #overlay_tile
            #screen.blit(tile_underground1_21,(counter * 64, counter2 * 64))
        elif i == 48:
            #screen.blit(tile_underground1_87,(counter * 64, counter2 * 64))#87 is a unique tile used for the underlay of transparent walls.
            screen.blit(tile_underground1_48,(counter * 64 - worldx, counter2 * 64 - worldy)) #overlay_tile
            #screen.blit(tile_underground1_21,(counter * 64, counter2 * 64))
        elif i == 49:
            screen.blit(tile_underground1_49,(counter * 64 - worldx, counter2 * 64 - worldy)) #overlay_tile
            #screen.blit(tile_underground1_21,(counter * 64, counter2 * 64))

        elif i == 50:
            screen.blit(tile_underground1_50,(counter * 64 - worldx, counter2 * 64 - worldy))
        elif i == 51:
            screen.blit(tile_underground1_51,(counter * 64 - worldx, counter2 * 64 - worldy))
        elif i == 52:
            screen.blit(tile_underground1_52,(counter * 64 - worldx, counter2 * 64 - worldy))
        elif i == 53:
            screen.blit(tile_underground1_53,(counter * 64 - worldx, counter2 * 64 - worldy))
        elif i == 54:
            screen.blit(tile_underground1_54,(counter * 64 - worldx, counter2 * 64 - worldy))
        elif i == 55:
            screen.blit(tile_underground1_55,(counter * 64 - worldx, counter2 * 64 - worldy))
        elif i == 56:
            screen.blit(tile_underground1_56,(counter * 64 - worldx, counter2 * 64 - worldy))
        elif i == 57:
            screen.blit(tile_underground1_57,(counter * 64 - worldx, counter2 * 64 - worldy))
            #screen.blit(tile_underground1_21,(counter * 64, counter2 * 64))#overlay_tile
        elif i == 58:
            screen.blit(tile_underground1_58,(counter * 64 - worldx, counter2 * 64 - worldy))
        elif i == 59:
            screen.blit(tile_underground1_59,(counter * 64 - worldx, counter2 * 64 - worldy))
            
        elif i == 60:
            screen.blit(tile_underground1_60,(counter * 64 - worldx, counter2 * 64 - worldy))
        elif i == 61:
            screen.blit(tile_underground1_61,(counter * 64 - worldx, counter2 * 64 - worldy))
        elif i == 62:
            screen.blit(tile_underground1_62,(counter * 64 - worldx, counter2 * 64 - worldy))
        elif i == 63:
            screen.blit(tile_underground1_63,(counter * 64 - worldx, counter2 * 64 - worldy))
        elif i == 64:
            screen.blit(tile_underground1_64,(counter * 64 - worldx, counter2 * 64 - worldy))
        elif i == 65:
            screen.blit(tile_underground1_65,(counter * 64 - worldx, counter2 * 64 - worldy))
        elif i == 66:
            #screen.blit(tile_underground1_87,(counter * 64, counter2 * 64))#87 is a unique tile used for the underlay of transparent walls.
            screen.blit(tile_underground1_66,(counter * 64 - worldx, counter2 * 64 - worldy))#overlay_tile
        elif i == 67:
            screen.blit(tile_underground1_67,(counter * 64 - worldx, counter2 * 64 - worldy))
        elif i == 68:
            screen.blit(tile_underground1_68,(counter * 64 - worldx, counter2 * 64 - worldy))
        elif i == 69:
            screen.blit(tile_underground1_69,(counter * 64 - worldx, counter2 * 64 - worldy))

        elif i == 70:
            screen.blit(tile_underground1_70,(counter * 64 - worldx, counter2 * 64 - worldy))
        elif i == 71:
            screen.blit(tile_underground1_71,(counter * 64 - worldx, counter2 * 64 - worldy))
        elif i == 72:
            screen.blit(tile_underground1_72,(counter * 64 - worldx, counter2 * 64 - worldy))#overlay_tile
            #screen.blit(tile_underground1_21,(counter * 64, counter2 * 64))
        elif i == 73:
            screen.blit(tile_underground1_73,(counter * 64 - worldx, counter2 * 64 - worldy))#overlay_tile
            #screen.blit(tile_underground1_21,(counter * 64, counter2 * 64))
        elif i == 74:
            screen.blit(tile_underground1_74,(counter * 64 - worldx, counter2 * 64 - worldy))
        elif i == 75:
            screen.blit(tile_underground1_75,(counter * 64 - worldx, counter2 * 64 - worldy))
        elif i == 76:
            screen.blit(tile_underground1_76,(counter * 64 - worldx, counter2 * 64 - worldy))
        elif i == 77:
            screen.blit(tile_underground1_77,(counter * 64 - worldx, counter2 * 64 - worldy))
        elif i == 78:
            screen.blit(tile_underground1_78,(counter * 64 - worldx, counter2 * 64 - worldy))
        elif i == 79:
            screen.blit(tile_underground1_21,(counter * 64, counter2 * 64 - worldy))
            #screen.blit(tile_underground1_79,(counter * 64, counter2 * 64))#overlay_tile

        elif i == 80:
            screen.blit(tile_underground1_80,(counter * 64 - worldx, counter2 * 64 - worldy))
        elif i == 81:
            screen.blit(tile_underground1_81,(counter * 64 - worldx, counter2 * 64 - worldy))
        elif i == 82:
            screen.blit(tile_underground1_82,(counter * 64 - worldx, counter2 * 64 - worldy))
        elif i == 83:
            screen.blit(tile_underground1_83,(counter * 64 - worldx, counter2 * 64 - worldy))

        elif i == 84: #Passage Tile
            screen.blit(tile_underground1_0,(counter * 64 - worldx, counter2 * 64 - worldy))  ##### Changed to 0 for visual overlay
        elif i == 85: #Passage Tile
            screen.blit(tile_underground1_85,(counter * 64 - worldx, counter2 * 64 - worldy))  
        elif i == 86:
            screen.blit(tile_underground1_86,(counter * 64 - worldx, counter2 * 64 - worldy))

    ######################################################
    #OVERWORLD#

        elif i == 87:
            screen.blit(tile_overworld1_1,(counter * 64 - worldx, counter2 * 64 - worldy))

        elif i == 88:
            screen.blit(tile_overworld1_2,(counter * 64 - worldx, counter2 * 64 - worldy))

        elif i == 89:
            screen.blit(tile_overworld1_3,(counter * 64 - worldx, counter2 * 64 - worldy))

        elif i == 90:
            screen.blit(tile_overworld1_4,(counter * 64 - worldx, counter2 * 64 - worldy))

        elif i == 91:
            screen.blit(tile_overworld1_5,(counter * 64 - worldx, counter2 * 64 - worldy))

        elif i == 92:
            screen.blit(tile_overworld1_6,(counter * 64 - worldx, counter2 * 64 - worldy))

        elif i == 93:
            screen.blit(tile_overworld1_7,(counter * 64 - worldx, counter2 * 64 - worldy))

        elif i == 94:
            screen.blit(tile_overworld1_8,(counter * 64 - worldx, counter2 * 64 - worldy))

        elif i == 95:
            screen.blit(tile_overworld1_9,(counter * 64 - worldx, counter2 * 64 - worldy))

        elif i == 96:
            screen.blit(tile_overworld1_10,(counter * 64 - worldx, counter2 * 64 - worldy))

        elif i == 97:
            screen.blit(tile_overworld1_11,(counter * 64 - worldx, counter2 * 64 - worldy))

        elif i == 98:
            screen.blit(tile_overworld1_50,(counter * 64 - worldx, counter2 * 64 - worldy))

        elif i == 99:
            screen.blit(tile_overworld1_51,(counter * 64 - worldx, counter2 * 64 - worldy))

        elif i == 100:
            screen.blit(tile_overworld1_52,(counter * 64 - worldx, counter2 * 64 - worldy))

        elif i == 101:
            screen.blit(tile_overworld1_53,(counter * 64 - worldx, counter2 * 64 - worldy))

        elif i == 102:
            screen.blit(tile_overworld1_54,(counter * 64 - worldx, counter2 * 64 - worldy))

        elif i == 103:
            screen.blit(tile_overworld1_55,(counter * 64 - worldx, counter2 * 64 - worldy))

        elif i == 104:
            screen.blit(tile_overworld1_56,(counter * 64 - worldx, counter2 * 64 - worldy))

        elif i == 105:
            screen.blit(tile_overworld1_57,(counter * 64 - worldx, counter2 * 64 - worldy))

        elif i == 106:
            screen.blit(tile_overworld1_58,(counter * 64 - worldx, counter2 * 64 - worldy))

        elif i == 107:
            screen.blit(tile_overworld1_59,(counter * 64 - worldx, counter2 * 64 - worldy))

        elif i == 108:
            screen.blit(tile_overworld1_60,(counter * 64 - worldx, counter2 * 64 - worldy))

        elif i == 109:
            screen.blit(tile_overworld1_61,(counter * 64 - worldx, counter2 * 64 - worldy))

        elif i == 110:
            screen.blit(tile_overworld1_62,(counter * 64 - worldx, counter2 * 64 - worldy))

        elif i == 111:
            screen.blit(tile_overworld1_63,(counter * 64 - worldx, counter2 * 64 - worldy))

        elif i == 112:
            screen.blit(tile_overworld1_64,(counter * 64 - worldx, counter2 * 64 - worldy))

        elif i == 113:
            screen.blit(tile_overworld1_65,(counter * 64 - worldx, counter2 * 64 - worldy))

        elif i == 114:
            screen.blit(tile_overworld1_66,(counter * 64 - worldx, counter2 * 64 - worldy))

        elif i == 115:
            screen.blit(tile_overworld1_67,(counter * 64 - worldx, counter2 * 64 - worldy))

        elif i == 116:
            screen.blit(tile_overworld1_68,(counter * 64 - worldx, counter2 * 64 - worldy))

        elif i == 117:
            screen.blit(tile_overworld1_69,(counter * 64 - worldx, counter2 * 64 - worldy))

        elif i == 118:
            screen.blit(tile_overworld1_70,(counter * 64 - worldx, counter2 * 64 - worldy))

        elif i == 119:
            screen.blit(tile_overworld1_71,(counter * 64 - worldx, counter2 * 64 - worldy))

        elif i == 120:
            screen.blit(tile_overworld1_72,(counter * 64 - worldx, counter2 * 64 - worldy))

        elif i == 121:
            screen.blit(tile_overworld1_73,(counter * 64 - worldx, counter2 * 64 - worldy))

###################

    elif type == 1:

        #
        if i == 84: #Passage Tile
            screen.blit(tile_underground1_84,(counter * 64 - worldx, counter2 * 64 - worldy))
    
    counter += 1
    if counter == 20:
        counter = 0

def teleport(teleportTile):
    global map
    global map1
    global map2
    global map3
    global FloorLevel

    if FloorLevel == 1:
        if teleportTile == 69:
            map = map2
            FloorLevel = 2
            P.teleport(208)

        elif teleportTile == 192:
            map = map3
            FloorLevel = 3
            P.teleport(144)

    elif FloorLevel == 2:
        if teleportTile == 208:
            map = map1
            FloorLevel = 1
            P.teleport(69)

    elif FloorLevel == 3:
        if teleportTile == 144:
            map = map1
            FloorLevel = 1
            P.teleport(192)
        
        if teleportTile == 84:
            map = map4
            FloorLevel = 1
            P.teleport (65)


playMenu = True
while playMenu == True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            #quit()
            sys.exit()

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_ESCAPE]:
       pygame.display.quit()
       pygame.quit() 

    if pressed[pygame.K_SPACE]:
        playMenu = False

    #StartMenu image
    screen.blit(StartMenu,(0,0))

    pygame.display.update()

##########################################################################################
playGame = True
while playGame == True: #Main Menu

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            #quit()
            sys.exit()

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_ESCAPE]:
       pygame.display.quit()
       pygame.quit()

##########################################################################################

##########################################################################################

    #Search1
    EnableMapEditor = False
    if EnableMapEditor == True:
        mousexy = pygame.mouse.get_pos()
        mousex = mousexy[0] / 64
        mousey = mousexy[1] / 64
    
        mouseTile = (int(mousex) + (int(mousey)* 20))

        screen.blit(tile_underground1_1,(1290                 ,0))
        screen.blit(tile_underground1_2,(1290 + 64 + 5        ,0))
        screen.blit(tile_underground1_3,(1290 + (64 * 2) + 10 ,0))
        screen.blit(tile_underground1_4,(1290 + (64 * 3) + 15 ,0))

        screen.blit(tile_underground1_5,(1290                 , 64 + 5))
        screen.blit(tile_underground1_6,(1290 + 64 + 5        , 64 + 5))
        screen.blit(tile_underground1_7,(1290 + (64 * 2) + 10 , 64 + 5))
        screen.blit(tile_underground1_8,(1290 + (64 * 3) + 15 , 64 + 5))

        screen.blit(tile_underground1_9,(1290                  , (64 * 2) + 10))
        screen.blit(tile_underground1_10,(1290 + 64 + 5        , (64 * 2) + 10))
        screen.blit(tile_underground1_11,(1290 + (64 * 2) + 10 , (64 * 2) + 10))
        screen.blit(tile_underground1_12,(1290 + (64 * 3) + 15 , (64 * 2) + 10))

        screen.blit(tile_underground1_13,(1290                 , (64 * 3) + 15))
        screen.blit(tile_underground1_14,(1290 + 64 + 5        , (64 * 3) + 15))
        screen.blit(tile_underground1_15,(1290 + (64 * 2) + 10 , (64 * 3) + 15))
        screen.blit(tile_underground1_16,(1290 + (64 * 3) + 15 , (64 * 3) + 15))

        screen.blit(tile_underground1_17,(1290                 , (64 * 4) + 20))
        screen.blit(tile_underground1_18,(1290 + 64 + 5        , (64 * 4) + 20))
        screen.blit(tile_underground1_19,(1290 + (64 * 2) + 10 , (64 * 4) + 20))
        screen.blit(tile_underground1_20,(1290 + (64 * 3) + 15 , (64 * 4) + 20))

        screen.blit(tile_underground1_21,(1290                 , (64 * 5) + 25))
        screen.blit(tile_underground1_22,(1290 + 64 + 5        , (64 * 5) + 25))
        screen.blit(tile_underground1_23,(1290 + (64 * 2) + 10 , (64 * 5) + 25))
        screen.blit(tile_underground1_24,(1290 + (64 * 3) + 15 , (64 * 5) + 25))

        screen.blit(tile_underground1_25,(1290                 , (64 * 6) + 30))
        screen.blit(tile_underground1_26,(1290 + 64 + 5        , (64 * 6) + 30))
        screen.blit(tile_underground1_27,(1290 + (64 * 2) + 10 , (64 * 6) + 30))
        screen.blit(tile_underground1_28,(1290 + (64 * 3) + 15 , (64 * 6) + 30))

        screen.blit(tile_underground1_29,(1290                 , (64 * 7) + 35))
        screen.blit(tile_underground1_33,(1290 + 64 + 5        , (64 * 7) + 35))
        screen.blit(tile_underground1_34,(1290 + (64 * 2) + 10 , (64 * 7) + 35))
        screen.blit(tile_underground1_35,(1290 + (64 * 3) + 15 , (64 * 7) + 35))

        screen.blit(tile_underground1_36,(1290                 , (64 * 8) + 40))
        screen.blit(tile_underground1_37,(1290 + 64 + 5        , (64 * 8) + 40))
        screen.blit(tile_underground1_38,(1290 + (64 * 2) + 10 , (64 * 8) + 40))

        screen.blit(tile_underground1_30,(1290                 , (64 * 9) + 45))
        screen.blit(tile_underground1_31,(1290 + 64 + 5        , (64 * 9) + 45))
        screen.blit(tile_underground1_32,(1290 + (64 * 2) + 10 , (64 * 9) + 45))

        screen.blit(tile_underground1_42,(1290                 , (64 * 10) + 50))
        screen.blit(tile_underground1_43,(1290 + 64 + 5        , (64 * 10) + 50))
        screen.blit(tile_underground1_44,(1290 + (64 * 2) + 10 , (64 * 10) + 50))

        screen.blit(tile_underground1_80,(1290                 , (64 * 11) + 55))
        screen.blit(tile_underground1_81,(1290 + 64 + 5        , (64 * 11) + 55))
        screen.blit(tile_underground1_82,(1290 + (64 * 2) + 10 , (64 * 11) + 55))
        screen.blit(tile_underground1_83,(1290 + (64 * 3) + 15 , (64 * 11) + 55))


        ### More tiles. (Column Next)

        screen.blit(tile_underground1_39,(1576                 ,0))
        screen.blit(tile_underground1_40,(1576 + 64 + 5        ,0))
        screen.blit(tile_underground1_41,(1576 + (64 * 2) + 10 ,0))

        screen.blit(tile_underground1_45,(1576                 ,64 + 5))
        screen.blit(tile_underground1_46,(1576 + 64 + 5        ,64 + 5))
        screen.blit(tile_underground1_47,(1576 + (64 * 2) + 10 ,64 + 5))

        screen.blit(tile_underground1_48,(1576                  , (64 * 2) + 10))
        screen.blit(tile_underground1_49,(1576 + 64 + 5        , (64 * 2) + 10))
        screen.blit(tile_underground1_50,(1576 + (64 * 2) + 10 , (64 * 2) + 10))

        screen.blit(tile_underground1_51,(1576                 , (64 * 3) + 15))
        screen.blit(tile_underground1_52,(1576 + 64 + 5        , (64 * 3) + 15))
        screen.blit(tile_underground1_53,(1576 + (64 * 2) + 10 , (64 * 3) + 15))

        screen.blit(tile_underground1_54,(1576                 , (64 * 4) + 20))
        screen.blit(tile_underground1_55,(1576 + 64 + 5        , (64 * 4) + 20))
        screen.blit(tile_underground1_56,(1576 + (64 * 2) + 10 , (64 * 4) + 20))

        screen.blit(tile_underground1_57,(1576                 , (64 * 5) + 25))
        screen.blit(tile_underground1_58,(1576 + 64 + 5        , (64 * 5) + 25))
        screen.blit(tile_underground1_59,(1576 + (64 * 2) + 10 , (64 * 5) + 25))

        screen.blit(tile_underground1_60,(1576                 , (64 * 6) + 30))
        screen.blit(tile_underground1_61,(1576 + 64 + 5        , (64 * 6) + 30))
        screen.blit(tile_underground1_62,(1576 + (64 * 2) + 10 , (64 * 6) + 30))

        screen.blit(tile_underground1_63,(1576                 , (64 * 7) + 35))
        screen.blit(tile_underground1_64,(1576 + 64 + 5        , (64 * 7) + 35))
        screen.blit(tile_underground1_65,(1576 + (64 * 2) + 10 , (64 * 7) + 35))

        screen.blit(tile_underground1_66,(1576                 , (64 * 8) + 40))
        screen.blit(tile_underground1_67,(1576 + 64 + 5        , (64 * 8) + 40))
        screen.blit(tile_underground1_68,(1576 + (64 * 2) + 10 , (64 * 8) + 40))

        screen.blit(tile_underground1_69,(1576                 , (64 * 9) + 45))
        screen.blit(tile_underground1_70,(1576 + 64 + 5        , (64 * 9) + 45))
        screen.blit(tile_underground1_71,(1576 + (64 * 2) + 10 , (64 * 9) + 45))

        screen.blit(tile_underground1_72,(1576                 , (64 * 10) + 50))
        screen.blit(tile_underground1_73,(1576 + 64 + 5        , (64 * 10) + 50))
        screen.blit(tile_underground1_74,(1576 + (64 * 2) + 10 , (64 * 10) + 50))

        screen.blit(tile_underground1_75,(1576                 , (64 * 11) + 55))
        screen.blit(tile_underground1_76,(1576 + 64 + 5        , (64 * 11) + 55))
        screen.blit(tile_underground1_77,(1576 + (64 * 2) + 10 , (64 * 11) + 55))

        screen.blit(tile_underground1_78,(1576                 , (64 * 12) + 60))
        screen.blit(tile_underground1_79,(1576 + 64 + 5        , (64 * 12) + 60))
        screen.blit(tile_underground1_84,(1576 + (64 * 2) + 10 , (64 * 12) + 60))#jump


        if pygame.mouse.get_pressed()[0]:
            if mousexy[0] > 1280 and mousexy[0] < 1566: ##using these to help with less "if" statements (chunking them out)
                if mousexy[1] > 0 and mousexy[1] < 69:#coulmn 1
                    if mousexy[0] > 1290 and mousexy[0] < 1359:
                        selectedTile = 1
                    elif mousexy[0] > 1359 and mousexy[0] < 1428:
                        selectedTile = 2
                    elif mousexy[0] > 1428 and mousexy[0] < 1497:
                        selectedTile = 3
                    elif mousexy[0] > 1497 and mousexy[0] < 1566:
                        selectedTile = 4

                elif mousexy[1] > 69 and mousexy[1] < 143: #column 2
                    if mousexy[0] > 1290 and mousexy[0] < 1359:
                        selectedTile = 5
                    elif mousexy[0] > 1359 and mousexy[0] < 1428:
                        selectedTile = 6
                    elif mousexy[0] > 1428 and mousexy[0] < 1497:
                        selectedTile = 7
                    elif mousexy[0] > 1497 and mousexy[0] < 1566:
                        selectedTile = 8

                elif mousexy[1] > 143 and mousexy[1] < 212: #column 3
                    if mousexy[0] > 1290 and mousexy[0] < 1359:
                        selectedTile = 9
                    elif mousexy[0] > 1359 and mousexy[0] < 1428:
                        selectedTile = 10
                    elif mousexy[0] > 1428 and mousexy[0] < 1497:
                        selectedTile = 11
                    elif mousexy[0] > 1497 and mousexy[0] < 1566:
                        selectedTile = 12

                elif mousexy[1] > 212 and mousexy[1] < 281: #column 4
                    if mousexy[0] > 1290 and mousexy[0] < 1359:
                        selectedTile = 13
                    elif mousexy[0] > 1359 and mousexy[0] < 1428:
                        selectedTile = 14
                    elif mousexy[0] > 1428 and mousexy[0] < 1497:
                        selectedTile = 15
                    elif mousexy[0] > 1497 and mousexy[0] < 1566:
                        selectedTile = 16

                elif mousexy[1] > 281 and mousexy[1] < 350: #column 5
                    if mousexy[0] > 1290 and mousexy[0] < 1359:
                        selectedTile = 17
                    elif mousexy[0] > 1359 and mousexy[0] < 1428:
                        selectedTile = 18
                    elif mousexy[0] > 1428 and mousexy[0] < 1497:
                        selectedTile = 19
                    elif mousexy[0] > 1497 and mousexy[0] < 1566:
                        selectedTile = 20

                elif mousexy[1] > 350 and mousexy[1] < 419: #column 6
                    if mousexy[0] > 1290 and mousexy[0] < 1359:
                        selectedTile = 21
                    elif mousexy[0] > 1359 and mousexy[0] < 1428:
                        selectedTile = 22
                    elif mousexy[0] > 1428 and mousexy[0] < 1497:
                        selectedTile = 23
                    elif mousexy[0] > 1497 and mousexy[0] < 1566:
                        selectedTile = 24

                elif mousexy[1] > 419 and mousexy[1] < 488: #column 7
                    if mousexy[0] > 1290 and mousexy[0] < 1359:
                        selectedTile = 25
                    elif mousexy[0] > 1359 and mousexy[0] < 1428:
                        selectedTile = 26
                    elif mousexy[0] > 1428 and mousexy[0] < 1497:
                        selectedTile = 27
                    elif mousexy[0] > 1497 and mousexy[0] < 1566:
                        selectedTile = 28

                elif mousexy[1] > 488 and mousexy[1] < 577: #column 8
                    if mousexy[0] > 1290 and mousexy[0] < 1359:
                        selectedTile = 29
                    elif mousexy[0] > 1359 and mousexy[0] < 1428:
                        selectedTile = 33
                    elif mousexy[0] > 1428 and mousexy[0] < 1497:
                        selectedTile = 34
                    elif mousexy[0] > 1497 and mousexy[0] < 1566:
                        selectedTile = 35
                    

                elif mousexy[1] > 577 and mousexy[1] < 626: #column 9
                    if mousexy[0] > 1290 and mousexy[0] < 1359:
                        selectedTile = 36
                    elif mousexy[0] > 1359 and mousexy[0] < 1428:
                        selectedTile = 37
                    elif mousexy[0] > 1428 and mousexy[0] < 1497:
                        selectedTile = 38

                elif mousexy[1] > 626 and mousexy[1] < 695: #column 10
                    if mousexy[0] > 1290 and mousexy[0] < 1359:
                        selectedTile = 30
                    elif mousexy[0] > 1359 and mousexy[0] < 1428:
                        selectedTile = 31
                    elif mousexy[0] > 1428 and mousexy[0] < 1497:
                        selectedTile = 32

                elif mousexy[1] > 695 and mousexy[1] < 764: #column 11
                    if mousexy[0] > 1290 and mousexy[0] < 1359:
                        selectedTile = 42
                    elif mousexy[0] > 1359 and mousexy[0] < 1428:
                        selectedTile = 43
                    elif mousexy[0] > 1428 and mousexy[0] < 1497:
                        selectedTile = 44

            elif mousexy[0] > 1566 and mousexy[0] < 1780: ##using these to help with less "if" statements (chunking them out) ######################## *1*
                if mousexy[1] > 0 and mousexy[1] < 69:#coulmn 1
                    if mousexy[0] > 1290 + 286 and mousexy[0] < 1359  + 286:
                        selectedTile = 39
                    elif mousexy[0] > 1359 + 286 and mousexy[0] < 1428 + 286:
                        selectedTile = 40
                    elif mousexy[0] > 1428 + 286 and mousexy[0] < 1497 + 286:
                        selectedTile = 41

                elif mousexy[1] > 69 and mousexy[1] < 143: #column 2
                    if mousexy[0] > 1290 + 286 and mousexy[0] < 1359 + 286:
                        selectedTile = 45
                    elif mousexy[0] > 1359 + 286 and mousexy[0] < 1428 + 286:
                        selectedTile = 46
                    elif mousexy[0] > 1428 + 286 and mousexy[0] < 1497+ 286:
                        selectedTile = 47

                elif mousexy[1] > 143 and mousexy[1] < 212: #column 3
                    if mousexy[0] > 1290 + 286 and mousexy[0] < 1359 + 286:
                        selectedTile = 48
                    elif mousexy[0] > 1359 + 286 and mousexy[0] < 1428+ 286:
                        selectedTile = 49
                    elif mousexy[0] > 1428 + 286 and mousexy[0] < 1497+ 286:
                        selectedTile = 50

                elif mousexy[1] > 212 and mousexy[1] < 281: #column 4
                    if mousexy[0] > 1290 + 286 and mousexy[0] < 1359 + 286:
                        selectedTile = 51
                    elif mousexy[0] > 1359 + 286 and mousexy[0] < 1428 + 286:
                        selectedTile = 52
                    elif mousexy[0] > 1428 + 286 and mousexy[0] < 1497 + 286:
                        selectedTile = 53

                elif mousexy[1] > 281 and mousexy[1] < 350: #column 5
                    if mousexy[0] > 1290 + 286 and mousexy[0] < 1359 + 286:
                        selectedTile = 54
                    elif mousexy[0] > 1359 + 286 and mousexy[0] < 1428 + 286:
                        selectedTile = 55
                    elif mousexy[0] > 1428 + 286 and mousexy[0] < 1497 + 286:
                        selectedTile = 56

                elif mousexy[1] > 350 and mousexy[1] < 419: #column 6
                    if mousexy[0] > 1290 + 286 and mousexy[0] < 1359 + 286:
                        selectedTile = 57
                    elif mousexy[0] > 1359 + 286 and mousexy[0] < 1428 + 286:
                        selectedTile = 58
                    elif mousexy[0] > 1428 + 286 and mousexy[0] < 1497 + 286:
                        selectedTile = 59

                elif mousexy[1] > 419 and mousexy[1] < 488: #column 7
                    if mousexy[0] > 1290 + 286 and mousexy[0] < 1359 + 286:
                        selectedTile = 60
                    elif mousexy[0] > 1359 + 286 and mousexy[0] < 1428 + 286:
                        selectedTile = 61
                    elif mousexy[0] > 1428 + 286 and mousexy[0] < 1497 + 286:
                        selectedTile = 62

                elif mousexy[1] > 488 and mousexy[1] < 577: #column 8
                    if mousexy[0] > 1290 + 286 and mousexy[0] < 1359 + 286:
                        selectedTile = 63
                    elif mousexy[0] > 1359 + 286 and mousexy[0] < 1428 + 286:
                        selectedTile = 64
                    elif mousexy[0] > 1428 + 286 and mousexy[0] < 1497 + 286:
                        selectedTile = 65

                elif mousexy[1] > 577 and mousexy[1] < 626: #column 9
                    if mousexy[0] > 1290 + 286 and mousexy[0] < 1359 + 286:
                        selectedTile = 66
                    elif mousexy[0] > 1359 + 286 and mousexy[0] < 1428 + 286:
                        selectedTile = 67
                    elif mousexy[0] > 1428 + 286 and mousexy[0] < 1497 + 286:
                        selectedTile = 68

                elif mousexy[1] > 626 and mousexy[1] < 695: #column 10
                    if mousexy[0] > 1290 + 286 and mousexy[0] < 1359 + 286:
                        selectedTile = 69
                    elif mousexy[0] > 1359 + 286 and mousexy[0] < 1428 + 286:
                        selectedTile = 70
                    elif mousexy[0] > 1428 + 286 and mousexy[0] < 1497 + 286:
                        selectedTile = 71

                elif mousexy[1] > 695 and mousexy[1] < 764: #column 11
                    if mousexy[0] > 1290 + 286 and mousexy[0] < 1359 + 286:
                        selectedTile = 72
                    elif mousexy[0] > 1359 + 286 and mousexy[0] < 1428 + 286:
                        selectedTile = 73
                    elif mousexy[0] > 1428 + 286 and mousexy[0] < 1497 + 286:
                        selectedTile = 74

                elif mousexy[1] > 764 and mousexy[1] < 833: #column 12
                    if mousexy[0] > 1290 + 286 and mousexy[0] < 1359 + 286:
                        selectedTile = 75
                    elif mousexy[0] > 1359 + 286 and mousexy[0] < 1428 + 286:
                        selectedTile = 76
                    elif mousexy[0] > 1428 + 286 and mousexy[0] < 1497 + 286:
                        selectedTile = 77

                elif mousexy[1] > 833 and mousexy[1] < 902: #column 13
                    if mousexy[0] > 1290 + 286 and mousexy[0] < 1359 + 286:
                        selectedTile = 78
                    elif mousexy[0] > 1359 + 286 and mousexy[0] < 1428 + 286:
                        selectedTile = 79
                    elif mousexy[0] > 1428 + 286 and mousexy[0] < 1497 + 286:
                        selectedTile = 84

            elif mousexy[0] < 1280 and mousexy[1] < 920:
                try:
                    map[mouseTile] = selectedTile
                except:
                    pass

        #Old Method of changing Tiles
        if pressed[pygame.K_6]:
            if map[mouseTile] < 121:
                map[mouseTile] = map[mouseTile] + 1
                pygame.time.delay(100)

        elif pressed[pygame.K_4]:
            if map[mouseTile] > 0:
                map[mouseTile] = map[mouseTile] - 1
                pygame.time.delay(100)


#SAVE FUNCTION#
        if (pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL])  and pressed[pygame.K_s]:
            text_file = open("editor.txt","w")

            txtCounter = 0
            for i in range(12):
                text_file.write( str(map[txtCounter])+ ',' + 
                                 str(map[txtCounter + 1]) + ',' +
                                 str(map[txtCounter + 2]) + ',' +
                                 str(map[txtCounter + 3]) + ',' +
                                 str(map[txtCounter + 4]) + ',' +
                                 str(map[txtCounter + 5]) + ',' +
                                 str(map[txtCounter + 6]) + ',' +
                                 str(map[txtCounter + 7]) + ',' +
                                 str(map[txtCounter + 8]) + ',' +
                                 str(map[txtCounter + 9]) + ',' +
                                 str(map[txtCounter + 10])+ ',' + 
                                 str(map[txtCounter + 11]) + ',' +
                                 str(map[txtCounter + 12]) + ',' +
                                 str(map[txtCounter + 13]) + ',' +
                                 str(map[txtCounter + 14]) + ',' +
                                 str(map[txtCounter + 15]) + ',' +
                                 str(map[txtCounter + 16]) + ',' +
                                 str(map[txtCounter + 17]) + ',' +
                                 str(map[txtCounter + 18]) + ',' +
                                 str(map[txtCounter + 19]) + ',\n')
                txtCounter += 20
            print ("SAVED THE MAP!")
            pygame.time.delay(100)
##########################################################################################
    def drawMap():
        global sk
        global s1
        global P
    ##############################
        #Create an array for each possible enemy#

        #NPC[0,1,2,3,4,5,6,7,8,9,10... etc]

        #use this for the drawing and spawning and dying of enemies / NPC's#

        #sort by y pos. draw by y pos. //
        drawZ = [sk.getY() , "sk.draw()",s1.getY() , "s1.draw()", P.getY() , "P.draw()"]

        #DRAW UNDERLAYER #START OUT THE DRAWING WITH THE TOP MOST
        for i in range(20):
            draw_Tile(i,0,0)
    

        #DRAW UNDERLAYER
        for i in range(20):
            draw_Tile(i,1,0)

        if drawZ[0] == 0: #NEED TO CHECK IF THE obj IS ALIVE OR NOT!
            eval(drawZ[1])#Uses the DrawZ to know what to draw in each order.
        if drawZ[2] == 0:
            eval(drawZ[3])
        if drawZ[4] == 0:
            eval(drawZ[5])

        #DRAW OVERLAYER
        for i in range(20):
            draw_Tile(i,0,1)

     ########################################################################################   
        #DRAW UNDERLAYER
        for i in range(20):
            draw_Tile(i,2,0)

        if drawZ[0] == 1:
            eval(drawZ[1])
        if drawZ[2] == 1:
            eval(drawZ[3])
        if drawZ[4] == 1:
            eval(drawZ[5])

        #DRAW OVERLAYER
        for i in range(20):
            draw_Tile(i,1,1)

    ########################################################################################
        #DRAW UNDERLAYER
        for i in range(20):
            draw_Tile(i,3,0)

        if drawZ[0] == 2:
            eval(drawZ[1])
        if drawZ[2] == 2:
            eval(drawZ[3])
        if drawZ[4] == 2:
            eval(drawZ[5])

        #DRAW OVERLAYER
        for i in range(20):
            draw_Tile(i,2,1)

     ########################################################################################   
        #DRAW UNDERLAYER
        for i in range(20):
            draw_Tile(i,4,0)

        if drawZ[0] == 3:
            eval(drawZ[1])
        if drawZ[2] == 3:
            eval(drawZ[3])
        if drawZ[4] == 3:
            eval(drawZ[5])

        #DRAW OVERLAYER
        for i in range(20):
            draw_Tile(i,3,1)

     ########################################################################################    
         #DRAW UNDERLAYER
        for i in range(20):
            draw_Tile(i,5,0)

        if drawZ[0] == 4:
            eval(drawZ[1])
        if drawZ[2] == 4:
            eval(drawZ[3])
        if drawZ[4] == 4:
            eval(drawZ[5])

        #DRAW OVERLAYER
        for i in range(20):
            draw_Tile(i,4,1)

     ########################################################################################
         #DRAW UNDERLAYER
        for i in range(20):
            draw_Tile(i,6,0) 

        if drawZ[0] == 5:
            eval(drawZ[1])
        if drawZ[2] == 5:
            eval(drawZ[3])
        if drawZ[4] == 5:
            eval(drawZ[5])

        #DRAW OVERLAYER
        for i in range(20):
            draw_Tile(i,5,1)

     ########################################################################################    
         #DRAW UNDERLAYER
        for i in range(20):
            draw_Tile(i,7,0)

        if drawZ[0] == 6:
            eval(drawZ[1])
        if drawZ[2] == 6:
            eval(drawZ[3])
        if drawZ[4] == 6:
            eval(drawZ[5])

        #DRAW OVERLAYER
        for i in range(20):
            draw_Tile(i,6,1)

     ########################################################################################    
         #DRAW UNDERLAYER
        for i in range(20):
            draw_Tile(i,8,0)

        if drawZ[0] == 7:
            eval(drawZ[1])
        if drawZ[2] == 7:
            eval(drawZ[3])
        if drawZ[4] == 7:
            eval(drawZ[5])

        #DRAW OVERLAYER
        for i in range(20):
            draw_Tile(i,7,1)
     ########################################################################################    
         #DRAW UNDERLAYER
        for i in range(20):
            draw_Tile(i,9,0)

        if drawZ[0] == 8:
            eval(drawZ[1])
        if drawZ[2] == 8:
            eval(drawZ[3])
        if drawZ[4] == 8:
            eval(drawZ[5])

        #DRAW OVERLAYER
        for i in range(20):
            draw_Tile(i,8,1)

     ########################################################################################    
        #DRAW UNDERLAYER
        for i in range(20):
            draw_Tile(i,10,0)

        if drawZ[0] == 9:
            eval(drawZ[1])
        if drawZ[2] == 9:
            eval(drawZ[3])
        if drawZ[4] == 9:
            eval(drawZ[5])

        #DRAW OVERLAYER
        for i in range(20):
            draw_Tile(i,9,1)

        #DRAW UNDERLAYER
        for i in range(20):
            draw_Tile(i,11,0)

        #DRAW OVERLAYER
        for i in range(20):
            draw_Tile(i,10,1)

        #DRAW UNDERLAYER? Overlay? (all the comments may be backwards for the overlay underlay ^
        for i in range(20):
            draw_Tile(i,11,1)

        ## lower map draw character 1 (extra addition...)

        if drawZ[0] == 10:
            eval(drawZ[1])
        if drawZ[2] == 10:
            eval(drawZ[3])
        if drawZ[4] == 10:
            eval(drawZ[5])

        ## lower map draw character 1 (extra addition...)

        if drawZ[0] == 11:
            eval(drawZ[1])
        if drawZ[2] == 11:
            eval(drawZ[3])
        if drawZ[4] == 11:
            eval(drawZ[5])

##########################################################################################
   
        
##########################################################################################
    if oneTime == True:

        sk = Skeleton((64 * 8) -32,64 * 3,0)
        s1 = Skeleton((64 * 8) -32,64 * 8,2)
        P = Player()
        
        #pygame.mixer.music.load('mainMusic.mp3')
        #pygame.mixer.music.play(-1)

        oneTime = False
    
    if gameState == 0:

        P.movement()
        P.getAttack()

    elif gameState == 1:

        sk.movement()
        s1.movement()

        


    drawMap()
    P.animateObject()
    sk.animateObject()
    s1.animateObject()

    #Check to see if any damage happens
    sk.checkDamage(P.getAttack()) 
    s1.checkDamage(P.getAttack())

    playerPos = P.getPos()
    playerX = playerPos[0]
    playerY = playerPos[1]
    

    #Darkness layer looks good but is very laggy...
    if darknessCounter >= 0 and darknessCounter < 4: screen.blit(darkness000,(playerX + 64 - 1280,playerY + 64 - 720))
    elif darknessCounter >= 4 and darknessCounter < 8: screen.blit(darkness001,(playerX + 64 - 1280,playerY + 64 - 720))
    elif darknessCounter >= 8 and darknessCounter < 12: screen.blit(darkness002,(playerX + 64 - 1280,playerY + 64 - 720))
    elif darknessCounter >= 12 and darknessCounter < 16: screen.blit(darkness001,(playerX + 64 - 1280,playerY + 64 - 720))

    darknessCounter += 1
    
    if darknessCounter == 16:
        darknessCounter = 0
        
    screen.blit(heartImage,(1280 - 50, 0))
    screen.blit(heartImage,(1280 - 40 - 50, 0))
    screen.blit(heartImage,(1280 - 80 - 50, 0))

    if ItemPick == 0:
        screen.blit(ItemBoxSword, (1280 - (84/2) -64 , 50))
    elif ItemPick == 1:
        screen.blit(ItemBoxFishing, (1280 - (84/2) -64 , 50))

    if P.getFishing_cast() == True:
        screen.blit(fishingLine_000,(playerX -32,playerY +64))

    fps = font.render("FPS: " + str(int(clock.get_fps())), True, pygame.Color('white'))

    screen.blit(fps, (50, 50))

    textHover = "BEN"

    text_width, text_height = font.size(str(textHover))
    message = font.render(str(textHover), True, pygame.Color('white'))
    centeredText = (576 + 64 - (text_width / 2))
    screen.blit(message, (centeredText, 246))

    pygame.display.update()

    screen.fill((40,37,34))

##########################################################################################
    clock.tick(30)
