#include <stdio.h>
#include <stdlib.h>
#include <time.h>

long exp_mod(int base, int power, int n)
{
  if (power == 0)
    return 1;

  if (power % 2)
    return (base * exp_mod(base, power - 1, n)) % n;

  long aux = exp_mod(base, power / 2, n);
  if (aux != 1 && aux != n - 1 && (aux * aux) % n == 1)
    return 0;
  return (aux * aux) % n;
}

int miller_rabin_test(int n, int k)
{
  srand(time(NULL));
  
  for (int i = 0; i < k; i++)
    {
      int r = 1 + (rand() % (n - 1));
      if (exp_mod(r, n - 1, n) != 1)
	return 0;
    }

  return 1;
}

int main()
{
  for (int i = 2; i < 100; i++)
      if (miller_rabin_test(i, 10))
	printf("%d is a prime number according to miller-rabin test.\n", i);

  return 0;
}
