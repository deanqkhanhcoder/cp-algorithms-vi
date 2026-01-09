---
tags:
  - Translated
e_maxx_link: euler_function
---

# Hàm phi Euler (Euler's totient function) {: #euler-totient-function}

Hàm phi Euler, còn được gọi là **phi-function** $\phi (n)$, đếm số lượng các số nguyên nằm giữa 1 và $n$, mà nguyên tố cùng nhau với $n$. Hai số được gọi là nguyên tố cùng nhau nếu ước chung lớn nhất của chúng bằng $1$ ($1$ được coi là nguyên tố cùng nhau với bất kỳ số nào).

Dưới đây là các giá trị của $\phi(n)$ cho một vài số nguyên dương đầu tiên:

$$\begin{array}{|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|}
\hline
n & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 & 10 & 11 & 12 & 13 & 14 & 15 & 16 & 17 & 18 & 19 & 20 & 21 \\\\ \hline
\phi(n) & 1 & 1 & 2 & 2 & 4 & 2 & 6 & 4 & 6 & 4 & 10 & 4 & 12 & 6 & 8 & 8 & 16 & 6 & 18 & 8 & 12 \\\\ \hline
\end{array}$$

## Các tính chất (Properties) {: #properties}

Các tính chất sau đây của hàm phi Euler đủ để tính toán nó cho bất kỳ số nào:

  - Nếu $p$ là một số nguyên tố, thì $\gcd(p, q) = 1$ với mọi $1 \le q < p$. Do đó chúng ta có:
  
$$\phi (p) = p - 1.$$

  - Nếu $p$ là một số nguyên tố và $k \ge 1$, thì có chính xác $p^k / p$ số giữa $1$ và $p^k$ chia hết cho $p$.
    Điều này cho chúng ta:
    
$$\phi(p^k) = p^k - p^{k-1}.$$

  - Nếu $a$ và $b$ là nguyên tố cùng nhau, thì:
    
    \[\phi(a b) = \phi(a) \cdot \phi(b).\]
    
    Quan hệ này không dễ thấy. Nó xuất phát từ [Định lý thặng dư Trung Hoa](chinese-remainder-theorem.md). Định lý thặng dư Trung Hoa đảm bảo rằng, với mỗi $0 \le x < a$ và mỗi $0 \le y < b$, tồn tại duy nhất một $0 \le z < a b$ với $z \equiv x \pmod{a}$ và $z \equiv y \pmod{b}$. Không khó để chỉ ra rằng $z$ nguyên tố cùng nhau với $a b$ khi và chỉ khi $x$ nguyên tố cùng nhau với $a$ và $y$ nguyên tố cùng nhau với $b$. Do đó lượng số nguyên nguyên tố cùng nhau với $a b$ bằng tích của lượng số của $a$ và $b$.

  - Tổng quát, với $a$ và $b$ không nguyên tố cùng nhau, phương trình

    \[\phi(ab) = \phi(a) \cdot \phi(b) \cdot \dfrac{d}{\phi(d)}\]

    với $d = \gcd(a, b)$ giữ đúng.

Như vậy, sử dụng ba tính chất đầu tiên, chúng ta có thể tính $\phi(n)$ thông qua phân tích thừa số của $n$ (phân rã $n$ thành tích các thừa số nguyên tố của nó).
Nếu $n = {p_1}^{a_1} \cdot {p_2}^{a_2} \cdots {p_k}^{a_k}$, trong đó $p_i$ là các thừa số nguyên tố của $n$,

$$\begin{align}
\phi (n) &= \phi ({p_1}^{a_1}) \cdot \phi ({p_2}^{a_2}) \cdots  \phi ({p_k}^{a_k}) \\\\
&= \left({p_1}^{a_1} - {p_1}^{a_1 - 1}\right) \cdot \left({p_2}^{a_2} - {p_2}^{a_2 - 1}\right) \cdots \left({p_k}^{a_k} - {p_k}^{a_k - 1}\right) \\\\
&= p_1^{a_1} \cdot \left(1 - \frac{1}{p_1}\right) \cdot p_2^{a_2} \cdot \left(1 - \frac{1}{p_2}\right) \cdots p_k^{a_k} \cdot \left(1 - \frac{1}{p_k}\right) \\\\
&= n \cdot \left(1 - \frac{1}{p_1}\right) \cdot \left(1 - \frac{1}{p_2}\right) \cdots \left(1 - \frac{1}{p_k}\right)
\end{align}$$

## Cài đặt (Implementation) {: #implementation}

Dưới đây là một cài đặt sử dụng phân tích thừa số trong $O(\sqrt{n})$:

```cpp
int phi(int n) {
    int result = n;
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            while (n % i == 0)
                n /= i;
            result -= result / i;
        }
    }
    if (n > 1)
        result -= result / n;
    return result;
}
```

## Hàm phi Euler từ $1$ đến $n$ trong $O(n \log\log{n})$ (Euler totient function from $1$ to $n$ in $O(n \log\log{n})$) {: #etf_1_to_n data-toc-label="Euler totient function from 1 to n in <script type=\"math/tex\">O(n log log n)</script>"}

Nếu chúng ta cần hàm phi của tất cả các số giữa $1$ và $n$, thì việc phân tích thừa số tất cả $n$ số là không hiệu quả.
Chúng ta có thể sử dụng cùng ý tưởng như [Sàng Eratosthenes](sieve-of-eratosthenes.md).
Nó vẫn dựa trên tính chất được trình bày ở trên, nhưng thay vì cập nhật kết quả tạm thời cho từng thừa số nguyên tố cho từng số, chúng ta tìm tất cả các số nguyên tố và với mỗi số nguyên tố cập nhật kết quả tạm thời của tất cả các số chia hết cho số nguyên tố đó.

Vì cách tiếp cận này về cơ bản giống với Sàng Eratosthenes, độ phức tạp cũng sẽ giống nhau: $O(n \log \log n)$

```cpp
void phi_1_to_n(int n) {
    vector<int> phi(n + 1);
    for (int i = 0; i <= n; i++)
        phi[i] = i;
    
    for (int i = 2; i <= n; i++) {
        if (phi[i] == i) {
            for (int j = i; j <= n; j += i)
                phi[j] -= phi[j] / i;
        }
    }
}
```

### Tìm hàm phi từ $L$ đến $R$ bằng sàng phân đoạn (Finding the totient from $L$ to $R$ using the segmented sieve) {: #finding-the-totient-from-l-to-r-using-the-segmented-sieve data-toc-label="Finding the totient from L to R using the segmented sieve"}

Nếu chúng ta cần hàm phi của tất cả các số giữa $L$ và $R$, chúng ta có thể sử dụng cách tiếp cận [sàng phân đoạn](sieve-of-eratosthenes.md#segmented-sieve).

Thuật toán đầu tiên tính trước tất cả các số nguyên tố lên đến $\sqrt{R}$ bằng cách sử dụng [sàng tuyến tính](prime-sieve-linear.md) trong thời gian và không gian $O(\sqrt{R})$. Đối với mỗi số trong khoảng $[L, R]$, sau đó nó áp dụng công thức $\phi$ dựa trên phân tích thừa số bằng cách lặp qua các số nguyên tố này. Chúng ta duy trì một mảng dư để theo dõi phần chưa phân tích của mỗi số. Nếu phần dư vẫn lớn hơn 1 sau khi xử lý tất cả các số nguyên tố nhỏ, nó chỉ ra một thừa số nguyên tố lớn hơn $\sqrt{R}$, được xử lý trong bước cuối cùng. Độ phức tạp tổng thể cho việc tính toán phạm vi là $O((R - L + 1) \log \log R) + \sqrt{R}$.


```cpp
const long long MAX_RANGE = 1e6 + 6;
vector<long long> primes;
long long phi[MAX_RANGE], rem[MAX_RANGE];

vector<int> linear_sieve(int n) { 
    vector<bool> composite(n + 1, 0);
    vector<int> prime;

    // 0 and 1 are not composite (nor prime)
    composite[0] = composite[1] = 1;

    for(int i = 2; i <= n; i++) {
        if(!composite[i]) prime.push_back(i);
        for(int j = 0; j < prime.size() && i * prime[j] <= n; j++) {
            composite[i * prime[j]] = true;
            if(i % prime[j] == 0) break;
        }
    }
    return prime;
}

// To get the value of phi(x) for L <= x <= R, use phi[x - L].
void segmented_phi(long long L, long long R) { 
    for(long long i = L; i <= R; i++) {
        rem[i - L] = i;
        phi[i - L] = i;
    }

    for(long long i : primes) {
        for(long long j = max(i * i, (L + i - 1) / i * i); j <= R; j += i) {
            phi[j - L] -= phi[j - L] / i;
            while(rem[j - L] % i == 0) rem[j - L] /= i;
        }
    }

    for(long long i = 0; i < R - L + 1; i++) {
        if(rem[i] > 1) phi[i] -= phi[i] / rem[i];
    }
}
```

## Tính chất tổng ước số (Divisor sum property) {: #divsum}

Tính chất thú vị này được thiết lập bởi Gauss:

$$ \sum_{d|n} \phi{(d)} = n$$

Ở đây tổng là trên tất cả các ước số dương $d$ của $n$.

Ví dụ các ước số của 10 là 1, 2, 5 và 10.
Do đó $\phi{(1)} + \phi{(2)} + \phi{(5)} + \phi{(10)} = 1 + 1 + 4 + 4 = 10$.

### Tìm hàm phi từ 1 đến $n$ bằng tính chất tổng ước số (Finding the totient from 1 to $n$ using the divisor sum property) {: #finding-the-totient-from-1-to-n-using-the-divisor-sum-property data-toc-label="Finding the totient from 1 to n using the divisor sum property"}

Tính chất tổng ước số cũng cho phép chúng ta tính hàm phi của tất cả các số giữa 1 và $n$.
Cài đặt này đơn giản hơn một chút so với cài đặt trước đó dựa trên Sàng Eratosthenes, tuy nhiên cũng có độ phức tạp tệ hơn một chút: $O(n \log n)$

```cpp
void phi_1_to_n(int n) {
    vector<int> phi(n + 1);
    phi[0] = 0;
    phi[1] = 1;
    for (int i = 2; i <= n; i++)
        phi[i] = i - 1;
    
    for (int i = 2; i <= n; i++)
        for (int j = 2 * i; j <= n; j += i)
              phi[j] -= phi[i];
}
```

## Ứng dụng trong định lý Euler (Application in Euler's theorem) {: #application}

Tính chất nổi tiếng và quan trọng nhất của hàm phi Euler được thể hiện trong **định lý Euler**: 

$$a^{\phi(m)} \equiv 1 \pmod m \quad \text{nếu } a \text{ và } m \text{ là nguyên tố cùng nhau.}$$

Trong trường hợp cụ thể khi $m$ là số nguyên tố, định lý Euler trở thành **định lý Fermat nhỏ**:

$$a^{m - 1} \equiv 1 \pmod m$$

Định lý Euler và hàm phi Euler xuất hiện khá thường xuyên trong các ứng dụng thực tế, ví dụ cả hai đều được sử dụng để tính [nghịch đảo nhân modulo](module-inverse.md).

Như là hệ quả trực tiếp chúng ta cũng nhận được sự tương đương:

$$a^n \equiv a^{n \bmod \phi(m)} \pmod m$$

Điều này cho phép tính $x^n \bmod m$ cho $n$ rất lớn, đặc biệt nếu $n$ là kết quả của một tính toán khác, vì nó cho phép tính $n$ dưới một modulo.

### Lý thuyết nhóm (Group Theory) {: #group-theory}
$\phi(n)$ là [cấp của nhóm nhân modulo n](https://en.wikipedia.org/wiki/Multiplicative_group_of_integers_modulo_n) $(\mathbb Z / n\mathbb Z)^\times$, đó là nhóm các đơn vị (các phần tử có nghịch đảo nhân). Các phần tử có nghịch đảo nhân chính xác là những số nguyên tố cùng nhau với $n$.

[Cấp nhân](https://en.wikipedia.org/wiki/Multiplicative_order) của một phần tử $a$ mod $n$, ký hiệu $\operatorname{ord}_n(a)$, là $k>0$ nhỏ nhất sao cho $a^k \equiv 1 \pmod m$. $\operatorname{ord}_n(a)$ là kích thước của nhóm con được sinh bởi $a$, vì vậy theo Định lý Lagrange, cấp nhân của bất kỳ $a$ nào cũng phải chia hết $\phi(n)$. Nếu cấp nhân của $a$ là $\phi(n)$, mức lớn nhất có thể, thì $a$ là một [căn nguyên thủy](primitive-root.md) và nhóm là cyclic theo định nghĩa. 

## Tổng quát hóa (Generalization) {: #generalization}

Có một phiên bản ít được biết đến hơn của sự tương đương cuối cùng, cho phép tính $x^n \bmod m$ hiệu quả cho $x$ và $m$ không nguyên tố cùng nhau.
Với $x, m$ bất kỳ và $n \geq \log_2 m$:

$$x^{n}\equiv x^{\phi(m)+[n \bmod \phi(m)]} \mod m$$

Chứng minh:

Gọi $p_1, \dots, p_t$ là các ước số nguyên tố chung của $x$ và $m$, và $k_i$ là số mũ của chúng trong $m$.
Với chúng ta định nghĩa $a = p_1^{k_1} \dots p_t^{k_t}$, làm cho $\frac{m}{a}$ nguyên tố cùng nhau với $x$.
Và gọi $k$ là số nhỏ nhất sao cho $a$ chia hết $x^k$.
Giả sử $n \ge k$, chúng ta có thể viết:

$$\begin{align}x^n \bmod m &= \frac{x^k}{a}ax^{n-k}\bmod m \\
&= \frac{x^k}{a}\left(ax^{n-k}\bmod m\right) \bmod m \\
&= \frac{x^k}{a}\left(ax^{n-k}\bmod a \frac{m}{a}\right) \bmod m \\
&=\frac{x^k}{a} a \left(x^{n-k} \bmod \frac{m}{a}\right)\bmod m \\
&= x^k\left(x^{n-k} \bmod \frac{m}{a}\right)\bmod m
\end{align}$$

Sự tương đương giữa dòng thứ ba và thứ tư xuất phát từ thực tế là $ab \bmod ac = a(b \bmod c)$.
Thật vậy nếu $b = cd + r$ với $r < c$, thì $ab = acd + ar$ với $ar < ac$.

Vì $x$ và $\frac{m}{a}$ nguyên tố cùng nhau, chúng ta có thể áp dụng định lý Euler và nhận được công thức hiệu quả (vì $k$ rất nhỏ; thực tế $k \le \log_2 m$):

$$x^n \bmod m = x^k\left(x^{n-k \bmod \phi(\frac{m}{a})} \bmod \frac{m}{a}\right)\bmod m.$$

Công thức này khó áp dụng, nhưng chúng ta có thể sử dụng nó để phân tích hành vi của $x^n \bmod m$. Chúng ta có thể thấy rằng dãy các lũy thừa $(x^1 \bmod m, x^2 \bmod m, x^3 \bmod m, \dots)$ đi vào một chu trình có độ dài $\phi\left(\frac{m}{a}\right)$ sau $k$ (hoặc ít hơn) phần tử đầu tiên. 
$\phi\left(\frac{m}{a}\right)$ chia hết $\phi(m)$ (vì $a$ và $\frac{m}{a}$ nguyên tố cùng nhau chúng ta có $\phi(a) \cdot \phi\left(\frac{m}{a}\right) = \phi(m)$), do đó chúng ta cũng có thể nói rằng chu kỳ có độ dài $\phi(m)$.
Và vì $\phi(m) \ge \log_2 m \ge k$, chúng ta có thể kết luận công thức mong muốn, đơn giản hơn nhiều:

$$ x^n \equiv x^{\phi(m)} x^{(n - \phi(m)) \bmod \phi(m)} \bmod m \equiv x^{\phi(m)+[n \bmod \phi(m)]} \mod m.$$

## Bài tập luyện tập {: #practice-problems}

* [SPOJ #4141 "Euler Totient Function" [Difficulty: CakeWalk]](http://www.spoj.com/problems/ETF/)
* [UVA #10179 "Irreducible Basic Fractions" [Difficulty: Easy]](http://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1120)
* [UVA #10299 "Relatives" [Difficulty: Easy]](http://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1240)
* [UVA #11327 "Enumerating Rational Numbers" [Difficulty: Medium]](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2302)
* [TIMUS #1673 "Admission to Exam" [Difficulty: High]](http://acm.timus.ru/problem.aspx?space=1&num=1673)
* [UVA 10990 - Another New Function](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1931)
* [Codechef - Golu and Sweetness](https://www.codechef.com/problems/COZIE)
* [SPOJ - LCM Sum](http://www.spoj.com/problems/LCMSUM/)
* [GYM - Simple Calculations  (F)](http://codeforces.com/gym/100975)
* [UVA 13132 - Laser Mirrors](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=5043)
* [SPOJ - GCDEX](http://www.spoj.com/problems/GCDEX/)
* [UVA 12995 - Farey Sequence](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=4878)
* [SPOJ - Totient in Permutation (easy)](http://www.spoj.com/problems/TIP1/)
* [LOJ - Mathematically Hard](http://lightoj.com/volume_showproblem.php?problem=1007)
* [SPOJ - Totient Extreme](http://www.spoj.com/problems/DCEPCA03/)
* [SPOJ - Playing with GCD](http://www.spoj.com/problems/NAJPWG/)
* [SPOJ - G Force](http://www.spoj.com/problems/DCEPC12G/)
* [SPOJ - Smallest Inverse Euler Totient Function](http://www.spoj.com/problems/INVPHI/)
* [Codeforces - Power Tower](http://codeforces.com/problemset/problem/906/D)
* [Kattis - Exponial](https://open.kattis.com/problems/exponial)
* [LeetCode - 372. Super Pow](https://leetcode.com/problems/super-pow/)
* [Codeforces - The Holmes Children](http://codeforces.com/problemset/problem/776/E)
* [Codeforces - Small GCD](https://codeforces.com/contest/1900/problem/D)
