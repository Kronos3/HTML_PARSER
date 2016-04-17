/*
 * file.hpp
 * 
 * Copyright 2016 Andrei Tumbar <atadmin@Helios>
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


#ifndef __HTML_PARSER_FILE__
#define __HTML_PARSER_FILE__

#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include "_misc_tools.hpp"

using namespace std;

/*! \class File
 *
 * class File is meant to create vector of strings to be used
 * during reading files line by line
 *
 */
class File
{
	public:
	
	/// Empty file constructor
	ifstream file;
	
	/** String with whole file stored affecter File () is
	 * called
	 */
	stringstream text;
	
	/** Used during readline () function
	 * Every time this function is run then currentLine will increase by 1
	 */
	size_t currentLine;
	
	File ( string fileName )
	{
		/// Open the file
		file.open ( fileName.c_str ( ) );
		
		/// Send text from file to text
		text << file.rdbuf();
	}
	
	/// Return a vector of strings with each element as a line in the file
	vector<string> readlines ( )
	{
		vector < string > returnList ( misc::split ( text.str ( ), '\n' ) );
		
		/// Return the generated list
		return returnList;
	}
	
	string read ( const char *endChars="\n" )
	{
		return text.str ( );
	}
	
	/** Return a string of the currentLine in file **/
	string readline ( )
	{
		/// Create a buffer to later be returned
		string buffstr;
		
		vector<string> readFile = readlines ( );
		
		if ( currentLine > readFile.size ( ) )
		{
			/// Set buffstr to line
			buffstr = readFile [ currentLine ];
		}
		
		/// Add one to currentLine
		currentLine++;
		
		/// Return the str
		return buffstr;
	}
	
	/** Get a specific line in the file
	 * Will use readlines to create an array and then
	 * get specific line
	*/
	string get ( int line )
	{
		string buffstr; //!< Create a buffer to later be returned
		
		buffstr = readlines ( ) [line]; /// Set buffstr to line
		
		currentLine++; /// Add one to currentLine
		
		/// Return the str
		return buffstr;
	}
};
#endif
