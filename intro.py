from manimlib.imports import *

class IntroAnimationScene(Scene):
    def construct(self):
        ellipse = Ellipse(width=1.618, height=1, color=RED)
        ellipse.scale(5)
        golden_hexagon = Polygon(np.array([0.618,1,0]),np.array([1,0,0]),np.array([0.618,-1,0]),np.array([-0.618,-1,0]),np.array([-1,0,0]),np.array([-0.618,1,0]))
        hexagon = RegularPolygon()
        hexagon.scale(3)
        hexagon.rotate(-TAU/4)
        text = TextMobject("Elliptigon").scale(1.3)
        title = TextMobject("Title")
        title.move_to(0.5*DOWN)
        title.scale(0.8)

        self.play(GrowFromCenter(ellipse))
        self.play(Transform(ellipse,hexagon))
        self.play(Write(text))
        self.wait(0.3)
        self.play(ApplyMethod(text.shift,0.5*UP), run_time=0.8)
        self.play(Write(title), run_time=0.8)
        self.wait(2.9)

class Kirchoff_1_IntroAnimationScene(Scene):
    def construct(self):
        ellipse = Ellipse(width=1.618, height=1, color=RED)
        ellipse.scale(5)
        golden_hexagon = Polygon(np.array([0.618,1,0]),np.array([1,0,0]),np.array([0.618,-1,0]),np.array([-0.618,-1,0]),np.array([-1,0,0]),np.array([-0.618,1,0]))
        hexagon = RegularPolygon()
        hexagon.scale(3)
        hexagon.rotate(-TAU/4)
        text = TextMobject("Elliptigon").scale(1.3)
        title = TextMobject("Kirchhoff's Laws")
        title.move_to(0.5*DOWN)
        title.scale(0.8)

        title2 = TextMobject("Sample Problem 1")
        title2.move_to(DOWN)
        title2.scale(0.8)

        self.play(GrowFromCenter(ellipse))
        self.play(Transform(ellipse,hexagon))
        self.play(Write(text))
        self.wait(0.3)
        self.play(ApplyMethod(text.shift,0.5*UP), run_time=0.8)
        self.play(Write(title), Write(title2), run_time=0.8)
        self.wait(2.9)

class Kirchoff_2_IntroAnimationScene(Scene):
    def construct(self):
        ellipse = Ellipse(width=1.618, height=1, color=RED)
        ellipse.scale(5)
        golden_hexagon = Polygon(np.array([0.618,1,0]),np.array([1,0,0]),np.array([0.618,-1,0]),np.array([-0.618,-1,0]),np.array([-1,0,0]),np.array([-0.618,1,0]))
        hexagon = RegularPolygon()
        hexagon.scale(3)
        hexagon.rotate(-TAU/4)
        text = TextMobject("Elliptigon").scale(1.3)
        title = TextMobject("Kirchhoff's Laws")
        title.move_to(0.5*DOWN)
        title.scale(0.8)

        title2 = TextMobject("Sample Problem 2")
        title2.move_to(DOWN)
        title2.scale(0.8)

        self.play(GrowFromCenter(ellipse))
        self.play(Transform(ellipse,hexagon))
        self.play(Write(text))
        self.wait(0.3)
        self.play(ApplyMethod(text.shift,0.5*UP), run_time=0.8)
        self.play(Write(title), Write(title2), run_time=0.8)
        self.wait(2.9)

class MeshAnalysisIntroAnimationScene(Scene):
    def construct(self):
        ellipse = Ellipse(width=1.618, height=1, color=RED)
        ellipse.scale(5)
        golden_hexagon = Polygon(np.array([0.618,1,0]),np.array([1,0,0]),np.array([0.618,-1,0]),np.array([-0.618,-1,0]),np.array([-1,0,0]),np.array([-0.618,1,0]))
        hexagon = RegularPolygon()
        hexagon.scale(3)
        hexagon.rotate(-TAU/4)
        text = TextMobject("Elliptigon").scale(1.3)
        title = TextMobject("Mesh Analysis")
        title.move_to(0.5*DOWN)
        title.scale(0.8)

        self.play(GrowFromCenter(ellipse))
        self.play(Transform(ellipse,hexagon))
        self.play(Write(text))
        self.wait(0.3)
        self.play(ApplyMethod(text.shift,0.5*UP), run_time=0.8)
        self.play(Write(title), run_time=0.8)
        self.wait(2.9)

class NodalAnalysisIntroAnimationScene(Scene):
    def construct(self):
        ellipse = Ellipse(width=1.618, height=1, color=RED)
        ellipse.scale(5)
        golden_hexagon = Polygon(np.array([0.618,1,0]),np.array([1,0,0]),np.array([0.618,-1,0]),np.array([-0.618,-1,0]),np.array([-1,0,0]),np.array([-0.618,1,0]))
        hexagon = RegularPolygon()
        hexagon.scale(3)
        hexagon.rotate(-TAU/4)
        text = TextMobject("Elliptigon").scale(1.3)
        title = TextMobject("Nodal Analysis")
        title.move_to(0.5*DOWN)
        title.scale(0.8)

        self.play(GrowFromCenter(ellipse))
        self.play(Transform(ellipse,hexagon))
        self.play(Write(text))
        self.wait(0.3)
        self.play(ApplyMethod(text.shift,0.5*UP), run_time=0.8)
        self.play(Write(title), run_time=0.8)
        self.wait(2.9)

class AlternatingCurrentIntroAnimationScene(Scene):
    def construct(self):
        ellipse = Ellipse(width=1.618, height=1, color=RED)
        ellipse.scale(5)
        golden_hexagon = Polygon(np.array([0.618,1,0]),np.array([1,0,0]),np.array([0.618,-1,0]),np.array([-0.618,-1,0]),np.array([-1,0,0]),np.array([-0.618,1,0]))
        hexagon = RegularPolygon()
        hexagon.scale(3)
        hexagon.rotate(-TAU/4)
        text = TextMobject("Elliptigon").scale(1.3)
        title = TextMobject("Alternating Current")
        title.move_to(0.5*DOWN)
        title.scale(0.8)

        self.play(GrowFromCenter(ellipse))
        self.play(Transform(ellipse,hexagon))
        self.play(Write(text))
        self.wait(0.3)
        self.play(ApplyMethod(text.shift,0.5*UP), run_time=0.8)
        self.play(Write(title), run_time=0.8)
        self.wait(2.9)

class WhyACIntroAnimationScene(Scene):
    def construct(self):
        ellipse = Ellipse(width=1.618, height=1, color=RED)
        ellipse.scale(5)
        golden_hexagon = Polygon(np.array([0.618,1,0]),np.array([1,0,0]),np.array([0.618,-1,0]),np.array([-0.618,-1,0]),np.array([-1,0,0]),np.array([-0.618,1,0]))
        hexagon = RegularPolygon()
        hexagon.scale(3)
        hexagon.rotate(-TAU/4)
        text = TextMobject("Elliptigon").scale(1.3)
        title = TextMobject("Why Do We Use AC?")
        title.move_to(0.5*DOWN)
        title.scale(0.8)

        self.play(GrowFromCenter(ellipse))
        self.play(Transform(ellipse,hexagon))
        self.play(Write(text))
        self.wait(0.3)
        self.play(ApplyMethod(text.shift,0.5*UP), run_time=0.8)
        self.play(Write(title), run_time=0.8)
        self.wait(2.9)

class MathBehindACIntroAnimationScene(Scene):
    def construct(self):
        ellipse = Ellipse(width=1.618, height=1, color=RED)
        ellipse.scale(5)
        golden_hexagon = Polygon(np.array([0.618,1,0]),np.array([1,0,0]),np.array([0.618,-1,0]),np.array([-0.618,-1,0]),np.array([-1,0,0]),np.array([-0.618,1,0]))
        hexagon = RegularPolygon()
        hexagon.scale(3)
        hexagon.rotate(-TAU/4)
        text = TextMobject("Elliptigon").scale(1.3)
        title = TextMobject("The Math Behind AC")
        title.move_to(0.5*DOWN)
        title.scale(0.8)

        self.play(GrowFromCenter(ellipse))
        self.play(Transform(ellipse,hexagon))
        self.play(Write(text))
        self.wait(0.3)
        self.play(ApplyMethod(text.shift,0.5*UP), run_time=0.8)
        self.play(Write(title), run_time=0.8)
        self.wait(2.9)

class RLCSeriesIntroAnimationScene(Scene):
    def construct(self):
        ellipse = Ellipse(width=1.618, height=1, color=RED)
        ellipse.scale(5)
        golden_hexagon = Polygon(np.array([0.618,1,0]),np.array([1,0,0]),np.array([0.618,-1,0]),np.array([-0.618,-1,0]),np.array([-1,0,0]),np.array([-0.618,1,0]))
        hexagon = RegularPolygon()
        hexagon.scale(3)
        hexagon.rotate(-TAU/4)
        text = TextMobject("Elliptigon").scale(1.3)
        title = TextMobject("RLC Series Circuits")
        title.move_to(0.5*DOWN)
        title.scale(0.8)

        self.play(GrowFromCenter(ellipse))
        self.play(Transform(ellipse,hexagon))
        self.play(Write(text))
        self.wait(0.3)
        self.play(ApplyMethod(text.shift,0.5*UP), run_time=0.8)
        self.play(Write(title), run_time=0.8)
        self.wait(2.9)
