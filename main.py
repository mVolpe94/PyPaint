# draw mouse trail

import pygame, math

WINDOW = pygame.display.set_mode((500,450))

running = 1

BLUE_TRAIL = []
RED_TRAIL  = []
GREEN_TRAIL = []
YELLOW_TRAIL = []
MAGENTA_TRAIL = []
ORANGE_TRAIL = []



paint_mode = 1
index = paint_mode -1
paint_color = (255,255,255)



paint = True
while running:



    pygame.draw.rect(WINDOW, (50,40,40), (0,0,40,450))
    pygame.draw.rect(WINDOW, (255,0,0), (0,20,40,40))
    pygame.draw.rect(WINDOW, (0,255,0), (0,70,40,40))
    pygame.draw.rect(WINDOW, (0,100,200), (0,120,40,40))
    pygame.draw.rect(WINDOW, (255,255,0), (0,170,40,40))
    pygame.draw.rect(WINDOW, (128,0,128), (0,220,40,40))
    pygame.draw.rect(WINDOW, (255,69,0), (0,270,40,40))



    def draw_trail(color):
        paint_color = color
        for line in BLUE_TRAIL:
            pygame.draw.circle(WINDOW, (0,100,200), (line[0], line[1]), paint_mode, index)
        for line in RED_TRAIL:
            pygame.draw.circle(WINDOW, (0,0,0), (line[0], line[1]), paint_mode, index)
        for line in GREEN_TRAIL:
            pygame.draw.circle(WINDOW, (0,100,200), (line[0], line[1]), paint_mode, index)


    def clearTrails():
        BLUE_TRAIL.clear()
        RED_TRAIL.clear()
        GREEN_TRAIL.clear()
        YELLOW_TRAIL.clear()
        MAGENTA_TRAIL.clear()
        ORANGE_TRAIL.clear()

    for event in pygame.event.get():
        key = pygame.key.get_pressed()


        if event.type == pygame.QUIT:
            pygame.quit()

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                """
                if index < 1:
                    print("INVALID PAINT MODE")
                else:
                    paint_mode -= 2
                    print(paint_mode)
                """
                paint_mode = 2
                index = paint_mode-1
            elif event.key == pygame.K_EQUALS:

                paint_mode += 2
                print(paint_mode)

            elif event.key == pygame.K_RETURN:
                clearTrails()
                WINDOW.fill((0,0,0))
                pygame.draw.rect(WINDOW, (50,40,40), (0,0,40,450))
                pygame.draw.rect(WINDOW, (255,0,0), (0,20,40,40))
                pygame.draw.rect(WINDOW, (0,255,0), (0,70,40,40))
                pygame.draw.rect(WINDOW, (0,100,200), (0,120,40,40))
                pygame.draw.rect(WINDOW, (255,255,0), (0,170,40,40))
                pygame.draw.rect(WINDOW, (128,0,128), (0,220,40,40))
                pygame.draw.rect(WINDOW, (255,69,0), (0,270,40,40))
                pygame.draw.rect(WINDOW, (255,69,0), (0,270,40,40))

        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("BUTTONDOWN")
            #(0,0,40,450)
            if pygame.mouse.get_pos()[0] in range(0,40) and pygame.mouse.get_pos()[1] in range(
            0,450):
                clearTrails()
                draw_trail((255,0,0)) # default
                print(paint_color)
                paint = False
            if pygame.mouse.get_pos()[0] in range(0,40) and pygame.mouse.get_pos()[1] in range(
            20,60):
                clearTrails()
                draw_trail((255,0,0))
                paint_color = (255,0,0)
                print(paint_color)
                paint = True

            elif pygame.mouse.get_pos()[0] in range(0,40) and pygame.mouse.get_pos()[1] in range(
            70,110):
                clearTrails()
                draw_trail((0,255,0))
                paint_color = (0,255,0)
                print(paint_color)
                paint = True

            elif pygame.mouse.get_pos()[0] in range(0,40) and pygame.mouse.get_pos()[1] in range(
            120,160):
                clearTrails()
                draw_trail((0,100,200))
                paint_color = (0,100,200)

            elif pygame.mouse.get_pos()[0] in range(0,40) and pygame.mouse.get_pos()[1] in range(
            170,210):
                clearTrails()
                draw_trail((255,255,0))
                paint_color = (255,255,0)

                print(paint_color)
                paint = True

            elif pygame.mouse.get_pos()[0] in range(0,40) and pygame.mouse.get_pos()[1] in range(
            220,270):
                clearTrails()
                draw_trail((128,0,128))
                paint_color = (128,0,128)

                print(paint_color)
                paint = True

            elif pygame.mouse.get_pos()[0] in range(0,40) and pygame.mouse.get_pos()[1] in range(170,320):
                clearTrails()
                draw_trail((255,69,0))
                paint_color = (255,69,0)

                print(paint_color)
                paint = True





        elif event.type == pygame.MOUSEMOTION:

            print(pygame.mouse.get_pos())
            if pygame.mouse.get_pos()[0] in range(0,40) and pygame.mouse.get_pos()[1] in range(
            0,450):
                paint = False
                if pygame.mouse.get_pos()[0] in range(0,40) and pygame.mouse.get_pos()[1] in range(120,160):
                    pygame.draw.rect(WINDOW, (255,0,0), (0,20,40,40))
                    pygame.draw.rect(WINDOW, (0,255,0), (0,70,40,40))
                    pygame.draw.rect(WINDOW, (0,0,255), (0,120,40,40))

                elif pygame.mouse.get_pos()[0] in range(0,40) and pygame.mouse.get_pos()[1] in range(20,70):
                    pygame.draw.rect(WINDOW, (100,0,0), (0,20,40,40))
                    pygame.draw.rect(WINDOW, (0,255,0), (0,70,40,40))
                    pygame.draw.rect(WINDOW, (0,100,200), (0,120,40,40))

                elif pygame.mouse.get_pos()[0] in range(0,40) and pygame.mouse.get_pos()[1] in range(70,110):
                    pygame.draw.rect(WINDOW, (255,0,0), (0,20,40,40))
                    pygame.draw.rect(WINDOW, (0,100,0), (0,70,40,40))
                    pygame.draw.rect(WINDOW, (0,100,200), (0,120,40,40))

                elif pygame.mouse.get_pos()[0] in range(0,40) and pygame.mouse.get_pos()[1] in range(170,210):
                    pygame.draw.rect(WINDOW, (255,0,0), (0,20,40,40))
                    pygame.draw.rect(WINDOW, (0,255,0), (0,70,40,40))
                    pygame.draw.rect(WINDOW, (0,100,200), (0,120,40,40))
                    pygame.draw.rect(WINDOW, (150,150,0), (0,170,40,40))
                elif pygame.mouse.get_pos()[0] in range(0,40) and pygame.mouse.get_pos()[1] in range(220,270):
                    pygame.draw.rect(WINDOW, (255,0,0), (0,20,40,40))
                    pygame.draw.rect(WINDOW, (0,255,0), (0,70,40,40))
                    pygame.draw.rect(WINDOW, (0,100,200), (0,120,40,40))
                    pygame.draw.rect(WINDOW, (255,255,0), (0,170,40,40))
                    pygame.draw.rect(WINDOW, (80,0,80), (0,220,40,40))
                elif pygame.mouse.get_pos()[0] in range(0,40) and pygame.mouse.get_pos()[1] in range(170,320):
                    pygame.draw.rect(WINDOW, (255,0,0), (0,20,40,40))
                    pygame.draw.rect(WINDOW, (0,255,0), (0,70,40,40))
                    pygame.draw.rect(WINDOW, (0,100,200), (0,120,40,40))
                    pygame.draw.rect(WINDOW, (255,255,0), (0,170,40,40))
                    pygame.draw.rect(WINDOW, (128,0,128), (0,220,40,40))
                    pygame.draw.rect(WINDOW, (255,69,0), (0,270,40,40))

            else:
                paint = True
            if paint:
                if pygame.mouse.get_pressed()[0]:
                    pi = math.pi
                    x, y = pygame.mouse.get_pos()
                    pygame.draw.circle(WINDOW, paint_color, (x, y), paint_mode, index)



                    pygame.display.update()
        pygame.display.update()