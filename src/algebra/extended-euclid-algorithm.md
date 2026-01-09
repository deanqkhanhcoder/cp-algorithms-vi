---
tags:
  - Translated
e_maxx_link: extended_euclid_algorithm
---

# Thuật toán Euclid mở rộng (Extended Euclidean Algorithm) {: #extended-euclid-algorithm}

Trong khi [thuật toán Euclid](euclid-algorithm.md) chỉ tính ước chung lớn nhất (GCD) của hai số nguyên $a$ và $b$, phiên bản mở rộng còn tìm cách biểu diễn GCD theo $a$ và $b$, tức là các hệ số $x$ và $y$ sao cho:

$$a \cdot x + b \cdot y = \gcd(a, b)$$

Quan trọng cần lưu ý là theo [Đẳng thức Bézout](https://en.wikipedia.org/wiki/B%C3%A9zout%27s_identity), chúng ta luôn có thể tìm thấy một biểu diễn như vậy. Ví dụ, $\gcd(55, 80) = 5$, do đó chúng ta có thể biểu diễn $5$ dưới dạng tổ hợp tuyến tính với các số hạng $55$ và $80$: $55 \cdot 3 + 80 \cdot (-2) = 5$ 

Một dạng tổng quát hơn của bài toán đó được thảo luận trong bài viết về [Phương trình Diophantine tuyến tính](linear-diophantine-equation.md).
Nó sẽ dựa trên thuật toán này.

## Thuật toán (Algorithm) {: #algorithm}

Chúng ta sẽ ký hiệu GCD của $a$ và $b$ là $g$ trong phần này.

Những thay đổi so với thuật toán gốc rất đơn giản.
Nếu chúng ta nhớ lại thuật toán, chúng ta có thể thấy rằng thuật toán kết thúc với $b = 0$ và $a = g$.
Đối với các tham số này, chúng ta có thể dễ dàng tìm thấy các hệ số, cụ thể là $g \cdot 1 + 0 \cdot 0 = g$.

Bắt đầu từ các hệ số này $(x, y) = (1, 0)$, chúng ta có thể đi ngược lên các lời gọi đệ quy.
Tất cả những gì chúng ta cần làm là tìm ra cách các hệ số $x$ và $y$ thay đổi trong quá trình chuyển đổi từ $(a, b)$ sang $(b, a \bmod b)$.

Giả sử chúng ta tìm thấy các hệ số $(x_1, y_1)$ cho $(b, a \bmod b)$:

$$b \cdot x_1 + (a \bmod b) \cdot y_1 = g$$

và chúng ta muốn tìm cặp $(x, y)$ cho $(a, b)$:

$$ a \cdot x + b \cdot y = g$$

Chúng ta có thể biểu diễn $a \bmod b$ như sau:

$$ a \bmod b = a - \left\lfloor \frac{a}{b} \right\rfloor \cdot b$$

Thay thế biểu thức này vào phương trình hệ số của $(x_1, y_1)$ ta được:

$$ g = b \cdot x_1 + (a \bmod b) \cdot y_1 = b \cdot x_1 + \left(a - \left\lfloor \frac{a}{b} \right\rfloor \cdot b \right) \cdot y_1$$

và sau khi sắp xếp lại các số hạng:

$$g = a \cdot y_1 + b \cdot \left( x_1 - y_1 \cdot \left\lfloor \frac{a}{b} \right\rfloor \right)$$

Chúng ta đã tìm thấy các giá trị của $x$ và $y$:

$$\begin{cases}
x = y_1 \\
y = x_1 - y_1 \cdot \left\lfloor \frac{a}{b} \right\rfloor
\end{cases} $$

## Cài đặt (Implementation) {: #implementation}

```{.cpp file=extended_gcd}
int gcd(int a, int b, int& x, int& y) {
    if (b == 0) {
        x = 1;
        y = 0;
        return a;
    }
    int x1, y1;
    int d = gcd(b, a % b, x1, y1);
    x = y1;
    y = x1 - y1 * (a / b);
    return d;
}
```

Hàm đệ quy ở trên trả về GCD và các giá trị của hệ số cho `x` và `y` (được truyền tham chiếu vào hàm).

Cài đặt này của thuật toán Euclid mở rộng tạo ra kết quả chính xác cho cả các số nguyên âm.

## Phiên bản lặp (Iterative version) {: #iterative-version}

Cũng có thể viết thuật toán Euclid mở rộng theo cách lặp.
Vì nó tránh đệ quy, mã sẽ chạy nhanh hơn một chút so với mã đệ quy.

```{.cpp file=extended_gcd_iter}
int gcd(int a, int b, int& x, int& y) {
    x = 1, y = 0;
    int x1 = 0, y1 = 1, a1 = a, b1 = b;
    while (b1) {
        int q = a1 / b1;
        tie(x, x1) = make_tuple(x1, x - q * x1);
        tie(y, y1) = make_tuple(y1, y - q * y1);
        tie(a1, b1) = make_tuple(b1, a1 - q * b1);
    }
    return a1;
}
```

Nếu bạn nhìn kỹ vào các biến `a1` và `b1`, bạn có thể nhận thấy rằng chúng nhận chính xác các giá trị giống như trong phiên bản lặp của [thuật toán Euclid](euclid-algorithm.md#implementation) thông thường. Vì vậy, thuật toán ít nhất sẽ tính đúng GCD.

Để biết tại sao thuật toán tính đúng các hệ số, hãy xem xét rằng các bất biến sau đây giữ nguyên tại bất kỳ thời điểm nào (trước khi vòng lặp while bắt đầu và ở cuối mỗi lần lặp):

$$x \cdot a + y \cdot b = a_1$$

$$x_1 \cdot a + y_1 \cdot b = b_1$$

Gọi các giá trị ở cuối một lần lặp được ký hiệu bằng dấu phẩy ($'$), và giả sử $q = \frac{a_1}{b_1}$. Từ [thuật toán Euclid](euclid-algorithm.md), chúng ta có:

$$a_1' = b_1$$

$$b_1' = a_1 - q \cdot b_1$$

Để bất biến đầu tiên giữ nguyên, điều sau phải đúng:

$$x' \cdot a + y' \cdot b = a_1' = b_1$$

$$x' \cdot a + y' \cdot b = x_1 \cdot a + y_1 \cdot b$$

Tương tự đối với bất biến thứ hai, điều sau phải giữ nguyên:

$$x_1' \cdot a + y_1' \cdot b = a_1 - q \cdot b_1$$

$$x_1' \cdot a + y_1' \cdot b = (x - q \cdot x_1) \cdot a + (y - q \cdot y_1) \cdot b$$

Bằng cách so sánh các hệ số của $a$ và $b$, các phương trình cập nhật cho mỗi biến có thể được suy ra, đảm bảo rằng các bất biến được duy trì trong suốt thuật toán.


Ở cuối chúng ta biết rằng $a_1$ chứa GCD, vì vậy $x \cdot a + y \cdot b = g$.
Điều đó có nghĩa là chúng ta đã tìm thấy các hệ số cần thiết.

Bạn thậm chí có thể tối ưu hóa mã hơn nữa, và loại bỏ biến $a_1$ và $b_1$ khỏi mã, và chỉ sử dụng lại $a$ và $b$.
Tuy nhiên nếu bạn làm vậy, bạn sẽ mất khả năng lập luận về các bất biến.

## Bài tập luyện tập {: #practice-problems}

* [UVA - 10104 - Euclid Problem](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1045)
* [GYM - (J) Once Upon A Time](http://codeforces.com/gym/100963)
* [UVA - 12775 - Gift Dilemma](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=4628)

---
