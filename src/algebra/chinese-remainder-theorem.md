---
tags:
  - Translated
e_maxx_link: chinese_theorem
---

# Định lý phần dư Trung Hoa

Định lý phần dư Trung Hoa (sẽ được gọi là CRT trong phần còn lại của bài viết này) được phát hiện bởi nhà toán học Trung Quốc Tôn Tử.

## Phát biểu

Cho $m = m_1 \cdot m_2 \cdots m_k$, trong đó $m_i$ là các số nguyên tố cùng nhau từng đôi một. Ngoài $m_i$, chúng ta cũng được cho một hệ phương trình đồng dư

$$\left\{\begin{array}{rcl}
    a & \equiv & a_1 \pmod{m_1} \\
    a & \equiv & a_2 \pmod{m_2} \\
      & \vdots & \\
    a & \equiv & a_k \pmod{m_k}
\end{array}\right.$$

trong đó $a_i$ là một số hằng số đã cho. Dạng ban đầu của CRT sau đó phát biểu rằng hệ phương trình đồng dư đã cho luôn có *một và chỉ một* nghiệm modulo $m$.

Ví dụ: hệ phương trình đồng dư

$$\left\{\begin{array}{rcl}
    a & \equiv & 2 \pmod{3} \\
    a & \equiv & 3 \pmod{5} \\
    a & \equiv & 2 \pmod{7}
\end{array}\right.$$

có nghiệm là $23$ modulo $105$, vì $23 \bmod{3} = 2$, $23 \bmod{5} = 3$, và $23 \bmod{7} = 2$.
Chúng ta có thể viết mọi nghiệm dưới dạng $23 + 105\cdot k$ với $k \in \mathbb{Z}$.


### Hệ quả

Một hệ quả của CRT là phương trình

$$x \equiv a \pmod{m}$$

tương đương với hệ phương trình

$$\left\{\begin{array}{rcl}
    x & \equiv & a_1 \pmod{m_1} \\
      & \vdots & \\
    x & \equiv & a_k \pmod{m_k}
\end{array}\right.$$

(Như trên, giả sử rằng $m = m_1 m_2 \cdots m_k$ và $m_i$ là các số nguyên tố cùng nhau từng đôi một).

## Giải pháp cho hai Modulo

Xét một hệ hai phương trình với $m_1, m_2$ nguyên tố cùng nhau:

$$
\left\{\begin{align}
    a &\equiv a_1 \pmod{m_1} \\
    a &\equiv a_2 \pmod{m_2} \\
\end{align}\right.
$$

Chúng ta muốn tìm một nghiệm cho $a \pmod{m_1 m_2}$. Sử dụng [Thuật toán Euclid mở rộng](extended-euclid-algorithm.md) chúng ta có thể tìm các hệ số Bézout $n_1, n_2$ sao cho

$$n_1 m_1 + n_2 m_2 = 1.$$

Thực tế $n_1$ và $n_2$ chỉ là [nghịch đảo modular](module-inverse.md) của $m_1$ và $m_2$ theo modulo $m_2$ và $m_1$.
Chúng ta có $n_1 m_1 \equiv 1 \pmod{m_2}$ nên $n_1 \equiv m_1^{-1} \pmod{m_2}$, và ngược lại $n_2 \equiv m_2^{-1} \pmod{m_1}$.

Với hai hệ số đó, chúng ta có thể xác định một nghiệm:

$$a = a_1 n_2 m_2 + a_2 n_1 m_1 \bmod{m_1 m_2}$$

Dễ dàng xác minh rằng đây thực sự là một nghiệm bằng cách tính $a \bmod{m_1}$ và $a \bmod{m_2}$.

$$ 
\begin{array}{rcll}
a & \equiv & a_1 n_2 m_2 + a_2 n_1 m_1 & \pmod{m_1}\
  & \equiv & a_1 (1 - n_1 m_1) + a_2 n_1 m_1 & \pmod{m_1}\
  & \equiv & a_1 - a_1 n_1 m_1 + a_2 n_1 m_1 & \pmod{m_1}\
  & \equiv & a_1 & \pmod{m_1}
\end{array}
$$

Lưu ý rằng Định lý phần dư Trung Hoa cũng đảm bảo rằng chỉ có 1 nghiệm tồn tại modulo $m_1 m_2$.
Điều này cũng dễ chứng minh.

Giả sử bạn có hai nghiệm khác nhau là $x$ và $y$.
Vì $x \equiv a_i \pmod{m_i}$ và $y \equiv a_i \pmod{m_i}$, suy ra $x - y \equiv 0 \pmod{m_i}$ và do đó $x - y \equiv 0 \pmod{m_1 m_2}$ hoặc tương đương $x \equiv y \pmod{m_1 m_2}$.
Vì vậy, $x$ và $y$ thực ra là cùng một nghiệm.

## Giải pháp cho trường hợp tổng quát

### Giải pháp quy nạp

Vì $m_1 m_2$ nguyên tố cùng nhau với $m_3$, chúng ta có thể lặp đi lặp lại giải pháp cho hai modulo một cách quy nạp cho bất kỳ số lượng modulo nào.
Đầu tiên, bạn tính $b_2 := a \pmod{m_1 m_2}$ bằng cách sử dụng hai đồng dư thức đầu tiên,
sau đó bạn có thể tính $b_3 := a \pmod{m_1 m_2 m_3}$ bằng cách sử dụng các đồng dư thức $a \equiv b_2 \pmod{m_1 m_2}$ và $a \equiv a_3 \pmod {m_3}$, v.v.

### Xây dựng trực tiếp

Có thể xây dựng trực tiếp tương tự như phép nội suy Lagrange.

Đặt $M_i := \prod_{i \neq j} m_j$, là tích của tất cả các modulo trừ $m_i$, và $N_i$ là nghịch đảo modular $N_i := M_i^{-1} \bmod{m_i}$.
Khi đó, một nghiệm của hệ phương trình đồng dư là:

$$a \equiv \sum_{i=1}^k a_i M_i N_i \pmod{m_1 m_2 \cdots m_k}$$

Chúng ta có thể kiểm tra đây thực sự là một nghiệm, bằng cách tính $a \bmod{m_i}$ cho tất cả các $i$.
Bởi vì $M_j$ là bội số của $m_i$ với $i \neq j$, chúng ta có

$$\begin{array}{rcll}
a & \equiv & \sum_{j=1}^k a_j M_j N_j & \pmod{m_i} \\
  & \equiv & a_i M_i N_i              & \pmod{m_i} \\
  & \equiv & a_i M_i M_i^{-1}         & \pmod{m_i} \\
  & \equiv & a_i                      & \pmod{m_i}
\end{array}$$

### Cài đặt

```{.cpp file=chinese_remainder_theorem}
struct Congruence {
    long long a, m;
};

long long chinese_remainder_theorem(vector<Congruence> const& congruences) {
    long long M = 1;
    for (auto const& congruence : congruences) {
        M *= congruence.m;
    }

    long long solution = 0;
    for (auto const& congruence : congruences) {
        long long a_i = congruence.a;
        long long M_i = M / congruence.m;
        long long N_i = mod_inv(M_i, congruence.m);
        solution = (solution + a_i * M_i % M * N_i) % M;
    }
    return solution;
}
```

## Giải pháp cho các modulo không nguyên tố cùng nhau

Như đã đề cập, thuật toán trên chỉ hoạt động với các modulo $m_1, m_2, \dots, m_k$ nguyên tố cùng nhau.

Trong trường hợp không nguyên tố cùng nhau, một hệ phương trình đồng dư có đúng một nghiệm modulo $\text{lcm}(m_1, m_2, \dots, m_k)$, hoặc không có nghiệm nào cả.

Ví dụ: trong hệ sau, đồng dư thức đầu tiên ngụ ý rằng nghiệm là số lẻ, và đồng dư thức thứ hai ngụ ý rằng nghiệm là số chẵn.
Một số không thể vừa lẻ vừa chẵn, do đó rõ ràng không có nghiệm.

$$\left\{\begin{align}
    a & \equiv 1 \pmod{4} \\
    a & \equiv 2 \pmod{6}
\end{align}\right.$$

Khá đơn giản để xác định xem một hệ có nghiệm hay không.
Và nếu có, chúng ta có thể sử dụng thuật toán ban đầu để giải một hệ phương trình đồng dư đã được sửa đổi một chút.

Một đồng dư thức đơn $a \equiv a_i \pmod{m_i}$ tương đương với hệ phương trình đồng dư $a \equiv a_i \pmod{p_j^{n_j}}$ trong đó $p_1^{n_1} p_2^{n_2}\cdots p_k^{n_k}$ là phân tích thừa số nguyên tố của $m_i$.

Với thực tế này, chúng ta có thể sửa đổi hệ phương trình đồng dư thành một hệ chỉ có các lũy thừa của số nguyên tố làm modulo.
Ví dụ: hệ phương trình đồng dư ở trên tương đương với:

$$\left\{\begin{array}{ll}
    a \equiv 1          & \pmod{4} \\
    a \equiv 2 \equiv 0 & \pmod{2} \\
    a \equiv 2          & \pmod{3}
\end{array}\right.$$

Bởi vì ban đầu một số modulo có các thừa số chung, chúng ta sẽ nhận được một số modulo đồng dư dựa trên cùng một số nguyên tố, tuy nhiên có thể với các lũy thừa nguyên tố khác nhau.

Bạn có thể quan sát thấy rằng, đồng dư thức với modulo là lũy thừa nguyên tố cao nhất sẽ là đồng dư thức mạnh nhất trong tất cả các đồng dư thức dựa trên cùng một số nguyên tố.
Hoặc nó sẽ gây ra mâu thuẫn với một số đồng dư thức khác, hoặc nó sẽ bao hàm tất cả các đồng dư thức khác.

Trong trường hợp của chúng ta, đồng dư thức đầu tiên $a \equiv 1 \pmod{4}$ ngụ ý $a \equiv 1 \pmod{2}$, và do đó mâu thuẫn với đồng dư thức thứ hai $a \equiv 0 \pmod{2}$.
Do đó, hệ phương trình đồng dư này không có nghiệm.

Nếu không có mâu thuẫn, thì hệ phương trình có nghiệm.
Chúng ta có thể bỏ qua tất cả các đồng dư thức ngoại trừ những đồng dư thức có modulo là lũy thừa nguyên tố cao nhất.
Các modulo này bây giờ là nguyên tố cùng nhau, và do đó chúng ta có thể giải quyết hệ này bằng thuật toán đã thảo luận trong các phần trên.

Ví dụ: hệ sau có nghiệm modulo $\text{lcm}(10, 12) = 60$.

$$\left\{\begin{align}
    a & \equiv 3 \pmod{10} \\
    a & \equiv 5 \pmod{12}
\end{align}\right.$$

Hệ phương trình đồng dư tương đương với hệ phương trình đồng dư:

$$\left\{\begin{align}
    a & \equiv 3 \equiv 1 \pmod{2} \\
    a & \equiv 3 \equiv 3 \pmod{5} \\
    a & \equiv 5 \equiv 1 \pmod{4} \\
    a & \equiv 5 \equiv 2 \pmod{3}
\end{align}\right.$$

Đồng dư thức duy nhất có cùng modulo nguyên tố là $a \equiv 1 \pmod{4}$ và $a \equiv 1 \pmod{2}$.
Cái đầu tiên đã bao hàm cái thứ hai, vì vậy chúng ta có thể bỏ qua cái thứ hai và giải hệ sau với các modulo nguyên tố cùng nhau thay thế:

$$\left\{\begin{align}
    a & \equiv 3 \equiv 3 \pmod{5} \\
    a & \equiv 5 \equiv 1 \pmod{4} \\
    a & \equiv 5 \equiv 2 \pmod{3}
\end{align}\right.$$

Nó có nghiệm $53 \pmod{60}$, và thực sự $53 \bmod{10} = 3$ và $53 \bmod{12} = 5$.

## Thuật toán Garner

Một hệ quả khác của CRT là chúng ta có thể biểu diễn các số lớn bằng cách sử dụng một mảng các số nguyên nhỏ.

Thay vì thực hiện nhiều tính toán với các số rất lớn, có thể tốn kém (hãy nghĩ đến việc thực hiện các phép chia với các số có 1000 chữ số), bạn có thể chọn một vài modulo nguyên tố cùng nhau và biểu diễn số lớn dưới dạng một hệ phương trình đồng dư, và thực hiện tất cả các phép toán trên hệ phương trình đó.
Bất kỳ số $a$ nào nhỏ hơn $m_1 m_2 \cdots m_k$ đều có thể được biểu diễn dưới dạng một mảng $a_1, \ldots, a_k$, trong đó $a \equiv a_i \pmod{m_i}$.

Bằng cách sử dụng thuật toán trên, bạn có thể tái tạo lại số lớn bất cứ khi nào bạn cần.

Ngoài ra, bạn có thể biểu diễn số trong biểu diễn **hệ cơ số hỗn hợp**:

$$a = x_1 + x_2 m_1 + x_3 m_1 m_2 + \ldots + x_k m_1 \cdots m_{k-1} \text{ với }x_i \in [0, m_i)$$

Thuật toán Garner, được thảo luận trong bài viết chuyên dụng [Thuật toán Garner](garners-algorithm.md), tính toán các hệ số $x_i$.
Và với các hệ số đó, bạn có thể khôi phục lại toàn bộ số.

## Bài tập luyện tập:

* [Google Code Jam - Golf Gophers](https://github.com/google/coding-competitions-archive/blob/main/codejam/2019/round_1a/golf_gophers/statement.pdf)
* [Hackerrank - Number of sequences](https://www.hackerrank.com/contests/w22/challenges/number-of-sequences)
* [Codeforces - Remainders Game](http://codeforces.com/problemset/problem/687/B)