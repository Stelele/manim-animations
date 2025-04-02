from manim import *

config.media_width = "75%"

class MainScene(Scene):
    def construct(self):
        t1 = Text("Hello There", font_size=100)
        t2 = Text("Have you heard of functions", font_size=60)

        self.play(Write(t1), run_time=2)
        self.play(t1.animate.shift(UP*1.5), run_time=2)
        self.play(FadeOut(t1), Write(t2), run_time=2)
        self.wait()

        t3 = Text("Think of a box", font_size=60)
        rect1 = Rectangle().set_fill(WHITE, 0.8)

        rect1.fill_color = WHITE
        self.play(t2.animate.shift(UP*1.5))
        self.play(FadeOut(t2), Write(t3), run_time=2)
        self.play(t3.animate.shift(UP*1.5), run_time=2)
        rect1.next_to(t3, DOWN, 1)
        self.play(Create(rect1), run_time = 2)
        self.wait()

        t4 = Text("You can put something in the box", font_size=60).shift(UP*1.5)
        arrow1 = Arrow(start=LEFT, end=RIGHT).next_to(rect1, LEFT, 0)
        self.play(Transform(t3, t4), Write(arrow1), run_time=2)
        self.wait(2)

        t5 = Text("And out comes something", font_size=60).shift(UP*1.5)
        arrow2 = Arrow(start=LEFT, end=RIGHT).next_to(rect1, RIGHT, 0)
        self.play(Transform(t3, t5), Write(arrow2), run_time=2)
        self.wait(2)

        t6 = Text("Lets see some examples", font_size=60).shift(UP*1.5)
        self.play(Transform(t3, t6), run_time=2)

        for i in range(2):
            crc1 = Circle().scale(0.5).next_to(arrow1, LEFT)
            sqr1 = Square().scale(0.5).next_to(arrow2, RIGHT)
            self.play(Write(crc1))
            self.play(Transform(crc1, sqr1), run_time=2)
            self.play(FadeOut(crc1))

            tri1 = Triangle().scale(0.5).next_to(arrow1, LEFT)
            crc2 = Circle().scale(0.5).next_to(arrow2, RIGHT)
            self.play(Write(tri1))
            self.play(Transform(tri1, crc2), run_time=2)
            self.play(FadeOut(tri1))

            sqr1 = Square().scale(0.5).next_to(arrow1, LEFT)
            tri2 = Triangle().scale(0.5).next_to(arrow2, RIGHT)
            self.play(Write(sqr1))
            self.play(Transform(sqr1, tri2), run_time=2)
            self.play(FadeOut(sqr1))

        t7 = Text("Did you notice the pattern", font_size=60).shift(UP*1.5)
        self.play(Transform(t3, t7), run_time=2)
        self.wait(2)

        t8 = Text("Each input", font_size=60).shift(UP*1.5)
        tri1 = Triangle()
        crc1 = Circle().next_to(tri1, UP)
        sqr1 = Square().next_to(tri1, DOWN)
        vg1 = VGroup(crc1, tri1, sqr1)
        vg1.scale(0.5).next_to(arrow1, LEFT)
        self.play(Transform(t3, t8), Write(vg1), run_time=2)
        self.wait(2)

        t9 = Text("Has a specific output", font_size=60).shift(UP*1.5)
        crc2 = Circle()
        sqr2 = Square().next_to(crc2, UP)
        tri2 = Triangle().next_to(crc2, DOWN)
        vg2 = VGroup(sqr2, crc2, tri2)
        vg2.scale(0.5).next_to(arrow2, RIGHT)
        self.play(Transform(t3, t9), Transform(vg1, vg2), run_time=2)
        self.wait(2)

        t10 = Text("If we look inside the box", font_size=60).shift(UP*1.5)
        mArrw2 = Arrow(LEFT, RIGHT)
        mArrw1 = Arrow(LEFT, RIGHT).next_to(mArrw2, UP)
        mArrw3 = Arrow(LEFT, RIGHT).next_to(mArrw2, DOWN)
        inTri = Triangle().scale(0.3)
        inCrc = Circle().next_to(inTri, UP).scale(0.3)
        inSqr = Square().next_to(inTri, DOWN).scale(0.3)
        outCrc = Circle().scale(0.3)
        outSqr = Square().next_to(outCrc, UP).scale(0.3)
        outTri = Triangle().next_to(outCrc, DOWN).scale(0.3)
        vg2 = VGroup(inTri, mArrw2, outCrc, inCrc, mArrw1, outSqr, inSqr, mArrw3, outTri)
        vg2.arrange_in_grid(rows=3).scale(0.7).shift(DOWN)
    
        self.play(Transform(t3, t10), FadeOut(vg1), Write(vg2), rect1.animate.set_fill(opacity=0), run_time=2)
        self.wait(2)
        