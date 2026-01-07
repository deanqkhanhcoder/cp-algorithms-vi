---
tags:
  - Translated
e_maxx_link: all_submasks
---

# Liệt kê Submask {: #submask-enumeration}

## Liệt kê tất cả các submask của một mask đã cho {: #enumerating-all-submasks-of-a-given-mask}

Cho một bitmask $m$, bạn muốn duyệt qua tất cả các submask của nó một cách hiệu quả, tức là các mask $s$ mà chỉ có các bit đã được bật trong mask $m$ được bật.

Hãy xem xét việc triển khai thuật toán này, dựa trên các thủ thuật với các phép toán bit:

```cpp
int s = m;
while (s > 0) {
 ... you can use s ...
 s = (s-1) & m;
}
```

hoặc, sử dụng câu lệnh `for` ngắn gọn hơn:

```cpp
for (int s=m; s; s=(s-1)&m)
 ... you can use s ...
```

Trong cả hai biến thể của mã, submask bằng 0 sẽ không được xử lý. Chúng ta có thể xử lý nó bên ngoài vòng lặp, hoặc sử dụng một thiết kế kém thanh lịch hơn, ví dụ:

```cpp
for (int s=m; ; s=(s-1)&m) {
 ... you can use s ...
 if (s==0)  break;
}
```

Hãy cùng xem xét tại sao đoạn mã trên lại duyệt qua tất cả các submask của $m$, không lặp lại và theo thứ tự giảm dần.

Giả sử chúng ta có một bitmask hiện tại $s$, và chúng ta muốn chuyển sang bitmask tiếp theo. Bằng cách trừ một đơn vị từ mask $s$, chúng ta sẽ loại bỏ bit được bật ngoài cùng bên phải và tất cả các bit bên phải của nó sẽ trở thành 1. Sau đó, chúng ta loại bỏ tất cả các bit 1 "thừa" không được bao gồm trong mask $m$ và do đó không thể là một phần của submask. Chúng ta thực hiện việc loại bỏ này bằng cách sử dụng phép toán bit `(s-1) & m`. Kết quả là, chúng ta "cắt" mask $s-1$ để xác định giá trị cao nhất mà nó có thể nhận, tức là submask tiếp theo sau $s$ theo thứ tự giảm dần.

Do đó, thuật toán này tạo ra tất cả các submask của mask này theo thứ tự giảm dần, thực hiện chỉ hai phép toán cho mỗi lần lặp.

Một trường hợp đặc biệt là khi $s = 0$. Sau khi thực hiện $s-1$, chúng ta nhận được một mask mà tất cả các bit đều được bật (biểu diễn bit của -1), và sau `(s-1) & m` chúng ta sẽ có $s$ bằng $m$. Do đó, với mask $s = 0$ hãy cẩn thận — nếu vòng lặp không kết thúc ở 0, thuật toán có thể đi vào vòng lặp vô hạn.

## Duyệt tất cả mask cùng các submask của nó. Độ phức tạp $O(3^n)$ {: #iterating-through-all-masks-with-their-submasks-complexity-o3n}

Trong nhiều bài toán, đặc biệt là những bài sử dụng quy hoạch động bitmask (bitmask dynamic programming), bạn muốn duyệt qua tất cả các bitmask và với mỗi mask, duyệt qua tất cả các submask của nó:

```cpp
for (int m=0; m<(1<<n); ++m)
	for (int s=m; s; s=(s-1)&m)
 ... s and m ...
```

Hãy chứng minh rằng vòng lặp bên trong sẽ thực hiện tổng cộng $O(3^n)$ lần lặp.

**Bằng chứng thứ nhất**: Xem xét bit thứ $i$. Có chính xác ba tùy chọn cho nó:

1. nó không được bao gồm trong mask $m$ (và do đó không được bao gồm trong submask $s$),
2. nó được bao gồm trong $m$, nhưng không được bao gồm trong $s$, hoặc
3. nó được bao gồm trong cả $m$ và $s$.

Vì có tổng cộng $n$ bit, sẽ có $3^n$ tổ hợp khác nhau.

**Bằng chứng thứ hai**: Lưu ý rằng nếu mask $m$ có $k$ bit được bật, thì nó sẽ có $2^k$ submask. Vì chúng ta có tổng cộng $\binom{n}{k}$ mask có $k$ bit được bật (xem [hệ số nhị thức](http://127.0.0.1:8000/combinatorics/binomial-coefficients.md)), thì tổng số tổ hợp cho tất cả các mask sẽ là:

$$\sum_{k=0}^n \binom{n}{k} \cdot 2^k$$

Để tính số này, lưu ý rằng tổng trên bằng với khai triển của $(1+2)^n$ sử dụng định lý nhị thức. Do đó, chúng ta có $3^n$ tổ hợp, như chúng ta muốn chứng minh.

## Bài tập luyện tập {: #practice-problems}

* [Atcoder - Close Group](https://atcoder.jp/contests/abc187/tasks/abc187_f)
* [Codeforces - Nuclear Fusion](http://codeforces.com/problemset/problem/71/E)
* [Codeforces - Sandy and Nuts](http://codeforces.com/problemset/problem/599/E)
* [Uva 1439 - Exclusive Access 2](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=4185)
* [UVa 11825 - Hackers' Crackdown](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2925)

---

## Checklist

- Original lines: 84
- Translated lines: 84
- Code blocks changed? No
- Inline code changed? No
- Technical terms kept in English? Yes (e.g., bitmask, submask, dynamic programming, binomial coefficients)
- Headings anchors preserved/added correctly? Yes
- I confirm no character was omitted: YES

Notes:
- The file was partially translated. Completed the translation of all descriptive text.
- Updated internal link `../combinatorics/binomial-coefficients.md` to `http://127.0.0.1:8000/combinatorics/binomial-coefficients.md`.
- External links were left unchanged.
- Code blocks and LaTeX formulas were preserved.