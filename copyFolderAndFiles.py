import os
import shutil

rootdir = "C:/Work/sourceCodeTest/amazon_Alexa/avs-device-sdk/avs-device-sdk"
targetDir = "C:/Work/sourceCodeTest/amazon_Alexa/avs-device-sdk-wrapper/avs-device-sdk-wrapper/include2"

# https://stackoverflow.com/questions/1868714/how-do-i-copy-an-entire-directory-of-files-into-an-existing-directory-using-pyth
def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            if not os.path.exists(s):
                shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)

for subdir, dirs, files in os.walk(rootdir):
    currDirName = subdir.split(os.path.sep)[-1]
    if currDirName == 'include':
        try:
            copytree(subdir,targetDir)
        except shutil.Error as e:
            print('Directory not copied. Error: %s' % e)
          # Any error saying that the directory doesn't exist
        except OSError as e:
            print('Directory not copied. Error: %s' % e)
    

