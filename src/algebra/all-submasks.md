---
tags:
  - Translated
e_maxx_link: all_submasks
---

# Liệt kê các mask con

## Liệt kê tất cả các mask con của một mask cho trước

Cho một bitmask $m$, ta muốn duyệt qua tất cả các mask con của nó một cách hiệu quả. Mask con $s$ là mask mà chỉ các bit đã được bật trong $m$ mới có thể được bật.

Xem xét cách cài đặt thuật toán này, dựa trên các thủ thuật với phép toán trên bit:

```cpp
int s = m;
while (s > 0) {
 ... bạn có thể dùng s ...
 s = (s-1) & m;
}
```

hoặc, dùng câu lệnh `for` gọn hơn:

```cpp
for (int s=m; s; s=(s-1)&m)
 ... bạn có thể dùng s ...
```

Trong cả hai phiên bản, mask con bằng 0 sẽ không được xử lý. Ta có thể xử lý nó bên ngoài vòng lặp, hoặc dùng một thiết kế kém thanh lịch hơn, ví dụ:

```cpp
for (int s=m; ; s=(s-1)&m) {
 ... bạn có thể dùng s ...
 if (s==0)  break;
}
```

Hãy xem xét tại sao đoạn mã trên duyệt qua tất cả các mask con của $m$, không lặp lại, và theo thứ tự giảm dần.

Giả sử ta có một bitmask hiện tại là $s$, và ta muốn chuyển sang mask con tiếp theo. Bằng cách trừ đi một đơn vị từ $s$, ta sẽ xóa bit 1 bên phải nhất và tất cả các bit bên phải nó sẽ trở thành 1. Sau đó, ta loại bỏ tất cả các bit 1 "thừa" không có trong mask $m$ và do đó không thể là một phần của mask con. Ta thực hiện việc loại bỏ này bằng cách sử dụng phép toán bit `(s-1) & m`. Kết quả là, ta "cắt" mask $s-1$ để xác định giá trị lớn nhất mà nó có thể nhận, tức là mask con ngay sau $s$ theo thứ tự giảm dần.

Do đó, thuật toán này sinh ra tất cả các mask con của mask đã cho theo thứ tự giảm dần, chỉ thực hiện hai phép toán mỗi vòng lặp.

Một trường hợp đặc biệt là khi $s = 0$. Sau khi thực hiện $s-1$, ta nhận được một mask mà tất cả các bit đều được bật (biểu diễn bit của -1), và sau phép toán `(s-1) & m`, ta sẽ có $s$ bằng $m$. Do đó, với mask $s = 0$ cần phải cẩn thận - nếu vòng lặp không kết thúc tại 0, thuật toán có thể bị lặp vô hạn.

## Duyệt qua tất cả các mask và các mask con của chúng. Độ phức tạp $O(3^n)$

Trong nhiều bài toán, đặc biệt là những bài sử dụng quy hoạch động bitmask, bạn muốn duyệt qua tất cả các bitmask và với mỗi mask, duyệt qua tất cả các mask con của nó:

```cpp
for (int m=0; m<(1<<n); ++m)
	for (int s=m; s; s=(s-1)&m)
 ... s và m ...
```

Hãy chứng minh rằng vòng lặp bên trong sẽ thực hiện tổng cộng $O(3^n)$ lần lặp.

**Chứng minh thứ nhất**: Xét bit thứ $i$. Có chính xác ba lựa chọn cho nó:

1. nó không nằm trong mask $m$ (và do đó cũng không nằm trong mask con $s$),
2. nó nằm trong $m$, nhưng không nằm trong $s$, hoặc
3. nó nằm trong cả $m$ và $s$.

Vì có tổng cộng $n$ bit, sẽ có $3^n$ tổ hợp khác nhau.

**Chứng minh thứ hai**: Lưu ý rằng nếu mask $m$ có $k$ bit được bật, thì nó sẽ có $2^k$ mask con. Vì chúng ta có tổng cộng $\binom{n}{k}$ mask có $k$ bit được bật (xem [Tổ hợp](../combinatorics/binomial-coefficients.md)), nên tổng số tổ hợp cho tất cả các mask sẽ là:

$$\sum_{k=0}^n \binom{n}{k} \cdot 2^k$$

Để tính con số này, lưu ý rằng tổng trên bằng khai triển của $(1+2)^n$ theo nhị thức Newton. Do đó, chúng ta có $3^n$ tổ hợp, như ta cần chứng minh.

## Bài tập luyện tập

* [Atcoder - Close Group](https://atcoder.jp/contests/abc187/tasks/abc187_f)
* [Codeforces - Nuclear Fusion](http://codeforces.com/problemset/problem/71/E)
* [Codeforces - Sandy and Nuts](http://codeforces.com/problemset/problem/599/E)
* [Uva 1439 - Exclusive Access 2](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=4185)
* [UVa 11825 - Hackers' Crackdown](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2925)