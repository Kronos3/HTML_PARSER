SOURCEDIR=src

.PHONY : subsystem
.DEFAULT_GOAL := subsystem
ROOT_DIR:=$(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

subsystem:
	$(MAKE) -C $(SOURCEDIR)

clean:
	$(MAKE) clean -C $(SOURCEDIR)

desktop:
	# Making .desktop file
	
	echo "#!/usr/bin/env xdg-open" > $(ROOT_DIR)/html_Parser.desktop
	echo "[Desktop Entry]" >> $(ROOT_DIR)/html_Parser.desktop
	echo "Type=Application" >> $(ROOT_DIR)/html_Parser.desktop
	echo "Version=2.3" >> $(ROOT_DIR)/html_Parser.desktop
	echo "Name=Html Parser" >> $(ROOT_DIR)/html_Parser.desktop
	echo "Comment=GUI for easier web creation" >> $(ROOT_DIR)/html_Parser.desktop
	echo "Exec=$(ROOT_DIR)/html_parser.py >> $(ROOT_DIR)/html_parser.log 2>&1" >> $(ROOT_DIR)/html_Parser.desktop
	echo "Icon=$(ROOT_DIR)/icon.png" >> $(ROOT_DIR)/html_Parser.desktop
	echo "Terminal=true" >> $(ROOT_DIR)/html_Parser.desktop
	echo "Categories=Languages;C++;Python" >> $(ROOT_DIR)/html_Parser.desktop
	echo "Name[en_US]=html_Parser" >> $(ROOT_DIR)/html_Parser.desktop
	
