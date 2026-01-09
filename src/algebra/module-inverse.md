---
tags:
  - Translated
e_maxx_link: reverse_element
---

# Nghịch đảo nhân Modulo (Modular Multiplicative Inverse) {: #modular-multiplicative-inverse}

## Định nghĩa (Definition) {: #definition}

Một [nghịch đảo nhân modulo](http://en.wikipedia.org/wiki/Modular_multiplicative_inverse) của một số nguyên $a$ là một số nguyên $x$ sao cho $a \cdot x$ đồng dư với $1$ modulo một số $m$ nào đó.
Để viết nó một cách hình thức: chúng ta muốn tìm một số nguyên $x$ sao cho 

$$a \cdot x \equiv 1 \mod m.$$

Chúng ta cũng sẽ ký hiệu $x$ đơn giản là $a^{-1}$.

Chúng ta nên lưu ý rằng nghịch đảo modulo không phải lúc nào cũng tồn tại. Ví dụ, cho $m = 4$, $a = 2$. 
Bằng cách kiểm tra tất cả các giá trị có thể modulo $m$, có thể thấy rõ rằng chúng ta không thể tìm thấy $a^{-1}$ thỏa mãn phương trình trên. 
Có thể chứng minh rằng nghịch đảo modulo tồn tại khi và chỉ khi $a$ và $m$ là nguyên tố cùng nhau (tức là $\gcd(a, m) = 1$).

Trong bài viết này, chúng tôi trình bày hai phương pháp để tìm nghịch đảo modulo trong trường hợp nó tồn tại, và một phương pháp để tìm nghịch đảo modulo cho tất cả các số trong thời gian tuyến tính.

## Tìm nghịch đảo Modulo bằng thuật toán Euclid mở rộng (Finding the Modular Inverse using Extended Euclidean algorithm) {: #finding-the-modular-inverse-using-extended-euclidean-algorithm}

Xét phương trình sau (với ẩn $x$ và $y$):

$$a \cdot x + m \cdot y = 1$$

Đây là một [Phương trình Diophantine tuyến tính hai ẩn](linear-diophantine-equation.md).
Như được trình bày trong bài viết được liên kết, khi $\gcd(a, m) = 1$, phương trình có một nghiệm có thể được tìm thấy bằng cách sử dụng [thuật toán Euclid mở rộng](extended-euclid-algorithm.md).
Lưu ý rằng $\gcd(a, m) = 1$ cũng là điều kiện để nghịch đảo modulo tồn tại.

Bây giờ, nếu chúng ta lấy modulo $m$ của cả hai vế, chúng ta có thể loại bỏ $m \cdot y$, và phương trình trở thành:

$$a \cdot x \equiv 1 \mod m$$

Do đó, nghịch đảo modulo của $a$ là $x$.

Cài đặt như sau:

```cpp
int x, y;
int g = extended_euclidean(a, m, x, y);
if (g != 1) {
    cout << "No solution!";
}
else {
    x = (x % m + m) % m;
    cout << x << endl;
}
```

Lưu ý cách chúng tôi sửa đổi `x`.
Kết quả `x` từ thuật toán Euclid mở rộng có thể âm, vì vậy `x % m` cũng có thể âm, và chúng ta phải cộng `m` trước để làm cho nó dương.

<div id="fermat-euler"></div>
## Tìm nghịch đảo Modulo bằng lũy thừa nhị phân (Finding the Modular Inverse using Binary Exponentiation) {: #finding-the-modular-inverse-using-binary-exponentiation}

Một phương pháp khác để tìm nghịch đảo modulo là sử dụng định lý Euler, trong đó nêu rằng sự đồng dư sau là đúng nếu $a$ và $m$ là nguyên tố cùng nhau:

$$a^{\phi (m)} \equiv 1 \mod m$$

$\phi$ là [Hàm phi Euler](phi-function.md).
Một lần nữa, lưu ý rằng $a$ và $m$ là nguyên tố cùng nhau cũng là điều kiện để nghịch đảo modulo tồn tại.

Nếu $m$ là một số nguyên tố, điều này đơn giản hóa thành [Định lý Fermat nhỏ](http://en.wikipedia.org/wiki/Fermat's_little_theorem):

$$a^{m - 1} \equiv 1 \mod m$$

Nhân cả hai vế của các phương trình trên với $a^{-1}$, và chúng ta nhận được:

* Đối với một modulo $m$ bất kỳ (nhưng nguyên tố cùng nhau): $a ^ {\phi (m) - 1} \equiv a ^{-1} \mod m$
* Đối với một modulo $m$ là số nguyên tố: $a ^ {m - 2} \equiv a ^ {-1} \mod m$

Từ những kết quả này, chúng ta có thể dễ dàng tìm thấy nghịch đảo modulo bằng cách sử dụng [thuật toán lũy thừa nhị phân](binary-exp.md), hoạt động trong thời gian $O(\log m)$.

Mặc dù phương pháp này dễ hiểu hơn phương pháp được mô tả trong đoạn trước, nhưng trong trường hợp $m$ không phải là số nguyên tố, chúng ta cần tính hàm phi Euler, liên quan đến việc phân tích thừa số của $m$, điều này có thể rất khó. Nếu phân tích thừa số nguyên tố của $m$ được biết, thì độ phức tạp của phương pháp này là $O(\log m)$.

<div id="finding-the-modular-inverse-using-euclidean-division"></div>
## Tìm nghịch đảo modulo cho modulo nguyên tố bằng phép chia Euclid (Finding the modular inverse for prime moduli using Euclidean Division) {: #finding-the-modular-inverse-for-prime-moduli-using-euclidean-division}

Cho một số nguyên tố modulo $m > a$ (hoặc chúng ta có thể áp dụng modulo để làm cho nó nhỏ hơn trong 1 bước), theo [Phép chia Euclid](https://en.wikipedia.org/wiki/Euclidean_division)

$$m = k \cdot a + r$$

trong đó $k = \left\lfloor \frac{m}{a} \right\rfloor$ và $r = m \bmod a$, thì

$$
\begin{align*}
& \implies & 0          & \equiv k \cdot a + r   & \mod m \\
& \iff & r              & \equiv -k \cdot a      & \mod m \\
& \iff & r \cdot a^{-1} & \equiv -k              & \mod m \\
& \iff & a^{-1}         & \equiv -k \cdot r^{-1} & \mod m
\end{align*}
$$

Lưu ý rằng lập luận này không đúng nếu $m$ không phải là số nguyên tố, vì sự tồn tại của $a^{-1}$ không ngụ ý sự tồn tại của $r^{-1}$
trong trường hợp tổng quát. Để thấy điều này, hãy thử tính $5^{-1}$ modulo $12$ với công thức trên. Chúng ta muốn đi đến $5$,
vì $5 \cdot 5 \equiv 1 \bmod 12$. Tuy nhiên, $12 = 2 \cdot 5 + 2$, và chúng ta có $k=2$ và $r=2$, với $2$ không khả nghịch modulo $12$.

Tuy nhiên, nếu modulo là số nguyên tố, tất cả $a$ với $0 < a < m$ đều khả nghịch modulo $m$, và chúng ta có hàm đệ quy sau (trong C++) để tính nghịch đảo modulo cho số $a$ đối với $m$

```{.cpp file=modular_inverse_euclidean_division}
int inv(int a) {
  return a <= 1 ? a : m - (long long)(m/a) * inv(m % a) % m;
}
```

Độ phức tạp thời gian chính xác của đệ quy này chưa được biết. Nó nằm đâu đó giữa $O(\frac{\log m}{\log\log m})$ và $O(m^{\frac{1}{3} - \frac{2}{177} + \epsilon})$.
Xem [Về độ dài của khai triển Pierce](https://arxiv.org/abs/2211.08374).
Trong thực tế, cài đặt này nhanh, v.d. đối với modulo $10^9 + 7$ nó sẽ luôn kết thúc trong ít hơn 50 lần lặp.

<div id="mod-inv-all-num"></div>
Áp dụng công thức này, chúng ta cũng có thể tính trước nghịch đảo modulo cho mọi số trong khoảng $[1, m-1]$ trong $O(m)$.

```{.cpp file=modular_inverse_euclidean_division_all}
inv[1] = 1;
for(int a = 2; a < m; ++a)
    inv[a] = m - (long long)(m/a) * inv[m%a] % m;
```

## Tìm nghịch đảo modulo cho mảng số modulo $m$ (Finding the modular inverse for array of numbers modulo $m$) {: #finding-the-modular-inverse-for-array-of-numbers-modulo-m}

Giả sử chúng ta được cho một mảng và chúng ta muốn tìm nghịch đảo modulo cho tất cả các số trong đó (tất cả chúng đều khả nghịch).
Thay vì tính toán nghịch đảo cho mọi số, chúng ta có thể mở rộng phân số bằng tích tiền tố (không bao gồm chính nó) và tích hậu tố (không bao gồm chính nó), và kết thúc chỉ tính toán một nghịch đảo duy nhất thay thế.

$$
\begin{align}
x_i^{-1} &= \frac{1}{x_i} = \frac{\overbrace{x_1 \cdot x_2 \cdots x_{i-1}}^{\text{prefix}_{i-1}} \cdot ~1~ \cdot \overbrace{x_{i+1} \cdot x_{i+2} \cdots x_n}^{\text{suffix}_{i+1}}}{x_1 \cdot x_2 \cdots x_{i-1} \cdot x_i \cdot x_{i+1} \cdot x_{i+2} \cdots x_n} \\
&= \text{prefix}_{i-1} \cdot \text{suffix}_{i+1} \cdot \left(x_1 \cdot x_2 \cdots x_n\right)^{-1}
\end{align}
$$

Trong mã, chúng ta chỉ cần tạo một mảng tích tiền tố (loại trừ chính nó, bắt đầu từ phần tử đơn vị), tính nghịch đảo modulo cho tích của tất cả các số và sau đó nhân nó với tích tiền tố và tích hậu tố (loại trừ chính nó).
Tích hậu tố được tính bằng cách lặp từ sau ra trước.

```cpp
std::vector<int> invs(const std::vector<int> &a, int m) {
    int n = a.size();
    if (n == 0) return {};
    std::vector<int> b(n);
    int v = 1;
    for (int i = 0; i != n; ++i) {
        b[i] = v;
        v = static_cast<long long>(v) * a[i] % m;
    }
    int x, y;
    extended_euclidean(v, m, x, y);
    x = (x % m + m) % m;
    for (int i = n - 1; i >= 0; --i) {
        b[i] = static_cast<long long>(x) * b[i] % m;
        x = static_cast<long long>(x) * a[i] % m;
    }
    return b;
}
```

## Bài tập luyện tập {: #practice-problems}

* [UVa 11904 - One Unit Machine](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3055)
* [Hackerrank - Longest Increasing Subsequence Arrays](https://www.hackerrank.com/contests/world-codesprint-5/challenges/longest-increasing-subsequence-arrays)
* [Codeforces 300C - Beautiful Numbers](http://codeforces.com/problemset/problem/300/C)
* [Codeforces 622F - The Sum of the k-th Powers](http://codeforces.com/problemset/problem/622/F)
* [Codeforces 717A - Festival Organization](http://codeforces.com/problemset/problem/717/A)
* [Codeforces 896D - Nephren Runs a Cinema](http://codeforces.com/problemset/problem/896/D)

---
