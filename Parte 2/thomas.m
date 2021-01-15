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