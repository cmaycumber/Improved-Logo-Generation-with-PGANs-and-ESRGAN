from PIL import Image
import os, sys

dataSet = sys.argv[1] if len(sys.argv) is 2 else 'logosResized'
resized = dataSet + 'Resized/'
directoryPath = 'images/' + dataSet + '/'
mainPath = os.getcwd() + '/'
finalPath = mainPath + "results/" + resized
path = mainPath + directoryPath
dirs = os.listdir( path )
final_size = int(sys.argv[2]) if len(sys.argv) is 3 else 32

def resize_aspect_fit():
    for item in dirs:
         if item == '.DS_Store':
             continue
         if not os.path.exists(finalPath):
            os.makedirs(finalPath)
         if os.path.isfile(path+item):
             im = Image.open(path+item)
             f, e = os.path.splitext(finalPath+item)
             size = im.size
             ratio = float(final_size) / max(size)
             new_image_size = tuple([int(x*ratio) for x in size])
             im = im.resize(new_image_size, Image.ANTIALIAS)
             new_im = Image.new("RGB", (final_size, final_size))
             new_im.paste(im, ((final_size-new_image_size[0])//2, (final_size-new_image_size[1])//2))
             new_im.save(f + '-resized.png', 'PNG', quality=90)
resize_aspect_fit()

