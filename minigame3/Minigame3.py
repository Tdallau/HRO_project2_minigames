



from PGS.PygameSimplified import *


import pygame as pg
import sys
from minigame3.HighScore import *

def menu():
    display_width = 800
    display_height = 600
    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)
    gameDisplay = pygame.display.set_mode((display_width, display_height))
    # pygame.display.set_caption('A bit Racey')
    clock = pygame.time.Clock()
   

    def text_objects(text, font):
        textSurface = font.render(text, True, white)
        return textSurface, textSurface.get_rect()

    def message_display(text):
        largeText = pygame.font.Font('freesansbold.ttf', 50)
        TextSurf, TextRect = text_objects(text, largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)

        pygame.display.update()

    def message_display1(text):
        largeText = pygame.font.Font('freesansbold.ttf', 25)
        TextSurf, TextRect = text_objects(text, largeText)
        TextRect.center = ((display_width / 2), (display_height / 1.7))
        gameDisplay.blit(TextSurf, TextRect)

    def message_display2(text):
        largeText = pygame.font.Font('freesansbold.ttf', 25)
        TextSurf, TextRect = text_objects(text, largeText)
        TextRect.center = ((display_width / 2), (display_height / 1.5))
        gameDisplay.blit(TextSurf, TextRect)

    class States(object):
        def __init__(self):
            self.done = False
            self.next = None
            self.quit = False
            self.previous = None


    class Menu(States):
        def __init__(self):
            States.__init__(self)
            self.next = 'game'

        def cleanup(self):
            print('cleaning up Menu state stuff')

        def startup(self):
            print('starting Menu state stuff')

        def get_event(self, event):
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_q:
                    self.done = True
                    
            elif event.type == pg.MOUSEBUTTONDOWN:
                self.done = True

        def update(self, screen, dt):
            self.draw(screen)

        def draw(self, screen):
            display_width = 800
            display_height = 600
            black = (0, 0, 0)
            white = (255, 255, 255)
            red = (255, 0, 0)
            gameDisplay = pygame.display.set_mode((display_width, display_height))
            # pygame.display.set_caption('A bit Racey')
            clock = pygame.time.Clock()



            message_display('Picnick Panic')
            message_display1("Gebruik de muis om de picnic items te vangen")
            message_display2("Klik om te beginnen")


    class Game(States):
        def __init__(self):
            States.__init__(self)
            self.next = 'menu'
            self.score = 0

        def cleanup(self):
            # Event.quit_game()
            self.done = True

        def startup(self):
            self.score = str(game())
            # print(str(game()))

        def get_event(self, event):
            if event.type == pg.KEYDOWN:
                print('Game State keydown')
            elif event.type == pg.MOUSEBUTTONDOWN:
                self.done = True

        def update(self, screen, dt):
            display_width = 800
            display_height = 600
            black = (0, 0, 0)
            white = (255, 255, 255)
            red = (255, 0, 0)
            gameDisplay = pygame.display.set_mode((display_width, display_height))
            # pygame.display.set_caption('A bit Racey')
            clock = pygame.time.Clock()

            message_display('Game Over')
            message_display1("Je score is " + str(self.score))
            message_display2("Klik om te sluiten")





    class Control:
        def __init__(self, **settings):
            self.__dict__.update(settings)
            self.done = False
            self.screen = pg.display.set_mode(self.size)
            self.clock = pg.time.Clock()

        def setup_states(self, state_dict, start_state):
            self.state_dict = state_dict
            self.state_name = start_state
            self.state = self.state_dict[self.state_name]

        def flip_state(self):
            self.state.done = False
            previous, self.state_name = self.state_name, self.state.next
            self.state.cleanup()
            self.state = self.state_dict[self.state_name]
            self.state.startup()
            self.state.previous = previous

        def update(self, dt):
            if self.state.quit:
                self.done = True
            elif self.state.done:
                self.flip_state()
            self.state.update(self.screen, dt)

        def event_loop(self):
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.done = True
                self.state.get_event(event)

        def main_game_loop(self):
            while not self.done:
                delta_time = self.clock.tick(self.fps) / 1000.0
                self.event_loop()
                self.update(delta_time)
                pg.display.update()


    settings = {
        'size': (600, 400),
        'fps': 60
    }

    app = Control(**settings)
    state_dict = {
        'menu': Menu(),
        'game': Game()
    }
    app.setup_states(state_dict, 'menu')
    app.main_game_loop()
    pg.quit()
    sys.exit()

def game():

    screen = pg.display.set_mode((800,640))

    # program code for catch a fish game

    # part 1: import all modules from Pygame Simplified



    # part 1.1
    fishWorld = World(1200, 600)
    goldFish = Actor()
    shark = Actor()
    badrock = Actor()
    stone = Actor()
    score_text = Text(fishWorld)
    score = 0
    topscore = score

    highscore = HighScore(0)
    print(highscore.amound)



    # part 1.2
    fishWorld.set_background("images/sea.png")
    shark.set_image("images/basket.png")
    goldFish.generate_rand_actors(3, "images/apple.png", fishWorld)
    goldFish.generate_rand_actors(3, "images/breadsticks.png", fishWorld)
    goldFish.generate_rand_actors(3, "images/Cheese.png", fishWorld)
    goldFish.generate_rand_actors(3, "images/grapes.png", fishWorld)
    goldFish.generate_rand_actors(3, "images/wine.png", fishWorld)

    # stone.generate_rand_actors(10, "images/badrock1.png", fishWorld)
    stone.generate_rand_actors(5, "images/tooth.png", fishWorld)
    stone.generate_rand_actors(2, "images/bed.png", fishWorld)
    stone.generate_rand_actors(1, "images/croc.png", fishWorld)


    # part 1.3
    score = 0

    # part 2: run code inside the while loop
    while True:
        # part 1.3
        timer_text = Text(fishWorld)
        # sets our timer to 5
        timer = 10
        Timer.decrement_timer(timer)
        timer_text.set_text("Timer:" + str(Timer.get_seconds()))
        timer_text.draw_text(fishWorld.width / 2, 40)
        timer_text.set_font("Calibri", 25)
        timer_text.set_colour(0, 0, 0)

        if Timer.get_seconds() == 1:
            highscore.checkForHighScore(score)
            return str(score)
            




        # part 2.1 - updates
        Event.update()
        shark.update()
        goldFish.update_actors()
        badrock.update_actors()
        stone.update_actors()



        for fishes in goldFish:
            fishes.move_by(0, 2)
            if fishes.y == 410 or goldFish.actor_group_length() <= 2:
                goldFish.generate_rand_actors(1, "images/apple.png", fishWorld)
            if fishes.y == 410 or goldFish.actor_group_length() <= 2:
                goldFish.generate_rand_actors(1, "images/breadsticks.png", fishWorld)
            if fishes.y == 410 or goldFish.actor_group_length() <= 2:
                goldFish.generate_rand_actors(1, "images/Cheese.png", fishWorld)
            elif fishes.y == 410 or goldFish.actor_group_length() <= 2:
                goldFish.generate_rand_actors(1, "images/grapes.png", fishWorld)
            elif fishes.y == 410 or goldFish.actor_group_length() <= 2:
                goldFish.generate_rand_actors(1, "images/wine.png", fishWorld)


        # part 2.1.1
        mousex, mousey = Event.mouse_pos
        shark.set_location(mousex, mousey)


        for stones in stone:
            stones.move_by(0, 2)
            if stones.y == 410 or stone.actor_group_length() <= 1:
                stone.generate_rand_actors(1, "images/croc.png", fishWorld)
            if stones.y == 410 or stone.actor_group_length() <= 2:
                stone.generate_rand_actors(1, "images/bed.png", fishWorld)
            if stones.y == 410 or stone.actor_group_length() <= 5:
                stone.generate_rand_actors(1, "images/tooth.png", fishWorld)

        if goldFish.collide_group(shark):
            score += 1

        if stone.collide_group(shark):
            score -= 2

        # part 2.2
        fishWorld.draw_background(0, 0)
        # draws and sets the location of the shark in the middle of the screen above the bottom of the screen
        fishWorld.draw_actor(shark, mousex, mousey)
        goldFish.draw_actors(fishWorld.window)
        badrock.draw_actors(fishWorld.window)
        stone.draw_actors(fishWorld.window)

        # part 2.3
        score_text.set_text("Score: " + str(score))
        score_text.draw_text(fishWorld.width / 2, 10)
    # print(end)


# menu()