SIZE = WIDTH, HEIGHT = 1000, 600
FPS = 50
PLATFORM_WIDTH = 32  # ширина платформ
PLATFORM_HEIGHT = 32
PLATFORM_COLOR = "#FF6262"
SPEED = 5
JUMP_POWER = 10
COLOR = "#888888"
GRAVITY = 0.35
PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32
PLATFORM_COLOR = "#FF6262"
ANIMATION_DELAY = 1  # скорость смены кадров
ANIMATION_RIGHT = [('data/r1.png'),
                   ('data/r2.png'),
                   ('data/r3.png'),
                   ('data/r4.png'),
                   ('data/r5.png')]
ANIMATION_LEFT = [('data/l1.png'),
                  ('data/l2.png'),
                  ('data/l3.png'),
                  ('data/l4.png'),
                  ('data/l5.png')]
ANIMATION_JUMP_LEFT = [('data/jl.png', 1)]
ANIMATION_JUMP_RIGHT = [('data/jr.png', 1)]
ANIMATION_JUMP = [('data/j.png', 1)]
ANIMATION_STAY = [('data/0.png', 1)]
LEVELS = {
    1:
        [
            "-----------------------------------------------------------------------------------------",
            "-                                                                                       -",
            "-                       --                                                              -",
            "-        *                                                                              -",
            "-            d                                                                          -",
            "-            --                                                                         -",
            "--                                                                                      -",
            "-                                                                                       -",
            "-                   ----     ---                                                        -",
            "-                                                                                       -",
            "--                                                                                      -",
            "-            *                                                                          -",
            "-                            ---                                                        -",
            "-                                                                                       -",
            "-                                                                                       -",
            "-  *   ---                  *                              *                            -",
            "-                                                                                       -",
            "-   -------         ----                                    ---                         -",
            "-                                                                                       -",
            "-lllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll-"],
    2:
        [
            "-----------------------------------------------------------------------------------------",
            "-                                                                                       -",
            "-                       --                                                              -",
            "-        *                                                                              -",
            "-            d                                                                          -",
            "-            --                                                                         -",
            "--                                                                                      -",
            "-                                                                                       -",
            "-                   ----     ---                                                        -",
            "-                                                                                       -",
            "--                                                                                      -",
            "-            *                                                                          -",
            "-                            ---                                                        -",
            "-                                                                                       -",
            "-                                                                                       -",
            "-  *   ---                  *                              *                            -",
            "-                                                                                       -",
            "-   -------         ----                                    ---                         -",
            "-                                                                                       -",
            "-lllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll-"],
    3:
        [
            "---------------------------------------------------------------------------------------",
            "-                                                                                     -",
            "-                                                                                     -",
            "-        *                                                                            -",
            "-            d                                                                        -",
            "-            --                                                                       -",
            "--                                                       *                            -",
            "-                                                                                     -",
            "-                   ----     ---                              ---                     -",
            "-                                   -              --               *                 -",
            "--                                             *                         ---          -",
            "-            *                             ---                                        -",
            "-                                                                                     -",
            "-                                                                             *       -",
            "-                                                                            --       -",
            "-  *   ---                  *                              *                          -",
            "-                                ---                                      ---         -",
            "-   -------         ----                 ---        ---         ---                   -",
            "-                                                                                     -",
            "-lllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll-"]

}
