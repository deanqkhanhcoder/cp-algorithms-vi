---
tags:
  - Translated
e_maxx_link: euclid_algorithm
---

# Thuật toán Euclid tìm ước chung lớn nhất

Cho hai số nguyên không âm $a$ và $b$, chúng ta phải tìm **ƯCLN** (ước chung lớn nhất) của chúng, tức là số lớn nhất là ước của cả $a$ và $b$.
Nó thường được ký hiệu là $\gcd(a, b)$. Về mặt toán học, nó được định nghĩa là:

$$\gcd(a, b) = \max \{k > 0 : (k \mid a) \text{ và } (k \mid b) \} $$

(ở đây ký hiệu "$\|$" biểu thị tính chia hết, tức là "$k \mid a$" có nghĩa là "$k$ chia hết cho $a$")

Khi một trong hai số bằng không, trong khi số kia khác không, ước chung lớn nhất của chúng, theo định nghĩa, là số thứ hai. Khi cả hai số đều bằng không, ước chung lớn nhất của chúng không được xác định (nó có thể là bất kỳ số lớn tùy ý nào), nhưng để bảo toàn tính kết hợp của $\gcd$, ta quy ước nó bằng không. Điều này cho chúng ta một quy tắc đơn giản: nếu một trong hai số bằng không, ước chung lớn nhất là số còn lại.

Thuật toán Euclid, được thảo luận dưới đây, cho phép tìm ước chung lớn nhất của hai số $a$ và $b$ trong $O(\log \min(a, b))$. Vì hàm này có tính **kết hợp**, để tìm ƯCLN của **nhiều hơn hai số**, chúng ta có thể thực hiện $\gcd(a, b, c) = \gcd(a, \gcd(b, c))$ và cứ thế.

Thuật toán được mô tả lần đầu tiên trong "Cơ sở" của Euclid (khoảng 300 TCN), nhưng có khả năng thuật toán này có nguồn gốc sớm hơn nữa.

## Thuật toán

Ban đầu, thuật toán Euclid được phát biểu như sau: trừ số nhỏ hơn khỏi số lớn hơn cho đến khi một trong hai số bằng không. Thật vậy, nếu $g$ chia hết cho $a$ và $b$, nó cũng chia hết cho $a-b$. Mặt khác, nếu $g$ chia hết cho $a-b$ và $b$, thì nó cũng chia hết cho $a = b + (a-b)$, điều đó có nghĩa là tập hợp các ước chung của $\{a, b\}$ và $\{b,a-b\}$ trùng nhau.

Lưu ý rằng $a$ vẫn là số lớn hơn cho đến khi $b$ được trừ khỏi nó ít nhất $\left\lfloor\frac{a}{b}\right\rfloor$ lần. Do đó, để tăng tốc, $a-b$ được thay thế bằng $a-\left\lfloor\frac{a}{b}\right\rfloor b = a \bmod b$. Khi đó thuật toán được phát biểu một cách cực kỳ đơn giản:

$$\gcd(a, b) = \begin{cases}a, & \text{nếu }b = 0 \\ \gcd(b, a \bmod b), & \text{nếu khác.}\\end{cases}$$ 

## Cài đặt {#implementation}

```cpp
int gcd (int a, int b) {
    if (b == 0)
        return a;
    else
        return gcd (b, a % b);
}
```

Sử dụng toán tử ba ngôi trong C++, chúng ta có thể viết nó thành một dòng.

```cpp
int gcd (int a, int b) {
    return b ? gcd (b, a % b) : a;
}
```

Và cuối cùng, đây là một cài đặt không đệ quy:

```cpp
int gcd (int a, int b) {
    while (b) {
        a %= b;
        swap(a, b);
    }
    return a;
}
```

Lưu ý rằng kể từ C++17, `gcd` được triển khai như một [hàm tiêu chuẩn](https://en.cppreference.com/w/cpp/numeric/gcd) trong C++.

## Độ phức tạp thời gian

Thời gian chạy của thuật toán được ước tính bằng định lý Lamé, định lý này thiết lập một mối liên hệ đáng ngạc nhiên giữa thuật toán Euclid và dãy Fibonacci:

Nếu $a > b \geq 1$ và $b < F_n$ đối với một số $n$ nào đó, thuật toán Euclid thực hiện tối đa $n-2$ lần gọi đệ quy.

Hơn nữa, có thể chỉ ra rằng cận trên của định lý này là tối ưu. Khi $a = F_n$ và $b = F_{n-1}$, $\gcd(a, b)$ sẽ thực hiện chính xác $n-2$ lần gọi đệ quy. Nói cách khác, các số Fibonacci liên tiếp là trường hợp đầu vào xấu nhất cho thuật toán Euclid.

Biết rằng các số Fibonacci tăng theo cấp số nhân, chúng ta có được thuật toán Euclid hoạt động trong $O(\log \min(a, b))$.

Một cách khác để ước tính độ phức tạp là nhận thấy rằng $a \bmod b$ trong trường hợp $a \geq b$ nhỏ hơn ít nhất 2 lần so với $a$, vì vậy số lớn hơn bị giảm ít nhất một nửa sau mỗi lần lặp của thuật toán. Áp dụng lý luận này cho trường hợp khi chúng ta tính ƯCLN của tập hợp các số $a_1,\dots,a_n \leq C$, điều này cũng cho phép chúng ta ước tính tổng thời gian chạy là $O(n + \log C)$, thay vì $O(n \log C)$, vì mỗi lần lặp không tầm thường của thuật toán đều làm giảm ứng cử viên ƯCLN hiện tại đi ít nhất một hệ số 2.

## Bội chung nhỏ nhất

Việc tính bội chung nhỏ nhất (thường được ký hiệu là **BCNN**) có thể được quy về việc tính ƯCLN bằng công thức đơn giản sau:

$$\text{lcm}(a, b) = \frac{a \cdot b}{\gcd(a, b)}$$

Do đó, BCNN có thể được tính bằng thuật toán Euclid với cùng độ phức tạp thời gian:

Một cài đặt khả thi, khéo léo tránh tràn số nguyên bằng cách chia $a$ cho ƯCLN trước, được đưa ra ở đây:

```cpp
int lcm (int a, int b) {
    return a / gcd(a, b) * b;
}
```

## ƯCLN nhị phân

Thuật toán ƯCLN nhị phân là một tối ưu hóa cho thuật toán Euclid thông thường.

Phần chậm của thuật toán thông thường là các phép toán modulo. Các phép toán modulo, mặc dù chúng ta coi chúng là $O(1)$, nhưng chậm hơn nhiều so với các phép toán đơn giản hơn như cộng, trừ hoặc các phép toán trên bit.
Vì vậy, sẽ tốt hơn nếu tránh chúng.

Hóa ra, bạn có thể thiết kế một thuật toán ƯCLN nhanh chóng tránh các phép toán modulo.
Nó dựa trên một vài thuộc tính:

  - Nếu cả hai số đều chẵn, thì chúng ta có thể tách thừa số hai ra khỏi cả hai và tính ƯCLN của các số còn lại: $\gcd(2a, 2b) = 2 \gcd(a, b)$.
  - Nếu một trong hai số chẵn và số kia lẻ, thì chúng ta có thể loại bỏ thừa số 2 khỏi số chẵn: $\gcd(2a, b) = \gcd(a, b)$ nếu $b$ lẻ.
  - Nếu cả hai số đều lẻ, thì việc trừ một số cho số kia sẽ không làm thay đổi ƯCLN: $\gcd(a, b) = \gcd(b, a-b)$

Chỉ sử dụng các thuộc tính này và một số hàm thao tác bit nhanh từ GCC, chúng ta có thể triển khai một phiên bản nhanh:

```cpp
int gcd(int a, int b) {
    if (!a || !b)
        return a | b;
    unsigned shift = __builtin_ctz(a | b);
    a >>= __builtin_ctz(a);
    do {
        b >>= __builtin_ctz(b);
        if (a > b)
            swap(a, b);
        b -= a;
    } while (b);
    return a << shift;
}
```

Lưu ý, một tối ưu hóa như vậy thường không cần thiết, và hầu hết các ngôn ngữ lập trình đã có một hàm ƯCLN trong thư viện chuẩn của họ.
Ví dụ: C++17 có một hàm `std::gcd` như vậy trong header `numeric`.

## Bài tập luyện tập

- [CSAcademy - Greatest Common Divisor](https://csacademy.com/contest/archive/task/gcd/)
- [Codeforces 1916B - Two Divisors](https://codeforces.com/contest/1916/problem/B)