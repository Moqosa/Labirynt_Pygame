import pygame
import sys
sys.setrecursionlimit(1000)
import time

class Game:

    def __init__(self):
        pygame.init() #Inicjalizacja całej gry
        self.screen = pygame.display.set_mode((1920, 1080))
        self.end_point = pygame.Rect(760, 530, 30, 30)
        self.player = pygame.Rect(20, 1040, 30, 30)
        self.map_width = 1920
        self.map_height = 1080
        self.font = pygame.font.Font(None, 36)
        self.text = self.font.render("You Won!!!", False, (255, 255, 255))
        self.count = 0
        self.count_text = self.font.render(f"{self.count}", False, (255, 255, 255))
        self.rule_text = self.font.render("Press Q to exit", False, (255, 255, 255))
        self.map_cleared = False
        pygame.display.set_caption("The gameaaaaaaa")

    def run_game(self):


        while True:
            self.check_events()
            self.keyboard_check_events()
            self.update_screen()
            self.map_stage01()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                    sys.exit()

            if self.player.colliderect(self.line1) or self.player.colliderect(self.line2) or self.player.colliderect(self.line3) or self.player.colliderect(self.line4) \
                    or self.player.colliderect(self.line5) or self.player.colliderect(self.line6) or self.player.colliderect(self.line7):
                self.player.x = 20
                self.player.y = 1040
                self.count += 1
                self.count_text = self.font.render(f"Deaths: {self.count}", False, (255, 0, 0))

    def check_events(self): #Wyście z gry
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()



    def keyboard_check_events(self): #Poruszanie gracza
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.player.left > 0:
            self.player.x -= 1.5
        elif keys[pygame.K_d] and self.player.right < self.map_width:
            self.player.x += 1.5
        elif keys[pygame.K_w] and self.player.top > 0:
            self.player.y -= 1.5
        elif keys[pygame.K_s] and self.player.bottom < self.map_height:
            self.player.y += 1.5


    def map_stage01(self):
        self.screen.fill((0, 0, 0))
        self.line1 = pygame.draw.line(self.screen, (0, 250, 0), (70, 1080), (70, 50)) # Linia 1
        self.line2 = pygame.draw.line(self.screen, (0, 250, 0), (70, 50), (1850, 50))  # Linia 2
        self.line3 = pygame.draw.line(self.screen, (0, 250, 0), (1850, 50), (1850, 1020))  # Linia 3
        self.line4 = pygame.draw.line(self.screen, (0, 250, 0), (1850, 1020), (800, 1020))  # Linia 4
        self.line5 = pygame.draw.line(self.screen, (0, 250, 0), (800, 1020), (800, 520))  # Linia 5
        self.line6 = pygame.draw.line(self.screen, (0, 250, 0), (750, 1100), (750, 520))  # Linia 6
        self.line7 = pygame.draw.line(self.screen, (0, 250, 0), (800, 520), (750, 520))  # Linia 7

    def update_screen(self):

        if self.count >= 1:
            self.screen.blit(self.count_text, (1600, 150))  # Wyświetlenie śmierci gracza

        self.screen.blit(self.rule_text, (1600,200)) #Wyświetlenie zasad gry

        if self.player.colliderect(self.end_point): #Instrukcja warunkowa do przejścia gry
            self.screen.blit(self.text, (100, 100))

        pygame.draw.rect(self.screen, (0,0,255), self.player) #Narysowanie gracza
        pygame.draw.rect(self.screen, (0,255,0), self.end_point) #Narysowanie miejsca punktu końca gry
        pygame.display.flip()


if __name__ == "__main__":
    game = Game()
    game.run_game()

