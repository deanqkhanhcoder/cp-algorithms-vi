---
tags:
  - Original
---

<!--?title Continued fractions -->
# Liên phân số (Continued fractions) {: #continued-fractions}

**Liên phân số** (continued fraction) là một biểu diễn của số thực dưới dạng một dãy số hữu tỷ hội tụ cụ thể. Chúng rất hữu ích trong lập trình thi đấu vì chúng dễ tính toán và có thể được sử dụng hiệu quả để tìm xấp xỉ hữu tỷ tốt nhất có thể của số thực cơ bản (trong số tất cả các số có mẫu số không vượt quá một giá trị nhất định).

Bên cạnh đó, liên phân số có liên quan chặt chẽ đến thuật toán Euclid, điều này làm cho chúng trở nên hữu ích trong một loạt các bài toán lý thuyết số.

## Biểu diễn liên phân số (Continued fraction representation) {: #continued-fraction-representation}

!!! info "Định nghĩa"
    Cho $a_0, a_1, \dots, a_k \in \mathbb Z$ và $a_1, a_2, \dots, a_k \geq 1$. Khi đó biểu thức

    $$r=a_0 + \frac{1}{a_1 + \frac{1}{\dots + \frac{1}{a_k}}},$$

    được gọi là **biểu diễn liên phân số** của số hữu tỷ $r$ và được ký hiệu ngắn gọn là $r=[a_0;a_1,a_2,\dots,a_k]$.

??? example
    Cho $r = \frac{5}{3}$. Có hai cách để biểu diễn nó dưới dạng liên phân số:

    $$
    \begin{align}
    r = [1;1,1,1] &= 1+\frac{1}{1+\frac{1}{1+\frac{1}{1}}},\\
    r = [1;1,2] &= 1+\frac{1}{1+\frac{1}{2}}.
    \end{align}
    $$

Người ta chứng minh được rằng bất kỳ số hữu tỷ nào cũng có thể được biểu diễn dưới dạng liên phân số theo đúng $2$ cách:

$$r = [a_0;a_1,\dots,a_k,1] = [a_0;a_1,\dots,a_k+1].$$

hơn nữa, độ dài $k$ của liên phân số như vậy được ước tính là $k = O(\log \min(p, q))$ đối với $r=\frac{p}{q}$.

Lý do đằng sau điều này sẽ rõ ràng khi chúng ta đi sâu vào chi tiết của việc xây dựng liên phân số.

!!! info "Định nghĩa"
    Cho $a_0,a_1,a_2, \dots$ là một dãy số nguyên sao cho $a_1, a_2, \dots \geq 1$. Gọi $r_k = [a_0; a_1, \dots, a_k]$. Khi đó biểu thức

    $$r = a_0 + \frac{1}{a_1 + \frac{1}{a_2+\dots}} = \lim\limits_{k \to \infty} r_k.$$

    được gọi là **biểu diễn liên phân số** của số vô tỷ $r$ và được ký hiệu ngắn gọn là $r = [a_0;a_1,a_2,\dots]$.

Lưu ý rằng đối với $r=[a_0;a_1,\dots]$ và số nguyên $k$, ta có $r+k = [a_0+k; a_1, \dots]$.

Một quan sát quan trọng khác là $\frac{1}{r}=[0;a_0, a_1, \dots]$ khi $a_0 > 0$ và $\frac{1}{r} = [a_1; a_2, \dots]$ khi $a_0 = 0$.

!!! info "Định nghĩa"
    Trong định nghĩa trên, các số hữu tỷ $r_0, r_1, r_2, \dots$ được gọi là các **giản phân** (convergents) của $r$.

    Tương ứng, mỗi $r_k = [a_0; a_1, \dots, a_k] = \frac{p_k}{q_k}$ được gọi là **giản phân** thứ $k$ của $r$.

??? example
    Xét $r = [1; 1, 1, 1, \dots]$. Người ta có thể chứng minh bằng quy nạp rằng $r_k = \frac{F_{k+2}}{F_{k+1}}$, trong đó $F_k$ là dãy Fibonacci được định nghĩa là $F_0 = 0$, $F_1 = 1$ và $F_{k} = F_{k-1} + F_{k-2}$. Từ công thức Binet, người ta biết rằng

    $$r_k = \frac{\phi^{k+2} - \psi^{k+2}}{\phi^{k+1} - \psi^{k+1}},$$

    trong đó $\phi = \frac{1+\sqrt{5}}{2} \approx 1.618$ là tỷ lệ vàng và $\psi = \frac{1-\sqrt{5}}{2} = -\frac{1}{\phi} \approx -0.618$. Do đó,

    $$r = 1+\frac{1}{1+\frac{1}{1+\dots}}=\lim\limits_{k \to \infty} r_k = \phi = \frac{1+\sqrt{5}}{2}.$$

    Lưu ý rằng trong trường hợp cụ thể này, một cách khác để tìm $r$ sẽ là giải phương trình

    $$r = 1+\frac{1}{r} \implies r^2 = r + 1. $$


!!! info "Định nghĩa"
    Cho $r_k = [a_0; a_1, \dots, a_{k-1}, a_k]$. Các số $[a_0; a_1, \dots, a_{k-1}, t]$ với $1 \leq t \leq a_k$ được gọi là **bán giản phân** (semiconvergents).

    Chúng ta thường sẽ gọi các (bán) giản phân lớn hơn $r$ là (bán) giản phân **trên** và những (bán) giản phân nhỏ hơn $r$ là (bán) giản phân **dưới**.

!!! info "Định nghĩa"
    Bổ sung cho các giản phân, chúng ta định nghĩa **[thương đầy đủ](https://en.wikipedia.org/wiki/Complete_quotient)** (complete quotients) là $s_k = [a_k; a_{k+1}, a_{k+2}, \dots]$.

    Tương ứng, chúng ta sẽ gọi mỗi $s_k$ là thương đầy đủ thứ $k$ của $r$.

Từ các định nghĩa trên, người ta có thể kết luận rằng $s_k \geq 1$ với $k \geq 1$.

Xem $[a_0; a_1, \dots, a_k]$ như một biểu thức đại số hình thức và cho phép các số thực bất kỳ thay vì $a_i$, chúng ta nhận được

$$r = [a_0; a_1, \dots, a_{k-1}, s_k].$$

Cụ thể, $r = [s_0] = s_0$. Mặt khác, chúng ta có thể biểu diễn $s_k$ dưới dạng

$$s_k = [a_k; s_{k+1}] = a_k + \frac{1}{s_{k+1}},$$

có nghĩa là chúng ta có thể tính $a_k = \lfloor s_k \rfloor$ và $s_{k+1} = (s_k - a_k)^{-1}$ từ $s_k$.

Dãy $a_0, a_1, \dots$ được xác định rõ trừ khi $s_k=a_k$, điều này chỉ xảy ra khi $r$ là một số hữu tỷ.

Do đó, biểu diễn liên phân số được xác định duy nhất cho bất kỳ số vô tỷ $r$ nào.

### Cài đặt {: #implementation}

Trong các đoạn mã, chúng ta hầu như sẽ giả sử các liên phân số hữu hạn.

Từ $s_k$, chuyển đổi sang $s_{k+1}$ trông như sau

$$s_k =\left\lfloor s_k \right\rfloor + \frac{1}{s_{k+1}}.$$

Từ biểu thức này, thương đầy đủ tiếp theo $s_{k+1}$ thu được là

$$s_{k+1} = \left(s_k-\left\lfloor s_k\right\rfloor\right)^{-1}.$$

Đối với $s_k=\frac{p}{q}$ điều đó có nghĩa là

$$
s_{k+1} = \left(\frac{p}{q}-\left\lfloor \frac{p}{q} \right\rfloor\right)^{-1} = \frac{q}{p-q\cdot \lfloor \frac{p}{q} \rfloor} = \frac{q}{p \bmod q}.
$$

Do đó, việc tính toán biểu diễn liên phân số cho $r=\frac{p}{q}$ tuân theo các bước của thuật toán Euclid cho $p$ và $q$.

Từ điều này cũng suy ra rằng $\gcd(p_k, q_k) = 1$ đối với $\frac{p_k}{q_k} = [a_0; a_1, \dots, a_k]$. Do đó, các giản phân luôn là tối giản.

=== "C++"
    ```cpp
    auto fraction(int p, int q) {
        vector<int> a;
        while(q) {
            a.push_back(p / q);
            tie(p, q) = make_pair(q, p % q);
        }
        return a;
    }
    ```
=== "Python"
    ```py
    def fraction(p, q):
        a = []
        while q:
            a.append(p // q)
            p, q = q, p % q
        return a
    ```

## Các kết quả chính {: #key-results}

Để cung cấp một số động lực cho việc nghiên cứu sâu hơn về liên phân số, chúng tôi đưa ra một số sự thật chính ngay bây giờ.

??? note "Công thức truy hồi"
    Đối với các giản phân $r_k = \frac{p_k}{q_k}$, công thức truy hồi sau đây được áp dụng, cho phép tính toán nhanh chóng:
    
    $$\frac{p_k}{q_k}=\frac{a_k p_{k-1} + p_{k-2}}{a_k q_{k-1} + q_{k-2}},$$
    
    trong đó $\frac{p_{-1}}{q_{-1}}=\frac{1}{0}$ và $\frac{p_{-2}}{q_{-2}}=\frac{0}{1}$.

??? note "Độ lệch"
    Độ lệch của $r_k = \frac{p_k}{q_k}$ so với $r$ có thể được ước tính chung là
    
    $$\left|\frac{p_k}{q_k}-r\right| \leq \frac{1}{q_k q_{k+1}} \leq \frac{1}{q_k^2}.$$
    
    Nhân cả hai vế với $q_k$, chúng ta nhận được ước tính thay thế:
    
    $$|p_k - q_k r| \leq \frac{1}{q_{k+1}}.$$

    Từ công thức truy hồi ở trên suy ra rằng $q_k$ tăng nhanh ít nhất như số Fibonacci.

    Trong hình dưới đây bạn có thể thấy trực quan hóa cách các giản phân $r_k$ tiến tới $r=\frac{1+\sqrt 5}{2}$:

    ![](https://upload.wikimedia.org/wikipedia/commons/b/b4/Golden_ration_convergents.svg)

    $r=\frac{1+\sqrt 5}{2}$ được biểu thị bằng đường chấm xanh. Các giản phân lẻ tiến tới nó từ phía trên và các giản phân chẵn tiến tới nó từ phía dưới.

??? note "Bao lồi lưới"
    Xem xét các bao lồi của các điểm nằm trên và dưới đường thẳng $y=rx$.
    
    Các giản phân lẻ $(q_k;p_k)$ là các đỉnh của bao lồi trên, trong khi các giản phân chẵn $(q_k;p_k)$ là các đỉnh của bao lồi dưới.
    
    Tất cả các đỉnh nguyên trên các bao lồi thu được là $(q;p)$ sao cho
    
    $$\frac{p}{q} = \frac{tp_{k-1} + p_{k-2}}{tq_{k-1} + q_{k-2}}$$
    
    đối với số nguyên $0 \leq t \leq a_k$. Nói cách khác, tập hợp các điểm lưới trên các bao lồi tương ứng với tập hợp các bán giản phân.

    Trong hình dưới đây, bạn có thể thấy các giản phân và bán giản phân (các điểm màu xám trung gian) của $r=\frac{9}{7}$.

    ![](https://upload.wikimedia.org/wikipedia/commons/9/92/Continued_convergents_geometry.svg)

??? note "Xấp xỉ tốt nhất"
    Cho $\frac{p}{q}$ là phân số để tối thiểu hóa $\left|r-\frac{p}{q}\right|$ với điều kiện $q \leq x$ cho một số $x$.
    
    Khi đó $\frac{p}{q}$ là một bán giản phân của $r$.

Sự thật cuối cùng cho phép tìm các xấp xỉ hữu tỷ tốt nhất của $r$ bằng cách kiểm tra các bán giản phân của nó.

Dưới đây bạn sẽ tìm thấy giải thích thêm và một chút trực giác cũng như cách giải thích cho những sự thật này.

## Giản phân (Convergents) {: #convergents}

Hãy xem xét kỹ hơn các giản phân đã được định nghĩa trước đó. Đối với $r=[a_0, a_1, a_2, \dots]$, các giản phân của nó là

\begin{gather}
r_0=[a_0],\\r_1=[a_0, a_1],\\ \dots,\\ r_k=[a_0, a_1, \dots, a_k].
\end{gather}

Giản phân là khái niệm cốt lõi của liên phân số, vì vậy việc nghiên cứu các tính chất của chúng là rất quan trọng.

Đối với số $r$, giản phân thứ $k$ của nó $r_k = \frac{p_k}{q_k}$ có thể được tính như sau

$$r_k = \frac{P_k(a_0,a_1,\dots,a_k)}{P_{k-1}(a_1,\dots,a_k)} = \frac{a_k p_{k-1} + p_{k-2}}{a_k q_{k-1} + q_{k-2}},$$

trong đó $P_k(a_0,\dots,a_k)$ là [continuant](https://en.wikipedia.org/wiki/Continuant_(mathematics)), một đa thức nhiều biến được định nghĩa là

$$P_k(x_0,x_1,\dots,x_k) = \det \begin{bmatrix}
x_k & 1 & 0 & \dots & 0 \\
-1 & x_{k-1} & 1 & \dots & 0 \\
0 & -1 & x_2 & . & \vdots \\
\vdots & \vdots & . & \ddots & 1 \\
0 & 0 & \dots & -1 & x_0
\end{bmatrix}_{\textstyle .}$$

Do đó, $r_k$ là một [mediant](https://en.wikipedia.org/wiki/Mediant_(mathematics)) có trọng số của $r_{k-1}$ và $r_{k-2}$.

Để nhất quán, hai giản phân bổ sung $r_{-1} = \frac{1}{0}$ và $r_{-2} = \frac{0}{1}$ được định nghĩa.

??? hint "Giải thích chi tiết"

    Tử số và mẫu số của $r_k$ có thể được xem như các đa thức nhiều biến của $a_0, a_1, \dots, a_k$:

    $$r_k = \frac{P_k(a_0, a_1, \dots, a_k)}{Q_k(a_0,a_1, \dots, a_k)}.$$

    Từ định nghĩa của các giản phân,

    $$r_k = a_0 + \frac{1}{[a_1;a_2,\dots, a_k]}= a_0 + \frac{Q_{k-1}(a_1, \dots, a_k)}{P_{k-1}(a_1, \dots, a_k)} = \frac{a_0 P_{k-1}(a_1, \dots, a_k) + Q_{k-1}(a_1, \dots, a_k)}{P_{k-1}(a_1, \dots, a_k)}.$$

    Từ điều này suy ra $Q_k(a_0, \dots, a_k) = P_{k-1}(a_1, \dots, a_k)$. Điều này mang lại mối quan hệ

    $$P_k(a_0, \dots, a_k) = a_0 P_{k-1}(a_1, \dots, a_k) + P_{k-2}(a_2, \dots, a_k).$$

    Ban đầu, $r_0 = \frac{a_0}{1}$ và $r_1 = \frac{a_0 a_1 + 1}{a_1}$, do đó

    $$\begin{align}P_0(a_0)&=a_0,\\ P_1(a_0, a_1) &= a_0 a_1 + 1.\end{align}$$

    Để nhất quán, thuận tiện khi định nghĩa $P_{-1} = 1$ và $P_{-2}=0$ và nói một cách hình thức rằng $r_{-1} = \frac{1}{0}$ và $r_{-2}=\frac{0}{1}$.

    Từ giải tích số, người ta biết rằng định thức của một ma trận ba đường chéo tùy ý

    $$T_k = \det \begin{bmatrix}
    a_0 & b_0 & 0 & \dots & 0 \\
    c_0 & a_1 & b_1 & \dots & 0 \\
    0 & c_1 & a_2 & . & \vdots \\
    \vdots & \vdots & . & \ddots & c_{k-1} \\
    0 & 0 & \dots & b_{k-1} & a_k
    \end{bmatrix}$$

    có thể được tính toán đệ quy là $T_k = a_k T_{k-1} - b_{k-1} c_{k-1} T_{k-2}$. So sánh nó với $P_k$, chúng ta có một biểu thức trực tiếp

    $$P_k = \det \begin{bmatrix}
    x_k & 1 & 0 & \dots & 0 \\
    -1 & x_{k-1} & 1 & \dots & 0 \\
    0 & -1 & x_2 & . & \vdots \\
    \vdots & \vdots & . & \ddots & 1 \\
    0 & 0 & \dots & -1 & x_0
    \end{bmatrix}_{\textstyle .}$$

    Đa thức này còn được gọi là [continuant](https://en.wikipedia.org/wiki/Continuant_(mathematics)) do mối quan hệ chặt chẽ của nó với liên phân số. Continuant sẽ không thay đổi nếu trình tự trên đường chéo chính bị đảo ngược. Điều này mang lại một công thức thay thế để tính toán nó:

    $$P_k(a_0, \dots, a_k) = a_k P_{k-1}(a_0, \dots, a_{k-1}) + P_{k-2}(a_0, \dots, a_{k-2}).$$

### Cài đặt {: #implementation-1}

Chúng ta sẽ tính toán các giản phân dưới dạng một cặp các dãy $p_{-2}, p_{-1}, p_0, p_1, \dots, p_k$ và $q_{-2}, q_{-1}, q_0, q_1, \dots, q_k$:

=== "C++"
    ```cpp
    auto convergents(vector<int> a) {
        vector<int> p = {0, 1};
        vector<int> q = {1, 0};
        for(auto it: a) {
            p.push_back(p[p.size() - 1] * it + p[p.size() - 2]);
            q.push_back(q[q.size() - 1] * it + q[q.size() - 2]);
        }
        return make_pair(p, q);
    }
    ```
=== "Python"
    ```py
    def convergents(a):
        p = [0, 1]
        q = [1, 0]
        for it in a:
            p.append(p[-1]*it + p[-2])
            q.append(q[-1]*it + q[-2])
        return p, q
    ```

## Cây liên phân số (Trees of continued fractions) {: #trees-of-continued-fractions}

Có hai cách chính để hợp nhất tất cả các liên phân số có thể thành các cấu trúc cây hữu ích.

### Cây Stern-Brocot (Stern-Brocot tree) {: #stern-brocot-tree}

[Cây Stern-Brocot](../others/stern_brocot_tree_farey_sequences.md) là một cây tìm kiếm nhị phân chứa tất cả các số hữu tỷ dương phân biệt.

Cây thường trông như sau:

<figure>
<img src="https://upload.wikimedia.org/wikipedia/commons/3/37/SternBrocotTree.svg">
<figcaption>
<a href="https://commons.wikimedia.org/wiki/File:SternBrocotTree.svg">Hình ảnh</a> bởi <a href="https://commons.wikimedia.org/wiki/User:Aaron_Rotenberg">Aaron Rotenberg</a> được cấp phép theo <a href="https://creativecommons.org/licenses/by-sa/3.0/deed.en">CC BY-SA 3.0</a>
</figcaption>
</figure>

Các phân số $\frac{0}{1}$ và $\frac{1}{0}$ được giữ "ảo" ở phía bên trái và bên phải của cây tương ứng.

Khi đó phân số trong một nút là mediant $\frac{a+c}{b+d}$ của hai phân số $\frac{a}{b}$ và $\frac{c}{d}$ phía trên nó.

Công thức truy hồi $\frac{p_k}{q_k}=\frac{a_k p_{k-1} + p_{k-2}}{a_k q_{k-1} + q_{k-2}}$ có nghĩa là biểu diễn liên phân số mã hóa đường dẫn đi đến $\frac{p_k}{q_k}$ trong cây. Để tìm $[a_0; a_1, \dots, a_{k}, 1]$, người ta phải thực hiện $a_0$ bước sang phải, $a_1$ bước sang trái, $a_2$ bước sang phải vân vân cho đến $a_k$.

Cha của $[a_0; a_1, \dots, a_k,1]$ khi đó là phân số thu được bằng cách lùi lại một bước theo hướng cuối cùng đã sử dụng.

Nói cách khác, đó là $[a_0; a_1, \dots, a_k-1,1]$ khi $a_k > 1$ và $[a_0; a_1, \dots, a_{k-1}, 1]$ khi $a_k = 1$.

Do đó, các con của $[a_0; a_1, \dots, a_k, 1]$ là $[a_0; a_1, \dots, a_k+1, 1]$ và $[a_0; a_1, \dots, a_k, 1, 1]$.

Hãy đánh chỉ số cây Stern-Brocot. Đỉnh gốc được gán chỉ số $1$. Sau đó đối với một đỉnh $v$, chỉ số của con bên trái được gán bằng cách thay đổi bit dẫn đầu của $v$ từ $1$ thành $10$ và đối với con bên phải, nó được gán bằng cách thay đổi bit dẫn đầu từ $1$ thành $11$:

<figure><img src="https://upload.wikimedia.org/wikipedia/commons/1/18/Stern-brocot-index.svg" width="500px"/></figure>

Trong cách đánh chỉ số này, biểu diễn liên phân số của một số hữu tỷ chỉ định [mã hóa độ dài chạy](https://en.wikipedia.org/wiki/Run-length_encoding) (run-length encoding) của chỉ số nhị phân của nó.

Đối với $\frac{5}{2} = [2;2] = [2;1,1]$, chỉ số của nó là $1011_2$ và mã hóa độ dài chạy của nó, xét các bit theo thứ tự tăng dần, là $[2;1,1]$.

Một ví dụ khác là $\frac{2}{5} = [0;2,2]=[0;2,1,1]$, có chỉ số $1100_2$ và mã hóa độ dài chạy của nó, quả thực, là $[0;2,2]$.

Đáng chú ý là cây Stern-Brocot, trên thực tế, là một [treap](../data_structures/treap.md). Nghĩa là, nó là một cây tìm kiếm nhị phân theo $\frac{p}{q}$, nhưng nó là một heap theo cả $p$ và $q$.

!!! example "So sánh các liên phân số"
    Bạn được cho $A=[a_0; a_1, \dots, a_n]$ và $B=[b_0; b_1, \dots, b_m]$. Phân số nào nhỏ hơn?
??? hint "Lời giải"
    Giả sử rằng $A$ và $B$ là số vô tỷ và biểu diễn liên phân số của chúng biểu thị một sự đi xuống vô tận trong cây Stern-Brocot.

    Như chúng ta đã đề cập, trong biểu diễn này $a_0$ biểu thị số lần rẽ phải trong quá trình đi xuống, $a_1$ biểu thị số lần rẽ trái tiếp theo, v.v. Do đó, khi chúng ta so sánh $a_k$ và $b_k$, nếu $a_k = b_k$ chúng ta chỉ nên chuyển sang so sánh $a_{k+1}$ và $b_{k+1}$. Ngược lại, nếu chúng ta đang ở các lần rẽ phải, chúng ta nên kiểm tra xem $a_k < b_k$ và nếu chúng ta đang ở các lần rẽ trái, chúng ta nên kiểm tra xem $a_k > b_k$ để biết liệu $A < B$.

    Nói cách khác, đối với $A$ và $B$ vô tỷ, $A < B$ khi và chỉ khi $(a_0, -a_1, a_2, -a_3, \dots) < (b_0, -b_1, b_2, -b_3, \dots)$ với so sánh từ điển.

    Bây giờ, sử dụng $\infty$ một cách hình thức như một phần tử của biểu diễn liên phân số, có thể mô phỏng các số vô tỷ $A-\varepsilon$ và $A+\varepsilon$, nghĩa là, các phần tử nhỏ hơn (lớn hơn) $A$, nhưng lớn hơn (nhỏ hơn) bất kỳ số thực nào khác. Cụ thể, đối với $A=[a_0; a_1, \dots, a_n]$, một trong hai phần tử này có thể được mô phỏng là $[a_0; a_1, \dots, a_n, \infty]$ và phần tử kia có thể được mô phỏng là $[a_0; a_1, \dots, a_n - 1, 1, \infty]$.

    Cái nào tương ứng với $A-\varepsilon$ và cái nào với $A+\varepsilon$ có thể được xác định bởi tính chẵn lẻ của $n$ hoặc bằng cách so sánh chúng như các số vô tỷ.

    === "Python"
        ```py
        # check if a < b assuming that a[-1] = b[-1] = infty and a != b
        def less(a, b):
            a = [(-1)**i*a[i] for i in range(len(a))]
            b = [(-1)**i*b[i] for i in range(len(b))]
            return a < b

        # [a0; a1, ..., ak] -> [a0, a1, ..., ak-1, 1]
        def expand(a):
            if a: # empty a = inf
                a[-1] -= 1
                a.append(1)
            return a

        # return a-eps, a+eps
        def pm_eps(a):
            b = expand(a.copy())
            a.append(float('inf'))
            b.append(float('inf'))
            return (a, b) if less(a, b) else (b, a)
        ```

!!! example "Điểm trong tốt nhất"
    Bạn được cho $\frac{0}{1} \leq \frac{p_0}{q_0} < \frac{p_1}{q_1} \leq \frac{1}{0}$. Tìm số hữu tỷ $\frac{p}{q}$ sao cho $(q; p)$ nhỏ nhất theo thứ tự từ điển và $\frac{p_0}{q_0} < \frac{p}{q} < \frac{p_1}{q_1}$.

??? hint "Lời giải"
    Về mặt cây Stern-Brocot, điều đó có nghĩa là chúng ta cần tìm LCA của $\frac{p_0}{q_0}$ và $\frac{p_1}{q_1}$. Do mối liên hệ giữa cây Stern-Brocot và liên phân số, LCA này sẽ tương ứng đại khái với tiền tố chung lớn nhất của các biểu diễn liên phân số cho $\frac{p_0}{q_0}$ và $\frac{p_1}{q_1}$.

    Vì vậy, nếu $\frac{p_0}{q_0} = [a_0; a_1, \dots, a_{k-1}, a_k, \dots]$ và $\frac{p_1}{q_1} = [a_0; a_1, \dots, a_{k-1}, b_k, \dots]$ là các số vô tỷ, LCA là $[a_0; a_1, \dots, \min(a_k, b_k)+1]$.

    Đối với $r_0$ và $r_1$ hữu tỷ, một trong số chúng có thể chính là LCA, điều này đòi hỏi chúng ta phải xét trường hợp. Để đơn giản hóa lời giải cho $r_0$ và $r_1$ hữu tỷ, có thể sử dụng biểu diễn liên phân số của $r_0 + \varepsilon$ và $r_1 - \varepsilon$ đã được rút ra trong bài toán trước.

    === "Python"
        ```py
        # finds lexicographically smallest (q, p)
        # such that p0/q0 < p/q < p1/q1
        def middle(p0, q0, p1, q1):
            a0 = pm_eps(fraction(p0, q0))[1]
            a1 = pm_eps(fraction(p1, q1))[0]
            a = []
            for i in range(min(len(a0), len(a1))):
                a.append(min(a0[i], a1[i]))
                if a0[i] != a1[i]:
                    break
            a[-1] += 1
            p, q = convergents(a)
            return p[-1], q[-1]
        ```

!!! example "[GCJ 2019, Round 2 - New Elements: Part 2](https://codingcompetitions.withgoogle.com/codejam/round/0000000000051679/0000000000146184)"
    Bạn được cho $N$ cặp số nguyên dương $(C_i, J_i)$. Bạn cần tìm một cặp số nguyên dương $(x, y)$ sao cho $C_i x + J_i y$ là một dãy tăng nghiêm ngặt.

    Trong số các cặp như vậy, hãy tìm cặp nhỏ nhất theo thứ tự từ điển.
??? hint "Lời giải"
    Diễn giải lại đề bài, $A_i x + B_i y$ phải dương với mọi $i$, trong đó $A_i = C_i - C_{i-1}$ và $B_i = J_i - J_{i-1}$.

    Trong số các phương trình như vậy, chúng ta có bốn nhóm quan trọng cho $A_i x + B_i y > 0$:

    1. $A_i, B_i > 0$ có thể bị bỏ qua vì chúng ta đang tìm kiếm $x, y > 0$.
    2. $A_i, B_i \leq 0$ sẽ cung cấp "IMPOSSIBLE" như một câu trả lời.
    3. $A_i > 0$, $B_i \leq 0$. Các ràng buộc như vậy tương đương với $\frac{y}{x} < \frac{A_i}{-B_i}$.
    4. $A_i \leq 0$, $B_i > 0$. Các ràng buộc như vậy tương đương với $\frac{y}{x} > \frac{-A_i}{B_i}$.

    Gọi $\frac{p_0}{q_0}$ là $\frac{-A_i}{B_i}$ lớn nhất từ nhóm thứ tư và $\frac{p_1}{q_1}$ là $\frac{A_i}{-B_i}$ nhỏ nhất từ nhóm thứ ba.

    Bài toán bây giờ là, cho $\frac{p_0}{q_0} < \frac{p_1}{q_1}$, tìm một phân số $\frac{p}{q}$ sao cho $(q;p)$ nhỏ nhất theo thứ tự từ điển và $\frac{p_0}{q_0} < \frac{p}{q} < \frac{p_1}{q_1}$.
    === "Python"
        ```py
            def solve():
            n = int(input())
            C = [0] * n
            J = [0] * n
            # p0/q0 < y/x < p1/q1
            p0, q0 = 0, 1
            p1, q1 = 1, 0
            fail = False
            for i in range(n):
                C[i], J[i] = map(int, input().split())
                if i > 0:
                    A = C[i] - C[i-1]
                    B = J[i] - J[i-1]
                    if A <= 0 and B <= 0:
                        fail = True
                    elif B > 0 and A < 0: # y/x > (-A)/B if B > 0
                        if (-A)*q0 > p0*B:
                            p0, q0 = -A, B
                    elif B < 0 and A > 0: # y/x < A/(-B) if B < 0
                        if A*q1 < p1*(-B):
                            p1, q1 = A, -B
            if p0*q1 >= p1*q0 or fail:
                return 'IMPOSSIBLE'

            p, q = middle(p0, q0, p1, q1)
            return str(q) + ' ' + str(p)
        ```

### Cây Calkin-Wilf (Calkin-Wilf tree) {: #calkin-wilf-tree}

Một cách đơn giản hơn để tổ chức các liên phân số trong một cây nhị phân là [cây Calkin-Wilf](https://en.wikipedia.org/wiki/Calkin–Wilf_tree).

Cây thường trông như sau:

<figure>
<img src="https://upload.wikimedia.org/wikipedia/commons/8/82/Calkin–Wilf_tree.svg" width="500px"/>
<figcaption><a href="https://commons.wikimedia.org/wiki/File:Calkin–Wilf_tree.svg">Hình ảnh</a> bởi <a href="https://commons.wikimedia.org/wiki/User:Olli_Niemitalo">Olli Niemitalo</a>, <a href="https://commons.wikimedia.org/wiki/User:Proz">Proz</a> được cấp phép theo <a href="https://creativecommons.org/publicdomain/zero/1.0/deed.en">CC0 1.0</a></figcaption>
</figure>

Ở gốc của cây, là số $\frac{1}{1}$. Sau đó, đối với đỉnh có số $\frac{p}{q}$, các con của nó là $\frac{p}{p+q}$ và $\frac{p+q}{q}$.

Không giống như cây Stern-Brocot, cây Calkin-Wilf không phải là cây *tìm kiếm* nhị phân, vì vậy nó không thể được sử dụng để thực hiện tìm kiếm nhị phân hữu tỷ.

Trong cây Calkin-Wilf, cha trực tiếp của một phân số $\frac{p}{q}$ là $\frac{p-q}{q}$ khi $p>q$ và $\frac{p}{q-p}$ khi ngược lại.

Đối với cây Stern-Brocot, chúng ta đã sử dụng công thức truy hồi cho các giản phân. Để vẽ mối liên hệ giữa liên phân số và cây Calkin-Wilf, chúng ta nên nhớ lại công thức truy hồi cho các thương đầy đủ. Nếu $s_k = \frac{p}{q}$, thì $s_{k+1} = \frac{q}{p \mod q} = \frac{q}{p-\lfloor p/q \rfloor \cdot q}$.

Mặt khác, nếu chúng ta liên tục đi từ $s_k = \frac{p}{q}$ đến cha của nó trong cây Calkin-Wilf khi $p > q$, chúng ta sẽ kết thúc ở $\frac{p \mod q}{q} = \frac{1}{s_{k+1}}$. Nếu chúng ta tiếp tục làm như vậy, chúng ta sẽ kết thúc ở $s_{k+2}$, sau đó là $\frac{1}{s_{k+3}}$ và cứ thế. Từ điều này chúng ta có thể suy ra rằng:

1. Khi $a_0> 0$, cha trực tiếp của $[a_0; a_1, \dots, a_k]$ trong cây Calkin-Wilf là $\frac{p-q}{q}=[a_0 - 1; a_1, \dots, a_k]$.
2. Khi $a_0 = 0$ và $a_1 > 1$, cha trực tiếp của nó là $\frac{p}{q-p} = [0; a_1 - 1, a_2, \dots, a_k]$.
3. Và khi $a_0 = 0$ và $a_1 = 1$, cha trực tiếp của nó là $\frac{p}{q-p} = [a_2; a_3, \dots, a_k]$.

Tương ứng, các con của $\frac{p}{q} = [a_0; a_1, \dots, a_k]$ là

1. $\frac{p+q}{q}=1+\frac{p}{q}$, đó là $[a_0+1; a_1, \dots, a_k]$,
2. $\frac{p}{p+q} = \frac{1}{1+\frac{q}{p}}$, đó là $[0, 1, a_0, a_1, \dots, a_k]$ đối với $a_0 > 0$ và $[0, a_1+1, a_2, \dots, a_k]$ đối với $a_0=0$.

Đáng chú ý, nếu chúng ta liệt kê các đỉnh của cây Calkin-Wilf theo thứ tự tìm kiếm theo chiều rộng (tức là, gốc có số $1$, và các con của đỉnh $v$ có chỉ số $2v$ và $2v+1$ tương ứng), chỉ số của số hữu tỷ trong cây Calkin-Wilf sẽ giống như trong cây Stern-Brocot.

Do đó, các số trên cùng một cấp của cây Stern-Brocot và cây Calkin-Wilf là giống nhau, nhưng thứ tự của chúng khác nhau thông qua [bit-reversal permutation](https://en.wikipedia.org/wiki/Bit-reversal_permutation).
## Sự hội tụ (Convergence) {: #convergence}

Đối với số $r$ và giản phân thứ $k$ của nó $r_k=\frac{p_k}{q_k}$ công thức sau đây được áp dụng:

$$r_k = a_0 + \sum\limits_{i=1}^k \frac{(-1)^{i-1}}{q_i q_{i-1}}.$$

Cụ thể, nó có nghĩa là

$$r_k - r_{k-1} = \frac{(-1)^{k-1}}{q_k q_{k-1}}$$

và 

$$p_k q_{k-1} - p_{k-1} q_k = (-1)^{k-1}.$$

Từ điều này chúng ta có thể kết luận rằng

$$\left| r-\frac{p_k}{q_k} \right| \leq \frac{1}{q_{k+1}q_k} \leq \frac{1}{q_k^2}.$$

Bất đẳng thức sau là do thực tế rằng $r_k$ và $r_{k+1}$ thường nằm ở các phía khác nhau của $r$, do đó

$$|r-r_k| = |r_k-r_{k+1}|-|r-r_{k+1}| \leq |r_k - r_{k+1}|.$$

??? tip "Giải thích chi tiết"

    Để ước tính $|r-r_k|$, chúng ta bắt đầu bằng cách ước tính sự khác biệt giữa các giản phân liền kề. Theo định nghĩa,

    $$\frac{p_k}{q_k} - \frac{p_{k-1}}{q_{k-1}} = \frac{p_k q_{k-1} - p_{k-1} q_k}{q_k q_{k-1}}.$$

    Thay thế $p_k$ và $q_k$ trong tử số bằng các công thức truy hồi của chúng, chúng ta nhận được

    $$\begin{align} p_k q_{k-1} - p_{k-1} q_k &= (a_k p_{k-1} + p_{k-2}) q_{k-1} - p_{k-1} (a_k q_{k-1} + q_{k-2})
    \\&= p_{k-2} q_{k-1} - p_{k-1} q_{k-2},\end{align}$$

    do đó tử số của $r_k - r_{k-1}$ luôn là tử số phủ định của $r_{k-1} - r_{k-2}$. Nó, đến lượt nó, bằng $1$ đối với

    $$r_1 - r_0=\left(a_0+\frac{1}{a_1}\right)-a_0=\frac{1}{a_1},$$

    do đó

    $$r_k - r_{k-1} = \frac{(-1)^{k-1}}{q_k q_{k-1}}.$$

    Điều này mang lại một biểu diễn thay thế của $r_k$ như một tổng riêng của chuỗi vô hạn:

    $$r_k = (r_k - r_{k-1}) + \dots + (r_1 - r_0) + r_0
    = a_0 + \sum\limits_{i=1}^k \frac{(-1)^{i-1}}{q_i q_{i-1}}.$$

    Từ quan hệ truy hồi suy ra rằng $q_k$ tăng đơn điệu nhanh ít nhất như số Fibonacci, do đó

    $$r = \lim\limits_{k \to \infty} r_k = a_0 + \sum\limits_{i=1}^\infty \frac{(-1)^{i-1}}{q_i q_{i-1}}$$

    luôn được xác định rõ, vì chuỗi cơ bản luôn hội tụ. Đáng chú ý, chuỗi dư

    $$r-r_k = \sum\limits_{i=k+1}^\infty \frac{(-1)^{i-1}}{q_i q_{i-1}}$$

    có cùng dấu với $(-1)^k$ do tốc độ $q_i q_{i-1}$ giảm. Do đó các $r_k$ có chỉ số chẵn tiến tới $r$ từ phía dưới trong khi các $r_k$ có chỉ số lẻ tiến tới nó từ phía trên:

    <figure><img src="https://upload.wikimedia.org/wikipedia/commons/b/b4/Golden_ration_convergents.svg" width="600px"/>
    <figcaption>_Các giản phân của $r=\phi = \frac{1+\sqrt{5}}{2}=[1;1,1,\dots]$ và khoảng cách của chúng tới $r$._</figcaption></figure>

    Từ hình này chúng ta có thể thấy rằng

    $$|r-r_k| = |r_k - r_{k+1}| - |r-r_{k+1}| \leq |r_k - r_{k+1}|,$$

    do đó khoảng cách giữa $r$ và $r_k$ không bao giờ lớn hơn khoảng cách giữa $r_k$ và $r_{k+1}$:

    $$\left|r-\frac{p_k}{q_k}\right| \leq \frac{1}{q_k q_{k+1}} \leq \frac{1}{q_k^2}.$$

!!! example "Euclid mở rộng?"
    Bạn được cho $A, B, C \in \mathbb Z$. Tìm $x, y \in \mathbb Z$ sao cho $Ax + By = C$.
??? hint "Lời giải"
    Mặc dù bài toán này thường được giải bằng [thuật toán Euclid mở rộng](../algebra/extended-euclid-algorithm.md), có một giải pháp đơn giản và trực tiếp với liên phân số.

    Cho $\frac{A}{B}=[a_0; a_1, \dots, a_k]$. Đã được chứng minh ở trên rằng $p_k q_{k-1} - p_{k-1} q_k = (-1)^{k-1}$. Thay thế $p_k$ và $q_k$ bằng $A$ và $B$, chúng ta nhận được

    $$Aq_{k-1} - Bp_{k-1} = (-1)^{k-1} g,$$

    trong đó $g = \gcd(A, B)$. Nếu $C$ chia hết cho $g$, thì nghiệm là $x = (-1)^{k-1}\frac{C}{g} q_{k-1}$ và $y = (-1)^{k}\frac{C}{g} p_{k-1}$.
    
    === "Python"
        ```py
        # return (x, y) such that Ax+By=C
        # assumes that such (x, y) exists
        def dio(A, B, C):
            p, q = convergents(fraction(A, B))
            C //= A // p[-1] # divide by gcd(A, B)
            t = (-1) if len(p) % 2 else 1
            return t*C*q[-2], -t*C*p[-2]
        ```

## Biến đổi phân tuyến tính (Linear fractional transformations) {: #linear-fractional-transformations}

Một khái niệm quan trọng khác đối với liên phân số là cái gọi là [biến đổi phân tuyến tính](https://en.wikipedia.org/wiki/Linear_fractional_transformation).

!!! info "Định nghĩa"
    Một **biến đổi phân tuyến tính** là một hàm $f : \mathbb R \to \mathbb R$ sao cho $f(x) = \frac{ax+b}{cx+d}$ với một số $a,b,c,d \in \mathbb R$.

Một hợp thành $(L_0 \circ L_1)(x) = L_0(L_1(x))$ của các biến đổi phân tuyến tính $L_0(x)=\frac{a_0 x + b_0}{c_0 x + d_0}$ và $L_1(x)=\frac{a_1 x + b_1}{c_1 x + d_1}$ chính nó là một biến đổi phân tuyến tính:

$$\frac{a_0\frac{a_1 x + b_1}{c_1 x + d_1} + b_0}{c_0 \frac{a_1 x + b_1}{c_1 x + d_1} + d_0} = \frac{a_0(a_1 x + b_1) + b_0 (c_1 x + d_1)}{c_0 (a_1 x + b_1) + d_0 (c_1 x + d_1)} = \frac{(a_0 a_1 + b_0 c_1) x + (a_0 b_1 + b_0 d_1)}{(c_0 a_1 + d_0 c_1) x + (c_0 b_1 + d_0 d_1)}.$$

Nghịch đảo của một biến đổi phân tuyến tính, cũng là một biến đổi phân tuyến tính:

$$y = \frac{ax+b}{cx+d} \iff y(cx+d) = ax + b \iff x = -\frac{dy-b}{cy-a}.$$
!!! example "[DMOPC '19 Contest 7 P4 - Bob and Continued Fractions](https://dmoj.ca/problem/dmopc19c7p4)"
    Bạn được cho một mảng các số nguyên dương $a_1, \dots, a_n$. Bạn cần trả lời $m$ truy vấn. Mỗi truy vấn là để tính $[a_l; a_{l+1}, \dots, a_r]$.
??? hint "Lời giải"
    Chúng ta có thể giải quyết vấn đề này với segment tree nếu chúng ta có thể nối các liên phân số.

    Một điều thường đúng là $[a_0; a_1, \dots, a_k, b_0, b_1, \dots, b_k] = [a_0; a_1, \dots, a_k, [b_1; b_2, \dots, b_k]]$.

    Hãy ký hiệu $L_{k}(x) = [a_k; x] = a_k + \frac{1}{x} = \frac{a_k\cdot x+1}{1\cdot x + 0}$. Lưu ý rằng $L_k(\infty) = a_k$. Trong ký hiệu này, điều sau đúng

    $$[a_0; a_1, \dots, a_k, x] = [a_0; [a_1; [\dots; [a_k; x]]]] = (L_0 \circ L_1 \circ \dots \circ L_k)(x) = \frac{p_k x + p_{k-1}}{q_k x + q_{k-1}}.$$

    Do đó, bài toán quy về việc tính toán

    $$(L_l \circ L_{l+1} \circ \dots \circ L_r)(\infty).$$

    Hợp thành của các biến đổi có tính kết hợp, vì vậy có thể tính toán trong mỗi nút của segment tree hợp thành của các biến đổi trong cây con của nó.

!!! example "Biến đổi phân tuyến tính của một liên phân số"
    Cho $L(x) = \frac{ax+b}{cx+d}$. Tính biểu diễn liên phân số $[b_0; b_1, \dots, b_m]$ của $L(A)$ đối với $A=[a_0; a_1, \dots, a_n]$.

    _Điều này cho phép tính $A + \frac{p}{q} = \frac{qA + p}{q}$ và $A \cdot \frac{p}{q} = \frac{p A}{q}$ với bất kỳ $\frac{p}{q}$._

??? hint "Lời giải"
    Như chúng ta đã lưu ý ở trên, $[a_0; a_1, \dots, a_k] = (L_{a_0} \circ L_{a_1} \circ \dots \circ L_{a_k})(\infty)$, do đó $L([a_0; a_1, \dots, a_k]) = (L \circ L_{a_0} \circ L_{a_1} \circ \dots L_{a_k})(\infty)$.

    Vì vậy, bằng cách thêm $L_{a_0}$, $L_{a_1}$ và vân vân một cách tuần tự, chúng ta sẽ có thể tính

    $$(L \circ L_{a_0} \circ \dots \circ L_{a_k})(x) = L\left(\frac{p_k x + p_{k-1}}{q_k x + q_{k-1}}\right)=\frac{a_k x + b_k}{c_k x + d_k}.$$

    Vì $L(x)$ khả nghịch, nó cũng đơn điệu trong $x$. Do đó, với bất kỳ $x \geq 0$ điều sau đúng $L(\frac{p_k x + p_{k-1}}{q_k x + q_{k-1}})$ nằm giữa $L(\frac{p_k}{q_k}) = \frac{a_k}{c_k}$ và $L(\frac{p_{k-1}}{q_{k-1}}) = \frac{b_k}{d_k}$.

    Hơn nữa, đối với $x=[a_{k+1}; \dots, a_n]$ nó bằng với $L(A)$. Do đó, $b_0 = \lfloor L(A) \rfloor$ nằm giữa $\lfloor L(\frac{p_k}{q_k}) \rfloor$ và $\lfloor L(\frac{p_{k-1}}{q_{k-1}}) \rfloor$. Khi chúng bằng nhau, chúng cũng bằng $b_0$.

    Lưu ý rằng $L(A) = (L_{b_0} \circ L_{b_1} \circ \dots \circ L_{b_m})(\infty)$. Biết $b_0$, chúng ta có thể hợp thành $L_{b_0}^{-1}$ với biến đổi hiện tại và tiếp tục thêm $L_{a_{k+1}}$, $L_{a_{k+2}}$ và cứ thế, tìm kiếm các sàn (floors) mới để đồng ý, từ đó chúng ta sẽ có thể suy ra $b_1$ và cứ thế cho đến khi chúng ta khôi phục tất cả các giá trị của $[b_0; b_1, \dots, b_m]$.

!!! example "Số học liên phân số"
    Cho $A=[a_0; a_1, \dots, a_n]$ và $B=[b_0; b_1, \dots, b_m]$. Tính biểu diễn liên phân số của $A+B$ và $A \cdot B$.
??? hint "Lời giải"
    Ý tưởng ở đây tương tự như bài toán trước, nhưng thay vì $L(x) = \frac{ax+b}{cx+d}$ bạn nên xem xét biến đổi phân tuyến tính song tuyến (bilinear) $L(x, y) = \frac{axy+bx+cy+d}{exy+fx+gy+h}$.

    Thay vì $L(x) \mapsto L(L_{a_k}(x))$ bạn sẽ thay đổi biến đổi hiện tại của mình thành $L(x, y) \mapsto L(L_{a_k}(x), y)$ hoặc $L(x, y) \mapsto L(x, L_{b_k}(y))$.

    Sau đó, bạn kiểm tra xem nếu $\lfloor \frac{a}{e} \rfloor = \lfloor \frac{b}{f} \rfloor = \lfloor \frac{c}{g} \rfloor = \lfloor \frac{d}{h} \rfloor$ và nếu tất cả chúng đều đồng ý, bạn sử dụng giá trị này làm $c_k$ trong phân số kết quả và thay đổi biến đổi thành

    $$L(x, y) \mapsto \frac{1}{L(x, y) - c_k}.$$

!!! info "Định nghĩa"
    Một liên phân số $x = [a_0; a_1, \dots]$ được gọi là **tuần hoàn** nếu $x = [a_0; a_1, \dots, a_k, x]$ với một số $k$.

    Một liên phân số $x = [a_0; a_1, \dots]$ được gọi là **tuần hoàn cuối cùng** (eventually periodic) nếu $x = [a_0; a_1, \dots, a_k, y]$, trong đó $y$ là tuần hoàn.

Đối với $x = [1; 1, 1, \dots]$ ta có $x = 1 + \frac{1}{x}$, do đó $x^2 = x + 1$. Có một mối liên hệ chung giữa các liên phân số tuần hoàn và phương trình bậc hai. Xem xét phương trình sau:

$$ x = [a_0; a_1, \dots, a_k, x].$$

Một mặt, phương trình này có nghĩa là biểu diễn liên phân số của $x$ là tuần hoàn với chu kỳ $k+1$.

Mặt khác, sử dụng công thức cho các giản phân, phương trình này có nghĩa là

$$x = \frac{p_k x + p_{k-1}}{q_k x + q_{k-1}}.$$

Nghĩa là, $x$ là một biến đổi phân tuyến tính của chính nó. Từ phương trình suy ra rằng $x$ là nghiệm của phương trình bậc hai:

$$q_k x^2 + (q_{k-1}-p_k)x - p_{k-1} = 0.$$

Lý luận tương tự cũng đúng cho các liên phân số tuần hoàn cuối cùng, nghĩa là $x = [a_0; a_1, \dots, a_k, y]$ đối với $y=[b_0; b_1, \dots, b_k, y]$. Thật vậy, từ phương trình đầu tiên ta suy ra rằng $x = L_0(y)$ và từ phương trình thứ hai là $y = L_1(y)$, trong đó $L_0$ và $L_1$ là các biến đổi phân tuyến tính. Do đó,

$$x = (L_0 \circ L_1)(y) = (L_0 \circ L_1 \circ L_0^{-1})(x).$$

Người ta có thể chứng minh thêm (và điều đó lần đầu tiên được thực hiện bởi Lagrange) rằng đối với bất kỳ phương trình bậc hai $ax^2+bx+c=0$ nào với các hệ số nguyên, nghiệm $x$ của nó là một liên phân số tuần hoàn cuối cùng.

!!! example "Số vô tỷ bậc hai"
    Tìm liên phân số của $\alpha = \frac{x+y\sqrt{n}}{z}$ trong đó $x, y, z, n \in \mathbb Z$ và $n > 0$ không phải là một số chính phương.
??? hint "Lời giải"
    Đối với thương đầy đủ thứ $k$ là $s_k$ của số đó, điều chung sau đây đúng

    $$\alpha = [a_0; a_1, \dots, a_{k-1}, s_k] = \frac{s_k p_{k-1} + p_{k-2}}{s_k q_{k-1} + q_{k-2}}.$$

    Do đó, 

    $$s_k = -\frac{\alpha q_{k-1} - p_{k-1}}{\alpha q_k - p_k} = -\frac{q_{k-1} y \sqrt n + (x q_{k-1} - z p_{k-1})}{q_k y \sqrt n + (xq_k-zp_k)}.$$

    Nhân tử số và mẫu số với $(xq_k - zp_k) - q_k y \sqrt n$, chúng ta sẽ loại bỏ $\sqrt n$ ở mẫu số, do đó các thương đầy đủ có dạng

    $$s_k = \frac{x_k + y_k \sqrt n}{z_k}.$$

    Hãy tìm $s_{k+1}$, giả sử rằng $s_k$ đã biết.

    Đầu tiên, $a_k = \lfloor s_k \rfloor = \left\lfloor \frac{x_k + y_k \lfloor \sqrt n \rfloor}{z_k} \right\rfloor$. Sau đó,

    $$s_{k+1} = \frac{1}{s_k-a_k} = \frac{z_k}{(x_k - z_k a_k) + y_k \sqrt n} = \frac{z_k (x_k - y_k a_k) - y_k z_k \sqrt n}{(x_k - y_k a_k)^2 - y_k^2 n}.$$

    Do đó, nếu chúng ta ký hiệu $t_k = x_k - y_k a_k$, điều sau sẽ đúng

    \begin{align}x_{k+1} &=& z_k t_k, \\ y_{k+1} &=& -y_k z_k, \\ z_{k+1} &=& t_k^2 - y_k^2 n.\end{align}

    Điều tuyệt vời về biểu diễn như vậy là nếu chúng ta rút gọn $x_{k+1}, y_{k+1}, z_{k+1}$ bằng ước chung lớn nhất của chúng, kết quả sẽ là duy nhất. Do đó, chúng ta có thể sử dụng nó để kiểm tra xem trạng thái hiện tại đã được lặp lại chưa và cũng để kiểm tra chỉ số trước đó có trạng thái này ở đâu.

    Dưới đây là mã để tính toán biểu diễn liên phân số cho $\alpha = \sqrt n$:

    === "Python"
        ```py
        # compute the continued fraction of sqrt(n)
        def sqrt(n):
            n0 = math.floor(math.sqrt(n))
            x, y, z = 1, 0, 1
            a = []
            def step(x, y, z):
                a.append((x * n0 + y) // z)
                t = y - a[-1]*z
                x, y, z = -z*x, z*t, t**2 - n*x**2
                g = math.gcd(x, math.gcd(y, z))
                return x // g, y // g, z // g

            used = dict()
            for i in range(n):
                used[x, y, z] = i
                x, y, z = step(x, y, z)
                if (x, y, z) in used:
                    return a
        ```

    Sử dụng cùng hàm `step` nhưng khác $x$, $y$ và $z$ ban đầu, có thể tính toán nó cho $\frac{x+y \sqrt{n}}{z}$ bất kỳ.

!!! example "[Tavrida NU Akai Contest - Continued Fraction](https://timus.online/problem.aspx?space=1&num=1814)"
    Bạn được cho $x$ và $k$, $x$ không phải là số chính phương. Gọi $\sqrt x = [a_0; a_1, \dots]$, tìm $\frac{p_k}{q_k}=[a_0; a_1, \dots, a_k]$ với $0 \leq k \leq 10^9$.
??? hint "Lời giải"
    Sau khi tính chu kỳ của $\sqrt x$, có thể tính $a_k$ bằng lũy thừa nhị phân trên biến đổi phân tuyến tính được tạo ra bởi biểu diễn liên phân số. Để tìm biến đổi kết quả, bạn nén chu kỳ có kích thước $T$ thành một biến đổi duy nhất và lặp lại nó $\lfloor \frac{k-1}{T}\rfloor$ lần, sau đó bạn kết hợp nó thủ công với các biến đổi còn lại.

    === "Python"
        ```py
        x, k = map(int, input().split())

        mod = 10**9+7
        
        # compose (A[0]*x + A[1]) / (A[2]*x + A[3]) and (B[0]*x + B[1]) / (B[2]*x + B[3])
        def combine(A, B):
            return [t % mod for t in [A[0]*B[0]+A[1]*B[2], A[0]*B[1]+A[1]*B[3], A[2]*B[0]+A[3]*B[2], A[2]*B[1]+A[3]*B[3]]]

        A = [1, 0, 0, 1] # (x + 0) / (0*x + 1) = x

        a = sqrt(x)

        T = len(a) - 1 # period of a

        # apply ak + 1/x = (ak*x+1)/(1x+0) to (Ax + B) / (Cx + D)
        for i in reversed(range(1, len(a))):
            A = combine([a[i], 1, 1, 0], A)

        def bpow(A, n):
            return [1, 0, 0, 1] if not n else combine(A, bpow(A, n-1)) if n % 2 else bpow(combine(A, A), n // 2)


        C = (0, 1, 0, 0) # = 1 / 0
        while k % T:
            i = k % T
            C = combine([a[i], 1, 1, 0], C)
            k -= 1

        C = combine(bpow(A, k // T), C)
        C = combine([a[0], 1, 1, 0], C)
        print(str(C[1]) + '/' + str(C[3]))
        ```

## Ý nghĩa hình học (Geometric interpretation) {: #geometric-interpretation}

Gọi $\vec r_k = (q_k;p_k)$ đối với giản phân $r_k = \frac{p_k}{q_k}$. Khi đó, công thức truy hồi sau được áp dụng:

$$\vec r_k = a_k \vec r_{k-1} + \vec r_{k-2}.$$

Gọi $\vec r = (1;r)$. Khi đó, mỗi vectơ $(x;y)$ tương ứng với số bằng hệ số góc của nó $\frac{y}{x}$.

Với khái niệm [tích giả vô hướng](../geometry/basic-geometry.md) (pseudoscalar product) $(x_1;y_1) \times (x_2;y_2) = x_1 y_2 - x_2 y_1$, có thể chứng minh (xem giải thích bên dưới) rằng

$$s_k = -\frac{\vec r_{k-2} \times \vec r}{\vec r_{k-1} \times \vec r} = \left|\frac{\vec r_{k-2} \times \vec r}{\vec r_{k-1} \times \vec r}\right|.$$

Phương trình cuối cùng là do thực tế rằng $r_{k-1}$ và $r_{k-2}$ nằm ở các phía khác nhau của $r$, do đó các tích giả vô hướng của $\vec r_{k-1}$ và $\vec r_{k-2}$ với $\vec r$ có dấu phân biệt. Với $a_k = \lfloor s_k \rfloor$ trong tâm trí, công thức cho $\vec r_k$ bây giờ trông như

$$\vec r_k = \vec r_{k-2} + \left\lfloor \left| \frac{\vec r \times \vec r_{k-2}}{\vec r \times \vec r_{k-1}}\right|\right\rfloor \vec r_{k-1}.$$

Lưu ý rằng $\vec r_k \times r = (q;p) \times (1;r) = qr - p$, do đó

$$a_k = \left\lfloor \left| \frac{q_{k-1}r-p_{k-1}}{q_{k-2}r-p_{k-2}} \right| \right\rfloor.$$

??? hint "Giải thích"
    Như chúng ta đã lưu ý, $a_k = \lfloor s_k \rfloor$, trong đó $s_k = [a_k; a_{k+1}, a_{k+2}, \dots]$. Mặt khác, từ truy hồi giản phân chúng ta suy ra rằng

    $$r = [a_0; a_1, \dots, a_{k-1}, s_k] = \frac{s_k p_{k-1} + p_{k-2}}{s_k q_{k-1} + q_{k-2}}.$$

    Ở dạng vectơ, nó viết lại thành

    $$\vec r \parallel s_k \vec r_{k-1} + \vec r_{k-2},$$

    có nghĩa là $\vec r$ và $s_k \vec r_{k-1} + \vec r_{k-2}$ cùng phương (tức là, có cùng hệ số góc). Lấy [tích giả vô hướng](../geometry/basic-geometry.md) của cả hai phần với $\vec r$, chúng ta nhận được

    $$0 = s_k (\vec r_{k-1} \times \vec r) + (\vec r_{k-2} \times \vec r),$$

    mang lại công thức cuối cùng

    $$s_k = -\frac{\vec r_{k-2} \times \vec r}{\vec r_{k-1} \times \vec r}.$$

!!! example "Thuật toán kéo mũi (Nose stretching algorithm)"
    Mỗi lần bạn thêm $\vec r_{k-1}$ vào vectơ $\vec p$, giá trị của $\vec p \times \vec r$ tăng thêm $\vec r_{k-1} \times \vec r$.

    Do đó, $a_k=\lfloor s_k \rfloor$ là số nguyên tối đa các vectơ $\vec r_{k-1}$ có thể được thêm vào $\vec r_{k-2}$ mà không thay đổi dấu của tích chéo với $\vec r$.

    Nói cách khác, $a_k$ là số lần nguyên tối đa bạn có thể thêm $\vec r_{k-1}$ vào $\vec r_{k-2}$ mà không cắt qua đường thẳng được xác định bởi $\vec r$:

    <figure><img src="https://upload.wikimedia.org/wikipedia/commons/9/92/Continued_convergents_geometry.svg" width="700px"/>
    <figcaption>_Các giản phân của $r=\frac{7}{9}=[0;1,3,2]$. Các bán giản phân tương ứng với các điểm trung gian giữa các mũi tên màu xám._</figcaption></figure>

    Trong hình trên, $\vec r_2 = (4;3)$ thu được bằng cách lặp lại việc thêm $\vec r_1 = (1;1)$ vào $\vec r_0 = (1;0)$.

    Khi không thể thêm $\vec r_1$ vào $\vec r_0$ nữa mà không cắt qua đường thẳng $y=rx$, chúng ta đi sang phía bên kia và lặp lại việc thêm $\vec r_2$ vào $\vec r_1$ để thu được $\vec r_3 = (9;7)$.

    Quy trình này tạo ra các vectơ dài hơn theo cấp số nhân, tiếp cận đường thẳng.

    Vì tính chất này, quy trình tạo ra các vectơ giản phân tiếp theo được Boris Delaunay đặt tên là **thuật toán kéo mũi** (nose stretching algorithm).

Nếu chúng ta nhìn vào tam giác được vẽ trên các điểm $\vec r_{k-2}$, $\vec r_{k}$ và $\vec 0$ chúng ta sẽ nhận thấy rằng diện tích gấp đôi của nó là

$$|\vec r_{k-2} \times \vec r_k| = |\vec r_{k-2} \times (\vec r_{k-2} + a_k \vec r_{k-1})| = a_k |\vec r_{k-2} \times \vec r_{k-1}| = a_k.$$

Kết hợp với [Định lý Pick](../geometry/picks-theorem.md), điều đó có nghĩa là không có điểm lưới nào nằm hoàn toàn bên trong tam giác và các điểm lưới duy nhất trên biên của nó là $\vec 0$ và $\vec r_{k-2} + t \cdot \vec r_{k-1}$ cho tất cả số nguyên $t$ sao cho $0 \leq t \leq a_k$. Khi được nối lại cho tất cả các $k$ có thể, điều đó có nghĩa là không có điểm nguyên nào trong không gian giữa các đa giác được tạo bởi các vectơ giản phân có chỉ số chẵn và lẻ.
