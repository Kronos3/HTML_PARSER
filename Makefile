SOURCEDIR=src

.PHONY : subsystem
.DEFAULT_GOAL := subsystem

subsystem:
	$(MAKE) -C $(SOURCEDIR)

clean:
	$(MAKE) clean -C $(SOURCEDIR)
