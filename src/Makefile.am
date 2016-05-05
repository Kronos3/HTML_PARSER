CXX = g++
LXX = g++
INCDIRS = .

bin_PROGRAMS = parser
parser_SOURCES = parser.cpp body.cpp file.cpp _misc_tools.cpp option.cpp optionset.cpp signal_group.cpp signal_parser.cpp signal_rewrite.cpp template.cpp template_set.cpp template_variable.cpp

OBJ: $(parser_SOURCES)
	$(CXX) $(parser_SOURCES) -I $(INCDIRS)

all: OBJ
	$(LXX) -o $(bin_PROGRAMS) *.o

clean:
	rm *.o
