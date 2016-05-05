CXX = g++
LINKER = g++
INCDIRS = -I.

bin_PROGRAMS = parser
parser_SOURCES = parser.cpp body.cpp body.h file.cpp file.h html_config.hpp include.h _misc_tools.cpp _misc_tools.h option.cpp option.h optionset.h optionset.cpp signal_group.cpp signal_group.h signal_parser.cpp signal_parser.h signal_rewrite.cpp signal_rewrite.h template.cpp template.h template_set.cpp template_set.h template_variable.cpp template_variable.h

exec:
	gcc -o parser $(OBJ)
