function funs = parte2_p2
  
  warning('off', 'all');
  
  % Formato para mostrar los datos 
  format short;
  
  % Ingresamos las funciones y los valores 
  p  = @(x) -1/x;
  q  = @(x) (1/(4*x^2))-1;
  f  = @(x) 0;
  N  = 8;
  a  = 1;
  b  = 6;
  y0 = 1;
  yN = 0;
  
  % Calculamos los puntos 'x' y 'y' con la función edo2
  [x, y] = parte2_p1.edo2(p, q, f, N, a, b, y0, yN)
  
  % Calculamos el polinomio de lagrange 
  polSym = lagrangeP(x,y);
  polCoefficients = sym2poly(polSym)
  polFunction = function_handle(polSym);
  
  % Creamos los puntos en x para el polinomio
  polX   = a:((b-a)/(N*10)):b;
  
  % Calculamos los valores en y dados por el polinomio de lagrange
  polY   = polFunction(polX);
  
  % Mostramos la grafica
  plot(polX, polY, 'b',x, y, 'or');
  
  % Cambiamos el formato para mostrar mayor precision en el error 
  format long;
  yAproximado = polFunction(x);
  errorRelativo = errorLagrange(y, yAproximado)  
  display("\n\nJustificación: El error asociado al polinomio es de orden  de 10(-8) por lo que se puede considerar una buena aproximacion a la funcion.")
 
endfunction

function p = lagrangeP(x, y)
  % Calculamos el polinomio de interpolacion
  syms xsym;
  % Inicialmos el polinomio en 0
  p = 0;
  for i=1:length(x)
    % Calculamos el L(i)
    L = 1;
    for j=1:length(x)
      if j~=i
        L = L*((xsym-x(j))/(x(i)-x(j)));
      endif
    endfor
    L = L*y(i);
    % Sumamos el L(i) al polinomio
    p = p+L;
  endfor
endfunction

function error = errorLagrange(yOriginal, yAproximado)
  
  % Calculamos el promedio del error relativo de los puntos
  error = 0;
  for i=1:length(yOriginal)-1
    error = error + abs(yOriginal(i)-yAproximado(i))/abs(yOriginal(i));
  endfor
  error = error/(length(yOriginal)-1);
  
endfunction




