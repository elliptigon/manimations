title = "ENTER TITLE HERE"
MANIM_OPTS = 

all:
	echo $(title) | manim intro.py IntroAnimationScene -p $(MANIM_OPTS)

preview:
	echo $(title) | manim intro.py IntroAnimationScene -pl $(MANIM_OPTS)