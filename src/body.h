/*
 * body.h
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


#ifndef BODY_H
#define BODY_H

#include "include.h"
#include "signal_parser.h"
#include "file.h"

using namespace std;

class body
{
	public:
	
	vector < string > body_in;
	vector < string > body_out;
	
	HTML_CONFIG config;
	HTML_SIG sig;
	signal_parser sig_parser;
	
	string title;
	string buff_file;
	
	void init ( HTML_CONFIG _config, string file_in, string file_out, string _title );
	void write_file ( string new_file );
};

#endif /* BODY_H */ 
