int fast_mult_rec(int a, int b)
{
  if (b == 0) return 0;
  if (b % 2) return a + fast_mult(a, (b - 1) >> 1) + fast_mult(a, (b - 1) >> 1);
  else return fast_mult(a, b >> 1) + fast_mult(a, b >> 1);
}
