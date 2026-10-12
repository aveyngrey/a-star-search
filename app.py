import pygame

pygame.init()
screen = pygame.display.set_mode((700,700))
pygame.display.set_caption("A* Search")
clock = pygame.time.Clock()
running = True
started = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if started:
            continue

        if pygame.mouse.get_pressed()[0]:
            pass
        elif pygame.mouse.get_pressed()[2]:
            pass

    screen.fill("gray")

    pygame.display.flip()

    clock.tick(60)

pygame.quit()

