/*
  T, by definition, is:
  T_{pq}(a, b) = (bq + aq + ap, bp + aq)

  Applying T twice gives us:
  T_{pq}^2(a, b) = T_{pq}(bq + aq + ap, bp + aq)
  = ((bp+aq)q + (bq+aq+ap)q + (bq+aq+ap)p, (bp+aq)p + (bq+aq+ap)q)
  = (bpq + aqq + bqq + aqq + apq + bqp + aqp + app, bpp + aqp + bqq + aqq + apq)
  = (b(pq+qq+qp) + a(pq+qq+qp) + a(qq+pp), b(pp+qq) + a(pq+qq+qp))
  = T_{(pp+qq)(pq+qq+qp)}
 */
int fast_generalized_fibonacci_transform(int a, int b, int p, int q, int count)
{
  if (count == 0) return b;

  if (count % 2) return fast_transform(b*q + a*q + a*p,
				       b*p + a*q,
				       p,
				       q,
				       count - 1);

  return fast_transform(a,
			b,
			p*p + q*q,
			p*q + q*q + q*p,
			count >> 1);  
}
