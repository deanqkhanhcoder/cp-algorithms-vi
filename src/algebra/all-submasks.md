---
tags:
  - Translated
e_maxx_link: all_submasks
---

# Liệt kê Submask {: #submask-enumeration}

## Liệt kê tất cả submask của một mask cho trước {: #enumerating-all-submasks-of-a-given-mask}

Cho một bitmask $m$, bạn muốn duyệt hiệu quả qua tất cả các submask của nó, tức là các mask $s$ mà chỉ có các bit được bật trong mask $m$ mới được bật.

Xem xét cài đặt thuật toán này, dựa trên các thủ thuật thao tác bit:

```cpp
int s = m;
while (s > 0) {
 ... you can use s ...
 s = (s-1) & m;
}
```

hoặc, sử dụng vòng lặp `for` gọn hơn:

```cpp
for (int s=m; s; s=(s-1)&m)
 ... you can use s ...
```

Trong cả hai biến thể code, submask bằng 0 sẽ không được xử lý. Chúng ta có thể xử lý nó bên ngoài vòng lặp, hoặc sử dụng thiết kế kém thanh lịch hơn, ví dụ:

```cpp
for (int s=m; ; s=(s-1)&m) {
 ... you can use s ...
 if (s==0)  break;
}
```

Hãy xem tại sao code trên duyệt qua tất cả các submask của $m$, không lặp lại, và theo thứ tự giảm dần.

Giả sử chúng ta có bitmask hiện tại $s$, và chúng ta muốn chuyển sang bitmask tiếp theo. Bằng cách trừ mask $s$ đi một đơn vị, chúng ta sẽ xóa bit bật phải nhất và tất cả các bit bên phải nó sẽ trở thành 1. Sau đó chúng ta loại bỏ tất cả các bit 1 "thừa" không có trong mask $m$ và do đó không thể là một phần của submask. Chúng ta thực hiện việc loại bỏ này bằng cách sử dụng phép toán bit `(s-1) & m`. Kết quả là, chúng ta "cắt" mask $s-1$ để xác định giá trị lớn nhất mà nó có thể nhận, đó là submask tiếp theo sau $s$ theo thứ tự giảm dần.

Do đó, thuật toán này sinh tất cả các submask của mask này theo thứ tự giảm dần, chỉ thực hiện hai phép toán mỗi lần lặp.

Một trường hợp đặc biệt là khi $s = 0$. Sau khi thực hiện $s-1$ chúng ta nhận được mask mà tất cả các bit đều bật (biểu diễn bit của -1), và sau `(s-1) & m` chúng ta sẽ có $s$ bằng $m$. Vì vậy, với mask $s = 0$ hãy cẩn thận — nếu vòng lặp không kết thúc tại 0, thuật toán có thể rơi vào vòng lặp vô hạn.

## Duyệt tất cả mask cùng các submask của nó. Độ phức tạp $O(3^n)$ {: #iterating-through-all-masks-with-their-submasks-complexity-o3n}

Trong nhiều bài toán, đặc biệt là những bài sử dụng quy hoạch động bitmask (bitmask DP), bạn muốn duyệt qua tất cả bitmask và với mỗi mask, duyệt qua tất cả các submask của nó:

```cpp
for (int m=0; m<(1<<n); ++m)
	for (int s=m; s; s=(s-1)&m)
 ... s and m ...
```

Hãy chứng minh rằng vòng lặp trong sẽ thực hiện tổng cộng $O(3^n)$ lần lặp.

**Chứng minh 1**: Xem xét bit thứ $i$. Có đúng ba khả năng cho nó:

1. nó không nằm trong mask $m$ (và do đó không nằm trong submask $s$),
2. nó nằm trong $m$, nhưng không nằm trong $s$, hoặc
3. nó nằm trong cả $m$ và $s$.

Vì có tổng cộng $n$ bit, sẽ có $3^n$ tổ hợp khác nhau.

**Chứng minh 2**: Lưu ý rằng nếu mask $m$ có $k$ bit bật, thì nó sẽ có $2^k$ submask. Vì chúng ta có tổng cộng $\binom{n}{k}$ mask có $k$ bit bật (xem [hệ số nhị thức](../combinatorics/binomial-coefficients.md)), nên tổng số tổ hợp cho tất cả các mask sẽ là:

$$\sum_{k=0}^n \binom{n}{k} \cdot 2^k$$

Để tính số này, lưu ý rằng tổng trên bằng khai triển của $(1+2)^n$ sử dụng định lý nhị thức. Do đó, chúng ta có $3^n$ tổ hợp, như chúng ta muốn chứng minh.

## Bài tập luyện tập {: #practice-problems}

* [Atcoder - Close Group](https://atcoder.jp/contests/abc187/tasks/abc187_f)
* [Codeforces - Nuclear Fusion](http://codeforces.com/problemset/problem/71/E)
* [Codeforces - Sandy and Nuts](http://codeforces.com/problemset/problem/599/E)
* [Uva 1439 - Exclusive Access 2](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=4185)
* [UVa 11825 - Hackers' Crackdown](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2925)
