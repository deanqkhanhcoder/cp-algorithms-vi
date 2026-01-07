# Thuật toán Garner

Một hệ quả của [Định lý phần dư Trung Hoa](chinese-remainder-theorem.md) là chúng ta có thể biểu diễn các số lớn bằng một mảng các số nguyên nhỏ.
Ví dụ, đặt $p$ là tích của $1000$ số nguyên tố đầu tiên. $p$ có khoảng $3000$ chữ số.

Bất kỳ số $a$ nào nhỏ hơn $p$ đều có thể được biểu diễn dưới dạng một mảng $a_1, \ldots, a_k$, trong đó $a_i \equiv a \pmod{p_i}$.
Nhưng để làm được điều này, rõ ràng chúng ta cần biết cách lấy lại số $a$ từ biểu diễn của nó.
Một cách đã được thảo luận trong bài viết về Định lý phần dư Trung Hoa.

Trong bài viết này, chúng ta thảo luận về một giải pháp thay thế, Thuật toán Garner, cũng có thể được sử dụng cho mục đích này.

## Biểu diễn hệ cơ số hỗn hợp

Chúng ta có thể biểu diễn số $a$ trong biểu diễn **hệ cơ số hỗn hợp**:

$$a = x_1 + x_2 p_1 + x_3 p_1 p_2 + \ldots + x_k p_1 \cdots p_{k-1} \text{ với }x_i \in [0, p_i)$$

Một biểu diễn hệ cơ số hỗn hợp là một hệ đếm theo vị trí, đó là một sự tổng quát hóa của các hệ đếm thông thường, như hệ nhị phân hoặc hệ thập phân.
Ví dụ, hệ thập phân là một hệ đếm theo vị trí với cơ số 10.
Mọi số được biểu diễn dưới dạng một chuỗi các chữ số $d_1 d_2 d_3 \dots d_n$ từ $0$ đến $9$. Ví dụ, chuỗi $415$ biểu diễn số $4 \cdot 10^2 + 1 \cdot 10^1 + 5 \cdot 10^0$.
Nói chung, chuỗi chữ số $d_1 d_2 d_3 \dots d_n$ biểu diễn số $d_1 b^{n-1} + d_2 b^{n-2} + \cdots + d_n b^0$ trong hệ đếm theo vị trí với cơ số $b$.

Trong một hệ cơ số hỗn hợp, chúng ta không còn một cơ số duy nhất nữa. Cơ số thay đổi từ vị trí này sang vị trí khác.

## Thuật toán Garner

Thuật toán Garner tính toán các chữ số $x_1, \ldots, x_k$.
Lưu ý rằng các chữ số này tương đối nhỏ.
Chữ số $x_i$ là một số nguyên từ $0$ đến $p_i - 1$.

Đặt $r_{ij}$ là nghịch đảo của $p_i$ modulo $p_j$

$$r_{ij} = (p_i)^{-1} \pmod{p_j}$$

có thể được tìm thấy bằng thuật toán được mô tả trong [Nghịch đảo modular](module-inverse.md).

Thay thế $a$ từ biểu diễn hệ cơ số hỗn hợp vào phương trình đồng dư đầu tiên, chúng ta có được

$$a_1 \equiv x_1 \pmod{p_1}.$$

Thay vào phương trình thứ hai cho ra

$$a_2 \equiv x_1 + x_2 p_1 \pmod{p_2},$$

có thể được viết lại bằng cách trừ $x_1$ và chia cho $p_1$ để có được

$$\begin{array}{rclr}
    a_2 - x_1 &\equiv& x_2 p_1 &\pmod{p_2} \\
    (a_2 - x_1) r_{12} &\equiv& x_2 &\pmod{p_2} \\
    x_2 &\equiv& (a_2 - x_1) r_{12} &\pmod{p_2}
\end{array}$$

Tương tự, chúng ta có được rằng

$$x_3 \equiv ((a_3 - x_1) r_{13} - x_2) r_{23} \pmod{p_3}.$$

Bây giờ, chúng ta có thể thấy rõ một mẫu hình đang nổi lên, có thể được thể hiện bằng đoạn mã sau:

```cpp
for (int i = 0; i < k; ++i) {
    x[i] = a[i];
    for (int j = 0; j < i; ++j) {
        x[i] = r[j][i] * (x[i] - x[j]);

        x[i] = x[i] % p[i];
        if (x[i] < 0)
            x[i] += p[i];
    }
}
```

Vì vậy, chúng ta đã học cách tính các chữ số $x_i$ trong thời gian $O(k^2)$. Số $a$ bây giờ có thể được tính bằng công thức đã đề cập trước đó

$$a = x_1 + x_2 \cdot p_1 + x_3 \cdot p_1 \cdot p_2 + \ldots + x_k \cdot p_1 \cdots p_{k-1}$$

Điều đáng chú ý là trong thực tế, chúng ta gần như chắc chắn cần phải tính toán câu trả lời $a$ bằng [Số học với độ chính xác tùy ý](big-integer.md), nhưng các chữ số $x_i$ (vì chúng nhỏ) thường có thể được tính bằng các kiểu dữ liệu tích hợp sẵn, và do đó thuật toán Garner rất hiệu quả.

## Cài đặt thuật toán Garner

Thuận tiện để triển khai thuật toán này bằng Java, vì nó có hỗ trợ tích hợp cho các số lớn thông qua lớp `BigInteger`.

Ở đây, chúng tôi trình bày một cách triển khai có thể lưu trữ các số lớn dưới dạng một tập hợp các phương trình đồng dư.
Nó hỗ trợ phép cộng, trừ và nhân.
Và với thuật toán Garner, chúng ta có thể chuyển đổi tập hợp các phương trình thành số nguyên duy nhất.
Trong mã này, chúng ta lấy 100 số nguyên tố lớn hơn $10^9$, cho phép biểu diễn các số lớn tới $10^{900}$.

```java
final int SZ = 100;
int pr[] = new int[SZ];
int r[][] = new int[SZ][SZ];

void init() {
    for (int x = 1000 * 1000 * 1000, i = 0; i < SZ; ++x)
        if (BigInteger.valueOf(x).isProbablePrime(100))
            pr[i++] = x;

    for (int i = 0; i < SZ; ++i)
        for (int j = i + 1; j < SZ; ++j)
            r[i][j] =
                BigInteger.valueOf(pr[i]).modInverse(BigInteger.valueOf(pr[j])).intValue();
}

class Number {
    int a[] = new int[SZ];

    public Number() {
    }

    public Number(int n) {
        for (int i = 0; i < SZ; ++i)
            a[i] = n % pr[i];
    }

    public Number(BigInteger n) {
        for (int i = 0; i < SZ; ++i)
            a[i] = n.mod(BigInteger.valueOf(pr[i])).intValue();
    }

    public Number add(Number n) {
        Number result = new Number();
        for (int i = 0; i < SZ; ++i)
            result.a[i] = (a[i] + n.a[i]) % pr[i];
        return result;
    }

    public Number subtract(Number n) {
        Number result = new Number();
        for (int i = 0; i < SZ; ++i)
            result.a[i] = (a[i] - n.a[i] + pr[i]) % pr[i];
        return result;
    }

    public Number multiply(Number n) {
        Number result = new Number();
        for (int i = 0; i < SZ; ++i)
            result.a[i] = (int)((a[i] * 1l * n.a[i]) % pr[i]);
        return result;
    }

    public BigInteger bigIntegerValue(boolean can_be_negative) {
        BigInteger result = BigInteger.ZERO, mult = BigInteger.ONE;
        int x[] = new int[SZ];
        for (int i = 0; i < SZ; ++i) {
            x[i] = a[i];
            for (int j = 0; j < i; ++j) {
                long cur = (x[i] - x[j]) * 1l * r[j][i];
                x[i] = (int)((cur % pr[i] + pr[i]) % pr[i]);
            }
            result = result.add(mult.multiply(BigInteger.valueOf(x[i])));
            mult = mult.multiply(BigInteger.valueOf(pr[i]));
        }

        if (can_be_negative)
            if (result.compareTo(mult.shiftRight(1)) >= 0)
                result = result.subtract(mult);

        return result;
    }
}
```