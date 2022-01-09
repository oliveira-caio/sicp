#include <stdio.h>

typedef struct
{
  int num;
  int den;
} rational;

int my_gcd(int a, int b)
{
  if (b == 0)
    return a;

  if (a > b)
    return my_gcd(b, a % b);

  return my_gcd(a, b % a);
}

void make_rational(rational *r, int x, int y)
{
  int gcd;

  if (y < 0)
    {
      x = -x;
      y = -y;
    }

  if (x > 0)
    gcd = my_gcd(x, y);
  else
    gcd = my_gcd(-x, y);

  r->num = x / gcd;
  r->den = y / gcd;

  return;
}

int numerator(rational *r)
{
  return r->num;
}

int denominator(rational *r)
{
  return r->den;
}

void print_rational(rational *r)
{
  printf("%d / %d\n", r->num, r->den);
  return;
}

int main()
{
  rational one_half;

  make_rational(&one_half, -1, -2);
  print_rational(&one_half);

  return 0;
}
