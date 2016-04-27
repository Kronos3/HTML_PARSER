/*
 * template_set.hpp
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

#ifndef __HTML_TEMPLATE_VAR_SET__
#define __HTML_TEMPLATE_VAR_SET__

#include <iostream>
#include "template_variable.hpp"

typedef struct
{
	vector < template_variable > template_list;
	vector < string > names;
	
	void add ( template_variable var )
	{
		template_list.push_back ( var );
		names.push_back ( var.name );
	}
	
	template_variable operator [] ( string name )
	{
		for ( size_t it = 0; it != names.size ( ); it++ )
		{
			if ( names [ it ] == name )
			{
				return template_list [ it ];
			}
		}
		template_variable buff;
		return buff;
	}
} template_set;

#endif
