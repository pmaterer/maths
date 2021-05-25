import math
import numpy as np
from manim import *

config.background_color = BLACK
config.frame_width = 19

class RightTriangle(GraphScene):
    
    def __init__(self, **kwargs):
        GraphScene.__init__(
            self,
            x_min=0,
            x_max=5,
            y_min=0,
            y_max=5,
            x_labeled_nums=np.arange(0, 5, 1),
            y_labeled_nums=np.arange(0, 5, 1),
            **kwargs
        )

    def construct(self):
        self.setup_axes()

        a = 3.2
        b = 2.8
        c = math.sqrt((a**2) + (b**2))

        origin = self.coords_to_point(0, 0)
        a_point = self.coords_to_point(a, 0)
        b_point = self.coords_to_point(0, b)

        dot1 = Dot(a_point)
        dot2 = Dot(b_point)
        dot3 = Dot(origin)

        line1 = Line(dot3.get_center(), dot1.get_center(), color=RED)
        line2 = Line(dot1.get_center(), dot2.get_center(), color=PURPLE)
        line3 = Line(dot2.get_center(), dot3.get_center(), color=BLUE)

        right_angle = RightAngle(line3, line1, length=0.4, quadrant=(-1, 1))

        # pythagorean theorem
        # hypotenuse = math.sqrt((**2) + (b**2))
        theta_angle = math.asin(line3.get_length() / line2.get_length())

        theta = Arc(
            radius=1, 
            start_angle=line2.get_angle(), 
            angle=theta_angle, 
            arc_center=line2.get_start()
        )
        theta_symbol = MathTex(r"\theta").move_to(
            Arc(
                radius=1 + 3 * SMALL_BUFF, 
                start_angle=line2.get_angle(), 
                angle=theta_angle, 
                arc_center=line2.get_start()
            )
        )

        a_text = Text(f"a = {a}")
        a_text.next_to(line1, LEFT)

        b_text = Text(f"b = {b}")
        b_text.next_to(line2, DOWN)
        
        self.add(dot1, dot2, dot3,
            line1, line2, line3,
            theta, theta_symbol, right_angle,
            a_text, b_text)

class PolarCartesian(GraphScene):
    
    def __init__(self, **kwargs):
        GraphScene.__init__(
            self,
            x_min=0,
            x_max=5,
            y_min=0,
            y_max=5,
            x_labeled_nums=np.arange(0, 5, 1),
            y_labeled_nums=np.arange(0, 5, 1),
            **kwargs
        )

    def construct(self):
        self.setup_axes()

        a = 2.5
        b = 3
        c = math.sqrt((a**2) + (b**2))

        origin = self.coords_to_point(0, 0)
        a_point = self.coords_to_point(a, 0)
        b_point = self.coords_to_point(0, b)

        dot1 = Dot(a_point)
        dot2 = Dot(b_point)
        dot3 = Dot(origin)

        line1 = Line(dot3.get_center(), dot1.get_center(), color=RED)
        line2 = Line(dot1.get_center(), dot2.get_center(), color=PURPLE)
        line3 = Line(dot2.get_center(), dot3.get_center(), color=BLUE)

        right_angle = RightAngle(line3, line1, length=0.4, quadrant=(-1, 1))

        # pythagorean theorem
        # hypotenuse = math.sqrt((**2) + (b**2))
        theta_angle = math.asin(line3.get_length() / line2.get_length())

        theta = Arc(
            radius=1, 
            start_angle=line2.get_angle(), 
            angle=theta_angle, 
            arc_center=line2.get_start()
        )
        theta_symbol = MathTex(r"\theta").move_to(
            Arc(
                radius=1 + 3 * SMALL_BUFF, 
                start_angle=line2.get_angle(), 
                angle=theta_angle, 
                arc_center=line2.get_start()
            )
        )

        b1 = Brace(line1, buff=0.5)
        b2 = Brace(line2, buff=0.5, direction=line2.copy().rotate(line3.get_angle()).get_unit_vector())
        b3 = Brace(line3, buff=0.5, direction=line3.copy().rotate(line3.get_angle()).get_unit_vector())

        b1_text = b1.get_text(r"$x = r * \cos(\theta)$")
        b2_text = b2.get_text(f"$r$")
        b3_text = b3.get_text(r"$x = r * \sin(\theta)$")


        
        self.add(dot1, dot2, dot3,
            line1, line2, line3,
            theta, theta_symbol, right_angle,
            b1, b1_text, b2, b2_text, b3, b3_text)