from PIL import Image
import subprocess

def cleanFile(filePath,newFilePath):
    img = Image.open(filePath)

    #对图片进行阈值过滤，然后保存
    img = img.point(lambda x: 0 if x < 143 else 255)
    img.save(newFilePath)

    #调用系统的tesserct命令对图片进行OCR识别
    subprocess.call(["tesseract",newFilePath,"output"])

    #打开文件读取结果
    file = open("output.txt","r")
    print(file.read())
    file.close()

cleanFile("tess2.jpg","tess2clean.png")