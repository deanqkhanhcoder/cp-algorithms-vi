---
tags:
  - Translated
e_maxx_link: matrix_rank
---

# Tìm hạng của ma trận (Finding the rank of a matrix) {: #finding-the-rank-of-a-matrix}

**Hạng của ma trận** (**The rank of a matrix**) là số lượng lớn nhất các hàng/cột độc lập tuyến tính của ma trận. Hạng không chỉ được xác định cho ma trận vuông.

Hạng của ma trận cũng có thể được định nghĩa là bậc lớn nhất của bất kỳ định thức con (minor) khác không nào trong ma trận.

Giả sử ma trận là hình chữ nhật và có kích thước $N \times M$.
Lưu ý rằng nếu ma trận là ma trận vuông và định thức của nó khác không, thì hạng là $N$ ($=M$); nếu không nó sẽ nhỏ hơn. Nói chung, hạng của ma trận không vượt quá $\min (N, M)$.

## Thuật toán (Algorithm) {: #algorithm}

Bạn có thể tìm kiếm hạng bằng cách sử dụng [khử Gaussian](linear-system-gauss.md). Chúng ta sẽ thực hiện các thao tác tương tự như khi giải hệ thống hoặc tìm định thức của nó. Nhưng nếu ở bất kỳ bước nào trong cột thứ $i$ không có hàng nào có mục khác rỗng trong số những hàng mà chúng ta chưa chọn, thì chúng ta bỏ qua bước này.
Ngược lại, nếu chúng ta tìm thấy một hàng có phần tử khác không trong cột thứ $i$ trong bước thứ $i$, thì chúng ta đánh dấu hàng này là hàng đã chọn, tăng hạng lên một (ban đầu hạng được đặt bằng $0$), và thực hiện các thao tác thông thường là trừ hàng này khỏi phần còn lại.

## Độ phức tạp (Complexity) {: #complexity}

Thuật toán này chạy trong $\mathcal{O}(n^3)$.

## Cài đặt (Implementation) {: #implementation}
```cpp title="matrix-rank"
const double EPS = 1E-9;

int compute_rank(vector<vector<double>> A) {
    int n = A.size();
    int m = A[0].size();

    int rank = 0;
    vector<bool> row_selected(n, false);
    for (int i = 0; i < m; ++i) {
        int j;
        for (j = 0; j < n; ++j) {
            if (!row_selected[j] && abs(A[j][i]) > EPS)
                break;
        }

        if (j != n) {
            ++rank;
            row_selected[j] = true;
            for (int p = i + 1; p < m; ++p)
                A[j][p] /= A[j][i];
            for (int k = 0; k < n; ++k) {
                if (k != j && abs(A[k][i]) > EPS) {
                    for (int p = i + 1; p < m; ++p)
                        A[k][p] -= A[j][p] * A[k][i];
                }
            }
        }
    }
    return rank;
}
```
## Bài tập (Problems) {: #problems}
 * [TIMUS1041 Nikifor](http://acm.timus.ru/problem.aspx?space=1&num=1041)
