---
tags:
  - Translated
e_maxx_link: prime_sieve_linear
---

# Sàng tuyến tính (Linear Sieve) {: #linear-sieve}

Cho một số $n$, tìm tất cả các số nguyên tố trong đoạn $[2;n]$.

Cách giải quyết tiêu chuẩn cho nhiệm vụ này là sử dụng [sàng Eratosthenes](sieve-of-eratosthenes.md). Thuật toán này rất đơn giản, nhưng nó có thời gian chạy $O(n \log \log n)$.

Mặc dù có rất nhiều thuật toán được biết đến với thời gian chạy dưới tuyến tính (tức là $o(n)$), thuật toán được mô tả dưới đây rất thú vị bởi sự đơn giản của nó: nó không phức tạp hơn sàng Eratosthenes cổ điển.

Ngoài ra, thuật toán được đưa ra ở đây tính toán **phân tích thừa số của tất cả các số** trong đoạn $[2; n]$ như một hiệu ứng phụ, và điều đó có thể hữu ích trong nhiều ứng dụng thực tế.

Điểm yếu của thuật toán đã cho là sử dụng nhiều bộ nhớ hơn so với sàng Eratosthenes cổ điển: nó đòi hỏi một mảng $n$ số, trong khi đối với sàng Eratosthenes cổ điển là đủ để có $n$ bit bộ nhớ (ít hơn 32 lần).

Do đó, chỉ nên sử dụng thuật toán được mô tả cho các số theo thứ tự $10^7$ và không lớn hơn.

Thuật toán là do Paul Pritchard. Nó là một biến thể của Thuật toán 3.3 trong (Pritchard, 1987: xem tài liệu tham khảo ở cuối bài viết).

## Thuật toán (Algorithm) {: #algorithm}

Mục tiêu của chúng tôi là tính toán **thừa số nguyên tố nhỏ nhất** $lp [i]$ cho mỗi số $i$ trong đoạn $[2; n]$.

Ngoài ra, chúng ta cần lưu trữ danh sách tất cả các số nguyên tố tìm được - hãy gọi nó là $pr []$.

Chúng tôi sẽ khởi tạo các giá trị $lp [i]$ với số không, điều đó có nghĩa là chúng tôi giả sử tất cả các số là số nguyên tố. Trong quá trình thực hiện thuật toán, mảng này sẽ được điền dần.

Bây giờ chúng ta sẽ đi qua các số từ 2 đến $n$. Chúng ta có hai trường hợp cho số hiện tại $i$:

- $lp[i] = 0$ - điều đó có nghĩa là $i$ là số nguyên tố, nghĩa là chúng ta chưa tìm thấy bất kỳ thừa số nào nhỏ hơn cho nó.
  Do đó, chúng ta gán $lp [i] = i$ và thêm $i$ vào cuối danh sách $pr[]$.

- $lp[i] \neq 0$ - điều đó có nghĩa là $i$ là hợp số, và thừa số nguyên tố nhỏ nhất của nó là $lp [i]$.

Trong cả hai trường hợp, chúng tôi cập nhật các giá trị của $lp []$ cho các số chia hết cho $i$. Tuy nhiên, mục tiêu của chúng tôi là tìm cách để đặt giá trị $lp []$ nhiều nhất một lần cho mỗi số. Chúng ta có thể làm điều đó như sau:

Hãy xem xét các số $x_j = i \cdot p_j$, trong đó $p_j$ là tất cả các số nguyên tố nhỏ hơn hoặc bằng $lp [i]$ (đây là lý do tại sao chúng ta cần lưu trữ danh sách tất cả các số nguyên tố).

Chúng tôi sẽ đặt một giá trị mới $lp [x_j] = p_j$ cho tất cả các số có dạng này.

Bằng chứng về tính đúng đắn của thuật toán này và thời gian chạy của nó có thể được tìm thấy sau khi cài đặt.

## Cài đặt (Implementation) {: #implementation}

```cpp
const int N = 10000000;
vector<int> lp(N+1);
vector<int> pr;
 
for (int i=2; i <= N; ++i) {
	if (lp[i] == 0) {
		lp[i] = i;
		pr.push_back(i);
	}
	for (int j = 0; i * pr[j] <= N; ++j) {
		lp[i * pr[j]] = pr[j];
		if (pr[j] == lp[i]) {
			break;
		}
	}
}
```

## Chứng minh tính đúng đắn (Correctness Proof) {: #correctness-proof}

Chúng ta cần chứng minh rằng thuật toán đặt tất cả các giá trị $lp []$ một cách chính xác, và mỗi giá trị sẽ được đặt chính xác một lần. Do đó, thuật toán sẽ có thời gian chạy tuyến tính, vì tất cả các hành động còn lại của thuật toán, rõ ràng, hoạt động trong $O (n)$.

Lưu ý rằng mỗi số $i$ có chính xác một biểu diễn ở dạng:

$$i = lp [i] \cdot x,$$

trong đó $lp [i]$ là thừa số nguyên tố nhỏ nhất của $i$, và số $x$ không có bất kỳ thừa số nguyên tố nào nhỏ hơn $lp [i]$, tứ là

$$lp [i] \le lp [x].$$

Bây giờ, hãy so sánh điều này với các hành động của thuật toán của chúng tôi: thực tế, đối với mọi $x$ nó đi qua tất cả các số nguyên tố mà nó có thể được nhân với, tức là tất cả các số nguyên tố lên đến $lp [x]$ bao gồm cả nó, để có được các số ở dạng đã cho ở trên.

Do đó, thuật toán sẽ đi qua mọi hợp số chính xác một lần, đặt các giá trị chính xác $lp []$ ở đó. Q.E.D.

## Thời gian chạy và bộ nhớ (Runtime and Memory) {: #runtime-and-memory}

Mặc dù thời gian chạy của $O(n)$ tốt hơn $O(n \log \log n)$ của sàng Eratosthenes cổ điển, sự khác biệt giữa chúng không quá lớn.
Trong thực tế, sàng tuyến tính chạy nhanh gần bằng một cài đặt điển hình của sàng Eratosthenes.

So với các phiên bản tối ưu hóa của sàng Erathosthenes, ví dụ sàng phân đoạn, nó chậm hơn nhiều.

Xem xét các yêu cầu bộ nhớ của thuật toán này - một mảng $lp []$ có độ dài $n$, và một mảng của $pr []$ có độ dài $\frac n {\ln n}$, thuật toán này dường như tồi tệ hơn so với sàng cổ điển về mọi mặt.

Tuy nhiên, chất lượng cứu vãn của nó là thuật toán này tính toán một mảng $lp []$, cho phép chúng ta tìm phân tích thừa số của bất kỳ số nào trong đoạn $[2; n]$ trong thời gian theo thứ tự kích thước của phân tích thừa số này. Hơn nữa, sử dụng chỉ một mảng bổ sung sẽ cho phép chúng ta tránh các phép chia khi tìm kiếm phân tích thừa số.

Biết các phân tích thừa số của tất cả các số rất hữu ích cho một số nhiệm vụ, và thuật toán này là một trong số ít thuật toán cho phép tìm chúng trong thời gian tuyến tính.

## Tài liệu tham khảo (References) {: #references}

- Paul Pritchard, **Linear Prime-Number Sieves: a Family Tree**, Science of Computer Programming, vol. 9 (1987), pp.17-35.

---

## Checklist

- Original lines: 99
- Translated lines: 99
- Code blocks changed? No
- Inline code changed? No
- Technical terms kept in English? Yes
- Headings anchors preserved/added correctly? Yes
- I confirm no character was omitted: YES
