import pygame
import random


class Car():
    def __init__(self, x, y, w, h, color):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = color

    def draw(self, surf):
        pygame.draw.rect(surf, self.color, self.rect)

class Player(Car):
 
    def __init__(self):
        super().__init__(100, 100, 100, 50, (153, 51, 102))
        self.speed = 1
    
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_s]:
            self.rect.y += self.speed
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_d]:
            self.rect.x += self.speed

        self.rect.clamp_ip(pygame.Rect(0, 0, 1920, 1080))

class NPC(Car):
    def __init__(self):
        x = 1920
        y = random.randint(0, 1080 - 50)
        super().__init__(x, y, 100, 50, (255, 255, 204))
        self.speed = 2

    def update(self):
        self.rect.x -= self.speed

class UpdateNPC():
    def __init__(self, spawn_delay=300):
        self.npcs = []
        self.spawn_timer = 0
        self.spawn_delay = spawn_delay

    def update(self):
        self.spawn_timer += 1
        if self.spawn_timer >= self.spawn_delay:
            self.npcs.append(NPC())
            self.spawn_timer = 0

        for npc in self.npcs:
            npc.update()

        self.npcs = [npc for npc in self.npcs if npc.rect.right > 0]

    def draw(self, surf):
        for npc in self.npcs:
            npc.draw(surf)

def main():
    pygame.init()
    pygame.display.set_caption("Twelve 'o Clock Wheelman") #Play on Midnight Motorist xd
    clock = pygame.time.Clock()
    clock.tick(60)

    player = Player()
    updated_npc = UpdateNPC(spawn_delay=300)
    resolution = (1920, 1080)
    screen = pygame.display.set_mode(resolution)
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        player.update()
        updated_npc.update()

        screen.fill((0, 0, 0))
        player.draw(screen)
        updated_npc.draw(screen)

        pygame.display.flip()
        
    pygame.quit()


if __name__ == "__main__":
    main()
