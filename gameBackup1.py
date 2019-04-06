#October Dare 10/7/2018 - 48 Hour Challenge
import pygame, os
pygame.init()
os.environ['SDL_VIDEO_WINDOW_POS'] = str(50) + "," + str(50)

screen = pygame.display.set_mode((640,480))
clock = pygame.time.Clock()

#Load Images#
backgroundImage = pygame.image.load('blackBackground.png')
tile_1 = pygame.image.load('Tile (1).png')
tile_2 = pygame.image.load('Tile (2).png')
tile_3 = pygame.image.load('Tile (3).png')
tile_4 = pygame.image.load('Tile (4).png')
tile_5 = pygame.image.load('Tile (5).png')
tile_6 = pygame.image.load('Tile (6).png')
tile_7 = pygame.image.load('Tile (7).png')
tile_8 = pygame.image.load('Tile (8).png')
tile_9 = pygame.image.load('Tile (9).png')

tile_10 = pygame.image.load('Tile (10).png')
tile_11 = pygame.image.load('Tile (11).png')
tile_12 = pygame.image.load('Tile (12).png')
tile_13 = pygame.image.load('Tile (13).png')
tile_14 = pygame.image.load('Tile (14).png')
tile_15 = pygame.image.load('Tile (15).png')
tile_16 = pygame.image.load('Tile (16).png')
tile_17 = pygame.image.load('Tile (17).png')
tile_18 = pygame.image.load('Tile (18).png')
tile_19 = pygame.image.load('Tile (19).png')

tile_20 = pygame.image.load('Tile (20).png')
tile_21 = pygame.image.load('Tile (21).png')
tile_22 = pygame.image.load('Tile (22).png')
tile_23 = pygame.image.load('Tile (23).png')
tile_24 = pygame.image.load('Tile (24).png')
tile_25 = pygame.image.load('Tile (25).png')
tile_26 = pygame.image.load('Tile (26).png')
tile_27 = pygame.image.load('Tile (27).png')
tile_28 = pygame.image.load('Tile (28).png')
tile_29 = pygame.image.load('Tile (29).png')

tile_30 = pygame.image.load('Tile (30).png')
tile_31 = pygame.image.load('Tile (31).png')
tile_32 = pygame.image.load('Tile (32).png')
tile_33 = pygame.image.load('Tile (33).png')
tile_34 = pygame.image.load('Tile (34).png')
tile_35 = pygame.image.load('Tile (35).png')
tile_36 = pygame.image.load('Tile (36).png')
tile_37 = pygame.image.load('Tile (37).png')
tile_38 = pygame.image.load('Tile (38).png')
tile_39 = pygame.image.load('Tile (39).png')

tile_40 = pygame.image.load('Tile (40).png')
tile_41 = pygame.image.load('Tile (41).png')
tile_42 = pygame.image.load('Tile (42).png')
tile_43 = pygame.image.load('Tile (43).png')
tile_44 = pygame.image.load('Tile (44).png')
tile_45 = pygame.image.load('Tile (45).png')
tile_46 = pygame.image.load('Tile (46).png')
tile_47 = pygame.image.load('Tile (47).png')
tile_48 = pygame.image.load('Tile (48).png')
tile_49 = pygame.image.load('Tile (49).png')

tile_50 = pygame.image.load('Tile (50).png')
tile_51 = pygame.image.load('Tile (51).png')
tile_52 = pygame.image.load('Tile (52).png')
tile_53 = pygame.image.load('Tile (53).png')
tile_54 = pygame.image.load('Tile (54).png')
tile_55 = pygame.image.load('Tile (55).png')
tile_56 = pygame.image.load('Tile (56).png')
tile_57 = pygame.image.load('Tile (57).png')
tile_58 = pygame.image.load('Tile (58).png')
tile_59 = pygame.image.load('Tile (59).png')

tile_60 = pygame.image.load('Tile (60).png')
tile_61 = pygame.image.load('Tile (61).png')
tile_62 = pygame.image.load('Tile (62).png')
tile_63 = pygame.image.load('Tile (63).png')
tile_64 = pygame.image.load('Tile (64).png')
tile_65 = pygame.image.load('Tile (65).png')
tile_66 = pygame.image.load('Tile (66).png')
tile_67 = pygame.image.load('Tile (67).png')
tile_68 = pygame.image.load('Tile (68).png')
tile_69 = pygame.image.load('Tile (69).png')

tile_70 = pygame.image.load('Tile (70).png')
tile_71 = pygame.image.load('Tile (71).png')
tile_72 = pygame.image.load('Tile (72).png')
tile_73 = pygame.image.load('Tile (73).png')
tile_74 = pygame.image.load('Tile (74).png')
tile_75 = pygame.image.load('Tile (75).png')
tile_76 = pygame.image.load('Tile (76).png')
tile_77 = pygame.image.load('Tile (77).png')
tile_78 = pygame.image.load('Tile (78).png')
tile_79 = pygame.image.load('Tile (79).png')

tile_80 = pygame.image.load('Tile (80).png')
tile_81 = pygame.image.load('Tile (81).png')
tile_82 = pygame.image.load('Tile (82).png')
tile_83 = pygame.image.load('Tile (83).png')

playGame = True
while playGame == True:

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            sys.exit()

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_ESCAPE]:
       pygame.display.quit()
       pygame.quit()

##########################################################################################

    map = [  7, 6, 7, 6, 7, 7, 6, 7, 6, 7,
            11, 9,11, 9,11,11, 9,11, 9,11,
            15,16,15,16,15,15,16,15,13,15,
            39,39,39,39,39,39,39,39,39,39,
            21,22,23,24,25,26,27,28,29,52,
            31,32,33,34,51,51,51,38,39,52,
            41,42,43,44,51,51,51,48,49,52]

##########################################################################################
    #Draw Methods
    screen.blit(backgroundImage,(0,0))

    counter = 0
    counter2 = 0
    for i in map:
        if i == 1:
            screen.blit(tile_1,(counter * 64, counter2 * 64))
        elif i == 2:
            screen.blit(tile_2,(counter * 64, counter2 * 64))
        elif i == 3:
            screen.blit(tile_3,(counter * 64, counter2 * 64))
        elif i == 4:
            screen.blit(tile_4,(counter * 64, counter2 * 64))
        elif i == 5:
            screen.blit(tile_5,(counter * 64, counter2 * 64))
        elif i == 6:
            screen.blit(tile_6,(counter * 64, counter2 * 64))
        elif i == 7:
            screen.blit(tile_7,(counter * 64, counter2 * 64))
        elif i == 8:
            screen.blit(tile_8,(counter * 64, counter2 * 64))
        elif i == 9:
            screen.blit(tile_9,(counter * 64, counter2 * 64))

        elif i == 10:
            screen.blit(tile_10,(counter * 64, counter2 * 64))
        elif i == 11:
            screen.blit(tile_11,(counter * 64, counter2 * 64))
        elif i == 12:
            screen.blit(tile_12,(counter * 64, counter2 * 64))
        elif i == 13:
            screen.blit(tile_13,(counter * 64, counter2 * 64))
        elif i == 14:
            screen.blit(tile_14,(counter * 64, counter2 * 64))
        elif i == 15:
            screen.blit(tile_15,(counter * 64, counter2 * 64))
        elif i == 16:
            screen.blit(tile_16,(counter * 64, counter2 * 64))
        elif i == 17:
            screen.blit(tile_17,(counter * 64, counter2 * 64))
        elif i == 18:
            screen.blit(tile_18,(counter * 64, counter2 * 64))
        elif i == 19:
            screen.blit(tile_19,(counter * 64, counter2 * 64))


        elif i == 20:
            screen.blit(tile_20,(counter * 64, counter2 * 64))
        elif i == 21:
            screen.blit(tile_21,(counter * 64, counter2 * 64))
        elif i == 22:
            screen.blit(tile_22,(counter * 64, counter2 * 64))
        elif i == 23:
            screen.blit(tile_23,(counter * 64, counter2 * 64))
        elif i == 24:
            screen.blit(tile_24,(counter * 64, counter2 * 64))
        elif i == 25:
            screen.blit(tile_25,(counter * 64, counter2 * 64))
        elif i == 26:
            screen.blit(tile_26,(counter * 64, counter2 * 64))
        elif i == 27:
            screen.blit(tile_27,(counter * 64, counter2 * 64))
        elif i == 28:
            screen.blit(tile_28,(counter * 64, counter2 * 64))
        elif i == 29:
            screen.blit(tile_29,(counter * 64, counter2 * 64))
            
        elif i == 30:
            screen.blit(tile_30,(counter * 64, counter2 * 64))
        elif i == 31:
            screen.blit(tile_31,(counter * 64, counter2 * 64))
        elif i == 32:
            screen.blit(tile_32,(counter * 64, counter2 * 64))
        elif i == 33:
            screen.blit(tile_33,(counter * 64, counter2 * 64))
        elif i == 34:
            screen.blit(tile_34,(counter * 64, counter2 * 64))
        elif i == 35:
            screen.blit(tile_35,(counter * 64, counter2 * 64))
        elif i == 36:
            screen.blit(tile_36,(counter * 64, counter2 * 64))
        elif i == 37:
            screen.blit(tile_37,(counter * 64, counter2 * 64))
        elif i == 38:
            screen.blit(tile_38,(counter * 64, counter2 * 64))
        elif i == 39:
            screen.blit(tile_39,(counter * 64, counter2 * 64))
            
        elif i == 40:
            screen.blit(tile_40,(counter * 64, counter2 * 64))
        elif i == 41:
            screen.blit(tile_41,(counter * 64, counter2 * 64))
        elif i == 42:
            screen.blit(tile_42,(counter * 64, counter2 * 64))
        elif i == 43:
            screen.blit(tile_43,(counter * 64, counter2 * 64))
        elif i == 44:
            screen.blit(tile_44,(counter * 64, counter2 * 64))
        elif i == 45:
            screen.blit(tile_45,(counter * 64, counter2 * 64))
        elif i == 46:
            screen.blit(tile_46,(counter * 64, counter2 * 64))
        elif i == 47:
            screen.blit(tile_47,(counter * 64, counter2 * 64))
        elif i == 48:
            screen.blit(tile_48,(counter * 64, counter2 * 64))
        elif i == 49:
            screen.blit(tile_49,(counter * 64, counter2 * 64))

        elif i == 50:
            screen.blit(tile_50,(counter * 64, counter2 * 64))
        elif i == 51:
            screen.blit(tile_51,(counter * 64, counter2 * 64))
        elif i == 52:
            screen.blit(tile_52,(counter * 64, counter2 * 64))
        elif i == 53:
            screen.blit(tile_53,(counter * 64, counter2 * 64))
        elif i == 54:
            screen.blit(tile_54,(counter * 64, counter2 * 64))
        elif i == 55:
            screen.blit(tile_55,(counter * 64, counter2 * 64))
        elif i == 56:
            screen.blit(tile_56,(counter * 64, counter2 * 64))
        elif i == 57:
            screen.blit(tile_57,(counter * 64, counter2 * 64))
        elif i == 58:
            screen.blit(tile_58,(counter * 64, counter2 * 64))
        elif i == 59:
            screen.blit(tile_59,(counter * 64, counter2 * 64))
            
        elif i == 60:
            screen.blit(tile_60,(counter * 64, counter2 * 64))
        elif i == 61:
            screen.blit(tile_61,(counter * 64, counter2 * 64))
        elif i == 62:
            screen.blit(tile_62,(counter * 64, counter2 * 64))
        elif i == 63:
            screen.blit(tile_63,(counter * 64, counter2 * 64))
        elif i == 64:
            screen.blit(tile_64,(counter * 64, counter2 * 64))
        elif i == 65:
            screen.blit(tile_65,(counter * 64, counter2 * 64))
        elif i == 66:
            screen.blit(tile_66,(counter * 64, counter2 * 64))
        elif i == 67:
            screen.blit(tile_67,(counter * 64, counter2 * 64))
        elif i == 68:
            screen.blit(tile_68,(counter * 64, counter2 * 64))
        elif i == 69:
            screen.blit(tile_69,(counter * 64, counter2 * 64))

        elif i == 70:
            screen.blit(tile_70,(counter * 64, counter2 * 64))
        elif i == 71:
            screen.blit(tile_71,(counter * 64, counter2 * 64))
        elif i == 72:
            screen.blit(tile_72,(counter * 64, counter2 * 64))
        elif i == 73:
            screen.blit(tile_73,(counter * 64, counter2 * 64))
        elif i == 74:
            screen.blit(tile_74,(counter * 64, counter2 * 64))
        elif i == 75:
            screen.blit(tile_75,(counter * 64, counter2 * 64))
        elif i == 76:
            screen.blit(tile_76,(counter * 64, counter2 * 64))
        elif i == 77:
            screen.blit(tile_77,(counter * 64, counter2 * 64))
        elif i == 78:
            screen.blit(tile_78,(counter * 64, counter2 * 64))
        elif i == 79:
            screen.blit(tile_79,(counter * 64, counter2 * 64))

        elif i == 80:
            screen.blit(tile_80,(counter * 64, counter2 * 64))
        elif i == 81:
            screen.blit(tile_81,(counter * 64, counter2 * 64))
        elif i == 82:
            screen.blit(tile_82,(counter * 64, counter2 * 64))
        elif i == 83:
            screen.blit(tile_83,(counter * 64, counter2 * 64))
       
        counter += 1
        if counter == 10:
            counter2 += 1
            counter = 0
    
    pygame.display.update()

##########################################################################################

    clock.tick(60)
