function funs = parte2_p1
  
  funs.edo2   = @edo2;
  funs.thomas = @thomas;
  
end

function [x, y] = edo2(p, q, f, N, a, b, y0, yn)
    
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
    y = thomas(A, d, N-1);
    
    % Agregamos los extremos
    x = [a,x,b];
    y = [y0,y,yn];
    
endfunction

function y = thomas(A, d, N)
  
  % Construimos vectores p y q 
  p = zeros(1,N-1);
  q = zeros(1,N);
  p(1) = A(1,2)/A(1,1);
  q(1) = d(1)/A(1,1);
  for i=2:N-1
    p(i) = A(i,i+1)/(A(i,i)-p(i-1)*A(i,i-1));
    q(i) = (d(i)-q(i-1)*A(i,i-1))/(A(i,i)-p(i-1)*A(i,i-1));
  endfor
  q(N) = (d(N)-q(N-1)*A(N,N-1))/(A(N,N)-p(N-1)*A(N,N-1));
  
  % Obtenemos la solucion 
  y = zeros(1, N);
  y(N) = q(N);
  for i=N-1:-1:1
    y(i) = q(i)-p(i)*y(i+1); 
  endfor

endfunction