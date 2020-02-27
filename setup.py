import os.path as opath
import platform
import os
import sys

SRC_DIR = opath.join(os.getcwd(), 'src')
BUILD_DIR = opath.join(os.getcwd(), 'build')
LIB_DIR = opath.join(os.getcwd(), 'lib')

CXX = 'clang++' if platform.system() == 'Darwin' else 'g++'
CXX_OPT = '-std=c++11'


SRC_EXT, OBJ_EXT = 'cpp', 'o'
SOURCES, OBJECTS = [], []
for fn in os.listdir(SRC_DIR):
	if not fn.endswith(SRC_EXT):
		continue
	SOURCES.append(opath.join(SRC_DIR, fn))
	OBJECTS.append(opath.join(BUILD_DIR, fn.replace(SRC_EXT, OBJ_EXT)))
UTIL_STAT_LIB = opath.join(LIB_DIR, 'libutil.a')


def getFiles4Comp():
	if not opath.exists(BUILD_DIR):
		os.mkdir(BUILD_DIR)
		assert len(SOURCES) == len(OBJECTS)
		return SOURCES, OBJECTS
	#
	tarSrcs, tarObjs = [], []
	for i in range(len(SOURCES)):
		src_fpath, obj_fpath = SOURCES[i], OBJECTS[i]
		if not opath.exists(obj_fpath) or \
			opath.getctime(obj_fpath) < opath.getmtime(src_fpath):
			tarSrcs.append(src_fpath)
			tarObjs.append(obj_fpath)
	#
	assert len(tarSrcs) == len(tarObjs)
	return tarSrcs, tarObjs


def genStatLib():
	tarSrcs, tarObjs = getFiles4Comp()
	for i in range(len(tarSrcs)):
		src_fpath, obj_fpath = tarSrcs[i], tarObjs[i]
		print("Compile a object file") 
		print("Target file:", src_fpath, "; Pre-req:", obj_fpath) 
		res = os.system('%s -c %s %s -o %s' % (CXX, CXX_OPT, src_fpath, obj_fpath))
		assert res == 0
		print("Build Success!!!") 
	if not opath.exists(UTIL_STAT_LIB) or len(tarSrcs) > 1:
		if not opath.exists(LIB_DIR):
			os.mkdir(LIB_DIR)
		res = os.system("ar rvs %s %s" % (UTIL_STAT_LIB, ' '.join(OBJECTS)))
		assert res == 0
		print("Build Success!!!") 
	else:
		print("The library exists already") 


if __name__ == '__main__':
	if sys.argv[1] == 'genStatLib':
		genStatLib()
	else:
		print("type: python setup.py genStatLib")



	# print("This is the name of the script: ", sys.argv[0]) 
	# print("Number of arguments: ", len(sys.argv)) 
	# print("The arguments are: " , str(sys.argv)) 
