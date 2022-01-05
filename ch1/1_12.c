#include <stdio.h>

int pascal_number(int row, int n)
{
  if (row == 1) return 1;
  if (n == 1 || n == row) return 1;
  if (n < 1) return 0;
  return pascal_number(row - 1, n - 1) + pascal_number(row - 1, n);
}

int main()
{
  printf("%d\n", pascal_number(9, 6));
  return 0;
}
