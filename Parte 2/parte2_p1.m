function [x, y] = parte2_p1(p, q, f, N, a, b, y0, yn)

  % Calculamos h
  h = (b-a)/N;
  
  % Obtenemos el vector x
  x = [a+h:h:b-h];
  
  % Construimos la matriz 
  A = zeros(N-1);
  for i=1:N-1
    if i==1
      A(i,i) = 2+(h^2)*q(x(i));
      A(i,i+1) = (h/2)*p(x(i))-1;
    elseif i==N-1
      A(i,i-1) = (-h/2)*p(x(i))-1;
      A(i,i) = 2+(h^2)*q(x(i));
    else
      A(i,i-1) = (-h/2)*p(x(i))-1;
      A(i,i) = 2+(h^2)*q(x(i));
      A(i,i+1) = (h/2)*p(x(i))-1;
    endif
  endfor
  
  % Construimos el vector d
  e0 = ((h/2)*p(x(1))+1)*y0;
  eN = ((-h/2)*p(x(N-1))+1)*yn;
  d = zeros(1,N-1);
  for j=1:N-1
    d(j) = -(h^2)*f(x(j));
    if j==1
      d(j) = d(j) + e0;
    elseif j==N-1
      d(j) = d(j) + eN;
    endif
  endfor
  A
  d
  
  % Con la matriz construida obtenemos los valores por medio del método Thomas
  y = thomas(A,d, N-1);
  
  
endfunction
