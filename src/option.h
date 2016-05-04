/*
 * option.h
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


#ifndef OPTION_H
#define OPTION_H

#include <iostream>
#include <map>
#include <string>
#include <vector>
#include "_misc_tools.h"

using namespace std;

class option
{
	public:
		string name;
		string _type;
		string value;
		bool bool_val;
		bool used;
		string desc;
		map < string, string > _map;
		
		string _long;
		string _short;
		
		string bool_toggle ( string in );
		void init ( string __long, string _default, string __short, string __type, string _desc );
		void option_sig ( string op, bool feeded );
};

#endif /* OPTION_H */ 
