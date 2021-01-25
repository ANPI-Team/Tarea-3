function funs = parte2_p2
  
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
  
  % Calculamos los valores dados por el polinomio de lagrange
  polX   = a:((b-a)/(N*10)):b;
  polY   = zeros(1, length(polX));

  for i=1:length(polX)
    polY(i) = lagPol(polX(i), x, y);
  endfor

  plot(polX, polY, 'b',x, y, 'or');
  
  % Cambiamos el formato para mostrar mayor precision en el error 
  format long;
  error = errorLagrange(y0, polY(1))
 
endfunction
  
function y = lagPol(x, xVector, yVector)
  
  % Calculamos  los puntos por medio de la interpolacion de Lagrange 
  N   = length(xVector);
  sum = 0;
  for i=1:N
      p=1;
      for j=1:N
          if j~=i
              p = p*(x-xVector(j))/(xVector(i)-xVector(j));
          end
      end
      sum = sum + p*yVector(i);
  end
  y=sum;
  
endfunction

function error = errorLagrange(yOriginal, yAproximado)
  
  % Calculamos el error relativo 
  error = abs(yOriginal-yAproximado)/abs(yOriginal);
  
endfunction



