import random
import pygame


WIDTH = 800
HEIGHT = 600
FPS = 30
WHITE = (255, 255, 255)



def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


class Square:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.color = random_color()

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))


def main():

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()


    squares = []
    center_x = WIDTH // 2
    center_y = HEIGHT // 2
    for i in range(19):
        size = 200 - i * 10
        rect = Square(center_x - size // 2, center_y - size // 2, size)
        squares.append(rect)


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        screen.fill(WHITE)


        for square in squares:
            square.draw(screen)
            square.color = random_color()


        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()



if __name__ == "__main__":
    main()
