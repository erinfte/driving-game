import pygame
import random


class Car():
      def __init__(self, x, y, w, h, color):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = color

        def draw(self, surf):
            pygame.draw.rect(surf, self.color, self.rect)

# class Player(Car):
 
    # def __init__(self):
        #x =
        #y =
    
    # def update(self):
        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_w]:
            # self.rect.y -= self.speed
        # if keys[pygame.K_s]:
            # self.rect.y += self.speed
        # if keys[pygame.K_a]:
            # self.rect.x -= self.speed
        # if keys[pygame.K_d]:
            # self.rect.x += self.speed

# class NPC(Car):

    # def __init__(self):

    # def update(self):

def main():
    pygame.init()
    pygame.display.set_caption("Twelve 'o Clock Wheelman") #Play on Midnight Motorist xd
    clock = pygame.time.Clock()
    resolution = (800, 600)
    screen = pygame.display.set_mode(resolution)
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
