#include <stdio.h>
#include <time.h>
#include <stdlib.h>

/*
  computes base^power mod n
*/
long exp_mod(int base, int power, int n)
{
  if (power == 0)
    return 1;

  if (power % 2)
    return (base * exp_mod(base, power - 1, n)) % n;

  long aux = exp_mod(base, power / 2, n);
  return (aux * aux) % n;
}

/*
  n is the number we wanna check is prime and k is the number of random
  numbers we gonna generate in fermat's test.
*/
int fermat_test(int n, int k)
{
  srand(time(NULL));
  
  for (int i = 0; i < k; i++)
    {
      int r = 1 + rand() % (n - 1);
      if (exp_mod(r, n, n) != r)
	  return 0;
    }

  return 1;
}

/*
  a and b are the bound of the search and n is the number of primes you wanna
  find.
*/
void search_for_primes(int a, int b, int n)
{
  int i;
  clock_t start;
  
  if (a % 2)
    i = a;
  else
    i = a + 1;

  for (i; i <= b && n > 0; i += 2)
    {
      start = clock();
      if (fermat_test(i, 10))
	{
	  n--;
	  printf("'prime': %d   \t time taken: %.10lf\n", i,
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
