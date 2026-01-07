---
tags:
    - Original
---

# Kiểm tra tính nguyên tố

Bài viết này mô tả nhiều thuật toán để xác định một số có phải là số nguyên tố hay không.

## Phép chia thử

Theo định nghĩa, một số nguyên tố không có ước số nào khác ngoài $1$ và chính nó.
Một hợp số có ít nhất một ước số bổ sung, gọi là $d$.
Đương nhiên $rac{n}{d}$ cũng là một ước của $n$.
Dễ thấy rằng, hoặc $d \le \sqrt{n}$ hoặc $rac{n}{d} \le \sqrt{n}$, do đó một trong các ước $d$ và $rac{n}{d}$ là $\le \sqrt{n}$.
Chúng ta có thể sử dụng thông tin này để kiểm tra tính nguyên tố.

Chúng ta cố gắng tìm một ước không tầm thường, bằng cách kiểm tra xem có bất kỳ số nào trong khoảng từ $2$ đến $\sqrt{n}$ là ước của $n$ hay không.
Nếu có, thì $n$ chắc chắn không phải là số nguyên tố, nếu không thì nó là số nguyên tố.

```cpp
bool isPrime(int x) {
    for (int d = 2; d * d <= x; d++) {
        if (x % d == 0)
            return false;
    }
    return x >= 2;
}
```

Đây là dạng đơn giản nhất của một phép kiểm tra số nguyên tố.
Bạn có thể tối ưu hóa hàm này khá nhiều, ví dụ bằng cách chỉ kiểm tra tất cả các số lẻ trong vòng lặp, vì số nguyên tố chẵn duy nhất là 2.
Nhiều tối ưu hóa như vậy được mô tả trong bài viết về [phân tích thừa số nguyên tố](factorization.md).

## Phép thử tính nguyên tố Fermat

Đây là một phép thử xác suất.

Định lý nhỏ của Fermat (xem thêm [hàm phi Euler](phi-function.md)) phát biểu rằng, đối với một số nguyên tố $p$ và một số nguyên $a$ nguyên tố cùng nhau với $p$, phương trình sau đây đúng:

$$a^{p-1} \equiv 1 \bmod p$$

Nói chung, định lý này không đúng đối với các hợp số.

Điều này có thể được sử dụng để tạo ra một phép thử tính nguyên tố.
Chúng ta chọn một số nguyên $2 \le a \le p - 2$, và kiểm tra xem phương trình có đúng hay không.
Nếu nó không đúng, ví dụ: $a^{p-1} \not\equiv 1 \bmod p$, chúng ta biết rằng $p$ không thể là một số nguyên tố.
Trong trường hợp này, chúng ta gọi cơ sở $a$ là *nhân chứng Fermat* cho tính hợp số của $p$.

Tuy nhiên, cũng có thể phương trình đúng đối với một hợp số.
Vì vậy, nếu phương trình đúng, chúng ta không có bằng chứng cho tính nguyên tố.
Chúng ta chỉ có thể nói rằng $p$ là *có thể là số nguyên tố*.
Nếu hóa ra số đó thực sự là hợp số, chúng ta gọi cơ sở $a$ là *kẻ nói dối Fermat*.

Bằng cách chạy phép thử cho tất cả các cơ sở $a$ có thể, chúng ta thực sự có thể chứng minh một số là số nguyên tố.
Tuy nhiên, điều này không được thực hiện trong thực tế, vì nó tốn nhiều công sức hơn nhiều so với việc chỉ thực hiện *phép chia thử*.
Thay vào đó, phép thử sẽ được lặp lại nhiều lần với các lựa chọn ngẫu nhiên cho $a$.
Nếu chúng ta không tìm thấy nhân chứng nào cho tính hợp số, rất có thể số đó thực sự là số nguyên tố.

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

Chúng ta sử dụng [Lũy thừa nhị phân](binary-exp.md) để tính toán hiệu quả lũy thừa $a^{p-1}$.

Tuy nhiên, có một tin xấu:
tồn tại một số hợp số mà $a^{n-1} \equiv 1 \bmod n$ đúng với mọi $a$ nguyên tố cùng nhau với $n$, ví dụ như số $561 = 3 \cdot 11 \cdot 17$.
Những số như vậy được gọi là *số Carmichael*.
Phép thử tính nguyên tố Fermat chỉ có thể xác định các số này, nếu chúng ta có may mắn lớn và chọn một cơ sở $a$ với $\gcd(a, n) \ne 1$.

Phép thử Fermat vẫn được sử dụng trong thực tế, vì nó rất nhanh và các số Carmichael rất hiếm.
Ví dụ: chỉ tồn tại 646 số như vậy dưới $10^9$.

## Phép thử tính nguyên tố Miller-Rabin

Phép thử Miller-Rabin mở rộng các ý tưởng từ phép thử Fermat.

Đối với một số lẻ $n$, $n-1$ là số chẵn và chúng ta có thể tách ra tất cả các lũy thừa của 2.
Chúng ta có thể viết:

$$n - 1 = 2^s \cdot d,~	ext{với}~d~	ext{lẻ}.$$ 

Điều này cho phép chúng ta phân tích phương trình của định lý nhỏ Fermat:

$$\begin{array}{rl}
    a^{n-1} \equiv 1 \bmod n &\Longleftrightarrow a^{2^s d} - 1 \equiv 0 \bmod n \\

    &\Longleftrightarrow (a^{2^{s-1} d} + 1) (a^{2^{s-1} d} - 1) \equiv 0 \bmod n \\

    &\Longleftrightarrow (a^{2^{s-1} d} + 1) (a^{2^{s-2} d} + 1) (a^{2^{s-2} d} - 1) \equiv 0 \bmod n \\

    &\quad\vdots \\

    &\Longleftrightarrow (a^{2^{s-1} d} + 1) (a^{2^{s-2} d} + 1) \cdots (a^{d} + 1) (a^{d} - 1) \equiv 0 \bmod n \\
\end{array}$$

Nếu $n$ là số nguyên tố, thì $n$ phải chia hết cho một trong các thừa số này.
Và trong phép thử tính nguyên tố Miller-Rabin, chúng ta kiểm tra chính xác mệnh đề đó, là một phiên bản chặt chẽ hơn của mệnh đề của phép thử Fermat.
Đối với một cơ sở $2 \le a \le n-2$ chúng ta kiểm tra xem hoặc

$$a^d \equiv 1 \bmod n$$

đúng hoặc

$$a^{2^r d} \equiv -1 \bmod n$$

đúng với một số $0 \le r \le s - 1$.

Nếu chúng ta tìm thấy một cơ sở $a$ không thỏa mãn bất kỳ đẳng thức nào ở trên, thì chúng ta đã tìm thấy một *nhân chứng* cho tính hợp số của $n$.
Trong trường hợp này, chúng ta đã chứng minh rằng $n$ không phải là một số nguyên tố.

Tương tự như phép thử Fermat, cũng có thể tập hợp các phương trình được thỏa mãn đối với một hợp số.
Trong trường hợp đó, cơ sở $a$ được gọi là *kẻ nói dối mạnh*.
Nếu một cơ sở $a$ thỏa mãn các phương trình (một trong số chúng), $n$ chỉ là *số nguyên tố xác suất mạnh*.
Tuy nhiên, không có số nào giống như các số Carmichael, nơi tất cả các cơ sở không tầm thường đều nói dối.
Trên thực tế, có thể chỉ ra rằng, nhiều nhất là $\frac{1}{4}$ các cơ sở có thể là những kẻ nói dối mạnh.
Nếu $n$ là hợp số, chúng ta có xác suất $\ge 75\%$ rằng một cơ sở ngẫu nhiên sẽ cho chúng ta biết nó là hợp số.
Bằng cách thực hiện nhiều lần lặp, chọn các cơ sở ngẫu nhiên khác nhau, chúng ta có thể nói với xác suất rất cao liệu số đó có thực sự là số nguyên tố hay là hợp số.

Đây là một triển khai cho số nguyên 64 bit.

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

bool MillerRabin(u64 n, int iter=5) { // trả về true nếu n có thể là số nguyên tố, nếu không trả về false.
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

Trước khi thực hiện phép thử Miller-Rabin, bạn có thể kiểm tra thêm xem một trong vài số nguyên tố đầu tiên có phải là một ước số không.
Điều này có thể tăng tốc độ kiểm tra rất nhiều, vì hầu hết các hợp số đều có các ước nguyên tố rất nhỏ.
Ví dụ: $88\%$ tất cả các số có một thừa số nguyên tố nhỏ hơn $100$.

### Phiên bản tất định

Miller đã chỉ ra rằng có thể làm cho thuật toán trở thành tất định bằng cách chỉ kiểm tra tất cả các cơ sở $\le O((\ln n)^2)$.
Bach sau đó đã đưa ra một giới hạn cụ thể, chỉ cần kiểm tra tất cả các cơ sở $a \le 2 \ln(n)^2$.

Đây vẫn là một số lượng cơ sở khá lớn.
Vì vậy, mọi người đã đầu tư khá nhiều sức mạnh tính toán vào việc tìm ra các giới hạn dưới.
Hóa ra, để kiểm tra một số nguyên 32 bit, chỉ cần kiểm tra 4 cơ sở nguyên tố đầu tiên: 2, 3, 5 và 7.
Hợp số nhỏ nhất không qua được phép thử này là $3,215,031,751 = 151 \cdot 751 \cdot 28351$.
Và để kiểm tra số nguyên 64 bit, chỉ cần kiểm tra 12 cơ sở nguyên tố đầu tiên: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, và 37.

Điều này dẫn đến triển khai tất định sau:

```cpp
bool MillerRabin(u64 n) { // trả về true nếu n là số nguyên tố, nếu không trả về false.
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

Cũng có thể thực hiện kiểm tra chỉ với 7 cơ sở: 2, 325, 9375, 28178, 450775, 9780504 và 1795265022.
Tuy nhiên, vì các số này (ngoại trừ 2) không phải là số nguyên tố, bạn cần kiểm tra thêm xem số bạn đang kiểm tra có bằng bất kỳ ước nguyên tố nào của các cơ sở đó không: 2, 3, 5, 13, 19, 73, 193, 407521, 299210837.

## Bài tập luyện tập

- [SPOJ - Prime or Not](https://www.spoj.com/problems/PON/)
- [Project euler - Investigating a Prime Pattern](https://projecteuler.net/problem=146)