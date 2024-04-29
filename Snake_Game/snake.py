from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]  # THIS IS TUPLE
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def reset(self):
        for seg in self.segment:
            seg.hideturtle()
        self.segment.clear()
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)  # it will take input from the tuple.
        self.segment.append(new_segment)  # 'new_segment' will store the element in the 'segment' list.

    def extend(self):
        self.add_segment(self.segment[-1].position())  # it will get the position of the last segment of the snake.

    def move(self):
        for seg_num in range(len(self.segment) - 1, 0, -1):  # it will work like start= len(self.segment)-1 ,end= 0,
            # step= -1. means len(self.segment)-1 element move to -1 step ahead, and it will continue till 0.
            new_x = self.segment[seg_num - 1].xcor()
            new_y = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
