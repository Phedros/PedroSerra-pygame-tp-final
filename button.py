import pygame

#images buttons
    # Intro
start_img = pygame.image.load("images\caracters\extras\start.png")
settings_img = pygame.image.load("images\caracters\extras\settings.png")
exit_img = pygame.image.load("images\caracters\extras\exit.png")
    #Pause
resume_img = pygame.image.load(r"images\caracters\extras\resume.png")
settings_pause_img = pygame.image.load("images\caracters\extras\settings_pause.png")
quit_img = pygame.image.load("images\caracters\extras\quit.png")
    #Game Over
menu_img = pygame.image.load("images\caracters\extras\menu2.png")

class Button():
    def __init__(self,x,y,image) -> None:
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

    def draw(self,screen,pos_mouse):
        screen.blit(self.image, (self.rect.x, self.rect.y))

        if self.rect.collidepoint(pos_mouse):
            pass

