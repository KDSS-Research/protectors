import random
import re
print('     Nuitka Hider v1.0\n\n     By KDSS-Research\n\nIm not responsible for any illegal actions with that tool!')
path=''
issaved = False
global mysettings
phrases=[
'NUITKA_ONEFILE_PARENT',
"Error, couldn't runtime expand directory spec",
'Failed to send CTRL-C to child process.',
'Error, failed to locate onefile filename.',
'Error, failed to register signal handler.',
'Error, failed to access unpacked executable.',
'dont-search-path',
"Error, couldn't runtime expand temporary files.",
"Error, couldn't decode attached data.",
"Error, couldn't read attached data.",
"Error, couldn't find attached data.",
"Error, couldn't allocate memory.",
"Error, couldn't launch child.",
"Error, failed to open ",
"for writing."
]
print('     Base currently contains',str(len(phrases)),'exposing lines.')
path = input('\nEnter EXE path: ')
print('Loading generator')
count = 0
def generate(num):
    result = ''
    for i in range(num):
        result += random.choice("1234567890QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm")
    return result
print('Loading EXE...')
mem = open(path,'rb').read()
print('Starting patching...')
for i in range(len(phrases)):
    if phrases[i].encode() in mem:
        
        try:
            forgen = generate(len(phrases[i])).encode()
            mem = re.sub(b""+phrases[i].encode()+b"", forgen, mem)
        except Exception as e:
            if issaved == True:
                print('Error ocurred! Saved to file "errorlog.bin", you can send it to me.')
                open('errorlog.bin','a').write(str(e)+';{ID='+str(i)+'}\n')
            else:
                print('Error ocurred! Saved to file "errorlog.bin", you can send it to me.')
                open('errorlog.bin','w').write(str(e)+';{ID='+str(i)+'}\n')
                issaved = True
        count += 1
print('Used',str(count)+'/'+str(len(phrases)),'of signatures')
open(path.replace('.exe','')+'_hided.exe','wb').write(mem)
print('Work completed! Saved as '+path.replace('.exe','')+'_hided.exe')
input()