import pygame

pygame.init() # 초기화

# 화면 크기 
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀
pygame.display.set_caption("Nam Game")

# 배경 이미지 
background = pygame.image.load("C:/projects/pythongame/background.png")

# 이벤트 루프
running = True # 게임이 진행중인지
while running:
    for event in pygame.event.get():  # 어떤 이벤트가 발생했나
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생했나
            running = False # 게임이 진행중이 아님
    
    #screen.fill((0,0,255))
    screen.blit(background, (0, 0)) # 배경 그리기

    pygame.display.update() # 게임 화면 다시 그리기

# pygame 종료 
pygame.quit()