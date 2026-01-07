---
tags:
  - Translated
e_maxx_link: primitive_root
---

# Căn nguyên thủy

## Định nghĩa

Trong số học modular, một số $g$ được gọi là `căn nguyên thủy modulo n` nếu mọi số nguyên tố cùng nhau với $n$ đều đồng dư với một lũy thừa của $g$ modulo $n$. Về mặt toán học, $g$ là một `căn nguyên thủy modulo n` khi và chỉ khi với mọi số nguyên $a$ sao cho $\gcd(a, n) = 1$, tồn tại một số nguyên $k$ sao cho:

$g^k \equiv a \pmod n$.

$k$ sau đó được gọi là `chỉ số` hoặc `logarit rời rạc` của $a$ cơ sở $g$ modulo $n$. $g$ cũng được gọi là `phần tử sinh` của nhóm nhân các số nguyên modulo $n$.

Đặc biệt, trong trường hợp $n$ là một số nguyên tố, các lũy thừa của căn nguyên thủy chạy qua tất cả các số từ $1$ đến $n-1$.

## Sự tồn tại

Căn nguyên thủy modulo $n$ tồn tại khi và chỉ khi:

* $n$ là 1, 2, 4, hoặc
* $n$ là lũy thừa của một số nguyên tố lẻ $(n = p^k)$, hoặc
* $n$ là hai lần lũy thừa của một số nguyên tố lẻ $(n = 2 \cdot p^k)$.

Định lý này được Gauss chứng minh vào năm 1801.

## Mối quan hệ với hàm Euler

Đặt $g$ là một căn nguyên thủy modulo $n$. Khi đó, chúng ta có thể chỉ ra rằng số $k$ nhỏ nhất mà $g^k \equiv 1 \pmod n$ bằng $\phi (n)$. Hơn nữa, điều ngược lại cũng đúng, và thực tế này sẽ được sử dụng trong bài viết này để tìm một căn nguyên thủy.

Hơn nữa, số lượng căn nguyên thủy modulo $n$, nếu có, bằng $\phi (\phi (n) )$.

## Thuật toán tìm căn nguyên thủy

Một thuật toán ngây thơ là xem xét tất cả các số trong phạm vi $[1, n-1]$. Và sau đó kiểm tra xem mỗi số có phải là một căn nguyên thủy hay không, bằng cách tính tất cả các lũy thừa của nó để xem chúng có khác nhau không. Thuật toán này có độ phức tạp $O(g \cdot n)$, sẽ quá chậm. Trong phần này, chúng tôi đề xuất một thuật toán nhanh hơn sử dụng một số định lý nổi tiếng.

Từ phần trước, chúng ta biết rằng nếu số $k$ nhỏ nhất mà $g^k \equiv 1 \pmod n$ là $\phi (n)$, thì $g$ là một căn nguyên thủy. Vì với bất kỳ số $a$ nào nguyên tố cùng nhau với $n$, chúng ta biết từ định lý Euler rằng $a ^ { \phi (n) } \equiv 1 \pmod n$, sau đó để kiểm tra xem $g$ có phải là căn nguyên thủy không, chỉ cần kiểm tra rằng với mọi $d$ nhỏ hơn $\phi (n)$, $g^d \not \equiv 1 \pmod n$. Tuy nhiên, thuật toán này vẫn quá chậm.

Từ định lý Lagrange, chúng ta biết rằng chỉ số của 1 của bất kỳ số nào modulo $n$ phải là một ước của $\phi (n)$. Do đó, chỉ cần xác minh cho tất cả các ước thực sự $d \mid \phi (n)$ rằng $g^d \not \equiv 1 \pmod n$. Đây đã là một thuật toán nhanh hơn nhiều, nhưng chúng ta vẫn có thể làm tốt hơn.

Phân tích thừa số $\phi (n) = p_1 ^ {a_1} \cdots p_s ^ {a_s}$. Chúng tôi chứng minh rằng trong thuật toán trước, chỉ cần xem xét các giá trị của $d$ có dạng $\frac { \phi (n) } {p_j}$. Thật vậy, đặt $d$ là một ước thực sự bất kỳ của $\phi (n)$. Khi đó, rõ ràng, tồn tại một $j$ sao cho $d \mid \frac { \phi (n) } {p_j}$, tức là $d \cdot k = \frac { \phi (n) } {p_j}$. Tuy nhiên, nếu $g^d \equiv 1 \pmod n$, chúng ta sẽ có:

$g ^ { \frac { \phi (n)} {p_j} } \equiv g ^ {d \cdot k} \equiv (g^d) ^k \equiv 1^k \equiv 1 \pmod n$.

tức là trong số các số có dạng $\frac {\phi (n)} {p_i}$, sẽ có ít nhất một số mà các điều kiện không được thỏa mãn.

Bây giờ chúng ta có một thuật toán hoàn chỉnh để tìm căn nguyên thủy:

* Đầu tiên, tìm $\phi (n)$ và phân tích thừa số nó.
* Sau đó lặp qua tất cả các số $g \in [1, n]$, và đối với mỗi số, để kiểm tra xem nó có phải là căn nguyên thủy không, chúng ta làm như sau:

    * Tính tất cả $g ^ { \frac {\phi (n)} {p_i}} \pmod n$.
    * Nếu tất cả các giá trị được tính toán khác $1$, thì $g$ là một căn nguyên thủy.

    Thời gian chạy của thuật toán này là $O(Ans \cdot \log \phi (n) \cdot \log n)$ (giả sử $\phi (n)$ có $\log \phi (n)$ ước số).

Shoup (1990, 1992) đã chứng minh, giả sử [giả thuyết Riemann tổng quát](http://en.wikipedia.org/wiki/Generalized_Riemann_hypothesis), rằng $g$ là $O(\log^6 p)$.

## Cài đặt

Đoạn mã sau giả định rằng modulo `p` là một số nguyên tố. Để nó hoạt động với bất kỳ giá trị nào của `p`, chúng ta phải thêm phép tính $\phi (p)$. 

```cpp
int powmod (int a, int b, int p) {
	int res = 1;
	while (b)
		if (b & 1)
			res = int (res * 1ll * a % p),  --b;
		else
			a = int (a * 1ll * a % p),  b >>= 1;
	return res;
}
 
int generator (int p) {
	vector<int> fact;
	int phi = p-1,  n = phi;
	for (int i=2; i*i<=n; ++i)
		if (n % i == 0) {
			fact.push_back (i);
			while (n % i == 0)
				n /= i;
		}
	if (n > 1)
		fact.push_back (n);
 
	for (int res=2; res<=p; ++res) {
		bool ok = true;
		for (size_t i=0; i<fact.size() && ok; ++i)
			ok &= powmod (res, phi / fact[i], p) != 1;
		if (ok)  return res;
	}
	return -1;
}
```