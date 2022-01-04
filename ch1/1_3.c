int sum_squares(int x, int y, int z)
{
  if (x >= y)
    {
    if (y >= z)
      {
	return x * x + y * y;
      }
    else
      {
	return x * x + z * z;
      }
    }
  else
    {
      if (x >= z)
	{
	  return x * x + y * y;
	}
      else
	{
	  return y * y + z * z;
	}
    }
}

teste
