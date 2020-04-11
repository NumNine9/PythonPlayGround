import os
from datetime import datetime
print(os.getcwd())
#os.chdir('c:/Users/Num9/visual basic')
print(os.getcwd())
os.chdir('c:/Users/Num9/visual basic')
#print(os.makedirs('NEW FOLDS/sub-dir'))
#print(os.rmdir('NEW FOLDS/sub-dir'))
#print(os.rmdir('sbu-dir'))
#print(os.stat('Using The OS Module.py'))
#print(os.listdir())
#mod_time = os.stat('Using The OS Module.py').st_mtime
#print(datetime.fromtimestamp(mod_time))
'''for dirpath,dirnames, filenames in os.walk( 'c:/Users/Num9/visual basic'):
    print('Current Path: ')
    print('Directories: ')
    print('Files: ')
    print()
 
'''
os.chdir('c:/Users/Num9')
print(os.environ.get('HOME'))
file_path=os.path.join(os.environ.get('HOME'),'text.txt') #not working
print(file_path)