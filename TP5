import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class AttackType:
    ROCK = 0
    PAPER = 1
    SCISSORS = 2

class Persontype:
    compy = 0
    faceBeard = 1

attack_images = [
    r"C:\Users\mrdam\OneDrive\Desktop\Python\School\TP1-6\Images Pour TP5\srock.png",
    r"C:\Users\mrdam\OneDrive\Desktop\Python\School\TP1-6\Images Pour TP5\spaper.png",
    r"C:\Users\mrdam\OneDrive\Desktop\Python\School\TP1-6\Images Pour TP5\scissors.png"
]

people_images = [
    r"C:\Users\mrdam\OneDrive\Desktop\Python\School\TP1-6\Images Pour TP5\compy.png",
    r"C:\Users\mrdam\OneDrive\Desktop\Python\School\TP1-6\Images Pour TP5\faceBeard.png",
]

class GameState:
    START = 0
    PLAYER_CHOICE = 1
    COMPUTER_CHOICE = 2
    ROUND_RESULT = 3

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BLACK)

        self.rock_sprite = arcade.Sprite(attack_images[AttackType.ROCK], scale=0.5)
        self.rock_sprite.center_x = SCREEN_WIDTH // 6
        self.rock_sprite.center_y = SCREEN_HEIGHT // 3

        self.paper_sprite = arcade.Sprite(attack_images[AttackType.PAPER], scale=0.5)
        self.paper_sprite.center_x = SCREEN_WIDTH // 4
        self.paper_sprite.center_y = SCREEN_HEIGHT // 3

        self.scissors_sprite = arcade.Sprite(attack_images[AttackType.SCISSORS], scale=0.5)
        self.scissors_sprite.center_x = SCREEN_WIDTH // 3
        self.scissors_sprite.center_y = SCREEN_HEIGHT // 3

        self.compy_sprite = arcade.Sprite(people_images[Persontype.compy], scale=1.5)
        self.compy_sprite.center_x = SCREEN_WIDTH // 1.35
        self.compy_sprite.center_y = SCREEN_HEIGHT // 2

        self.faceBeard_sprite = arcade.Sprite(people_images[Persontype.faceBeard], scale=0.3)
        self.faceBeard_sprite.center_x = SCREEN_WIDTH // 4
        self.faceBeard_sprite.center_y = SCREEN_HEIGHT // 2

        self.player_attack_type = None
        self.computer_attack_type = None
        self.round_active = False 
        self.player_score = 0
        self.computer_score = 0
        self.game_state = GameState.START
        self.result_text = ""
        self.player_choice_confirmed = False

    def on_draw(self):
        arcade.start_render()

        arcade.draw_text("Roche, Papier, Ciseaux", SCREEN_WIDTH // 2, SCREEN_HEIGHT - 60, arcade.color.WHITE, font_size=50, anchor_x="center")

        if self.game_state != GameState.START:
            arcade.draw_text(f"Le Pointage du Joueur est de: {self.player_score}", 35, 100, arcade.color.WHITE, font_size=15)
            arcade.draw_text(f"Le Pointage de l'Ordinatuer est de: {self.computer_score}", 425, 100, arcade.color.WHITE, font_size=15)

            self.rock_sprite.draw()
            self.paper_sprite.draw()
            self.scissors_sprite.draw()
            self.compy_sprite.draw()
            self.faceBeard_sprite.draw()

            if self.game_state == GameState.ROUND_RESULT:
                arcade.draw_text(self.result_text, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.5, arcade.color.WHITE, font_size=25, anchor_x="center")
                arcade.draw_text("Appuyer sur la touche ESPACE pour commencer une nouvelle partie", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.25, arcade.color.WHITE, font_size=18, anchor_x="center")
                if self.computer_attack_type is not None:
                    if self.computer_attack_type == AttackType.ROCK:
                        self.computer_attack_type_image_sprite = arcade.Sprite(attack_images[AttackType.ROCK], scale=0.5)
                        self.computer_attack_type_image_sprite.center_x = SCREEN_WIDTH // 1.35
                        self.computer_attack_type_image_sprite.center_y = SCREEN_HEIGHT // 3

                    elif self.computer_attack_type == AttackType.PAPER:
                        self.computer_attack_type_image_sprite = arcade.Sprite(attack_images[AttackType.PAPER], scale=0.5)
                        self.computer_attack_type_image_sprite.center_x = SCREEN_WIDTH // 1.35
                        self.computer_attack_type_image_sprite.center_y = SCREEN_HEIGHT // 3
                    
                    elif self.computer_attack_type == AttackType.SCISSORS:
                        self.computer_attack_type_image_sprite = arcade.Sprite(attack_images[AttackType.SCISSORS], scale=0.5)
                        self.computer_attack_type_image_sprite.center_x = SCREEN_WIDTH // 1.35
                        self.computer_attack_type_image_sprite.center_y = SCREEN_HEIGHT // 3
                    
                    else:
                        pass

                self.computer_attack_type_image_sprite.draw()

            if self.game_state == GameState.PLAYER_CHOICE and not self.player_choice_confirmed and self.player_attack_type is not None:
                arcade.draw_text("Appuyer sur la touche ENTER pour confirmer votre choix", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 1.25, arcade.color.WHITE, font_size=18, anchor_x="center")

    def on_mouse_press(self, x, y, button, modifiers):
        if self.game_state == GameState.PLAYER_CHOICE and not self.round_active:
            if self.rock_sprite.collides_with_point((x, y)):
                self.player_attack_type = AttackType.ROCK
            elif self.paper_sprite.collides_with_point((x, y)):
                self.player_attack_type = AttackType.PAPER
            elif self.scissors_sprite.collides_with_point((x, y)):
                self.player_attack_type = AttackType.SCISSORS

    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE:
            if self.game_state == GameState.START:
                self.game_state = GameState.PLAYER_CHOICE
            elif self.game_state == GameState.ROUND_RESULT:
                self.game_state = GameState.PLAYER_CHOICE
                self.player_attack_type = None
                self.computer_attack_type = None
                self.round_active = False
                self.player_choice_confirmed = False

        if key == arcade.key.ENTER:
            if self.game_state == GameState.PLAYER_CHOICE and not self.round_active and self.player_attack_type is not None:
                self.round_active = True
                self.computer_attack_type = random.choice([AttackType.ROCK, AttackType.PAPER, AttackType.SCISSORS])
                self.game_state = GameState.ROUND_RESULT
                if self.player_attack_type == self.computer_attack_type:
                    self.result_text = "Le match est nul"
                elif (
                        (self.player_attack_type == AttackType.ROCK and self.computer_attack_type == AttackType.SCISSORS)
                        or (self.player_attack_type == AttackType.PAPER and self.computer_attack_type == AttackType.ROCK)
                        or (self.player_attack_type == AttackType.SCISSORS and self.computer_attack_type == AttackType.PAPER)
                ):
                    self.player_score += 1
                    self.result_text = "Le joueur a gagné"
                else:
                    self.computer_score += 1
                    self.result_text = "L'ordinateur a gagné"

def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "Roche, Paper, Ciseaux")
    arcade.run()

if __name__ == "__main__":
    main()
