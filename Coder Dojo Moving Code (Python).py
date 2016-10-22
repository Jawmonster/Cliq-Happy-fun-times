{\rtf1\ansi\ansicpg1252\cocoartf1404\cocoasubrtf470
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import simplegui\
\
class ShapeAttributes:\
    \
    def __init__(self):\
        self.line_width = 10\
        self.line_color = "seagreen"\
        self.fill_color = "lightgreen"\
\
class Circle:\
    \
    def __init__(self):\
        self.radius = 50\
        self.center_point = (100, 200)\
        \
    def update_x(self, shift_x):\
        self.center_point = (\
            self.center_point[0] + shift_x,\
            self.center_point[1])\
        \
    def update_y(self, shift_y):\
        self.center_point = (\
            self.center_point[1] + shift_y,\
            self.center_point[0])\
     \
class Character:\
    \
    key_map = \{\
            "left": 37,\
            "up":  38,\
            "right": 39,\
            "down": 40\
        \}\
    \
    def __init__(self):\
        self.circle_shape = Circle()\
        self.shape_attributes = ShapeAttributes()\
        self.movement = 10\
        \
    def draw_me(self, canvas):\
        canvas.draw_circle(\
            self.circle_shape.center_point,\
            self.circle_shape.radius,\
            self.shape_attributes.line_width,\
            self.shape_attributes.line_color,\
            self.shape_attributes.fill_color\
        )\
        \
    def move(self, key):\
        if self.key_map["right"] == key:\
            self.circle_shape.update_x(self.movement)\
        if self.key_map["left"] == key:\
            self.circle_shape.update_x(-self.movement)\
        if self.key_map["up"] == key:\
            self.circle_shape.update_y(-self.movement)\
        if self.key_map["down"] == key:\
            self.circle_shape.update_y(self.movement)\
        print key\
        \
cliq = Character()\
        \
# Handler to draw on canvas\
def draw(canvas):\
    cliq.draw_me(canvas)\
\
# Create a frame and assign callbacks to event handlers\
frame = simplegui.create_frame("Home", 500, 500)\
frame.set_draw_handler(draw)\
frame.set_keydown_handler(cliq.move)\
frame.start()\
}