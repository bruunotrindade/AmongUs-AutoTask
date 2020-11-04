import pyautogui
from PIL import ImageGrab, Image, ImageOps
import time
import keyboard
from settings import *
import tensorflow.keras
import numpy as np
import datetime

def load_model_ocr():
    print('Carregando o modelo do OCR...')
    np.set_printoptions(suppress=True)
    model = tensorflow.keras.models.load_model('./keras_model.h5')
    print('Modelo carregado...')
    return model


def compare_pixel_color(image, pixels, colorMin, colorMax=None):
    R, G, B = image.getpixel(pixels)

    result = (R >= colorMin[0] and G >= colorMin[1] and B >= colorMin[2])

    if colorMax is not None:
        result = result and (R <= colorMin[0] and G <= colorMin[1] and B <= colorMin[2])

    return result

model_ocr = load_model_ocr()

while True:
    if keyboard.is_pressed(TASK_CHOICES[WIRE]["KEY_PRESS"]):
        image = ImageGrab.grab()

        if compare_pixel_color(image, TASK_CHOICES[WIRE]["START_PIXEL_POS"], TASK_CHOICES[WIRE]["START_PIXEL_COLOR"], 
            TASK_CHOICES[WIRE]["START_PIXEL_COLOR"]):
            
            print("FAZENDO OS FIOS...")
            pyautogui.moveTo(1920/2, 1080/2)
            time.sleep(0.001)

            for y_left in TASK_CHOICES[WIRE]["Y_POS"]:
                left_R, left_G, left_B = image.getpixel((TASK_CHOICES[WIRE]["LEFT_SIDE_COLOR"], y_left))

                print(f"LEFT[{y_left}]=> R={left_R}, G={left_G}, B={left_B}")

                pyautogui.moveTo(TASK_CHOICES[WIRE]["LEFT_SIDE_CLICK"], y_left)

                for y_right in TASK_CHOICES[WIRE]["Y_POS"]:
                    right_R, right_G, right_B = image.getpixel((TASK_CHOICES[WIRE]["RIGHT_SIDE_COLOR"], y_right))
                    if left_R == right_R and left_G == right_G and left_B == right_B:
                        print(f"ENCONTRADO => {y_right}")
                        pyautogui.dragTo(TASK_CHOICES[WIRE]["RIGHT_SIDE_CLICK"], y_right, duration=0.2, 
                            button="left", tween=pyautogui.easeOutQuad)
                        break

                print()
        else:
            print("FIOS NÃO ENCONTRADOS")
            time.sleep(0.5)

    elif keyboard.is_pressed(TASK_CHOICES[CARD]["KEY_PRESS"]):
        image = ImageGrab.grab()
        if compare_pixel_color(image, TASK_CHOICES[CARD]["START_PIXEL_POS"], TASK_CHOICES[CARD]["START_PIXEL_COLOR"]):
            print("CARTAO...")
            pyautogui.click(TASK_CHOICES[CARD]["HIDE_CARD_POS"])
            time.sleep(0.6)
            pyautogui.moveTo(TASK_CHOICES[CARD]["CARD_POS_START"])
            pyautogui.dragTo(TASK_CHOICES[CARD]["CARD_POS_END"], duration=1.0, button="left", 
                tween=pyautogui.easeInOutQuad)
        else:
            print("CARTÃO NÃO ENCONTRADO")
            time.sleep(0.5)

    elif keyboard.is_pressed(TASK_CHOICES[REACTOR_NUMBERS]["KEY_PRESS"]):
        size = TASK_CHOICES[REACTOR_NUMBERS]["SQUARE_SIZE"]
        ind = 1
        positions = {}

        for square in TASK_CHOICES[REACTOR_NUMBERS]["SQUARES_MIN_POS"]:
            #ImageGrab.grab(bbox=(square[0], square[1], square[0]+size, square[1]+size)).save("img"+str(ind)+"-"+str(datetime.datetime.now().timestamp())+".jpg", "JPEG")
            image = ImageGrab.grab(bbox=(square[0], square[1], square[0]+size, square[1]+size))
            ind += 1

            data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
            size_img = (224, 224)
            image = ImageOps.fit(image, size_img, Image.ANTIALIAS)

            image_array = np.asarray(image)
            normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

            data[0] = normalized_image_array

            prediction = model_ocr.predict(data)
            number = np.argmax(prediction)
            print(f'Predicted Number: {number + 1}')

            middle_size = size / 2
            pos_click = (square[0] + middle_size, square[1] + middle_size)

            positions[number] = pos_click
        
        # Clicando na ordem certa
        for i in range(10):
            print(f'Clicando em: {i+1}')
            pyautogui.click(positions[i])
            time.sleep(0.1)



