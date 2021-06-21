from asciimatics.screen import Screen
from asciimatics.scene import Scene
from asciimatics.effects import Print, Cycle
from asciimatics.renderers import StaticRenderer

def demo(screen):
    effects = [
        Print(
            screen, StaticRenderer(images=[r"""ddskdsj ${""" + '1' + r"""} dskdsk"""]) ,
            screen.height // 2 - 8)
    ]
    screen.play([Scene(effects, 500)])

Screen.wrapper(demo)