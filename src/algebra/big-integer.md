---
tags:
  - Translated
e_maxx_link: big_integer
---

# Số học với độ chính xác tùy ý

Số học với độ chính xác tùy ý, còn được gọi là "bignum" hoặc đơn giản là "số học số lớn", là một tập hợp các cấu trúc dữ liệu và thuật toán cho phép xử lý các số lớn hơn nhiều so với các kiểu dữ liệu tiêu chuẩn. Dưới đây là một số loại số học với độ chính xác tùy ý.

## Số học số nguyên lớn cổ điển

Ý tưởng chính là số được lưu trữ dưới dạng một mảng các "chữ số" của nó trong một cơ số nào đó. Một số cơ số thường được sử dụng nhất là thập phân, lũy thừa của mười ($10^4$ hoặc $10^9$) và nhị phân.

Các phép toán trên các số ở dạng này được thực hiện bằng các thuật toán "cấp 1" như cộng, trừ, nhân và chia theo cột. Cũng có thể sử dụng các thuật toán nhân nhanh: biến đổi Fourier nhanh và thuật toán Karatsuba.

Ở đây chúng tôi chỉ mô tả số học số lớn cho các số nguyên không âm. Để mở rộng các thuật toán để xử lý các số nguyên âm, người ta phải giới thiệu và duy trì thêm cờ "số âm" hoặc sử dụng biểu diễn số nguyên bù hai.

### Cấu trúc dữ liệu

Chúng ta sẽ lưu trữ các số dưới dạng `vector<int>`, trong đó mỗi phần tử là một "chữ số" của số đó.

```cpp
typedef vector<int> lnum;
```

Để cải thiện hiệu suất, chúng ta sẽ sử dụng $10^9$ làm cơ số, để mỗi "chữ số" của số lớn chứa 9 chữ số thập phân cùng một lúc.

```cpp
const int base = 1000*1000*1000;
```

Các chữ số sẽ được lưu trữ theo thứ tự từ ít có nghĩa nhất đến có nghĩa nhất. Tất cả các hoạt động sẽ được thực hiện sao cho sau mỗi hoạt động, kết quả không có số 0 đứng đầu, miễn là các toán hạng cũng không có số 0 đứng đầu. Tất cả các hoạt động có thể dẫn đến một số có các số 0 đứng đầu phải được theo sau bởi đoạn mã loại bỏ chúng. Lưu ý rằng trong biểu diễn này, có hai ký hiệu hợp lệ cho số không: một vector rỗng và một vector có một chữ số không duy nhất.

### Xuất dữ liệu

In số nguyên lớn là hoạt động dễ nhất. Đầu tiên, chúng ta in phần tử cuối cùng của vector (hoặc 0 nếu vector rỗng), theo sau là các phần tử còn lại được đệm bằng các số 0 đứng đầu nếu cần để chúng dài đúng 9 chữ số.

```cpp
printf ("%d", a.empty() ? 0 : a.back());
for (int i=(int)a.size()-2; i>=0; --i)
	printf ("%09d", a[i]);
```

Lưu ý rằng chúng ta ép kiểu `a.size()` thành số nguyên để tránh tràn số nguyên không dấu nếu vector chứa ít hơn 2 phần tử.

### Nhập dữ liệu

Để đọc một số nguyên lớn, hãy đọc ký hiệu của nó vào một `string` và sau đó chuyển đổi nó thành "các chữ số":

```cpp
for (int i=(int)s.length(); i>0; i-=9)
	if (i < 9)
		a.push_back (atoi (s.substr (0, i).c_str()));
	else
		a.push_back (atoi (s.substr (i-9, 9).c_str()));
```

Nếu chúng ta sử dụng một mảng `char` thay vì `string`, mã sẽ còn ngắn hơn:

```cpp
for (int i=(int)strlen(s); i>0; i-=9) {
	s[i] = 0;
	a.push_back (atoi (i>=9 ? s+i-9 : s));
}
```

Nếu đầu vào có thể chứa các số 0 đứng đầu, chúng có thể được loại bỏ như sau:

```cpp
while (a.size() > 1 && a.back() == 0)
	a.pop_back();
```

### Phép cộng

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

### Phép trừ

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

Lưu ý rằng sau khi thực hiện phép trừ, chúng ta loại bỏ các số 0 đứng đầu để giữ đúng tiền đề rằng các số nguyên lớn của chúng ta không có số 0 đứng đầu.

### Phép nhân với số nguyên ngắn

Nhân số nguyên lớn $a$ với số nguyên ngắn $b$ ($b < base$) và lưu kết quả vào $a$:

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

Tối ưu hóa bổ sung: Nếu thời gian chạy cực kỳ quan trọng, bạn có thể thử thay thế hai phép chia bằng một phép chia bằng cách chỉ tìm kết quả nguyên của phép chia (biến `carry`) và sau đó sử dụng nó để tìm modulo bằng phép nhân. Điều này thường làm cho mã chạy nhanh hơn, mặc dù không đáng kể.

### Phép nhân với số nguyên lớn

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

### Phép chia cho số nguyên ngắn

Chia số nguyên lớn $a$ cho số nguyên ngắn $b$ ($b < base$), lưu kết quả nguyên vào $a$ và số dư vào `carry`:

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

## Số học số nguyên lớn cho biểu diễn phân tích thừa số

Ý tưởng là lưu trữ số nguyên dưới dạng phân tích thừa số của nó, tức là lũy thừa của các số nguyên tố chia hết cho nó.

Cách tiếp cận này rất dễ thực hiện và cho phép thực hiện phép nhân và chia dễ dàng (nhanh hơn về mặt tiệm cận so với phương pháp cổ điển), nhưng không hỗ trợ phép cộng hoặc trừ. Nó cũng rất hiệu quả về bộ nhớ so với phương pháp cổ điển.

Phương pháp này thường được sử dụng cho các phép tính modulo một số không nguyên tố M; trong trường hợp này, một số được lưu trữ dưới dạng lũy thừa của các ước của M chia hết cho số đó, cộng với phần còn lại modulo M.

## Số học số nguyên lớn trong các modulo nguyên tố (Thuật toán Garner)

Ý tưởng là chọn một tập hợp các số nguyên tố (thường chúng đủ nhỏ để vừa với kiểu dữ liệu số nguyên tiêu chuẩn) và lưu trữ một số nguyên dưới dạng một vector các số dư từ phép chia số nguyên đó cho mỗi số nguyên tố đó.

Định lý phần dư Trung Hoa nói rằng biểu diễn này là đủ để khôi phục duy nhất bất kỳ số nào từ 0 đến tích của các số nguyên tố này trừ một. [Thuật toán Garner](garners-algorithm.md) cho phép khôi phục số từ biểu diễn đó về số nguyên bình thường.

Phương pháp này cho phép tiết kiệm bộ nhớ so với phương pháp cổ điển (mặc dù mức tiết kiệm không đáng kể như trong biểu diễn phân tích thừa số). Bên cạnh đó, nó cho phép thực hiện các phép cộng, trừ và nhân nhanh chóng trong thời gian tỷ lệ với số lượng số nguyên tố được sử dụng làm modulo (xem bài viết [Định lý phần dư Trung Hoa](chinese-remainder-theorem.md) để biết cách thực hiện).

Sự đánh đổi là việc chuyển đổi số nguyên trở lại dạng bình thường khá tốn công sức và đòi hỏi phải thực hiện số học số lớn cổ điển với phép nhân. Bên cạnh đó, phương pháp này không hỗ trợ phép chia.

## Số học phân số với độ chính xác tùy ý

Phân số xuất hiện trong các cuộc thi lập trình ít thường xuyên hơn số nguyên và số học số lớn khó thực hiện hơn nhiều đối với phân số, vì vậy các cuộc thi lập trình chỉ có một tập hợp con nhỏ của số học phân số lớn.

### Số học với phân số tối giản

Một số được biểu diễn dưới dạng phân số tối giản $\frac{a}{b}$, trong đó $a$ và $b$ là các số nguyên. Tất cả các phép toán trên phân số có thể được biểu diễn dưới dạng các phép toán trên tử số và mẫu số nguyên của các phân số này. Thông thường, điều này đòi hỏi sử dụng số học số lớn cổ điển để lưu trữ tử số và mẫu số, nhưng đôi khi một kiểu dữ liệu số nguyên 64-bit tích hợp sẵn là đủ.

### Lưu trữ vị trí dấu phẩy động như một kiểu riêng biệt

Đôi khi một bài toán đòi hỏi xử lý các số rất nhỏ hoặc rất lớn mà không cho phép tràn số trên hoặc tràn số dưới. Kiểu dữ liệu double tích hợp sẵn sử dụng 8-10 byte và cho phép các giá trị của số mũ trong phạm vi $[-308; 308]$, đôi khi có thể không đủ.

Cách tiếp cận rất đơn giản: một biến số nguyên riêng biệt được sử dụng để lưu trữ giá trị của số mũ, và sau mỗi hoạt động, số dấu phẩy động được chuẩn hóa, tức là trả về khoảng $[0.1; 1)$ bằng cách điều chỉnh số mũ tương ứng.

Khi hai số như vậy được nhân hoặc chia, số mũ của chúng phải được cộng hoặc trừ tương ứng. Khi các số được cộng hoặc trừ, chúng phải được đưa về cùng một số mũ trước tiên bằng cách nhân một trong số chúng với 10 lũy thừa của hiệu số mũ.

Lưu ý cuối cùng, cơ số của số mũ không nhất thiết phải bằng 10. Dựa trên biểu diễn nội bộ của các số dấu phẩy động, việc sử dụng 2 làm cơ số của số mũ là hợp lý nhất.

## Bài tập luyện tập

* [UVA - How Many Fibs?](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1124)
* [UVA - Product](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1047)
* [UVA - Maximum Sub-sequence Product](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=728)
* [SPOJ - Fast Multiplication](https://www.spoj.com/problems/MUL/en/)
* [SPOJ - GCD2](https://www.spoj.com/problems/GCD2/)
* [UVA - Division](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1024)
* [UVA - Fibonacci Freeze](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=436)
* [UVA - Krakovia](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1866)
* [UVA - Simplifying Fractions](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1755)
* [UVA - 500!](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=564)
* [Hackerrank - Factorial digit sum](https://www.hackerrank.com/contests/projecteuler/challenges/euler020/problem)
* [UVA - Immortal Rabbits](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=4803)
* [SPOJ - 0110SS](https.spoj.com/problems/IWGBS/)
* [Codeforces - Notepad](http://codeforces.com/contest/17/problem/D)