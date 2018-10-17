gnuplot \
    -e "set terminal png" \
    -e "l(x)=a*x+b" \
    -e "s(x)=c*x**2+d*x+e" \
    -e "w(x)=f*x**3+g*x**2+h*x+i" \
    -e "fit l(x) \"salida_incremental.txt\" using 1:2 via a, b" \
    -e "fit s(x) \"salida_incremental.txt\" using 1:2 via c, d, e" \
    -e "fit w(x) \"salida_incremental.txt\" using 1:2 via f, g, h, i" \
    -e "plot \"salida_incremental.txt\" using 1:2 with lines, l(x), s(x), w(x)" > incremental.png

gnuplot \
    -e "set terminal png" \
    -e "l(x)=a*x+b" \
    -e "s(x)=c*x**2+d*x+e" \
    -e "w(x)=f*x**3+g*x**2+h*x+i" \
    -e "r(x)=j*x*log(k*x)/log(2)" \
    -e "fit l(x) \"salida_dc.txt\" using 1:2 via a, b" \
    -e "fit s(x) \"salida_dc.txt\" using 1:2 via c, d, e" \
    -e "fit w(x) \"salida_dc.txt\" using 1:2 via f, g, h, i" \
    -e "fit r(x) \"salida_dc.txt\" using 1:2 via j, k" \
    -e "plot \"salida_dc.txt\" using 1:2 with lines, l(x), s(x), w(x), r(x)" > dc.png


gnuplot \
    -e "set terminal png" \
    -e "l(x)=a*x+b" \
    -e "s(x)=c*x**2+d*x+e" \
    -e "w(x)=f*x**3+g*x**2+h*x+i" \
    -e "fit l(x) \"salida_jarvis.txt\" using 1:2 via a, b" \
    -e "fit s(x) \"salida_jarvis.txt\" using 1:2 via c, d, e" \
    -e "fit w(x) \"salida_jarvis.txt\" using 1:2 via f, g, h, i" \
    -e "plot \"salida_jarvis.txt\" using 1:2 with lines, l(x), s(x), w(x)" > jarvis.png

