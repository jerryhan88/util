import os.path as opath
import platform
import os
import sys
from glob import glob

CXX = 'clang++' if platform.system() == 'Darwin' else 'g++'
CXX_OPT = '-std=c++11'

SRC_DIR = opath.join(os.getcwd(), 'src')
BUILD_DIR = opath.join(os.getcwd(), 'build')
LIB_DIR = opath.join(os.getcwd(), 'lib')

SRC_EXT, OBJ_EXT = 'cpp', 'o'
SOURCES = glob(SRC_DIR + '/**/*.%s' % SRC_EXT, recursive=True)
OBJECTS = [fpath.replace('src', 'build').replace(SRC_EXT, OBJ_EXT) for fpath in SOURCES]

UTIL_STL = opath.join(LIB_DIR, 'libutil.a')

def hasFlag(flag):
	for i in range(len(sys.argv)):
		if sys.argv[i] == flag:
			return True
	else:
		return False

def comCPP(src_fpath, obj_fpath):
	if not opath.exists(obj_fpath) or \
		opath.getctime(obj_fpath) < opath.getmtime(src_fpath):
		os.makedirs(opath.dirname(obj_fpath), exist_ok=True)
		print("Start compile") 
		print("Target file:", obj_fpath, "; Pre-req:", src_fpath) 
		res = os.system('%s -c %s %s -o %s' % (CXX, CXX_OPT, src_fpath, obj_fpath))
		assert res == 0
		print("Build Success!!!\n")

def genSTL():
	for i in range(len(SOURCES)):
		src_fpath, obj_fpath = SOURCES[i], OBJECTS[i]
		comCPP(src_fpath, obj_fpath)
	if not opath.exists(UTIL_STL):
		os.makedirs(opath.dirname(UTIL_STL), exist_ok=True)
		print("Build a static library")
		res = os.system("ar rvs %s %s" % (UTIL_STL, ' '.join(OBJECTS)))
		assert res == 0
		print("Successfully build the library\n") 
	else:
		print("The library exists already\n") 


if __name__ == '__main__':
	if len(sys.argv) == 1:
		genSTL()
	else:
		if hasFlag('clean'):
			os.system('rm -rf %s' % BUILD_DIR)
			os.system('rm -rf %s' % LIB_DIR)
		if hasFlag('stl'):
			genSTL()

