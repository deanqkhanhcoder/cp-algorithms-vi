---
tags:
  - Translated
e_maxx_link: factorial_divisors
---

# Tìm số mũ của ước số giai thừa

Bạn được cho hai số $n$ và $k$. Tìm số nguyên lớn nhất $x$ sao cho $k^x$ là ước của $n!$.

## $k$ là số nguyên tố {data-toc-label="Prime k"}

Trước tiên hãy xem xét trường hợp $k$ là số nguyên tố. Biểu thức tường minh cho giai thừa là

$$n! = 1 \cdot 2 \cdot 3 \ldots (n-1) \cdot n$$

Lưu ý rằng mỗi phần tử thứ $k$ của tích chia hết cho $k$, tức là cộng thêm $+1$ vào câu trả lời; số lượng các phần tử như vậy là $\Bigl\lfloor\dfrac{n}{k}\Bigr\rfloor$.

Tiếp theo, mỗi phần tử thứ $k^2$ chia hết cho $k^2$, tức là cộng thêm một $+1$ nữa vào câu trả lời (lũy thừa đầu tiên của $k$ đã được đếm ở đoạn trước). Số lượng các phần tử như vậy là $\Bigl\lfloor\dfrac{n}{k^2}\Bigr\rfloor$.

Và cứ thế, với mỗi $i$, mỗi phần tử thứ $k^i$ lại cộng thêm một $+1$ nữa vào câu trả lời, và có $\Bigl\lfloor\dfrac{n}{k^i}\Bigr\rfloor$ phần tử như vậy.

Câu trả lời cuối cùng là

$$\Bigl\lfloor\dfrac{n}{k}\Bigr\rfloor + \Bigl\lfloor\dfrac{n}{k^2}\Bigr\rfloor + \ldots + \Bigl\lfloor\dfrac{n}{k^i}\Bigr\rfloor + \ldots$$

Kết quả này còn được gọi là [Công thức Legendre](https://en.wikipedia.org/wiki/Legendre%27s_formula).
Tổng tất nhiên là hữu hạn, vì chỉ có khoảng $\log_k n$ phần tử đầu tiên là khác không. Do đó, thời gian chạy của thuật toán này là $O(\log_k n)$.

### Cài đặt

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

## $k$ là hợp số {data-toc-label="Composite k"}

Ý tưởng tương tự không thể được áp dụng trực tiếp. Thay vào đó, chúng ta có thể phân tích thừa số $k$, biểu diễn nó dưới dạng $k = k_1^{p_1} \cdot \ldots \cdot k_m^{p_m}$. Đối với mỗi $k_i$, chúng ta tìm số lần nó xuất hiện trong $n!$ bằng thuật toán được mô tả ở trên - hãy gọi giá trị này là $a_i$. Câu trả lời cho $k$ là hợp số sẽ là

$$\min_ {i=1 \ldots m} \dfrac{a_i}{p_i}
```