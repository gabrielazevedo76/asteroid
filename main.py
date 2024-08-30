import pygame

import constants


def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

    screen = pygame.display.set_mode(
        (constants.SCREEN_HEIGHT, constants.SCREEN_WIDTH))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((0, 0, 0))
        pygame.display.update()


if __name__ == "__main__":
    main()
