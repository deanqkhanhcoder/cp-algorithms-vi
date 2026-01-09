---
tags:
  - Translated
e_maxx_link: big_integer
---

# Số học độ chính xác tùy ý (Arbitrary-Precision Arithmetic) {: #arbitrary-precision-arithmetic}

Số học độ chính xác tùy ý, còn được gọi là "bignum" hay đơn giản là "số học lớn" (long arithmetic) là một tập hợp các cấu trúc dữ liệu và thuật toán cho phép xử lý các số lớn hơn nhiều so với khả năng lữu trữ của các kiểu dữ liệu chuẩn. Dưới đây là một số loại số học độ chính xác tùy ý.

## Số học số nguyên lớn cổ điển {: #classical-integer-long-arithmetic}

Ý tưởng chính là số được lưu trữ dưới dạng mảng các "chữ số" của nó trong một cơ số nào đó. Một số cơ số được sử dụng thường xuyên nhất là thập phân, lũy thừa của thập phân ($10^4$ hoặc $10^9$) và nhị phân.

Các phép toán trên các số ở dạng này được thực hiện bằng cách sử dụng các thuật toán "học đường" như cộng, trừ, nhân và chia theo cột. Cũng có thể sử dụng các thuật toán nhân nhanh: biến đổi Fourier nhanh (FFT) và thuật toán Karatsuba.

Ở đây chúng tôi chỉ mô tả số học lớn cho các số nguyên không âm. Để mở rộng các thuật toán xử lý số nguyên âm, người ta phải giới thiệu và duy trì thêm cờ "số âm" hoặc sử dụng biểu diễn số nguyên bù hai.

### Cấu trúc dữ liệu {: #data-structure}

Chúng ta sẽ lưu trữ các số dưới dạng `vector<int>`, trong đó mỗi phần tử là một "chữ số" đơn lẻ của số đó.

```cpp
typedef vector<int> lnum;
```

Để cải thiện hiệu suất, chúng ta sẽ sử dụng $10^9$ làm cơ số, để mỗi "chữ số" của số lớn chứa 9 chữ số thập phân cùng một lúc.

```cpp
const int base = 1000*1000*1000;
```

Các chữ số sẽ được lưu trữ theo thứ tự từ ít quan trọng nhất đến quan trọng nhất. Tất cả các phép toán sẽ được cài đặt sao cho sau mỗi phép toán, kết quả không có bất kỳ số không dẫn đầu nào, miễn là các toán hạng cũng không có số không dẫn đầu. Tất cả các phép toán có thể dẫn đến một số có số không dẫn đầu nên được theo sau bởi mã loại bỏ chúng. Lưu ý rằng trong biểu diễn này có hai ký hiệu hợp lệ cho số không: một vector rỗng, và một vector với một chữ số không duy nhất.

### Xuất (Output) {: #output}

In ra số nguyên lớn là thao tác dễ nhất. Đầu tiên chúng ta in phần tử cuối cùng của vector (hoặc 0 nếu vector rỗng), theo sau là các phần tử còn lại được đệm bằng các số không dẫn đầu nếu cần thiết để chúng có độ dài chính xác 9 chữ số.

```cpp
printf ("%d", a.empty() ? 0 : a.back());
for (int i=(int)a.size()-2; i>=0; --i)
	printf ("%09d", a[i]);
```

Lưu ý rằng chúng ta ép kiểu `a.size()` sang số nguyên để tránh tràn số nguyên không dấu (unsigned underflow) nếu vector chứa ít hơn 2 phần tử.

### Nhập (Input) {: #input}

Để đọc một số nguyên lớn, đọc ký hiệu của nó vào một `string` và sau đó chuyển đổi nó thành các "chữ số":

```cpp
for (int i=(int)s.length(); i>0; i-=9)
	if (i < 9)
		a.push_back (atoi (s.substr (0, i).c_str()));
	else
		a.push_back (atoi (s.substr (i-9, 9).c_str()));
```

Nếu chúng ta sử dụng mảng `char` thay vì `string`, code sẽ còn ngắn hơn:

```cpp
for (int i=(int)strlen(s); i>0; i-=9) {
	s[i] = 0;
	a.push_back (atoi (i>=9 ? s+i-9 : s));
}
```

Nếu đầu vào có thể chứa các số không dẫn đầu, chúng có thể được loại bỏ như sau:

```cpp
while (a.size() > 1 && a.back() == 0)
	a.pop_back();
```

### Phép cộng {: #addition}

Tăng số nguyên lớn $a$ thêm $b$ và lưu kết quả vào $a$:

```cpp
int carry = 0;
for (size_t i=0; i<max(a.size(),b.size()) || carry; ++i) {
	if (i == a.size())
		a.push_back (0);
	a[i] += carry + (i < b.size() ? b[i] : 0);
	carry = a[i] >= base;
	if (carry)  a[i] -= base;
}
```

### Phép trừ {: #subtraction}

Giảm số nguyên lớn $a$ đi $b$ ($a \ge b$) và lưu kết quả vào $a$:

```cpp
int carry = 0;
for (size_t i=0; i<b.size() || carry; ++i) {
	a[i] -= carry + (i < b.size() ? b[i] : 0);
	carry = a[i] < 0;
	if (carry)  a[i] += base;
}
while (a.size() > 1 && a.back() == 0)
	a.pop_back();
```

Lưu ý rằng sau khi thực hiện phép trừ, chúng ta loại bỏ các số không dẫn đầu để tuân thủ tiền đề là các số nguyên lớn của chúng ta không có số không dẫn đầu.

### Nhân với số nguyên nhỏ {: #multiplication-by-short-integer}

Nhân số nguyên lớn $a$ với số nguyên nhỏ $b$ ($b < base$) và lưu kết quả vào $a$:

```cpp
int carry = 0;
for (size_t i=0; i<a.size() || carry; ++i) {
	if (i == a.size())
		a.push_back (0);
	long long cur = carry + a[i] * 1ll * b;
	a[i] = int (cur % base);
	carry = int (cur / base);
}
while (a.size() > 1 && a.back() == 0)
	a.pop_back();
```

Tối ưu hóa bổ sung: Nếu thời gian chạy cực kỳ quan trọng, bạn có thể thử thay thế hai phép chia bằng một phép chia bằng cách chỉ tìm kết quả nguyên của phép chia (biến `carry`) và sau đó sử dụng nó để tìm modulo bằng phép nhân. Điều này thường làm cho code nhanh hơn, mặc dù không đặc biệt nhiều.

### Nhân với số nguyên lớn {: #multiplication-by-long-integer}

Nhân các số nguyên lớn $a$ và $b$ và lưu kết quả vào $c$:

```cpp
lnum c (a.size()+b.size());
for (size_t i=0; i<a.size(); ++i)
	for (int j=0, carry=0; j<(int)b.size() || carry; ++j) {
		long long cur = c[i+j] + a[i] * 1ll * (j < (int)b.size() ? b[j] : 0) + carry;
		c[i+j] = int (cur % base);
		carry = int (cur / base);
	}
while (c.size() > 1 && c.back() == 0)
	c.pop_back();
```

### Chia cho số nguyên nhỏ {: #division-by-short-integer}

Chia số nguyên lớn $a$ cho số nguyên nhỏ $b$ ($b < base$), lưu thương số nguyên vào $a$ và phần dư vào `carry`:

```cpp
int carry = 0;
for (int i=(int)a.size()-1; i>=0; --i) {
	long long cur = a[i] + carry * 1ll * base;
	a[i] = int (cur / b);
	carry = int (cur % b);
}
while (a.size() > 1 && a.back() == 0)
	a.pop_back();
```

## Số học số nguyên lớn dùng biểu diễn phân tích thừa số {: #long-integer-arithmetic-for-factorization-representation}

Ý tưởng là lưu trữ số nguyên dưới dạng phân tích thừa số của nó, tức là các lũy thừa của các số nguyên tố chia hết cho nó.

Cách tiếp cận này rất dễ cài đặt, và cho phép thực hiện phép nhân và chia dễ dàng (nhanh hơn về mặt tiệm cận so với phương pháp cổ điển), nhưng không hỗ trợ phép cộng hoặc trừ. Nó cũng rất tiết kiệm bộ nhớ so với cách tiếp cận cổ điển.

Phương pháp này thường được sử dụng cho các phép tính modulo một số không nguyên tố M; trong trường hợp này, một số được lưu trữ dưới dạng các lũy thừa của các ước của M chia hết cho số đó, cộng với phần dư modulo M.

## Số học số nguyên lớn theo modulo nguyên tố (Thuật toán Garner) {: #long-integer-arithmetic-in-prime-modulos-garner-algorithm}

Ý tưởng là chọn một tập hợp các số nguyên tố (thường chúng đủ nhỏ để vừa với kiểu dữ liệu số nguyên chuẩn) và lưu trữ một số nguyên dưới dạng vector các phần dư từ phép chia số nguyên đó cho mỗi số nguyên tố này.

Định lý thặng dư Trung Hoa phát biểu rằng biểu diễn này là đủ để khôi phục duy nhất bất kỳ số nào từ 0 đến tích của các số nguyên tố này trừ một. [Thuật toán Garner](garners-algorithm.md) cho phép khôi phục số từ biểu diễn như vậy về số nguyên bình thường.

Phương pháp này cho phép tiết kiệm bộ nhớ so với cách tiếp cận cổ điển (mặc dù mức tiết kiệm không đáng kể như trong biểu diễn phân tích thừa số). Ngoài ra, nó cho phép thực hiện phép cộng, trừ và nhân nhanh trong thời gian tỷ lệ với số lượng số nguyên tố được sử dụng làm modulo (xem bài viết [Định lý thặng dư Trung Hoa](chinese-remainder-theorem.md) để biết cài đặt).

Sự đánh đổi là việc chuyển đổi số nguyên trở lại dạng bình thường khá tốn công sức và đòi hỏi phải cài đặt số học độ chính xác tùy ý cổ điển với phép nhân. Ngoài ra, phương pháp này không hỗ trợ phép chia.

## Số học phân số độ chính xác tùy ý {: #fractional-arbitrary-precision-arithmetic}

Phân số xuất hiện trong các kỳ thi lập trình ít thường xuyên hơn số nguyên, và số học lớn khó cài đặt hơn nhiều đối với phân số, vì vậy các kỳ thi lập trình chỉ có một tập hợp nhỏ số học lớn phân số.

### Số học trên phân số tối giản {: #arithmetic-in-irreducible-fractions}

Một số được biểu diễn dưới dạng phân số tối giản $\frac{a}{b}$, trong đó $a$ và $b$ là các số nguyên. Tất cả các phép toán trên phân số có thể được biểu diễn dưới dạng các phép toán trên tử số và mẫu số nguyên của các phân số này. Thường thì điều này đòi hỏi phải sử dụng số học độ chính xác tùy ý cổ điển để lưu trữ tử số và mẫu số, nhưng đôi khi kiểu dữ liệu số nguyên 64-bit tích hợp sẵn là đủ.

### Lưu trữ vị trí dấu phẩy động dưới dạng kiểu riêng biệt {: #storing-floating-point-position-as-separate-type}

Đôi khi một bài toán yêu cầu xử lý các số rất nhỏ hoặc rất lớn mà không cho phép tràn số (overflow hoặc underflow). Kiểu dữ liệu double tích hợp sẵn sử dụng 8-10 byte và cho phép giá trị của số mũ trong khoảng $[-308; 308]$, đôi khi có thể là không đủ.

Cách tiếp cận rất đơn giản: một biến số nguyên riêng biệt được sử dụng để lưu trữ giá trị của số mũ, và sau mỗi phép toán, số dấu phẩy động được chuẩn hóa, tức là đưa về khoảng $[0.1; 1)$ bằng cách điều chỉnh số mũ tương ứng.

Khi hai số như vậy được nhân hoặc chia, các số mũ của chúng nên được cộng hoặc trừ tương ứng. Khi các số được cộng hoặc trừ, chúng phải được đưa về cùng số mũ trước bằng cách nhân một trong số chúng với 10 lũy thừa hiệu của các giá trị số mũ.

Cuối cùng, cơ số mũ không nhất thiết phải bằng 10. Dựa trên biểu diễn nội bộ của các số dấu phẩy động, hợp lý nhất là sử dụng 2 làm cơ số mũ.

## Bài tập luyện tập {: #practice-problems}


* [UVA - How Many Fibs?](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1124)
* [UVA - Product](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1047)
* [UVA - Maximum Sub-sequence Product](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=728)
* [SPOJ - Fast Multiplication](http://www.spoj.com/problems/MUL/en/)
* [SPOJ - GCD2](http://www.spoj.com/problems/GCD2/)
* [UVA - Division](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1024)
* [UVA - Fibonacci Freeze](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=436)
* [UVA - Krakovia](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1866)
* [UVA - Simplifying Fractions](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1755)
* [UVA - 500!](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=564)
* [Hackerrank - Factorial digit sum](https://www.hackerrank.com/contests/projecteuler/challenges/euler020/problem)
* [UVA - Immortal Rabbits](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=4803)
* [SPOJ - 0110SS](http://www.spoj.com/problems/IWGBS/)
* [Codeforces - Notepad](http://codeforces.com/contest/17/problem/D)
