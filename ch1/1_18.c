int fast_mult_iter(int a, int b)
{
  int ans = 0;
  while (b > 0)
    {
      if (b % 2) ans = ans + a;
      a = a << 1;
      b = b >> 1;
    }
  return ans;
}
