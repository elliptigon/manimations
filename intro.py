from manimlib.imports import *

class IntroAnimationScene(Scene):
    def construct(self):
        ellipse = Ellipse(width=1.618, height=1, color=RED)
        ellipse.scale(5)
        golden_hexagon = Polygon(np.array([0.618,1,0]),np.array([1,0,0]),np.array([0.618,-1,0]),np.array([-0.618,-1,0]),np.array([-1,0,0]),np.array([-0.618,1,0]))
        hexagon = RegularPolygon()
        hexagon.scale(3)
        hexagon.rotate(-TAU/4)
        elliptigonTitle = TextMobject("Elliptigon").scale(1.3)
        titleText = input("Enter the title:")
        title = TextMobject(titleText)
        title.move_to(0.5*DOWN)
        title.scale(0.8)

        self.play(GrowFromCenter(ellipse))
        self.play(Transform(ellipse,hexagon))
        self.play(Write(elliptigonTitle))
        self.wait(0.3)
        self.play(ApplyMethod(elliptigonTitle.shift,0.5*UP), run_time=0.8)
        self.play(Write(title), run_time=0.8)
        self.wait(2.9)