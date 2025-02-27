# section 1 - setup
import codesters, random 
from codesters import StageClass
stage = StageClass()
stage.disable_all_walls()
player = codesters.Sprite("shark")
stage.set_background("ocean")
player.set_size(0.5)
object_speed = 8 
Object_speed = 250
lives = 3

# section 2 - objects
def falling_object():
        global object_speed,lives
        if lives!=0: #game is not over
                x=random.randint(-250,250)
                y=0

                object = codesters.Sprite("fish",x,y)
                object.set_size(1)
                object.set_x_speed(object_speed)
stage.event_interval(falling_object,2)

def collision(player,object):
        global lives

        if object.get_image_name() == "fish": 
                stage.remove_sprite(object)
                lives-= 1
                if lives==0:
                        player.say(f"out of lives-you loose!", 5)
                else:
                        player.say(f"{lives} lives",0.5)
player.event_collision(collision)

def go_right():
        player.move_right(10)

player.event_key("right", go_right)

def go_left():
        player.move_left(10)

player.event_key("left", go_left)