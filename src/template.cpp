/*
 * template.cpp
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


#include "template.h"

using namespace std;

void Template::init ( HTML_CONFIG _config, string _template_name )
{
	template_name = _template_name;
	template_content = File ( template_name ).readlines ( );
	
	template_out = template_content;
	config = _config;
	
	for ( size_t i = template_out.size ( ) - 1 ; i != 0; i-- )
	{
		int indent = 0;
		if ( template_out [ i ].empty ( ) )
		{
			continue; 
		}
		
		for ( size_t j = 0; j != template_out [ i ].length ( ); j++ )
		{
			if ( template_out [ i ] [ j ] == ' ' or template_out [ i ] [ j ] == '	' )
			{
				indent += 1;
			}
			else
			{
				break;
			}
		}
		if ( template_out [ i ] [ indent ] == '[' )
		{
			template_variable buff;
			buff.init_name ( template_out, i, indent );
			if ( config.variables [ buff.name ] == "$" )
			{
				string buff_str;
				if ( buff.name == "BODY" )
				{
					template_vars.add ( buff );
					continue;
				}
				else if ( buff.name == "TITLE" )
				{
					template_vars.add ( buff );
					continue;
				}
				else if ( buff.name == "CSS" )
				{
					buff_str = config.variables [ "css" ];
				}
				else if ( buff.name == "JS" )
				{
					buff_str = config.variables [ "js" ];
				}
				buff.init ( config.variables [ buff.name ], config, true, buff_str );
			}
			else
			{
				buff.init ( config.variables [ buff.name ], config, false, "" );
			}
			template_out = buff.format_file ( );
			template_vars.add ( buff );
		}
	}
}

vector < string > Template::new_file ( body IN )
{
	string body_file = IN.buff_file;
	string title = IN.title;
	
	vector < string > BUFF = template_out;
	int l = BUFF.size ( );
	for ( vector < string >::iterator i = BUFF.end ( ) - 1; i >= BUFF.begin ( ); i-- )
	{
		int indent = 0;
		l--;
		if ( i->empty ( ) or *i == "\n" )
		{
			continue;
		}
		
		for ( string::iterator j = i->begin ( ); j != i->end ( ); j++ )
		{
			if ( *j == ' ' or *j == '	' )
			{
				indent += 1;
			}
			else
			{
				break;
			}
		}
		if ( i->substr ( indent, 5 ) == "[BODY" )
		{
			template_variable buff;
			buff.init_name ( BUFF, l, indent );
			buff.init ( body_file, config, false, "" );
			BUFF = buff.format_file ( );
		}
		else if ( i->substr ( indent, 6 ) == "[TITLE" )
		{
			template_variable buff;
			buff.init_name ( BUFF, l, indent );
			ofstream temp;
			temp.open ( "title.temp", ios::out | ios::trunc );
			temp << "<title>" + title + "</title>";
			temp.close ( );
			
			buff.init ( "title.temp", config, false, "" );
			BUFF = buff.format_file ( );
			system ( "rm -rf title.temp" );
		}
		i = BUFF.begin ( ) + l;
	}
	return BUFF;
}
