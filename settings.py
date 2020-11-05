CLOSE = '0'
WIRE = 1
CARD = 2
REACTOR_NUMBERS = 3

TASK_CHOICES = {
    WIRE: {
        "LEFT_SIDE_COLOR": 562,
        "LEFT_SIDE_CLICK": 597,
        "RIGHT_SIDE_COLOR": 1335,
        "RIGHT_SIDE_CLICK": 1276,
        "Y_POS": [271, 459, 646, 827],
        "KEY_PRESS": '1',
        "START_PIXEL_COLOR": (57, 62, 66),
        "START_PIXEL_POS": (534, 166)
    },
    CARD: {
        "HIDE_CARD_POS": (824, 810),
        "CARD_POS_START": (522, 427),
        "CARD_POS_END": (1479, 427),
        "KEY_PRESS": "2",
        "START_PIXEL_COLOR": (220, 220, 220),
        "START_PIXEL_POS": (824, 810)
    },
    REACTOR_NUMBERS: {
        "KEY_PRESS": "3",
        "FRAME_MIN_X": 578,
        "FRAME_MIN_Y": 388,
        "FRAME_MAX_X": 1338,
        "FRAME_MAX_Y": 688,
        "SQUARE_SIZE": 135,
        "SQUARES_MIN_POS": [
            (585, 393), (738, 393), (892, 393),
            (1045, 393), (1198, 393),   
            (585, 550), (738, 550), (892, 550),
            (1045, 550), (1198, 550)
        ]
    }
}