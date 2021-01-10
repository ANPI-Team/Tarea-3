function [x,y] = edo_test()
  p = @(x) -1/x;
  q = @(x) 1/(4*x^2) - 1;
  f = @(x) 0;
  N = 8;
  a = 1;
  b = 6;
  y0 = 1;
  yN = 0;
  
  [x, y] = parte2_p1(p, q, f, N, a, b, y0, yN);
  
endfunction
