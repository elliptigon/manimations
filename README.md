# manimations
A collection of manim based animations used for elliptigon videos

## Generating an Intro

To generate an intro, make sure you have manim installed properly, then clone the repo and run the following command:

```
make title="YOUR_TITLE_HERE"
```

To preview an intro scene at lower resolution and framerate, run the following instead:

```
make preview title="YOUR_TITLE_HERE"
```

Use this for faster rendering when trying out new intros, but make sure the final render is high quality.

You can also use any other flags supported by manim by setting the `MANIM_OPTS` variable. For example, this command generates the intro and skips to the last frame in the scene:

```
make title="YOUR_TITLE_HERE" MANIM_OPTS=-s
```

