#include <stdio.h>

long exp_mod(int base, int power, int n)
{
  if (power == 0)
    return 1;
  
  if (power % 2)
    return (base * exp_mod(base, power - 1, n)) % n;

  long aux = exp_mod(base, power / 2, n);
  return (aux * aux) % n;
}

int is_carmichael(int n)
{
  for (int i = 1; i < n; i++)
      if (exp_mod(i, n, n) != i)
	return 0;

  return 1;
}

int main()
{

  if (!is_carmichael(4))
    printf("%d is not carmichael\n", 4);
  
  if (is_carmichael(561))
    printf("%d is carmichael\n", 561);

  if (is_carmichael(1105))
    printf("%d is carmichael\n", 1105);

  if (is_carmichael(1729))
    printf("%d is carmichael\n", 1729);

  if (is_carmichael(2465))
    printf("%d is carmichael\n", 2465);

  if (is_carmichael(2821))
    printf("%d is carmichael\n", 2821);

  if (is_carmichael(6601))
    printf("%d is carmichael\n", 6601);
  
  return 0;
}
