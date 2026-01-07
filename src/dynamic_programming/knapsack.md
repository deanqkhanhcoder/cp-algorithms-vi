---
tags:
  - Original
---

# Bài toán Balo
Kiến thức yêu cầu: [Giới thiệu về Quy hoạch động](http://127.0.0.1:8000/dynamic_programming/intro-to-dp.html)

## Giới thiệu
Xét ví dụ sau:
### [[USACO07 Dec] Charm Bracelet](https://www.acmicpc.net/problem/6144) 
Có $n$ vật phẩm phân biệt và một chiếc balo có sức chứa $W$. Mỗi vật có hai thuộc tính: trọng lượng ($w_{i}$) và giá trị ($v_{i}$).
Bạn cần chọn một tập con các vật để bỏ vào balo sao cho tổng trọng lượng không vượt quá $W$ và tổng giá trị là lớn nhất.

Trong ví dụ trên, mỗi vật chỉ có hai trạng thái (lấy hoặc không lấy), tương ứng với nhị phân 0 và 1. Vì vậy, loại bài toán này được gọi là "balo 0-1".

## Balo 0-1

### Giải thích

Với ví dụ trên, đầu vào của bài toán là: trọng lượng của vật thứ $i$ là $w_{i}$, giá trị là $v_{i}$, và sức chứa tối đa của balo là $W$.

Gọi $f_{i, j}$ là trạng thái quy hoạch động lưu giá trị lớn nhất balo có thể đạt khi chỉ xét $i$ vật đầu tiên và sức chứa còn lại là $j$.

Giả sử tất cả các trạng thái của $i-1$ vật đầu đã được xử lý, vật thứ $i$ có những lựa chọn nào?

- Nếu không cho vật vào balo, sức chứa còn lại không đổi và tổng giá trị không thay đổi. Do đó, giá trị tối đa trong trường hợp này là $f_{i-1, j}$.
- Nếu cho vật vào balo, sức chứa còn lại giảm $w_{i}$ và tổng giá trị tăng $v_{i}$, nên giá trị tối đa trong trường hợp này là $f_{i-1, j-w_i} + v_i$.

Từ đó suy ra công thức chuyển tiếp:

$$f_{i, j} = \max(f_{i-1, j}, f_{i-1, j-w_i} + v_i)$$

Hơn nữa, vì $f_{i}$ chỉ phụ thuộc vào $f_{i-1}$ nên ta có thể loại bỏ chỉ số $i$. Ta có quy tắc chuyển tiếp:

$$f_j \gets \max(f_j, f_{j-w_i}+v_i)$$

quy tắc này phải được thực hiện theo thứ tự **giảm dần** của $j$ (để $f_{j-w_i}$ tương ứng với $f_{i-1,j-w_i}$ chứ không phải $f_{i,j-w_i}$).

**Hiểu rõ quy tắc chuyển tiếp này rất quan trọng, vì hầu hết các chuyển tiếp cho bài toán balo được suy ra theo cách tương tự.**

### Cài đặt

Thuật toán mô tả có thể được cài đặt trong $O(nW)$ như sau:

``` .c++
for (int i = 1; i <= n; i++)
  for (int j = W; j >= w[i]; j--)
    f[j] = max(f[j], f[j - w[i]] + v[i]);
```

Một lần nữa, lưu ý thứ tự thực thi. Cần tuân thủ chặt chẽ để đảm bảo bất biến sau: Ngay trước khi cặp $(i, j)$ được xử lý, $f_k$ tương ứng với $f_{i,k}$ khi $k > j$, nhưng tương ứng với $f_{i-1,k}$ khi $k < j$. Điều này đảm bảo $f_{j-w_i}$ được lấy từ bước $(i-1)$ thay vì bước $i$.

## Balo đầy đủ (Complete Knapsack)

Mô hình balo đầy đủ tương tự như balo 0-1, khác biệt duy nhất là một vật có thể được chọn số lần không giới hạn thay vì chỉ một lần.

Ta vẫn có thể dùng ý tưởng của balo 0-1 để định nghĩa trạng thái: $f_{i, j}$ là giá trị lớn nhất balo có thể đạt được khi xét $i$ vật đầu tiên với sức chứa tối đa $j$.

Cần lưu ý rằng mặc dù định nghĩa trạng thái giống balo 0-1, quy tắc chuyển tiếp lại khác.

### Giải thích

Cách hiển nhiên là với $i$ vật đầu, liệt kê số lần lấy mỗi vật. Độ phức tạp của cách này là $O(n^2W)$.

Công thức chuyển tiếp thu được là:

$$f_{i, j} = \max\limits_{k=0}^{\infty}(f_{i-1, j-k\cdot w_i} + k\cdot v_i)$$

Đồng thời, nó có thể được đơn giản hóa thành dạng "phẳng":

$$f_{i, j} = \max(f_{i-1, j},f_{i, j-w_i} + v_i)$$

Lý do cách này hoạt động là vì $f_{i, j-w_i}$ đã được cập nhật từ $f_{i, j-2\cdot w_i}$ và các bước trước đó.

Tương tự balo 0-1, ta có thể loại bỏ chỉ số $i$ để tối ưu bộ nhớ, dẫn tới cùng quy tắc chuyển tiếp:

$$f_j \gets \max(f_j, f_{j-w_i}+v_i)$$

### Cài đặt

Thuật toán có thể được cài đặt trong $O(nW)$ như sau:

``` .c++
for (int i = 1; i <= n; i++)
  for (int j = w[i]; j <= W; j++)
    f[j] = max(f[j], f[j - w[i]] + v[i]);
```

Mặc dù có cùng quy tắc chuyển tiếp, đoạn mã trên không đúng cho balo 0-1.

Quan sát kỹ, ta thấy với vật đang xử lý $i$ và trạng thái hiện tại $f_{i,j}$,
khi $j\geqslant w_{i}$, $f_{i,j}$ sẽ bị ảnh hưởng bởi $f_{i,j-w_{i}}$.
Điều này tương đương với việc có thể cho vật $i$ vào balo nhiều lần, phù hợp với balo đầy đủ chứ không phải balo 0-1.

## Balo nhiều (Multiple Knapsack)

Balo nhiều là một biến thể của balo 0-1. Khác biệt chính là có $k_i$ bản sao của mỗi vật thay vì chỉ 1.

### Giải thích

Ý tưởng rất đơn giản là: "chọn mỗi vật $k_i$ lần" tương đương với "chọn $k_i$ bản sao của cùng một vật từng cái một". Do đó chuyển về mô hình balo 0-1, có thể mô tả bằng công thức chuyển tiếp:

$$f_{i, j} = \max_{k=0}^{k_i}(f_{i-1,j-k\cdot w_i} + k\cdot v_i)$$

Độ phức tạp thời gian của cách này là $O(W\sum\limits_{i=1}^{n}k_i)$.

### Tối ưu hoá chia theo nhị phân (Binary Grouping)

Chúng ta vẫn cân nhắc chuyển mô hình balo nhiều sang mô hình balo 0-1 để tối ưu. Độ phức tạp $O(Wn)$ không thể tối ưu thêm bằng cách trên, do đó ta tập trung vào thành phần $O(\sum k_i)$.

Gọi $A_{i, j}$ là bản tách thứ $j$ của vật thứ $i$. Trong cách tách đơn giản đã nêu, $A_{i, j}$ biểu diễn cùng một vật cho mọi $j \le k_i$. Nguyên nhân chính dẫn đến hiệu suất thấp là ta thực hiện nhiều công việc lặp lại. Ví dụ, việc chọn \{A_{i, 1},A_{i, 2}\} và chọn \{A_{i, 2}, A_{i, 3}\} đôi khi tương đương. Do đó tối ưu phương pháp tách sẽ làm giảm đáng kể độ phức tạp thời gian.

Việc gom nhóm được thực hiện hiệu quả hơn bằng cách sử dụng phân nhóm theo nhị phân.

Cụ thể, $A_{i, j}$ tương ứng với $2^j$ vật đơn lẻ ($j\in[0,\lfloor \log_2(k_i+1)\rfloor-1]$). Nếu $k_i + 1$ không phải lũy thừa của 2, một nhóm bổ sung có kích thước $k_i-(2^{\lfloor \log_2(k_i+1)\rfloor}-1)$ sẽ được dùng để bù.

Thông qua phương pháp tách trên, có thể tạo mọi tổng không vượt quá $k_i$ bằng cách chọn một vài $A_{i, j}$. Sau khi tách, ta chỉ cần áp dụng phương pháp balo 0-1 để giải bài toán đã chuyển đổi.

Tối ưu này cho độ phức tạp thời gian $O(W\sum\limits_{i=1}^{n}\log k_i)$.

### Implementation

```c++
index = 0;
for (int i = 1; i <= n; i++) {
  int c = 1, p, h, k;
  cin >> p >> h >> k;
  while (k > c) {
    k -= c;
    list[++index].w = c * p;
    list[index].v = c * h;
    c *= 2;
  }
  list[++index].w = p * k;
  list[index].v = h * k;
}
```

### Tối ưu bằng hàng đợi đơn điệu (Monotone Queue Optimization)

Trong tối ưu này, mục tiêu là chuyển bài toán balo thành bài toán [hàng đợi cực đại](http://127.0.0.1:8000/data_structures/stack_queue_modification.html).

Để tiện mô tả, đặt $g_{x, y} = f_{i, x \cdot w_i + y}$ và $g'_{x, y} = f_{i-1, x \cdot w_i + y}$. Khi đó quy tắc chuyển tiếp có thể viết là:

$$g_{x, y} = \max_{k=0}^{k_i}(g'_{x-k, y} + v_i \cdot k)$$

Đặt tiếp $G_{x, y} = g'_{x, y} - v_i \cdot x$. Khi đó quy tắc chuyển tiếp có thể biểu diễn là:

$$g_{x, y} \gets \max_{k=0}^{k_i}(G_{x-k, y}) + v_i \cdot x$$

Điều này biến thành dạng tối ưu điển hình sử dụng hàng đợi đơn điệu. $G_{x, y}$ có thể được tính trong $O(1)$, nên với mỗi $y$ cố định, ta có thể tính $g_{x, y}$ trong $O(\lfloor \frac{W}{w_i} \rfloor)$ thời gian.
Do đó, độ phức tạp để tìm tất cả $g_{x, y}$ là $O(\lfloor \frac{W}{w_i} \rfloor) \times O(w_i) = O(W)$.
Bằng cách này, tổng độ phức tạp của thuật toán giảm xuống còn $O(nW)$.

## Balo hỗn hợp (Mixed Knapsack)

Bài toán balo hỗn hợp là tổ hợp của ba mô hình đã mô tả ở trên. Tức là: có vật chỉ lấy được một lần, có vật lấy vô hạn lần, và có vật chỉ lấy được tối đa $k$ lần.

Bài toán có vẻ phức tạp, nhưng nếu bạn hiểu các ý tưởng cốt lõi của các bài toán balo trước đó và kết hợp chúng lại, bạn có thể giải được. Pseudocode cho lời giải như sau:

```c++
for (each item) {
  if (0-1 knapsack)
    Apply 0-1 knapsack code;
  else if (complete knapsack)
    Apply complete knapsack code;
  else if (multiple knapsack)
    Apply multiple knapsack code;
}
```

## Bài tập thực hành

- [Atcoder: Knapsack-1](https://atcoder.jp/contests/dp/tasks/dp_d)
- [Atcoder: Knapsack-2](https://atcoder.jp/contests/dp/tasks/dp_e)
- [LeetCode - 494. Target Sum](https://leetcode.com/problems/target-sum)
- [LeetCode - 416. Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum)
- [CSES: Book Shop II](https://cses.fi/problemset/task/1159)
- [DMOJ: Knapsack-3](https://dmoj.ca/problem/knapsack)
- [DMOJ: Knapsack-4](https://dmoj.ca/problem/knapsack4)
