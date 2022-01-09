#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double average(double x, double y)
{
  return (x + y) / 2;
}

double square(double x)
{
  return x * x;
}

typedef struct
{
  double x;
  double y;
} point;

void make_point(point *p, double x, double y)
{
  p->x = x;
  p->y = y;
  return;
}

void print_point(point *p)
{
  printf("(%lf, %lf)\n", p->x, p->y);
  return;
}

typedef struct
{
  point start;
  point end;
} segment;

void make_segment(segment *seg, point *st, point *end)
{
  seg->start = *st;
  seg->end = *end;
  return;
}

double length(segment *s)
{
  return sqrt(square((s->end).x - (s->start).x)
	      + square((s->end).y - (s->start).y));
}

void print_segment(segment *seg)
{
  print_point(&(seg->start));
  printf("|\n");
  print_point(&(seg->end));
  return;
}

point *midpoint(segment *seg)
{
  point *mid = (point *) malloc(sizeof(point));

  mid->x = average((seg->start).x, (seg->end).x);
  mid->y = average((seg->start).y, (seg->end).y);

  return mid;
}

/*
  since life is too short, i'll not worry about the orthogonality of the
  segments of the rectangle in this problem. that's not the point of the
  exercise anyway (the point is making the functions area and perimeter
  below independent of the representation of a rectangle).

  at codology (https://codology.net/post/sicp-solution-exercise-2-3/) they
  gave what probably is the best solution for a representation of a rectangle,
  which requires as parameters a point, the height, the width and an angle.
  my ideas (since i was not interested in checking orthogonality) for
  representing a rectangle were simpler: store the base and the height as
  segments directly or store three points because three (distincts) points
  determine a losangle. the last is also the second approach described
  in codology.
*/
typedef struct
{
  point p_one;
  point p_two;
  point p_three;
} rectangle;

typedef struct
{
  segment base;
  segment height;
} rectangle_segments;

void make_rectangle_points(rectangle *r,
			   point *p1,
			   point *p2,
			   point *p3)
{
  r->p_one = *p1;
  r->p_two = *p2;
  r->p_three = *p3;
  return;
}

void make_rectangle_segments(rectangle_segments *rs,
			     segment *b,
			     segment *h)
{
  rs->base = *b;
  rs->height = *h;
  return;
}

/*
  the base and the height functions obviously depend on the way we represent
  a rectangle. since the representation using segments is trivial, i'll let
  it commented and use only the one using points.

segment *base(rectangle_segments *rs)
{
  return &(rs->base);
}

segment *height(rectangle_segments *rs)
{
  return &(rs->height);
}
*/

segment *base(rectangle *r)
{
  segment *base = (segment *) malloc(sizeof(segment));

  make_segment(base, &(r->p_two), &(r->p_three));

  return base;
}

segment *height(rectangle *r)
{
  segment *height = (segment *) malloc(sizeof(segment));

  make_segment(height, &(r->p_two), &(r->p_three));

  return height;
}

double area(rectangle *r)
{
  return length(base(r)) * length(height(r));
}

double perimeter(rectangle *r)
{
  return 2 * (length(base(r)) + length(height(r)));
}

int main()
{
  point origin, zero_one, one_one;
  segment base_rec, height_rec;
  rectangle rec;
  rectangle_segments rs;

  make_point(&origin, 0, 0);
  make_point(&zero_one, 0, 1);
  make_point(&one_one, 1, 1);
  make_rectangle_points(&rec, &origin, &zero_one, &one_one);

  printf("area rectangle: %.5lf, perimeter rectangle: %.5lf\n",
	 area(&rec),
	 perimeter(&rec));


  make_segment(&base_rec, &zero_one, &one_one);
  make_segment(&height_rec, &origin, &zero_one);
  make_rectangle_segments(&rs, &base_rec, &height_rec);

  /* printf("area rectangle: %.5lf, perimeter rectangle: %.5lf\n", */
  /* 	 area(&rs), */
  /* 	 perimeter(&rs)); */

  return 0;
}
