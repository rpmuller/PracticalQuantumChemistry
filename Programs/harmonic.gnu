set yrange [0:170]
set data style lines
set ylabel 'Energy (h)'
set xlabel 'x (au)'
plot 'harmonic.dat' using 1:2 title 'V=50*x^2','harmonic.dat' using 1:3 title 'Root 1', 'harmonic.dat' using 1:4 title 'Root 2', 'harmonic.dat' using 1:5 title 'Root 3'
pause -1
set term post color solid
set output 'harmonic.eps'
replot

