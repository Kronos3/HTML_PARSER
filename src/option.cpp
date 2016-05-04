/*
 * option.cpp
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


#include "option.h"

using namespace std;

string option::bool_toggle ( string in )
{
	if ( misc::stob ( in ) )
	{
		in = "false";
	}
	else
	{
		in = "true";
	}
	return in;
}

void option::init ( string __long, string _default, string __short = "", string __type = "string", string _desc = "" )
{
	_long = __long;
	_short = __short;
	_type = __type;
	value = _default;
	desc = _desc;
	used = false;
	bool_val = misc::stob ( _default );
}

void option::option_sig ( string op, bool feeded )
{
	vector < string > BUFF ( misc::split ( op, '=', false ) );
	
	if ( BUFF.size ( ) == 1 and _type == "bool" )
	{
		value = bool_toggle ( value );
	}
	else if ( _type != "bool" and BUFF.size ( ) == 1 )
	{
		value = "";
	}
	else
	{
		value = BUFF [ 1 ];
	}
	
	if ( _type == "bool" )
	{
		bool_val = misc::stob ( value );
	}
	
	used = feeded;
}
