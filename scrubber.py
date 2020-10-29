import os
import sys
import codecs
from mutagen.mp4 import MP4

# Get directory from first argument or use current directory
if (len(sys.argv) > 1):
    fpath = sys.argv[1]
else:
    fpath = os.path.abspath(os.path.dirname(sys.argv[0]))
    
for fn in os.listdir(fpath):

    fname = os.path.join(fpath, fn)
    if fname.lower().endswith('.mp4'):
        print(fn)
        mp4 = MP4(fname)        
        try:
            mp4.delete()
            mp4.save()
            print('Erased tags')
        except:
            print('No tags')
print('Complete')
