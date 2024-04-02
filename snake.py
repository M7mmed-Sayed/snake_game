from turtle import Turtle, Screen

INIT_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
STEP_DISTANCE = 20
SCALE = 0.2
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
screen = Screen()
image_path = "headsnake.gif"
image_body_path = "body.gif"

screen.addshape(image_path)
screen.addshape("headsnakeleft.gif")
screen.addshape("headsnakeup.gif")
screen.addshape("headsnakedown.gif")


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for pos in INIT_POSITIONS:
            if INIT_POSITIONS[0] == pos:
                self.add_segment(pos, True)
            else:
                self.add_segment(pos, False)

    def add_segment(self, pos, head):
        shape = "square"
        if head:
            shape = image_path
        new_seg = Turtle(shape)
        new_seg.color("green")
        new_seg.penup()
        new_seg.goto(pos)
        self.segments.append(new_seg)

    def extend(self):
        self.add_segment(self.segments[-1].position(),False)

    def move(self):
        for seg_id in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_id - 1].xcor()
            new_y = self.segments[seg_id - 1].ycor()
            self.segments[seg_id].goto(new_x, new_y)
        self.segments[0].forward(STEP_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.segments[0].shape("headsnakeup.gif")
            self.segments[0].setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.segments[0].shape("headsnakedown.gif")
            self.segments[0].setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.segments[0].shape("headsnakeleft.gif")
            self.segments[0].setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.segments[0].shape("headsnake.gif")
            self.segments[0].setheading(RIGHT)
