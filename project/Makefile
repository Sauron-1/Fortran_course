FC = gfortran
PY = python3
PLOTER = plot.py
TEX = xelatex

OBJPATH = obj
VPATH = src

objects = parameters.o runge_kutta.o functions.o equation.o solve_global.o solve.o
exe = solve.out
data = test.dat
pict = xi-theta.eps xi-s.eps
report = report.pdf

.PHONY: all
all: $(report)

$(objects): %.o: %.f90
	$(FC) -c $< -o $(OBJPATH)/$@

$(exe): $(objects)
	$(FC) $(addprefix $(OBJPATH)/, $(objects)) -o $@

$(data): $(exe)
	./$(exe)

$(pict): $(data)
	$(PY) $(PLOTER)

$(report): $(pict) report.tex
	$(TEX) report.tex

.PHONY: clean
clean:
	rm -f *.mod
	rm -f $(OBJPATH)/*
	rm -f $(data)
	rm -f $(pict)
	rm -f $(exe)
	rm -f report.aux report.out report.log report.pdf

.PHONY: clean_cmpl
clean_cmpl:
	rm -f *.mod
	rm -f $(OBJPATH)/*
	rm -f report.aux report.out report.log
