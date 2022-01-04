#include <stdio.h>
#include <math.h>

int good_guess(double guess, double old_guess, double fraction)
{
  if (fabs(guess - old_guess) < (fraction * guess)) return 1;
  return 0;
}

double improve_guess(double x, double guess)
{
  return (2 * guess + (x / (guess * guess))) / 3;
}

double my_cbrt_rec(double x, double guess, double old_guess, double fraction)
{
  if (good_guess(guess, old_guess, fraction)) return guess;
  return my_cbrt_rec(x, improve_guess(x, guess), guess, fraction);
}

double my_cbrt(double x, double fraction)
{
  return my_cbrt_rec(x, 1.0, 0.0, fraction);
}

int main()
{
  double x = 8.0, fraction = 0.000001;
  printf("%lf\n", my_cbrt(x, fraction));
  return 0;
}
