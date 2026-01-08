---
tags:
  - Translated
e_maxx_link: segment_to_line
---

# Tìm phương trình đường thẳng cho một đoạn thẳng (Finding the equation of a line for a segment) {: #finding-the-equation-of-a-line-for-a-segment}

Nhiệm vụ là: cho tọa độ các đầu mút của một đoạn thẳng, xây dựng một đường thẳng đi qua nó.

Chúng ta giả sử rằng đoạn thẳng là không suy biến, tức là có độ dài lớn hơn 0 (nếu không, tất nhiên, có vô số đường thẳng khác nhau đi qua nó).

### Trường hợp hai chiều (Two-dimensional case) {: #two-dimensional-case}

Giả sử đoạn thẳng đã cho là $PQ$, tức là tọa độ đã biết của các đầu mút của nó là $P_x , P_y , Q_x , Q_y$.

Cần phải xây dựng **phương trình đường thẳng trong mặt phẳng** đi qua đoạn thẳng này, tức là tìm các hệ số $A , B , C$ trong phương trình đường thẳng:

$$A x + B y + C = 0.$$

Lưu ý rằng đối với các bộ ba $(A, B, C)$ được yêu cầu, có **vô số** nghiệm mô tả đoạn thẳng đã cho: bạn có thể nhân tất cả ba hệ số với một số khác không tùy ý và nhận được cùng một đường thẳng.
Do đó, nhiệm vụ của chúng ta là tìm một trong những bộ ba này.

Dễ dàng xác minh (bằng cách thay thế các biểu thức này và tọa độ của các điểm $P$ và $Q$ vào phương trình đường thẳng) rằng bộ hệ số sau phù hợp:

$$\begin{align}
A &= P_y - Q_y, \\
B &= Q_x - P_x, \\
C &= - A P_x - B P_y.
\end{align}$$

### Trường hợp số nguyên (Integer case) {: #integer-case}

Một lợi thế quan trọng của phương pháp xây dựng đường thẳng này là nếu tọa độ của các đầu mút là số nguyên, thì các hệ số thu được cũng sẽ là **số nguyên**. Trong một số trường hợp, điều này cho phép thực hiện các phép toán hình học mà không cần dùng đến số thực.

Tuy nhiên, có một nhược điểm nhỏ: đối với cùng một đường thẳng, có thể thu được các bộ ba hệ số khác nhau.
Để tránh điều này, nhưng không đi xa khỏi các hệ số nguyên, bạn có thể áp dụng kỹ thuật sau, thường được gọi là **tối giản hóa** (rationing). Tìm [ước chung lớn nhất](../algebra/euclid-algorithm.md) của các số $| A | , | B | , | C |$, chúng ta chia tất cả ba hệ số cho nó, và sau đó chúng ta thực hiện việc chuẩn hóa dấu: nếu $A <0$ hoặc $A = 0, B <0$ thì nhân tất cả ba hệ số với $-1$.
Kết quả là, chúng ta sẽ đi đến kết luận rằng đối với các đường thẳng giống hệt nhau, các bộ ba hệ số giống hệt nhau sẽ thu được, điều này giúp dễ dàng kiểm tra các đường thẳng có bằng nhau hay không.

### Trường hợp số thực (Real case) {: #real-case}

Khi làm việc với số thực, bạn phải luôn nhận thức được các sai số.

Các hệ số $A$ và $B$ sẽ có bậc của các tọa độ ban đầu, hệ số $C$ có bậc của bình phương của chúng. Đây có thể đã là những con số khá lớn, và, ví dụ, khi chúng ta [cắt các đường thẳng](lines-intersection.md), chúng sẽ trở nên lớn hơn nữa, điều này có thể dẫn đến sai số làm tròn lớn ngay cả khi tọa độ của các điểm cuối có bậc $10^3$.

Do đó, khi làm việc với số thực, mong muốn tạo ra cái gọi là **chuẩn hóa** (normalization), điều này rất đơn giản: cụ thể là làm cho các hệ số sao cho $A ^ 2 + B ^ 2 = 1$. Để làm điều này, hãy tính số $Z$:

$$Z = \sqrt{A ^ 2 + B ^ 2},$$

và chia tất cả ba hệ số $A , B , C$ cho nó.

Do đó, bậc của các hệ số $A$ và $B$ sẽ không phụ thuộc vào bậc của các tọa độ đầu vào, và hệ số $C$ sẽ cùng bậc với các tọa độ đầu vào. Trong thực tế, điều này dẫn đến sự cải thiện đáng kể về độ chính xác của các tính toán.

Cuối cùng, chúng tôi đề cập đến việc **so sánh** các đường thẳng - trên thực tế, sau khi chuẩn hóa như vậy, đối với cùng một đường thẳng, chỉ có hai bộ ba hệ số có thể thu được: sai khác nhau một phép nhân với $-1$.
Theo đó, nếu chúng ta thực hiện một chuẩn hóa bổ sung tính đến dấu (nếu $A < -\varepsilon$ hoặc $| A | < \varepsilon$, $B <- \varepsilon$ thì nhân với $-1$), các hệ số kết quả sẽ là duy nhất.

### Trường hợp ba chiều và đa chiều (Three-dimensional and multidimensional case) {: #three-dimensional-and-multidimensional-case}

Ngay cả trong trường hợp ba chiều, **không có phương trình đơn giản** nào mô tả một đường thẳng (nó có thể được định nghĩa là giao điểm của hai mặt phẳng, tức là, một hệ thống gồm hai phương trình, nhưng đây là một phương pháp bất tiện).

Do đó, trong các trường hợp ba chiều và đa chiều, chúng ta phải sử dụng **phương pháp tham số để định nghĩa một đường thẳng**, tức là dưới dạng một điểm $p$ và một vector $v$:

$$p + v t, ~~~ t \in \mathbb{R}.$$

Tức là một đường thẳng là tất cả các điểm có thể thu được từ một điểm $p$ cộng với một vector $v$ với một hệ số tùy ý (tham số $t$).

Việc **xây dựng** một đường thẳng ở dạng tham số dọc theo tọa độ của các đầu mút của một đoạn thẳng là tầm thường, chúng ta chỉ cần lấy một đầu của đoạn thẳng cho điểm $p$, và vector từ đầu thứ nhất đến đầu thứ hai — cho vector $v$.
