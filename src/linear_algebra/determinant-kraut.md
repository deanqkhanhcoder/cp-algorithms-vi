---
title: Tính định thức bằng phương pháp Kraut (Calculating the determinant using Kraut method)
tags:
  - Original
---
# Tính định thức bằng phương pháp Kraut trong $O(N^3)$ (Calculating the determinant using Kraut method in $O(N^3)$) {: #calculating-the-determinant-using-kraut-method}

Trong bài viết này, chúng tôi sẽ mô tả cách tìm định thức của ma trận bằng phương pháp Kraut, phương pháp này hoạt động trong $O(N^3)$.

Thuật toán Kraut tìm cách phân rã ma trận $A$ dưới dạng $A = L U$ trong đó $L$ là ma trận tam giác dưới và $U$ là ma trận tam giác trên. Không mất tính tổng quát, chúng ta có thể giả định rằng tất cả các phần tử đường chéo của $L$ đều bằng 1. Một khi chúng ta biết các ma trận này, thật dễ dàng để tính toán định thức của $A$: nó bằng tích của tất cả các phần tử trên đường chéo chính của ma trận $U$.

Có một định lý nói rằng bất kỳ ma trận nghịch đảo nào cũng có phân rã LU, và nó là duy nhất, khi và chỉ khi tất cả các định thức con chính của nó đều khác không. Chúng tôi chỉ xem xét phân rã như vậy trong đó đường chéo của ma trận $L$ bao gồm các số một.

Gọi $A$ là ma trận và $N$ - kích thước của nó. Chúng ta sẽ tìm các phần tử của ma trận $L$ và $U$ bằng các bước sau:

 1. Đặt $L_{i i} = 1$ cho $i = 1, 2, ..., N$.
 2. Đối với mỗi $j = 1, 2, ..., N$ thực hiện:
      - Đối với $i = 1, 2, ..., j$ tìm các giá trị 
        
        \[U_{ij} = A_{ij} - \sum_{k=1}^{i-1} L_{ik} \cdot U_{kj}\]
 
      - Tiếp theo, đối với $i = j+1, j+2, ..., N$ tìm các giá trị
 
        \[L_{ij} = \frac{1}{U_{jj}} \left(A_{ij} - \sum_{k=1}^{j-1} L_{ik} \cdot U_{kj} \right).\]

## Cài đặt (Implementation) {: #implementation}

```java
static BigInteger det (BigDecimal a [][], int n) {
	try {

	for (int i=0; i<n; i++) {
		boolean nonzero = false;
		for (int j=0; j<n; j++)
			if (a[i][j].compareTo (new BigDecimal (BigInteger.ZERO)) > 0)
				nonzero = true;
		if (!nonzero)
			return BigInteger.ZERO;
	}

	BigDecimal scaling [] = new BigDecimal [n];
	for (int i=0; i<n; i++) {
		BigDecimal big = new BigDecimal (BigInteger.ZERO);
		for (int j=0; j<n; j++)
			if (a[i][j].abs().compareTo (big) > 0)
				big = a[i][j].abs();
		scaling[i] = (new BigDecimal (BigInteger.ONE)) .divide
			(big, 100, BigDecimal.ROUND_HALF_EVEN);
	}

	int sign = 1;

	for (int j=0; j<n; j++) {
		for (int i=0; i<j; i++) {
			BigDecimal sum = a[i][j];
			for (int k=0; k<i; k++)
				sum = sum.subtract (a[i][k].multiply (a[k][j]));
			a[i][j] = sum;
		}

		BigDecimal big = new BigDecimal (BigInteger.ZERO);
		int imax = -1;
		for (int i=j; i<n; i++) {
			BigDecimal sum = a[i][j];
			for (int k=0; k<j; k++)
				sum = sum.subtract (a[i][k].multiply (a[k][j]));
			a[i][j] = sum;
			BigDecimal cur = sum.abs();
			cur = cur.multiply (scaling[i]);
			if (cur.compareTo (big) >= 0) {
				big = cur;
				imax = i;
			}
		}

		if (j != imax) {
			for (int k=0; k<n; k++) {
				BigDecimal t = a[j][k];
				a[j][k] = a[imax][k];
				a[imax][k] = t;
			}

			BigDecimal t = scaling[imax];
			scaling[imax] = scaling[j];
			scaling[j] = t;

			sign = -sign;
		}

		if (j != n-1)
			for (int i=j+1; i<n; i++)
				a[i][j] = a[i][j].divide
					(a[j][j], 100, BigDecimal.ROUND_HALF_EVEN);

	}

	BigDecimal result = new BigDecimal (1);
	if (sign == -1)
		result = result.negate();
	for (int i=0; i<n; i++)
		result = result.multiply (a[i][i]);

	return result.divide
		(BigDecimal.valueOf(1), 0, BigDecimal.ROUND_HALF_EVEN).toBigInteger();
	}
	catch (Exception e) {
		return BigInteger.ZERO;
	}
}
```
