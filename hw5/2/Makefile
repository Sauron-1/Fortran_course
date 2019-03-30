FC = gfortran
FCFLAGS = -fopenmp
PY = python3
DRAW = draw.py

OBJECTS = global.o routines.o parallel.o main.o
PICTURES = parallel0.eps parallel1.eps parallel2.eps parallel3.eps LW.eps

.PHONY: all clean exe clean_compile
all : exe $(PICTURES)

$(PICTURES) : %.eps : %.dat
	$(PY) $(DRAW) $<

exe : parallel.exe main.exe
	./parallel.exe
	./main.exe

parallel.exe : global.o routines.o parallel.o
	$(FC) global.o routines.o parallel.o $(FCFLAGS) -o $@

main.exe : global.o routines.o main.o
	$(FC) global.o routines.o main.o -o $@

$(OBJECTS) : %.o: %.f90
	$(FC) -c $< -o $@

clean:
	rm *.o *.exe *.dat *.eps *.mod

clean_compile:
	rm *.o *.exe *.mod
