#encoding=utf-8
import sys
import posixpath 
import ntpath
import macpath
#
# emulate "import os.path" (sort of)...

if sys.platform == "win32":
    
    pathmodule = ntpath
elif sys.platform == "mac" or sys.platform == "darwin":
    
    pathmodule = macpath
else:
    # assume it's a posix platform
    pathmodule = posixpath


print 'sys.platform ',sys.platform

print 'posixpath ',posixpath
print 'ntpath ',ntpath
print 'macpath ',macpath


