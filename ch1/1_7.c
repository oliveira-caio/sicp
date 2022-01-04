#include <stdio.h>
#include <math.h>

int good_guess(double guess, double old_guess, double fraction, double x)
{
  if (fabs(guess - old_guess) < (fraction * guess)) return 1;
  return 0;
}

double improve_guess(double x, double guess)
{
  return (guess + (x / guess)) / 2;
}

double my_sqrt_rec(double x, double guess, double old_guess, double fraction)
{
  if (good_guess(guess, old_guess, fraction, x)) return guess;
  return my_sqrt_rec(x, improve_guess(x, guess), guess, fraction);
}

double my_sqrt(double x, double fraction)
{
  return my_sqrt_rec(x, 1.0, 0, fraction);
}

int main()
{
  double x = 2.0, fraction = 0.0001;
  printf("%lf\n", my_sqrt(x, fraction));

  return 0;
}
