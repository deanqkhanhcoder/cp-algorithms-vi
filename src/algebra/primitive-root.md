---
tags:
  - Translated
e_maxx_link: primitive_root
---

# Căn nguyên thủy (Primitive Root) {: #primitive-root}

## Định nghĩa (Definition) {: #definition}

Trong số học modulo, một số $g$ được gọi là một `căn nguyên thủy modulo n` nếu mọi số nguyên tố cùng nhau với $n$ đều đồng dư với một lũy thừa của $g$ modulo $n$. Về mặt toán học, $g$ là một `căn nguyên thủy modulo n` khi và chỉ khi đối với bất kỳ số nguyên $a$ nào sao cho $\gcd(a, n) = 1$, tồn tại một số nguyên $k$ sao cho:

$g^k \equiv a \pmod n$.

$k$ sau đó được gọi là `chỉ số` hoặc `logarit rời rạc` của $a$ theo cơ số $g$ modulo $n$. $g$ cũng được gọi là `phần tử sinh` của nhóm nhân các số nguyên modulo $n$.

Cụ thể, đối với trường hợp $n$ là một số nguyên tố, các lũy thừa của căn nguyên thủy chạy qua tất cả các số từ $1$ đến $n-1$.

## Sự tồn tại (Existence) {: #existence}

Căn nguyên thủy modulo $n$ tồn tại khi và chỉ khi:

* $n$ là 1, 2, 4, hoặc
* $n$ là lũy thừa của một số nguyên tố lẻ $(n = p^k)$, hoặc
* $n$ là hai lần lũy thừa của một số nguyên tố lẻ $(n = 2 \cdot p^k)$.

Định lý này được chứng minh bởi Gauss vào năm 1801.

## Quan hệ với hàm Euler (Relation with the Euler function) {: #relation-with-the-euler-function}

Gọi $g$ là một căn nguyên thủy modulo $n$. Khi đó chúng ta có thể chỉ ra rằng số nhỏ nhất $k$ mà $g^k \equiv 1 \pmod n$ bằng $\phi (n)$. Hơn nữa, điều ngược lại cũng đúng, và thực tế này sẽ được sử dụng trong bài viết này để tìm một căn nguyên thủy.

Hơn nữa, số lượng căn nguyên thủy modulo $n$, nếu có, bằng $\phi (\phi (n) )$.

## Thuật toán tìm căn nguyên thủy (Algorithm for finding a primitive root) {: #algorithm-for-finding-a-primitive-root}

Một thuật toán ngây thơ là xem xét tất cả các số trong phạm vi $[1, n-1]$. Và sau đó kiểm tra xem mỗi số có phải là một căn nguyên thủy hay không, bằng cách tính tất cả lũy thừa của nó để xem liệu chúng có khác nhau hay không. Thuật toán này có độ phức tạp $O(g \cdot n)$, sẽ quá chậm. Trong phần này, chúng tôi đề xuất một thuật toán nhanh hơn sử dụng một số định lý nổi tiếng.

Từ phần trước, chúng ta biết rằng nếu số nhỏ nhất $k$ mà $g^k \equiv 1 \pmod n$ là $\phi (n)$, thì $g$ là một căn nguyên thủy. Vì đối với bất kỳ số $a$ nào nguyên tố cùng nhau với $n$, chúng ta biết từ định lý Euler rằng $a ^ { \phi (n) } \equiv 1 \pmod n$, nên để kiểm tra xem $g$ có phải là căn nguyên thủy hay không, chỉ cần kiểm tra xem với mọi $d$ nhỏ hơn $\phi (n)$, $g^d \not \equiv 1 \pmod n$. Tuy nhiên, thuật toán này vẫn quá chậm.

Từ định lý Lagrange, chúng ta biết rằng chỉ số của 1 của bất kỳ số nào modulo $n$ phải là một ước số của $\phi (n)$. Do đó, là đủ để xác minh cho tất cả các ước số thực sự $d \mid \phi (n)$ rằng $g^d \not \equiv 1 \pmod n$. Đây đã là một thuật toán nhanh hơn nhiều, nhưng chúng ta vẫn có thể làm tốt hơn.

Phân tích thừa số $\phi (n) = p_1 ^ {a_1} \cdots p_s ^ {a_s}$. Chúng tôi chứng minh rằng trong thuật toán trước đó, chỉ cần xem xét các giá trị của $d$ có dạng $\frac { \phi (n) } {p_j}$. Thật vậy, giả sử $d$ là bất kỳ ước số thực sự nào của $\phi (n)$. Khi đó, rõ ràng, tồn tại $j$ sao cho $d \mid \frac { \phi (n) } {p_j}$, tức là $d \cdot k = \frac { \phi (n) } {p_j}$. Tuy nhiên, nếu $g^d \equiv 1 \pmod n$, chúng ta sẽ nhận được:

$g ^ { \frac { \phi (n)} {p_j} } \equiv g ^ {d \cdot k} \equiv (g^d) ^k \equiv 1^k \equiv 1 \pmod n$.

tức là trong số các số có dạng $\frac {\phi (n)} {p_i}$, sẽ có ít nhất một số sao cho các điều kiện không được đáp ứng.

Bây giờ chúng ta có một thuật toán hoàn chỉnh để tìm căn nguyên thủy:

* Đầu tiên, tìm $\phi (n)$ và phân tích thừa số nó.
* Sau đó lặp qua tất cả các số $g \in [1, n]$, và đối với mỗi số, để kiểm tra xem nó có phải là căn nguyên thủy hay không, chúng ta thực hiện như sau:

    * Tính tất cả $g ^ { \frac {\phi (n)} {p_i}} \pmod n$.
    * Nếu tất cả các giá trị được tính khác với $1$, thì $g$ là một căn nguyên thủy.

    Thời gian chạy của thuật toán này là $O(Ans \cdot \log \phi (n) \cdot \log n)$ (giả sử rằng $\phi (n)$ có $\log \phi (n)$ ước số).

Shoup (1990, 1992) đã chứng minh, giả sử [giả thuyết Riemann tổng quát](http://en.wikipedia.org/wiki/Generalized_Riemann_hypothesis), rằng $g$ là $O(\log^6 p)$.

## Cài đặt (Implementation) {: #implementation}

Mã sau đây giả định rằng modulo `p` là một số nguyên tố. Để làm cho nó hoạt động cho bất kỳ giá trị nào của `p`, chúng ta phải thêm tính toán của $\phi (p)$.

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

---

## Checklist

- Original lines: 97
- Translated lines: 97
- Code blocks changed? No
- Inline code changed? No
- Technical terms kept in English? Yes
- Headings anchors preserved/added correctly? Yes
- I confirm no character was omitted: YES
