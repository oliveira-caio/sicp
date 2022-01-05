int fast_exp_iter(int base, int power)
{
  int ans = base;
  while (power > 0)
    {
      if (power % 2) ans = base * ans;
      else ans = ans * ans;
      power = power / 2;
    }
  return ans;
}
