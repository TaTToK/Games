import pygame
import random

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
orange = (255, 100, 10)
tan = (230, 220, 170)

dis_width = 600
dis_height = 400

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption("Змейка")

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def Your_score(score):
    value = score_font.render("Ваш счет: " + str(score), True, yellow)
    dis.blit(value, [0, 0])

def our_snake(snake_block, snake_list, snake_color):
    for x in snake_list:
        pygame.draw.rect(dis, snake_color, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
    foodx2 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody2 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
    foodx3 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody3 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            dis.fill(blue)
            message("Вы проиграли. С-заново. Q-выход.", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        pygame.draw.rect(dis, orange, [foodx2, foody2, snake_block, snake_block])
        pygame.draw.rect(dis, tan, [foodx3, foody3, snake_block, snake_block])
        pygame.draw.line(dis, red, (0, 0), (0, 800))
        pygame.draw.line(dis, red, (0, 0), (800, 0))
        pygame.draw.line(dis, red, (0, 399), (600, 399))
        pygame.draw.line(dis, red, (599, 0), (599, 399))
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
        list = [white,yellow,red,green,orange,tan]
        random.shuffle(list)
        a = 0
        if a == 0:
            our_snake(snake_block, snake_List, list[0])
            a+=1

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
            snake_color = green
            our_snake(snake_block, snake_List, snake_color)
        elif x1 == foodx2 and y1 == foody2:
            foodx2 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody2 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
            snake_color = orange
            our_snake(snake_block, snake_List, snake_color)
        elif x1 == foodx3 and y1 == foody3:
            foodx3 = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody3 = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake -= 1
            snake_color = tan
            our_snake(snake_block, snake_List, snake_color)

        Your_score(Length_of_snake - 1)

        pygame.display.update()

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()