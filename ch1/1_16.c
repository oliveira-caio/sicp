int fast_exp_iter(int base, int power)
{
  int ans = 1;
  while (power > 0)
    {
      if (power % 2) ans = base * ans;
      base = base * base;
      power = power / 2;
    }
  return ans;
}
