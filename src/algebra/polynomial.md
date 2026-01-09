---
tags:
  - Original
---

# Các phép toán trên đa thức và chuỗi (Operations on polynomials and series) {: #operations-on-polynomials-and-series}

Các bài toán trong lập trình thi đấu, đặc biệt là các bài toán liên quan đến liệt kê một loại nào đó, thường được giải quyết bằng cách đưa bài toán về tính toán trên đa thức và chuỗi lũy thừa hình thức.

Điều này bao gồm các khái niệm như nhân đa thức, nội suy, và những cái phức tạp hơn, như logarit và hàm mũ của đa thức. Trong bài viết này, một cái nhìn tổng quan ngắn gọn về các phép toán như vậy và các cách tiếp cận phổ biến cho chúng được trình bày.

## Khái niệm cơ bản và sự thật (Basic Notion and facts) {: #basic-notion-and-facts}

Trong phần này, chúng tôi tập trung nhiều hơn vào các định nghĩa và tính chất "trực quan" của các phép toán đa thức khác nhau. Các chi tiết kỹ thuật về việc cài đặt và độ phức tạp của chúng sẽ được đề cập trong các phần sau.

### Nhân đa thức (Polynomial multiplication) {: #polynomial-multiplication}

!!! info "Định nghĩa"
	**Đa thức một biến (Univariate polynomial)** là một biểu thức có dạng $A(x) = a_0 + a_1 x + \dots + a_n x^n$.

Các giá trị $a_0, \dots, a_n$ là các hệ số đa thức, thường được lấy từ một tập hợp số hoặc cấu trúc giống số nào đó. Trong bài viết này, chúng tôi giả sử rằng các hệ số được lấy từ một [trường (field)](https://en.wikipedia.org/wiki/Field_(mathematics)) nào đó, nghĩa là các phép toán cộng, trừ, nhân và chia được xác định rõ ràng cho chúng (ngoại trừ phép chia cho $0$) và chúng thường cư xử theo cách tương tự như số thực.
	
Ví dụ điển hình của trường như vậy là trường các số dư modulo số nguyên tố $p$.

Để đơn giản, chúng tôi sẽ bỏ thuật ngữ _một biến_, vì đây là loại đa thức duy nhất chúng tôi xem xét trong bài viết này. Chúng tôi cũng sẽ viết $A$ thay vì $A(x)$ bất cứ khi nào có thể, điều này sẽ dễ hiểu từ ngữ cảnh. Giả sử rằng hoặc $a_n \neq 0$ hoặc $A(x)=0$.

!!! info "Định nghĩa"
	**Tích** của hai đa thức được định nghĩa bằng cách khai triển nó như một biểu thức số học:

	$$
	A(x) B(x) = \left(\sum\limits_{i=0}^n a_i x^i \right)\left(\sum\limits_{j=0}^m b_j x^j\right) = \sum\limits_{i,j} a_i b_j x^{i+j} = \sum\limits_{k=0}^{n+m} c_k x^k = C(x).
	$$

	Dãy $c_0, c_1, \dots, c_{n+m}$ của các hệ số của $C(x)$ được gọi là **tích chập (convolution)** của $a_0, \dots, a_n$ và $b_0, \dots, b_m$.

!!! info "Định nghĩa"
	**Bậc** của một đa thức $A$ với $a_n \neq 0$ được định nghĩa là $\deg A = n$.
	
	Để nhất quán, bậc của $A(x) = 0$ được định nghĩa là $\deg A = -\infty$.

Theo khái niệm này, $\deg AB = \deg A + \deg B$ cho bất kỳ đa thức $A$ và $B$ nào.

Tích chập là cơ sở để giải quyết nhiều bài toán liệt kê.

!!! Example "Ví dụ"
	Bạn có $n$ vật thể loại thứ nhất và $m$ vật thể loại thứ hai.

	Các vật thể loại thứ nhất có giá trị $a_1, \dots, a_n$, và các vật thể loại thứ hai có giá trị $b_1, \dots, b_m$.

	Bạn chọn một vật thể loại thứ nhất và một vật thể loại thứ hai. Có bao nhiêu cách để có được tổng giá trị là $k$?

??? hint "Lời giải"
	Xem xét tích $(x^{a_1} + \dots + x^{a_n})(x^{b_1} + \dots + x^{b_m})$. Nếu bạn khai triển nó, mỗi đơn thức sẽ tương ứng với cập $(a_i, b_j)$ và đóng góp vào hệ số gần $x^{a_i+b_j}$. Nói cách khác, câu trả lời là hệ số gần $x^k$ trong tích.

!!! Example "Ví dụ"
	Bạn gieo một xúc xắc $6$ mặt $n$ lần và tính tổng kết quả từ tất cả các lần gieo. Xác suất để nhận được tổng $k$ là bao nhiêu?

??? hint "Lời giải"
	Câu trả lời là số lượng kết quả có tổng $k$, chia cho tổng số kết quả, đó là $6^n$.

	Số lượng kết quả có tổng $k$ là bao nhiêu? Với $n=1$, nó có thể được biểu diễn bởi một đa thức $A(x) = x^1+x^2+\dots+x^6$.

	Với $n=2$, sử dụng cùng cách tiếp cận như ví dụ trên, chúng tôi kết luận rằng nó được biểu diễn bởi đa thức $(x^1+x^2+\dots+x^6)^2$.

	Như vậy, câu trả lời cho bài toán là hệ số thứ $k$ của $(x^1+x^2+\dots+x^6)^n$, chia cho $6^n$.

Hệ số gần $x^k$ trong đa thức $A(x)$ được ký hiệu ngắn gọn là $[x^k]A$.

### Chuỗi lũy thừa hình thức (Formal power series) {: #formal-power-series}

!!! info "Định nghĩa"
	Một **chuỗi lũy thừa hình thức** là một tổng vô hạn $A(x) = a_0 + a_1 x + a_2 x^2 + \dots$, được xem xét bất kể tính chất hội tụ của nó.

Nói cách khác, khi chúng ta xem xét ví dụ một tổng $1+\frac{1}{2}+\frac{1}{4}+\frac{1}{8}+\dots=2$, chúng ta ngụ ý rằng nó _hội tụ_ về $2$ khi số lượng số hạng tiến tới vô cùng. Tuy nhiên, chuỗi hình thức chỉ được xem xét dưới dạng các dãy tạo nên chúng.

!!! info "Định nghĩa"
	**Tích** của chuỗi lũy thừa hình thức $A(x)$ và $B(x)$, cũng được định nghĩa bằng cách khai triển nó như một biểu thức số học:


	$$
	A(x) B(x) = \left(\sum\limits_{i=0}^\infty a_i x^i \right)\left(\sum\limits_{j=0}^\infty b_j x^j\right) = \sum\limits_{i,j} a_i b_j x^{i+j} = \sum\limits_{k=0}^{\infty} c_k x^k = C(x),
	$$

	trong đó các hệ số $c_0, c_1, \dots$ được định nghĩa là các tổng hữu hạn

	$$
	c_k = \sum\limits_{i=0}^k a_i b_{k-i}.
	$$

	Dãy $c_0, c_1, \dots$ cũng được gọi là một **tích chập (convolution)** của $a_0, a_1, \dots$ và $b_0, b_1, \dots$, khái quát hóa khái niệm cho các dãy vô hạn.

Do đó, các đa thức có thể được coi là chuỗi lũy thừa hình thức, nhưng với số lượng hữu hạn các hệ số.

Chuỗi lũy thừa hình thức đóng một vai trò quan trọng trong tổ hợp liệt kê, nơi chúng được nghiên cứu như là [hàm sinh](https://en.wikipedia.org/wiki/Generating_function) cho các dãy khác nhau. Thật không may, giải thích chi tiết về hàm sinh và trực giác đằng sau chúng sẽ nằm ngoài phạm vi của bài viết này, do đó độc giả tò mò được tham khảo ví dụ [tại đây](https://codeforces.com/blog/entry/103979) để biết chi tiết về ý nghĩa tổ hợp của chúng.

Tuy nhiên, chúng tôi sẽ đề cập rất ngắn gọn rằng nếu $A(x)$ và $B(x)$ là các hàm sinh cho các dãy liệt kê một số vật thể theo số lượng "nguyên tử" trong chúng (ví dụ: cây theo số lượng đỉnh), thì tích $A(x) B(x)$ liệt kê các vật thể có thể được mô tả như là các cặp vật thể của loại $A$ và $B$, liệt kê theo tổng số lượng "nguyên tử" trong cặp.

!!! Example "Ví dụ"
	Gọi $A(x) = \sum\limits_{i=0}^\infty 2^i x^i$ liệt kê các gói đá, mỗi viên đá được tô bằng một trong $2$ màu (vì vậy, có $2^i$ gói như vậy kích thước $i$) và $B(x) = \sum\limits_{j=0}^{\infty} 3^j x^j$ liệt kê các gói đá, mỗi viên đá được tô bằng một trong $3$ màu. Khi đó $C(x) = A(x) B(x) = \sum\limits_{k=0}^\infty c_k x^k$ sẽ liệt kê các vật thể có thể được mô tả là "hai gói đá, gói thứ nhất chỉ gồm các viên đá loại $A$, gói thứ hai chỉ gồm các viên đá loại $B$, với tổng số viên đá là $k$" cho $c_k$.

Tương tự, có một ý nghĩa trực quan đối với một số hàm khác trên chuỗi lũy thừa hình thức.

### Chia đa thức (Long polynomial division) {: #long-polynomial-division}

Tương tự như số nguyên, có thể định nghĩa phép chia dài trên đa thức.

!!! info "Định nghĩa"

	Đối với bất kỳ đa thức $A$ và $B \neq 0$ nào, người ta có thể biểu diễn $A$ dưới dạng

	$$
	A = D \cdot B + R,~ \deg R < \deg B,
	$$

	trong đó $R$ được gọi là **phần dư (remainder)** của $A$ modulo $B$ và $D$ được gọi là **thương (quotient)**.

Gọi $\deg A = n$ và $\deg B = m$, cách ngây thơ để làm điều đó là sử dụng phép chia dài, trong đó bạn nhân $B$ với đơn thức $\frac{a_n}{b_m} x^{n - m}$ và trừ nó khỏi $A$, cho đến khi bậc của $A$ nhỏ hơn bậc của $B$. Những gì còn lại của $A$ cuối cùng sẽ là phần dư (do đó có tên gọi như vậy), và các đa thức mà bạn đã nhân $B$ trong quá trình đó, cộng lại với nhau, tạo thành thương.

!!! info "Định nghĩa"
	Nếu $A$ và $B$ có cùng phần dư modulo $C$, chúng được gọi là **tương đương** modulo $C$, được ký hiệu là
	
	$$
	A \equiv B \pmod{C}.
	$$
	
Phép chia đa thức dài hữu ích vì nhiều tính chất quan trọng của nó:

- $A$ là bội của $B$ khi và chỉ khi $A \equiv 0 \pmod B$.

- Nó ngụ ý rằng $A \equiv B \pmod C$ khi và chỉ khi $A-B$ là bội của $C$.

- Cụ thể, $A \equiv B \pmod{C \cdot D}$ ngụ ý $A \equiv B \pmod{C}$.

- Đối với bất kỳ đa thức tuyến tính $x-r$ nào, điều này giữ đúng $A(x) \equiv A(r) \pmod{x-r}$.

- Nó ngụ ý rằng $A$ là bội của $x-r$ khi và chỉ khi $A(r)=0$.

- Đối với modulo là $x^k$, điều này giữ đúng $A \equiv a_0 + a_1 x + \dots + a_{k-1} x^{k-1} \pmod{x^k}$.

Lưu ý rằng phép chia dài không thể được định nghĩa đúng cho chuỗi lũy thừa hình thức. Thay vào đó, đối với bất kỳ $A(x)$ nào sao cho $a_0 \neq 0$, có thể định nghĩa một chuỗi lũy thừa hình thức nghịch đảo $A^{-1}(x)$, sao cho $A(x) A^{-1}(x) = 1$. Thực tế này, đến lượt nó, có thể được sử dụng để tính kết quả của phép chia dài cho các đa thức.

## Cài đặt cơ bản (Basic implementation) {: #basic-implementation}
[Tại đây](https://cp-algorithms.github.io/cp-algorithms-aux/cp-algo/math/poly.hpp) bạn có thể tìm thấy cài đặt cơ bản của đại số đa thức.

Nó hỗ trợ tất cả các phép toán tầm thường và một số phương thức hữu ích khác. Class chính là `poly<T>` cho các đa thức với các hệ số kiểu `T`.

Tất cả các phép toán số học `+`, `-`, `*`, `%` và `/` đều được hỗ trợ, `%` và `/` đại diện cho phần dư và thương trong phép chia Euclid.

Ngoài ra còn có class `modular<m>` để thực hiện các phép toán số học trên các phần dư modulo một số nguyên tố `m`.

Các hàm hữu ích khác:

- `deriv()`: tính đạo hàm $P'(x)$ của $P(x)$.
- `integr()`: tính tích phân bất định $Q(x) = \int P(x)$ của $P(x)$ sao cho $Q(0)=0$.
- `inv(size_t n)`: tính $n$ hệ số đầu tiên của $P^{-1}(x)$ trong $O(n \log n)$.
- `log(size_t n)`: tính $n$ hệ số đầu tiên của $\ln P(x)$ trong $O(n \log n)$.
- `exp(size_t n)`: tính $n$ hệ số đầu tiên của $\exp P(x)$ trong $O(n \log n)$.
- `pow(size_t k, size_t n)`: tính $n$ hệ số đầu tiên cho $P^{k}(x)$ trong $O(n \log nk)$.
- `deg()`: trả về bậc của $P(x)$.
- `lead()`: trả về hệ số của $x^{\deg P(x)}$.
- `resultant(poly<T> a, poly<T> b)`: tính kết thức của $a$ và $b$ trong $O(|a| \cdot |b|)$.
- `bpow(T x, size_t n)`: tính $x^n$.
- `bpow(T x, size_t n, T m)`: tính $x^n \pmod{m}$.
- `chirpz(T z, size_t n)`: tính $P(1), P(z), P(z^2), \dots, P(z^{n-1})$ trong $O(n \log n)$.
- `vector<T> eval(vector<T> x)`: đánh giá $P(x_1), \dots, P(x_n)$ trong $O(n \log^2 n)$.
- `poly<T> inter(vector<T> x, vector<T> y)`: nội suy một đa thức bởi một tập hợp các cặp $P(x_i) = y_i$ trong $O(n \log^2 n)$.
- Và nhiều hơn nữa, hãy thoải mái khám phá mã!

## Số học (Arithmetic) {: #arithmetic}

### Phép nhân (Multiplication) {: #multiplication}

Phép toán cốt lõi là phép nhân của hai đa thức. Nghĩa là, cho các đa thức $A$ và $B$:

$$A = a_0 + a_1 x + \dots + a_n x^n$$

$$B = b_0 + b_1 x + \dots + b_m x^m$$

Bạn phải tính đa thức $C = A \cdot B$, được định nghĩa là

$$\boxed{C = \sum\limits_{i=0}^n \sum\limits_{j=0}^m a_i b_j x^{i+j}}  = c_0 + c_1 x + \dots + c_{n+m} x^{n+m}.$$

Nó có thể được tính trong $O(n \log n)$ thông qua [Biến đổi Fourier nhanh](fft.md) và hầu như tất cả các phương pháp ở đây sẽ sử dụng nó như chương trình con.

### Chuỗi nghịch đảo (Inverse series) {: #inverse-series}

Nếu $A(0) \neq 0$ luôn tồn tại một chuỗi lũy thừa hình thức vô hạn $A^{-1}(x) = q_0+q_1 x + q_2 x^2 + \dots$ sao cho $A^{-1} A = 1$. Thường hữu ích khi tính $k$ hệ số đầu tiên của $A^{-1}$ (nghĩa là, tính nó modulo $x^k$). Có hai cách chính để tính nó.

#### Chia để trị (Divide and conquer) {: #divide-and-conquer}

Thuật toán này đã được đề cập trong [bài viết của Schönhage](http://algo.inria.fr/seminars/sem00-01/schoenhage.pdf) và được lấy cảm hứng từ [phương pháp Graeffe](https://en.wikipedia.org/wiki/Graeffe's_method). Được biết rằng đối với $B(x)=A(x)A(-x)$ điều này giữ đúng $B(x)=B(-x)$, nghĩa là, $B(x)$ là một đa thức chẵn. Nó có nghĩa là nó chỉ có các hệ số khác không với số mũ chẵn và có thể được biểu diễn dưới dạng $B(x)=T(x^2)$. Do đó, chúng ta có thể thực hiện chuyển đổi sau:

$$A^{-1}(x) \equiv \frac{1}{A(x)} \equiv \frac{A(-x)}{A(x)A(-x)} \equiv \frac{A(-x)}{T(x^2)} \pmod{x^k}$$

Lưu ý rằng $T(x)$ có thể được tính bằng một phép nhân duy nhất, sau đó chúng ta chỉ quan tâm đến nửa đầu của các hệ số của chuỗi nghịch đảo của nó. Điều này làm giảm hiệu quả bài toán ban đầu về việc tính $A^{-1} \pmod{x^k}$ thành tính $T^{-1} \pmod{x^{\lceil k / 2 \rceil}}$.

Độ phức tạp của phương pháp này có thể được ước tính là

$$T(n) = T(n/2) + O(n \log n) = O(n \log n).$$

#### Thuật toán Sieveking–Kung (Sieveking–Kung algorithm) {: #sieveking-kung-algorithm}

Quy trình chung được mô tả ở đây được gọi là nâng Hensel (Hensel lifting), vì nó tuân theo bổ đề Hensel. Chúng tôi sẽ đề cập chi tiết hơn ở phần dưới, nhưng bây giờ hãy tập trung vào giải pháp ad hoc. Phần "nâng" ở đây có nghĩa là chúng ta bắt đầu với xấp xỉ $B_0=q_0=a_0^{-1}$, đó là $A^{-1} \pmod x$ và sau đó lặp đi lặp lại nâng từ $\bmod x^a$ lên $\bmod x^{2a}$.

Gọi $B_k \equiv A^{-1} \pmod{x^a}$. Xấp xỉ tiếp theo cần tuân theo phương trình $A B_{k+1} \equiv 1 \pmod{x^{2a}}$ và có thể được biểu diễn dưới dạng $B_{k+1} = B_k + x^a C$. Từ đây suy ra phương trình

$$A(B_k + x^{a}C) \equiv 1 \pmod{x^{2a}}.$$

Gọi $A B_k \equiv 1 + x^a D \pmod{x^{2a}}$, thì phương trình trên ngụ ý

$$x^a(D+AC) \equiv 0 \pmod{x^{2a}} \implies D \equiv -AC \pmod{x^a} \implies C \equiv -B_k D \pmod{x^a}.$$

Từ đây, người ta có thể thu được công thức cuối cùng, đó là

$$x^a C \equiv -B_k x^a D  \equiv B_k(1-AB_k) \pmod{x^{2a}} \implies \boxed{B_{k+1} \equiv B_k(2-AB_k) \pmod{x^{2a}}}$$

Do đó bắt đầu với $B_0 \equiv a_0^{-1} \pmod x$ chúng ta sẽ tính toán dãy $B_k$ sao cho $AB_k \equiv 1 \pmod{x^{2^k}}$ với độ phức tạp

$$T(n) = T(n/2) + O(n \log n) = O(n \log n).$$

Thuật toán ở đây có vẻ phức tạp hơn một chút so với thuật toán đầu tiên, nhưng nó có một lý luận rất vững chắc và thực tế đằng sau nó, cũng như tiềm năng tổng quát hóa lớn nếu nhìn từ một góc độ khác, sẽ được giải thích thêm ở phần dưới.

### Phép chia Euclid (Euclidean division) {: #euclidean-division}

Xét hai đa thức $A(x)$ và $B(x)$ có bậc $n$ và $m$. Như đã nói trước đó, bạn có thể viết lại $A(x)$ thành

$$A(x) = B(x) D(x) + R(x), \deg R < \deg B.$$

Gọi $n \geq m$, nó sẽ ngụ ý rằng $\deg D = n - m$ và $n-m+1$ hệ số dẫn đầu của $A$ không ảnh hưởng đến $R$. Nó có nghĩa là bạn có thể khôi phục $D(x)$ từ $n-m+1$ hệ số lớn nhất của $A(x)$ và $B(x)$ nếu bạn coi nó như một hệ phương trình.

Hệ phương trình tuyến tính chúng ta đang nói đến có thể được viết dưới dạng sau:

$$\begin{bmatrix} a_n \\ \vdots \\ a_{m+1} \\ a_{m} \end{bmatrix} = \begin{bmatrix}
b_m & \dots & 0 & 0 \\
\vdots & \ddots & \vdots & \vdots \\
\dots & \dots & b_m & 0 \\
\dots & \dots & b_{m-1} & b_m
\end{bmatrix} \begin{bmatrix}d_{n-m} \\ \vdots \\ d_1 \\ d_0\end{bmatrix}$$

Từ vẻ ngoài của nó, chúng ta có thể kết luận rằng với sự ra đời của các đa thức đảo ngược

$$A^R(x) = x^nA(x^{-1})= a_n + a_{n-1} x + \dots + a_0 x^n$$

$$B^R(x) = x^m B(x^{-1}) = b_m + b_{m-1} x + \dots + b_0 x^m$$

$$D^R(x) = x^{n-m}D(x^{-1}) = d_{n-m} + d_{n-m-1} x + \dots + d_0 x^{n-m}$$

hệ thống có thể được viết lại thành

$$A^R(x) \equiv B^R(x) D^R(x) \pmod{x^{n-m+1}}.$$

Từ đây bạn có thể khôi phục tất cả các hệ số của $D(x)$ một cách rõ ràng:

$$\boxed{D^R(x) \equiv A^R(x) (B^R(x))^{-1} \pmod{x^{n-m+1}}}$$

Và từ đây, đến lượt nó, bạn có thể khôi phục $R(x)$ dưới dạng $R(x) = A(x) - B(x)D(x)$.

Lưu ý rằng ma trận ở trên được gọi là [ma trận Toeplitz](https://en.wikipedia.org/wiki/Toeplitz_matrix) tam giác và, như chúng ta thấy ở đây, việc giải hệ phương trình tuyến tính với ma trận Toeplitz tùy ý, thực tế, tương đương với phép đảo ngược đa thức. Hơn nữa, ma trận nghịch đảo của nó cũng sẽ là ma trận Toeplitz tam giác và các mục của nó, theo thuật ngữ được sử dụng ở trên, là các hệ số của $(B^R(x))^{-1} \pmod{x^{n-m+1}}$.

## Tính toán các hàm của đa thức (Calculating functions of polynomial) {: #calculating-functions-of-polynomial}

### Phương pháp Newton (Newton's method) {: #newtons-method}

Hãy tổng quát hóa thuật toán Sieveking–Kung. Xét phương trình $F(P) = 0$ trong đó $P(x)$ phải là một đa thức và $F(x)$ là một hàm giá trị đa thức nào đó được định nghĩa là

$$F(x) = \sum\limits_{i=0}^\infty \alpha_i (x-\beta)^i,$$

trong đó $\beta$ là một hằng số nào đó. Có thể chứng minh rằng nếu chúng ta giới thiệu một biến hình thức mới $y$, chúng ta có thể biểu diễn $F(x)$ dưới dạng

$$F(x) = F(y) + (x-y)F'(y) + (x-y)^2 G(x,y),$$

trong đó $F'(x)$ là chuỗi lũy thừa hình thức đạo hàm được định nghĩa là

$$F'(x) = \sum\limits_{i=0}^\infty (i+1)\alpha_{i+1}(x-\beta)^i,$$

và $G(x, y)$ là một chuỗi lũy thừa hình thức nào đó của $x$ và $y$. Với kết quả này, chúng ta có thể tìm nghiệm lặp đi lặp lại.

Gọi $F(Q_k) \equiv 0 \pmod{x^{a}}$. Chúng ta cần tìm $Q_{k+1} \equiv Q_k + x^a C \pmod{x^{2a}}$ sao cho $F(Q_{k+1}) \equiv 0 \pmod{x^{2a}}$.

Thay thế $x = Q_{k+1}$ và $y=Q_k$ trong công thức trên, chúng ta nhận được

$$F(Q_{k+1}) \equiv F(Q_k) + (Q_{k+1} - Q_k) F'(Q_k) + (Q_{k+1} - Q_k)^2 G(x, y) \pmod x^{2a}.$$

Vì $Q_{k+1} - Q_k \equiv 0 \pmod{x^a}$, điều đó cũng giữ đúng rằng $(Q_{k+1} - Q_k)^2 \equiv 0 \pmod{x^{2a}}$, do đó

$$0 \equiv F(Q_{k+1}) \equiv F(Q_k) + (Q_{k+1} - Q_k) F'(Q_k) \pmod{x^{2a}}.$$

Công thức cuối cùng cho chúng ta giá trị của $Q_{k+1}$:

$$\boxed{Q_{k+1} = Q_k - \dfrac{F(Q_k)}{F'(Q_k)} \pmod{x^{2a}}}$$

Do đó, biết cách đảo ngược đa thức và cách tính $F(Q_k)$, chúng ta có thể tìm $n$ hệ số của $P$ với độ phức tạp

$$T(n) = T(n/2) + f(n),$$

trong đó $f(n)$ là thời gian cần thiết để tính $F(Q_k)$ và $F'(Q_k)^{-1}$ thường là $O(n \log n)$.

Quy tắc lặp trên được gọi trong phân tích số là [Phương pháp Newton](https://en.wikipedia.org/wiki/Newton%27s_method).

#### Bổ đề Hensel (Hensel's lemma) {: #hensels-lemma}

Như đã đề cập trước đó, về mặt hình thức và tổng quát kết quả này được gọi là [Bổ đề Hensel](https://en.wikipedia.org/wiki/Hensel%27s_lemma) và nó thực tế có thể được sử dụng theo nghĩa rộng hơn nữa khi chúng ta làm việc với một chuỗi các vành lồng nhau. Trong trường hợp cụ thể này, chúng ta đã làm việc với một chuỗi các phần dư đa thức modulo $x$, $x^2$, $x^3$, v.v.

Một ví dụ khác mà việc nâng Hensel có thể hữu ích là cái gọi là [số p-adic](https://en.wikipedia.org/wiki/P-adic_number) nơi chúng ta, thực tế, làm việc với dãy các phần dư số nguyên modulo $p$, $p^2$, $p^3$, v.v. Ví dụ, phương pháp Newton có thể được sử dụng để tìm tất cả các [số tự đồng cấu (automorphic numbers)](https://en.wikipedia.org/wiki/Automorphic_number) (các số có tận cùng là chính nó khi bình phương) với một cơ số đã cho. Bài toán được để lại như một bài tập cho người đọc. Bạn có thể xem xét bài toán [này](https://acm.timus.ru/problem.aspx?space=1&num=1698) để kiểm tra xem giải pháp của bạn có hoạt động cho các số cơ số $10$ hay không.

### Logarit (Logarithm) {: #logarithm}

Đối với hàm $\ln P(x)$ được biết rằng: 

$$
\boxed{(\ln P(x))' = \dfrac{P'(x)}{P(x)}}
$$

Do đó chúng ta có thể tính $n$ hệ số của $\ln P(x)$ trong $O(n \log n)$.

### Chuỗi nghịch đảo (Inverse series) {: #inverse-series-1}

Turns out, chúng ta có thể nhận được công thức cho $A^{-1}$ bằng cách sử dụng phương pháp Newton.
Đối với điều này chúng ta lấy phương trình $A=Q^{-1}$, do đó:

$$F(Q) = Q^{-1} - A$$

$$F'(Q) = -Q^{-2}$$

$$\boxed{Q_{k+1} \equiv Q_k(2-AQ_k) \pmod{x^{2^{k+1}}}}$$

### Hàm mũ (Exponent) {: #exponent}

Hãy tìm hiểu cách tính $e^{P(x)}=Q(x)$. Điều đó phải giữ đúng rằng $\ln Q = P$, do đó:

$$F(Q) = \ln Q - P$$

$$F'(Q) = Q^{-1}$$

$$\boxed{Q_{k+1} \equiv Q_k(1 + P - \ln Q_k) \pmod{x^{2^{k+1}}}}$$

### Lũy thừa thứ $k$ ($k$-th power) {: #k-th-power data-toc-label="k-th power"}

Bây giờ chúng ta cần tính $P^k(x)=Q$. Điều này có thể được thực hiện thông qua công thức sau:

$$Q = \exp\left[k \ln P(x)\right]$$

Tuy nhiên hãy lưu ý rằng, bạn có thể tính logarit và hàm mũ một cách chính xác chỉ khi bạn có thể tìm thấy một số $Q_0$ ban đầu.

Để tìm nó, bạn nên tính logarit hoặc hàm mũ của hệ số hằng số của đa thức.

Nhưng cách hợp lý duy nhất để làm điều đó là nếu $P(0)=1$ cho $Q = \ln P$ để $Q(0)=0$ và nếu $P(0)=0$ cho $Q = e^P$ để $Q(0)=1$.

Do đó bạn có thể sử dụng công thức trên chỉ nếu $P(0) = 1$. Nếu không, nếu $P(x) = \alpha x^t T(x)$ trong đó $T(0)=1$ bạn có thể viết rằng:

$$\boxed{P^k(x) = \alpha^kx^{kt} \exp[k \ln T(x)]}$$

Lưu ý rằng bạn cũng có thể tính một số căn bậc $k$ của một đa thức nếu bạn có thể tính $\sqrt[k]{\alpha}$, ví dụ cho $\alpha=1$.

## Đánh giá và Nội suy (Evaluation and Interpolation) {: #evaluation-and-interpolation}

### Biến đổi Chirp-z (Chirp-z Transform) {: #chirp-z-transform}

Đối với trường hợp cụ thể khi bạn cần đánh giá một đa thức tại các điểm $x_r = z^{2r}$ bạn có thể thực hiện những điều sau:

$$A(z^{2r}) = \sum\limits_{k=0}^n a_k z^{2kr}$$

Hãy thay thế $2kr = r^2+k^2-(r-k)^2$. Khi đó tổng này viết lại thành:

$$\boxed{A(z^{2r}) = z^{r^2}\sum\limits_{k=0}^n (a_k z^{k^2}) z^{-(r-k)^2}}$$

Điều này lên đến hệ số $z^{r^2}$ bằng với tích chập của các dãy $u_k = a_k z^{k^2}$ và $v_k = z^{-k^2}$.

Lưu ý rằng $u_k$ có chỉ số từ $0$ đến $n$ ở đây và $v_k$ có chỉ số từ $-n$ đến $m$ trong đó $m$ là lũy thừa tối đa của $z$ mà bạn cần.

Bây giờ nếu bạn cần đánh giá một đa thức tại các điểm $x_r = z^{2r+1}$ bạn có thể giảm nó về nhiệm vụ trước đó bằng biến đổi $a_k \to a_k z^k$.

Nó cung cấp cho chúng ta một thuật toán $O(n \log n)$ khi bạn cần tính toán các giá trị trong lũy thừa của $z$, do đó bạn có thể tính DFT cho các lũy thừa không phải là hai.

Một quan sát khác là $kr = \binom{k+r}{2} - \binom{k}{2} - \binom{r}{2}$. Khi đó chúng ta có

$$\boxed{A(z^r) = z^{-\binom{r}{2}}\sum\limits_{k=0}^n \left(a_k z^{-\binom{k}{2}}\right)z^{\binom{k+r}{2}}}$$

Hệ số của $x^{n+r}$ của tích của các đa thức $A_0(x) = \sum\limits_{k=0}^n a_{n-k}z^{-\binom{n-k}{2}}x^k$ và $A_1(x) = \sum\limits_{k\geq 0}z^{\binom{k}{2}}x^k$ bằng $z^{\binom{r}{2}}A(z^r)$. Bạn có thể sử dụng công thức $z^{\binom{k+1}{2}}=z^{\binom{k}{2}+k}$ để tính các hệ số của $A_0(x)$ và $A_1(x)$.

### Đánh giá đa điểm (Multi-point Evaluation) {: #multi-point-evaluation}
Giả sử bạn cần tính $A(x_1), \dots, A(x_n)$. Như đã đề cập trước đó, $A(x) \equiv A(x_i) \pmod{x-x_i}$. Do đó bạn có thể làm như sau:

1. Tính một cây phân đoạn sao cho trong đoạn $[l,r)$ chứa tích $P_{l, r}(x) = (x-x_l)(x-x_{l+1})\dots(x-x_{r-1})$.
2. Bắt đầu với $l=1$ và $r=n+1$ tại nút gốc. Gọi $m=\lfloor(l+r)/2\rfloor$. Hãy di chuyển xuống $[l,m)$ với đa thức $A(x) \pmod{P_{l,m}(x)}$.
3. Điều này sẽ tính toán đệ quy $A(x_l), \dots, A(x_{m-1})$, bây giờ làm tương tự cho $[m,r)$ với $A(x) \pmod{P_{m,r}(x)}$.
4. Nối các kết quả từ cuộc gọi đệ quy thứ nhất và thứ hai và trả về chúng.

Toàn bộ quy trình sẽ chạy trong $O(n \log^2 n)$.

### Nội suy (Interpolation) {: #interpolation}

Có một công thức trực tiếp của Lagrange để nội suy một đa thức, cho tập hợp các cặp $(x_i, y_i)$:

$$\boxed{A(x) = \sum\limits_{i=1}^n y_i \prod\limits_{j \neq i}\dfrac{x-x_j}{x_i - x_j}}$$

Tính toán trực tiếp nó là một điều khó nhưng hóa ra, chúng ta có thể tính nó trong $O(n \log^2 n)$ với cách tiếp cận chia để trị:

Xét $P(x) = (x-x_1)\dots(x-x_n)$. Để biết các hệ số của các mẫu số trong $A(x)$ chúng ta nên tính các tích như: 

$$
P_i = \prod\limits_{j \neq i} (x_i-x_j)
$$

Nhưng nếu bạn xem xét đạo hàm $P'(x)$ bạn sẽ thấy rằng $P'(x_i) = P_i$. Do đó bạn có thể tính $P_i$ thông qua đánh giá trong $O(n \log^2 n)$.

Bây giờ hãy xem xét thuật toán đệ quy được thực hiện trên cùng một cây phân đoạn như trong đánh giá đa điểm. Nó bắt đầu ở các lá với giá trị $\dfrac{y_i}{P_i}$ trong mỗi lá.

Khi chúng ta quay trở lại từ đệ quy, chúng ta nên hợp nhất các kết quả từ các đỉnh bên trái và bên phải dưới dạng $A_{l,r} = A_{l,m}P_{m,r} + P_{l,m} A_{m,r}$.

Theo cách này khi bạn quay lại gốc, bạn sẽ có chính xác $A(x)$ trong đó.
Toàn bộ quy trình cũng hoạt động trong $O(n \log^2 n)$.

## GCD và Kết thức (GCD and Resultants) {: #gcd-and-resultants}

Giả sử bạn được cho các đa thức $A(x) = a_0 + a_1 x + \dots + a_n x^n$ và $B(x) = b_0 + b_1 x + \dots + b_m x^m$.

Gọi $\lambda_0, \dots, \lambda_n$ là các nghiệm của $A(x)$ và gọi $\mu_0, \dots, \mu_m$ là các nghiệm của $B(x)$ được tính với số bội của chúng.

Bạn muốn biết liệu $A(x)$ và $B(x)$ có bất kỳ nghiệm nào chung hay không. Có hai cách liên kết với nhau để làm điều đó.

### Thuật toán Euclid (Euclidean algorithm) {: #euclidean-algorithm}

Chà, chúng tôi đã có một [bài viết](euclid-algorithm.md) về nó. Đối với một miền tùy ý, bạn có thể viết thuật toán Euclid dễ dàng như:

```cpp
template<typename T>
T gcd(const T &a, const T &b) {
	return b == T(0) ? a : gcd(b, a % b);
}
```

Có thể chứng minh rằng đối với các đa thức $A(x)$ và $B(x)$, nó sẽ hoạt động trong $O(nm)$.

### Kết thức (Resultant) {: #resultant}

Hãy tính tích $A(\mu_0)\cdots A(\mu_m)$. Nó sẽ bằng không khi và chỉ khi một số $\mu_i$ là nghiệm của $A(x)$.

Để đối xứng, chúng ta cũng có thể nhân nó với $b_m^n$ và viết lại toàn bộ tích dưới dạng sau:

$$\boxed{\mathcal{R}(A, B) = b_m^n\prod\limits_{j=0}^m A(\mu_j) = b_m^n a_m^n \prod\limits_{i=0}^n \prod\limits_{j=0}^m (\mu_j - \lambda_i)= (-1)^{mn}a_n^m \prod\limits_{i=0}^n B(\lambda_i)}$$

Giá trị được định nghĩa ở trên được gọi là kết thức của các đa thức $A(x)$ và $B(x)$. Từ định nghĩa, bạn có thể tìm thấy các tính chất sau:

1. $\mathcal R(A, B) = (-1)^{nm} \mathcal R(B, A)$.
2. $\mathcal R(A, B)= a_n^m b_m^n$ khi $n=0$ hoặc $m=0$.
3. Nếu $b_m=1$ thì $\mathcal R(A - CB, B) = \mathcal R(A, B)$ cho một đa thức tùy ý $C(x)$ và $n,m \geq 1$.
4. Từ điều này suy ra $\mathcal R(A, B) = b_m^{\deg(A) - \deg(A-CB)}\mathcal R(A - CB, B)$ cho $A(x)$, $B(x)$, $C(x)$ tùy ý.

Kỳ diệu thay, nó có nghĩa là kết thức của hai đa thức thực sự luôn nằm trong cùng một vành với các hệ số của chúng!

Ngoài ra, các tính chất này cho phép chúng ta tính kết thức cùng với thuật toán Euclid, hoạt động trong $O(nm)$.


```cpp
template<typename T>
T resultant(poly<T> a, poly<T> b) {
	if(b.is_zero()) {
		return 0;
	} else if(b.deg() == 0) {
		return bpow(b.lead(), a.deg());
	} else {
		int pw = a.deg();
		a %= b;
		pw -= a.deg();
		base mul = bpow(b.lead(), pw) * base((b.deg() & a.deg() & 1) ? -1 : 1);
		base ans = resultant(b, a);
		return ans * mul;
	}
}
```

### Thuật toán Half-GCD (Half-GCD algorithm) {: #half-gcd-algorithm}

Có một cách để tính GCD và kết thức trong $O(n \log^2 n)$.

Quy trình để làm điều đó thực hiện một biến đổi tuyến tính $2 \times 2$ ánh xạ một cặp đa thức $a(x)$, $b(x)$ thành cặp khác $c(x), d(x)$ sao cho $\deg d(x) \leq \frac{\deg a(x)}{2}$. Nếu bạn đủ cẩn thận, bạn có thể tính half-GCD của bất kỳ cặp đa thức nào với tối đa $2$ cuộc gọi đệ quy đến các đa thức nhỏ hơn ít nhất $2$ lần.

Các chi tiết cụ thể của thuật toán hơi tẻ nhạt để giải thích, tuy nhiên bạn có thể tìm thấy cài đặt của nó trong thư viện, dưới dạng hàm `half_gcd`.

Sau khi half-GCD được cài đặt, bạn có thể áp dụng lặp đi lặp lại nó cho các đa thức cho đến khi bạn giảm xuống còn cặp $\gcd(a, b)$ và $0$.

## Bài tập {: #problems}

- [CodeChef - RNG](https://www.codechef.com/problems/RNG)
- [CodeForces - Basis Change](https://codeforces.com/gym/102129/problem/D)
- [CodeForces - Permutant](https://codeforces.com/gym/102129/problem/G)
- [CodeForces - Medium Hadron Collider](https://codeforces.com/gym/102129/problem/C)

---
