---
tags:
  - Original
---

# Số lượng ước / Tổng các ước (Number of divisors / sum of divisors) {: #number-of-divisors-sum-of-divisors}

Trong bài viết này, chúng ta thảo luận về cách tính số lượng ước $d(n)$ và tổng các ước $\sigma(n)$ của một số $n$ đã cho.

## Số lượng ước (Number of divisors) {: #number-of-divisors}

Rõ ràng rằng phân tích thừa số nguyên tố của một ước $d$ phải là một tập con của phân tích thừa số nguyên tố của $n$, v.d. $6 = 2 \cdot 3$ là một ước của $60 = 2^2 \cdot 3 \cdot 5$.
Vì vậy, chúng ta chỉ cần tìm tất cả các tập con khác nhau của phân tích thừa số nguyên tố của $n$.

Thông thường, số lượng tập con là $2^x$ cho một tập hợp có $x$ phần tử.
Tuy nhiên, điều này không còn đúng nữa nếu có các phần tử lặp lại trong tập hợp. Trong trường hợp của chúng ta, một số thừa số nguyên tố có thể xuất hiện nhiều lần trong phân tích thừa số nguyên tố của $n$.

Nếu một thừa số nguyên tố $p$ xuất hiện $e$ lần trong phân tích thừa số nguyên tố của $n$, thì chúng ta có thể sử dụng thừa số $p$ tối đa $e$ lần trong tập con.
Điều đó có nghĩa là chúng ta có $e+1$ lựa chọn.

Do đó, nếu phân tích thừa số nguyên tố của $n$ là $p_1^{e_1} \cdot p_2^{e_2} \cdots p_k^{e_k}$, trong đó $p_i$ là các số nguyên tố phân biệt, thì số lượng ước là:

$$d(n) = (e_1 + 1) \cdot (e_2 + 1) \cdots (e_k + 1)$$

Một cách suy nghĩ về nó là như sau:

* Nếu chỉ có một ước nguyên tố phân biệt $n = p_1^{e_1}$, thì rõ ràng có $e_1 + 1$ ước ($1, p_1, p_1^2, \dots, p_1^{e_1}$).

* Nếu có hai ước nguyên tố phân biệt $n = p_1^{e_1} \cdot p_2^{e_2}$, thì bạn có thể sắp xếp tất cả các ước dưới dạng bảng.

$$\begin{array}{c|ccccc}
& 1 & p_2 & p_2^2 & \dots & p_2^{e_2} \\\\\hline
1 & 1 & p_2 & p_2^2 & \dots & p_2^{e_2} \\\\
p_1 & p_1 & p_1 \cdot p_2 & p_1 \cdot p_2^2 & \dots & p_1 \cdot p_2^{e_2} \\\\
p_1^2 & p_1^2 & p_1^2 \cdot p_2 & p_1^2 \cdot p_2^2 & \dots & p_1^2 \cdot p_2^{e_2} \\\\
\vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\\\
p_1^{e_1} & p_1^{e_1} & p_1^{e_1} \cdot p_2 & p_1^{e_1} \cdot p_2^2 & \dots & p_1^{e_1} \cdot p_2^{e_2} \\\\
\end{array}$$

Vì vậy, số lượng ước là tầm thường $(e_1 + 1) \cdot (e_2 + 1)$.

* Một lập luận tương tự có thể được đưa ra nếu có nhiều hơn hai thừa số nguyên tố phân biệt.


```cpp
long long numberOfDivisors(long long num) {
    long long total = 1;
    for (int i = 2; (long long)i * i <= num; i++) {
        if (num % i == 0) {
            int e = 0;
            do {
                e++;
                num /= i;
            } while (num % i == 0);
            total *= e + 1;
        }
    }
    if (num > 1) {
        total *= 2;
    }
    return total;
}
```

## Tổng các ước (Sum of divisors) {: #sum-of-divisors}

Chúng ta có thể sử dụng cùng một lập luận của phần trước.

* Nếu chỉ có một ước nguyên tố phân biệt $n = p_1^{e_1}$, thì tổng là:

$$1 + p_1 + p_1^2 + \dots + p_1^{e_1} = \frac{p_1^{e_1 + 1} - 1}{p_1 - 1}$$

* Nếu có hai ước nguyên tố phân biệt $n = p_1^{e_1} \cdot p_2^{e_2}$, thì chúng ta có thể tạo cùng một bảng như trước.
  Sự khác biệt duy nhất là bây giờ chúng ta muốn tính tổng thay vì đếm các phần tử.
  Dễ thấy rằng, tổng của mỗi tổ hợp có thể được biểu diễn như sau:

$$\left(1 + p_1 + p_1^2 + \dots + p_1^{e_1}\right) \cdot \left(1 + p_2 + p_2^2 + \dots + p_2^{e_2}\right)$$

$$ = \frac{p_1^{e_1 + 1} - 1}{p_1 - 1} \cdot \frac{p_2^{e_2 + 1} - 1}{p_2 - 1}$$

* Tổng quát, với $n = p_1^{e_1} \cdot p_2^{e_2} \cdots p_k^{e_k}$ chúng ta nhận được công thức:

$$\sigma(n) = \frac{p_1^{e_1 + 1} - 1}{p_1 - 1} \cdot \frac{p_2^{e_2 + 1} - 1}{p_2 - 1} \cdots \frac{p_k^{e_k + 1} - 1}{p_k - 1}$$

```cpp
long long SumOfDivisors(long long num) {
    long long total = 1;

    for (int i = 2; (long long)i * i <= num; i++) {
        if (num % i == 0) {
            int e = 0;
            do {
                e++;
                num /= i;
            } while (num % i == 0);

            long long sum = 0, pow = 1;
            do {
                sum += pow;
                pow *= i;
            } while (e-- > 0);
            total *= sum;
        }
    }
    if (num > 1) {
        total *= (1 + num);
    }
    return total;
}
```

## Hàm nhân tính (Multiplicative functions) {: #multiplicative-functions}

Một hàm nhân tính là một hàm $f(x)$ thỏa mãn

$$f(a \cdot b) = f(a) \cdot f(b)$$

nếu $a$ và $b$ nguyên tố cùng nhau.

Cả $d(n)$ và $\sigma(n)$ đều là các hàm nhân tính.

Các hàm nhân tính có rất nhiều tính chất thú vị, có thể rất hữu ích trong các bài toán lý thuyết số.
Ví dụ, tích chập Dirichlet của hai hàm nhân tính cũng là một hàm nhân tính.

## Bài tập luyện tập {: #practice-problems}

  - [SPOJ - COMDIV](https://www.spoj.com/problems/COMDIV/)
  - [SPOJ - DIVSUM](https://www.spoj.com/problems/DIVSUM/)
  - [SPOJ - DIVSUM2](https://www.spoj.com/problems/DIVSUM2/)

---

## Checklist

- Original lines: 130
- Translated lines: 130
- Code blocks changed? No
- Inline code changed? No
- Technical terms kept in English? Yes
- Headings anchors preserved/added correctly? Yes
- I confirm no character was omitted: YES
