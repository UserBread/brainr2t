import webbrowser
import pyscreenshot
import pyautogui
import time
import os
import urllib3
from PIL import Image
from PIL import ImageGrab

class ScreenshotHelper:
    def OpenSite(self, url: str):
        webbrowser.open(url, new=1, autoraise=True)


if __name__ == '__main__':
    sh = ScreenshotHelper()
    sh.OpenSite('https://www.reddit.com/r/nosleep/comments/1uekkv5/i_responded_to_a_shady_craigslist_ad_for_a_2d/')
    time.sleep(1.5)
    for i in range(3):
        image = ImageGrab.grab()
        image = image.crop(box=(500, 200, 1300, 1000))
        image.save(f"test{i}.png")
        if open(f'test{i}.png', 'rb').read() == open("empty.png", "rb").read():
            os.remove(f"test{i}.png")
        pyautogui.press('pagedown')
        time.sleep(0.5)
