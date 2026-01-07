---
tags:
  - Original
---

# Các phép toán trên đa thức và chuỗi

Các bài toán trong lập trình thi đấu, đặc biệt là những bài liên quan đến việc đếm một loại nào đó, thường được giải quyết bằng cách quy bài toán về việc tính toán một cái gì đó trên các đa thức và chuỗi lũy thừa hình thức.

Điều này bao gồm các khái niệm như nhân đa thức, nội suy, và những khái niệm phức tạp hơn, như logarit và mũ của đa thức. Trong bài viết này, một cái nhìn tổng quan ngắn gọn về các phép toán như vậy và các cách tiếp cận phổ biến đối với chúng sẽ được trình bày.

## Khái niệm cơ bản và sự thật

Trong phần này, chúng ta tập trung hơn vào các định nghĩa và các thuộc tính "trực quan" của các phép toán đa thức khác nhau. Các chi tiết kỹ thuật về việc triển khai và độ phức tạp của chúng sẽ được đề cập trong các phần sau.

### Phép nhân đa thức

!!! info "Định nghĩa"
	**Đa thức một biến** là một biểu thức có dạng $A(x) = a_0 + a_1 x + \dots + a_n x^n$.

Các giá trị $a_0, \dots, a_n$ là các hệ số của đa thức, thường được lấy từ một tập hợp các số hoặc các cấu trúc giống số. Trong bài viết này, chúng ta giả định rằng các hệ số được lấy từ một [trường](https://en.wikipedia.org/wiki/Field_(mathematics)) nào đó, có nghĩa là các phép toán cộng, trừ, nhân và chia được định nghĩa rõ ràng cho chúng (ngoại trừ phép chia cho $0$) và chúng thường hoạt động tương tự như các số thực.
	
Ví dụ điển hình của một trường như vậy là trường các số dư modulo một số nguyên tố $p$.

Để đơn giản, chúng ta sẽ bỏ qua thuật ngữ _một biến_, vì đây là loại đa thức duy nhất chúng ta xem xét trong bài viết này. Chúng ta cũng sẽ viết $A$ thay vì $A(x)$ ở bất cứ đâu có thể, điều này sẽ dễ hiểu từ ngữ cảnh. Giả định rằng hoặc $a_n \neq 0$ hoặc $A(x)=0$.

!!! info "Định nghĩa"
	**Tích** của hai đa thức được định nghĩa bằng cách khai triển nó như một biểu thức số học:

	$$
	A(x) B(x) = \left(\sum\limits_{i=0}^n a_i x^i \right)\left(\sum\limits_{j=0}^m b_j x^j\right) = \sum\limits_{i,j} a_i b_j x^{i+j} = \sum\limits_{k=0}^{n+m} c_k x^k = C(x).
	$$

	Dãy $c_0, c_1, \dots, c_{n+m}$ của các hệ số của $C(x)$ được gọi là **tích chập** của $a_0, \dots, a_n$ và $b_0, \dots, b_m$.

!!! info "Định nghĩa"
	**Bậc** của một đa thức $A$ với $a_n \neq 0$ được định nghĩa là $\deg A = n$.
	
	Để nhất quán, bậc của $A(x) = 0$ được định nghĩa là $\deg A = -{\infty}$.

Trong khái niệm này, $\deg AB = \deg A + \deg B$ đối với bất kỳ đa thức $A$ và $B$ nào.

Tích chập là cơ sở để giải quyết nhiều bài toán đếm.

!!! Example
	Bạn có $n$ vật thể loại thứ nhất và $m$ vật thể loại thứ hai.

	Các vật thể loại thứ nhất có giá trị $a_1, \dots, a_n$, và các vật thể loại thứ hai có giá trị $b_1, \dots, b_m$.

	Bạn chọn một vật thể duy nhất của loại thứ nhất và một vật thể duy nhất của loại thứ hai. Có bao nhiêu cách để có được tổng giá trị $k$?

??? hint "Lời giải"
	Xét tích $(x^{a_1} + \dots + x^{a_n})(x^{b_1} + \dots + x^{b_m})$. Nếu bạn khai triển nó, mỗi đơn thức sẽ tương ứng với cặp $(a_i, b_j)$ và đóng góp vào hệ số gần $x^{a_i+b_j}$. Nói cách khác, câu trả lời là hệ số gần $x^k$ trong tích.

!!! Example
	Bạn tung một con xúc xắc $6$ mặt $n$ lần và cộng các kết quả từ tất cả các lần tung. Xác suất để có được tổng $k$ là bao nhiêu?

??? hint "Lời giải"
	Câu trả lời là số kết quả có tổng $k$, chia cho tổng số kết quả, là $6^n$.

	Số kết quả có tổng $k$ là bao nhiêu? Đối với $n=1$, nó có thể được biểu diễn bằng một đa thức $A(x) = x^1+x^2+\dots+x^6$.

	Đối với $n=2$, sử dụng cùng một cách tiếp cận như trong ví dụ trên, chúng ta kết luận rằng nó được biểu diễn bằng đa thức $(x^1+x^2+\dots+x^6)^2$.

	Nói như vậy, câu trả lời cho bài toán là hệ số thứ $k$ của $(x^1+x^2+\dots+x^6)^n$, chia cho $6^n$.

Hệ số của $x^k$ trong đa thức $A(x)$ được ký hiệu ngắn gọn là $[x^k]A$.

### Chuỗi lũy thừa hình thức

!!! info "Định nghĩa"
	Một **chuỗi lũy thừa hình thức** là một tổng vô hạn $A(x) = a_0 + a_1 x + a_2 x^2 + \dots$, được xem xét bất kể các thuộc tính hội tụ của nó.

Nói cách khác, khi chúng ta xem xét ví dụ một tổng $1+\frac{1}{2}+\frac{1}{4}+\frac{1}{8}+\dots=2$, chúng ta ngụ ý rằng nó _hội tụ_ về $2$ khi số lượng các số hạng tiến đến vô cùng. Tuy nhiên, các chuỗi hình thức chỉ được xem xét dưới dạng các dãy tạo nên chúng.

!!! info "Định nghĩa"
	**Tích** của các chuỗi lũy thừa hình thức $A(x)$ và $B(x)$, cũng được định nghĩa bằng cách khai triển nó như một biểu thức số học:


	$$ 
	A(x) B(x) = \left(\sum\limits_{i=0}^\infty a_i x^i \right)\left(\sum\limits_{j=0}^\infty b_j x^j\right) = \sum\limits_{i,j} a_i b_j x^{i+j} = \sum\limits_{k=0}^{\infty} c_k x^k = C(x),
	$$ 

	trong đó các hệ số $c_0, c_1, \dots$ được định nghĩa là các tổng hữu hạn

	$$ 
	c_k = \sum\limits_{i=0}^k a_i b_{k-i}. 
	$$ 

	Dãy $c_0, c_1, \dots$ cũng được gọi là **tích chập** của $a_0, a_1, \dots$ và $b_0, b_1, \dots$, tổng quát hóa khái niệm cho các dãy vô hạn.

Do đó, các đa thức có thể được coi là các chuỗi lũy thừa hình thức, nhưng với số lượng hệ số hữu hạn.

Các chuỗi lũy thừa hình thức đóng một vai trò quan trọng trong tổ hợp đếm, nơi chúng được nghiên cứu như các [hàm sinh](https://en.wikipedia.org/wiki/Generating_function) cho các dãy khác nhau. Giải thích chi tiết về các hàm sinh và trực giác đằng sau chúng, thật không may, sẽ nằm ngoài phạm vi của bài viết này, do đó người đọc tò mò được giới thiệu ví dụ [tại đây](https://codeforces.com/blog/entry/103979) để biết chi tiết về ý nghĩa tổ hợp của chúng.

Tuy nhiên, chúng ta sẽ đề cập rất ngắn gọn rằng nếu $A(x)$ và $B(x)$ là các hàm sinh cho các dãy đếm một số đối tượng theo số lượng "nguyên tử" trong chúng (ví dụ: cây theo số đỉnh), thì tích $A(x) B(x)$ đếm các đối tượng có thể được mô tả là các cặp đối tượng của loại $A$ và $B$, đếm theo tổng số "nguyên tử" trong cặp.

!!! Example
	Đặt $A(x) = \sum\limits_{i=0}^\infty 2^i x^i$ đếm các gói đá, mỗi viên đá được tô màu bằng một trong $2$ màu (vì vậy, có $2^i$ gói như vậy có kích thước $i$) và $B(x) = \sum\limits_{j=0}^{\infty} 3^j x^j$ đếm các gói đá, mỗi viên đá được tô màu bằng một trong $3$ màu. Khi đó $C(x) = A(x) B(x) = \sum\limits_{k=0}^\infty c_k x^k$ sẽ đếm các đối tượng có thể được mô tả là "hai gói đá, gói đầu tiên chỉ có các viên đá loại $A$, gói thứ hai chỉ có các viên đá loại $B$, với tổng số đá là $k$" cho $c_k$.

Theo cách tương tự, có một ý nghĩa trực quan đối với một số hàm khác trên các chuỗi lũy thừa hình thức.

### Phép chia đa thức dài

Tương tự như các số nguyên, có thể định nghĩa phép chia dài trên các đa thức.

!!! info "Định nghĩa"

	Đối với bất kỳ đa thức $A$ và $B \neq 0$ nào, người ta có thể biểu diễn $A$ dưới dạng

	$$ 
	A = D \cdot B + R,~ \deg R < \deg B,
	$$ 

	trong đó $R$ được gọi là **dư** của $A$ modulo $B$ và $D$ được gọi là **thương**.

Ký hiệu $\deg A = n$ và $\deg B = m$, cách ngây thơ để làm điều đó là sử dụng phép chia dài, trong đó bạn nhân $B$ với đơn thức $\frac{a_n}{b_m} x^{n - m}$ và trừ nó khỏi $A$, cho đến khi bậc của $A$ nhỏ hơn bậc của $B$. Những gì còn lại của $A$ cuối cùng sẽ là phần dư (do đó có tên gọi này), và các đa thức mà bạn đã nhân với $B$ trong quá trình, cộng lại với nhau, tạo thành thương.

!!! info "Định nghĩa"
	Nếu $A$ và $B$ có cùng phần dư modulo $C$, chúng được cho là **tương đương** modulo $C$, được ký hiệu là
	
	$$ 
	A \equiv B \pmod{C}.
	$$ 
	
Phép chia đa thức dài hữu ích vì nhiều thuộc tính quan trọng của nó:

- $A$ là bội của $B$ khi và chỉ khi $A \equiv 0 \pmod B$.

- Điều đó ngụ ý rằng $A \equiv B \pmod C$ khi và chỉ khi $A-B$ là bội của $C$.

- Cụ thể, $A \equiv B \pmod{C \cdot D}$ ngụ ý $A \equiv B \pmod{C}$.

- Đối với bất kỳ đa thức tuyến tính $x-r$ nào, nó đúng rằng $A(x) \equiv A(r) \pmod{x-r}$.

- Điều đó ngụ ý rằng $A$ là bội của $x-r$ khi và chỉ khi $A(r)=0$.

- Đối với modulo là $x^k$, nó đúng rằng $A \equiv a_0 + a_1 x + \dots + a_{k-1} x^{k-1} \pmod{x^k}$.

Lưu ý rằng phép chia dài không thể được định nghĩa đúng cho các chuỗi lũy thừa hình thức. Thay vào đó, đối với bất kỳ $A(x)$ nào sao cho $a_0 \neq 0$, có thể định nghĩa một chuỗi lũy thừa hình thức nghịch đảo $A^{-1}(x)$, sao cho $A(x) A^{-1}(x) = 1$. Thực tế này, đến lượt nó, có thể được sử dụng để tính toán kết quả của phép chia dài cho các đa thức.

## Triển khai cơ bản
[Ở đây](https://cp-algorithms.github.io/cp-algorithms-aux/cp-algo/math/poly.hpp) bạn có thể tìm thấy triển khai cơ bản của đại số đa thức.

Nó hỗ trợ tất cả các phép toán tầm thường và một số phương thức hữu ích khác. Lớp chính là `poly<T>` cho các đa thức với các hệ số kiểu `T`.

Tất cả các phép toán số học `+`, `-`, `*`, `%` và `/` đều được hỗ trợ, `%` và `/` đại diện cho phần dư và thương trong phép chia Euclid.

Ngoài ra còn có lớp `modular<m>` để thực hiện các phép toán số học trên các số dư modulo một số nguyên tố `m`.

Các hàm hữu ích khác:

- `deriv()`: tính đạo hàm $P'(x)$ của $P(x)$.
- `integr()`: tính tích phân không xác định $Q(x) = \int P(x)$ của $P(x)$ sao cho $Q(0)=0$.
- `inv(size_t n)`: tính $n$ hệ số đầu tiên của $P^{-1}(x)$ trong $O(n \log n)$.
- `log(size_t n)`: tính $n$ hệ số đầu tiên của $\ln P(x)$ trong $O(n \log n)$.
- `exp(size_t n)`: tính $n$ hệ số đầu tiên của $\exp P(x)$ trong $O(n \log n)$.
- `pow(size_t k, size_t n)`: tính $n$ hệ số đầu tiên cho $P^{k}(x)$ trong $O(n \log nk)$.
- `deg()`: trả về bậc của $P(x)$.
- `lead()`: trả về hệ số của $x^{\deg P(x)}$.
- `resultant(poly<T> a, poly<T> b)`: tính hợp kết của $a$ và $b$ trong $O(|a| \cdot |b|)$.
- `bpow(T x, size_t n)`: tính $x^n$.
- `bpow(T x, size_t n, T m)`: tính $x^n \pmod{m}$.
- `chirpz(T z, size_t n)`: tính $P(1), P(z), P(z^2), \dots, P(z^{n-1})$ trong $O(n \log n)$.
- `vector<T> eval(vector<T> x)`: đánh giá $P(x_1), \dots, P(x_n)$ trong $O(n \log^2 n)$.
- `poly<T> inter(vector<T> x, vector<T> y)`: nội suy một đa thức bằng một tập hợp các cặp $P(x_i) = y_i$ trong $O(n \log^2 n)$.
- Và một số hàm khác, hãy thoải mái khám phá mã!

## Số học

### Phép nhân

Phép toán cốt lõi là phép nhân của hai đa thức. Tức là, cho các đa thức $A$ và $B$:

$$A = a_0 + a_1 x + \dots + a_n x^n$$

$$B = b_0 + b_1 x + \dots + b_m x^m$$

Bạn phải tính đa thức $C = A \cdot B$, được định nghĩa là

$$\boxed{C = \sum\limits_{i=0}^n \sum\limits_{j=0}^m a_i b_j x^{i+j}}  = c_0 + c_1 x + \dots + c_{n+m} x^{n+m}.$$ 

Nó có thể được tính trong $O(n \log n)$ thông qua [Biến đổi Fourier nhanh](fft.md) và hầu hết tất cả các phương pháp ở đây sẽ sử dụng nó như một chương trình con.

### Chuỗi nghịch đảo

Nếu $A(0) \neq 0$ luôn tồn tại một chuỗi lũy thừa hình thức vô hạn $A^{-1}(x) = q_0+q_1 x + q_2 x^2 + \dots$ sao cho $A^{-1} A = 1$. Thường rất hữu ích khi tính $k$ hệ số đầu tiên của $A^{-1}$ (tức là, để tính nó modulo $x^k$). Có hai cách chính để tính toán nó.

#### Chia để trị

Thuật toán này được đề cập trong [bài viết của Schönhage](http://algo.inria.fr/seminars/sem00-01/schoenhage.pdf) và được lấy cảm hứng từ [phương pháp của Graeffe](https://en.wikipedia.org/wiki/Graeffe's_method). Ta biết rằng đối với $B(x)=A(x)A(-x)$ thì $B(x)=B(-x)$, tức là $B(x)$ là một đa thức chẵn. Điều đó có nghĩa là nó chỉ có các hệ số khác không với các số chẵn và có thể được biểu diễn dưới dạng $B(x)=T(x^2)$. Do đó, chúng ta có thể thực hiện phép chuyển đổi sau:

$$A^{-1}(x) \equiv \frac{1}{A(x)} \equiv \frac{A(-x)}{A(x)A(-x)} \equiv \frac{A(-x)}{T(x^2)} \pmod{x^k}$$ 

Lưu ý rằng $T(x)$ có thể được tính bằng một phép nhân duy nhất, sau đó chúng ta chỉ quan tâm đến nửa đầu của các hệ số của chuỗi nghịch đảo của nó. Điều này làm giảm hiệu quả bài toán ban đầu về tính $A^{-1} \pmod{x^k}$ thành tính $T^{-1} \pmod{x^{\lceil k / 2 \rceil}}$.

Độ phức tạp của phương pháp này có thể được ước tính là

$$T(n) = T(n/2) + O(n \log n) = O(n \log n).$$ 

#### Thuật toán Sieveking–Kung

Quá trình chung được mô tả ở đây được gọi là nâng Hensel, vì nó xuất phát từ bổ đề Hensel. Chúng ta sẽ đề cập đến nó chi tiết hơn ở phần sau, nhưng bây giờ hãy tập trung vào giải pháp đặc biệt. Phần "nâng" ở đây có nghĩa là chúng ta bắt đầu với phép xấp xỉ $B_0=q_0=a_0^{-1}$, là $A^{-1} \pmod x$ và sau đó lặp đi lặp lại nâng từ $\bmod x^a$ lên $\bmod x^{2a}$.

Đặt $B_k \equiv A^{-1} \pmod{x^a}$. Phép xấp xỉ tiếp theo cần tuân theo phương trình $A B_{k+1} \equiv 1 \pmod{x^{2a}}$ và có thể được biểu diễn dưới dạng $B_{k+1} = B_k + x^a C$. Từ đó suy ra phương trình

$$A(B_k + x^{a}C) \equiv 1 \pmod{x^{2a}}.$$ 

Đặt $A B_k \equiv 1 + x^a D \pmod{x^{2a}}$, khi đó phương trình trên ngụ ý

$$x^a(D+AC) \equiv 0 \pmod{x^{2a}} \implies D \equiv -AC \pmod{x^a} \implies C \equiv -B_k D \pmod{x^a}.$$ 

Từ đó, người ta có thể có được công thức cuối cùng, là

$$x^a C \equiv -B_k x^a D  \equiv B_k(1-AB_k) \pmod{x^{2a}} \implies \boxed{B_{k+1} \equiv B_k(2-AB_k) \pmod{x^{2a}}}$$ 

Do đó, bắt đầu với $B_0 \equiv a_0^{-1} \pmod x$, chúng ta sẽ tính toán dãy $B_k$ sao cho $AB_k \equiv 1 \pmod{x^{2^k}}$ với độ phức tạp

$$T(n) = T(n/2) + O(n \log n) = O(n \log n).$$ 

Thuật toán ở đây có vẻ hơi phức tạp hơn thuật toán đầu tiên, nhưng nó có một lý luận rất vững chắc và thực tế đằng sau nó, cũng như một tiềm năng tổng quát hóa lớn nếu nhìn từ một góc độ khác, sẽ được giải thích thêm bên dưới.

### Phép chia Euclid

Xét hai đa thức $A(x)$ và $B(x)$ có bậc $n$ và $m$. Như đã nói trước đó, bạn có thể viết lại $A(x)$ thành

$$A(x) = B(x) D(x) + R(x), \deg R < \deg B.$$ 

Đặt $n \geq m$, điều đó sẽ ngụ ý rằng $\deg D = n - m$ và $n-m+1$ hệ số hàng đầu của $A$ không ảnh hưởng đến $R$. Điều đó có nghĩa là bạn có thể khôi phục $D(x)$ từ $n-m+1$ hệ số lớn nhất của $A(x)$ và $B(x)$ nếu bạn coi nó như một hệ phương trình tuyến tính.

Hệ phương trình tuyến tính mà chúng ta đang nói đến có thể được viết dưới dạng sau:

$$\begin{bmatrix} a_n \ \vdots \ a_{m+1} \ a_{m} \end{bmatrix} = \begin{bmatrix}
 b_m & \dots & 0 & 0 \ \vdots & \ddots & \vdots & \vdots \ \dots & \dots & b_m & 0 \ \dots & \dots & b_{m-1} & b_m
\end{bmatrix} \begin{bmatrix}d_{n-m} \ \vdots \ d_1 \ d_0
\end{bmatrix}$$ 

Từ vẻ ngoài của nó, chúng ta có thể kết luận rằng với sự ra đời của các đa thức đảo ngược

$$A^R(x) = x^nA(x^{-1})= a_n + a_{n-1} x + \dots + a_0 x^n$$ 

$$B^R(x) = x^m B(x^{-1}) = b_m + b_{m-1} x + \dots + b_0 x^m$$ 

$$D^R(x) = x^{n-m}D(x^{-1}) = d_{n-m} + d_{n-m-1} x + \dots + d_0 x^{n-m}$$ 

các hệ thống có thể được viết lại là

$$A^R(x) \equiv B^R(x) D^R(x) \pmod{x^{n-m+1}}.$$ 

Từ đó bạn có thể khôi phục một cách rõ ràng tất cả các hệ số của $D(x)$:

$$\boxed{D^R(x) \equiv A^R(x) (B^R(x))^{-1} \pmod{x^{n-m+1}}}$$ 

Và từ đó, đến lượt nó, bạn có thể khôi phục $R(x)$ là $R(x) = A(x) - B(x)D(x)$.

Lưu ý rằng ma trận ở trên là một ma trận được gọi là [ma trận Toeplitz](https://en.wikipedia.org/wiki/Toeplitz_matrix) tam giác và, như chúng ta thấy ở đây, việc giải hệ phương trình tuyến tính với ma trận Toeplitz tùy ý, trên thực tế, tương đương với nghịch đảo đa thức. Hơn nữa, ma trận nghịch đảo của nó cũng sẽ là ma trận Toeplitz tam giác và các phần tử của nó, theo các thuật ngữ được sử dụng ở trên, là các hệ số của $(B^R(x))^{-1} \pmod{x^{n-m+1}}$.

## Tính toán các hàm của đa thức

### Phương pháp Newton

Hãy tổng quát hóa thuật toán Sieveking–Kung. Xét phương trình $F(P) = 0$ trong đó $P(x)$ phải là một đa thức và $F(x)$ là một hàm có giá trị đa thức được định nghĩa là

$$F(x) = \sum\limits_{i=0}^\infty \alpha_i (x-\beta)^i,$$ 

trong đó $\beta$ là một hằng số nào đó. Có thể chứng minh rằng nếu chúng ta giới thiệu một biến hình thức mới $y$, chúng ta có thể biểu diễn $F(x)$ dưới dạng

$$F(x) = F(y) + (x-y)F'(y) + (x-y)^2 G(x,y),$$ 

trong đó $F'(x)$ là chuỗi lũy thừa hình thức đạo hàm được định nghĩa là

$$F'(x) = \sum\limits_{i=0}^\infty (i+1)\alpha_{i+1}(x-\beta)^i,$$ 

và $G(x, y)$ là một chuỗi lũy thừa hình thức nào đó của $x$ và $y$. Với kết quả này, chúng ta có thể tìm nghiệm một cách lặp đi lặp lại.

Đặt $F(Q_k) \equiv 0 \pmod{x^{a}}$. Chúng ta cần tìm $Q_{k+1} \equiv Q_k + x^a C \pmod{x^{2a}}$ sao cho $F(Q_{k+1}) \equiv 0 \pmod{x^{2a}}$.

Thay thế $x = Q_{k+1}$ và $y=Q_k$ vào công thức trên, chúng ta có được

$$F(Q_{k+1}) \equiv F(Q_k) + (Q_{k+1} - Q_k) F'(Q_k) + (Q_{k+1} - Q_k)^2 G(x, y) \pmod x^{2a}.$$ 

Vì $Q_{k+1} - Q_k \equiv 0 \pmod{x^a}$, nó cũng đúng rằng $(Q_{k+1} - Q_k)^2 \equiv 0 \pmod{x^{2a}}$, do đó

$$0 \equiv F(Q_{k+1}) \equiv F(Q_k) + (Q_{k+1} - Q_k) F'(Q_k) \pmod{x^{2a}}.$$ 

Công thức cuối cùng cho chúng ta giá trị của $Q_{k+1}$:

$$\boxed{Q_{k+1} = Q_k - \dfrac{F(Q_k)}{F'(Q_k)} \pmod{x^{2a}}}$$ 

Do đó, biết cách nghịch đảo các đa thức và cách tính $F(Q_k)$, chúng ta có thể tìm thấy $n$ hệ số của $P$ với độ phức tạp

$$T(n) = T(n/2) + f(n),$$ 

trong đó $f(n)$ là thời gian cần thiết để tính $F(Q_k)$ và $F'(Q_k)^{-1}$ thường là $O(n \log n)$.

Quy tắc lặp ở trên được biết đến trong phân tích số là [phương pháp của Newton](https://en.wikipedia.org/wiki/Newton%27s_method).

#### Bổ đề Hensel

Như đã đề cập trước đó, một cách hình thức và chung chung, kết quả này được gọi là [bổ đề Hensel](https://en.wikipedia.org/wiki/Hensel%27s_lemma) và nó thực sự có thể được sử dụng theo một nghĩa rộng hơn khi chúng ta làm việc với một chuỗi các vành lồng nhau. Trong trường hợp cụ thể này, chúng ta đã làm việc với một chuỗi các phần dư đa thức modulo $x$, $x^2$, $x^3$, v.v.

Một ví dụ khác mà việc nâng Hensel có thể hữu ích là các số được gọi là [số p-adic](https://en.wikipedia.org/wiki/P-adic_number) nơi chúng ta, trên thực tế, làm việc với chuỗi các số dư nguyên modulo $p$, $p^2$, $p^3$, v.v. Ví dụ, phương pháp của Newton có thể được sử dụng để tìm tất cả các [số tự hình](https://en.wikipedia.org/wiki/Automorphic_number) có thể có (các số kết thúc bằng chính nó khi bình phương) với một cơ số đã cho. Bài toán này được để lại như một bài tập cho người đọc. Bạn có thể xem xét bài toán [này](https://acm.timus.ru/problem.aspx?space=1&num=1698) để kiểm tra xem giải pháp của bạn có hoạt động đối với các số cơ số $10$ hay không.


### Lôgarit

Đối với hàm $\ln P(x)$, ta biết rằng:

$$ 
\boxed{(\ln P(x))' = \dfrac{P'(x)}{P(x)}} 
$$ 

Do đó, chúng ta có thể tính $n$ hệ số của $\ln P(x)$ trong $O(n \log n)$.


### Chuỗi nghịch đảo

Hóa ra, chúng ta có thể có được công thức cho $A^{-1}$ bằng phương pháp của Newton.
Đối với điều này, chúng ta lấy phương trình $A=Q^{-1}$, do đó:

$$F(Q) = Q^{-1} - A$$ 

$$F'(Q) = -Q^{-2}$$ 

$$\boxed{Q_{k+1} \equiv Q_k(2-AQ_k) \pmod{x^{2^{k+1}}}}$$ 

### Mũ

Hãy học cách tính $e^{P(x)}=Q(x)$. Nó phải đúng rằng $\ln Q = P$, do đó:

$$F(Q) = \ln Q - P$$ 

$$F'(Q) = Q^{-1}$$ 

$$\boxed{Q_{k+1} \equiv Q_k(1 + P - \ln Q_k) \pmod{x^{2^{k+1}}}}$$ 

### Lũy thừa bậc $k$ { data-toc-label="k-th power" } 

Bây giờ chúng ta cần tính $P^k(x)=Q$. Điều này có thể được thực hiện thông qua công thức sau:

$$Q = \exp\left[k \ln P(x)\right]$$ 

Tuy nhiên, lưu ý rằng bạn chỉ có thể tính toán các lôgarit và các mũ một cách chính xác nếu bạn có thể tìm thấy một số $Q_0$ ban đầu.

Để tìm nó, bạn nên tính lôgarit hoặc mũ của hệ số hằng của đa thức.

Nhưng cách hợp lý duy nhất để làm điều đó là nếu $P(0)=1$ đối với $Q = \ln P$ để $Q(0)=0$ và nếu $P(0)=0$ đối với $Q = e^P$ để $Q(0)=1$.

Do đó, bạn chỉ có thể sử dụng công thức trên nếu $P(0) = 1$. Nếu không, nếu $P(x) = \alpha x^t T(x)$ trong đó $T(0)=1$, bạn có thể viết rằng:

$$\boxed{P^k(x) = \alpha^kx^{kt} \exp[k \ln T(x)]}$$ 

Lưu ý rằng bạn cũng có thể tính một số căn bậc $k$ của một đa thức nếu bạn có thể tính $\sqrt[k]{\alpha}$, ví dụ đối với $\alpha=1$.

## Đánh giá và Nội suy

### Biến đổi Chirp-z

Đối với trường hợp cụ thể khi bạn cần đánh giá một đa thức tại các điểm $x_r = z^{2r}$, bạn có thể làm như sau:

$$A(z^{2r}) = \sum\limits_{k=0}^n a_k z^{2kr}$$ 

Hãy thay thế $2kr = r^2+k^2-(r-k)^2$. Khi đó tổng này viết lại thành:

$$\boxed{A(z^{2r}) = z^{r^2}\sum\limits_{k=0}^n (a_k z^{k^2}) z^{-(r-k)^2}}$$ 

Đây là, cho đến hệ số $z^{r^2}$, bằng tích chập của các dãy $u_k = a_k z^{k^2}$ và $v_k = z^{-k^2}$.

Lưu ý rằng $u_k$ có các chỉ số từ $0$ đến $n$ ở đây và $v_k$ có các chỉ số từ $-n$ đến $m$ trong đó $m$ là lũy thừa tối đa của $z$ mà bạn cần.

Bây giờ nếu bạn cần đánh giá một đa thức tại các điểm $x_r = z^{2r+1}$, bạn có thể quy nó về bài toán trước bằng phép biến đổi $a_k \to a_k z^k$.

Nó cho chúng ta một thuật toán $O(n \log n)$ khi bạn cần tính các giá trị theo lũy thừa của $z$, do đó bạn có thể tính DFT cho các giá trị không phải là lũy thừa của hai.

Một quan sát khác là $kr = \binom{k+r}{2} - \binom{k}{2} - \binom{r}{2}$. Khi đó chúng ta có

$$\boxed{A(z^r) = z^{-\binom{r}{2}}\sum\limits_{k=0}^n \left(a_k z^{-\binom{k}{2}}\right)z^{\binom{k+r}{2}}}$$ 

Hệ số của $x^{n+r}$ của tích các đa thức $A_0(x) = \sum\limits_{k=0}^n a_{n-k}z^{-\binom{n-k}{2}}x^k$ và $A_1(x) = \sum\limits_{k\geq 0}z^{\binom{k}{2}}x^k$ bằng $z^{\binom{r}{2}}A(z^r)$. Bạn có thể sử dụng công thức $z^{\binom{k+1}{2}}=z^{\binom{k}{2}+k}$ để tính các hệ số của $A_0(x)$ và $A_1(x)$.

### Đánh giá đa điểm
Giả sử bạn cần tính $A(x_1), \dots, A(x_n)$. Như đã đề cập trước đó, $A(x) \equiv A(x_i) \pmod{x-x_i}$. Do đó, bạn có thể làm như sau:

1. Tính một cây phân đoạn sao cho trong đoạn $[l,r)$ có tích $P_{l, r}(x) = (x-x_l)(x-x_{l+1})\dots(x-x_{r-1})$.
2. Bắt đầu với $l=1$ và $r=n+1$ tại nút gốc. Đặt $m=\lfloor(l+r)/2\rfloor$. Hãy đi xuống $[l,m)$ với đa thức $A(x) \pmod{P_{l,m}(x)}$.
3. Điều này sẽ đệ quy tính $A(x_l), \dots, A(x_{m-1})$, bây giờ làm tương tự cho $[m,r)$ với $A(x) \pmod{P_{m,r}(x)}$.
4. Nối các kết quả từ lệnh gọi đệ quy thứ nhất và thứ hai và trả về chúng.

Toàn bộ thủ tục sẽ chạy trong $O(n \log^2 n)$.

### Nội suy

Có một công thức trực tiếp của Lagrange để nội suy một đa thức, cho một tập hợp các cặp $(x_i, y_i)$:

$$\boxed{A(x) = \sum\limits_{i=1}^n y_i \prod\limits_{j \neq i}\dfrac{x-x_j}{x_i - x_j}}$$ 

Tính toán trực tiếp là một việc khó nhưng hóa ra, chúng ta có thể tính nó trong $O(n \log^2 n)$ với một cách tiếp cận chia để trị:

Xét $P(x) = (x-x_1)\dots(x-x_n)$. Để biết các hệ số của các mẫu số trong $A(x)$, chúng ta nên tính các tích như:

$$ 
 P_i = \prod\limits_{j \neq i} (x_i-x_j) 
 $$ 

Nhưng nếu bạn xem xét đạo hàm $P'(x)$, bạn sẽ thấy rằng $P'(x_i) = P_i$. Do đó, bạn có thể tính $P_i$ thông qua đánh giá trong $O(n \log^2 n)$.

Bây giờ hãy xem xét thuật toán đệ quy được thực hiện trên cùng một cây phân đoạn như trong đánh giá đa điểm. Nó bắt đầu ở các lá với giá trị $\dfrac{y_i}{P_i}$ trong mỗi lá.

Khi chúng ta trở về từ đệ quy, chúng ta nên hợp nhất các kết quả từ các đỉnh trái và phải thành $A_{l,r} = A_{l,m}P_{m,r} + P_{l,m} A_{m,r}$.

Bằng cách này, khi bạn quay trở lại gốc, bạn sẽ có chính xác $A(x)$ trong đó.
Toàn bộ thủ tục cũng hoạt động trong $O(n \log^2 n)$.

## ƯCLN và Hợp kết

Giả sử bạn được cho các đa thức $A(x) = a_0 + a_1 x + \dots + a_n x^n$ và $B(x) = b_0 + b_1 x + \dots + b_m x^m$.

Đặt $\lambda_0, \dots, \lambda_n$ là các nghiệm của $A(x)$ và đặt $\mu_0, \dots, \mu_m$ là các nghiệm của $B(x)$ được đếm cùng với các bội số của chúng.

Bạn muốn biết liệu $A(x)$ và $B(x)$ có bất kỳ nghiệm chung nào không. Có hai cách liên kết với nhau để làm điều đó.

### Thuật toán Euclid

Chà, chúng ta đã có một [bài viết](euclid-algorithm.md) về nó. Đối với một miền tùy ý, bạn có thể viết thuật toán Euclid dễ dàng như sau:

```cpp
template<typename T>
T gcd(const T &a, const T &b) {
	return b == T(0) ? a : gcd(b, a % b);
}
```

Có thể chứng minh rằng đối với các đa thức $A(x)$ và $B(x)$, nó sẽ hoạt động trong $O(nm)$.


### Hợp kết

Hãy tính tích $A(\mu_0)\cdots A(\mu_m)$. Nó sẽ bằng không khi và chỉ khi một số $\mu_i$ là nghiệm của $A(x)$.

Để đối xứng, chúng ta cũng có thể nhân nó với $b_m^n$ và viết lại toàn bộ tích dưới dạng sau:

$$\boxed{\mathcal{R}(A, B) = b_m^n\prod\limits_{j=0}^m A(\mu_j) = b_m^n a_m^n \prod\limits_{i=0}^n \prod\limits_{j=0}^m (\mu_j - \lambda_i)= (-1)^{mn}a_n^m \prod\limits_{i=0}^n B(\lambda_i)}$$ 

Giá trị được định nghĩa ở trên được gọi là hợp kết của các đa thức $A(x)$ và $B(x)$. Từ định nghĩa, bạn có thể tìm thấy các thuộc tính sau:

1. $\mathcal R(A, B) = (-1)^{nm} \mathcal R(B, A)$.
2. $\mathcal R(A, B)= a_n^m b_m^n$ khi $n=0$ hoặc $m=0$.
3. Nếu $b_m=1$ thì $\mathcal R(A - CB, B) = \mathcal R(A, B)$ đối với một đa thức tùy ý $C(x)$ và $n,m \geq 1$.
4. Từ đó suy ra $\mathcal R(A, B) = b_m^{\deg(A) - \deg(A-CB)}\mathcal R(A - CB, B)$ đối với $A(x)$, $B(x)$, $C(x)$ tùy ý.

Thật kỳ diệu, điều đó có nghĩa là hợp kết của hai đa thức thực sự luôn đến từ cùng một vành với các hệ số của chúng!

Các thuộc tính này cũng cho phép chúng ta tính toán hợp kết cùng với thuật toán Euclid, hoạt động trong $O(nm)$.


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

### Thuật toán Half-GCD

Có một cách để tính ƯCLN và hợp kết trong $O(n \log^2 n)$.

Thủ tục để làm như vậy thực hiện một phép biến đổi tuyến tính $2 \times 2$ ánh xạ một cặp đa thức $a(x)$, $b(x)$ thành một cặp khác $c(x), d(x)$ sao cho $\deg d(x) \leq \frac{\deg a(x)}{2}$. Nếu bạn đủ cẩn thận, bạn có thể tính half-GCD của bất kỳ cặp đa thức nào với tối đa $2$ lần gọi đệ quy đến các đa thức nhỏ hơn ít nhất $2$ lần.

Các chi tiết cụ thể của thuật toán hơi tẻ nhạt để giải thích, tuy nhiên bạn có thể tìm thấy việc triển khai của nó trong thư viện, dưới dạng hàm `half_gcd`.

Sau khi half-GCD được triển khai, bạn có thể áp dụng nó lặp đi lặp lại cho các đa thức cho đến khi bạn giảm xuống còn cặp $\gcd(a, b)$ và $0$.

## Các bài toán

- [CodeChef - RNG](https://www.codechef.com/problems/RNG)
- [CodeForces - Basis Change](https://codeforces.com/gym/102129/problem/D)
- [CodeForces - Permutant](https://codeforces.com/gym/102129/problem/G)
- [CodeForces - Medium Hadron Collider](https://codeforces.com/gym/102129/problem/C)