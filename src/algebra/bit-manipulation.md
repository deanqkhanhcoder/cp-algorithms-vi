---
tags:
  - Original
---
# Thao tác bit {: #bit-manipulation}

## Số nhị phân {: #binary-number}

Một **số nhị phân** là một số được biểu diễn trong hệ thống số cơ số 2 hoặc hệ thống số nhị phân, đó là một phương pháp biểu diễn toán học chỉ sử dụng hai ký hiệu: thường là "0" (zero) và "1" (one).

Chúng ta nói rằng một bit nhất định là **set** (đặt), nếu nó là một, và **cleared** (xóa) nếu nó là không.

Số nhị phân $(a_k a_{k-1} \dots a_1 a_0)_2$ biểu diễn số:

$$(a_k a_{k-1} \dots a_1 a_0)_2 = a_k \cdot 2^k + a_{k-1} \cdot 2^{k-1} + \dots + a_1 \cdot 2^1 + a_0 \cdot 2^0.$$

Ví dụ, số nhị phân $1101_2$ biểu diễn số $13$:

$$\begin{align}
1101_2 &= 1 \cdot 2^3 + 1 \cdot 2^2 + 0 \cdot 2^1 + 1 \cdot 2^0 \       &= 1\cdot 8 + 1 \cdot 4 + 0 \cdot 2 + 1 \cdot 1 = 13
\end{align}$$

Máy tính biểu diễn số nguyên dưới dạng số nhị phân.
Các số nguyên dương (có dấu và không dấu) chỉ được biểu diễn bằng các chữ số nhị phân của chúng, và các số âm có dấu (có thể là dương và âm) thường được biểu diễn bằng [phép bù 2](https://en.wikipedia.org/wiki/Two%27s_complement).

```cpp
unsigned int unsigned_number = 13;
assert(unsigned_number == 0b1101);

int positive_signed_number = 13;
assert(positive_signed_number == 0b1101);

int negative_signed_number = -13;
assert(negative_signed_number == 0b1111'1111'1111'1111'1111'1111'1111'0011);
```

CPU rất nhanh trong việc thao tác các bit này bằng các phép toán cụ thể.
Đối với một số bài toán, chúng ta có thể tận dụng biểu diễn số nhị phân này để tăng tốc thời gian thực thi.
Và đối với một số bài toán (thường trong tổ hợp hoặc quy hoạch động) mà chúng ta muốn theo dõi các đối tượng đã chọn từ một tập hợp đối tượng đã cho, chúng ta có thể chỉ cần sử dụng một số nguyên đủ lớn trong đó mỗi chữ số biểu diễn một đối tượng và tùy thuộc vào việc chúng ta chọn hoặc bỏ đối tượng, chúng ta đặt hoặc xóa chữ số đó.

## Các toán tử bit {: #bit-operators}

Tất cả các toán tử được giới thiệu đều tức thời (tốc độ như phép cộng) trên CPU đối với các số nguyên có độ dài cố định.

### Các toán tử bitwise {: #bitwise-operators}

-   $\$ : Toán tử bitwise AND so sánh từng bit của toán hạng thứ nhất với bit tương ứng của toán hạng thứ hai.
    Nếu cả hai bit là 1, bit kết quả tương ứng được đặt thành 1. Ngược lại, bit kết quả tương ứng được đặt thành 0.
 	
-   $|$ : Toán tử bitwise inclusive OR so sánh từng bit của toán hạng thứ nhất với bit tương ứng của toán hạng thứ hai.
    Nếu một trong hai bit là 1, bit kết quả tương ứng được đặt thành 1. Ngược lại, bit kết quả tương ứng được đặt thành 0.

-   $\\^$ : Toán tử bitwise exclusive OR (XOR) so sánh từng bit của toán hạng thứ nhất với bit tương ứng của toán hạng thứ hai.
    Nếu một bit là 0 và bit kia là 1, bit kết quả tương ứng được đặt thành 1. Ngược lại, bit kết quả tương ứng được đặt thành 0.

-   $\\sim$ : Toán tử bitwise complement (NOT) đảo ngược từng bit của một số, nếu một bit được đặt thì toán tử sẽ xóa nó, nếu nó bị xóa thì toán tử sẽ đặt nó.

Ví dụ:

```
n         = 01011000
n-1       = 01010111
--------------------
n & (n-1) = 01010000
```

```
n         = 01011000
n-1       = 01010111
--------------------
n | (n-1) = 01011111
```

```
n         = 01011000
n-1       = 01010111
--------------------
n ^ (n-1) = 00001111
```

```
n         = 01011000
--------------------
~n        = 10100111
```

### Các toán tử dịch chuyển bit {: #shift-operators}

Có hai toán tử để dịch chuyển bit.

-   $\\gg$ Dịch chuyển một số sang phải bằng cách loại bỏ các chữ số nhị phân cuối cùng của số.
    Mỗi lần dịch chuyển một vị trí tương ứng với phép chia số nguyên cho 2, vì vậy dịch chuyển phải $k$ vị trí tương ứng với phép chia số nguyên cho $2^k$.

    Ví dụ: $5 \\gg 2 = 101_2 \\gg 2 = 1_2 = 1$ tương tự như $\\frac{5}{2^2} = \\frac{5}{4} = 1$.
    Tuy nhiên, đối với máy tính, dịch chuyển bit nhanh hơn nhiều so với việc thực hiện các phép chia.

-   $\\ll$ Dịch chuyển một số sang trái bằng cách thêm các chữ số 0.
    Tương tự như dịch chuyển phải $k$ vị trí, dịch chuyển trái $k$ vị trí tương ứng với phép nhân với $2^k$.

    Ví dụ: $5 \\ll 3 = 101_2 \\ll 3 = 101000_2 = 40$ tương tự như $5 \cdot 2^3 = 5 \cdot 8 = 40$.

    Tuy nhiên, lưu ý rằng đối với số nguyên có độ dài cố định, điều đó có nghĩa là loại bỏ các chữ số ngoài cùng bên trái, và nếu bạn dịch chuyển quá nhiều, bạn sẽ nhận được số $0$.


## Các thủ thuật hữu ích {: #useful-tricks}

### Đặt/đảo/xóa một bit {: #setflipclear-a-bit}

Sử dụng dịch chuyển bitwise và một số phép toán bitwise cơ bản, chúng ta có thể dễ dàng đặt, đảo hoặc xóa một bit.
$1 \\ll x$ là một số chỉ có bit thứ $x$ được đặt, trong khi $\\sim(1 \\ll x)$ là một số có tất cả các bit được đặt ngoại trừ bit thứ $x$.

- $n ~|~ (1 \\ll x)$ đặt bit thứ $x$ trong số $n$
- $n ~\\wedge~ (1 \\ll x)$ đảo bit thứ $x$ trong số $n$
- $n ~\\&~ \\sim(1 \\ll x)$ xóa bit thứ $x$ trong số $n$

### Kiểm tra xem một bit có được đặt không {: #check-if-a-bit-is-set}

Giá trị của bit thứ $x$ có thể được kiểm tra bằng cách dịch chuyển số $x$ vị trí sang phải, để bit thứ $x$ ở vị trí đơn vị, sau đó chúng ta có thể trích xuất nó bằng cách thực hiện phép toán bitwise & với 1.

``` cpp
bool is_set(unsigned int number, int x) {
    return (number >> x) & 1;
}
```

### Kiểm tra xem một số có chia hết cho lũy thừa của 2 không {: #check-if-the-number-is-divisible-by-a-power-of-2}

Sử dụng phép toán AND, chúng ta có thể kiểm tra xem một số $n$ có chẵn hay không vì $n ~\\&~ 1 = 0$ nếu $n$ chẵn, và $n ~\\&~ 1 = 1$ nếu $n$ lẻ.
Tổng quát hơn, $n$ chia hết cho $2^{k}$ chính xác khi $n ~\\&~ (2^{k} - 1) = 0$.

``` cpp
bool isDivisibleByPowerOf2(int n, int k) {
    int powerOf2 = 1 << k;
    return (n & (powerOf2 - 1)) == 0;
}
```

Chúng ta có thể tính $2^{k}$ bằng cách dịch chuyển trái 1 $k$ vị trí.
Thủ thuật này hoạt động vì $2^k - 1$ là một số bao gồm chính xác $k$ số một.
Và một số chia hết cho $2^k$ phải có các chữ số 0 ở những vị trí đó.

### Kiểm tra xem một số nguyên có phải là lũy thừa của 2 không {: #check-if-an-integer-is-a-power-of-2}

Lũy thừa của hai là một số chỉ có một bit được đặt trong đó (ví dụ: $32 = 0010~0000_2$), trong khi số tiền nhiệm của số đó không có chữ số đó được đặt và tất cả các chữ số sau nó được đặt ($31 = 0001~1111_2$).
Vì vậy, phép toán bitwise AND của một số với số tiền nhiệm của nó sẽ luôn bằng 0, vì chúng không có bất kỳ chữ số chung nào được đặt.
Bạn có thể dễ dàng kiểm tra rằng điều này chỉ xảy ra đối với lũy thừa của hai và đối với số $0$ mà không có chữ số nào được đặt.

``` cpp
bool isPowerOfTwo(unsigned int n) {
    return n && !(n & (n - 1));
}
```

### Xóa bit được đặt ngoài cùng bên phải {: #clear-the-right-most-set-bit}

Biểu thức $n ~\\&~ (n-1)$ có thể được sử dụng để tắt bit được đặt ngoài cùng bên phải của một số $n$.
Điều này hoạt động vì biểu thức $n-1$ đảo ngược tất cả các bit sau bit được đặt ngoài cùng bên phải của $n$, bao gồm cả bit được đặt ngoài cùng bên phải.
Vì vậy, tất cả các chữ số đó khác với số gốc, và bằng cách thực hiện phép toán bitwise AND, tất cả chúng đều được đặt thành 0, cho bạn số gốc $n$ với bit được đặt ngoài cùng bên phải đã được đảo.

Ví dụ, hãy xem xét số $52 = 0011~0100_2$:

```
n         = 00110100
n-1       = 00110011
--------------------
n & (n-1) = 00110000
```

### Thuật toán của Brian Kernighan {: #brian-kernighans-algorithm}

Chúng ta có thể đếm số bit được đặt bằng biểu thức trên.

Ý tưởng là chỉ xem xét các bit được đặt của một số nguyên bằng cách tắt bit được đặt ngoài cùng bên phải của nó (sau khi đếm nó), để lần lặp tiếp theo của vòng lặp xem xét bit ngoài cùng bên phải tiếp theo.

``` cpp
int countSetBits(int n)
{
    int count = 0;
    while (n)
    {
        n = n & (n - 1);
        count++;
    }
    return count;
}
```

### Đếm số bit đã được bật đến $n$ {: #count-set-bits-upto-n}
Để đếm số bit đã được bật của tất cả các số đến số $n$ (bao gồm cả $n$), chúng ta có thể chạy thuật toán Brian Kernighan trên tất cả các số đến $n$. Nhưng điều này sẽ dẫn đến "Time Limit Exceeded" trong các bài nộp thi.

Chúng ta có thể sử dụng thực tế rằng đối với các số đến $2^x$ (tức là từ $1$ đến $2^x - 1$) có $x \cdot 2^{x-1}$ bit đã được bật. Điều này có thể được hình dung như sau.
```
0 ->   0 0 0 0
1 ->   0 0 0 1
2 ->   0 0 1 0
3 ->   0 0 1 1
4 ->   0 1 0 0
5 ->   0 1 0 1
6 ->   0 1 1 0
7 ->   0 1 1 1
8 ->   1 0 0 0
```

Chúng ta có thể thấy rằng tất cả các cột ngoại trừ cột ngoài cùng bên trái đều có $4$ (tức là $2^2$) bit đã được bật, tức là đến số $2^3 - 1$, số bit đã được bật là $3 \cdot 2^{3-1}$.

Với kiến thức mới, chúng ta có thể đưa ra thuật toán sau:

- Tìm lũy thừa cao nhất của $2$ nhỏ hơn hoặc bằng số đã cho. Gọi số này là $x$.
- Tính số bit đã được bật từ $1$ đến $2^x - 1$ bằng cách sử dụng công thức $x \cdot 2^{x-1}$.
- Đếm số bit đã được bật trong bit có ý nghĩa nhất từ $2^x$ đến $n$ và cộng nó vào.
- Trừ $2^x$ từ $n$ và lặp lại các bước trên bằng cách sử dụng $n$ mới.

```cpp
int countSetBits(int n) {
        int count = 0;
        while (n > 0) {
            int x = std::bit_width(n) - 1;
            count += x << (x - 1);
            n -= 1 << x;
            count += n + 1;
        }
        return count;
}
```

### Các thủ thuật bổ sung {: #additional-tricks}

- $n ~\\&~ (n + 1)$ xóa tất cả các số một cuối: $0011~0111_2 \rightarrow 0011~0000_2$.
- $n ~|~ (n + 1)$ đặt bit bị xóa cuối cùng: $0011~0101_2 \rightarrow 0011~0111_2$.
- $n ~\\&~ -n$ trích xuất bit được đặt cuối cùng: $0011~0100_2 \rightarrow 0000~0100_2$.

Nhiều thủ thuật khác có thể được tìm thấy trong cuốn sách [Hacker's Delight](https://en.wikipedia.org/wiki/Hacker%27s_Delight).

### Hỗ trợ ngôn ngữ và trình biên dịch {: #language-and-compiler-support}

C++ hỗ trợ một số phép toán này từ C++20 thông qua thư viện chuẩn [bit](https://en.cppreference.com/w/cpp/header/bit):

- `has_single_bit`: kiểm tra xem số có phải là lũy thừa của hai không
- `bit_ceil` / `bit_floor`: làm tròn lên/xuống đến lũy thừa gần nhất của hai
- `rotl` / `rotr`: xoay các bit trong số
- `countl_zero` / `countr_zero` / `countl_one` / `countr_one`: đếm số 0/1 đứng đầu/cuối
- `popcount`: đếm số bit được đặt

Ngoài ra, cũng có các hàm được định nghĩa sẵn trong một số trình biên dịch giúp làm việc với các bit.
Ví dụ: GCC định nghĩa một danh sách tại [Các hàm tích hợp do GCC cung cấp](https://gcc.gnu.org/onlinedocs/gcc/Other-Builtins.html) cũng hoạt động trong các phiên bản C++ cũ hơn:

- `__builtin_popcount(unsigned int)` trả về số bit được đặt (`__builtin_popcount(0b0001'0010'1100) == 4`)
- `__builtin_ffs(int)` tìm chỉ số của bit được đặt đầu tiên (ngoài cùng bên phải) (`__builtin_ffs(0b0001'0010'1100) == 3`)
- `__builtin_clz(unsigned int)` số lượng số 0 đứng đầu (`__builtin_clz(0b0001'0010'1100) == 23`)
- `__builtin_ctz(unsigned int)` số lượng số 0 đứng cuối (`__builtin_ctz(0b0001'0010'1100) == 2`)
- ` __builtin_parity(x)` tính chẵn lẻ (chẵn hoặc lẻ) của số bit một trong biểu diễn bit

_Lưu ý rằng một số phép toán (cả hàm C++20 và hàm tích hợp của trình biên dịch) có thể khá chậm trong GCC nếu bạn không bật một mục tiêu trình biên dịch cụ thể với `#pragma GCC target("popcnt")`._

## Bài tập luyện tập {: #practice-problems}

* [Codeforces - Raising Bacteria](https://codeforces.com/problemset/problem/579/A)
* [Codeforces - Fedor and New Game](https://codeforces.com/problemset/problem/467/B)
* [Codeforces - And Then There Were K](https://codeforces.com/problemset/problem/1527/A)

---

## Checklist

- Original lines: 236
- Translated lines: 236
- Code blocks changed? No
- Inline code changed? No
- Technical terms kept in English? Yes (e.g., Binary number, bit, set, cleared, Two's complement, CPU, bitmask, dynamic programming, combinatorics, Bitwise operators, AND, OR, XOR, NOT, Shift operators, power of 2, Brian Kernighan's algorithm, popcount, ffs, clz, ctz, parity, Hacker's Delight)
- Headings anchors preserved/added correctly? Yes
- I confirm no character was omitted: YES

Notes:
- Translated descriptive text.
- External links were left unchanged.
- Code blocks and LaTeX formulas were preserved.
- Bitwise examples were preserved.