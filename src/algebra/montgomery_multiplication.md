---
tags:
  - Original
---

# Phép nhân Montgomery (Montgomery Multiplication) {: #montgomery-multiplication}

Nhiều thuật toán trong lý thuyết số, như [kiểm tra số nguyên tố](primality_tests.md) hoặc [phân tích thừa số nguyên](factorization.md), và trong mật mã, như RSA, yêu cầu rất nhiều phép toán modulo với một số lớn.
Một phép nhân như $x y \bmod{n}$ khá chậm để tính toán với các thuật toán điển hình, vì nó yêu cầu một phép chia để biết $n$ phải được trừ bao nhiêu lần từ tích.
Và phép chia là một phép toán thực sự đắt đỏ, đặc biệt là với các số lớn.

**Phép nhân Montgomery (modular)** là một phương pháp cho phép tính toán các phép nhân như vậy nhanh hơn.
Thay vì chia tích và trừ $n$ nhiều lần, nó cộng các bội số của $n$ để triệt tiêu các bit thấp hơn và sau đó chỉ loại bỏ các bit thấp hơn.

## Biểu diễn Montgomery (Montgomery representation) {: #montgomery-representation}

Tuy nhiên, phép nhân Montgomery không miễn phí.
Thuật toán chỉ hoạt động trong **không gian Montgomery**.
Và chúng ta cần chuyển đổi các số của mình vào không gian đó, trước khi chúng ta có thể bắt đầu nhân.

Đối với không gian, chúng ta cần một số nguyên dương $r \ge n$ nguyên tố cùng nhau với $n$, tức là $\gcd(n, r) = 1$.
Trong thực tế, chúng ta luôn chọn $r$ là $2^m$ cho một số nguyên dương $m$, vì các phép nhân, phép chia và phép toán modulo $r$ sau đó có thể được cài đặt hiệu quả bằng cách sử dụng phép dịch và các phép toán bit khác.
$n$ sẽ là một số lẻ trong hầu hết các ứng dụng, vì không khó để phân tích thừa số một số chẵn.
Vì vậy, mỗi lũy thừa của $2$ sẽ là nguyên tố cùng nhau với $n$.

Đại diện $\bar{x}$ của một số $x$ trong không gian Montgomery được định nghĩa là: 

$$\bar{x} := x \cdot r \bmod n$$

Lưu ý, phép chuyển đổi thực sự là một phép nhân như vậy mà chúng ta muốn tối ưu hóa.
Vì vậy, đây vẫn là một hoạt động đắt đỏ.
Tuy nhiên, bạn chỉ cần chuyển đổi một số một lần vào không gian.
Ngay khi bạn ở trong không gian Montgomery, bạn có thể thực hiện bao nhiêu phép toán tùy ý một cách hiệu quả.
Và cuối cùng bạn chuyển đổi kết quả cuối cùng trở lại.
Vì vậy, miễn là bạn đang thực hiện nhiều phép toán modulo $n$, điều này sẽ không thành vấn đề.

Bên trong không gian Montgomery, bạn vẫn có thể thực hiện hầu hết các phép toán như bình thường.
Bạn có thể cộng hai phần tử ($x \cdot r + y \cdot r \equiv (x + y) \cdot r \bmod n$), trừ, kiểm tra sự bằng nhau, và thậm chí tính ước chung lớn nhất của một số với $n$ (vì $\gcd(n, r) = 1$).
Tất cả với các thuật toán thông thường.

Tuy nhiên điều này không đúng đối với phép nhân.

Chúng ta mong đợi kết quả là:

$$\bar{x} * \bar{y} = \overline{x \cdot y} = (x \cdot y) \cdot r \bmod n.$$

Nhưng phép nhân thông thường sẽ cho chúng ta:

$$\bar{x} \cdot \bar{y} = (x \cdot y) \cdot r \cdot r \bmod n.$$

Do đó phép nhân trong không gian Montgomery được định nghĩa là:

$$\bar{x} * \bar{y} := \bar{x} \cdot \bar{y} \cdot r^{-1} \bmod n.$$

## Rút gọn Montgomery (Montgomery reduction) {: #montgomery-reduction}

Phép nhân của hai số trong không gian Montgomery yêu cầu tính toán hiệu quả $x \cdot r^{-1} \bmod n$.
Phép toán này được gọi là **Rút gọn Montgomery**, và còn được gọi là thuật toán **REDC**.

Bởi vì $\gcd(n, r) = 1$, chúng ta biết rằng có hai số $r^{-1}$ và $n^{\prime}$ với $0 < r^{-1}, n^{\prime} < n$ với

$$r \cdot r^{-1} + n \cdot n^{\prime} = 1.$$

Cả $r^{-1}$ và $n^{\prime}$ đều có thể được tính bằng cách sử dụng [Thuật toán Euclid mở rộng](extended-euclid-algorithm.md).

Sử dụng đồng nhất thức này, chúng ta có thể viết $x \cdot r^{-1}$ dưới dạng:

$$\begin{aligned}
x \cdot r^{-1} &= x \cdot r \cdot r^{-1} / r = x \cdot (-n \cdot n^{\prime} + 1) / r \\
&= (-x \cdot n \cdot n^{\prime} + x) / r \equiv (-x \cdot n \cdot n^{\prime} + l \cdot r \cdot n + x) / r \bmod n\\
&\equiv ((-x \cdot n^{\prime} + l \cdot r) \cdot n + x) / r \bmod n
\end{aligned}$$

Sự tương đương giữ cho bất kỳ số nguyên tùy ý $l$.
Điều này có nghĩa là, chúng ta có thể cộng hoặc trừ một bội số tùy ý của $r$ vào $x \cdot n^{\prime}$, hoặc nói cách khác, chúng ta có thể tính $q := x \cdot n^{\prime}$ modulo $r$.

Điều này cho chúng ta thuật toán sau để tính $x \cdot r^{-1} \bmod n$:

```text
function reduce(x):
    q = (x mod r) * n' mod r
    a = (x - q * n) / r
    if a < 0:
        a += n
    return a
```

Vì $x < n \cdot n < r \cdot n$ (ngay cả khi $x$ là tích của một phép nhân) và $q \cdot n < r \cdot n$ chúng ta biết rằng $-n < (x - q \cdot n) / r < n$.
Do đó phép toán modulo cuối cùng được cài đặt bằng cách sử dụng một lần kiểm tra và một phép cộng.

Như chúng ta thấy, chúng ta có thể thực hiện rút gọn Montgomery mà không cần bất kỳ phép toán modulo nặng nề nào.
Nếu chúng ta chọn $r$ là lũy thừa của $2$, các phép toán modulo và chia trong thuật toán có thể được tính toán bằng cách sử dụng bitmask và dịch.

Một ứng dụng thứ hai của rút gọn Montgomery là chuyển một số trở lại từ không gian Montgomery vào không gian bình thường.

## Mẹo nghịch đảo nhanh (Fast inverse trick) {: #fast-inverse-trick}

Để tính toán nghịch đảo $n^{\prime} := n^{-1} \bmod r$ một cách hiệu quả, chúng ta có thể sử dụng mẹo sau (được lấy cảm hứng từ phương pháp Newton):

$$a \cdot x \equiv 1 \bmod 2^k \Longrightarrow a \cdot x \cdot (2 - a \cdot x) \equiv 1 \bmod 2^{2k}$$

Điều này có thể dễ dàng được chứng minh.
Nếu chúng ta có $a \cdot x = 1 + m \cdot 2^k$, thì chúng ta có:

$$\begin{aligned}
a \cdot x \cdot (2 - a \cdot x) &= 2 \cdot a \cdot x - (a \cdot x)^2 \\
&= 2 \cdot (1 + m \cdot 2^k) - (1 + m \cdot 2^k)^2 \\
&= 2 + 2 \cdot m \cdot 2^k - 1 - 2 \cdot m \cdot 2^k - m^2 \cdot 2^{2k} \\
&= 1 - m^2 \cdot 2^{2k} \\
&\equiv 1 \bmod 2^{2k}.
\end{aligned}$$

Điều này có nghĩa là chúng ta có thể bắt đầu với $x = 1$ là nghịch đảo của $a$ modulo $2^1$, áp dụng mẹo một vài lần và trong mỗi lần lặp, chúng ta nhân đôi số bit chính xác của $x$.

## Cài đặt (Implementation) {: #implementation}

Sử dụng trình biên dịch GCC, chúng ta vẫn có thể tính $x \cdot y \bmod n$ một cách hiệu quả, khi cả ba số đều là số nguyên 64 bit, vì trình biên dịch hỗ trợ số nguyên 128 bit với các kiểu `__int128` và `__uint128`.

```cpp
long long result = (__int128)x * y % n;
```

Tuy nhiên không có kiểu nào cho số nguyên 256 bit.
Do đó, ở đây chúng tôi sẽ trình bày một cài đặt cho phép nhân 128 bit.

```cpp
using u64 = uint64_t;
using u128 = __uint128_t;
using i128 = __int128_t;

struct u256 {
    u128 high, low;

    static u256 mult(u128 x, u128 y) {
        u64 a = x >> 64, b = x;
        u64 c = y >> 64, d = y;
        // (a*2^64 + b) * (c*2^64 + d) =
        // (a*c) * 2^128 + (a*d + b*c)*2^64 + (b*d)
        u128 ac = (u128)a * c;
        u128 ad = (u128)a * d;
        u128 bc = (u128)b * c;
        u128 bd = (u128)b * d;
        u128 carry = (u128)(u64)ad + (u128)(u64)bc + (bd >> 64u);
        u128 high = ac + (ad >> 64u) + (bc >> 64u) + (carry >> 64u);
        u128 low = (ad << 64u) + (bc << 64u) + bd;
        return {high, low};
    }
};

struct Montgomery {
    Montgomery(u128 n) : mod(n), inv(1) {
        for (int i = 0; i < 7; i++)
            inv *= 2 - n * inv;
    }

    u128 init(u128 x) {
        x %= mod;
        for (int i = 0; i < 128; i++) {
            x <<= 1;
            if (x >= mod)
                x -= mod;
        }
        return x;
    }

    u128 reduce(u256 x) {
        u128 q = x.low * inv;
        i128 a = x.high - u256::mult(q, mod).high;
        if (a < 0)
            a += mod;
        return a;
    }

    u128 mult(u128 a, u128 b) {
        return reduce(u256::mult(a, b));
    }

    u128 mod, inv;
};
```

## Biến đổi nhanh (Fast transformation) {: #fast-transformation}

Phương pháp hiện tại để chuyển đổi một số vào không gian Montgomery khá chậm.
Có những cách nhanh hơn.

Bạn có thể nhận thấy mối quan hệ sau:

$$\bar{x} := x \cdot r \bmod n = x \cdot r^2 / r = x * r^2$$

Chuyển đổi một số vào không gian chỉ là một phép nhân bên trong không gian của số đó với $r^2$.
Do đó, chúng ta có thể tính trước $r^2 \bmod n$ và chỉ cần thực hiện phép nhân thay vì dịch số 128 lần.

Trong mã sau, chúng ta khởi tạo `r2` với `-n % n`, tương đương với $r - n \equiv r \bmod n$, dịch nó 4 lần để nhận được $r \cdot 2^4 \bmod n$.
Số này có thể được hiểu là $2^4$ trong không gian Montgomery.
Nếu chúng ta bình phương nó $5$ lần, chúng ta nhận được $(2^4)^{2^5} = (2^4)^{32} = 2^{128} = r$ trong không gian Montgomery, chính xác là $r^2 \bmod n$.

```
struct Montgomery {
    Montgomery(u128 n) : mod(n), inv(1), r2(-n % n) {
        for (int i = 0; i < 7; i++)
            inv *= 2 - n * inv;

        for (int i = 0; i < 4; i++) {
            r2 <<= 1;
            if (r2 >= mod)
                r2 -= mod;
        }
        for (int i = 0; i < 5; i++)
            r2 = mul(r2, r2);
    }

    u128 init(u128 x) {
        return mult(x, r2);
    }

    u128 mod, inv, r2;
};
```

---

## Checklist

- Original lines: 220
- Translated lines: 220
- Code blocks changed? No
- Inline code changed? No
- Technical terms kept in English? Yes
- Headings anchors preserved/added correctly? Yes
- I confirm no character was omitted: YES
