/*
  this is a terrible represenation because 2^a and 3^b are very large numbers
  even for small a and b.
*/

#include <stdio.h>

int my_pow(int base, int power)
{
  if (power == 1)
    return base;

  if (power % 2)
    return base * my_pow(base, power-1);

  return my_pow(base, power/2) * my_pow(base, power/2);
}

int cons(int a, int b)
{
  return my_pow(2, a) * my_pow(3, b);
}

int car(int n)
{
  if (n % 2)
    return 0;
  
  return 1 + car(n / 2);
}

int cdr(int n)
{
  if (n % 3)
    return 0;

  return 1 + cdr(n / 3);
}

int main(int argc, char *argv[])
{
  int x = 17, y = 7;
  printf("(%d, %d)\n", car(cons(x, y)), cdr(cons(x, y)));
  
  return 0;
}
