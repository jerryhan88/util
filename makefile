SRC_DIR := ./src
BUILD_DIR := ./build
LIB_DIR := ./lib

CXX = clang++
CXX_OPT := -std=c++11

SRC_EXT := cpp
OBJ_EXT := o
SOURCES := $(shell find $(SRC_DIR) -type f -name *.$(SRC_EXT))
OBJECTS := $(patsubst $(SRC_DIR)/%,$(BUILD_DIR)/%,$(SOURCES:.$(SRC_EXT)=.$(OBJ_EXT)))

UTIL_STAT_LIB := $(LIB_DIR)/libutil.a

all: $(UTIL_STAT_LIB)
	@mkdir -p $(dir $(UTIL_STAT_LIB))
	ar rvs $(UTIL_STAT_LIB) $(OBJECTS)
	@echo "Build Success!!!"

echoTest:
	@echo "echo TEST"

#Compile each .cpp file
$(BUILD_DIR)/%.$(OBJ_EXT): $(SRC_DIR)/%.$(SRC_EXT)
	@mkdir -p $(dir $@)
	@echo "Compile a object file"
	@echo "Target file:" $@ "; Pre-req:" $<
	$(CXX) -c $(CXX_OPT) $< -o $@
	@echo "Build Success!!!"
	@echo ""

$(UTIL_STAT_LIB): $(OBJECTS)
	@mkdir -p $(dir $(UTIL_STAT_LIB))
	ar rvs $(UTIL_STAT_LIB) $(OBJECTS)
	@echo "Build Success!!!"

clean:
	@rm -rf $(BUILD_DIR)
	@rm -rf $(LIB_DIR)