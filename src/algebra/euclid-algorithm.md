---
tags:
  - Translated
e_maxx_link: euclid_algorithm
---

# Thuật toán Euclid để tính ước chung lớn nhất (Euclidean algorithm for computing the greatest common divisor) {: #euclidean-algorithm-gcd}

Cho hai số nguyên không âm $a$ và $b$, chúng ta phải tìm **GCD** (ước chung lớn nhất) của chúng, tức là số lớn nhất là ước của cả $a$ và $b$.
Nó thường được ký hiệu là $\gcd(a, b)$. Về mặt toán học nó được định nghĩa là:

$$\gcd(a, b) = \max \{k > 0 : (k \mid a) \text{ và } (k \mid b) \}$$

(ở đây ký hiệu "$\mid$" biểu thị tính chia hết, tức là "$k \mid a$" có nghĩa là "$k$ chia hết cho $a$")

Khi một trong các số bằng không, trong khi số kia khác không, ước chung lớn nhất của chúng, theo định nghĩa, là số thứ hai. Khi cả hai số đều bằng không, ước chung lớn nhất của chúng không xác định (nó có thể là bất kỳ số nào lớn tùy ý), nhưng thuận tiện khi định nghĩa nó cũng bằng không để bảo toàn tính kết hợp của $\gcd$. Điều này mang lại cho chúng ta một quy tắc đơn giản: nếu một trong các số bằng không, ước chung lớn nhất là số kia.

Thuật toán Euclid, được thảo luận dưới đây, cho phép tìm ước chung lớn nhất của hai số $a$ và $b$ trong $O(\log \min(a, b))$. Vì hàm này có **tính kết hợp**, để tìm GCD của **nhiều hơn hai số**, chúng ta có thể làm $\gcd(a, b, c) = \gcd(a, \gcd(b, c))$ và cứ thế.

Thuật toán được mô tả lần đầu tiên trong "Cơ sở" của Euclid (khoảng 300 trước Công nguyên), nhưng có thể thuật toán có nguồn gốc sớm hơn nữa.

## Thuật toán (Algorithm) {: #algorithm}

Ban đầu, thuật toán Euclid được phát biểu như sau: trừ số nhỏ hơn khỏi số lớn hơn cho đến khi một trong các số bằng không. Thật vậy, nếu $g$ chia hết cho $a$ và $b$, nó cũng chia hết cho $a-b$. Mặt khác, nếu $g$ chia hết cho $a-b$ và $b$, thì nó cũng chia hết cho $a = b + (a-b)$, điều đó có nghĩa là tập hợp các ước chung của $\{a, b\}$ và $\{b,a-b\}$ trùng nhau.

Lưu ý rằng $a$ vẫn là số lớn hơn cho đến khi $b$ được trừ khỏi nó ít nhất $\left\lfloor\frac{a}{b}\right\rfloor$ lần. Do đó, để tăng tốc mọi thứ, $a-b$ được thay thế bằng $a-\left\lfloor\frac{a}{b}\right\rfloor b = a \bmod b$. Khi đó thuật toán được phát biểu theo cách cực kỳ đơn giản:

$$\gcd(a, b) = \begin{cases}a,&\text{nếu }b = 0 \\ \gcd(b, a \bmod b),&\text{ngược lại.}\end{cases}$$

## Cài đặt (Implementation) {: #implementation}

```cpp
int gcd (int a, int b) {
    if (b == 0)
        return a;
    else
        return gcd (b, a % b);
}
```

Sử dụng toán tử tam phân trong C++, chúng ta có thể viết nó dưới dạng một dòng.

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

Lưu ý rằng kể từ C++17, `gcd` được cài đặt như một [hàm chuẩn](https://en.cppreference.com/w/cpp/numeric/gcd) trong C++.

## Độ phức tạp thời gian (Time Complexity) {: #time-complexity}

Thời gian chạy của thuật toán được ước tính bởi định lý Lamé, định lý này thiết lập một mối liên hệ đáng ngạc nhiên giữa thuật toán Euclid và dãy Fibonacci:

Nếu $a > b \geq 1$ và $b < F_n$ với một số $n$, thuật toán Euclid thực hiện tối đa $n-2$ lời gọi đệ quy.

Hơn nữa, có thể chỉ ra rằng cận trên của định lý này là tối ưu. Khi $a = F_n$ và $b = F_{n-1}$, $gcd(a, b)$ sẽ thực hiện chính xác $n-2$ lời gọi đệ quy. Nói cách khác, các số Fibonacci liên tiếp là đầu vào trường hợp xấu nhất cho thuật toán Euclid.

Cho rằng các số Fibonacci tăng theo cấp số nhân, chúng ta nhận được rằng thuật toán Euclid hoạt động trong $O(\log \min(a, b))$.

Một cách khác để ước tính độ phức tạp là nhận thấy rằng $a \bmod b$ cho trường hợp $a \geq b$ nhỏ hơn ít nhất $2$ lần so với $a$, vì vậy số lớn hơn giảm ít nhất một nửa sau mỗi lần lặp của thuật toán. Áp dụng lý luận này cho trường hợp khi chúng ta tính GCD của tập hợp các số $a_1,\dots,a_n \leq C$, điều này cũng cho phép chúng ta ước tính tổng thời gian chạy là $O(n + \log C)$, thay vì $O(n \log C)$, vì mỗi lần lặp không tầm thường của thuật toán giảm ứng cử viên GCD hiện tại đi ít nhất một hệ số $2$.

## Bội chung nhỏ nhất (Least common multiple) {: #least-common-multiple}

Việc tính toán bội chung nhỏ nhất (thường được ký hiệu là **LCM**) có thể được quy về việc tính toán GCD với công thức đơn giản sau:

$$\text{lcm}(a, b) = \frac{a \cdot b}{\gcd(a, b)}$$

Do đó, LCM có thể được tính toán bằng thuật toán Euclid với cùng độ phức tạp thời gian:

Một cài đặt khả thi, tránh tràn số nguyên một cách khéo léo bằng cách chia $a$ cho GCD trước, được đưa ra dưới đây:

```cpp
int lcm (int a, int b) {
    return a / gcd(a, b) * b;
}
```

## GCD nhị phân (Binary GCD) {: #binary-gcd}

Thuật toán GCD nhị phân là một tối ưu hóa cho thuật toán Euclid thông thường.

Phần chậm của thuật toán thông thường là các phép toán modulo. Các phép toán modulo, mặc dù chúng ta xem chúng là $O(1)$, chậm hơn nhiều so với các phép toán đơn giản hơn như cộng, trừ hoặc các phép toán bit.
Vì vậy sẽ tốt hơn nếu tránh chúng.

Hóa ra, bạn có thể thiết kế một thuật toán GCD nhanh tránh các phép toán modulo.
Nó dựa trên một vài tính chất:

  - Nếu cả hai số đều chẵn, thì chúng ta có thể đưa thừa số hai ra ngoài và tính GCD của các số còn lại: $\gcd(2a, 2b) = 2 \gcd(a, b)$.
  - Nếu một trong các số là chẵn và số kia là lẻ, thì chúng ta có thể loại bỏ thừa số 2 khỏi số chẵn: $\gcd(2a, b) = \gcd(a, b)$ nếu $b$ là lẻ.
  - Nếu cả hai số đều lẻ, thì trừ một số khỏi số kia sẽ không làm thay đổi GCD: $\gcd(a, b) = \gcd(b, a-b)$

Chỉ sử dụng các tính chất này, và một số hàm bit nhanh từ GCC, chúng ta có thể cài đặt một phiên bản nhanh:

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

Lưu ý rằng sự tối ưu hóa như vậy thường không cần thiết, và hầu hết các ngôn ngữ lập trình đã có hàm GCD trong thư viện chuẩn của chúng.
V.d. C++17 có hàm `std::gcd` trong header `numeric`.

## Bài tập luyện tập {: #practice-problems}

- [CSAcademy - Greatest Common Divisor](https://csacademy.com/contest/archive/task/gcd/)
- [Codeforces 1916B - Two Divisors](https://codeforces.com/contest/1916/problem/B)

---
