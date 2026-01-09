---
tags:
  - Translated
e_maxx_link: factorial_divisors
---

# Tìm lũy thừa của ước giai thừa (Finding Power of Factorial Divisor) {: #finding-power-of-factorial-divisor}

Bạn được cho hai số $n$ và $k$. Tìm số nguyên $x$ lớn nhất sao cho $k^x$ chia hết $n!$.

## $k$ nguyên tố (Prime $k$) {: #prime-k data-toc-label="Prime k"}

Đầu tiên hãy xem xét trường hợp $k$ nguyên tố. Biểu thức tường minh cho giai thừa

$$n! = 1 \cdot 2 \cdot 3 \ldots (n-1) \cdot n$$

Lưu ý rằng mỗi phần tử thứ $k$ của tích chia hết cho $k$, tức là thêm $+1$ vào câu trả lời; số lượng các phần tử như vậy là $\Bigl\lfloor\dfrac{n}{k}\Bigr\rfloor$.

Tiếp theo, mỗi phần tử thứ $k^2$ chia hết cho $k^2$, tức là thêm $+1$ nữa vào câu trả lời (lũy thừa đầu tiên của $k$ đã được tính trong đoạn trước). Số lượng các phần tử như vậy là $\Bigl\lfloor\dfrac{n}{k^2}\Bigr\rfloor$.

Và cứ thế, đối với mỗi $i$, mỗi phần tử thứ $k^i$ thêm $+1$ nữa vào câu trả lời, và có $\Bigl\lfloor\dfrac{n}{k^i}\Bigr\rfloor$ phần tử như vậy.

Câu trả lời cuối cùng là

$$\Bigl\lfloor\dfrac{n}{k}\Bigr\rfloor + \Bigl\lfloor\dfrac{n}{k^2}\Bigr\rfloor + \ldots + \Bigl\lfloor\dfrac{n}{k^i}\Bigr\rfloor + \ldots$$

Kết quả này còn được gọi là [Công thức Legendre](https://en.wikipedia.org/wiki/Legendre%27s_formula).
Tổng tất nhiên là hữu hạn, vì chỉ khoảng $\log_k n$ phần tử đầu tiên là khác không. Do đó, thời gian chạy của thuật toán này là $O(\log_k n)$.

### Cài đặt {: #implementation}

```cpp

int fact_pow (int n, int k) {
	int res = 0;
	while (n) {
		n /= k;
		res += n;
	}
	return res;
}

```

## $k$ hợp số (Composite $k$) {: #composite-k data-toc-label="Composite k"}

Ý tưởng tương tự không thể được áp dụng trực tiếp. Thay vào đó chúng ta có thể phân tích thừa số $k$, biểu diễn nó dưới dạng $k = k_1^{p_1} \cdot \ldots \cdot k_m^{p_m}$. Với mỗi $k_i$, chúng ta tìm số lần nó xuất hiện trong $n!$ bằng cách sử dụng thuật toán được mô tả ở trên - gọi giá trị này là $a_i$. Câu trả lời cho $k$ hợp số sẽ là

$$\min_ {i=1 \ldots m} \dfrac{a_i}{p_i}$$
