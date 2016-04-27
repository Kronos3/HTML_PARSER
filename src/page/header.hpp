/*
 * header.hpp
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
 
#ifndef __HTML_PARSER_HEADER__
#define __HTML_PARSER_HEADER__

#include <iostream>
#include "../config/html_config.hpp"

using namespace std;

class header
{
	public:
	
	string source_file;
	vector < string > content;
	
	vector < string > header_out;
	
	HTML_CONFIG config;
	
	void init ( HTML_CONFIG _config, string _source_file, vector < string > _header_out )
	{
		config = _config;
		source_file = _source_file;
		content = File ( _source_file ).readlines ( );
		
		header_out = _header_out;
	}
};

#endif
