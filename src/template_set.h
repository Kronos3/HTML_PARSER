/*
 * template_set.h
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


#ifndef TEMPLATE_SET_H
#define TEMPLATE_SET_H

#include "include.h"
#include "template_variable.h"

using namespace std;

class template_set
{
	public:
		vector < template_variable > template_list;
		vector < string > names;
		
		void add ( template_variable var );
		template_variable operator [] ( string name );
};

#endif /* TEMPLATE_SET_H */ 
