---
tags:
  - Translated
e_maxx_link: binomial_coeff
---

# Tổ hợp

Tổ hợp chập $k$ của $n$, ký hiệu $\binom n k$, là số cách chọn một tập hợp gồm $k$ phần tử từ $n$ phần tử khác nhau mà không tính đến thứ tự sắp xếp của các phần tử này (tức là số lượng các tập hợp không có thứ tự).

Tổ hợp cũng là các hệ số trong khai triển của $(a + b) ^ n$ (còn gọi là nhị thức Newton):

$$ (a+b)^n = \binom n 0 a^n + \binom n 1 a^{n-1} b + \binom n 2 a^{n-2} b^2 + \cdots + \binom n k a^{n-k} b^k + \cdots + \binom n n b^n $$

Người ta tin rằng công thức này, cũng như tam giác cho phép tính toán hiệu quả các hệ số, đã được Blaise Pascal phát hiện vào thế kỷ 17. Tuy nhiên, nó đã được nhà toán học Trung Quốc Dương Huy, sống ở thế kỷ 13, biết đến. Có lẽ nó đã được phát hiện bởi một học giả người Ba Tư Omar Khayyam. Hơn nữa, nhà toán học Ấn Độ Pingala, sống sớm hơn vào thế kỷ thứ 3 TCN, đã có những kết quả tương tự. Công lao của Newton là ông đã tổng quát hóa công thức này cho các số mũ không phải là số tự nhiên.

## Cách tính

**Công thức giải tích** để tính toán:

$$ \binom n k = \frac {n!} {k!(n-k)!} $$

Công thức này có thể dễ dàng suy ra từ bài toán sắp xếp có thứ tự (số cách chọn $k$ phần tử khác nhau từ $n$ phần tử khác nhau). Đầu tiên, hãy đếm số cách chọn có thứ tự của $k$ phần tử. Có $n$ cách để chọn phần tử đầu tiên, $n-1$ cách để chọn phần tử thứ hai, $n-2$ cách để chọn phần tử thứ ba, v.v. Kết quả là, chúng ta có được công thức về số lượng các cách sắp xếp có thứ tự: $n (n-1) (n-2) \cdots (n - k + 1) = \frac {n!} {(n-k)!}$. Chúng ta có thể dễ dàng chuyển sang các cách sắp xếp không có thứ tự, lưu ý rằng mỗi cách sắp xếp không có thứ tự tương ứng với chính xác $k!$ cách sắp xếp có thứ tự ($k!$ là số hoán vị có thể có của $k$ phần tử). Chúng ta có được công thức cuối cùng bằng cách chia $\frac {n!} {(n-k)!}$ cho $k!$.

**Công thức truy hồi** (liên quan đến "Tam giác Pascal" nổi tiếng):

$$ \binom n k = \binom {n-1} {k-1} + \binom {n-1} k $$

Dễ dàng suy ra điều này bằng cách sử dụng công thức giải tích.

Lưu ý rằng đối với $n \lt k$ giá trị của $\binom n k$ được giả định là không.

## Các tính chất

Tổ hợp có nhiều thuộc tính khác nhau. Dưới đây là những thuộc tính đơn giản nhất:

*   Quy tắc đối xứng:

    \[ \binom n k = \binom n {n-k} \]

*   Phân tích thành nhân tử:

    \[ \binom n k = \frac n k \binom {n-1} {k-1} \]

*   Tổng theo $k$:

    \[ \sum_{k = 0}^n \binom n k = 2 ^ n \]

*   Tổng theo $n$:

    \[ \sum_{m = 0}^n \binom m k = \binom {n + 1} {k + 1} \]

*   Tổng theo $n$ và $k$:

    \[ \sum_{k = 0}^m  \binom {n + k} k = \binom {n + m + 1} m \]

*   Tổng các bình phương:

    \[ {\binom n 0}^2 + {\binom n 1}^2 + \cdots + {\binom n n}^2 = \binom {2n} n \]

*   Tổng có trọng số:

    \[ 1 \binom n 1 + 2 \binom n 2 + \cdots + n \binom n n = n 2^{n-1} \]

*   Kết nối với [số Fibonacci](../algebra/fibonacci-numbers.md):

    \[ \binom n 0 + \binom {n-1} 1 + \cdots + \binom {n-k} k + \cdots + \binom 0 n = F_{n+1} \]

## Tính toán

### Tính toán trực tiếp bằng công thức giải tích

Công thức đầu tiên, đơn giản, rất dễ viết mã, nhưng phương pháp này có khả năng bị tràn số ngay cả với các giá trị tương đối nhỏ của $n$ và $k$ (ngay cả khi câu trả lời hoàn toàn vừa với một kiểu dữ liệu nào đó, việc tính toán các giai thừa trung gian có thể dẫn đến tràn số). Do đó, phương pháp này thường chỉ có thể được sử dụng với [số học số lớn](../algebra/big-integer.md):

```cpp
int C(int n, int k) {
    int res = 1;
    for (int i = n - k + 1; i <= n; ++i)
        res *= i;
    for (int i = 2; i <= k; ++i)
        res /= i;
    return res;
}
```

### Cài đặt cải tiến

Lưu ý rằng trong việc triển khai ở trên, tử số và mẫu số có cùng số lượng thừa số ($k$), mỗi thừa số lớn hơn hoặc bằng 1. Do đó, chúng ta có thể thay thế phân số của mình bằng một tích của $k$ phân số, mỗi phân số là một giá trị thực. Tuy nhiên, ở mỗi bước sau khi nhân câu trả lời hiện tại với mỗi phân số tiếp theo, câu trả lời vẫn sẽ là số nguyên (điều này xuất phát từ thuộc tính phân tích thành nhân tử). 

Cài đặt C++:

```cpp
int C(int n, int k) {
    double res = 1;
    for (int i = 1; i <= k; ++i)
        res = res * (n - k + i) / i;
    return (int)(res + 0.01);
}
```

Ở đây, chúng ta cẩn thận ép kiểu số dấu phẩy động thành một số nguyên, có tính đến việc do các lỗi tích lũy, nó có thể nhỏ hơn một chút so với giá trị thực (ví dụ, $2.99999$ thay vì $3$).

### Tam giác Pascal

Bằng cách sử dụng quan hệ truy hồi, chúng ta có thể xây dựng một bảng các hệ số nhị thức (tam giác Pascal) và lấy kết quả từ đó. Ưu điểm của phương pháp này là các kết quả trung gian không bao giờ vượt quá câu trả lời và việc tính toán mỗi phần tử bảng mới chỉ cần một phép cộng. Nhược điểm là thực thi chậm đối với $n$ và $k$ lớn nếu bạn chỉ cần một giá trị duy nhất chứ không phải toàn bộ bảng (bởi vì để tính $\binom n k$, bạn sẽ cần xây dựng một bảng gồm tất cả các $\binom i j, 1 \le i \le n, 1 \le j \le n$, hoặc ít nhất là đến $1 \le j \le \min (i, 2k)$). Độ phức tạp thời gian có thể được coi là $\mathcal{O}(n^2)$.

Cài đặt C++:

```cpp
const int maxn = ...;
int C[maxn + 1][maxn + 1];
C[0][0] = 1;
for (int n = 1; n <= maxn; ++n) {
    C[n][0] = C[n][n] = 1;
    for (int k = 1; k < n; ++k)
        C[n][k] = C[n - 1][k - 1] + C[n - 1][k];
}
```

Nếu không cần toàn bộ bảng giá trị, chỉ cần lưu trữ hai hàng cuối cùng của nó là đủ (hàng thứ $n$ hiện tại và hàng thứ $n-1$ trước đó).

### Tính toán trong $O(1)$ {data-toc-label="Calculation in O(1)"}

Cuối cùng, trong một số tình huống, việc tính trước tất cả các giai thừa là có lợi để tạo ra bất kỳ hệ số nhị thức cần thiết nào chỉ với hai phép chia sau đó. Điều này có thể có lợi khi sử dụng [số học số lớn](../algebra/big-integer.md), khi bộ nhớ không cho phép tính trước toàn bộ tam giác Pascal.


## Tính tổ hợp modulo $m$ {data-toc-label="Computing binomial coefficients modulo m"}

Khá thường xuyên bạn gặp phải vấn đề tính toán các hệ số nhị thức modulo một số $m$.

### Tổ hợp cho $n$ nhỏ {data-toc-label="Binomial coefficient for small n"}

Cách tiếp cận tam giác Pascal đã được thảo luận trước đây có thể được sử dụng để tính tất cả các giá trị của $\binom{n}{k} \bmod m$ đối với $n$ đủ nhỏ, vì nó đòi hỏi độ phức tạp thời gian $\mathcal{O}(n^2)$. Cách tiếp cận này có thể xử lý bất kỳ modulo nào, vì chỉ sử dụng các phép toán cộng.


### Tổ hợp modulo số nguyên tố lớn

Công thức cho tổ hợp là

$$\binom n k = \frac {n!} {k!(n-k)!},$$

vì vậy nếu chúng ta muốn tính nó modulo một số nguyên tố $m > n$, chúng ta có

$$\binom n k \equiv n! \cdot (k!)^{-1} \cdot ((n-k)!)^{-1} \mod m.$$

Trước tiên, chúng ta tính trước tất cả các giai thừa modulo $m$ cho đến $\text{MAXN}!$ trong thời gian $O(\text{MAXN})$.

```cpp
factorial[0] = 1;
for (int i = 1; i <= MAXN; i++) {
    factorial[i] = factorial[i - 1] * i % m;
}
```

Và sau đó chúng ta có thể tính toán tổ hợp trong thời gian $O(\log m)$.

```cpp
long long binomial_coefficient(int n, int k) {
    return factorial[n] * inverse(factorial[k] * factorial[n - k] % m) % m;
}
```

Chúng ta thậm chí có thể tính toán tổ hợp trong thời gian $O(1)$ nếu chúng ta tính trước nghịch đảo của tất cả các giai thừa trong $O(\text{MAXN} \log m)$ bằng phương pháp thông thường để tính nghịch đảo, hoặc thậm chí trong $O(\text{MAXN})$ thời gian bằng cách sử dụng đồng dư thức $(x!)^{-1} \equiv ((x-1)!)^{-1} \cdot x^{-1}$ và phương pháp để [tính tất cả các nghịch đảo](../algebra/module-inverse.md#mod-inv-all-num) trong $O(n)$.

```cpp
long long binomial_coefficient(int n, int k) {
    return factorial[n] * inverse_factorial[k] % m * inverse_factorial[n - k] % m;
}
```

### Tổ hợp modulo lũy thừa của số nguyên tố  { #mod-prime-pow}

Ở đây chúng ta muốn tính tổ hợp modulo một lũy thừa của số nguyên tố nào đó, tức là $m = p^b$ với $p$ là một số nguyên tố.
Nếu $p > \max(k, n-k)$, thì chúng ta có thể sử dụng cùng một phương pháp như đã mô tả trong phần trước.
Nhưng nếu $p \le \max(k, n-k)$, thì ít nhất một trong $k!$ và $(n-k)!$ không nguyên tố cùng nhau với $m$, và do đó chúng ta không thể tính nghịch đảo - chúng không tồn tại.
Tuy nhiên, chúng ta vẫn có thể tính toán tổ hợp.

Ý tưởng là như sau:
Chúng ta tính cho mỗi $x!$ số mũ lớn nhất $c$ sao cho $p^c$ chia hết cho $x!$, tức là $p^c ~|~ x!$.
Đặt $c(x)$ là số đó.
Và đặt $g(x) := \frac{x!}{p^{c(x)}}$.
Sau đó, chúng ta có thể viết tổ hợp như sau:

$$\binom n k = \frac {g(n) p^{c(n)}} {g(k) p^{c(k)} g(n-k) p^{c(n-k)}} = \frac {g(n)} {g(k) g(n-k)}p^{c(n) - c(k) - c(n-k)}$$

Điều thú vị là, $g(x)$ bây giờ không còn thừa số nguyên tố $p$.
Do đó, $g(x)$ nguyên tố cùng nhau với m, và chúng ta có thể tính nghịch đảo modular của $g(k)$ và $g(n-k)$.

Sau khi tính trước tất cả các giá trị cho $g$ và $c$, có thể được thực hiện hiệu quả bằng quy hoạch động trong $\mathcal{O}(n)$, chúng ta có thể tính tổ hợp trong thời gian $O(\log m)$.
Hoặc tính trước tất cả các nghịch đảo và tất cả các lũy thừa của $p$, và sau đó tính tổ hợp trong $O(1)$.

Lưu ý, nếu $c(n) - c(k) - c(n-k) \ge b$, thì $p^b ~|~ p^{c(n) - c(k) - c(n-k)}$, và tổ hợp là $0$.

### Tổ hợp modulo một số bất kỳ

Bây giờ chúng ta tính tổ hợp modulo một modulus $m$ bất kỳ.

Đặt phân tích thừa số nguyên tố của $m$ là $m = p_1^{e_1} p_2^{e_2} \cdots p_h^{e_h}$.
Chúng ta có thể tính tổ hợp modulo $p_i^{e_i}$ cho mọi $i$.
Điều này cho chúng ta $h$ đồng dư khác nhau.
Vì tất cả các moduli $p_i^{e_i}$ đều nguyên tố cùng nhau, chúng ta có thể áp dụng [Định lý phần dư Trung Hoa](../algebra/chinese-remainder-theorem.md) để tính tổ hợp modulo tích của các moduli, đó là tổ hợp mong muốn modulo $m$.

### Tổ hợp cho $n$ lớn và modulo nhỏ {data-toc-label="Binomial coefficient for large n and small modulo"}

Khi $n$ quá lớn, các thuật toán $\mathcal{O}(n)$ đã thảo luận ở trên trở nên không thực tế. Tuy nhiên, nếu modulo $m$ nhỏ, vẫn có những cách để tính $\binom{n}{k} \bmod m$.

Khi modulo $m$ là số nguyên tố, có 2 lựa chọn:

* [Định lý Lucas](https://en.wikipedia.org/wiki/Lucas's_theorem) có thể được áp dụng, nó chia bài toán tính $\binom{n}{k} \bmod m$ thành $\log_m n$ bài toán có dạng $\binom{x_i}{y_i} \bmod m$ trong đó $x_i, y_i < m$.  Nếu mỗi hệ số rút gọn được tính bằng cách sử dụng các giai thừa và giai thừa nghịch đảo được tính trước, độ phức tạp là $\mathcal{O}(m + \log_m n)$.
* Phương pháp tính [giai thừa modulo P](../algebra/factorial-modulo.md) có thể được sử dụng để lấy các giá trị $g$ và $c$ cần thiết và sử dụng chúng như được mô tả trong phần [modulo lũy thừa của số nguyên tố](#mod-prime-pow). Điều này mất $\mathcal{O}(m \log_m n)$.

Khi $m$ không phải là số nguyên tố nhưng không có thừa số chính phương, các thừa số nguyên tố của $m$ có thể được lấy và hệ số modulo mỗi thừa số nguyên tố có thể được tính bằng một trong hai phương pháp trên, và câu trả lời tổng thể có thể được lấy bằng Định lý phần dư Trung Hoa.

Khi $m$ không phải là không có thừa số chính phương, một [tổng quát hóa của định lý Lucas cho các lũy thừa của số nguyên tố](https://web.archive.org/web/20170202003812/http://www.dms.umontreal.ca/~andrew/PDF/BinCoeff.pdf) có thể được áp dụng thay vì định lý Lucas.


## Bài tập luyện tập
* [Codechef - Number of ways](https://www.codechef.com/LTIME24/problems/NWAYS/)
* [Codeforces - Curious Array](http://codeforces.com/problemset/problem/407/C)
* [LightOj - Necklaces](http://www.lightoj.com/volume_showproblem.php?problem=1419)
* [HACKEREARTH: Binomial Coefficient](https://www.hackerearth.com/problem/algorithm/binomial-coefficient-1/description/)
* [SPOJ - Ada and Teams](http://www.spoj.com/problems/ADATEAMS/)
* [SPOJ - Greedy Walking](http://www.spoj.com/problems/UCV2013E/)
* [UVa 13214 - The Robot's Grid](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=5137)
* [SPOJ - Good Predictions](http://www.spoj.com/problems/GOODB/)
* [SPOJ - Card Game](http://www.spoj.com/problems/HC12/)
* [SPOJ - Topper Rama Rao](http://www.spoj.com/problems/HLP_RAMS/)
* [UVa 13184 - Counting Edges and Graphs](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=5095)
* [Codeforces - Anton and School 2](http://codeforces.com/contest/785/problem/D)
* [Codeforces - Bacterial Melee](http://codeforces.com/contest/760/problem/F)
* [Codeforces - Points, Lines and Ready-made Titles](http://codeforces.com/contest/872/problem/E)
* [SPOJ - The Ultimate Riddle](https://www.spoj.com/problems/DCEPC13D/)
* [CodeChef - Long Sandwich](https://www.codechef.com/MAY17/problems/SANDWICH/)
* [Codeforces - Placing Jinas](https://codeforces.com/problemset/problem/1696/E)

## Tài liệu tham khảo
* [Blog fishi.devtail.io](https://fishi.devtail.io/weblog/2015/06/25/computing-large-binomial-coefficients-modulo-prime-non-prime/)
* [Câu hỏi trên Mathematics StackExchange](https://math.stackexchange.com/questions/95491/n-choose-k-bmod-m-using-chinese-remainder-theorem)
* [Câu hỏi trên CodeChef Discuss](https://discuss.codechef.com/questions/98129/your-approach-to-solve-sandwich)