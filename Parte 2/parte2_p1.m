function [x, y] = edo2(p, q, f, N, a, b, y0, yn)
  
  % Calculamos h
  h = (b-a)/N
  
  % Construimos la matriz 
  A = zeros(N)
  for i=1:N
    if i==1
      A(i,i) = 2+(h^2)*q(i)
      A(i,i+1) = (h/2)*p(i)-1
    elseif i==N
      A(i,i-1) = (-h/2)*p(i)-1
      A(i,i) = 2+(h^2)*q(i)
    else
      A(i,i-1) = (-h/2)*p(i)-1
      A(i,i) = 2+(h^2)*q(i)
      A(i,i+1) = (h/2)*p(i)-1
    endif
  endfor
    
  % Construimos el vector d
  e0 = ((h/2)*p(1)+1)*y0
  eN = ((-h/2)*p(N-1)+1)*yn
  d = zeros(1,N)
  for j=1:N
    d(j) = ((-h/2)*p(j)-1)*y(j-1)  +  ( 2+(h^2)*q(j))*y(j)  +  ((h/2)*p(j)-1)*y(j+1)
    if i==1
      d(j) = d(j) + e0
    elseif i==N
      d(j) = d(j) + eN
    endif
  endfor
  
  % Con la matriz construida obtenemos los valores por medio del método Thomas
  x = [a:h:N]
  y = thomas(A,d)
  
endfunction
