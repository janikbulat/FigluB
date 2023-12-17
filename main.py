import pygame

class FGWindow:
    def __init__(self):
        self.window = pygame.display.set_mode((900, 700))
        pygame.display.set_caption('FigluB')

    def start(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        pygame.quit()

figlub_window = FGWindow()
figlub_window.start()
