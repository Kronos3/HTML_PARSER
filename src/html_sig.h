/*
 * html_sig.h
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


#ifndef HTML_SIG_H
#define HTML_SIG_H

#include <iostream>
#include "html_config.h"
#include "signal.h"

using namespace std;

class HTML_SIG
{
	public:
		HTML_CONFIG CONFIG;
		vector < string > file;
		vector < SIGNAL > SIGNALS;
		vector < string > sig_types;
		vector < vector < int > > line_start_end;
		
		void load ( HTML_CONFIG _CONFIG, string _file );
};

#endif /* HTML_SIG_H */ 
