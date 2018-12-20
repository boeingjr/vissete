.DEFAULT_GOAL := build
v=0.0.0

build:
	@python tools/incrementbuild.py
	@$(MAKE) -C Vissete build

run:
	@java -jar Vissete/target/Vissete.jar

clean:
	@$(MAKE) -C Vissete clean

version:
	@python tools/version.py $(v)

