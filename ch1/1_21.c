#include <stdio.h>

int smallest_divisor(int n)
{
  for (int i = 2; i * i <= n; i++)
    {
      if (n % i == 0) return i;
    }
  return n;
}

int main()
{
  printf("%d %d %d\n", smallest_divisor(199),
	 smallest_divisor(1999),
	 smallest_divisor(19999));

  return 0;
}
