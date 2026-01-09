---
tags:
  - Original
---
# Thao tác bit (Bit manipulation) {: #bit-manipulation}

## Số nhị phân (Binary number) {: #binary-number}

Một **số nhị phân** là một số được biểu diễn trong hệ đếm cơ số 2 hay hệ đếm nhị phân, nó là một phương pháp biểu diễn toán học chỉ sử dụng hai ký hiệu: thường là "0" (không) và "1" (một).

Chúng ta nói rằng một bit nhất định là **bật** (set), nếu nó là một, và **tắt** (cleared) nếu nó là không.

Số nhị phân $(a_k a_{k-1} \dots a_1 a_0)_2$ biểu diễn số:

$$(a_k a_{k-1} \dots a_1 a_0)_2 = a_k \cdot 2^k + a_{k-1} \cdot 2^{k-1} + \dots + a_1 \cdot 2^1 + a_0 \cdot 2^0.$$

Ví dụ số nhị phân $1101_2$ biểu diễn số $13$:

$$\begin{align}
1101_2 &= 1 \cdot 2^3 + 1 \cdot 2^2 + 0 \cdot 2^1 + 1 \cdot 2^0 \\
       &= 1\cdot 8 + 1 \cdot 4 + 0 \cdot 2 + 1 \cdot 1 = 13
\end{align}$$

Máy tính biểu diễn các số nguyên dưới dạng số nhị phân.
Các số nguyên dương (cả có dấu và không dấu) chỉ được biểu diễn bằng các chữ số nhị phân của chúng, và các số có dấu âm (có thể dương và âm) thường được biểu diễn bằng [Bù hai](https://en.wikipedia.org/wiki/Two%27s_complement) (Two's complement).

```cpp
unsigned int unsigned_number = 13;
assert(unsigned_number == 0b1101);

int positive_signed_number = 13;
assert(positive_signed_number == 0b1101);

int negative_signed_number = -13;
assert(negative_signed_number == 0b1111'1111'1111'1111'1111'1111'1111'0011);
```

CPU thao tác các bit này rất nhanh với các phép toán cụ thể.
Đối với một số bài toán, chúng ta có thể tận dụng các biểu diễn số nhị phân này và tăng tốc thời gian thực thi.
Và đối với một số bài toán (thường là trong tổ hợp hoặc quy hoạch động) nơi chúng ta muốn theo dõi các đối tượng chúng ta đã chọn từ một tập hợp các đối tượng nhất định, chúng ta chỉ cần sử dụng một số nguyên đủ lớn trong đó mỗi chữ số đại diện cho một đối tượng và tùy thuộc vào việc chúng ta chọn hay bỏ đối tượng, chúng ta bật hoặc tắt chữ số đó.

## Các toán tử bit (Bit operators) {: #bit-operators}

Tất cả các toán tử được giới thiệu sau đây là tức thì (cùng tốc độ với phép cộng) trên CPU cho các số nguyên có độ dài cố định.

### Các toán tử bitwise (Bitwise operators) {: #bitwise-operators}

-   $\&$ : Toán tử AND bitwise so sánh từng bit của toán hạng đầu tiên với bit tương ứng của toán hạng thứ hai.
    Nếu cả hai bit đều là 1, bit kết quả tương ứng được đặt thành 1. Ngược lại, bit kết quả tương ứng được đặt thành 0.
 	
-   $|$ : Toán tử OR bitwise (bao hàm) so sánh từng bit của toán hạng đầu tiên với bit tương ứng của toán hạng thứ hai.
    Nếu một trong hai bit là 1, bit kết quả tương ứng được đặt thành 1. Ngược lại, bit kết quả tương ứng được đặt thành 0.

-   $\wedge$ : Toán tử XOR bitwise (loại trừ) so sánh từng bit của toán hạng đầu tiên với bit tương ứng của toán hạng thứ hai.
    Nếu một bit là 0 và bit kia là 1, bit kết quả tương ứng được đặt thành 1. Ngược lại, bit kết quả tương ứng được đặt thành 0.

-   $\sim$ : Toán tử NOT bitwise (bù) lật từng bit của một số, nếu một bit đang bật toán tử sẽ tắt nó, nếu nó đang tắt toán tử sẽ bật nó.

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

### Các toán tử dịch (Shift operators) {: #shift-operators}

Có hai toán tử để dịch bit.

-   $\gg$ Dịch một số sang phải bằng cách loại bỏ vài chữ số nhị phân cuối cùng của số.
    Mỗi lần dịch một bit tương ứng với phép chia nguyên cho 2, vì vậy dịch phải $k$ lần tương ứng với phép chia nguyên cho $2^k$.

    V.d. $5 \gg 2 = 101_2 \gg 2 = 1_2 = 1$ giống như $\frac{5}{2^2} = \frac{5}{4} = 1$.
    Tuy nhiên đối với máy tính, việc dịch một số bit nhanh hơn nhiều so với thực hiện phép chia.

-   $\ll$ Dịch một số sang trái bằng cách thêm vào các chữ số không.
    Tương tự như dịch phải $k$ lần, dịch trái $k$ lần tương ứng với phép nhân với $2^k$.

    V.d. $5 \ll 3 = 101_2 \ll 3 = 101000_2 = 40$ giống như $5 \cdot 2^3 = 5 \cdot 8 = 40$.

    Tuy nhiên hãy chú ý rằng đối với số nguyên có độ dài cố định, điều đó có nghĩa là loại bỏ các chữ số bên trái nhất, và nếu bạn dịch quá nhiều, bạn sẽ nhận được số $0$.


## Các thủ thuật hữu ích {: #useful-tricks}

### Bật/lật/tắt một bit {: #set-flip-clear-a-bit}

Sử dụng các phép dịch bit và một số phép toán bitwise cơ bản, chúng ta có thể dễ dàng bật, lật hoặc tắt một bit.
$1 \ll x$ là số chỉ có bit thứ $x$ bật, trong khi $\sim(1 \ll x)$ là số có tất cả các bit bật ngoại trừ bit thứ $x$.

- $n ~|~ (1 \ll x)$ bật bit thứ $x$ trong số $n$
- $n ~\wedge~ (1 \ll x)$ lật bit thứ $x$ trong số $n$
- $n ~\&~ \sim(1 \ll x)$ tắt bit thứ $x$ trong số $n$

### Kiểm tra một bit có bật không {: #check-if-a-bit-is-set}

Giá trị của bit thứ $x$ có thể được kiểm tra bằng cách dịch số $x$ vị trí sang phải, sao cho bit thứ $x$ ở vị trí đơn vị, sau đó chúng ta có thể trích xuất nó bằng cách thực hiện phép AND bitwise với 1.

``` cpp
bool is_set(unsigned int number, int x) {
    return (number >> x) & 1;
}
```

### Kiểm tra số có chia hết cho lũy thừa của 2 không {: #check-if-the-number-is-divisible-by-a-power-of-2}

Sử dụng phép AND, chúng ta có thể kiểm tra xem số $n$ có chẵn hay không vì $n ~\&~ 1 = 0$ nếu $n$ chẵn, và $n ~\&~ 1 = 1$ nếu $n$ lẻ.
Tổng quát hơn, $n$ chia hết cho $2^{k}$ chính xác khi $n ~\&~ (2^{k} − 1) = 0$.

``` cpp
bool isDivisibleByPowerOf2(int n, int k) {
    int powerOf2 = 1 << k;
    return (n & (powerOf2 - 1)) == 0;
}
```

Chúng ta có thể tính $2^{k}$ bằng cách dịch trái 1 đi $k$ vị trí.
Thủ thuật này hoạt động, bởi vì $2^k - 1$ là số bao gồm đúng $k$ số một.
Và một số chia hết cho $2^k$ phải có các chữ số không ở những vị trí đó.

### Kiểm tra một số nguyên có phải là lũy thừa của 2 không {: #check-if-an-integer-is-a-power-of-2}

Lũy thừa của hai là một số chỉ có một bit duy nhất trong đó (ví dụ $32 = 0010~0000_2$), trong khi số liền trước của số đó có chữ số đó không bật và tất cả các chữ số sau nó đều bật ($31 = 0001~1111_2$).
Vì vậy phép AND bitwise của một số với số liền trước của nó sẽ luôn là 0, vì chúng không có bất kỳ chữ số chung nào bật.
Bạn có thể dễ dàng kiểm tra rằng điều này chỉ xảy ra đối với các lũy thừa của hai và số $0$ vốn đã không có chữ số nào bật.

``` cpp
bool isPowerOfTwo(unsigned int n) {
    return n && !(n & (n - 1));
}
```

### Tắt bit bật ngoài cùng bên phải {: #clear-the-right-most-set-bit}

Biểu thức $n ~\&~ (n-1)$ có thể được sử dụng để tắt bit bật ngoài cùng bên phải của số $n$.
Điều này hoạt động vì biểu thức $n-1$ lật tất cả các bit sau bit bật ngoài cùng bên phải của $n$, bao gồm cả bit bật ngoài cùng bên phải.
Vì vậy tất cả các chữ số đó đều khác với số ban đầu, và bằng cách thực hiện phép AND bitwise, chúng đều được đặt thành 0, cho bạn số ban đầu $n$ với bit bật ngoài cùng bên phải đã bị lật.

Ví dụ, xem xét số $52 = 0011~0100_2$:

```
n         = 00110100
n-1       = 00110011
--------------------
n & (n-1) = 00110000
```

### Thuật toán Brian Kernighan {: #brian-kernighans-algorithm}

Chúng ta có thể đếm số lượng bit bật bằng biểu thức trên.

Ý tưởng là chỉ xem xét các bit bật của một số nguyên bằng cách tắt bit bật ngoài cùng bên phải của nó (sau khi đếm nó), vì vậy lần lặp tiếp theo của vòng lặp sẽ xem xét bit Bật Ngoài Cùng Bên Phải Tiếp Theo.

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

### Đếm số bit bật đến $n$ {: #count-set-bits-upto-n}
Để đếm số lượng bit bật của tất cả các số đến số $n$ (tính cả $n$), chúng ta có thể chạy thuật toán Brian Kernighan trên tất cả các số đến $n$. Nhưng điều này sẽ dẫn đến "Time Limit Exceeded" trong các bài nộp.

Chúng ta có thể sử dụng thực tế là đối với các số đến $2^x$ (tức là từ $1$ đến $2^x - 1$) có $x \cdot 2^{x-1}$ bit bật. Điều này có thể được hình dung như sau.
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

Chúng ta có thể thấy rằng tất cả các cột ngoại trừ cột ngoài cùng bên trái đều có $4$ (tức là $2^2$) bit bật mỗi cột, tức là đến số $2^3 - 1$, số lượng bit bật là $3 \cdot 2^{3-1}$.

Với kiến thức mới này, chúng ta có thể đưa ra thuật toán sau:

- Tìm lũy thừa cao nhất của $2$ nhỏ hơn hoặc bằng số đã cho. Gọi số này là $x$.
- Tính số lượng bit bật từ $1$ đến $2^x - 1$ bằng cách sử dụng công thức $x \cdot 2^{x-1}$.
- Đếm số lượng bit bật ở bit quan trọng nhất từ $2^x$ đến $n$ và cộng vào.
- Trừ $2^x$ khỏi $n$ và lặp lại các bước trên sử dụng $n$ mới.

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

### Các thủ thuật khác {: #additional-tricks}

- $n ~\&~ (n + 1)$ tắt tất cả các số một ở cuối: $0011~0111_2 \rightarrow 0011~0000_2$.
- $n ~|~ (n + 1)$ bật bit tắt cuối cùng: $0011~0101_2 \rightarrow 0011~0111_2$.
- $n ~\&~ -n$ trích xuất bit bật cuối cùng: $0011~0100_2 \rightarrow 0000~0100_2$.

Nhiều thủ thuật khác có thể được tìm thấy trong cuốn sách [Hacker's Delight](https://en.wikipedia.org/wiki/Hacker%27s_Delight).

### Hỗ trợ của ngôn ngữ và trình biên dịch {: #language-and-compiler-support}

C++ hỗ trợ một số thao tác đó kể từ C++20 thông qua thư viện chuẩn [bit](https://en.cppreference.com/w/cpp/header/bit):

- `has_single_bit`: kiểm tra xem số có phải là lũy thừa của hai không
- `bit_ceil` / `bit_floor`: làm tròn lên/xuống đến lũy thừa tiếp theo của hai
- `rotl` / `rotr`: xoay các bit trong số
- `countl_zero` / `countr_zero` / `countl_one` / `countr_one`: đếm số không/số một dẫn đầu/ở cuối
- `popcount`: đếm số lượng bit bật

Ngoài ra, cũng có các hàm được định nghĩa trước trong một số trình biên dịch giúp làm việc với các bit.
V.d. GCC định nghĩa một danh sách tại [Các Hàm Tích Hợp Được Cung Cấp Bởi GCC](https://gcc.gnu.org/onlinedocs/gcc/Other-Builtins.html) cũng hoạt động trong các phiên bản cũ hơn của C++:

- `__builtin_popcount(unsigned int)` trả về số lượng bit bật (`__builtin_popcount(0b0001'0010'1100) == 4`)
- `__builtin_ffs(int)` tìm chỉ số của bit bật đầu tiên (phải nhất) (`__builtin_ffs(0b0001'0010'1100) == 3`)
- `__builtin_clz(unsigned int)` số lượng số không dẫn đầu (`__builtin_clz(0b0001'0010'1100) == 23`)
- `__builtin_ctz(unsigned int)` số lượng số không ở cuối (`__builtin_ctz(0b0001'0010'1100) == 2`)
- ` __builtin_parity(x)` tính chẵn lẻ (chẵn hoặc lẻ) của số lượng số một trong biểu diễn bit

_Lưu ý rằng một số thao tác (cả các hàm C++20 và các hàm tích hợp của trình biên dịch) có thể khá chậm trong GCC nếu bạn không bật một mục tiêu trình biên dịch cụ thể bằng `#pragma GCC target("popcnt")`._

## Bài tập luyện tập {: #practice-problems}

* [Codeforces - Raising Bacteria](https://codeforces.com/problemset/problem/579/A)
* [Codeforces - Fedor and New Game](https://codeforces.com/problemset/problem/467/B)
* [Codeforces - And Then There Were K](https://codeforces.com/problemset/problem/1527/A)
