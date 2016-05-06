CXX = g++
LXX = g++
INCDIRS = .
CFLAGS += -Wall -g

BIN = parser
BARE = parser body file _misc_tools option optionset signal_group signal_parser signal_rewrite template template_set template_variable signal html_sig html_config

OBJECTS = $(patsubst %,%.o, $(BARE))
SOURCES = $(patsubst %,%.cpp, $(BARE))
HEADERS = $(patsubst %,%.h, $(BARE))

.PHONY : all
.DEFAULT_GOAL := all

%.o : %.cpp %.h
	$(CXX) $(CFLAGS) -o $@ -c $< -I$(INCDIRS)

link: $(OBJECTS)
	$(LXX) $(OBJECTS) -o $(BIN)

all: link

clean:
	rm -rf $(OBJECTS)
	rm -rf $(BIN)
