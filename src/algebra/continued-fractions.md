---
tags:
  - Original
---

<!--?title Continued fractions -->
# Liên phân số

**Liên phân số** là một biểu diễn của một số thực dưới dạng một dãy hội tụ cụ thể của các số hữu tỉ. Chúng hữu ích trong lập trình thi đấu vì chúng dễ tính toán và có thể được sử dụng hiệu quả để tìm xấp xỉ hữu tỉ tốt nhất có thể của số thực cơ bản (trong số tất cả các số có mẫu số không vượt quá một giá trị đã cho).

Bên cạnh đó, liên phân số có liên quan chặt chẽ đến thuật toán Euclid, điều này làm cho chúng hữu ích trong một loạt các bài toán lý thuyết số.

## Biểu diễn liên phân số

!!! info "Định nghĩa"
    Cho $a_0, a_1, \dots, a_k \in \mathbb Z$ và $a_1, a_2, \dots, a_k \geq 1$. Khi đó biểu thức

    $$r=a_0 + \frac{1}{a_1 + \frac{1}{\dots + \frac{1}{a_k}}},$$

    được gọi là **biểu diễn liên phân số** của số hữu tỉ $r$ và được ký hiệu ngắn gọn là $r=[a_0;a_1,a_2,\dots,a_k]$.

??? example
    Cho $r = \frac{5}{3}$. Có hai cách để biểu diễn nó dưới dạng một liên phân số:

    $$
    \begin{align}
    r = [1;1,1,1] &= 1+\frac{1}{1+\frac{1}{1+\frac{1}{1}}},\n    r = [1;1,2] &= 1+\frac{1}{1+\frac{1}{2}}.
    \end{align}
    $$

Có thể chứng minh rằng bất kỳ số hữu tỉ nào cũng có thể được biểu diễn dưới dạng liên phân số theo đúng $2$ cách:

$$r = [a_0;a_1,\dots,a_k,1] = [a_0;a_1,\dots,a_k+1].$$ 

Hơn nữa, độ dài $k$ của liên phân số như vậy được ước tính là $k = O(\log \min(p, q))$ đối với $r=\frac{p}{q}$.

Lý do đằng sau điều này sẽ trở nên rõ ràng khi chúng ta đi sâu vào chi tiết của việc xây dựng liên phân số.

!!! info "Định nghĩa"
    Cho $a_0,a_1,a_2, \dots$ là một dãy số nguyên sao cho $a_1, a_2, \dots \geq 1$. Đặt $r_k = [a_0; a_1, \dots, a_k]$. Khi đó biểu thức

    $$r = a_0 + \frac{1}{a_1 + \frac{1}{a_2+\dots}} = \lim\limits_{k \to \infty} r_k.$$

    được gọi là **biểu diễn liên phân số** của số vô tỉ $r$ và được ký hiệu ngắn gọn là $r = [a_0;a_1,a_2,\dots]$.

Lưu ý rằng đối với $r=[a_0;a_1,\dots]$ và số nguyên $k$, ta có $r+k = [a_0+k; a_1, \dots]$.

Một quan sát quan trọng khác là $\frac{1}{r}=[0;a_0, a_1, \dots]$ khi $a_0 > 0$ và $\frac{1}{r} = [a_1; a_2, \dots]$ khi $a_0 = 0$.

!!! info "Định nghĩa"
    Trong định nghĩa trên, các số hữu tỉ $r_0, r_1, r_2, \dots$ được gọi là các **giản phân** của $r$.

    Tương ứng, từng $r_k = [a_0; a_1, \dots, a_k] = \frac{p_k}{q_k}$ được gọi là **giản phân** thứ $k$ của $r$.

??? example
    Xét $r = [1; 1, 1, 1, \dots]$. Có thể chứng minh bằng quy nạp rằng $r_k = \frac{F_{k+2}}{F_{k+1}}$, trong đó $F_k$ là dãy Fibonacci được định nghĩa là $F_0 = 0$, $F_1 = 1$ và $F_{k} = F_{k-1} + F_{k-2}$. Từ công thức Binet, ta biết rằng

    $$r_k = \frac{\phi^{k+2} - \psi^{k+2}}{\phi^{k+1} - \psi^{k+1}},$$

    trong đó $\phi = \frac{1+\sqrt{5}}{2} \approx 1.618$ là tỷ lệ vàng và $\psi = \frac{1-\sqrt{5}}{2} = -\frac{1}{\phi} \approx -0.618$. Do đó,

    $$r = 1+\frac{1}{1+\frac{1}{1+\dots}}=\lim\limits_{k \to \infty} r_k = \phi = \frac{1+\sqrt{5}}{2}.$$ 

    Lưu ý rằng trong trường hợp cụ thể này, một cách khác để tìm $r$ là giải phương trình

    $$r = 1+\frac{1}{r} \implies r^2 = r + 1. $$


!!! info "Định nghĩa"
    Cho $r_k = [a_0; a_1, \dots, a_{k-1}, a_k]$. Các số $[a_0; a_1, \dots, a_{k-1}, t]$ với $1 \leq t \leq a_k$ được gọi là **bán giản phân**.

    Chúng ta thường gọi các (bán) giản phân lớn hơn $r$ là các (bán) giản phân **trên** và những giản phân nhỏ hơn $r$ là các (bán) giản phân **dưới**.

!!! info "Định nghĩa"
    Bổ sung cho các giản phân, chúng ta định nghĩa các **[thương đầy đủ](https://en.wikipedia.org/wiki/Complete_quotient)** là $s_k = [a_k; a_{k+1}, a_{k+2}, \dots]$.

    Tương ứng, chúng ta sẽ gọi một $s_k$ riêng lẻ là thương đầy đủ thứ $k$ của $r$.

Từ các định nghĩa trên, có thể kết luận rằng $s_k \geq 1$ với $k \geq 1$.

Xem $[a_0; a_1, \dots, a_k]$ như một biểu thức đại số hình thức và cho phép các số thực tùy ý thay vì $a_i$, chúng ta có được

$$r = [a_0; a_1, \dots, a_{k-1}, s_k].$$

Đặc biệt, $r = [s_0] = s_0$. Mặt khác, chúng ta có thể biểu diễn $s_k$ dưới dạng

$$s_k = [a_k; s_{k+1}] = a_k + \frac{1}{s_{k+1}},$$

nghĩa là chúng ta có thể tính $a_k = \lfloor s_k \rfloor$ và $s_{k+1} = (s_k - a_k)^{-1}$ từ $s_k$.

Dãy $a_0, a_1, \dots$ được xác định rõ ràng trừ khi $s_k=a_k$, điều này chỉ xảy ra khi $r$ là một số hữu tỉ.

Do đó, biểu diễn liên phân số được xác định duy nhất cho bất kỳ số vô tỉ $r$ nào.

### Cài đặt

Trong các đoạn mã, chúng ta sẽ chủ yếu giả định các liên phân số hữu hạn.

Từ $s_k$, việc chuyển sang $s_{k+1}$ trông giống như

$$s_k =\left\lfloor s_k \right\rfloor + \frac{1}{s_{k+1}}.$$

Từ biểu thức này, thương đầy đủ tiếp theo $s_{k+1}$ được nhận là

$$s_{k+1} = \left(s_k-\left\lfloor s_k\right\rfloor\right)^{-1}.$$ 

Đối với $s_k=\frac{p}{q}$ điều đó có nghĩa là

$$
 s_{k+1} = \left(\frac{p}{q}-\left\lfloor \frac{p}{q} \right\rfloor\right)^{-1} = \frac{q}{p-q\cdot \lfloor \frac{p}{q} \rfloor} = \frac{q}{p \bmod q}. 
$$

Do đó, việc tính toán biểu diễn liên phân số cho $r=\frac{p}{q}$ tuân theo các bước của thuật toán Euclid cho $p$ và $q$.

Từ đó cũng suy ra rằng $\gcd(p_k, q_k) = 1$ đối với $\frac{p_k}{q_k} = [a_0; a_1, \dots, a_k]$. Do đó, các giản phân luôn là phân số tối giản.

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

## Các kết quả chính

Để cung cấp một số động lực cho việc nghiên cứu sâu hơn về liên phân số, chúng tôi đưa ra một số sự thật quan trọng ngay bây giờ.

??? note "Truy hồi"
    Đối với các giản phân $r_k = \frac{p_k}{q_k}$, hệ thức truy hồi sau đây đúng, cho phép tính toán nhanh chóng chúng:
    
    $$\frac{p_k}{q_k}=\frac{a_k p_{k-1} + p_{k-2}}{a_k q_{k-1} + q_{k-2}},$$ 
    
    trong đó $\frac{p_{-1}}{q_{-1}}=\frac{1}{0}$ và $\frac{p_{-2}}{q_{-2}}=\frac{0}{1}$.

??? note "Độ lệch"
    Độ lệch của $r_k = \frac{p_k}{q_k}$ so với $r$ có thể được ước tính chung là
    
    $$\left|\frac{p_k}{q_k}-r\right| \leq \frac{1}{q_k q_{k+1}} \leq \frac{1}{q_k^2}.$$ 
    
    Nhân cả hai vế với $q_k$, chúng ta có được ước tính thay thế:
    
    $$|p_k - q_k r| \leq \frac{1}{q_{k+1}}.$$ 

    Từ hệ thức truy hồi ở trên, suy ra rằng $q_k$ tăng ít nhất nhanh bằng các số Fibonacci.

    Trên hình ảnh dưới đây, bạn có thể thấy hình dung về cách các giản phân $r_k$ tiến gần đến $r=\frac{1+\sqrt 5}{2}$:

    ![](https://upload.wikimedia.org/wikipedia/commons/b/b4/Golden_ration_convergents.svg)

    $r=\frac{1+\sqrt 5}{2}$ được mô tả bằng đường chấm màu xanh. Các giản phân lẻ tiến đến nó từ trên và các giản phân chẵn tiến đến nó từ dưới.

??? note "Bao lồi lưới"
    Xét bao lồi của các điểm phía trên và phía dưới đường thẳng $y=rx$.
    
    Các giản phân lẻ $(q_k;p_k)$ là các đỉnh của bao lồi trên, trong khi các giản phân chẵn $(q_k;p_k)$ là các đỉnh của bao lồi dưới.
    
    Tất cả các đỉnh nguyên trên các bao lồi được nhận dưới dạng $(q;p)$ sao cho
    
    $$\frac{p}{q} = \frac{tp_{k-1} + p_{k-2}}{tq_{k-1} + q_{k-2}}$$ 
    
    với số nguyên $0 \leq t \leq a_k$. Nói cách khác, tập hợp các điểm lưới trên các bao lồi tương ứng với tập hợp các bán giản phân.

    Trên hình ảnh dưới đây, bạn có thể thấy các giản phân và bán giản phân (các điểm màu xám trung gian) của $r=\frac{9}{7}$.

    ![](https://upload.wikimedia.org/wikipedia/commons/9/92/Continued_convergents_geometry.svg)

??? note "Xấp xỉ tốt nhất"
    Đặt $\frac{p}{q}$ là phân số để tối thiểu hóa $\left|r-\frac{p}{q}\right|$ với điều kiện $q \leq x$ đối với một số $x$.
    
    Khi đó $\frac{p}{q}$ là một bán giản phân của $r$.

Sự thật cuối cùng cho phép tìm các xấp xỉ hữu tỉ tốt nhất của $r$ bằng cách kiểm tra các bán giản phân của nó.

Dưới đây bạn sẽ tìm thấy lời giải thích thêm và một chút trực giác và giải thích cho những sự thật này.

## Giản phân

Hãy xem xét kỹ hơn các giản phân đã được định nghĩa trước đó. Đối với $r=[a_0, a_1, a_2, \dots]$, các giản phân của nó là

\begin{gather}
 r_0=[a_0],\n r_1=[a_0, a_1],\n \dots,\n r_k=[a_0, a_1, \dots, a_k].
\end{gather}

Giản phân là khái niệm cốt lõi của liên phân số, vì vậy việc nghiên cứu các thuộc tính của chúng là rất quan trọng.

Đối với số $r$, giản phân thứ $k$ của nó là $r_k = \frac{p_k}{q_k}$ có thể được tính là

$$r_k = \frac{P_k(a_0,a_1,\dots,a_k)}{P_{k-1}(a_1,\dots,a_k)} = \frac{a_k p_{k-1} + p_{k-2}}{a_k q_{k-1} + q_{k-2}},$$ 

trong đó $P_k(a_0,\dots,a_k)$ là [the continuant](https://en.wikipedia.org/wiki/Continuant_(mathematics)), một đa thức đa biến được định nghĩa là

$$P_k(x_0,x_1,\dots,x_k) = \det \begin{bmatrix}
x_k & 1 & 0 & \dots & 0 \\
-1 & x_{k-1} & 1 & \dots & 0 \\
0 & -1 & x_2 & . & \vdots \\
\vdots & \vdots & . & \ddots & 1 \\
0 & 0 & \dots & -1 & x_0
\end{bmatrix}_{\textstyle .}$$

Do đó, $r_k$ là một [trung bình có trọng số](https://en.wikipedia.org/wiki/Mediant_(mathematics)) của $r_{k-1}$ và $r_{k-2}$.

Để nhất quán, hai giản phân bổ sung $r_{-1} = \frac{1}{0}$ và $r_{-2} = \frac{0}{1}$ được định nghĩa.

??? hint "Giải thích chi tiết"

    Tử số và mẫu số của $r_k$ có thể được xem như các đa thức đa biến của $a_0, a_1, \dots, a_k$:

    $$r_k = \frac{P_k(a_0, a_1, \dots, a_k)}{Q_k(a_0,a_1, \dots, a_k)}.$$

    Từ định nghĩa của các giản phân,

    $$r_k = a_0 + \frac{1}{[a_1;a_2,\dots, a_k]}= a_0 + \frac{Q_{k-1}(a_1, \dots, a_k)}{P_{k-1}(a_1, \dots, a_k)} = \frac{a_0 P_{k-1}(a_1, \dots, a_k) + Q_{k-1}(a_1, \dots, a_k)}{P_{k-1}(a_1, \dots, a_k)}.$$

    Từ đó suy ra $Q_k(a_0, \dots, a_k) = P_{k-1}(a_1, \dots, a_k)$. Điều này mang lại mối quan hệ

    $$P_k(a_0, \dots, a_k) = a_0 P_{k-1}(a_1, \dots, a_k) + P_{k-2}(a_2, \dots, a_k).$$

    Ban đầu, $r_0 = \frac{a_0}{1}$ và $r_1 = \frac{a_0 a_1 + 1}{a_1}$, do đó

    $$\begin{align}P_0(a_0)&=a_0,\ P_1(a_0, a_1) &= a_0 a_1 + 1.\end{align}$$ 

    Để nhất quán, thuận tiện để định nghĩa $P_{-1} = 1$ và $P_{-2}=0$ và chính thức nói rằng $r_{-1} = \frac{1}{0}$ và $r_{-2}=\frac{0}{1}$.

    Từ phân tích số, ta biết rằng định thức của một ma trận ba đường chéo tùy ý

    $$T_k = \det \begin{bmatrix}
     a_0 & b_0 & 0 & \dots & 0 \\
     c_0 & a_1 & b_1 & \dots & 0 \\
     0 & c_1 & a_2 & . & \vdots \\
     \vdots & \vdots & . & \ddots & c_{k-1} \\
     0 & 0 & \dots & b_{k-1} & a_k
    \end{bmatrix}$$

    có thể được tính đệ quy là $T_k = a_k T_{k-1} - b_{k-1} c_{k-1} T_{k-2}$. So sánh nó với $P_k$, chúng ta có được một biểu thức trực tiếp

    $$P_k = \det \begin{bmatrix}
    x_k & 1 & 0 & \dots & 0 \\
    -1 & x_{k-1} & 1 & \dots & 0 \\
    0 & -1 & x_2 & . & \vdots \\
    \vdots & \vdots & . & \ddots & 1 \\
    0 & 0 & \dots & -1 & x_0
    \end{bmatrix}_{\textstyle .}$$

    Đa thức này còn được gọi là [the continuant](https://en.wikipedia.org/wiki/Continuant_(mathematics)) do mối quan hệ chặt chẽ của nó với liên phân số. continuant sẽ không thay đổi nếu dãy trên đường chéo chính bị đảo ngược. Điều này mang lại một công thức thay thế để tính toán nó:

    $$P_k(a_0, \dots, a_k) = a_k P_{k-1}(a_0, \dots, a_{k-1}) + P_{k-2}(a_0, \dots, a_{k-2}).$$

### Cài đặt

Chúng ta sẽ tính toán các giản phân dưới dạng một cặp dãy $p_{-2}, p_{-1}, p_0, p_1, \dots, p_k$ và $q_{-2}, q_{-1}, q_0, q_1, \dots, q_k$:

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

## Cây liên phân số

Có hai cách chính để hợp nhất tất cả các liên phân số có thể thành các cấu trúc cây hữu ích.

### Cây Stern-Brocot

[Cây Stern-Brocot](../others/stern_brocot_tree_farey_sequences.md) là một cây tìm kiếm nhị phân chứa tất cả các số hữu tỉ dương phân biệt.

Cây thường trông như sau:

<figure>
<img src="https://upload.wikimedia.org/wikipedia/commons/3/37/SternBrocotTree.svg">
<figcaption>
<a href="https://commons.wikimedia.org/wiki/File:SternBrocotTree.svg">Hình ảnh</a> bởi <a href="https://commons.wikimedia.org/wiki/User:Aaron_Rotenberg">Aaron Rotenberg</a> được cấp phép theo <a href="https://creativecommons.org/licenses/by-sa/3.0/deed.en">CC BY-SA 3.0</a>
</figcaption>
</figure>

Các phân số $\frac{0}{1}$ và $\frac{1}{0}$ được giữ "ảo" ở hai bên trái và phải của cây tương ứng.

Khi đó, phân số trong một nút là trung bình $\frac{a+c}{b+d}$ của hai phân số $\frac{a}{b}$ và $\frac{c}{d}$ phía trên nó.

Hệ thức truy hồi $\frac{p_k}{q_k}=\frac{a_k p_{k-1} + p_{k-2}}{a_k q_{k-1} + q_{k-2}}$ có nghĩa là biểu diễn liên phân số mã hóa đường dẫn đến $\frac{p_k}{q_k}$ trong cây. Để tìm $[a_0; a_1, \dots, a_{k}, 1]$, người ta phải thực hiện $a_0$ lần di chuyển sang phải, $a_1$ lần di chuyển sang trái, $a_2$ lần di chuyển sang phải và cứ thế cho đến $a_k$.

Nút cha của $[a_0; a_1, \dots, a_k,1]$ sau đó là phân số thu được bằng cách lùi một bước theo hướng cuối cùng được sử dụng.

Nói cách khác, đó là $[a_0; a_1, \dots, a_k-1,1]$ khi $a_k > 1$ và $[a_0; a_1, \dots, a_{k-1}, 1]$ khi $a_k = 1$.

Do đó, các con của $[a_0; a_1, \dots, a_k, 1]$ là $[a_0; a_1, \dots, a_k+1, 1]$ và $[a_0; a_1, \dots, a_k, 1, 1]$.

Hãy đánh chỉ số cây Stern-Brocot. Đỉnh gốc được gán chỉ số $1$. Sau đó, đối với một đỉnh $v$, chỉ số của con trái của nó được gán bằng cách thay đổi bit đầu của $v$ từ $1$ thành $10$ và đối với con phải, nó được gán bằng cách thay đổi bit đầu từ $1$ thành $11$:

<figure><img src="https://upload.wikimedia.org/wikipedia/commons/1/18/Stern-brocot-index.svg" width="500px"/></figure>

Trong cách đánh chỉ số này, biểu diễn liên phân số của một số hữu tỉ chỉ định [mã hóa độ dài chạy](https://en.wikipedia.org/wiki/Run-length_encoding) của chỉ số nhị phân của nó.

Đối với $\frac{5}{2} = [2;2] = [2;1,1]$, chỉ số của nó là $1011_2$ và mã hóa độ dài chạy của nó, xét các bit theo thứ tự tăng dần, là $[2;1,1]$.

Một ví dụ khác là $\frac{2}{5} = [0;2,2]=[0;2,1,1]$, có chỉ số $1100_2$ và mã hóa độ dài chạy của nó, thực sự, là $[0;2,2]$.

Đáng chú ý là cây Stern-Brocot, trên thực tế, là một [treap](../data_structures/treap.md). Tức là, nó là một cây tìm kiếm nhị phân theo $\frac{p}{q}$, nhưng nó là một heap theo cả $p$ và $q$.

!!! example "So sánh các liên phân số"
    Bạn được cho $A=[a_0; a_1, \dots, a_n]$ và $B=[b_0; b_1, \dots, b_m]$. Phân số nào nhỏ hơn?
??? hint "Lời giải"
    Giả sử bây giờ $A$ và $B$ là vô tỉ và biểu diễn liên phân số của chúng biểu thị một sự đi xuống vô hạn trong cây Stern-Brocot.

    Như chúng ta đã đề cập, trong biểu diễn này, $a_0$ biểu thị số lần rẽ phải trong quá trình đi xuống, $a_1$ biểu thị số lần rẽ trái liên tiếp và cứ thế. Do đó, khi chúng ta so sánh $a_k$ và $b_k$, nếu $a_k = b_k$ chúng ta chỉ cần chuyển sang so sánh $a_{k+1}$ và $b_{k+1}$. Ngược lại, nếu chúng ta đang ở các đoạn đi xuống bên phải, chúng ta nên kiểm tra xem $a_k < b_k$ và nếu chúng ta đang ở các đoạn đi xuống bên trái, chúng ta nên kiểm tra xem $a_k > b_k$ để biết liệu $A < B$.

    Nói cách khác, đối với $A$ và $B$ vô tỉ, $A < B$ khi và chỉ khi $(a_0, -a_1, a_2, -a_3, \dots) < (b_0, -b_1, b_2, -b_3, \dots)$ với so sánh từ điển.

    Bây giờ, chính thức sử dụng $\infty$ như một phần tử của biểu diễn liên phân số, có thể mô phỏng các số vô tỉ $A-\varepsilon$ và $A+\varepsilon$, tức là các phần tử nhỏ hơn (lớn hơn) $A$, nhưng lớn hơn (nhỏ hơn) bất kỳ số thực nào khác. Cụ thể, đối với $A=[a_0; a_1, \dots, a_n]$, một trong hai phần tử này có thể được mô phỏng là $[a_0; a_1, \dots, a_n, \infty]$ và phần tử kia có thể được mô phỏng là $[a_0; a_1, \dots, a_n - 1, 1, \infty]$.

    Cái nào tương ứng với $A-\varepsilon$ và cái nào tương ứng với $A+\varepsilon$ có thể được xác định bằng tính chẵn lẻ của $n$ hoặc bằng cách so sánh chúng như các số vô tỉ.

    === "Python"
        ```py
        # kiểm tra xem a < b giả sử rằng a[-1] = b[-1] = infty và a != b
        def less(a, b):
            a = [(-1)**i*a[i] for i in range(len(a))]
            b = [(-1)**i*b[i] for i in range(len(b))]
            return a < b

        # [a0; a1, ..., ak] -> [a0, a1, ..., ak-1, 1]
        def expand(a):
            if a: # a rỗng = inf
                a[-1] -= 1
                a.append(1)
            return a

        # trả về a-eps, a+eps
        def pm_eps(a):
            b = expand(a.copy())
            a.append(float('inf'))
            b.append(float('inf'))
            return (a, b) if less(a, b) else (b, a)
        ```

!!! example "Điểm trong tốt nhất"
    Bạn được cho $\frac{0}{1} \leq \frac{p_0}{q_0} < \frac{p_1}{q_1} \leq \frac{1}{0}$. Tìm số hữu tỉ $\frac{p}{q}$ sao cho $(q; p)$ nhỏ nhất theo thứ tự từ điển và $\frac{p_0}{q_0} < \frac{p}{q} < \frac{p_1}{q_1}$.

??? hint "Lời giải"
    Theo thuật ngữ của cây Stern-Brocot, điều đó có nghĩa là chúng ta cần tìm LCA của $\frac{p_0}{q_0}$ và $\frac{p_1}{q_1}$. Do mối liên hệ giữa cây Stern-Brocot và liên phân số, LCA này sẽ gần đúng tương ứng với tiền tố chung lớn nhất của các biểu diễn liên phân số cho $\frac{p_0}{q_0}$ và $\frac{p_1}{q_1}$.

    Vì vậy, nếu $\frac{p_0}{q_0} = [a_0; a_1, \dots, a_{k-1}, a_k, \dots]$ và $\frac{p_1}{q_1} = [a_0; a_1, \dots, a_{k-1}, b_k, \dots]$ là các số vô tỉ, thì LCA là $[a_0; a_1, \dots, \min(a_k, b_k)+1]$.

    Đối với $r_0$ và $r_1$ hữu tỉ, một trong số chúng có thể là chính LCA, điều này sẽ đòi hỏi chúng ta phải xét trường hợp. Để đơn giản hóa giải pháp cho $r_0$ và $r_1$ hữu tỉ, có thể sử dụng biểu diễn liên phân số của $r_0 + \varepsilon$ và $r_1 - \varepsilon$ đã được rút ra trong bài toán trước.

    === "Python"
        ```py
        # tìm (q, p) nhỏ nhất theo thứ tự từ điển
        # sao cho p0/q0 < p/q < p1/q1
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
    Diễn đạt lại câu lệnh, $A_i x + B_i y$ phải dương với mọi $i$, trong đó $A_i = C_i - C_{i-1}$ và $B_i = J_i - J_{i-1}$.

    Trong số các phương trình như vậy, chúng ta có bốn nhóm quan trọng cho $A_i x + B_i y > 0$:

    1. $A_i, B_i > 0$ có thể bỏ qua vì chúng ta đang tìm $x, y > 0$.
    2. $A_i, B_i \leq 0$ sẽ cho câu trả lời "IMPOSSIBLE".
    3. $A_i > 0$, $B_i \leq 0$. Các ràng buộc như vậy tương đương với $\frac{y}{x} < \frac{A_i}{-B_i}$.
    4. $A_i \leq 0$, $B_i > 0$. Các ràng buộc như vậy tương đương với $\frac{y}{x} > \frac{-A_i}{B_i}$.

    Đặt $\frac{p_0}{q_0}$ là $\frac{-A_i}{B_i}$ lớn nhất từ nhóm thứ tư và $\frac{p_1}{q_1}$ là $\frac{A_i}{-B_i}$ nhỏ nhất từ nhóm thứ ba.

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

### Cây Calkin-Wilf

Một cách hơi đơn giản hơn để tổ chức các liên phân số trong một cây nhị phân là [cây Calkin-Wilf](https://en.wikipedia.org/wiki/Calkin–Wilf_tree).

Cây thường trông như thế này:

<figure>
<img src="https://upload.wikimedia.org/wikipedia/commons/8/82/Calkin–Wilf_tree.svg" width="500px"/>
<figcaption><a href="https://commons.wikimedia.org/wiki/File:Calkin–Wilf_tree.svg">Hình ảnh</a> bởi <a href="https://commons.wikimedia.org/wiki/User:Olli_Niemitalo">Olli Niemitalo</a>, <a href="https://commons.wikimedia.org/wiki/User:Proz">Proz</a> được cấp phép theo <a href="https://creativecommons.org/publicdomain/zero/1.0/deed.en">CC0 1.0</a></figcaption>
</figure>

Ở gốc của cây, số $\frac{1}{1}$ được đặt. Sau đó, đối với đỉnh có số $\frac{p}{q}$, các con của nó là $\frac{p}{p+q}$ và $\frac{p+q}{q}$.

Không giống như cây Stern-Brocot, cây Calkin-Wilf không phải là một cây tìm kiếm nhị phân, vì vậy nó không thể được sử dụng để thực hiện tìm kiếm nhị phân hữu tỉ.

Trong cây Calkin-Wilf, cha trực tiếp của một phân số $\frac{p}{q}$ là $\frac{p-q}{q}$ khi $p>q$ và $\frac{p}{q-p}$ nếu không.

Đối với cây Stern-Brocot, chúng ta đã sử dụng hệ thức truy hồi cho các giản phân. Để vẽ ra mối liên hệ giữa liên phân số và cây Calkin-Wilf, chúng ta nên nhớ lại hệ thức truy hồi cho các thương đầy đủ. Nếu $s_k = \frac{p}{q}$, thì $s_{k+1} = \frac{q}{p \bmod q} = \frac{q}{p-\lfloor p/q \rfloor \cdot q}$.

Mặt khác, nếu chúng ta lặp đi lặp lại đi từ $s_k = \frac{p}{q}$ đến cha của nó trong cây Calkin-Wilf khi $p > q$, chúng ta sẽ kết thúc ở $\frac{p \bmod q}{q} = \frac{1}{s_{k+1}}$. Nếu chúng ta tiếp tục làm như vậy, chúng ta sẽ kết thúc ở $s_{k+2}$, sau đó là $\frac{1}{s_{k+3}}$ và cứ thế. Từ đó chúng ta có thể suy ra rằng:

1. Khi $a_0> 0$, cha trực tiếp của $[a_0; a_1, \dots, a_k]$ trong cây Calkin-Wilf là $\frac{p-q}{q}=[a_0 - 1; a_1, \dots, a_k]$.
2. Khi $a_0 = 0$ và $a_1 > 1$, cha trực tiếp của nó là $\frac{p}{q-p} = [0; a_1 - 1, a_2, \dots, a_k]$.
3. Và khi $a_0 = 0$ và $a_1 = 1$, cha trực tiếp của nó là $\frac{p}{q-p} = [a_2; a_3, \dots, a_k]$.

Tương ứng, các con của $\frac{p}{q} = [a_0; a_1, \dots, a_k]$ là

1. $\frac{p+q}{q}=1+\frac{p}{q}$, là $[a_0+1; a_1, \dots, a_k]$,
2. $\frac{p}{p+q} = \frac{1}{1+\frac{q}{p}}$, là $[0, 1, a_0, a_1, \dots, a_k]$ đối với $a_0 > 0$ và $[0, a_1+1, a_2, \dots, a_k]$ đối với $a_0=0$.

Đáng chú ý, nếu chúng ta đánh số các đỉnh của cây Calkin-Wilf theo thứ tự tìm kiếm theo chiều rộng (tức là, gốc có số $1$, và các con của đỉnh $v$ có chỉ số $2v$ và $2v+1$ tương ứng), chỉ số của số hữu tỉ trong cây Calkin-Wilf sẽ giống như trong cây Stern-Brocot.

Do đó, các số ở cùng một cấp của cây Stern-Brocot và cây Calkin-Wilf là giống nhau, nhưng thứ tự của chúng khác nhau thông qua [hoán vị đảo ngược bit](https://en.wikipedia.org/wiki/Bit-reversal_permutation).
## Sự hội tụ

Đối với số $r$ và giản phân thứ $k$ của nó là $r_k=\frac{p_k}{q_k}$, công thức sau đây đúng:

$$r_k = a_0 + \sum\limits_{i=1}^k \frac{(-1)^{i-1}}{q_i q_{i-1}}.$$

Cụ thể, điều đó có nghĩa là

$$r_k - r_{k-1} = \frac{(-1)^{k-1}}{q_k q_{k-1}}$$

và

$$p_k q_{k-1} - p_{k-1} q_k = (-1)^{k-1}.$$ 

Từ đó chúng ta có thể kết luận rằng

$$\left| r-\frac{p_k}{q_k} \right| \leq \frac{1}{q_{k+1}q_k} \leq \frac{1}{q_k^2}.$$ 

Bất đẳng thức sau là do thực tế là $r_k$ và $r_{k+1}$ thường nằm ở hai phía khác nhau của $r$, do đó

$$|r-r_k| = |r_k-r_{k+1}|-|r-r_{k+1}| \leq |r_k - r_{k+1}|.$$

??? tip "Giải thích chi tiết"

    Để ước tính $|r-r_k|$, chúng ta bắt đầu bằng cách ước tính sự khác biệt giữa các giản phân liền kề. Theo định nghĩa,

    $$\frac{p_k}{q_k} - \frac{p_{k-1}}{q_{k-1}} = \frac{p_k q_{k-1} - p_{k-1} q_k}{q_k q_{k-1}}.$$

    Thay thế $p_k$ và $q_k$ trong tử số bằng các công thức truy hồi của chúng, chúng ta có được

    $$\begin{align} p_k q_{k-1} - p_{k-1} q_k &= (a_k p_{k-1} + p_{k-2}) q_{k-1} - p_{k-1} (a_k q_{k-1} + q_{k-2})
    \&= p_{k-2} q_{k-1} - p_{k-1} q_{k-2},\end{align}$$ 

    do đó tử số của $r_k - r_{k-1}$ luôn là tử số bị phủ định của $r_{k-1} - r_{k-2}$. Nó, đến lượt nó, bằng $1$ đối với

    $$r_1 - r_0=\left(a_0+\frac{1}{a_1}\right)-a_0=\frac{1}{a_1},$$

    do đó

    $$r_k - r_{k-1} = \frac{(-1)^{k-1}}{q_k q_{k-1}}.$$

    Điều này mang lại một biểu diễn thay thế của $r_k$ dưới dạng một tổng riêng của chuỗi vô hạn:

    $$r_k = (r_k - r_{k-1}) + \dots + (r_1 - r_0) + r_0
    = a_0 + \sum\limits_{i=1}^k \frac{(-1)^{i-1}}{q_i q_{i-1}}.$$

    Từ mối quan hệ truy hồi, suy ra rằng $q_k$ tăng đơn điệu ít nhất nhanh bằng các số Fibonacci, do đó

    $$r = \lim\limits_{k \to \infty} r_k = a_0 + \sum\limits_{i=1}^\infty \frac{(-1)^{i-1}}{q_i q_{i-1}}$$

    luôn được xác định rõ ràng, vì chuỗi cơ bản luôn hội tụ. Đáng chú ý, chuỗi dư

    $$r-r_k = \sum\limits_{i=k+1}^\infty \frac{(-1)^{i-1}}{q_i q_{i-1}}$$

    có cùng dấu với $(-1)^k$ do tốc độ giảm của $q_i q_{i-1}$. Do đó, các $r_k$ có chỉ số chẵn tiến đến $r$ từ bên dưới trong khi các $r_k$ có chỉ số lẻ tiến đến nó từ bên trên:

    <figure><img src="https://upload.wikimedia.org/wikipedia/commons/b/b4/Golden_ration_convergents.svg" width="600px"/>
    <figcaption>_Các giản phân của $r=\phi = \frac{1+\sqrt{5}}{2}=[1;1,1,\dots]$ và khoảng cách của chúng đến $r$._</figcaption></figure>

    Từ hình ảnh này, chúng ta có thể thấy rằng

    $$|r-r_k| = |r_k - r_{k+1}| - |r-r_{k+1}| \leq |r_k - r_{k+1}|,$$ 

    do đó khoảng cách giữa $r$ và $r_k$ không bao giờ lớn hơn khoảng cách giữa $r_k$ và $r_{k+1}$:

    $$\left|r-\frac{p_k}{q_k}\right| \leq \frac{1}{q_k q_{k+1}} \leq \frac{1}{q_k^2}.$$ 

!!! example "Euclid mở rộng?"
    Bạn được cho $A, B, C \in \mathbb Z$. Tìm $x, y \in \mathbb Z$ sao cho $Ax + By = C$.
??? hint "Lời giải"
    Mặc dù bài toán này thường được giải quyết bằng [thuật toán Euclid mở rộng](../algebra/extended-euclid-algorithm.md), có một giải pháp đơn giản và trực tiếp bằng liên phân số.

    Cho $\frac{A}{B}=[a_0; a_1, \dots, a_k]$. Đã được chứng minh ở trên rằng $p_k q_{k-1} - p_{k-1} q_k = (-1)^{k-1}$. Thay thế $p_k$ và $q_k$ bằng $A$ và $B$, chúng ta có được

    $$Aq_{k-1} - Bp_{k-1} = (-1)^{k-1} g,$$ 

    trong đó $g = \gcd(A, B)$. Nếu $C$ chia hết cho $g$, thì nghiệm là $x = (-1)^{k-1}\frac{C}{g} q_{k-1}$ và $y = (-1)^{k}\frac{C}{g} p_{k-1}$.
    
    === "Python"
        ```py
        # trả về (x, y) sao cho Ax+By=C
        # giả sử (x, y) như vậy tồn tại
        def dio(A, B, C):
            p, q = convergents(fraction(A, B))
            C //= A // p[-1] # chia cho gcd(A, B)
            t = (-1) if len(p) % 2 else 1
            return t*C*q[-2], -t*C*p[-2]
        ```

## Phép biến đổi phân tuyến tính

Một khái niệm quan trọng khác đối với liên phân số là cái gọi là [phép biến đổi phân tuyến tính](https://en.wikipedia.org/wiki/Linear_fractional_transformation).

!!! info "Định nghĩa"
    Một **phép biến đổi phân tuyến tính** là một hàm $f : \mathbb R \to \mathbb R$ sao cho $f(x) = \frac{ax+b}{cx+d}$ đối với một số $a,b,c,d \in \mathbb R$.

Một phép hợp $(L_0 \circ L_1)(x) = L_0(L_1(x))$ của các phép biến đổi phân tuyến tính $L_0(x)=\frac{a_0 x + b_0}{c_0 x + d_0}$ và $L_1(x)=\frac{a_1 x + b_1}{c_1 x + d_1}$ bản thân nó là một phép biến đổi phân tuyến tính:

$$\frac{a_0\frac{a_1 x + b_1}{c_1 x + d_1} + b_0}{c_0 \frac{a_1 x + b_1}{c_1 x + d_1} + d_0} = \frac{a_0(a_1 x + b_1) + b_0 (c_1 x + d_1)}{c_0 (a_1 x + b_1) + d_0 (c_1 x + d_1)} = \frac{(a_0 a_1 + b_0 c_1) x + (a_0 b_1 + b_0 d_1)}{(c_0 a_1 + d_0 c_1) x + (c_0 b_1 + d_0 d_1)}.$$

Nghịch đảo của một phép biến đổi phân tuyến tính cũng là một phép biến đổi phân tuyến tính:

$$y = \frac{ax+b}{cx+d} \iff y(cx+d) = ax + b \iff x = -\frac{dy-b}{cy-a}.$$ 
!!! example "[DMOPC '19 Contest 7 P4 - Bob and Continued Fractions](https://dmoj.ca/problem/dmopc19c7p4)"
    Bạn được cho một mảng các số nguyên dương $a_1, \dots, a_n$. Bạn cần trả lời $m$ truy vấn. Mỗi truy vấn là để tính $[a_l; a_{l+1}, \dots, a_r]$.
??? hint "Lời giải"
    Chúng ta có thể giải quyết bài toán này bằng cây phân đoạn nếu chúng ta có thể nối các liên phân số.

    Nói chung, đúng là $[a_0; a_1, \dots, a_k, b_0, b_1, \dots, b_k] = [a_0; a_1, \dots, a_k, [b_1; b_2, \dots, b_k]]$.

    Hãy ký hiệu $L_{k}(x) = [a_k; x] = a_k + \frac{1}{x} = \frac{a_k\cdot x+1}{1\cdot x + 0}$. Lưu ý rằng $L_k(\infty) = a_k$. Trong ký hiệu này, nó đúng rằng

    $$[a_0; a_1, \dots, a_k, x] = [a_0; [a_1; [\dots; [a_k; x]]]] = (L_0 \circ L_1 \circ \dots \circ L_k)(x) = \frac{p_k x + p_{k-1}}{q_k x + q_{k-1}}.$$

    Do đó, bài toán thu gọn về việc tính toán

    $$(L_l \circ L_{l+1} \circ \dots \circ L_r)(\infty).$$ 

    Phép hợp của các phép biến đổi là kết hợp, vì vậy có thể tính toán trong mỗi nút của một cây phân đoạn phép hợp của các phép biến đổi trong cây con của nó.

!!! example "Phép biến đổi phân tuyến tính của một liên phân số"
    Cho $L(x) = \frac{ax+b}{cx+d}$. Tính biểu diễn liên phân số $[b_0; b_1, \dots, b_m]$ của $L(A)$ đối với $A=[a_0; a_1, \dots, a_n]$.

    _Điều này cho phép tính $A + \frac{p}{q} = \frac{qA + p}{q}$ và $A \cdot \frac{p}{q} = \frac{p A}{q}$ đối với bất kỳ $\frac{p}{q}$ nào._

??? hint "Lời giải"
    Như chúng ta đã lưu ý ở trên, $[a_0; a_1, \dots, a_k] = (L_{a_0} \circ L_{a_1} \circ \dots \circ L_{a_k})(\infty)$, do đó $L([a_0; a_1, \dots, a_k]) = (L \circ L_{a_0} \circ L_{a_1} \circ \dots L_{a_k})(\infty)$.

    Do đó, bằng cách thêm tuần tự $L_{a_0}$, $L_{a_1}$ và cứ thế, chúng ta sẽ có thể tính toán

    $$(L \circ L_{a_0} \circ \dots \circ L_{a_k})(x) = L\left(\frac{p_k x + p_{k-1}}{q_k x + q_{k-1}}\right)=\frac{a_k x + b_k}{c_k x + d_k}.$$ 

    Vì $L(x)$ có thể đảo ngược, nó cũng đơn điệu trong $x$. Do đó, đối với bất kỳ $x \geq 0$ nào, nó đúng rằng $L(\frac{p_k x + p_{k-1}}{q_k x + q_{k-1}})$ nằm giữa $L(\frac{p_k}{q_k}) = \frac{a_k}{c_k}$ và $L(\frac{p_{k-1}}{q_{k-1}}) = \frac{b_k}{d_k}$.

    Hơn nữa, đối với $x=[a_{k+1}; \dots, a_n]$ nó bằng $L(A)$. Do đó, $b_0 = \lfloor L(A) \rfloor$ nằm giữa $\lfloor L(\frac{p_k}{q_k}) \rfloor$ và $\lfloor L(\frac{p_{k-1}}{q_{k-1}}) \rfloor$. Khi chúng bằng nhau, chúng cũng bằng $b_0$.

    Lưu ý rằng $L(A) = (L_{b_0} \circ L_{b_1} \circ \dots \circ L_{b_m})(\infty)$. Biết $b_0$, chúng ta có thể hợp $L_{b_0}^{-1}$ với phép biến đổi hiện tại và tiếp tục thêm $L_{a_{k+1}}$, $L_{a_{k+2}}$ và cứ thế, tìm kiếm các sàn mới để đồng ý, từ đó chúng ta sẽ có thể suy ra $b_1$ và cứ thế cho đến khi chúng ta khôi phục tất cả các giá trị của $[b_0; b_1, \dots, b_m]$.

!!! example "Số học liên phân số"
    Cho $A=[a_0; a_1, \dots, a_n]$ và $B=[b_0; b_1, \dots, b_m]$. Tính biểu diễn liên phân số của $A+B$ và $A \cdot B$.
??? hint "Lời giải"
    Ý tưởng ở đây tương tự như bài toán trước, nhưng thay vì $L(x) = \frac{ax+b}{cx+d}$ bạn nên xem xét phép biến đổi phân song tuyến tính $L(x, y) = \frac{axy+bx+cy+d}{exy+fx+gy+h}$.

    Thay vì $L(x) \mapsto L(L_{a_k}(x))$ bạn sẽ thay đổi phép biến đổi hiện tại của mình thành $L(x, y) \mapsto L(L_{a_k}(x), y)$ hoặc $L(x, y) \mapsto L(x, L_{b_k}(y))$.

    Sau đó, bạn kiểm tra xem $\lfloor \frac{a}{e} \rfloor = \lfloor \frac{b}{f} \rfloor = \lfloor \frac{c}{g} \rfloor = \lfloor \frac{d}{h} \rfloor$ và nếu tất cả chúng đều đồng ý, bạn sử dụng giá trị này làm $c_k$ trong phân số kết quả và thay đổi phép biến đổi thành

    $$L(x, y) \mapsto \frac{1}{L(x, y) - c_k}.$$ 

!!! info "Định nghĩa"
    Một liên phân số $x = [a_0; a_1, \dots]$ được cho là **tuần hoàn** nếu $x = [a_0; a_1, \dots, a_k, x]$ đối với một số $k$.

    Một liên phân số $x = [a_0; a_1, \dots]$ được cho là **tuần hoàn cuối cùng** nếu $x = [a_0; a_1, \dots, a_k, y]$, trong đó $y$ là tuần hoàn.

Đối với $x = [1; 1, 1, \dots]$ nó đúng rằng $x = 1 + \frac{1}{x}$, do đó $x^2 = x + 1$. Có một mối liên hệ chung giữa các liên phân số tuần hoàn và các phương trình bậc hai. Xét phương trình sau:

$$ x = [a_0; a_1, \dots, a_k, x].$$

Một mặt, phương trình này có nghĩa là biểu diễn liên phân số của $x$ là tuần hoàn với chu kỳ $k+1$.

Mặt khác, sử dụng công thức cho các giản phân, phương trình này có nghĩa là

$$x = \frac{p_k x + p_{k-1}}{q_k x + q_{k-1}}.$$

Tức là, $x$ là một phép biến đổi phân tuyến tính của chính nó. Từ phương trình suy ra rằng $x$ là một nghiệm của phương trình bậc hai:

$$q_k x^2 + (q_{k-1}-p_k)x - p_{k-1} = 0.$$

Lý luận tương tự đúng cho các liên phân số tuần hoàn cuối cùng, tức là $x = [a_0; a_1, \dots, a_k, y]$ đối với $y=[b_0; b_1, \dots, b_k, y]$. Thật vậy, từ phương trình đầu tiên chúng ta suy ra rằng $x = L_0(y)$ và từ phương trình thứ hai rằng $y = L_1(y)$, trong đó $L_0$ và $L_1$ là các phép biến đổi phân tuyến tính. Do đó,

$$x = (L_0 \circ L_1)(y) = (L_0 \circ L_1 \circ L_0^{-1})(x).$$ 

Người ta có thể chứng minh thêm (và điều này được Lagrange thực hiện lần đầu tiên) rằng đối với phương trình bậc hai tùy ý $ax^2+bx+c=0$ với các hệ số nguyên, nghiệm $x$ của nó là một liên phân số tuần hoàn cuối cùng.

!!! example "Số vô tỉ bậc hai"
    Tìm liên phân số của $\alpha = \frac{x+y\sqrt{n}}{z}$ trong đó $x, y, z, n \in \mathbb Z$ và $n > 0$ không phải là số chính phương.
??? hint "Lời giải"
    Đối với thương đầy đủ thứ $k$ là $s_k$ của số, nói chung nó đúng rằng

    $$\alpha = [a_0; a_1, \dots, a_{k-1}, s_k] = \frac{s_k p_{k-1} + p_{k-2}}{s_k q_{k-1} + q_{k-2}}.$$

    Do đó, 

    $$s_k = -\frac{\alpha q_{k-1} - p_{k-1}}{\alpha q_k - p_k} = -\frac{q_{k-1} y \sqrt n + (x q_{k-1} - z p_{k-1})}{q_k y \sqrt n + (xq_k-zp_k)}.$$

    Nhân tử số và mẫu số với $(xq_k - zp_k) - q_k y \sqrt n$, chúng ta sẽ loại bỏ $\sqrt n$ ở mẫu số, do đó các thương đầy đủ có dạng

    $$s_k = \frac{x_k + y_k \sqrt n}{z_k}.$$ 

    Hãy tìm $s_{k+1}$, giả sử rằng $s_k$ đã biết.

    Trước hết, $a_k = \lfloor s_k \rfloor = \left\lfloor \frac{x_k + y_k \lfloor \sqrt n \rfloor}{z_k} \right\rfloor$. Sau đó,

    $$s_{k+1} = \frac{1}{s_k-a_k} = \frac{z_k}{(x_k - z_k a_k) + y_k \sqrt n} = \frac{z_k (x_k - y_k a_k) - y_k z_k \sqrt n}{(x_k - y_k a_k)^2 - y_k^2 n}.$$ 

    Do đó, nếu chúng ta ký hiệu $t_k = x_k - y_k a_k$, nó sẽ đúng rằng

    \begin{align}x_{k+1} &=& z_k t_k, \\ y_{k+1} &=& -y_k z_k, \\ z_{k+1} &=& t_k^2 - y_k^2 n.\end{align}

    Điều hay về biểu diễn như vậy là nếu chúng ta rút gọn $x_{k+1}, y_{k+1}, z_{k+1}$ bằng ước chung lớn nhất của chúng, kết quả sẽ là duy nhất. Do đó, chúng ta có thể sử dụng nó để kiểm tra xem trạng thái hiện tại đã được lặp lại chưa và cũng để kiểm tra xem chỉ số trước đó có trạng thái này ở đâu.

    Dưới đây là mã để tính biểu diễn liên phân số cho $\alpha = \sqrt n$:

    === "Python"
        ```py
        # tính liên phân số của sqrt(n)
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

    Sử dụng cùng một hàm `step` nhưng các giá trị ban đầu của $x$, $y$ và $z$ khác nhau, có thể tính toán nó cho $\frac{x+y \sqrt{n}}{z}$ tùy ý.

!!! example "[Tavrida NU Akai Contest - Continued Fraction](https://timus.online/problem.aspx?space=1&num=1814)"
    Bạn được cho $x$ và $k$, $x$ không phải là số chính phương. Đặt $\sqrt x = [a_0; a_1, \dots]$, tìm $\frac{p_k}{q_k}=[a_0; a_1, \dots, a_k]$ đối với $0 \leq k \leq 10^9$.
??? hint "Lời giải"
    Sau khi tính toán chu kỳ của $\sqrt x$, có thể tính $a_k$ bằng cách sử dụng lũy thừa nhị phân trên phép biến đổi phân tuyến tính gây ra bởi biểu diễn liên phân số. Để tìm phép biến đổi kết quả, bạn nén chu kỳ có kích thước $T$ thành một phép biến đổi duy nhất và lặp lại nó $\lfloor \frac{k-1}{T}\rfloor$ lần, sau đó bạn kết hợp nó thủ công với các phép biến đổi còn lại.

    === "Python"
        ```py
        x, k = map(int, input().split())

        mod = 10**9+7
        
        # hợp (A[0]*x + A[1]) / (A[2]*x + A[3]) và (B[0]*x + B[1]) / (B[2]*x + B[3])
        def combine(A, B):
            return [t % mod for t in [A[0]*B[0]+A[1]*B[2], A[0]*B[1]+A[1]*B[3], A[2]*B[0]+A[3]*B[2], A[2]*B[1]+A[3]*B[3]]]

        A = [1, 0, 0, 1] # (x + 0) / (0*x + 1) = x

        a = sqrt(x)

        T = len(a) - 1 # chu kỳ của a

        # áp dụng ak + 1/x = (ak*x+1)/(1x+0) cho (Ax + B) / (Cx + D)
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

## Giải thích hình học

Đặt $\vec r_k = (q_k;p_k)$ đối với giản phân $r_k = \frac{p_k}{q_k}$. Khi đó, hệ thức truy hồi sau đây đúng:

$$\vec r_k = a_k \vec r_{k-1} + \vec r_{k-2}.$$ 

Đặt $\vec r = (1;r)$. Khi đó, mỗi vector $(x;y)$ tương ứng với số bằng hệ số góc của nó là $\frac{y}{x}$.

Với khái niệm [tích vô hướng giả](../geometry/basic-geometry.md) $(x_1;y_1) \times (x_2;y_2) = x_1 y_2 - x_2 y_1$, có thể chứng minh (xem giải thích bên dưới) rằng

$$s_k = -\frac{\vec r_{k-2} \times \vec r}{\vec r_{k-1} \times \vec r} = \left|\frac{\vec r_{k-2} \times \vec r}{\vec r_{k-1} \times \vec r}\right|.$$

Phương trình cuối cùng là do thực tế là $r_{k-1}$ và $r_{k-2}$ nằm ở hai phía khác nhau của $r$, do đó các tích vô hướng giả của $\vec r_{k-1}$ và $\vec r_{k-2}$ với $\vec r$ có dấu khác nhau. Với $a_k = \lfloor s_k \rfloor$ trong đầu, công thức cho $\vec r_k$ bây giờ trông giống như

$$\vec r_k = \vec r_{k-2} + \left\lfloor \left| \frac{\vec r \times \vec r_{k-2}}{\vec r \times \vec r_{k-1}}\right|\right\rfloor \vec r_{k-1}.$$ 

Lưu ý rằng $\vec r_k \times r = (q;p) \times (1;r) = qr - p$, do đó

$$a_k = \left\lfloor \left| \frac{q_{k-1}r-p_{k-1}}{q_{k-2}r-p_{k-2}} \right| \right\rfloor.$$

??? hint "Giải thích"
    Như chúng ta đã lưu ý, $a_k = \lfloor s_k \rfloor$, trong đó $s_k = [a_k; a_{k+1}, a_{k+2}, \dots]$. Mặt khác, từ hệ thức truy hồi của giản phân, chúng ta suy ra rằng

    $$r = [a_0; a_1, \dots, a_{k-1}, s_k] = \frac{s_k p_{k-1} + p_{k-2}}{s_k q_{k-1} + q_{k-2}}.$$

    Ở dạng vector, nó viết lại thành

    $$\vec r \parallel s_k \vec r_{k-1} + \vec r_{k-2},$$

    nghĩa là $\vec r$ và $s_k \vec r_{k-1} + \vec r_{k-2}$ là cùng phương (tức là có cùng hệ số góc). Lấy [tích vô hướng giả](../geometry/basic-geometry.md) của cả hai phần với $\vec r$, chúng ta có được

    $$0 = s_k (\vec r_{k-1} \times \vec r) + (\vec r_{k-2} \times \vec r),$$

    cho ra công thức cuối cùng

    $$s_k = -\frac{\vec r_{k-2} \times \vec r}{\vec r_{k-1} \times \vec r}.$$ 

!!! example "Thuật toán kéo dài mũi"
    Mỗi khi bạn cộng $\vec r_{k-1}$ vào vector $\vec p$, giá trị của $\vec p \times \vec r$ được tăng lên bởi $\vec r_{k-1} \times \vec r$.

    Do đó, $a_k=\lfloor s_k \rfloor$ là số nguyên lớn nhất của các vector $\vec r_{k-1}$ có thể được cộng vào $\vec r_{k-2}$ mà không làm thay đổi dấu của tích chéo với $\vec r$.

    Nói cách khác, $a_k$ là số nguyên lớn nhất số lần bạn có thể cộng $\vec r_{k-1}$ vào $\vec r_{k-2}$ mà không cắt qua đường thẳng được xác định bởi $\vec r$:

    <figure><img src="https://upload.wikimedia.org/wikipedia/commons/9/92/Continued_convergents_geometry.svg" width="700px"/>
    <figcaption>_Các giản phân của $r=\frac{7}{9}=[0;1,3,2]$. Các bán giản phân tương ứng với các điểm trung gian giữa các mũi tên màu xám._</figcaption></figure>

    Trên hình ảnh trên, $\vec r_2 = (4;3)$ thu được bằng cách cộng lặp đi lặp lại $\vec r_1 = (1;1)$ vào $\vec r_0 = (1;0)$.

    Khi không thể cộng thêm $\vec r_1$ vào $\vec r_0$ mà không cắt qua đường thẳng $y=rx$, chúng ta đi sang phía bên kia và cộng lặp đi lặp lại $\vec r_2$ vào $\vec r_1$ để thu được $\vec r_3 = (9;7)$.

    Thủ tục này tạo ra các vector dài hơn theo cấp số nhân, tiến gần đến đường thẳng.

    Đối với thuộc tính này, thủ tục tạo ra các vector giản phân kế tiếp được Boris Delaunay đặt tên là **thuật toán kéo dài mũi**.

Nếu chúng ta nhìn vào tam giác được vẽ trên các điểm $\vec r_{k-2}$, $\vec r_{k}$ và $\vec 0$, chúng ta sẽ nhận thấy rằng diện tích gấp đôi của nó là

$$|\vec r_{k-2} \times \vec r_k| = |\vec r_{k-2} \times (\vec r_{k-2} + a_k \vec r_{k-1})| = a_k |\vec r_{k-2} \times \vec r_{k-1}| = a_k.$$

Kết hợp với [định lý Pick](../geometry/picks-theorem.md), điều đó có nghĩa là không có điểm lưới nào nằm hoàn toàn bên trong tam giác và các điểm lưới duy nhất trên biên của nó là $\vec 0$ và $\vec r_{k-2} + t \cdot \vec r_{k-1}$ đối với tất cả các số nguyên $t$ sao cho $0 \leq t \leq a_k$. Khi được nối cho tất cả các $k$ có thể, điều đó có nghĩa là không có điểm nguyên nào trong không gian giữa các đa giác được hình thành bởi các vector giản phân có chỉ số chẵn và lẻ.

Điều này, đến lượt nó, có nghĩa là $\vec r_k$ với các hệ số lẻ tạo thành một bao lồi của các điểm lưới với $x \geq 0$ phía trên đường thẳng $y=rx$, trong khi $\vec r_k$ với các hệ số chẵn tạo thành một bao lồi của các điểm lưới với $x > 0$ phía dưới đường thẳng $y=rx$.


!!! info "Định nghĩa"

    Các đa giác này còn được gọi là **đa giác Klein**, được đặt theo tên của Felix Klein, người đầu tiên đề xuất giải thích hình học này cho các liên phân số.

## Ví dụ bài toán

Bây giờ hầu hết các sự thật và khái niệm quan trọng đã được giới thiệu, đã đến lúc đi sâu vào các ví dụ bài toán cụ thể.

!!! example "Bao lồi dưới đường thẳng"
    Tìm bao lồi của các điểm lưới $(x;y)$ sao cho $0 \leq x \leq N$ và $0 \leq y \leq rx$ đối với $r=[a_0;a_1,\dots,a_k]=\frac{p_k}{q_k}$.

??? hint "Lời giải"
    Nếu chúng ta đang xem xét tập hợp không bị chặn $0 \leq x$, bao lồi trên sẽ được cho bởi chính đường thẳng $y=rx$.

    Tuy nhiên, với ràng buộc bổ sung $x \leq N$, chúng ta sẽ cần phải đi chệch khỏi đường thẳng để duy trì bao lồi thích hợp.

    Đặt $t = \lfloor \frac{N}{q_k}\rfloor$, sau đó $t$ điểm lưới đầu tiên trên bao lồi sau $(0;0)$ là $\alpha \cdot (q_k; p_k)$ đối với số nguyên $1 \leq \alpha \leq t$.

    Tuy nhiên $(t+1)(q_k; p_k)$ không thể là điểm lưới tiếp theo vì $(t+1)q_k$ lớn hơn $N$.

    Để đến các điểm lưới tiếp theo trong bao lồi, chúng ta nên đến điểm $(x;y)$ mà đi chệch khỏi $y=rx$ một khoảng nhỏ nhất, trong khi duy trì $x \leq N$.

    <figure><img src="https://upload.wikimedia.org/wikipedia/commons/b/b1/Lattice-hull.svg" width="500px"/>
    <figcaption>Bao lồi của các điểm lưới dưới $y=\frac{4}{7}x$ đối với $0 \leq x \leq 19$ bao gồm các điểm $(0;0), (7;4), (14;8), (16;9), (18;10), (19;10)$.</figcaption></figure>

    Đặt $(x; y)$ là điểm cuối cùng hiện tại trong bao lồi. Khi đó điểm tiếp theo $(x'; y')$ là sao cho $x' \leq N$ và $(x'; y') - (x; y) = (\Delta x; \Delta y)$ càng gần đường thẳng $y=rx$ càng tốt. Nói cách khác, $(\Delta x; \Delta y)$ tối đa hóa $r \Delta x - \Delta y$ với điều kiện $\Delta x \leq N - x$ và $\Delta y \leq r \Delta x$.

    Các điểm như vậy nằm trên bao lồi của các điểm lưới dưới $y=rx$. Nói cách khác, $(\Delta x; \Delta y)$ phải là một bán giản phân dưới của $r$.

    Nói như vậy, $(\Delta x; \Delta y)$ có dạng $(q_{i-1}; p_{i-1}) + t \cdot (q_i; p_i)$ đối với một số lẻ $i$ và $0 \leq t < a_i$.

    Để tìm $i$ như vậy, chúng ta có thể duyệt qua tất cả các $i$ có thể bắt đầu từ cái lớn nhất và sử dụng $t = \lfloor \frac{N-x-q_{i-1}}{q_i} \rfloor$ đối với $i$ sao cho $N-x-q_{i-1} \geq 0$.

    Với $(\Delta x; \Delta y) = (q_{i-1}; p_{i-1}) + t \cdot (q_i; p_i)$, điều kiện $\Delta y \leq r \Delta x$ sẽ được bảo toàn bởi các thuộc tính của bán giản phân.

    Và $t < a_i$ sẽ đúng vì chúng ta đã sử dụng hết các bán giản phân thu được từ $i+2$, do đó $x + q_{i-1} + a_i q_i = x+q_{i+1}$ lớn hơn $N$.

    Bây giờ chúng ta có thể cộng $(\Delta x; \Delta y)$ vào $(x;y)$ $k = \lfloor \frac{N-x}{\Delta x} \rfloor$ lần trước khi chúng ta vượt quá $N$, sau đó chúng ta sẽ thử bán giản phân tiếp theo.

    === "C++"
        ```cpp
        // trả về [ah, ph, qh] sao cho các điểm r[i]=(ph[i], qh[i]) tạo thành bao lồi trên
        // của các điểm lưới trên 0 <= x <= N và 0 <= y <= r * x, trong đó r = [a0; a1, a2, ...]
        // và có ah[i]-1 điểm nguyên trên đoạn giữa r[i] và r[i+1]
        auto hull(auto a, int N) {
            auto [p, q] = convergents(a);
            int t = N / q.back();
            vector ah = {t};
            vector ph = {0, t*p.back()};
            vector qh = {0, t*q.back()};

            for(int i = q.size() - 1; i >= 0; i--) {
                if(i % 2) {
                    while(qh.back() + q[i - 1] <= N) {
                        t = (N - qh.back() - q[i - 1]) / q[i];
                        int dp = p[i - 1] + t * p[i];
                        int dq = q[i - 1] + t * q[i];
                        int k = (N - qh.back()) / dq;
                        ah.push_back(k);
                        ph.push_back(ph.back() + k * dp);
                        qh.push_back(qh.back() + k * dq);
                    }
                }
            }
            return make_tuple(ah, ph, qh);
        }
        ```
    === "Python"
        ```py
        # trả về [ah, ph, qh] sao cho các điểm r[i]=(ph[i], qh[i]) tạo thành bao lồi trên
        # của các điểm lưới trên 0 <= x <= N và 0 <= y <= r * x, trong đó r = [a0; a1, a2, ...]
        # và có ah[i]-1 điểm nguyên trên đoạn giữa r[i] và r[i+1]
        def hull(a, N):
            p, q = convergents(a)
            t = N // q[-1]
            ah = [t]
            ph = [0, t*p[-1]]
            qh = [0, t*q[-1]]
            for i in reversed(range(len(q))):
                if i % 2 == 1:
                    while qh[-1] + q[i-1] <= N:
                        t = (N - qh[-1] - q[i-1]) // q[i]
                        dp = p[i-1] + t*p[i]
                        dq = q[i-1] + t*q[i]
                        k = (N - qh[-1]) // dq
                        ah.append(k)
                        ph.append(ph[-1] + k * dp)
                        qh.append(qh[-1] + k * dq)
            return ah, ph, qh
        ```

!!! example "[Timus - Crime and Punishment](https://timus.online/problem.aspx?space=1&num=1430)"
    Bạn được cho các số nguyên $A$, $B$ và $N$. Tìm $x \geq 0$ và $y \geq 0$ sao cho $Ax + By \leq N$ và $Ax + By$ lớn nhất có thể.

??? hint "Lời giải"
    Trong bài toán này, $1 \leq A, B, N \leq 2 \cdot 10^9$, vì vậy nó có thể được giải quyết trong $O(\sqrt N)$. Tuy nhiên, có một giải pháp $O(\log N)$ với liên phân số.

    Để thuận tiện, chúng ta sẽ đảo ngược hướng của $x$ bằng cách thực hiện một phép thay thế $x \mapsto \lfloor \frac{N}{A}\rfloor - x$, để bây giờ chúng ta cần tìm điểm $(x; y)$ sao cho $0 \leq x \leq \lfloor \frac{N}{A} \rfloor$, $By - Ax \leq N \bmod A$ và $By - Ax$ lớn nhất có thể. $y$ tối ưu cho mỗi $x$ có giá trị là $\lfloor \frac{Ax + (N \bmod A)}{B} \rfloor$.

    Để xử lý nó một cách chung chung hơn, chúng ta sẽ viết một hàm tìm điểm tốt nhất trên $0 \leq x \leq N$ và $y = \lfloor \frac{Ax+B}{C} \rfloor$.

    Ý tưởng giải pháp cốt lõi trong bài toán này về cơ bản lặp lại bài toán trước, nhưng thay vì sử dụng các bán giản phân dưới để đi chệch khỏi đường thẳng, bạn sử dụng các bán giản phân trên để đến gần đường thẳng hơn mà không cắt qua nó và không vi phạm $x \leq N$. Thật không may, không giống như bài toán trước, bạn cần đảm bảo rằng bạn không cắt qua đường thẳng $y=\frac{Ax+B}{C}$ trong khi đến gần nó hơn, vì vậy bạn nên ghi nhớ điều này khi tính toán hệ số $t$ của bán giản phân.

    === "Python"
        ```py
        # (x, y) sao cho y = (A*x+B) // C,
        # Cy - Ax lớn nhất và 0 <= x <= N.
        def closest(A, B, C, N):
            # y <= (A*x + B)/C <=> diff(x, y) <= B
            def diff(x, y):
                return C*y-A*x
            a = fraction(A, C)
            p, q = convergents(a)
            ph = [B // C]
            qh = [0]
            for i in range(2, len(q) - 1):
                if i % 2 == 0:
                    while diff(qh[-1] + q[i+1], ph[-1] + p[i+1]) <= B:
                        t = 1 + (diff(qh[-1] + q[i-1], ph[-1] + p[i-1]) - B - 1) // abs(diff(q[i], p[i]))
                        dp = p[i-1] + t*p[i]
                        dq = q[i-1] + t*q[i]
                        k = (N - qh[-1]) // dq
                        if k == 0:
                            return qh[-1], ph[-1]
                        if diff(dq, dp) != 0:
                            k = min(k, (B - diff(qh[-1], ph[-1])) // diff(dq, dp))
                        qh.append(qh[-1] + k*dq)
                        ph.append(ph[-1] + k*dp)
            return qh[-1], ph[-1]

        def solve(A, B, N):
            x, y = closest(A, N % A, B, N // A)
            return N // A - x, y
        ```

!!! example "[June Challenge 2017 - Euler Sum](https://www.codechef.com/problems/ES)"
    Tính $\sum\limits_{x=1}^N \lfloor ex \rfloor$, trong đó $e = [2; 1, 2, 1, 1, 4, 1, 1, 6, 1, \dots, 1, 2n, 1, \dots]$ là số Euler và $N \leq 10^{4000}$.

??? hint "Lời giải"
    Tổng này bằng số điểm lưới $(x;y)$ sao cho $1 \leq x \leq N$ và $1 \leq y \leq ex$.    

    Sau khi xây dựng bao lồi của các điểm dưới $y=ex$, số này có thể được tính bằng [định lý Pick](../geometry/picks-theorem.md):

    === "C++"
        ```cpp
        // tổng floor(k * x) đối với k trong [1, N] và x = [a0; a1, a2, ...]
        int sum_floor(auto a, int N) {
            N++;
            auto [ah, ph, qh] = hull(a, N);

            // Số điểm lưới trong một hình thang vuông đứng
            // trên các điểm (0; 0) - (0; y1) - (dx; y2) - (dx; 0) có
            // a+1 điểm nguyên trên đoạn (0; y1) - (dx; y2).
            auto picks = [](int y1, int y2, int dx, int a) {
                int b = y1 + y2 + a + dx;
                int A = (y1 + y2) * dx;
                return (A - b + 2) / 2 + b - (y2 + 1);
            };

            int ans = 0;
            for(size_t i = 1; i < qh.size(); i++) {
                ans += picks(ph[i - 1], ph[i], qh[i] - qh[i - 1], ah[i - 1]);
            }
            return ans - N;
        }
        ```
    === "Python"
        ```py
        # tổng floor(k * x) đối với k trong [1, N] và x = [a0; a1, a2, ...]
        def sum_floor(a, N):
            N += 1
            ah, ph, qh = hull(a, N)

            # Số điểm lưới trong một hình thang vuông đứng
            # trên các điểm (0; 0) - (0; y1) - (dx; y2) - (dx; 0) có
            # a+1 điểm nguyên trên đoạn (0; y1) - (dx; y2).
            def picks(y1, y2, dx, a):
                b = y1 + y2 + a + dx
                A = (y1 + y2) * dx
                return (A - b + 2) // 2 + b - (y2 + 1)

            ans = 0
            for i in range(1, len(qh)):
                ans += picks(ph[i-1], ph[i], qh[i]-qh[i-1], ah[i-1])
            return ans - N
        ``` 

!!! example "[NAIPC 2019 - It's a Mod, Mod, Mod, Mod World](https://open.kattis.com/problems/itsamodmodmodmodworld)"
    Cho $p$, $q$ và $n$, tính $\sum\limits_{i=1}^n [p \cdot i \bmod q]$.

??? hint "Lời giải"
    Bài toán này rút gọn về bài toán trước nếu bạn lưu ý rằng $a \bmod b = a - \lfloor \frac{a}{b} \rfloor b$. Với thực tế này, tổng rút gọn thành

    $$\sum\limits_{i=1}^n \left(p \cdot i - \left\lfloor \frac{p \cdot i}{q} \right\rfloor q\right) = \frac{pn(n+1)}{2}-q\sum\limits_{i=1}^n \left\lfloor \frac{p \cdot i}{q}\right\rfloor.$$

    Tuy nhiên, tính tổng $\lfloor rx \rfloor$ đối với $x$ từ $1$ đến $N$ là điều chúng ta có thể làm được từ bài toán trước.

    === "C++"
        ```cpp
        void solve(int p, int q, int N) {
            cout << p * N * (N + 1) / 2 - q * sum_floor(fraction(p, q), N) << "\n";
        }
        ```
    === "Python"
        ```py
        def solve(p, q, N):
            return p * N * (N + 1) // 2 - q * sum_floor(fraction(p, q), N)
        ``` 

!!! example "[Library Checker - Sum of Floor of Linear](https://judge.yosupo.jp/problem/sum_of_floor_of_linear)"
    Cho $N$, $M$, $A$ và $B$, tính $\sum\limits_{i=0}^{N-1} \lfloor \frac{A \cdot i + B}{M} \rfloor$.

??? hint "Lời giải"
    Đây là bài toán phức tạp nhất về mặt kỹ thuật cho đến nay.

    Có thể sử dụng cùng một phương pháp và xây dựng bao lồi đầy đủ của các điểm dưới đường thẳng $y = \frac{Ax+B}{M}$.

    Chúng ta đã biết cách giải quyết nó đối với $B = 0$. Hơn nữa, chúng ta đã biết cách xây dựng bao lồi này đến điểm lưới gần nhất với đường thẳng này trên đoạn $[0, N-1]$ (điều này được thực hiện trong bài toán "Tội ác và hình phạt" ở trên).

    Bây giờ chúng ta nên lưu ý rằng một khi chúng ta đã đến điểm gần nhất với đường thẳng, chúng ta có thể chỉ cần giả định rằng đường thẳng thực sự đi qua điểm gần nhất, vì không có điểm lưới nào khác trên $[0, N-1]$ ở giữa đường thẳng thực tế và đường thẳng được di chuyển xuống một chút để đi qua điểm gần nhất.

    Nói như vậy, để xây dựng bao lồi đầy đủ dưới đường thẳng $y=\frac{Ax+B}{M}$ trên $[0, N-1]$, chúng ta có thể xây dựng nó đến điểm gần nhất với đường thẳng trên $[0, N-1]$ và sau đó tiếp tục như thể đường thẳng đi qua điểm này, sử dụng lại thuật toán để xây dựng bao lồi với $B=0$:

    === "Python"
        ```py
        # bao lồi của lưới (x, y) sao cho C*y <= A*x+B
        def hull(A, B, C, N):
            def diff(x, y):
                return C*y-A*x
            a = fraction(A, C)
            p, q = convergents(a)
            ah = []
            ph = [B // C]
            qh = [0]

            def insert(dq, dp):
                k = (N - qh[-1]) // dq
                if diff(dq, dp) > 0:
                    k = min(k, (B - diff(qh[-1], ph[-1])) // diff(dq, dp))
                ah.append(k)
                qh.append(qh[-1] + k*dq)
                ph.append(ph[-1] + k*dp)

            for i in range(1, len(q) - 1):
                if i % 2 == 0:
                    while diff(qh[-1] + q[i+1], ph[-1] + p[i+1]) <= B:
                        t = (B - diff(qh[-1] + q[i+1], ph[-1] + p[i+1])) // abs(diff(q[i], p[i]))
                        dp = p[i+1] - t*p[i]
                        dq = q[i+1] - t*q[i]
                        if dq < 0 or qh[-1] + dq > N:
                            break
                        insert(dq, dp)

            insert(q[-1], p[-1])

            for i in reversed(range(len(q))):
                if i % 2 == 1:
                    while qh[-1] + q[i-1] <= N:
                        t = (N - qh[-1] - q[i-1]) // q[i]
                        dp = p[i-1] + t*p[i]
                        dq = q[i-1] + t*q[i]
                        insert(dq, dp)
            return ah, ph, qh
        ```

!!! example "[OKC 2 - From Modular to Rational](https://codeforces.com/gym/102354/problem/I)"
    Có một số hữu tỉ $\frac{p}{q}$ sao cho $1 \leq p, q \leq 10^9$. Bạn có thể hỏi giá trị của $p q^{-1}$ modulo $m \sim 10^9$ đối với một số số nguyên tố $m$. Khôi phục $\frac{p}{q}$.

    _Phát biểu tương đương:_ Tìm $x$ sao cho $Ax \bmod M$ là nhỏ nhất đối với $1 \leq x \leq N$.

??? hint "Lời giải"
    Do định lý phần dư Trung Hoa, hỏi kết quả modulo một số số nguyên tố cũng giống như hỏi nó modulo tích của chúng. Do đó, không mất tính tổng quát, chúng ta sẽ giả định rằng chúng ta biết phần dư modulo một số đủ lớn $m$.

    Có thể có một số nghiệm có thể có $(p, q)$ đối với $p \equiv qr \pmod m$ đối với một phần dư $r$ đã cho. Tuy nhiên, nếu $(p_1, q_1)$ và $(p_2, q_2)$ đều là các nghiệm thì nó cũng đúng rằng $p_1 q_2 \equiv p_2 q_1 \pmod m$. Giả sử rằng $\frac{p_1}{q_1} \neq \frac{p_2}{q_2}$ thì điều đó có nghĩa là $|p_1 q_2 - p_2 q_1|$ ít nhất là $m$.

    Trong phát biểu, chúng ta được cho biết rằng $1 \leq p, q \leq 10^9$, vì vậy nếu cả $p_1, q_1$ và $p_2, q_2$ đều không quá $10^9$, thì sự khác biệt nhiều nhất là $10^{18}$. Đối với $m > 10^{18}$ điều đó có nghĩa là nghiệm $\frac{p}{q}$ với $1 \leq p, q \leq 10^9$ là duy nhất, như một số hữu tỉ.

    Vì vậy, bài toán thu gọn lại, cho trước $r$ modulo $m$, để tìm bất kỳ $q$ nào sao cho $1 \leq q \leq 10^9$ và $qr \bmod m \leq 10^9$.

    Điều này thực chất giống như tìm $q$ sao cho $qr \bmod m$ nhỏ nhất có thể đối với $1 \leq q \leq 10^9$.

    Đối với $qr = km + b$ điều đó có nghĩa là chúng ta cần tìm một cặp $(q, m)$ sao cho $1 \leq q \leq 10^9$ và $qr - km \geq 0$ là nhỏ nhất có thể.

    Vì $m$ là hằng số, chúng ta có thể chia cho nó và phát biểu lại là tìm $q$ sao cho $1 \leq q \leq 10^9$ và $\frac{r}{m} q - k \geq 0$ là nhỏ nhất có thể.

    Theo thuật ngữ của liên phân số, điều đó có nghĩa là $\frac{k}{q}$ là xấp xỉ Diophantine tốt nhất cho $\frac{r}{m}$ và chỉ cần kiểm tra các bán giản phân dưới của $\frac{r}{m}$ là đủ.

    === "Python"
        ```py
        # tìm Q sao cho Q*r mod m nhỏ nhất đối với 1 <= k <= n < m 
        def mod_min(r, n, m):
            a = fraction(r, m)
            p, q = convergents(a)
            for i in range(2, len(q)):
                if i % 2 == 1 and (i + 1 == len(q) or q[i+1] > n):
                    t = (n - q[i-1]) // q[i]
                    return q[i-1] + t*q[i]
        ```

## Bài tập thực hành

* [UVa OJ - Continued Fractions](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=775)
* [ProjectEuler+ #64: Odd period square roots](https://www.hackerrank.com/contests/projecteuler/challenges/euler064/problem)
* [Codeforces Round #184 (Div. 2) - Continued Fractions](https://codeforces.com/contest/305/problem/B)
* [Codeforces Round #201 (Div. 1) - Doodle Jump](https://codeforces.com/contest/346/problem/E)
* [Codeforces Round #325 (Div. 1) - Alice, Bob, Oranges and Apples](https://codeforces.com/contest/585/problem/C)
* [POJ Founder Monthly Contest 2008.03.16 - A Modular Arithmetic Challenge](http://poj.org/problem?id=3530)
* [2019 Multi-University Training Contest 5 - fraction](http://acm.hdu.edu.cn/showproblem.php?pid=6624)
* [SnackDown 2019 Elimination Round - Election Bait](https://www.codechef.com/SNCKEL19/problems/EBAIT)
* [Code Jam 2019 round 2 - Continued Fraction](https://github.com/google/coding-competitions-archive/blob/main/codejam/2019/round_2/new_elements_part_2/statement.pdf)

```