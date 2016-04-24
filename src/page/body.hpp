/*
 * body.hpp
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
 
#ifndef __HTML_PARSER_BODY__
#define __HTML_PARSER_BODY__

#include <iostream>
#include "signal_parser.hpp"

using namespace std;

class body
{
	public:
	vector < string > body_in;
	vector < string > body_out;
	
	HTML_CONFIG config;
	HTML_SIG sig;
	signal_parser sig_parser;
	
	void init ( HTML_CONFIG _config, string file_in )
	{
		
		
		config = _config;
		body_in = file_in;
		sig.load ( config, config.file );
		sig_parser.parse ( sig );
		body_out = sig_parser.output_file;
	}
};

#endif
