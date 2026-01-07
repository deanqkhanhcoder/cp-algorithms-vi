---
tags:
  - Original
---

# Lũy thừa nhị phân bằng cách phân tích

Xét bài toán tính $ax^y \pmod{2^d}$, cho các số nguyên $a$, $x$, $y$ và $d \geq 3$, trong đó $x$ là số lẻ.

Thuật toán dưới đây cho phép giải quyết bài toán này với $O(d)$ phép cộng và các phép toán nhị phân cùng một phép nhân duy nhất với $y$.

Do cấu trúc của nhóm nhân modulo $2^d$, bất kỳ số $x$ nào sao cho $x \equiv 1 \pmod 4$ đều có thể được biểu diễn dưới dạng

$$
x \equiv b^{L(x)} \pmod{2^d},
$$

trong đó $b \equiv 5 \pmod 8$. Không mất tính tổng quát, chúng ta giả sử rằng $x \equiv 1 \pmod 4$, vì chúng ta có thể quy $x \equiv 3 \pmod 4$ về $x \equiv 1 \pmod 4$ bằng cách thay thế $x \mapsto -x$ và $a \mapsto (-1)^{y} a$. Trong khái niệm này, $ax^y$ được biểu diễn là

$$
a x^y \equiv a b^{yL(x)} \pmod{2^d}.
$$

Ý tưởng cốt lõi của thuật toán là đơn giản hóa việc tính toán $L(x)$ và $b^{y L(x)}$ bằng cách sử dụng thực tế là chúng ta đang làm việc modulo $2^d$. Vì những lý do sẽ rõ ràng sau này, chúng ta sẽ làm việc với $4L(x)$ thay vì $L(x)$, nhưng lấy modulo $2^d$ thay vì $2^{d-2}$.

Trong bài viết này, chúng ta sẽ trình bày cách triển khai cho các số nguyên 32 bit. Đặt

* `mbin_log_32(r, x)` là một hàm tính $r+4L(x) \pmod{2^d}$;
* `mbin_exp_32(r, x)` là một hàm tính $r b^{\frac{x}{4}} \pmod{2^d}$;
* `mbin_power_odd_32(a, x, y)` là một hàm tính $ax^y \pmod{2^d}$.

Khi đó `mbin_power_odd_32` được triển khai như sau:

```cpp
uint32_t mbin_power_odd_32(uint32_t rem, uint32_t base, uint32_t exp) {
    if (base & 2) {
        /* số chia được coi là âm */
        base = -base;
        /* kiểm tra xem kết quả có nên là số âm không */
        if (exp & 1) {
            rem = -rem;
        }
    }
    return (mbin_exp_32(rem, mbin_log_32(0, base) * exp));
}
```

## Tính 4L(x) từ x

Cho $x$ là một số lẻ sao cho $x \equiv 1 \pmod 4$. Nó có thể được biểu diễn dưới dạng

$$
x \equiv (2^{a_1}+1)\dots(2^{a_k}+1) \pmod{2^d},
$$

trong đó $1 < a_1 < \dots < a_k < d$. Ở đây $L(\cdot)$ được định nghĩa rõ ràng cho mỗi nhân tử, vì chúng bằng $1$ modulo $4$. Do đó,

$$
4L(x) \equiv 4L(2^{a_1}+1)+\dots+4L(2^{a_k}+1) \pmod{2^{d}}.
$$

Vì vậy, nếu chúng ta tính trước $t_k = 4L(2^n+1)$ cho tất cả $1 < k < d$, chúng ta sẽ có thể tính $4L(x)$ cho bất kỳ số $x$ nào.

Đối với số nguyên 32 bit, chúng ta có thể sử dụng bảng sau:

```cpp
const uint32_t mbin_log_32_table[32] = {
    0x00000000, 0x00000000, 0xd3cfd984, 0x9ee62e18,
    0xe83d9070, 0xb59e81e0, 0xa17407c0, 0xce601f80,
    0xf4807f00, 0xe701fe00, 0xbe07fc00, 0xfc1ff800,
    0xf87ff000, 0xf1ffe000, 0xe7ffc000, 0xdfff8000,
    0xffff0000, 0xfffe0000, 0xfffc0000, 0xfff80000,
    0xfff00000, 0xffe00000, 0xffc00000, 0xff800000,
    0xff000000, 0xfe000000, 0xfc000000, 0xf8000000,
    0xf0000000, 0xe0000000, 0xc0000000, 0x80000000,
};
```

Trong thực tế, một cách tiếp cận hơi khác được sử dụng so với mô tả ở trên. Thay vì tìm phân tích thừa số cho $x$, chúng ta sẽ nhân liên tiếp $x$ với $2^n+1$ cho đến khi nó trở thành $1$ modulo $2^d$. Bằng cách này, chúng ta sẽ tìm thấy biểu diễn của $x^{-1}$, tức là

$$
x (2^{a_1}+1)\dots(2^{a_k}+1) \equiv 1 \pmod {2^d}.
$$

Để làm điều này, chúng ta lặp qua $n$ sao cho $1 < n < d$. Nếu $x$ hiện tại có bit thứ $n$ được bật, chúng ta nhân $x$ với $2^n+1$, điều này được thực hiện thuận tiện trong C++ là `x = x + (x << n)`. Điều này sẽ không thay đổi các bit thấp hơn $n$, nhưng sẽ biến bit thứ $n$ thành không, vì $x$ là số lẻ.

Với tất cả những điều này, hàm `mbin_log_32(r, x)` được triển khai như sau:

```cpp
uint32_t mbin_log_32(uint32_t r, uint32_t x) {
    uint8_t n;

    for (n = 2; n < 32; n++) {
        if (x & (1 << n)) {
            x = x + (x << n);
            r -= mbin_log_32_table[n];
        }
    }

    return r;
}
```

Lưu ý rằng $4L(x) = -4L(x^{-1})$, vì vậy thay vì cộng $4L(2^n+1)$, chúng ta trừ nó khỏi $r$, mà ban đầu bằng $0$.

## Tính x từ 4L(x)

Lưu ý rằng đối với $k \geq 1$ nó đúng rằng

$$
(a 2^{k}+1)^2 = a^2 2^{2k} +a 2^{k+1}+1 = b2^{k+1}+1,
$$

từ đó (bằng cách bình phương lặp đi lặp lại) chúng ta có thể suy ra rằng

$$
(2^a+1)^{2^b} \equiv 1 \pmod{2^{a+b}}.
$$

Áp dụng kết quả này cho $a=2^n+1$ và $b=d-k$, chúng ta suy ra rằng cấp nhân của $2^n+1$ là một ước của $2^{d-n}$.

Điều này, đến lượt nó, có nghĩa là $L(2^n+1)$ phải chia hết cho $2^{n}$, vì cấp của $b$ là $2^{d-2}$ và cấp của $b^y$ là $2^{d-2-v}$, trong đó $2^v$ là lũy thừa cao nhất của $2$ chia hết cho $y$, vì vậy chúng ta cần

$$
2^{d-k} \equiv 0 \pmod{2^{d-2-v}},
$$

do đó $v$ phải lớn hơn hoặc bằng $k-2$. Điều này hơi xấu và để giảm thiểu điều này, chúng ta đã nói ở đầu rằng chúng ta nhân $L(x)$ với $4$. Bây giờ nếu chúng ta biết $4L(x)$, chúng ta có thể phân rã duy nhất nó thành một tổng của $4L(2^n+1)$ bằng cách kiểm tra liên tiếp các bit trong $4L(x)$. Nếu bit thứ $n$ được đặt thành $1$, chúng ta sẽ nhân kết quả với $2^n+1$ và giảm $4L(x)$ hiện tại đi $4L(2^n+1)$.

Do đó, `mbin_exp_32` được triển khai như sau:

```cpp
uint32_t mbin_exp_32(uint32_t r, uint32_t x) {
    uint8_t n;

    for (n = 2; n < 32; n++) {
        if (x & (1 << n)) {
            r = r + (r << n);
            x -= mbin_log_32_table[n];
        }
    }

    return r;
}
```

## Tối ưu hóa thêm

Có thể giảm một nửa số lần lặp nếu bạn lưu ý rằng $4L(2^{d-1}+1)=2^{d-1}$ và đối với $2k \geq d$ nó đúng rằng

$$
(2^n+1)^2 \equiv 2^{2n} + 2^{n+1}+1 \equiv 2^{n+1}+1 \pmod{2^d},
$$

điều này cho phép suy ra rằng $4L(2^n+1)=2^n$ đối với $2n \geq d$. Vì vậy, bạn có thể đơn giản hóa thuật toán bằng cách chỉ đi đến $\frac{d}{2}$ và sau đó sử dụng thực tế ở trên để tính toán phần còn lại bằng các phép toán trên bit:

```cpp
uint32_t mbin_log_32(uint32_t r, uint32_t x) {
    uint8_t n;

    for (n = 2; n != 16; n++) {
        if (x & (1 << n)) {
            x = x + (x << n);
            r -= mbin_log_32_table[n];
        }
    }

    r -= (x & 0xFFFF0000);

    return r;
}

uint32_t mbin_exp_32(uint32_t r, uint32_t x) {
    uint8_t n;

    for (n = 2; n != 16; n++) {
        if (x & (1 << n)) {
            r = r + (r << n);
            x -= mbin_log_32_table[n];
        }
    }

    r *= 1 - (x & 0xFFFF0000);

    return r;
}
```

## Tính bảng logarit

Để tính bảng logarit, người ta có thể sửa đổi [thuật toán Pohlig–Hellman](https://en.wikipedia.org/wiki/Pohlig–Hellman_algorithm) cho trường hợp khi modulo là một lũy thừa của $2$.

Nhiệm vụ chính của chúng ta ở đây là tính $x$ sao cho $g^x \equiv y \pmod{2^d}$, trong đó $g=5$ và $y$ là một số loại $2^n+1$. 

Bình phương cả hai vế $k$ lần chúng ta đến

$$
g^{2^k x} \equiv y^{2^k} \pmod{2^d}.
$$

Lưu ý rằng cấp của $g$ không lớn hơn $2^{d}$ (trên thực tế, là $2^{d-2}$, nhưng chúng ta sẽ gắn với $2^d$ cho tiện), do đó sử dụng $k=d-1$ chúng ta sẽ có $g^1$ hoặc $g^0$ ở vế trái, điều này cho phép chúng ta xác định bit nhỏ nhất của $x$ bằng cách so sánh $y^{2^k}$ với $g$. Bây giờ giả sử rằng $x=x_0 + 2^k x_1$, trong đó $x_0$ là một phần đã biết và $x_1$ chưa được biết. Khi đó

$$
g^{x_0+2^k x_1} \equiv y \pmod{2^d}.
$$

Nhân cả hai vế với $g^{-x_0}$, chúng ta có được

$$
g^{2^k x_1} \equiv (g^{-x_0} y) \pmod{2^d}.
$$

Bây giờ, bình phương cả hai vế $d-k-1$ lần chúng ta có thể thu được bit tiếp theo của $x$, cuối cùng khôi phục tất cả các bit của nó.

## Tài liệu tham khảo

* [M30, Hans Petter Selasky, 2009](https://ia601602.us.archive.org/29/items/B-001-001-251/B-001-001-251.pdf#page=640)