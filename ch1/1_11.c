#include <stdio.h>

int f_rec(int n)
{
  if (n < 3) return n;
  return f_rec(n - 1) + 2*f_rec(n - 2) + 3*f_rec(n - 3);
}

int f_true_iter(int n)
{
  if (n < 3) return n;
  int a = 0, b = 1, c = 2, ans;

  for(int i = 3; i <= n; i++)
    {
      ans = c + 2*b + 3*a;
      int aux = b;
      b = c;
      a = aux;
      c = ans;
    }

  return ans;
}

int f_iter_rec(int n, int a, int b, int c, int cont)
{
  if (n < 3) return n;
  if (cont > n) return c;
  
  int ans = c + 2*b + 3*a;
  int aux = b;
  b = c;
  a = aux;
  c = ans;

  return f_iter_rec(n, a, b, c, cont + 1);
}

int main()
{
  printf("%d %d %d\n", f_rec(10), f_true_iter(10), f_iter_rec(10, 0, 1, 2, 3));

  return 0;
}
