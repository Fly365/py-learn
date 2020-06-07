# encoding=utf8
import tesserocr
from PIL import Image

image = Image.open('CheckCode.jpg')
# 传入L可将图片转化为灰度图像，传入1可将图片二值化处理
image = image.convert('L')
threshold = 127
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
image = image.point(table, '1')
# possibly an invalid tessdata path: D:\development\Anaconda3\/tessdata/
# tessdata整个目录复制到Anaconda3目录下即可
result = tesserocr.image_to_text(image)
print(result)