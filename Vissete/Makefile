.DEFAULT_GOAL := build
vrsn=0.0.1
bld=0

build:
	@echo "[make] Setting version and build numbers in Version.java and pom.xml"
	@sed -i 's:Version = .*;:Version = "$(vrsn)";:' src/main/java/no/boeingjr/vissete/Version.java
	@sed -i 's:Build = .*;:Build = $(bld);:' src/main/java/no/boeingjr/vissete/Version.java
	@sed -i "s:.*<version>.*SNAPSHOT</version>:              <version>$(vrsn)-SNAPSHOT</version>:" pom.xml
	@sed -i "s:.*<Vissete-Version>.*</Vissete-Version>:              <Vissete-Version>$(vrsn)</Vissete-Version>:" pom.xml
	@sed -i "s:.*<Vissete-Build>.*</Vissete-Build>:              <Vissete-Build>$(bld)</Vissete-Build>:" pom.xml
#	@mvn validate
	@mvn package
	@echo "[make] Please verify version number is correctly updated, use \"make version v=X.Y.Z\" and rerun \"make\""
	@grep "Version = " src/main/java/no/boeingjr/vissete/Version.java
	@grep "Build = " src/main/java/no/boeingjr/vissete/Version.java
	@grep "SNAPSHOT" pom.xml
	@grep "Vissete-Version" pom.xml
	@grep "Vissete-Build" pom.xml
	@ln target/Vissete-$(vrsn)-SNAPSHOT.jar target/Vissete.jar

clean:
	@mvn clean
