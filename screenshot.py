import pyautogui
import keyboard
import pyautogui as pag
from PIL import Image
import pytesseract as tess
tess.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"



# make a screenshot when u press the button "a"
def pressbutton():
    while True:
        if keyboard.is_pressed("a"):
            myScreenshot = pyautogui.screenshot()
            myScreenshot.save(r'C:\Users\Alexandra\Desktop\screenshot\screenshot_1.png')
            break

# find the cordonates of the cursor
def cursorpoz():
    #print(pyautogui.position()) #afiseaza coordonatele cursorului in momentul in care rukezi programu
    #pag.displayMousePosition()  #afiseaza coodonatele cursorului in timp real
    x = 24
    y = 58
    pyautogui.moveTo(x,y)

def cut(l,t,r,b):
   
    img = Image.open(r'C:\Users\Alexandra\Desktop\screenshot\tarkov.png')
    imgCropped = img.crop(box=(l,t,r,b))
    imgCropped.save(r'C:\Users\Alexandra\Desktop\screenshot\tarkov1.png')
    imgCropped.show()

def text():
    img = Image.open(r'C:\Users\Alexandra\Desktop\screenshot\tarkov1.png')
    print('==========================================================================')
    text = tess.image_to_string(img)
    print(text)


def main():
    l = 1250
    t = 143
    r = l+225
    b = t+65
    pressbutton()
    cursorpoz()
    cut(l,t,r,b)
    text()
    
    

if __name__ == "__main__":
    main()

        