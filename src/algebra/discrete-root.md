---
tags:
  - Translated
e_maxx_link: discrete_root
---

# Căn rời rạc (Discrete Root) {: #discrete-root}

Bài toán tìm căn rời rạc được định nghĩa như sau. Cho số nguyên tố $n$ và hai số nguyên $a$ và $k$, tìm tất cả các $x$ sao cho:

$x^k \equiv a \pmod n$

## Thuật toán (The algorithm) {: #the-algorithm}

Chúng ta sẽ giải bài toán này bằng cách đưa nó về [bài toán logarit rời rạc](discrete-log.md).

Hãy áp dụng khái niệm [căn nguyên thủy](primitive-root.md) modulo $n$. Gọi $g$ là một căn nguyên thủy modulo $n$. Lưu ý rằng vì $n$ là số nguyên tố, nó phải tồn tại, và nó có thể được tìm thấy trong $O(Ans \cdot \log \phi (n) \cdot \log n) = O(Ans \cdot \log^2 n)$ cộng với thời gian phân tích thừa số $\phi (n)$.

Chúng ta có thể dễ dàng loại bỏ trường hợp $a = 0$. Trong trường hợp này, rõ ràng chỉ có một câu trả lời: $x = 0$.

Vì chúng ta biết rằng $n$ là số nguyên tố và bất kỳ số nào giữa 1 và $n-1$ đều có thể được biểu diễn dưới dạng lũy thừa của căn nguyên thủy, chúng ta có thể biểu diễn bài toán căn rời rạc như sau:

$(g^y)^k \equiv a \pmod n$

trong đó

$x \equiv g^y \pmod n$

Điều này, đến lượt nó, có thể được viết lại thành

$(g^k)^y \equiv a \pmod n$

Bây giờ chúng ta có một ẩn $y$, đây là bài toán logarit rời rạc. Nghiệm có thể được tìm thấy bằng cách sử dụng thuật toán baby-step giant-step của Shanks trong $O(\sqrt {n} \log n)$ (hoặc chúng ta có thể xác minh rằng không có nghiệm nào).

Sau khi tìm thấy một nghiệm $y_0$, một trong các nghiệm của bài toán căn rời rạc sẽ là $x_0 = g^{y_0} \pmod n$.

## Tìm tất cả nghiệm từ một nghiệm đã biết {: #finding-all-solutions-from-one-known-solution}

Để giải bài toán đã cho một cách đầy đủ, chúng ta cần tìm tất cả các nghiệm khi biết một trong số chúng: $x_0 = g^{y_0} \pmod n$.

Hãy nhớ lại thực tế rằng một căn nguyên thủy luôn có cấp là $\phi (n)$, tức là lũy thừa nhỏ nhất của $g$ cho kết quả 1 là $\phi (n)$. Do đó, nếu chúng ta thêm số hạng $\phi (n)$ vào số mũ, chúng ta vẫn nhận được cùng một giá trị:

$x^k \equiv g^{ y_0 \cdot k + l \cdot \phi (n)} \equiv a \pmod n \forall l \in Z$

Do đó, tất cả các nghiệm đều có dạng:

$x = g^{y_0 + \frac {l \cdot \phi (n)}{k}} \pmod n \forall l \in Z$.

trong đó $l$ được chọn sao cho phân số phải là một số nguyên. Để điều này đúng, tử số phải chia hết cho bội chung nhỏ nhất của $\phi (n)$ và $k$. Hãy nhớ rằng bội chung nhỏ nhất của hai số $lcm(a, b) = \frac{a \cdot b}{gcd(a, b)}$; chúng ta sẽ nhận được

$x = g^{y_0 + i \frac {\phi (n)}{gcd(k, \phi (n))}} \pmod n \forall i \in Z$.

Đây là công thức cuối cùng cho tất cả các nghiệm của bài toán căn rời rạc.

## Cài đặt (Implementation) {: #implementation}

Dưới đây là một cài đặt đầy đủ, bao gồm các thủ tục tìm căn nguyên thủy, logarit rời rạc và tìm và in tất cả các nghiệm.

```cpp
int gcd(int a, int b) {
	return a ? gcd(b % a, a) : b;
}
 
int powmod(int a, int b, int p) {
	int res = 1;
	while (b > 0) {
		if (b & 1) {
			res = res * a % p;
		}
		a = a * a % p;
		b >>= 1;
	}
	return res;
}
 
// Finds the primitive root modulo p
int generator(int p) {
	vector<int> fact;
	int phi = p-1, n = phi;
	for (int i = 2; i * i <= n; ++i) {
		if (n % i == 0) {
			fact.push_back(i);
			while (n % i == 0)
				n /= i;
		}
	}
	if (n > 1)
		fact.push_back(n);
 
	for (int res = 2; res <= p; ++res) {
		bool ok = true;
		for (int factor : fact) {
			if (powmod(res, phi / factor, p) == 1) {
				ok = false;
				break;
			}
		}
		if (ok) return res;
	}
	return -1;
}
 
// This program finds all numbers x such that x^k = a (mod n)
int main() {
	int n, k, a;
	scanf("%d %d %d", &n, &k, &a);
	if (a == 0) {
		puts("1\n0");
		return 0;
	}
 
	int g = generator(n);
 
	// Baby-step giant-step discrete logarithm algorithm
	int sq = (int) sqrt (n + .0) + 1;
	vector<pair<int, int>> dec(sq);
	for (int i = 1; i <= sq; ++i)
		dec[i-1] = {powmod(g, i * sq * k % (n - 1), n), i};
	sort(dec.begin(), dec.end());
	int any_ans = -1;
	for (int i = 0; i < sq; ++i) {
		int my = powmod(g, i * k % (n - 1), n) * a % n;
		auto it = lower_bound(dec.begin(), dec.end(), make_pair(my, 0));
		if (it != dec.end() && it->first == my) {
			any_ans = it->second * sq - i;
			break;
		}
	}
	if (any_ans == -1) {
		puts("0");
		return 0;
	}
 
	// Print all possible answers
	int delta = (n-1) / gcd(k, n-1);
	vector<int> ans;
	for (int cur = any_ans % delta; cur < n-1; cur += delta)
		ans.push_back(powmod(g, cur, n));
	sort(ans.begin(), ans.end());
	printf("%d\n", ans.size());
	for (int answer : ans)
		printf("%d ", answer);
}
```

## Bài tập luyện tập {: #practice-problems}

* [Codeforces - Lunar New Year and a Recursive Sequence](https://codeforces.com/contest/1106/problem/F)
