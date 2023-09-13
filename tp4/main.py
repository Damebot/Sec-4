#Damian Lefebvre
#31 aout 2023
#TP4

import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Balle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.change_x = random.uniform(-5, 5)
        self.change_y = random.uniform(-5, 5)
        self.rayon = random.randint(10, 30)
        self.color = arcade.color.BLUE  # Changer la couleur si nécessaire

    def update(self):
        self.x += self.change_x
        self.y += self.change_y

        if self.x < 0 or self.x > SCREEN_WIDTH:
            self.change_x *= -1

        if self.y < 0 or self.y > SCREEN_HEIGHT:
            self.change_y *= -1

    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.rayon, self.color)

class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.change_x = random.uniform(-5, 5)
        self.change_y = random.uniform(-5, 5)
        self.width = random.randint(20, 50)
        self.height = random.randint(20, 50)
        self.color = arcade.color.RED  # Changer la couleur si nécessaire
        self.angle = 0

    def update(self):
        self.x += self.change_x
        self.y += self.change_y

        if self.x < 0 or self.x > SCREEN_WIDTH:
            self.change_x *= -1

        if self.y < 0 or self.y > SCREEN_HEIGHT:
            self.change_y *= -1

    def draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.width, self.height, self.color, self.angle)

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.WHITE)
        self.balle_list = []
        self.rectangle_list = []

    def on_draw(self):
        arcade.start_render()
        for balle in self.balle_list:
            balle.draw()
        for rectangle in self.rectangle_list:
            rectangle.draw()

    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            balle = Balle(x, y)
            self.balle_list.append(balle)
        elif button == arcade.MOUSE_BUTTON_RIGHT:
            rectangle = Rectangle(x, y)
            self.rectangle_list.append(rectangle)

    def update(self, delta_time):
        for balle in self.balle_list:
            balle.update()
        for rectangle in self.rectangle_list:
            rectangle.update()

def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "Balles et Rectangles")
    arcade.run()

if __name__ == "__main__":
    main()
