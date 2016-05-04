/*
 * signal_parser.h
 * 
 * Copyright 2016 Andrei Tumbar <atuser@Kronos>
 * 
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 * 
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
 * MA 02110-1301, USA.
 * 
 * 
 */


#ifndef SIGNAL_PARSER_H
#define SIGNAL_PARSER_H

#include "include.h"
#include "html_config.hpp"
#include "signal_group.h"
#include "signal_rewrite.h"
#include "_misc_tools.h"

using namespace std;

class signal_parser
{
	public:
		
		vector < string > input_file;
		vector < string > output_file;
		
		vector < SIGNAL > input_signals;
		vector < string > output_string;
		vector < int > str_len;
		vector < int > sig_line_numbers;
		
		signal_group sig_group;
		
		void parse ( HTML_SIG __input__ );
		void write_out ( );
};

#endif /* SIGNAL_PARSER_H */ 
