from turtle import Turtle


NO_OF_SLAB = 5
NO_OF_SEGMENT_IN_FIRST_SLAB = 11
STARTING_POSITION_X = 200
STARTING_POSITION_Y = 0
DISTANCE_BETWEEN_SEGMENT_X = 42
DISTANCE_BETWEEN_SEGMENT_Y = 22
STRETCH_WIDTH = 1
STRETCH_LENGTH = 2
COLOR = "blue"


class Block:

    def __init__(self):
        self.segment_list = []
        self.positions = []

    def create_positions(self,increment_per_slab=0):
        for num1 in range(NO_OF_SLAB):
            for num2 in range(NO_OF_SEGMENT_IN_FIRST_SLAB + increment_per_slab):
                x_cor = (STARTING_POSITION_X + DISTANCE_BETWEEN_SEGMENT_X * num1) - DISTANCE_BETWEEN_SEGMENT_X * num2
                y_cor = STARTING_POSITION_Y + DISTANCE_BETWEEN_SEGMENT_Y * num1
                tuple = (x_cor, y_cor)
                self.positions.append(tuple)
            increment_per_slab += 2

    def create_block(self):
        self.create_positions()
        for position in self.positions:
            self.add_segment(position)

    def add_segment(self,position):
        new_segment = Turtle("square")
        new_segment.color(COLOR)
        new_segment.shapesize(stretch_wid=STRETCH_WIDTH, stretch_len=STRETCH_LENGTH)
        new_segment.penup()
        new_segment.goto(position)
        self.segment_list.append(new_segment)








