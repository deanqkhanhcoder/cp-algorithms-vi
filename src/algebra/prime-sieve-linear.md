---
tags:
  - Translated
e_maxx_link: prime_sieve_linear
---

# Sàng tuyến tính

Cho một số $n$, tìm tất cả các số nguyên tố trong một đoạn $[2;n]$.

Cách tiêu chuẩn để giải quyết một nhiệm vụ là sử dụng [sàng Eratosthenes](sieve-of-eratosthenes.md). Thuật toán này rất đơn giản, nhưng nó có thời gian chạy là $O(n \log \log n)$.

Mặc dù có rất nhiều thuật toán đã biết với thời gian chạy dưới tuyến tính (tức là $o(n)$), thuật toán được mô tả dưới đây thú vị bởi sự đơn giản của nó: nó không phức tạp hơn sàng Eratosthenes cổ điển.

Bên cạnh đó, thuật toán được đưa ra ở đây tính toán **phân tích thừa số của tất cả các số** trong đoạn $[2; n]$ như một hiệu ứng phụ, và điều đó có thể hữu ích trong nhiều ứng dụng thực tế.

Điểm yếu của thuật toán đã cho là sử dụng nhiều bộ nhớ hơn sàng Eratosthenes cổ điển: nó đòi hỏi một mảng gồm $n$ số, trong khi đối với sàng Eratosthenes cổ điển, chỉ cần $n$ bit bộ nhớ là đủ (ít hơn 32 lần).

Do đó, chỉ có ý nghĩa khi sử dụng thuật toán được mô tả cho các số có bậc $10^7$ và không lớn hơn.

Thuật toán này là của Paul Pritchard. Nó là một biến thể của Thuật toán 3.3 trong (Pritchard, 1987: xem tài liệu tham khảo ở cuối bài viết).

## Thuật toán

Mục tiêu của chúng ta là tính toán **thừa số nguyên tố nhỏ nhất** $lp [i]$ cho mọi số $i$ trong đoạn $[2; n]$.

Bên cạnh đó, chúng ta cần lưu trữ danh sách tất cả các số nguyên tố đã tìm thấy - hãy gọi nó là $pr []$.

Chúng ta sẽ khởi tạo các giá trị $lp [i]$ bằng không, điều đó có nghĩa là chúng ta giả định tất cả các số đều là số nguyên tố. Trong quá trình thực hiện thuật toán, mảng này sẽ được điền dần.

Bây giờ chúng ta sẽ đi qua các số từ 2 đến $n$. Chúng ta có hai trường hợp cho số hiện tại $i$:

- $lp[i] = 0$ - điều đó có nghĩa là $i$ là số nguyên tố, tức là chúng ta chưa tìm thấy bất kỳ thừa số nào nhỏ hơn cho nó.  
  Do đó, chúng ta gán $lp [i] = i$ và thêm $i$ vào cuối danh sách $pr[]$.

- $lp[i] \neq 0$ - điều đó có nghĩa là $i$ là hợp số, và thừa số nguyên tố nhỏ nhất của nó là $lp [i]$.

Trong cả hai trường hợp, chúng ta cập nhật các giá trị của $lp []$ cho các số chia hết cho $i$. Tuy nhiên, mục tiêu của chúng ta là học cách làm như vậy để đặt một giá trị $lp []$ nhiều nhất một lần cho mỗi số. Chúng ta có thể làm như sau:

Hãy xem xét các số $x_j = i \cdot p_j$, trong đó $p_j$ là tất cả các số nguyên tố nhỏ hơn hoặc bằng $lp [i]$ (đây là lý do tại sao chúng ta cần lưu trữ danh sách tất cả các số nguyên tố).

Chúng ta sẽ đặt một giá trị mới $lp [x_j] = p_j$ cho tất cả các số có dạng này.

Chứng minh tính đúng đắn của thuật toán này và thời gian chạy của nó có thể được tìm thấy sau phần triển khai.

## Cài đặt

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

## Chứng minh tính đúng đắn

Chúng ta cần chứng minh rằng thuật toán đặt tất cả các giá trị $lp []$ một cách chính xác, và mỗi giá trị sẽ được đặt chính xác một lần. Do đó, thuật toán sẽ có thời gian chạy tuyến tính, vì tất cả các hành động còn lại của thuật toán, rõ ràng, hoạt động trong $O (n)$.

Lưu ý rằng mọi số $i$ có chính xác một biểu diễn dưới dạng:

$$i = lp [i] \cdot x,$$ 

trong đó $lp [i]$ là thừa số nguyên tố nhỏ nhất của $i$, và số $x$ không có bất kỳ thừa số nguyên tố nào nhỏ hơn $lp [i]$, tức là.

$$lp [i] \le lp [x].$$ 

Bây giờ, hãy so sánh điều này với các hành động của thuật toán của chúng ta: trên thực tế, đối với mọi $x$, nó đi qua tất cả các số nguyên tố mà nó có thể được nhân với, tức là tất cả các số nguyên tố cho đến $lp [x]$ bao gồm, để có được các số ở dạng đã cho ở trên.

Do đó, thuật toán sẽ đi qua mọi hợp số chính xác một lần, đặt các giá trị $lp []$ chính xác ở đó. Q.E.D.

## Thời gian chạy và bộ nhớ

Mặc dù thời gian chạy của $O(n)$ tốt hơn $O(n \log \log n)$ của sàng Eratosthenes cổ điển, sự khác biệt giữa chúng không quá lớn.
Trong thực tế, sàng tuyến tính chạy nhanh gần bằng một triển khai thông thường của sàng Eratosthenes.

So với các phiên bản tối ưu hóa của sàng Eratosthenes, ví dụ: sàng phân đoạn, nó chậm hơn nhiều.

Xem xét các yêu cầu về bộ nhớ của thuật toán này - một mảng $lp []$ có độ dài $n$, và một mảng của $pr []$ có độ dài  $rac n {\ln n}$, thuật toán này có vẻ tệ hơn sàng cổ điển về mọi mặt.

Tuy nhiên, phẩm chất cứu vãn của nó là thuật toán này tính toán một mảng $lp []$, cho phép chúng ta tìm phân tích thừa số của bất kỳ số nào trong đoạn $[2; n]$ trong thời gian bậc kích thước của phân tích thừa số này. Hơn nữa, chỉ cần sử dụng một mảng phụ sẽ cho phép chúng ta tránh các phép chia khi tìm phân tích thừa số.

Biết phân tích thừa số của tất cả các số là rất hữu ích cho một số nhiệm vụ, và thuật toán này là một trong số ít thuật toán cho phép tìm thấy chúng trong thời gian tuyến tính.

## Tài liệu tham khảo

- Paul Pritchard, **Linear Prime-Number Sieves: a Family Tree**, Science of Computer Programming, vol. 9 (1987), pp.17-35.