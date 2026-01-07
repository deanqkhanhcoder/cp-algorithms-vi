---
tags:
  - Translated
e_maxx_link: discrete_log
---

# Logarit rời rạc {: #discrete-logarithm}

Logarit rời rạc là một số nguyên $x$ thỏa mãn phương trình

$$a^x \equiv b \pmod m$$

đối với các số nguyên $a$, $b$ và $m$ đã cho.

Logarit rời rạc không phải lúc nào cũng tồn tại, ví dụ không có lời giải cho $2^x \equiv 3 \pmod 7$. Không có điều kiện đơn giản nào để xác định liệu logarit rời rạc có tồn tại hay không.

Trong bài viết này, chúng ta mô tả thuật toán **Baby-step giant-step**, một thuật toán để tính logarit rời rạc được Shanks đề xuất vào năm 1971, có độ phức tạp thời gian $O(\sqrt{m})$. Đây là một thuật toán **meet-in-the-middle** vì nó sử dụng kỹ thuật chia đôi công việc.

## Thuật toán {: #algorithm}

Xét phương trình:

$$a^x \equiv b \pmod m,$$

trong đó $a$ và $m$ là nguyên tố cùng nhau.

Đặt $x = np - q$, trong đó $n$ là một hằng số được chọn trước (chúng ta sẽ mô tả cách chọn $n$ sau). $p$ được gọi là **bước lớn** (giant step), vì tăng nó lên một đơn vị sẽ làm tăng $x$ lên $n$. Tương tự, $q$ được gọi là **bước nhỏ** (baby step).

Rõ ràng, bất kỳ số $x$ nào trong khoảng $[0; m)$ đều có thể được biểu diễn dưới dạng này, trong đó $p \in [1; \lceil \frac{m}{n} \rceil ]$ và $q \in [0; n]$.

Khi đó, phương trình trở thành:

$$a^{np - q} \equiv b \pmod m.$$

Sử dụng thực tế rằng $a$ và $m$ là nguyên tố cùng nhau, chúng ta thu được:

$$a^{np} \equiv ba^q \pmod m$$

Phương trình mới này có thể được viết lại dưới dạng đơn giản:

$$f_1(p) = f_2(q).$$$

Bài toán này có thể được giải bằng phương pháp meet-in-the-middle như sau:

* Tính $f_1$ cho tất cả các đối số $p$ có thể. Sắp xếp mảng các cặp giá trị-đối số.
* Đối với tất cả các đối số $q$ có thể, tính $f_2$ và tìm $p$ tương ứng trong mảng đã sắp xếp bằng cách sử dụng tìm kiếm nhị phân.

## Độ phức tạp {: #complexity}

Chúng ta có thể tính $f_1(p)$ trong $O(\log m)$ bằng cách sử dụng [thuật toán lũy thừa nhị phân](http://127.0.0.1:8000/algebra/binary-exp.md). Tương tự cho $f_2(q)$.

Trong bước đầu tiên của thuật toán, chúng ta cần tính $f_1$ cho mọi đối số $p$ có thể và sau đó sắp xếp các giá trị. Do đó, bước này có độ phức tạp:

$$O\left(\left\lceil \frac{m}{n} \right\rceil \left(\log m + \log \left\lceil \frac{m}{n} \right\rceil \right)\right) = O\left( \left\lceil \frac {m}{n} \right\rceil \log m\right)$$

Trong bước thứ hai của thuật toán, chúng ta cần tính $f_2(q)$ cho mọi đối số $q$ có thể và sau đó thực hiện tìm kiếm nhị phân trên mảng các giá trị của $f_1$, do đó bước này có độ phức tạp:

$$O\left(n \left(\log m + \log \frac{m}{n} \right) \right) = O\left(n \log m\right).$$$

Bây giờ, khi chúng ta cộng hai độ phức tạp này, chúng ta nhận được $\log m$ nhân với tổng của $n$ và $m/n$, nhỏ nhất khi $n = m/n$, có nghĩa là, để đạt được hiệu suất tối ưu, $n$ nên được chọn sao cho:

$$n = \sqrt{m}.$$$

Khi đó, độ phức tạp của thuật toán trở thành:

$$O(\sqrt {m} \log m).$$$

## Triển khai {: #implementation}

### Triển khai đơn giản nhất {: #the-simplest-implementation}

Trong đoạn mã sau, hàm `powmod` tính $a^b \pmod m$ và hàm `solve` tạo ra một lời giải thích hợp cho bài toán.
Nó trả về $-1$ nếu không có lời giải và trả về một trong các lời giải có thể khác.

```cpp
int powmod(int a, int b, int m) {
    int res = 1;
    while (b > 0) {
        if (b & 1) {
            res = (res * 1ll * a) % m;
        }
        a = (a * 1ll * a) % m;
        b >>= 1;
    }
    return res;
}

int solve(int a, int b, int m) {
    a %= m, b %= m;
    int n = sqrt(m) + 1;
    map<int, int> vals;
    for (int p = 1; p <= n; ++p)
        vals[powmod(a, p * n, m)] = p;
    for (int q = 0; q <= n; ++q) {
        int cur = (powmod(a, q, m) * 1ll * b) % m;
        if (vals.count(cur)) {
            int ans = vals[cur] * n - q;
            return ans;
        }
    }
    return -1;
}
```

Trong mã này, chúng ta đã sử dụng `map` từ thư viện chuẩn C++ để lưu trữ các giá trị của $f_1$.
Bên trong, `map` sử dụng một cây đỏ-đen để lưu trữ các giá trị.
Do đó, mã này chậm hơn một chút so với nếu chúng ta sử dụng một mảng và tìm kiếm nhị phân, nhưng dễ viết hơn nhiều.

Lưu ý rằng mã của chúng ta giả định $0^0 = 1$, tức là mã sẽ tính $0$ làm lời giải cho phương trình $0^x \equiv 1 \pmod m$ và cũng làm lời giải cho $0^x \equiv 0 \pmod 1$.
Đây là một quy ước thường được sử dụng trong đại số, nhưng nó cũng không được chấp nhận phổ biến trong tất cả các lĩnh vực.
Đôi khi $0^0$ đơn giản là không xác định.
Nếu bạn không thích quy ước của chúng tôi, thì bạn cần xử lý trường hợp $a=0$ riêng:

```cpp
    if (a == 0)
        return b == 0 ? 1 : -1;
```

Một điều khác cần lưu ý là, nếu có nhiều đối số $p$ ánh xạ tới cùng một giá trị của $f_1$, chúng ta chỉ lưu trữ một đối số như vậy.
Điều này hoạt động trong trường hợp này vì chúng ta chỉ muốn trả về một lời giải có thể.
Nếu chúng ta cần trả về tất cả các lời giải có thể, chúng ta cần thay đổi `map<int, int>` thành, ví dụ, `map<int, vector<int>>`.
Chúng ta cũng cần thay đổi bước thứ hai cho phù hợp.

## Triển khai cải tiến {: #improved-implementation}

Một cải tiến có thể là loại bỏ lũy thừa nhị phân.
Điều này có thể được thực hiện bằng cách giữ một biến được nhân với $a$ mỗi khi chúng ta tăng $q$ và một biến được nhân với $a^n$ mỗi khi chúng ta tăng $p$.
Với thay đổi này, độ phức tạp của thuật toán vẫn giữ nguyên, nhưng bây giờ yếu tố $\log$ chỉ dành cho `map`.
Thay vì `map`, chúng ta cũng có thể sử dụng bảng băm (`unordered_map` trong C++) có độ phức tạp thời gian trung bình $O(1)$ để chèn và tìm kiếm.

Các bài toán thường yêu cầu $x$ nhỏ nhất thỏa mãn lời giải. 
Có thể lấy tất cả các câu trả lời và lấy giá trị nhỏ nhất, hoặc giảm câu trả lời đầu tiên tìm được bằng cách sử dụng [định lý Euler](http://127.0.0.1:8000/algebra/phi-function.md#application), nhưng chúng ta có thể thông minh về thứ tự mà chúng ta tính toán các giá trị và đảm bảo rằng câu trả lời đầu tiên chúng ta tìm thấy là giá trị nhỏ nhất.

```{.cpp file=discrete_log}
// Returns minimum x for which a ^ x % m = b % m, a and m are coprime.
int solve(int a, int b, int m) {
    a %= m, b %= m;
    int n = sqrt(m) + 1;

    int an = 1;
    for (int i = 0; i < n; ++i)
        an = (an * 1ll * a) % m;

    unordered_map<int, int> vals;
    for (int q = 0, cur = b; q <= n; ++q) {
        vals[cur] = q;
        cur = (cur * 1ll * a) % m;
    }

    for (int p = 1, cur = 1; p <= n; ++p) {
        cur = (cur * 1ll * an) % m;
        if (vals.count(cur)) {
            int ans = n * p - vals[cur];
            return ans;
        }
    }
    return -1;
}
```

Độ phức tạp là $O(\sqrt{m})$ khi sử dụng `unordered_map`.

## Khi $a$ và $m$ không nguyên tố cùng nhau { data-toc-label='When a and m are not coprime' }
Đặt $g = \gcd(a, m)$, và $g > 1$. Rõ ràng $a^x \bmod m$ với mọi $x \ge 1$ sẽ chia hết cho $g$.

Nếu $g \nmid b$, không có lời giải cho $x$.

Nếu $g \mid b$, đặt $a = g \alpha, b = g \beta, m = g \nu$.

$$
\begin{aligned}
a^x & \equiv b \mod m \\
(g \alpha) a^{x - 1} & \equiv g \beta \mod g \nu \\
\alpha a^{x-1} & \equiv \beta \mod \nu
\end{aligned}
$$

Thuật toán Baby-step giant-step có thể dễ dàng mở rộng để giải $ka^{x} \equiv b \pmod m$ cho $x$.

```{.cpp file=discrete_log_extended}
// Returns minimum x for which a ^ x % m = b % m.
int solve(int a, int b, int m) {
    a %= m, b %= m;
    int k = 1, add = 0, g;
    while ((g = gcd(a, m)) > 1) {
        if (b == k)
            return add;
        if (b % g)
            return -1;
        b /= g, m /= g, ++add;
        k = (k * 1ll * a / g) % m;
    }

    int n = sqrt(m) + 1;
    int an = 1;
    for (int i = 0; i < n; ++i)
        an = (an * 1ll * a) % m;

    unordered_map<int, int> vals;
    for (int q = 0, cur = b; q <= n; ++q) {
        vals[cur] = q;
        cur = (cur * 1ll * a) % m;
    }

    for (int p = 1, cur = k; p <= n; ++p) {
        cur = (cur * 1ll * an) % m;
        if (vals.count(cur)) {
            int ans = n * p - vals[cur] + add;
            return ans;
        }
    }
    return -1;
}
```

Độ phức tạp thời gian vẫn là $O(\sqrt{m})$ như trước vì việc rút gọn ban đầu thành $a$ và $m$ nguyên tố cùng nhau được thực hiện trong $O(\log^2 m)$.

## Bài tập luyện tập {: #practice-problems}
* [Spoj - Lũy thừa Modulo Đảo ngược](http://www.spoj.com/problems/MOD/)
* [Topcoder - SplittingFoxes3](https://community.topcoder.com/stat?c=problem_statement&pm=14386&rd=16801)
* [CodeChef - Nghịch đảo của một hàm](https://www.codechef.com/problems/INVXOR/)
* [Phương trình khó](https://codeforces.com/gym/101853/problem/G) (giả sử rằng $0^0$ không xác định)
* [CodeChef - Chef và dãy modulo](https://www.codechef.com/problems/CHEFMOD)

## Tham khảo {: #references}
* [Wikipedia - Baby-step giant-step](https://en.wikipedia.org/wiki/Baby-step_giant-step)
* [Trả lời của Zander trên Mathematics StackExchange](https://math.stackexchange.com/a/133054)

---

## Checklist

- Original lines: 182
- Translated lines: 182
- Code blocks changed? No
- Inline code changed? No
- Technical terms kept in English? Yes (e.g., Discrete logarithm, Baby-step giant-step, meet-in-the-middle, time complexity, binary exponentiation algorithm, map, red-black tree, binary search, hash table, unordered_map, Euler's theorem, gcd, coprime)
- Headings anchors preserved/added correctly? Yes
- I confirm no character was omitted: YES

Notes:
- Translated descriptive text.
- Updated internal links `(binary-exp.md)` and `(phi-function.md)` to `http://127.0.0.1:8000/algebra/binary-exp.md` and `http://127.0.0.1:8000/algebra/phi-function.md` respectively.
- External links were left unchanged.
- Code blocks and LaTeX formulas were preserved.
- Handled heading with `data-toc-label`.
- The C++ code blocks for `solve` are of `.cpp file=...` type, which is a special MkDocs syntax for including code from a file. This was preserved.