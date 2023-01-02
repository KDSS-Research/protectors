import random
import re
import tqdm
import os
print('     PyInstaller Hider v1.3\n\n     By KDSS-Research\n\n     Im not responsible for any illegal actions with that tool!\n     That Program can: ')
'''
          - Hide strings
          - PyInstxtractor Bypass
'''
path=''
issaved = False
faker = False
faker_activated = False
global mysettings
phrases=[
'Error allocating decompression buffer',
'Error %d from inflate: %s',
'Error %d from inflateInit: %s',
'Cannot open archive file',
'Could not allocate read buffer',
'Could not read from file',
'Error decompressing %s',
'%s could not be extracted!',
'Failed to write all bytes for %s'
'Could not allocate buffer for TOC.',
'Could not read from file.',
'Error on file',
'Cannot allocate memory for ARCHIVE_STATUS',
'Fatal error detected',
'Error detected',
'%s%s: %s',
'Archive path exceeds PATH_MAX',
'Error opening archive %s',
'Error copying %s',
'%s%s%s%s%s',
'%s%s%s.pkg',
'%s%s%s.exe',
'%s%s%s%s%s%s%s',
'%s%s%s',
'Archive not found: %s',
'Error extracting %s',
'Could not get __main__ module.',
"Could not get __main__ module's dict.",
'%s.py',
'Name exceeds PATH_MAX',
'Failed to unmarshal code object for %s',
'Failed to execute script %s',
'Path of manifest-file (%s) length exceeds buffer[%d] space',
'pyi-windows-manifest-filename',
'Cannot open self %s or archive %s',
'Failed to get executable path.',
'Failed to convert executable path to UTF-8.',
'Failed to get address for Py_DontWriteBytecodeFlag',
'Failed to get address for Py_FileSystemDefaultEncoding',
'Failed to get address for Py_FrozenFlag',
'Failed to get address for Py_IgnoreEnvironmentFlag',
'Failed to get address for Py_NoSiteFlag',
'Failed to get address for Py_NoUserSiteDirectory',
'Failed to get address for Py_OptimizeFlag',
'Failed to get address for Py_VerboseFlag',
'Failed to get address for Py_BuildValue',
'Failed to get address for Py_DecRef',
'Failed to get address for Py_Finalize',
'Failed to get address for Py_IncRef',
'Failed to get address for Py_Initialize',
'Failed to get address for Py_SetPath',
'Failed to get address for Py_GetPath',
'Failed to get address for Py_SetProgramName',
'Failed to get address for Py_SetPythonHome',
'Failed to get address for Py_SetProgramName',
'Failed to get address for PyDict_GetItemString',
'Failed to get address for PyErr_Clear',
'Failed to get address for PyErr_Occurred',
'Failed to get address for PyErr_Print',
'Failed to get address for PyErr_Fetch',
'Failed to get address for PyErr_Restore',
'Failed to get address for PyImport_AddModule',
'Failed to get address for PyImport_ExecCodeModule',
'Failed to get address for PyImport_ImportModule',
'Failed to get address for PyList_Append',
'Failed to get address for PyList_New',
'Failed to get address for PyLong_AsLong',
'Failed to get address for PyModule_GetDict',
'Failed to get address for PyObject_CallFunction',
'Failed to get address for PyObject_CallFunctionObjArgs',
'Failed to get address for PyObject_SetAttrString',
'Failed to get address for PyObject_Str',
'Failed to get address for PyRun_SimpleString',
'Failed to get address for PySys_AddWarnOption',
'Failed to get address for PySys_SetArgvEx',
'Failed to get address for PySys_GetObject',
'Failed to get address for PySys_SetObject',
'Failed to get address for PySys_SetPath',
'Failed to get address for PyEval_EvalCode',
'Failed to get address for PyMarshal_ReadObjectFromString',
'Failed to get address for PyUnicode_FromString',
'Failed to get address for Py_DecodeLocale',
'Failed to get address for PyMem_RawFree',
'Failed to get address for PyUnicode_FromFormat',
'Failed to get address for PyUnicode_Decode',
'Failed to get address for PyUnicode_DecodeFSDefault',
'Failed to get address for PyUnicode_AsUTF8',
'Reported length (%d) of DLL name (%s) length exceeds buffer[%d] space',
'Path of ucrtbase.dll (%s) length exceeds buffer[%d] space',
'Path of DLL (%s) length exceeds buffer[%d] space',
"Error loading Python DLL '%s'.",
'Failed to convert Wflag %s using mbstowcs (invalid multibyte string)',
'Failed to convert argv to wchar_t',
'Failed to convert progname to wchar_t',
'Failed to convert pyhome to wchar_t',
'Failed to convert pypath to wchar_t',
'sys.path (based on %s) exceeds buffer[%d] space',
'Error detected starting Python VM.',
'Failed to get _MEIPASS as PyObject.',
'mod is NULL - %s',
'%U?%zu',
'Installing PYZ: Could not get sys.path',
'Failed to append to sys.path',
'LOADER: Failed to convert runtime-tmpdir to a wide string.',
'LOADER: Failed to expand environment variables in the runtime-tmpdir.',
'LOADER: Failed to obtain the absolute path of the runtime-tmpdir.',
'LOADER: Failed to set the TMP environment variable.',
'INTERNAL ERROR: cannot create temporary directory!',
'WARNING: file already exists but should not: %s',
'Error creating child process!',
'No error messages generated.',
'PyInstaller: FormatMessageW failed.',
'Out of memory.',
'PyInstaller: pyi_win32_utils_to_utf8 failed.',
'Failed to get ANSI buffer size.',
'Failed to encode wchar_t as UTF-8.',
'Failed to get wchar_t buffer size.',
'Failed to decode wchar_t from UTF-8',
'Failed to get UTF-8 buffer size.',
'starting Python VM.',
'incorrect header check',
'unknown compression method',
'invalid window size',
'unknown header flags set',
'header crc mismatch',
'invalid block type',
'invalid stored block lengths',
'too many length or distance symbols',
'invalid code lengths set',
'invalid bit length repeat',
'invalid code -- missing end-of-block',
'invalid literal/lengths set',
'invalid distances set',
'invalid literal/length code',
'invalid distance code',
'invalid distance too far back',
'incorrect data check',
'incorrect length check',
'Failed to get address for PyObject_GetAttrString',
'Could not allocate buffer for TOC.',
]
print('     Base currently contains',str(len(phrases)),'exposing lines.')
path = input('\nEnter EXE path: ')
if not os.path.exists(path):
    print('File not exists!')
    input()
    exit()
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

for i in tqdm.tqdm(range(len(phrases))):
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
print('Checking for pyinstaller signatures...')
if b'MEI\014\013\012\013\016' in mem:
    print('Found signatures, removing...')
    try:
        forgen = generate(len(b'MEI\014\013\012\013\016')).encode()
        mem = re.sub(b'MEI\014\013\012\013\016', forgen, mem)
    except Exception as e:
        if issaved == True:
            print('Error ocurred! Saved to file "errorlog.bin", you can send it to me.')
            open('errorlog.bin','a').write(str(e)+'\n')
        else:
            print('Error ocurred! Saved to file "errorlog.bin", you can send it to me.')
            open('errorlog.bin','w').write(str(e)+'\n')
            issaved = True
if count == 0 and b'MEI\014\013\012\013\016' not in mem:
    print('Nothing to patch. Patch not applied!')
else:       
    open(path.replace('.exe','')+'_hided.exe','wb').write(mem)
    print('Work completed! Saved as '+path.replace('.exe','')+'_hided.exe')
input()