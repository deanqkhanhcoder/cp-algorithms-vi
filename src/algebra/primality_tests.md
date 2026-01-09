---
tags:
    - Original
---

# Kiểm tra số nguyên tố (Primality tests) {: #primality-tests}

Bài viết này mô tả nhiều thuật toán để xác định xem một số có phải là số nguyên tố hay không.

## Phép chia thử (Trial division) {: #trial-division}

Theo định nghĩa, một số nguyên tố không có bất kỳ ước số nào khác ngoài $1$ và chính nó.
Một hợp số có ít nhất một ước số bổ sung, hãy gọi nó là $d$.
Đương nhiên $\frac{n}{d}$ cũng là một ước số của $n$.
Dễ thấy rằng, hoặc $d \le \sqrt{n}$ hoặc $\frac{n}{d} \le \sqrt{n}$, do đó một trong các ước số $d$ và $\frac{n}{d}$ là $\le \sqrt{n}$.
Chúng ta có thể sử dụng thông tin này để kiểm tra tính nguyên tố.

Chúng tôi cố gắng tìm một ước số không tầm thường, bằng cách kiểm tra xem có bất kỳ số nào giữa $2$ và $\sqrt{n}$ là ước số của $n$ hay không.
Nếu nó là một ước số, thì $n$ chắc chắn không phải là số nguyên tố, nếu không thì nó là số nguyên tố.

```cpp
bool isPrime(int x) {
    for (int d = 2; d * d <= x; d++) {
        if (x % d == 0)
            return false;
    }
    return x >= 2;
}
```

Đây là dạng đơn giản nhất của kiểm tra số nguyên tố.
Bạn có thể tối ưu hóa hàm này khá nhiều, ví dụ bằng cách chỉ kiểm tra tất cả các số lẻ trong vòng lặp, vì số nguyên tố chẵn duy nhất là 2.
Nhiều tối ưu hóa như vậy được mô tả trong bài viết về [phân tích thừa số nguyên](factorization.md).

## Kiểm tra tính nguyên tố Fermat (Fermat primality test) {: #fermat-primality-test}

Đây là một kiểm tra xác suất.

Định lý Fermat nhỏ (xem thêm [Hàm phi Euler](phi-function.md)) nêu rằng, đối với một số nguyên tố $p$ và một số nguyên $a$ nguyên tố cùng nhau, phương trình sau giữ đúng:

$$a^{p-1} \equiv 1 \bmod p$$

Nói chung định lý này không giữ đúng cho các hợp số.

Điều này có thể được sử dụng để tạo ra một kiểm tra tính nguyên tố.
Chúng ta chọn một số nguyên $2 \le a \le p - 2$, và kiểm tra xem phương trình có giữ đúng hay không.
Nếu nó không giữ đúng, ví dụ $a^{p-1} \not\equiv 1 \bmod p$, chúng ta biết rằng $p$ không thể là một số nguyên tố.
Trong trường hợp này, chúng ta gọi cơ số $a$ là một *nhân chứng Fermat (Fermat witness)* cho tính hợp số của $p$.

Tuy nhiên, cũng có thể phương trình giữ đúng cho một hợp số.
Vì vậy, nếu phương trình giữ đúng, chúng ta không có bằng chứng cho tính nguyên tố.
Chúng ta chỉ có thể nói rằng $p$ là *có thể là số nguyên tố (probably prime)*.
Nếu hóa ra con số thực sự là hợp số, chúng ta gọi cơ số $a$ là một *kẻ nói dối Fermat (Fermat liar)*.

Bằng cách chạy thử nghiệm cho tất cả các cơ số $a$ có thể, chúng ta thực sự có thể chứng minh rằng một số là số nguyên tố.
Tuy nhiên, điều này không được thực hiện trong thực tế, vì đây là nỗ lực nhiều hơn nhiều so với việc chỉ thực hiện *phép chia thử*.
Thay vào đó, kiểm tra sẽ được lặp lại nhiều lần với các lựa chọn ngẫu nhiên cho $a$.
Nếu chúng ta không tìm thấy nhân chứng nào cho tính hợp số, rất có thể con số thực sự là số nguyên tố.

```cpp
bool probablyPrimeFermat(int n, int iter=5) {
    if (n < 4)
        return n == 2 || n == 3;

    for (int i = 0; i < iter; i++) {
        int a = 2 + rand() % (n - 3);
        if (binpower(a, n - 1, n) != 1)
            return false;
    }
    return true;
}
```

Chúng tôi sử dụng [Lũy thừa nhị phân](binary-exp.md) để tính toán hiệu quả lũy thừa $a^{p-1}$.

Tuy nhiên có một tin xấu:
tồn tại một số hợp số trong đó $a^{n-1} \equiv 1 \bmod n$ giữ đúng cho tất cả $a$ nguyên tố cùng nhau với $n$, ví dụ đối với số $561 = 3 \cdot 11 \cdot 17$.
Những số như vậy được gọi là *số Carmichael*.
Kiểm tra tính nguyên tố Fermat chỉ có thể xác định các số này, nếu chúng ta vô cùng may mắn và chọn một cơ số $a$ với $\gcd(a, n) \ne 1$.

Kiểm tra Fermat vẫn đang được sử dụng trong thực tế, vì nó rất nhanh và số Carmichael rất hiếm.
Ví dụ chỉ tồn tại 646 số như vậy dưới $10^9$.

## Kiểm tra tính nguyên tố Miller-Rabin (Miller-Rabin primality test) {: #miller-rabin-primality-test}

Kiểm tra Miller-Rabin mở rộng các ý tưởng từ kiểm tra Fermat.

Đối với một số lẻ $n$, $n-1$ là chẵn và chúng ta có thể tách tất cả các lũy thừa của 2 ra.
Chúng ta có thể viết:

$$n - 1 = 2^s \cdot d,~\text{với}~d~\text{lẻ}.$$

Điều này cho phép chúng ta phân tích phương trình của định lý Fermat nhỏ:

$$\begin{array}{rl}
a^{n-1} \equiv 1 \bmod n &\Longleftrightarrow a^{2^s d} - 1 \equiv 0 \bmod n \\\\
&\Longleftrightarrow (a^{2^{s-1} d} + 1) (a^{2^{s-1} d} - 1) \equiv 0 \bmod n \\\\
&\Longleftrightarrow (a^{2^{s-1} d} + 1) (a^{2^{s-2} d} + 1) (a^{2^{s-2} d} - 1) \equiv 0 \bmod n \\\\
&\quad\vdots \\\\
&\Longleftrightarrow (a^{2^{s-1} d} + 1) (a^{2^{s-2} d} + 1) \cdots (a^{d} + 1) (a^{d} - 1) \equiv 0 \bmod n \\\\
\end{array}$$

Nếu $n$ là số nguyên tố, thì $n$ phải chia hết một trong những thừa số này.
Và trong kiểm tra tính nguyên tố Miller-Rabin, chúng tôi kiểm tra chính xác tuyên bố đó, đây là một phiên bản chặt chẽ hơn của tuyên bố kiểm tra Fermat.
Đối với một cơ số $2 \le a \le n-2$ chúng tôi kiểm tra xem liệu

$$a^d \equiv 1 \bmod n$$

giữ đúng hoặc

$$a^{2^r d} \equiv -1 \bmod n$$

giữ đúng cho một số $0 \le r \le s - 1$.

Nếu chúng ta tìm thấy một cơ số $a$ không thỏa mãn bất kỳ đẳng thức nào ở trên, thì chúng ta đã tìm thấy một *nhân chứng* cho tính hợp số của $n$.
Trong trường hợp này, chúng tôi đã chứng minh rằng $n$ không phải là một số nguyên tố.

Tương tự như kiểm tra Fermat, cũng có thể tập hợp các phương trình được thỏa mãn cho một hợp số.
Trong trường hợp đó, cơ số $a$ được gọi là *kẻ nói dối mạnh (strong liar)*.
Nếu một cơ số $a$ thỏa mãn các phương trình (một trong số chúng), $n$ chỉ là *số nguyên tố có khả năng mạnh (strong probable prime)*.
Tuy nhiên, không có số nào giống như số Carmichael, nơi tất cả các cơ số không tầm thường đều nói dối.
Thực tế có thể chỉ ra rằng, tối đa $\frac{1}{4}$ các cơ số có thể là kẻ nói dối mạnh.
Nếu $n$ là hợp số, chúng ta có xác suất $\ge 75\%$ rằng một cơ số ngẫu nhiên sẽ cho chúng ta biết rằng nó là hợp số.
Bằng cách thực hiện nhiều lần lặp, chọn các cơ số ngẫu nhiên khác nhau, chúng ta có thể biết với xác suất rất cao liệu con số có thực sự là số nguyên tố hay nếu nó là hợp số.

Dưới đây là một cài đặt cho số nguyên 64 bit.

```cpp
using u64 = uint64_t;
using u128 = __uint128_t;

u64 binpower(u64 base, u64 e, u64 mod) {
    u64 result = 1;
    base %= mod;
    while (e) {
        if (e & 1)
            result = (u128)result * base % mod;
        base = (u128)base * base % mod;
        e >>= 1;
    }
    return result;
}

bool check_composite(u64 n, u64 a, u64 d, int s) {
    u64 x = binpower(a, d, n);
    if (x == 1 || x == n - 1)
        return false;
    for (int r = 1; r < s; r++) {
        x = (u128)x * x % n;
        if (x == n - 1)
            return false;
    }
    return true;
};

bool MillerRabin(u64 n, int iter=5) { // returns true if n is probably prime, else returns false.
    if (n < 4)
        return n == 2 || n == 3;

    int s = 0;
    u64 d = n - 1;
    while ((d & 1) == 0) {
        d >>= 1;
        s++;
    }

    for (int i = 0; i < iter; i++) {
        int a = 2 + rand() % (n - 3);
        if (check_composite(n, a, d, s))
            return false;
    }
    return true;
}
```

Trước khi kiểm tra Miller-Rabin, bạn có thể kiểm tra thêm xem một trong vài số nguyên tố đầu tiên có phải là ước số hay không.
Điều này có thể tăng tốc độ kiểm tra lên rất nhiều, vì hầu hết các hợp số có các ước số nguyên tố rất nhỏ.
Ví dụ $88\%$ của tất cả các số có một thừa số nguyên tố nhỏ hơn $100$.

### Phiên bản đơn định (Deterministic version) {: #deterministic-version}

Miller đã chỉ ra rằng có thể làm cho thuật toán trở nên đơn định bằng cách chỉ kiểm tra tất cả các cơ số $\le O((\ln n)^2)$.
Bach sau đó đã đưa ra một giới hạn cụ thể, chỉ cần kiểm tra tất cả các cơ số $a \le 2 \ln(n)^2$.

Đây vẫn là một số lượng cơ số khá lớn.
Vì vậy, mọi người đã đầu tư khá nhiều sức mạnh tính toán vào việc tìm kiếm các giới hạn dưới.
Hóa ra, để kiểm tra một số nguyên 32 bit, chỉ cần kiểm tra 4 cơ số nguyên tố đầu tiên: 2, 3, 5 và 7.
Hợp số nhỏ nhất thất bại trong kiểm tra này là $3,215,031,751 = 151 \cdot 751 \cdot 28351$.
Và để kiểm tra số nguyên 64 bit, là đủ để kiểm tra 12 cơ số nguyên tố đầu tiên: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, và 37.

Kết quả là cài đặt đơn định sau:

```cpp
bool MillerRabin(u64 n) { // returns true if n is prime, else returns false.
    if (n < 2)
        return false;

    int r = 0;
    u64 d = n - 1;
    while ((d & 1) == 0) {
        d >>= 1;
        r++;
    }

    for (int a : {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37}) {
        if (n == a)
            return true;
        if (check_composite(n, a, d, r))
            return false;
    }
    return true;
}
```

Cũng có thể thực hiện kiểm tra với chỉ 7 cơ số: 2, 325, 9375, 28178, 450775, 9780504 và 1795265022.
Tuy nhiên, vì những con số này (trừ 2) không phải là số nguyên tố, bạn cần kiểm tra thêm xem số bạn đang kiểm tra có bằng bất kỳ ước số nguyên tố nào của các cơ số đó không: 2, 3, 5, 13, 19, 73, 193, 407521, 299210837.

## Bài tập luyện tập {: #practice-problems}

- [SPOJ - Prime or Not](https://www.spoj.com/problems/PON/)
- [Project euler - Investigating a Prime Pattern](https://projecteuler.net/problem=146)

---
