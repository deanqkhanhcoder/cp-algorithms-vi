---
tags:
  - Translated
e_maxx_link: determinant_gauss
---

# Tính định thức của ma trận bằng phương pháp Gauss (Calculating the determinant of a matrix by Gauss) {: #calculating-the-determinant-of-a-matrix-by-gauss}

Bài toán: Cho ma trận $A$ kích thước $N \times N$. Tính định thức của nó.

## Thuật toán (Algorithm) {: #algorithm}

Chúng tôi sử dụng ý tưởng của [Phương pháp Gauss để giải hệ phương trình tuyến tính](linear-system-gauss.md)

Chúng ta sẽ thực hiện các bước giống như trong giải hệ phương trình tuyến tính, chỉ loại trừ việc chia dòng hiện tại cho $a_{ij}$. Các phép toán này sẽ không thay đổi giá trị tuyệt đối của định thức của ma trận. Tuy nhiên, khi chúng ta trao đổi hai dòng của ma trận, dấu của định thức có thể thay đổi.

Sau khi áp dụng Gauss trên ma trận, chúng tôi nhận được một ma trận đường chéo, có định thức chỉ là tích của các phần tử trên đường chéo. Dấu, như đã đề cập trước đây, có thể được xác định bởi số lượng dòng được trao đổi (nếu lẻ, thì dấu của định thức nên được đảo ngược). Do đó, chúng ta có thể sử dụng thuật toán Gauss để tính toán định thức của ma trận với độ phức tạp $O(N^3)$.

Cần lưu ý rằng nếu tại một thời điểm nào đó, chúng ta không tìm thấy ô khác không trong cột hiện tại, thuật toán sẽ dừng và trả về 0.

## Cài đặt (Implementation) {: #implementation}

```cpp
const double EPS = 1E-9;
int n;
vector < vector<double> > a (n, vector<double> (n));

double det = 1;
for (int i=0; i<n; ++i) {
	int k = i;
	for (int j=i+1; j<n; ++j)
		if (abs (a[j][i]) > abs (a[k][i]))
			k = j;
	if (abs (a[k][i]) < EPS) {
		det = 0;
		break;
	}
	swap (a[i], a[k]);
	if (i != k)
		det = -det;
	det *= a[i][i];
	for (int j=i+1; j<n; ++j)
		a[i][j] /= a[i][i];
	for (int j=0; j<n; ++j)
		if (j != i && abs (a[j][i]) > EPS)
			for (int k=i+1; k<n; ++k)
				a[j][k] -= a[i][k] * a[j][i];
}

cout << det;
```

## Bài tập (Practice Problems) {: #practice-problems}
* [Codeforces - Wizards and Bets](http://codeforces.com/contest/167/problem/E)
