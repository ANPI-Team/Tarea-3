function [x,y] = edo_test()
  p = @(x) -x^2;
  q = @(x) 2*x;
  f = @(x) 3+x;
  N = 4;
  a = 0;
  b = 2;
  y0 = 1;
  yN = -1;
  
  [x, y] = parte2_p1(p, q, f, N, a, b, y0, yN);
  
endfunction
