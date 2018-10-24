# what flags you want to pass to the C compiler & linker
INCLUDES = $(shell root-config --cflags)
CXXFLAGS = -g

# this lists the binaries to produce, the (non-PHONY, binary) targets in
# the previous manual Makefile
bin_PROGRAMS = iblsla 
iblsla_SOURCES = MainGui.cc MainGui.hh main.cc HistoReader.cc HistoReader.hh DbTools.cc DbTools.hh ScanDef.cc ScanDef.hh dict.cc dict_pragma.hh Analysis.hh Analysis.cc IVMeasurementPoint.hh Astave.cc Astave.hh Sr1_converter.hh Sr1_converter.cc
iblsla_CXXFLAGS = -Wall -O2 -DBUILD
iblsla_LDFLAGS = $(shell root-config --glibs) -lTreePlayer 

# generate dictonary for MainGui so we can use signals and slots
dict.cc: MainGui.hh
	rootcint -f dict.cc -c MainGui.hh

clean-local:
	-rm dict.cc
	-rm dict.h
