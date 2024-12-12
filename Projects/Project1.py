import codesters
from codesters import StageClass 
stage = StageClass()
stage.set_background("winter")
q1 = codesters.Square(100, 100, 200, 'black')
q2 = codesters.Square(-100, 100, 200, 'white')
q3 = codesters.Square(-100, -100, 200, 'dark blue')
q4 = codesters.Square(100, -100, 200, 'purple')
s1 = codesters.Sprite("food", 100, 100)
s1.set_size(0.5)
s2 = codesters.Sprite("images", -100, -100)
s2.set_size(0.5)
s3 = codesters.Sprite("music", 100, -100)
s3.set_size(0.5)
s4 = codesters.Sprite("download", -100, 100)
s4.set_size(1.0)

message1 = codesters.Text("Zoey Jefferson or Jackson",0,220,"black")
message2 = codesters.Text("My favorite movie is rush hour!",0,-220,"black")