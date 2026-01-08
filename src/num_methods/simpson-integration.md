---
tags:
  - Translated
e_maxx_link: simpson_integrating
---

# Tích phân bằng công thức Simpson (Integration by Simpson's formula) {: #integration-by-simpsons-formula}

Chúng ta sẽ tính giá trị của một tích phân xác định

$$\int_a ^ b f (x) dx$$

Giải pháp được mô tả ở đây đã được xuất bản trong một trong những luận văn của **Thomas Simpson** vào năm 1743.

## Công thức Simpson (Simpson's formula) {: #simpsons-formula}

Cho $n$ là một số tự nhiên nào đó. Chúng ta chia đoạn tích phân $[a, b]$ thành $2n$ phần bằng nhau:

$$x_i = a + i h, ~~ i = 0 \ldots 2n,$$

$$h = \frac {b-a} {2n}.$$

Bây giờ chúng ta tính tích phân riêng biệt trên mỗi đoạn $[x_ {2i-2}, x_ {2i}]$, $i = 1 \ldots n$, và sau đó cộng tất cả các giá trị lại.

Vì vậy, giả sử chúng ta xem xét đoạn tiếp theo $[x_ {2i-2}, x_ {2i}],  i = 1 \ldots n$. Thay thế hàm $f(x)$ trên đó bằng một parabol $P(x)$ đi qua 3 điểm $(x_ {2i-2}, x_ {2i-1}, x_ {2i})$. Một parabol như vậy luôn tồn tại và là duy nhất; nó có thể được tìm thấy bằng giải tích.
Ví dụ, chúng ta có thể xây dựng nó bằng cách sử dụng nội suy đa thức Lagrange.
Điều duy nhất còn lại phải làm là tích phân đa thức này.
Nếu bạn làm điều này cho một hàm tổng quát $f$, bạn sẽ nhận được một biểu thức đơn giản đáng kể:

$$\int_{x_ {2i-2}} ^ {x_ {2i}} f (x) ~dx \approx \int_{x_ {2i-2}} ^ {x_ {2i}} P (x) ~dx = \left(f(x_{2i-2}) + 4f(x_{2i-1})+(f(x_{2i})\right)\frac {h} {3} $$

Cộng các giá trị này trên tất cả các đoạn, chúng ta thu được **công thức Simpson** cuối cùng:

$$\int_a ^ b f (x) dx \approx \left(f (x_0) + 4 f (x_1) + 2 f (x_2) + 4f(x_3) + 2 f(x_4) + \ldots + 4 f(x_{2N-1}) + f(x_{2N}) \right)\frac {h} {3} $$

## Sai số (Error) {: #error}

Sai số trong việc tính gần đúng tích phân theo công thức Simpson là

$$ -\tfrac{1}{90} \left(\tfrac{b-a}{2}\right)^5 f^{(4)}(\xi)$$

trong đó $\xi$ là một số nào đó giữa $a$ và $b$.

Sai số tỷ lệ thuận theo tiệm cận với $(b-a)^5$. Tuy nhiên, các dẫn xuất ở trên gợi ý một sai số tỷ lệ với $(b-a)^4$. Quy tắc Simpson có thêm một bậc vì các điểm mà tích phân được đánh giá được phân phối đối xứng trong khoảng $[a, b]$.

## Cài đặt (Implementation) {: #implementation}

Ở đây, $f(x)$ là một hàm người dùng định nghĩa nào đó.

```cpp
const int N = 1000 * 1000; // số lượng bước (đã nhân với 2)

double simpson_integration(double a, double b){
    double h = (b - a) / N;
    double s = f(a) + f(b); // a = x_0 and b = x_2n
    for (int i = 1; i <= N - 1; ++i) { // Tham khảo công thức Simpson cuối cùng
        double x = a + h * i;
        s += f(x) * ((i & 1) ? 4 : 2);
    }
    s *= h / 3;
    return s;
}
```

## Bài tập (Practice Problems) {: #practice-problems}

* [Latin American Regionals 2012 - Environment Protection](https://matcomgrader.com/problem/9335/environment-protection/)
