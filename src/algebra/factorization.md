---
tags:
  - Original
---

# Phân tích ra thừa số nguyên (Integer factorization) {: #integer-factorization}

Trong bài viết này, chúng tôi liệt kê một số thuật toán để phân tích các số nguyên ra thừa số, mỗi thuật toán có thể nhanh hoặc chậm tùy thuộc vào đầu vào của chúng.

Lưu ý, nếu số mà bạn muốn phân tích thực sự là một số nguyên tố, hầu hết các thuật toán sẽ chạy rất chậm. Điều này đặc biệt đúng đối với các thuật toán phân tích thừa số Fermat, Pollard's p-1 và Pollard's rho.
Do đó, việc thực hiện một [kiểm tra số nguyên tố](primality_tests.md) xác suất (hoặc tất định nhanh) trước khi cố gắng phân tích số đó là hợp lý nhất.

## Chia thử (Trial division) {: #trial-division}

Đây là thuật toán cơ bản nhất để tìm phân tích thừa số nguyên tố.

Chúng ta chia cho từng ước số có thể $d$.
Có thể nhận thấy rằng không thể có tất cả các thừa số nguyên tố của một hợp số $n$ lớn hơn $\sqrt{n}$.
Do đó, chúng ta chỉ cần kiểm tra các ước số $2 \le d \le \sqrt{n}$, điều này cho chúng ta phân tích thừa số nguyên tố trong $O(\sqrt{n})$.
(Đây là [thời gian giả đa thức](https://en.wikipedia.org/wiki/Pseudo-polynomial_time), tức là đa thức theo giá trị của đầu vào nhưng mũ theo số lượng bit của đầu vào.)

Ước số nhỏ nhất phải là một số nguyên tố.
Chúng ta loại bỏ số đã phân tích, và tiếp tục quá trình.
Nếu chúng ta không thể tìm thấy bất kỳ ước số nào trong khoảng $[2; \sqrt{n}]$, thì chính số đó phải là số nguyên tố.

```{.cpp file=factorization_trial_division1}
vector<long long> trial_division1(long long n) {
    vector<long long> factorization;
    for (long long d = 2; d * d <= n; d++) {
        while (n % d == 0) {
            factorization.push_back(d);
            n /= d;
        }
    }
    if (n > 1)
        factorization.push_back(n);
    return factorization;
}
```

### Phân tích thừa số bằng bánh xe (Wheel factorization) {: #wheel-factorization}

Đây là một sự tối ưu hóa của chia thử.
Khi chúng ta biết rằng số không chia hết cho 2, chúng ta không cần kiểm tra các số chẵn khác.
Điều này để lại cho chúng ta chỉ $50\%$ số lượng số cần kiểm tra.
Sau khi loại bỏ thừa số 2, và nhận được một số lẻ, chúng ta có thể chỉ cần bắt đầu với 3 và chỉ đếm các số lẻ khác.

```{.cpp file=factorization_trial_division2}
vector<long long> trial_division2(long long n) {
    vector<long long> factorization;
    while (n % 2 == 0) {
        factorization.push_back(2);
        n /= 2;
    }
    for (long long d = 3; d * d <= n; d += 2) {
        while (n % d == 0) {
            factorization.push_back(d);
            n /= d;
        }
    }
    if (n > 1)
        factorization.push_back(n);
    return factorization;
}
```

Phương pháp này có thể được mở rộng hơn nữa.
Nếu số không chia hết cho 3, chúng ta cũng có thể bỏ qua tất cả các bội số khác của 3 trong các tính toán trong tương lai.
Vì vậy chúng ta chỉ cần kiểm tra các số $5, 7, 11, 13, 17, 19, 23, \dots$.
Chúng ta có thể quan sát một mẫu của các số còn lại này.
Chúng ta cần kiểm tra tất cả các số có $d \bmod 6 = 1$ và $d \bmod 6 = 5$.
Vì vậy điều này để lại cho chúng ta chỉ $33.3\%$ phần trăm số lượng số cần kiểm tra.
Chúng ta có thể cài đặt điều này bằng cách loại bỏ các thừa số nguyên tố 2 và 3 trước, sau đó chúng ta bắt đầu với 5 và chỉ đếm các số dư $1$ và $5$ modulo $6$.

Dưới đây là một cài đặt cho các số nguyên tố 2, 3 và 5.
Thuận tiện khi lưu trữ các bước nhảy trong một mảng.

```{.cpp file=factorization_trial_division3}
vector<long long> trial_division3(long long n) {
    vector<long long> factorization;
    for (int d : {2, 3, 5}) {
        while (n % d == 0) {
            factorization.push_back(d);
            n /= d;
        }
    }
    static array<int, 8> increments = {4, 2, 4, 2, 4, 6, 2, 6};
    int i = 0;
    for (long long d = 7; d * d <= n; d += increments[i++]) {
        while (n % d == 0) {
            factorization.push_back(d);
            n /= d;
        }
        if (i == 8)
            i = 0;
    }
    if (n > 1)
        factorization.push_back(n);
    return factorization;
}
```

Nếu chúng ta tiếp tục mở rộng phương pháp này để bao gồm nhiều số nguyên tố hơn nữa, tỷ lệ phần trăm tốt hơn có thể đạt được, nhưng danh sách bỏ qua sẽ trở nên lớn hơn.

### Các số nguyên tố tính trước (Precomputed primes) {: #precomputed-primes}

Mở rộng phương pháp phân tích thừa số bằng bánh xe vô thời hạn, chúng ta sẽ chỉ còn lại các số nguyên tố cần kiểm tra. 
Một cách tốt để kiểm tra điều này là tính trước tất cả các số nguyên tố bằng [Sàng Eratosthenes](sieve-of-eratosthenes.md) cho đến $\sqrt{n}$, và kiểm tra chúng một cách riêng lẻ.

```{.cpp file=factorization_trial_division4}
vector<long long> primes;

vector<long long> trial_division4(long long n) {
    vector<long long> factorization;
    for (long long d : primes) {
        if (d * d > n)
            break;
        while (n % d == 0) {
            factorization.push_back(d);
            n /= d;
        }
    }
    if (n > 1)
        factorization.push_back(n);
    return factorization;
}
```

## Phương pháp phân tích thừa số Fermat (Fermat's factorization method) {: #fermats-factorization-method}

Chúng ta có thể viết một hợp số lẻ $n = p \cdot q$ dưới dạng hiệu của hai bình phương $n = a^2 - b^2$:

$$n = \left(\frac{p + q}{2}\right)^2 - \left(\frac{p - q}{2}\right)^2$$

Phương pháp phân tích thừa số Fermat cố gắng khai thác thực tế này bằng cách đoán bình phương đầu tiên $a^2$, và kiểm tra xem phần còn lại, $b^2 = a^2 - n$, có phải là một số chính phương hay không.
Nếu đúng, thì chúng ta đã tìm thấy các thừa số $a - b$ và $a + b$ của $n$.

```cpp
int fermat(int n) {
    int a = ceil(sqrt(n));
    int b2 = a*a - n;
    int b = round(sqrt(b2));
    while (b * b != b2) {
        a = a + 1;
        b2 = a*a - n;
        b = round(sqrt(b2));
    }
    return a - b;
}
```

Phương pháp phân tích thừa số này có thể rất nhanh nếu sự khác biệt giữa hai thừa số $p$ và $q$ nhỏ.
Thuật toán chạy trong thời gian $O(|p - q|)$.
Tuy nhiên trong thực tế, phương pháp này hiếm khi được sử dụng. Một khi các thừa số trở nên xa nhau hơn, nó cực kỳ chậm.

Tuy nhiên, vẫn có một số lượng lớn các tùy chọn tối ưu hóa liên quan đến phương pháp này.
Bằng cách xem xét các bình phương $a^2$ modulo một số nhỏ cố định, có thể quan sát thấy rằng một số giá trị $a$ nhất định không cần phải xem, vì chúng không thể tạo ra một số chính phương $a^2 - n$.


## Phương pháp Pollard's $p - 1$ (Pollard's $p - 1$ method) {: #pollards-p-1-method data-toc-label="Pollard's <script type='math/tex'>p - 1</script> method"}

Rất có khả năng một số $n$ có ít nhất một thừa số nguyên tố $p$ sao cho $p - 1$ là $\mathrm{B}$**-lũy thừa trơn** (powersmooth) với $\mathrm{B}$ nhỏ. Một số nguyên $m$ được gọi là $\mathrm{B}$-lũy thừa trơn nếu mọi lũy thừa nguyên tố chia hết $m$ đều tối đa là $\mathrm{B}$. Một cách hình thức, cho $\mathrm{B} \geqslant 1$ và cho $m$ là bất kỳ số nguyên dương nào. Giả sử phân tích thừa số nguyên tố của $m$ là $m = \prod {q_i}^{e_i}$, trong đó mỗi $q_i$ là một số nguyên tố và $e_i \geqslant 1$. Khi đó $m$ là $\mathrm{B}$-lũy thừa trơn nếu, với mọi $i$, ${q_i}^{e_i} \leqslant \mathrm{B}$. 
V.d. phân tích thừa số nguyên tố của $4817191$ là $1303 \cdot 3697$.
Và các giá trị, $1303 - 1$ và $3697 - 1$, lần lượt là $31$-lũy thừa trơn và $16$-lũy thừa trơn, vì $1303 - 1 = 2 \cdot 3 \cdot 7 \cdot 31$ và $3697 - 1 = 2^4 \cdot 3 \cdot 7 \cdot 11$.
Năm 1974 John Pollard đã phát minh ra một phương pháp để trích xuất các thừa số $p$, sao cho $p-1$ là $\mathrm{B}$-lũy thừa trơn, từ một hợp số.

Ý tưởng đến từ [Định lý Fermat nhỏ](phi-function.md#application).
Cho phân tích thừa số của $n$ là $n = p \cdot q$.
Nó nói rằng nếu $a$ nguyên tố cùng nhau với $p$, thì mệnh đề sau đúng:

$$a^{p - 1} \equiv 1 \pmod{p}$$

Điều này cũng có nghĩa là

$${\left(a^{(p - 1)}\right)}^k \equiv a^{k \cdot (p - 1)} \equiv 1 \pmod{p}.$$

Vì vậy với bất kỳ $M$ nào có $p - 1 ~|~ M$ chúng ta biết rằng $a^M \equiv 1$.
Điều này có nghĩa là $a^M - 1 = p \cdot r$, và do đó cũng có $p ~|~ \gcd(a^M - 1, n)$.

Do đó, nếu $p - 1$ đối với một thừa số $p$ của $n$ chia hết $M$, chúng ta có thể trích xuất một thừa số bằng cách sử dụng [thuật toán Euclid](euclid-algorithm.md).

Rõ ràng là $M$ nhỏ nhất là bội số của mọi số $\mathrm{B}$-lũy thừa trơn là $\text{lcm}(1,~2~,3~,4~,~\dots,~B)$.
Hoặc cách khác:

$$M = \prod_{\text{số nguyên tố } q \le B} q^{\lfloor \log_q B \rfloor}$$

Lưu ý, nếu $p-1$ chia hết $M$ đối với tất cả các thừa số nguyên tố $p$ của $n$, thì $\gcd(a^M - 1, n)$ sẽ chỉ là $n$.
Trong trường hợp này chúng ta không nhận được một thừa số.
Do đó, chúng ta sẽ cố gắng thực hiện $\gcd$ nhiều lần, trong khi chúng ta tính toán $M$.

Một số hợp số không có các thừa số $p$ sao cho $p-1$ lá $\mathrm{B}$-lũy thừa trơn với $\mathrm{B}$ nhỏ.
Ví dụ, đối với hợp số $100~000~000~000~000~493 = 763~013 \cdot 131~059~365~961$, các giá trị $p-1$ tương ứng là $190~753$-lũy thừa trơn và $1~092~161~383$-lũy thừa trơn.
Chúng ta sẽ phải chọn $B \geq 190~753$ để phân tích thừa số của số này.

Trong cài đặt sau, chúng tôi bắt đầu với $\mathrm{B} = 10$ và tăng $\mathrm{B}$ sau mỗi lần lặp.

```{.cpp file=factorization_p_minus_1}
long long pollards_p_minus_1(long long n) {
    int B = 10;
    long long g = 1;
    while (B <= 1000000 && g < n) {
        long long a = 2 + rand() %  (n - 3);
        g = gcd(a, n);
        if (g > 1)
            return g;

        // tính a^M
        for (int p : primes) {
            if (p >= B)
                continue;
            long long p_power = 1;
            while (p_power * p <= B)
                p_power *= p;
            a = power(a, p_power, n);

            g = gcd(a - 1, n);
            if (g > 1 && g < n)
                return g;
        }
        B *= 2;
    }
    return 1;
}

```

Quan sát thấy rằng đây là một thuật toán xác suất.
Hệ quả của điều này là có khả năng thuật toán hoàn toàn không thể tìm thấy một thừa số.

Độ phức tạp là $O(B \log B \log^2 n)$ mỗi lần lặp.

## Thuật toán Pollard's rho (Pollard's rho algorithm) {: #pollards-rho-algorithm}

Thuật toán Pollard's Rho là một thuật toán phân tích thừa số khác của John Pollard.

Cho phân tích thừa số nguyên tố của một số là $n = p q$.
Thuật toán xem xét một dãy giả ngẫu nhiên $\{x_i\} = \{x_0,~f(x_0),~f(f(x_0)),~\dots\}$ trong đó $f$ là một hàm đa thức, thường $f(x) = (x^2 + c) \bmod n$ được chọn với $c = 1$.

Trong trường hợp này, chúng ta không quan tâm đến dãy $\{x_i\}$. 
Chúng ta quan tâm nhiều hơn đến dãy $\{x_i \bmod p\}$.
Vì $f$ là một hàm đa thức, và tất cả các giá trị đều nằm trong khoảng $[0;~p)$, dãy này cuối cùng sẽ hội tụ thành một vòng lặp.
**Nghịch lý ngày sinh** thực sự gợi ý rằng số lượng phần tử kỳ vọng là $O(\sqrt{p})$ cho đến khi sự lặp lại bắt đầu.
Nếu $p$ nhỏ hơn $\sqrt{n}$, sự lặp lại có khả năng sẽ bắt đầu trong $O(\sqrt[4]{n})$.

Dưới đây là hình ảnh trực quan của một dãy như vậy $\{x_i \bmod p\}$ với $n = 2206637$, $p = 317$, $x_0 = 2$ và $f(x) = x^2 + 1$.
Từ dạng của dãy, bạn có thể thấy rất rõ tại sao thuật toán được gọi là thuật toán Pollard's $\rho$.

<div style="text-align: center;">
  <img src="pollard_rho.png" alt="Pollard's rho visualization">
</div>

Tuy nhiên, vẫn còn một câu hỏi mở.
Làm thế nào chúng ta có thể khai thác các tính chất của dãy $\{x_i \bmod p\}$ để có lợi cho chúng ta mà không cần biết chính số $p$?

Nó thực sự khá dễ dàng.
Có một chu trình trong dãy $\{x_i \bmod p\}_{i \le j}$ khi và chỉ khi có hai chỉ số $s, t \le j$ sao cho $x_s \equiv x_t \bmod p$.
Phương trình này có thể được viết lại thành $x_s - x_t \equiv 0 \bmod p$ hay tương tự là $p ~|~ \gcd(x_s - x_t, n)$.

Do đó, nếu chúng ta tìm thấy hai chỉ số $s$ và $t$ với $g = \gcd(x_s - x_t, n) > 1$, chúng ta đã tìm thấy một chu trình và cũng là một thừa số $g$ của $n$.
Có thể xảy ra trường hợp $g = n$.
Trong trường hợp này, chúng ta chưa tìm thấy một thừa số thích hợp, vì vậy chúng ta phải lặp lại thuật toán với một tham số khác (giá trị bắt đầu $x_0$ khác, hằng số $c$ khác trong hàm đa thức $f$).

Để tìm chu trình, chúng ta có thể sử dụng bất kỳ thuật toán phát hiện chu trình phổ biến nào.

### Thuật toán tìm chu trình của Floyd (Floyd's cycle-finding algorithm) {: #floyds-cycle-finding-algorithm}

Thuật toán này tìm một chu trình bằng cách sử dụng hai con trỏ di chuyển trên dãy với tốc độ khác nhau.
Trong mỗi lần lặp, con trỏ đầu tiên sẽ tiến một phần tử, trong khi con trỏ thứ hai tiến đến mỗi phần tử khác.
Sử dụng ý tưởng này, dễ dàng quan sát thấy rằng nếu có một chu trình, tại một thời điểm nào đó, con trỏ thứ hai sẽ quay lại gặp con trỏ đầu tiên trong các vòng lặp.
Nếu độ dài chu trình là $\lambda$ và $\mu$ là chỉ số đầu tiên mà chu trình bắt đầu, thì thuật toán sẽ chạy trong thời gian $O(\lambda + \mu)$.

Thuật toán này còn được gọi là [Thuật toán Rùa và Thỏ](../others/tortoise_and_hare.md), dựa trên câu chuyện ngụ ngôn trong đó một con rùa (con trỏ chậm) và một con thỏ (con trỏ nhanh hơn) chạy đua.

Thực sự có thể xác định tham số $\lambda$ và $\mu$ bằng cách sử dụng thuật toán này (cũng trong thời gian $O(\lambda + \mu)$ và không gian $O(1)$).
Khi phát hiện thấy chu trình, thuật toán sẽ trả về 'True'. 
Nếu dãy không có chu trình, thì hàm sẽ lặp vô hạn.
Tuy nhiên, sử dụng thuật toán Pollard's Rho, điều này có thể phòng tránh được. 

```text
function floyd(f, x0):
    tortoise = x0
    hare = f(x0)
    while tortoise != hare:
        tortoise = f(tortoise)
        hare = f(f(hare))
    return true
```

### Cài đặt {: #implementation}

Đầu tiên, đây là một cài đặt sử dụng **thuật toán tìm chu trình của Floyd**.
Thuật toán thường chạy trong thời gian $O(\sqrt[4]{n} \log(n))$.

```{.cpp file=pollard_rho}
long long mult(long long a, long long b, long long mod) {
    return (__int128)a * b % mod;
}

long long f(long long x, long long c, long long mod) {
    return (mult(x, x, mod) + c) % mod;
}

long long rho(long long n, long long x0=2, long long c=1) {
    long long x = x0;
    long long y = x0;
    long long g = 1;
    while (g == 1) {
        x = f(x, c, n);
        y = f(y, c, n);
        y = f(y, c, n);
        g = gcd(abs(x - y), n);
    }
    return g;
}
```

Bảng sau đây hiển thị các giá trị của $x$ và $y$ trong quá trình thực hiện thuật toán cho $n = 2206637$, $x_0 = 2$ và $c = 1$.

$$
\newcommand\T{\Rule{0pt}{1em}{.3em}}
\begin{array}{|l|l|l|l|l|l|}
\hline
i & x_i \bmod n & x_{2i} \bmod n & x_i \bmod 317 & x_{2i} \bmod 317 & \gcd(x_i - x_{2i}, n) \\
\hline
0   & 2       & 2       & 2       & 2       & -   \\
1   & 5       & 26      & 5       & 26      & 1   \\
2   & 26      & 458330  & 26      & 265     & 1   \\
3   & 677     & 1671573 & 43      & 32      & 1   \\
4   & 458330  & 641379  & 265     & 88      & 1   \\
5   & 1166412 & 351937  & 169     & 67      & 1   \\
6   & 1671573 & 1264682 & 32      & 169     & 1   \\
7   & 2193080 & 2088470 & 74      & 74      & 317 \\
\hline
\end{array}$$

Cài đặt sử dụng hàm `mult`, nhân hai số nguyên $\le 10^{18}$ mà không bị tràn bằng cách sử dụng kiểu `__int128` của GCC cho số nguyên 128-bit.
Nếu không có sẵn GCC, bạn có thể sử dụng ý tưởng tương tự như [lũy thừa nhị phân](binary-exp.md).

```{.cpp file=pollard_rho_mult2}
long long mult(long long a, long long b, long long mod) {
    long long result = 0;
    while (b) {
        if (b & 1)
            result = (result + a) % mod;
        a = (a + a) % mod;
        b >>= 1;
    }
    return result;
}
```

Ngoài ra bạn cũng có thể cài đặt [Phép nhân Montgomery](montgomery_multiplication.md).

Như đã nêu trước đó, nếu $n$ là hợp số và thuật toán trả về $n$ là thừa số, bạn phải lặp lại quy trình với các tham số khác nhau $x_0$ và $c$.
V.d. lựa chọn $x_0 = c = 1$ sẽ không phân tích được $25 = 5 \cdot 5$.
Thuật toán sẽ trả về $25$.
Tuy nhiên, lựa chọn $x_0 = 1$, $c = 2$ sẽ phân tích được nó.

### Thuật toán Brent (Brent's algorithm) {: #brents-algorithm}

Brent cài đặt một phương pháp tương tự như Floyd, sử dụng hai con trỏ.
Sự khác biệt là thay vì tiến các con trỏ một và hai vị trí tương ứng, chúng được tiến theo lũy thừa của hai. 
Ngay khi $2^i$ lớn hơn $\lambda$ và $\mu$, chúng ta sẽ tìm thấy chu trình.

```text
function floyd(f, x0):
    tortoise = x0
    hare = f(x0)
    l = 1
    while tortoise != hare:
        tortoise = hare
        repeat l times:
            hare = f(hare)
            if tortoise == hare:
                return true
        l *= 2
    return true
```

Thuật toán Brent cũng chạy trong thời gian tuyến tính, nhưng thường nhanh hơn Floyd, vì nó sử dụng ít lần đánh giá hàm $f$ hơn.

### Cài đặt {: #implementation-1}

Cài đặt đơn giản của thuật toán Brent có thể được tăng tốc bằng cách bỏ qua các số hạng $x_l - x_k$ nếu $k < \frac{3 \cdot l}{2}$.
Ngoài ra, thay vì thực hiện tính toán $\gcd$ ở mỗi bước, chúng ta nhân các số hạng và chỉ thực sự kiểm tra $\gcd$ sau mỗi vài bước và quay lui nếu vượt quá.

```{.cpp file=pollard_rho_brent}
long long brent(long long n, long long x0=2, long long c=1) {
    long long x = x0;
    long long g = 1;
    long long q = 1;
    long long xs, y;

    int m = 128;
    int l = 1;
    while (g == 1) {
        y = x;
        for (int i = 1; i < l; i++)
            x = f(x, c, n);
        int k = 0;
        while (k < l && g == 1) {
            xs = x;
            for (int i = 0; i < m && i < l - k; i++) {
                x = f(x, c, n);
                q = mult(q, abs(y - x), n);
            }
            g = gcd(q, n);
            k += m;
        }
        l *= 2;
    }
    if (g == n) {
        do {
            xs = f(xs, c, n);
            g = gcd(abs(xs - y), n);
        } while (g == 1);
    }
    return g;
}
```

Sự kết hợp của phép chia thử cho các số nguyên tố nhỏ cùng với phiên bản thuật toán Pollard's rho của Brent tạo nên một thuật toán phân tích thừa số rất mạnh mẽ.

## Bài tập luyện tập {: #practice-problems}

- [SPOJ - FACT0](https://www.spoj.com/problems/FACT0/)
- [SPOJ - FACT1](https://www.spoj.com/problems/FACT1/)
- [SPOJ - FACT2](https://www.spoj.com/problems/FACT2/)
- [GCPC 15 - Divisions](https://codeforces.com/gym/100753)
