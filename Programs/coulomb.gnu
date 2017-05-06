set yrange [-100:0]
set data style lines
set ylabel 'Energy (h)'
set xlabel 'x (au)'
plot 'coulomb.dat' using 1:2 title 'V = 1/x', 'coulomb.dat' using 1:3 title 'Root 1', 'coulomb.dat' using 1:4 title 'Root 2', 'coulomb.dat' using 1:5 title 'Root 3'
pause -1
set term post color solid
set output 'coulomb.eps'
replot

