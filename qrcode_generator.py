from pyqrcode import *
from png import *

url = pyqrcode.create('https://twitter.com/Jadson_Ricard0')
url.svg('ig-url.svg', scale=10)
url.png('ig-url.png', scale=10, module_color=(127, 17, 224), background=(255, 255, 255, 255))