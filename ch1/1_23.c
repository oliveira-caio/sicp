#include <stdio.h>
#include <time.h>

int smallest_divisor(int n)
{
  if (n % 2 == 0) return 2;

  for (int i = 3; i * i <= n; i += 2)
    {
      if (n % i == 0) return i;
    }

  return n;
}

int is_prime(int n)
{
  if (smallest_divisor(n) == n) return 1;
  return 0;
}

/*
  a and b are the bound of the search and n is the number of primes you wanna
  find.
*/
void search_for_primes(int a, int b, int n)
{
  int i;
  clock_t start;

  if (a % 2) i = a;
  else i = a + 1;

  for (i; i <= b && n > 0; i += 2)
    {
      start = clock();
      if (is_prime(i))
	{
	  n--;
	  printf("prime: %d\t time taken: %.10lf\n", i,
		 ((double) (clock() - start)) / CLOCKS_PER_SEC);
	}
    }

  return;
}

int main()
{
  search_for_primes(1000, 10000, 3);
  search_for_primes(10000, 100000, 3);
  search_for_primes(100000, 1000000, 3);
  search_for_primes(1000000, 10000000, 3);
  
  return 0;
}
