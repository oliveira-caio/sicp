#include <stdio.h>
#include <stdlib.h>

typedef struct
{
  double x;
  double y;
} point;

typedef struct
{
  point start;
  point end;
} segment;

void make_point(point *p, double x, double y)
{
  p->x = x;
  p->y = y;
  return;
}

void make_segment(segment *seg, point *st, point *end)
{
  seg->start = *st;
  seg->end = *end;
  return;
}

void print_point(point *p)
{
  printf("(%lf, %lf)\n", p->x, p->y);
  return;
}

void print_segment(segment *seg)
{
  print_point(&(seg->start));
  printf("|\n");
  print_point(&(seg->end));
  return;
}

double average(double x, double y)
{
  return (x + y) / 2;
}

point *midpoint(segment *seg)
{
  point *mid = (point *) malloc(sizeof(point));

  mid->x = average((seg->start).x, (seg->end).x);
  mid->y = average((seg->start).y, (seg->end).y);

  return mid;
}

int main()
{
  point origin, one;
  segment zero_one;

  make_point(&origin, 0, 0);
  make_point(&one, 0, 1);
  make_segment(&zero_one, &origin, &one);

  print_point(&origin);
  print_point(&one);
  print_segment(&zero_one);
  print_point(midpoint(&zero_one));

  return 0;
}
  
