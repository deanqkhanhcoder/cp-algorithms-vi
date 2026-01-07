---
tags:
  - Original
---
# Thao tác bit

## Số nhị phân

Một **số nhị phân** là một số được biểu diễn trong hệ đếm cơ số 2 hay hệ nhị phân, nó là một phương pháp biểu diễn toán học chỉ sử dụng hai ký hiệu: thường là "0" (không) và "1" (một).

Chúng ta nói rằng một bit nào đó được **bật** (set) nếu nó là một, và **tắt** (cleared) nếu nó là không.

Số nhị phân $(a_k a_{k-1} \dots a_1 a_0)_2$ biểu diễn số:

$$(a_k a_{k-1} \dots a_1 a_0)_2 = a_k \cdot 2^k + a_{k-1} \cdot 2^{k-1} + \dots + a_1 \cdot 2^1 + a_0 \cdot 2^0.$$

Ví dụ, số nhị phân $1101_2$ biểu diễn số $13$:

$$\begin{align}
1101_2 &= 1 \cdot 2^3 + 1 \cdot 2^2 + 0 \cdot 2^1 + 1 \cdot 2^0 \       &= 1\cdot 8 + 1 \cdot 4 + 0 \cdot 2 + 1 \cdot 1 = 13
\end{align}$$

Máy tính biểu diễn số nguyên dưới dạng số nhị phân.
Các số nguyên dương (cả có dấu và không dấu) chỉ được biểu diễn bằng các chữ số nhị phân của chúng, và các số có dấu âm (có thể là dương và âm) thường được biểu diễn bằng [phần bù hai](https://en.wikipedia.org/wiki/Two%27s_complement).

```cpp
unsigned int unsigned_number = 13;
assert(unsigned_number == 0b1101);

int positive_signed_number = 13;
assert(positive_signed_number == 0b1101);

int negative_signed_number = -13;
assert(negative_signed_number == 0b1111'1111'1111'1111'1111'1111'1111'0011);
```

CPU rất nhanh trong việc thao tác các bit này với các phép toán cụ thể.
Đối với một số bài toán, chúng ta có thể tận dụng các biểu diễn số nhị phân này để tăng tốc thời gian thực thi.
Và đối với một số bài toán (thường là trong tổ hợp hoặc quy hoạch động) nơi chúng ta muốn theo dõi các đối tượng nào chúng ta đã chọn từ một tập hợp các đối tượng đã cho, chúng ta chỉ cần sử dụng một số nguyên đủ lớn trong đó mỗi chữ số đại diện cho một đối tượng và tùy thuộc vào việc chúng ta chọn hay bỏ đối tượng, chúng ta bật hoặc tắt chữ số đó.

## Các toán tử bit

Tất cả các toán tử được giới thiệu đều là tức thời (cùng tốc độ với một phép cộng) trên CPU đối với các số nguyên có độ dài cố định.

### Các toán tử thao tác bit

-   $\$ : Toán tử AND bit so sánh từng bit của toán hạng đầu tiên với bit tương ứng của toán hạng thứ hai.
    Nếu cả hai bit đều là 1, bit kết quả tương ứng được đặt thành 1. Ngược lại, bit kết quả tương ứng được đặt thành 0.

-   $| $ : Toán tử OR bit bao hàm so sánh từng bit của toán hạng đầu tiên với bit tương ứng của toán hạng thứ hai.
    Nếu một trong hai bit là 1, bit kết quả tương ứng được đặt thành 1. Ngược lại, bit kết quả tương ứng được đặt thành 0.

-   $\\^$ : Toán tử OR loại trừ (XOR) bit so sánh từng bit của toán hạng đầu tiên với bit tương ứng của toán hạng thứ hai.
    Nếu một bit là 0 và bit kia là 1, bit kết quả tương ứng được đặt thành 1. Ngược lại, bit kết quả tương ứng được đặt thành 0.

-   $\\sim$ : Toán tử bù bit (NOT) đảo ngược từng bit của một số, nếu một bit được bật, toán tử sẽ tắt nó, nếu nó bị tắt, toán tử sẽ bật nó.

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

### Các toán tử dịch chuyển

Có hai toán tử để dịch chuyển bit.

-   $>>$ Dịch một số sang phải bằng cách xóa một vài chữ số nhị phân cuối cùng của số đó.
    Mỗi lần dịch một vị trí đại diện cho một phép chia số nguyên cho 2, vì vậy dịch phải $k$ vị trí đại diện cho một phép chia số nguyên cho $2^k$.

    Ví dụ $5 >> 2 = 101_2 >> 2 = 1_2 = 1$ cũng giống như $\frac{5}{2^2} = \frac{5}{4} = 1$.
    Tuy nhiên, đối với máy tính, dịch một vài bit nhanh hơn nhiều so với thực hiện phép chia.

-   $<<$ Dịch một số sang trái bằng cách nối thêm các chữ số không.
    Tương tự như dịch phải $k$ vị trí, dịch trái $k$ vị trí đại diện cho một phép nhân với $2^k$.

    Ví dụ $5 << 3 = 101_2 << 3 = 101000_2 = 40$ cũng giống như $5 \cdot 2^3 = 5 \cdot 8 = 40$.

    Tuy nhiên, lưu ý rằng đối với một số nguyên có độ dài cố định, điều đó có nghĩa là bỏ đi các chữ số ngoài cùng bên trái, và nếu bạn dịch quá nhiều, bạn sẽ kết thúc với số $0$.


## Các thủ thuật hữu ích

### Bật/đảo/tắt một bit

Sử dụng các phép dịch chuyển bit và một số phép toán bit cơ bản, chúng ta có thể dễ dàng bật, đảo hoặc tắt một bit.
$1 << x$ là một số chỉ có bit thứ $x$ được bật, trong khi $\sim(1 << x)$ là một số có tất cả các bit được bật ngoại trừ bit thứ $x$.

- $n ~|~ (1 << x)$ bật bit thứ $x$ trong số $n$
- $n ~\wedge~ (1 << x)$ đảo bit thứ $x$ trong số $n$
- $n ~\&~ \sim(1 << x)$ tắt bit thứ $x$ trong số $n$

### Kiểm tra một bit có được bật không

Giá trị của bit thứ $x$ có thể được kiểm tra bằng cách dịch số đó sang phải $x$ vị trí, để bit thứ $x$ ở vị trí đơn vị, sau đó chúng ta có thể trích xuất nó bằng cách thực hiện phép AND bit với 1.

``` cpp
bool is_set(unsigned int number, int x) {
    return (number >> x) & 1;
}
```

### Kiểm tra một số có chia hết cho lũy thừa của 2 không

Sử dụng phép toán AND, chúng ta có thể kiểm tra xem một số $n$ có phải là số chẵn không vì $n ~\&~ 1 = 0$ nếu $n$ là số chẵn, và $n ~\&~ 1 = 1$ nếu $n$ là số lẻ.
Tổng quát hơn, $n$ chia hết cho $2^{k}$ khi và chỉ khi $n ~\&~ (2^{k} - 1) = 0$.

``` cpp
bool isDivisibleByPowerOf2(int n, int k) {
    int powerOf2 = 1 << k;
    return (n & (powerOf2 - 1)) == 0;
}
```

Chúng ta có thể tính $2^{k}$ bằng cách dịch trái 1 $k$ vị trí.
Thủ thuật này hoạt động vì $2^k - 1$ là một số bao gồm chính xác $k$ số một.
Và một số chia hết cho $2^k$ phải có các chữ số không ở những vị trí đó.

### Kiểm tra một số nguyên có phải là lũy thừa của 2 không

Một lũy thừa của hai là một số chỉ có một bit duy nhất được bật (ví dụ: $32 = 0010~0000_2$), trong khi số liền trước của số đó có bit đó không được bật và tất cả các bit sau nó được bật ($31 = 0001~1111_2$).
Vì vậy, phép AND bit của một số với số liền trước của nó sẽ luôn là 0, vì chúng không có bất kỳ chữ số chung nào được bật.
Bạn có thể dễ dàng kiểm tra rằng điều này chỉ xảy ra đối với các lũy thừa của hai và đối với số $0$ vốn đã không có bit nào được bật.

``` cpp
bool isPowerOfTwo(unsigned int n) {
    return n && !(n & (n - 1));
}
```

### Tắt bit 1 bên phải nhất

Biểu thức $n ~\&~ (n-1)$ có thể được sử dụng để tắt bit 1 bên phải nhất của một số $n$.
Điều này hoạt động vì biểu thức $n-1$ đảo tất cả các bit sau bit 1 bên phải nhất của $n$, bao gồm cả bit 1 bên phải nhất.
Vì vậy, tất cả các chữ số đó đều khác với số ban đầu, và bằng cách thực hiện phép AND bit, tất cả chúng đều được đặt thành 0, cho bạn số $n$ ban đầu với bit 1 bên phải nhất được tắt.

Ví dụ, xét số $52 = 0011~0100_2$:

```
n         = 00110100
n-1       = 00110011
--------------------
n & (n-1) = 00110000
```

### Thuật toán của Brian Kernighan

Chúng ta có thể đếm số bit được bật bằng biểu thức trên.

Ý tưởng là chỉ xem xét các bit được bật của một số nguyên bằng cách tắt bit 1 bên phải nhất của nó (sau khi đếm nó), để lần lặp tiếp theo của vòng lặp xem xét bit 1 bên phải nhất tiếp theo.

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

### Đếm số bit được bật đến $n$
Để đếm số bit được bật của tất cả các số cho đến số $n$ (bao gồm cả $n$), chúng ta có thể chạy thuật toán của Brian Kernighan trên tất cả các số cho đến $n$. Nhưng điều này sẽ dẫn đến "Time Limit Exceeded" trong các bài nộp thi đấu.

Chúng ta có thể sử dụng thực tế là đối với các số lên đến $2^x$ (tức là từ $1$ đến $2^x - 1$) có $x \cdot 2^{x-1}$ bit được bật. Điều này có thể được hình dung như sau.
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

Chúng ta có thể thấy rằng tất cả các cột ngoại trừ cột ngoài cùng bên trái đều có $4$ (tức là $2^2$) bit được bật, tức là cho đến số $2^3 - 1$, số bit được bật là $3 \cdot 2^{3-1}$.

Với kiến thức mới này, chúng ta có thể đưa ra thuật toán sau:

- Tìm lũy thừa cao nhất của $2$ nhỏ hơn hoặc bằng số đã cho. Gọi số này là $x$.
- Tính số bit được bật từ $1$ đến $2^x - 1$ bằng công thức $x \cdot 2^{x-1}$.
- Đếm số bit được bật trong bit có nghĩa nhất từ $2^x$ đến $n$ và cộng nó vào.
- Trừ $2^x$ từ $n$ và lặp lại các bước trên với $n$ mới.

``` cpp
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

### Các thủ thuật bổ sung

- $n ~\&~ (n + 1)$ tắt tất cả các bit 1 ở cuối: $0011~0111_2 \rightarrow 0011~0000_2$.
- $n ~|~ (n + 1)$ bật bit 0 cuối cùng: $0011~0101_2 \rightarrow 0011~0111_2$.
- $n ~\&~ -n$ trích xuất bit 1 cuối cùng: $0011~0100_2 \rightarrow 0000~0100_2$.

Có thể tìm thấy nhiều hơn nữa trong cuốn sách [Hacker's Delight](https://en.wikipedia.org/wiki/Hacker%27s_Delight).

### Hỗ trợ ngôn ngữ và trình biên dịch

C++ hỗ trợ một số thao tác đó kể từ C++20 thông qua thư viện chuẩn [bit](https://en.cppreference.com/w/cpp/header/bit):

- `has_single_bit`: kiểm tra xem số có phải là lũy thừa của hai không
- `bit_ceil` / `bit_floor`: làm tròn lên/xuống đến lũy thừa của hai tiếp theo
- `rotl` / `rotr`: xoay các bit trong số
- `countl_zero` / `countr_zero` / `countl_one` / `countr_one`: đếm số không/một đứng đầu/cuối
- `popcount`: đếm số bit được bật

Ngoài ra, cũng có các hàm được xác định trước trong một số trình biên dịch giúp làm việc với các bit.
Ví dụ: GCC định nghĩa một danh sách tại [Các hàm tích hợp sẵn do GCC cung cấp](https://gcc.gnu.org/onlinedocs/gcc/Other-Builtins.html) cũng hoạt động trong các phiên bản C++ cũ hơn:

- `__builtin_popcount(unsigned int)` trả về số bit được bật (`__builtin_popcount(0b0001'0010'1100) == 4`)
- `__builtin_ffs(int)` tìm chỉ số của bit được bật đầu tiên (bên phải nhất) (`__builtin_ffs(0b0001'0010'1100) == 3`)
- `__builtin_clz(unsigned int)` số lượng số không đứng đầu (`__builtin_clz(0b0001'0010'1100) == 23`)
- `__builtin_ctz(unsigned int)` số lượng số không ở cuối (`__builtin_ctz(0b0001'0010'1100) == 2`)
- ` __builtin_parity(x)` tính chẵn lẻ (chẵn hoặc lẻ) của số lượng bit một trong biểu diễn bit

_Lưu ý rằng một số thao tác (cả hàm C++20 và hàm tích hợp sẵn của trình biên dịch) có thể khá chậm trong GCC nếu bạn không bật một mục tiêu trình biên dịch cụ thể với `#pragma GCC target("popcnt")`._

## Bài tập luyện tập

* [Codeforces - Raising Bacteria](https://codeforces.com/problemset/problem/579/A)
* [Codeforces - Fedor and New Game](https://codeforces.com/problemset/problem/467/B)
* [Codeforces - And Then There Were K](https://codeforces.com/problemset/problem/1527/A)