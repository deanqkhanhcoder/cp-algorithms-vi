---
tags:
  - Translated
e_maxx_link: binomial_coeff
---

# Hệ số nhị thức (Binomial Coefficients) {: #binomial-coefficients}

Hệ số nhị thức $\binom n k$ là số cách để chọn một tập hợp $k$ phần tử từ $n$ phần tử khác nhau mà không tính đến thứ tự sắp xếp của các phần tử này (tức là, số lượng tập hợp không có thứ tự).

Hệ số nhị thức cũng là các hệ số trong khai triển của $(a + b) ^ n$ (còn gọi là định lý nhị thức):

$$ (a+b)^n = \binom n 0 a^n + \binom n 1 a^{n-1} b + \binom n 2 a^{n-2} b^2 + \cdots + \binom n k a^{n-k} b^k + \cdots + \binom n n b^n $$

Người ta tin rằng công thức này, cũng như tam giác cho phép tính toán hiệu quả các hệ số, được phát hiện bởi Blaise Pascal vào thế kỷ 17. Tuy nhiên, nó đã được nhà toán học Trung Quốc Yang Hui, sống vào thế kỷ 13, biết đến. Có lẽ nó được phát hiện bởi một học giả Ba Tư Omar Khayyam. Hơn nữa, nhà toán học Ấn Độ Pingala, sống sớm hơn vào thế kỷ thứ 3 trước Công nguyên, đã có kết quả tương tự. Công lao của Newton là ông đã tổng quát hóa công thức này cho các số mũ không phải là số tự nhiên.

## Tính toán (Calculation) {: #calculation}

**Công thức giải tích** để tính toán:

$$ \binom n k = \frac {n!} {k!(n-k)!} $$

Công thức này có thể dễ dàng suy ra từ bài toán sắp xếp có thứ tự (số cách chọn $k$ phần tử khác nhau từ $n$ phần tử khác nhau). Đầu tiên, hãy đếm số lượng lựa chọn có thứ tự của $k$ phần tử. Có $n$ cách chọn phần tử đầu tiên, $n-1$ cách chọn phần tử thứ hai, $n-2$ cách chọn phần tử thứ ba, v.v. Kết quả là, chúng ta có công thức số lượng sắp xếp có thứ tự: $n (n-1) (n-2) \cdots (n - k + 1) = \frac {n!} {(n-k)!}$. Chúng ta có thể dễ dàng chuyển sang sắp xếp không thứ tự, lưu ý rằng mỗi sắp xếp không thứ tự tương ứng với chính xác $k!$ sắp xếp có thứ tự ($k!$ là số lượng hoán vị có thể có của $k$ phần tử). Chúng ta nhận được công thức cuối cùng bằng cách chia $\frac {n!} {(n-k)!}$ cho $k!$.

**Công thức truy hồi** (liên quan đến "Tam giác Pascal" nổi tiếng):

$$ \binom n k = \binom {n-1} {k-1} + \binom {n-1} k $$

Rất dễ để suy ra điều này bằng cách sử dụng công thức giải tích.

Lưu ý rằng đối với $n \lt k$ giá trị của $\binom n k$ được giả định là bằng không.

## Các tính chất (Properties) {: #properties}

Hệ số nhị thức có nhiều tính chất khác nhau. Dưới đây là những tính chất đơn giản nhất:

*   Quy tắc đối xứng:

    \[ \binom n k = \binom n {n-k} \]

*   Đưa ra ngoài (Factoring in):

    \[ \binom n k = \frac n k \binom {n-1} {k-1} \]

*   Tổng theo $k$:

    \[ \sum_{k = 0}^n \binom n k = 2 ^ n \]

*   Tổng theo $n$:

    \[ \sum_{m = 0}^n \binom m k = \binom {n + 1} {k + 1} \]

*   Tổng theo $n$ và $k$:

    \[ \sum_{k = 0}^m  \binom {n + k} k = \binom {n + m + 1} m \]

*   Tổng bình phương:

    \[ {\binom n 0}^2 + {\binom n 1}^2 + \cdots + {\binom n n}^2 = \binom {2n} n \]

*   Tổng có trọng số:

    \[ 1 \binom n 1 + 2 \binom n 2 + \cdots + n \binom n n = n 2^{n-1} \]

*   Liên hệ với [số Fibonacci](../algebra/fibonacci-numbers.md):

    \[ \binom n 0 + \binom {n-1} 1 + \cdots + \binom {n-k} k + \cdots + \binom 0 n = F_{n+1} \]

## Tính toán (Calculation) {: #calculation-1}

### Tính toán trực tiếp bằng công thức giải tích (Straightforward calculation using analytical formula) {: #straightforward-calculation-using-analytical-formula}

Công thức đầu tiên, trực tiếp rất dễ viết mã, nhưng phương pháp này có khả năng bị tràn số ngay cả đối với các giá trị tương đối nhỏ của $n$ và $k$ (ngay cả khi kết quả hoàn toàn phù hợp với một kiểu dữ liệu nào đó, việc tính toán các giai thừa trung gian có thể dẫn đến tràn số). Do đó, phương pháp này thường chỉ có thể được sử dụng với [số học lớn](../algebra/big-integer.md):

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

### Cài đặt cải tiến (Improved implementation) {: #improved-implementation}

Lưu ý rằng trong cài đặt trên tử số và mẫu số có cùng số lượng thừa số ($k$), mỗi thừa số lớn hơn hoặc bằng 1. Do đó, chúng ta có thể thay thế phân số của mình bằng tích $k$ phân số, mỗi phân số có giá trị thực. Tuy nhiên, ở mỗi bước sau khi nhân câu trả lời hiện tại với mỗi phân số tiếp theo, câu trả lời vẫn sẽ là số nguyên (điều này theo sau từ tính chất đưa ra ngoài).

Cài đặt C++:

```cpp
int C(int n, int k) {
    double res = 1;
    for (int i = 1; i <= k; ++i)
        res = res * (n - k + i) / i;
    return (int)(res + 0.01);
}
```

Ở đây chúng tôi cẩn thận ép kiểu số dấu phẩy động thành số nguyên, có tính đến việc do sai số tích lũy, nó có thể nhỏ hơn một chút so với giá trị thực (ví dụ: $2.99999$ thay vì $3$).

### Tam giác Pascal (Pascal's Triangle) {: #pascals-triangle}

Bằng cách sử dụng hệ thức truy hồi, chúng ta có thể xây dựng bảng các hệ số nhị thức (tam giác Pascal) và lấy kết quả từ đó. Ưu điểm của phương pháp này là kết quả trung gian không bao giờ vượt quá câu trả lời và tính toán mỗi phần tử bảng mới chỉ yêu cầu một phép cộng. Nhược điểm là thực thi chậm đối với $n$ và $k$ lớn nếu bạn chỉ cần một giá trị duy nhất chứ không phải toàn bộ bảng (bởi vì để tính $\binom n k$ bạn sẽ cần xây dựng bảng của tất cả $\binom i j, 1 \le i \le n, 1 \le j \le n$, hoặc ít nhất là đến $1 \le j \le \min (i, 2k)$). Độ phức tạp thời gian có thể được coi là $\mathcal{O}(n^2)$.

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

Nếu toàn bộ bảng giá trị không cần thiết, chỉ lưu trữ hai hàng cuối cùng của nó là đủ (hàng thứ $n$ hiện tại và hàng thứ $n-1$ trước đó).

### Tính toán trong $O(1)$ (Calculation in $O(1)$) {: #calculation-in-o1 data-toc-label="Calculation in O(1)"}

Cuối cùng, trong một số tình huống, có lợi khi tính trước tất cả các giai thừa để tạo ra bất kỳ hệ số nhị thức cần thiết nào chỉ với hai phép chia sau đó. Điều này có thể có lợi khi sử dụng [số học lớn](../algebra/big-integer.md), khi bộ nhớ không cho phép tính trước toàn bộ tam giác Pascal.

## Tính hệ số nhị thức modulo $m$ (Computing binomial coefficients modulo $m$) {: #computing-binomial-coefficients-modulo-m data-toc-label="Computing binomial coefficients modulo m"}

Khá thường xuyên bạn gặp bài toán tính hệ số nhị thức modulo một số $m$ nào đó.

### Hệ số nhị thức cho $n$ nhỏ (Binomial coefficient for small $n$) {: #binomial-coefficient-for-small-n data-toc-label="Binomial coefficient for small n"}

Cách tiếp cận tam giác Pascal đã thảo luận trước đó có thể được sử dụng để tính tất cả các giá trị của $\binom{n}{k} \bmod m$ cho $n$ khá nhỏ, vì nó yêu cầu độ phức tạp thời gian $\mathcal{O}(n^2)$. Cách tiếp cận này có thể xử lý bất kỳ modulo nào, vì chỉ các phép toán cộng được sử dụng.

### Hệ số nhị thức modulo số nguyên tố lớn (Binomial coefficient modulo large prime) {: #binomial-coefficient-modulo-large-prime}

Công thức cho các hệ số nhị thức là

$$\binom n k = \frac {n!} {k!(n-k)!},$$

vì vậy nếu chúng ta muốn tính nó modulo một số nguyên tố $m > n$ nào đó, chúng ta nhận được

$$\binom n k \equiv n! \cdot (k!)^{-1} \cdot ((n-k)!)^{-1} \mod m.$$

Đầu tiên chúng ta tính trước tất cả các giai thừa modulo $m$ lên đến $\text{MAXN}!$ trong thời gian $O(\text{MAXN})$.

```cpp
factorial[0] = 1;
for (int i = 1; i <= MAXN; i++) {
    factorial[i] = factorial[i - 1] * i % m;
}
```

Và sau đó chúng ta có thể tính hệ số nhị thức trong thời gian $O(\log m)$.

```cpp
long long binomial_coefficient(int n, int k) {
    return factorial[n] * inverse(factorial[k] * factorial[n - k] % m) % m;
}
```

Chúng ta thậm chí có thể tính hệ số nhị thức trong thời gian $O(1)$ nếu chúng ta tính trước nghịch đảo của tất cả các giai thừa trong $O(\text{MAXN} \log m)$ bằng phương pháp thông thường để tính nghịch đảo, hoặc thậm chí trong thời gian $O(\text{MAXN})$ bằng cách sử dụng đồng dư $(x!)^{-1} \equiv ((x-1)!)^{-1} \cdot x^{-1}$ và phương pháp để [tính tất cả nghịch đảo](../algebra/module-inverse.md#mod-inv-all-num) trong $O(n)$.

```cpp
long long binomial_coefficient(int n, int k) {
    return factorial[n] * inverse_factorial[k] % m * inverse_factorial[n - k] % m;
}
```

### Hệ số nhị thức modulo lũy thừa số nguyên tố (Binomial coefficient modulo prime power) {: #mod-prime-pow}

Ở đây chúng ta muốn tính hệ số nhị thức modulo một lũy thừa số nguyên tố nào đó, tức là $m = p^b$ cho một số nguyên tố $p$ nào đó.
Nếu $p > \max(k, n-k)$, thì chúng ta có thể sử dụng cùng một phương pháp như được mô tả trong phần trước.
Nhưng nếu $p \le \max(k, n-k)$, thì ít nhất một trong $k!$ và $(n-k)!$ không nguyên tố cùng nhau với $m$, và do đó chúng ta không thể tính nghịch đảo - chúng không tồn tại.
Tuy nhiên chúng ta có thể tính hệ số nhị thức.

Ý tưởng là như sau:
Chúng ta tính cho mỗi $x!$ số mũ lớn nhất $c$ sao cho $p^c$ chia hết $x!$, tức là $p^c ~|~ x!$.
Gọi $c(x)$ là số đó.
Và gọi $g(x) := \frac{x!}{p^{c(x)}}$.
Khi đó chúng ta có thể viết hệ số nhị thức như sau:

$$\binom n k = \frac {g(n) p^{c(n)}} {g(k) p^{c(k)} g(n-k) p^{c(n-k)}} = \frac {g(n)} {g(k) g(n-k)}p^{c(n) - c(k) - c(n-k)}$$

Điều thú vị là, $g(x)$ bây giờ không còn chứa ước số nguyên tố $p$.
Do đó $g(x)$ nguyên tố cùng nhau với m, và chúng ta có thể tính nghịch đảo modulo của $g(k)$ và $g(n-k)$.

Sau khi tính trước tất cả các giá trị cho $g$ và $c$, có thể được thực hiện hiệu quả bằng quy hoạch động trong $\mathcal{O}(n)$, chúng ta có thể tính hệ số nhị thức trong thời gian $O(\log m)$.
Hoặc tính trước tất cả nghịch đảo và tất cả các lũy thừa của $p$, và sau đó tính hệ số nhị thức trong $O(1)$.

Lưu ý, nếu $c(n) - c(k) - c(n-k) \ge b$, thì $p^b ~|~ p^{c(n) - c(k) - c(n-k)}$, và hệ số nhị thức là $0$.

### Hệ số nhị thức modulo một số tùy ý (Binomial coefficient modulo an arbitrary number) {: #binomial-coefficient-modulo-an-arbitrary-number}

Bây giờ chúng ta tính hệ số nhị thức modulo một số tùy ý $m$.

Gọi phân tích thừa số nguyên tố của $m$ là $m = p_1^{e_1} p_2^{e_2} \cdots p_h^{e_h}$.
Chúng ta có thể tính hệ số nhị thức modulo $p_i^{e_i}$ cho mỗi $i$.
Điều này cho chúng ta $h$ đồng dư khác nhau.
Vì tất cả các modulo $p_i^{e_i}$ là nguyên tố cùng nhau, chúng ta có thể áp dụng [Định lý thặng dư Trung Hoa](../algebra/chinese-remainder-theorem.md) để tính hệ số nhị thức modulo tích của các modulo, đó là hệ số nhị thức mong muốn modulo $m$.

### Hệ số nhị thức cho $n$ lớn và modulo nhỏ (Binomial coefficient for large $n$ and small modulo) {: #binomial-coefficient-for-large-n-and-small-modulo data-toc-label="Binomial coefficient for large n and small modulo"}

Khi $n$ quá lớn, các thuật toán $\mathcal{O}(n)$ được thảo luận ở trên trở nên không thực tế. Tuy nhiên, nếu modulo $m$ nhỏ vẫn có những cách để tính $\binom{n}{k} \bmod m$.

Khi modulo $m$ là số nguyên tố, có 2 tùy chọn:

* [Định lý Lucas](https://en.wikipedia.org/wiki/Lucas's_theorem) có thể được áp dụng để chia bài toán tính $\binom{n}{k} \bmod m$ thành $\log_m n$ bài toán có dạng $\binom{x_i}{y_i} \bmod m$ trong đó $x_i, y_i < m$. Nếu mỗi hệ số rút gọn được tính bằng cách sử dụng giai thừa và nghịch đảo giai thừa tính trước, độ phức tạp là $\mathcal{O}(m + \log_m n)$.
* Phương pháp tính [giai thừa modulo P](../algebra/factorial-modulo.md) có thể được sử dụng để lấy các giá trị $g$ và $c$ cần thiết và sử dụng chúng như được mô tả trong phần [modulo lũy thừa số nguyên tố](#mod-prime-pow). Điều này mất $\mathcal{O}(m \log_m n)$.

Khi $m$ không phải là số nguyên tố nhưng không chứa thừa số chính phương (square-free), các thừa số nguyên tố của $m$ có thể thu được và hệ số modulo mỗi thừa số nguyên tố có thể được tính bằng cách sử dụng một trong các phương pháp trên, và câu trả lời tổng thể có thể thu được bằng Định lý thặng dư Trung Hoa.

Khi $m$ không phải là square-free, một [tổng quát hóa của định lý Lucas cho lũy thừa số nguyên tố](https://web.archive.org/web/20170202003812/http://www.dms.umontreal.ca/~andrew/PDF/BinCoeff.pdf) có thể được áp dụng thay vì định lý Lucas.

## Bài tập luyện tập {: #practice-problems}
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

## Tài liệu tham khảo {: #references}
* [Blog fishi.devtail.io](https://fishi.devtail.io/weblog/2015/06/25/computing-large-binomial-coefficients-modulo-prime-non-prime/)
* [Câu hỏi trên Mathematics StackExchange](https://math.stackexchange.com/questions/95491/n-choose-k-bmod-m-using-chinese-remainder-theorem)
* [Câu hỏi trên CodeChef Discuss](https://discuss.codechef.com/questions/98129/your-approach-to-solve-sandwich)
