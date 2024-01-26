import pygame

pygame.init()

ScreenWidth = 1280
ScreenHeight = 720

screen = pygame.display.set_mode((ScreenWidth, ScreenHeight))
pygame.display.set_caption('Endless_Runner')

clock = pygame.time.Clock()
class Soldier(pygame.sprite.Sprite):
    def __init__(self, x, y, scale):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('files/assets/animations/adventurer-idle-00.png')
        self.image = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 8

    def draw(self):
        screen.blit(self.image, self.rect)

    def update(self):
        self.rect.x += self.speed
        if self.rect.x > ScreenWidth:
            self.rect.x = 0


player = Soldier(200, 200, 3)

run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    player.update()
    screen.fill((255, 255, 255))
    player.draw()

    pygame.display.update()
    clock.tick(60)
pygame.quit()
