from PIL import Image
import glob
import cv2

#picture = Image.open('C:/Users/eliza/Desktop/sample_data/images/last/last.MD,GARRET,B1263-KEETON-LEASE-8,,90100-page-002.jpg')
correct = 0
files = 0
for image_file in glob.iglob('C:/Users/eliza/Desktop/sample_data/images/others/*.jpg'):
        picture = Image.open(image_file)

        pixels = picture.getdata()
        black = 0
        total = len(pixels)
        print(pixels)
        current = 0
        for pixel in pixels:
                current += 1
                if current > total / 3 * 2:
                        if sum(pixel) < 50:
                                black += 1

        #print(image_file)
        files += 1
        if (black / float(total / 3 * 2)) > 0.02:
                print (black / float(total / 3 * 2))
                correct += 1
                print(correct, ' / ', files)
    