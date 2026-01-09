---
tags:
  - Translated
e_maxx_link: stern_brocot_farey
---

# Cây Stern-Brocot và dãy Farey (The Stern-Brocot tree and Farey sequences) {: #the-stern-brocot-tree-and-farey-sequences}

## Cây Stern-Brocot (Stern-Brocot tree) {: #stern-brocot-tree}

Cây Stern-Brocot là một cấu trúc thanh lịch để biểu diễn tập hợp tất cả các phân số dương. Nó được phát hiện độc lập bởi nhà toán học người Đức Moritz Stern vào năm 1858 và bởi nhà sản xuất đồng hồ người Pháp Achille Brocot vào năm 1861. Tuy nhiên, một số nguồn gán sự phát hiện này cho nhà toán học Hy Lạp cổ đại Eratosthenes.

Việc xây dựng bắt đầu ở lần lặp thứ 0 với hai phân số

$$
    \frac{0}{1}, \frac{1}{0}
$$

trong đó cần lưu ý rằng đại lượng thứ hai không phải là một phân số đúng nghĩa, nhưng nó có thể được hiểu là một phân số tối giản đại diện cho vô cực.

Ở mọi lần lặp tiếp theo, hãy xem xét tất cả các phân số liền kề $\frac{a}{b}$ và $\frac{c}{d}$ và chèn [trung gian (mediant)](https://en.wikipedia.org/wiki/Mediant_(mathematics)) $\frac{a+c}{b+d}$ vào giữa chúng.

Một vài lần lặp đầu tiên trông như thế này:

$$
    \begin{array}{c}
    \dfrac{0}{1}, \dfrac{1}{1}, \dfrac{1}{0} \\
    \dfrac{0}{1}, \dfrac{1}{2}, \dfrac{1}{1}, \dfrac{2}{1}, \dfrac{1}{0} \\
    \dfrac{0}{1}, \dfrac{1}{3}, \dfrac{1}{2}, \dfrac{2}{3}, \dfrac{1}{1}, \dfrac{3}{2}, \dfrac{2}{1}, \dfrac{3}{1}, \dfrac{1}{0}
    \end{array}
$$

Tiếp tục quá trình này đến vô cùng, nó bao gồm *tất cả* các phân số dương. Ngoài ra, tất cả các phân số sẽ là *duy nhất* và *tối giản*. Cuối cùng, các phân số cũng sẽ xuất hiện theo thứ tự tăng dần.

Trước khi chứng minh các tính chất này, hãy thực sự hiển thị một hình dung về cây Stern-Brocot, thay vì biểu diễn danh sách. Mỗi phân số trong cây có hai con. Mỗi con là trung gian của tổ tiên gần nhất ở bên trái và tổ tiên gần nhất ở bên phải.

<div style="text-align: center;">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/37/SternBrocotTree.svg/1024px-SternBrocotTree.svg.png" alt="Stern-Brocot tree">
</div>

## Chứng minh (Proofs) {: #proofs}

**Thứ tự (Ordering).** Chứng minh thứ tự rất đơn giản. Chúng tôi lưu ý rằng trung gian của hai phân số luôn nằm giữa các phân số

$$
    \frac{a}{b} \le \frac{a+c}{b+d} \le \frac{c}{d}
$$

với điều kiện là

$$
    \frac{a}{b} \le \frac{c}{d}.
$$

Hai bất đẳng thức có thể dễ dàng được chỉ ra bằng cách viết lại các phân số với mẫu số chung.

Vì thứ tự tăng dần trong lần lặp thứ 0, nó sẽ được duy trì ở mọi lần lặp tiếp theo.

**Tính tối giản (Irreducibility).** Để chứng minh điều này, chúng tôi sẽ chỉ ra rằng đối với bất kỳ hai phân số liền kề nào $\frac{a}{b}$ và $\frac{c}{d}$ chúng ta có

$$
    bc - ad = 1.
$$

Nhớ lại rằng một phương trình Diophantine với hai biến $ax+by=c$ có nghiệm khi và chỉ khi $c$ là bội số của $\gcd(a,b)$. Trong trường hợp của chúng tôi, điều này ngụ ý rằng $\gcd(a,b) = \gcd(c,d) = 1$, đó là những gì chúng tôi muốn chứng minh.

Rõ ràng ở lần lặp thứ 0 $bc - ad = 1$. Điều còn lại cần được chứng minh là các trung gian giữ được thuộc tính này.

Giả sử hai phân số liền kề của chúng tôi duy trì $bc - ad = 1$, sau khi trung gian được thêm vào danh sách

$$
    \frac{a}{b}, \frac{a+c}{b+d}, \frac{c}{d}
$$

các biểu thức mới trở thành

$$\begin{align}
    b(a+c) - a(b+d) &= 1 \\
    c(b+d) - d(a+c) &= 1
\end{align}$$

điều này, sử dụng $bc-ad=1$, có thể dễ dàng được chứng minh là đúng.

Từ đây chúng ta thấy rằng thuộc tính luôn được duy trì và do đó tất cả các phân số đều tối giản.

**Sự hiện diện của tất cả các phân số (The presence of all fractions).** Bằng chứng này liên quan chặt chẽ đến việc định vị một phân số trong cây Stern-Brocot. Từ thuộc tính thứ tự, chúng ta có cây con bên trái của một phân số chỉ chứa các phân số nhỏ hơn phân số cha và cây con bên phải chỉ chứa các phân số lớn hơn phân số cha. Điều này có nghĩa là chúng ta có thể tìm kiếm một phân số bằng cách duyệt qua cây từ gốc, đi sang trái nếu mục tiêu nhỏ hơn phân số và đi sang phải nếu mục tiêu lớn hơn.

Chọn một phân số mục tiêu dương tùy ý $\frac{x}{y}$. Nó rõ ràng nằm giữa $\frac{0}{1}$ và $\frac{1}{0}$, vì vậy cách duy nhất để phân số không nằm trong cây là nếu mất vô số bước để đến được nó.

Nếu đúng như vậy, chúng tôi sẽ tại tất cả các lần lặp có

$$
    \frac{a}{b} \lt \frac{x}{y} \lt \frac{c}{d}
$$

điều này (sử dụng thực tế là một số nguyên $z \gt 0 \iff z \ge 1$) có thể được viết lại thành

$$
\begin{align}
    bx - ay &\ge 1 \\
    cy - dx &\ge 1.
\end{align}
$$

Bây giờ nhân bất đẳng thức đầu tiên với $c+d$ và thứ hai với $a+b$ và cộng chúng để có được

$$
    (c+d)(bx - ay) + (a+b)(cy - dx) \ge a+b+c+d.
$$

Mở rộng điều này và sử dụng thuộc tính đã được hiển thị trước đó $bc-ad=1$, chúng tôi nhận được rằng

$$
    x+y \ge a+b+c+d.
$$

Và do tại mỗi lần lặp, ít nhất một trong các $a,b,c,d$ sẽ tăng lên, quá trình tìm kiếm phân số sẽ chứa không quá $x+y$ lần lặp. Điều này mâu thuẫn với giả định rằng đường đến $\frac{x}{y}$ là vô hạn và do đó $\frac{x}{y}$ phải là một phần của cây.

## Thuật toán xây dựng cây (Tree Building Algorithm) {: #tree-building-algorithm}

Để xây dựng bất kỳ cây con nào của cây Stern-Brocot, chỉ cần biết tổ tiên bên trái và bên phải là đủ. Ở cấp độ đầu tiên, tổ tiên bên trái và bên phải lần lượt là $\frac{0}{1}$ và $\frac{1}{0}$. Sử dụng chúng, chúng tôi tính toán trung gian và tiến hành sâu hơn một cấp, với trung gian thay thế tổ tiên bên phải trong cây con bên trái và ngược lại.

Mã giả này cố gắng xây dựng toàn bộ cây vô hạn:

```cpp
void build(int a = 0, int b = 1, int c = 1, int d = 0, int level = 1) {
    int x = a + c, y = b + d;

    ... output the current fraction x/y at the current level in the tree
    
    build(a, b, x, y, level + 1);
    build(x, y, c, d, level + 1);
}
```

## Thuật toán tìm kiếm phân số (Fraction Search Algorithm) {: #fraction-search-algorithm}

Thuật toán tìm kiếm đã được mô tả trong bằng chứng rằng tất cả các phân số đều xuất hiện trong cây, nhưng chúng tôi sẽ lặp lại ở đây. Thuật toán là một thuật toán tìm kiếm nhị phân. Ban đầu chúng ta đứng ở gốc cây và so sánh mục tiêu của mình với phân số hiện tại. Nếu chúng giống nhau, chúng tôi đã hoàn tất và dừng quá trình. Nếu mục tiêu của chúng tôi nhỏ hơn, chúng tôi di chuyển đến con bên trái, nếu không chúng tôi di chuyển đến con bên phải.

### Tìm kiếm ngây thơ (Naive search) {: #naive-search}

Dưới đây là một triển khai trả về đường dẫn đến một phân số nhất định $\frac{p}{q}$ dưới dạng một chuỗi các ký tự `'L'` và `'R'`, có nghĩa là duyệt đến con bên trái và bên phải tương ứng. Chuỗi ký tự này xác định duy nhất tất cả các phân số dương và được gọi là hệ thống số Stern-Brocot.

```cpp
string find(int p, int q) {
    int pL = 0, qL = 1;
    int pR = 1, qR = 0;
    int pM = 1, qM = 1;
    string res;
    while(pM != p || qM != q) {
        if(p * qM < pM * q) {
            res += 'L';
            tie(pR, qR) = {pM, qM};
        } else {
            res += 'R';
            tie(pL, qL) = {pM, qM};
        }
        tie(pM, qM) = pair{pL + pR, qL + qR};
    }
    return res;
}
```

Số vô tỷ trong hệ thống số Stern-Brocot tương ứng với chuỗi ký tự vô hạn. Dọc theo con đường vô tận hướng tới số vô tỷ, thuật toán sẽ tìm thấy các phân số rút gọn với các mẫu số tăng dần cung cấp xấp xỉ ngày càng tốt hơn của số vô tỷ. Vì vậy, bằng cách lấy một tiền tố của chuỗi vô hạn, các xấp xỉ với bất kỳ độ chính xác mong muốn nào đều có thể đạt được. Ứng dụng này rất quan trọng trong việc chế tạo đồng hồ, giải thích tại sao cây được phát hiện trong miền đó.

Lưu ý rằng đối với phân số $\frac{p}{q}$, độ dài của chuỗi kết quả có thể lớn tới $O(p+q)$, ví dụ khi phân số có dạng $\frac{p}{1}$. Điều này có nghĩa là thuật toán trên **không nên được sử dụng, trừ khi đây là độ phức tạp có thể chấp nhận được**!

### Tìm kiếm logarit (Logarithmic search) {: #logarithmic-search}

May mắn thay, có thể tăng cường thuật toán trên để đảm bảo độ phức tạp $O(\log (p+q))$. Đối với điều này, chúng ta nên lưu ý rằng nếu các phân số ranh giới hiện tại là $\frac{p_L}{q_L}$ và $\frac{p_R}{q_R}$, thì bằng cách thực hiện $a$ bước sang bên phải, chúng ta di chuyển đến phân số $\frac{p_L + a p_R}{q_L + a q_R}$, và bằng cách thực hiện $a$ bước sang bên trái, chúng ta di chuyển đến phân số $\frac{a p_L + p_R}{a q_L + q_R}$.

Do đó, thay vì thực hiện từng bước `L` hoặc `R` một, chúng ta có thể thực hiện $k$ bước theo cùng một hướng cùng một lúc, sau đó chúng ta sẽ chuyển sang đi theo hướng khác, và cứ thế. Theo cách này, chúng ta có thể tìm thấy đường dẫn đến phân số $\frac{p}{q}$ dưới dạng mã hóa độ dài chạy (run-length encoding) của nó.

Khi các hướng xen kẽ theo cách này, chúng tôi sẽ luôn biết nên chọn hướng nào. Vì vậy, để thuận tiện, chúng ta có thể biểu diễn một đường dẫn đến phân số $\frac{p}{q}$ dưới dạng một dãy các phân số

$$
\frac{p_0}{q_0}, \frac{p_1}{q_1}, \frac{p_2}{q_2}, \dots, \frac{p_n}{q_n}, \frac{p_{n+1}}{q_{n+1}} = \frac{p}{q}
$$

sao cho $\frac{p_{k-1}}{q_{k-1}}$ và $\frac{p_k}{q_k}$ là ranh giới của khoảng tìm kiếm ở bước thứ $k$, bắt đầu bằng $\frac{p_0}{q_0} = \frac{0}{1}$ và $\frac{p_1}{q_1} = \frac{1}{0}$. Sau đó, sau bước thứ $k$, chúng ta di chuyển đến một phân số

$$
\frac{p_{k+1}}{q_{k+1}} = \frac{p_{k-1} + a_k p_k}{q_{k-1} + a_k q_k},
$$

trong đó $a_k$ là một số nguyên dương. Nếu bạn quen thuộc với [liên phân số (continued fractions)](../algebra/continued-fractions.md), bạn sẽ nhận ra rằng dãy $\frac{p_i}{q_i}$ là dãy các phân số hội tụ của $\frac{p}{q}$ và dãy $[a_1; a_2, \dots, a_{n}, 1]$ đại diện cho liên phân số của $\frac{p}{q}$.

Điều này cho phép tìm mã hóa độ dài chạy của đường dẫn đến $\frac{p}{q}$ theo cách tuân theo thuật toán tính toán biểu diễn liên phân số của phân số $\frac{p}{q}$:

```cpp
auto find(int p, int q) {
    bool right = true;
    vector<pair<int, char>> res;
    while(q) {
        res.emplace_back(p / q, right ? 'R' : 'L');
        tie(p, q) = pair{q, p % q};
        right ^= 1;
    }
    res.back().first--;
    return res;
}
```

Tuy nhiên, cách tiếp cận này chỉ hoạt động nếu chúng ta đã biết $\frac{p}{q}$ và muốn tìm vị trí của nó trong cây Stern-Brocot.

Trên thực tế, thường thì trường hợp $\frac{p}{q}$ không được biết trước, nhưng chúng tôi có thể kiểm tra xem cụ thể $\frac{x}{y}$ liệu $\frac{x}{y} < \frac{p}{q}$.

Biết điều này, chúng ta có thể mô phỏng tìm kiếm trên cây Stern-Brocot bằng cách duy trì các ranh giới hiện tại $\frac{p_{k-1}}{q_{k-1}}$ và $\frac{p_k}{q_k}$, và tìm từng $a_k$ thông qua tìm kiếm nhị phân. Thuật toán sau đó kỹ thuật hơn một chút và có khả năng có độ phức tạp $O(\log^2(x+y))$, trừ khi công thức bài toán cho phép bạn tìm $a_k$ nhanh hơn (ví dụ, sử dụng `floor` của một biểu thức đã biết).

## Dãy Farey (Farey Sequence) {: #farey-sequence}

Dãy Farey bậc $n$ là dãy các phân số đã sắp xếp nằm giữa $0$ và $1$ có mẫu số không vượt quá $n$.

Các chuỗi được đặt theo tên của nhà địa chất học người Anh John Farey, người vào năm 1816 đã phỏng đoán rằng bất kỳ phân số nào trong chuỗi Farey đều là trung gian của các phân số lân cận của nó. Điều này đã được chứng minh một thời gian sau đó bởi Cauchy, nhưng độc lập với cả hai người họ, nhà toán học Haros đã đi đến kết luận gần như tương tự vào năm 1802.

Các chuỗi Farey có nhiều thuộc tính thú vị của riêng chúng, nhưng mối liên hệ với cây Stern-Brocot là rõ ràng nhất. Trên thực tế, các chuỗi Farey có thể thu được bằng cách cắt tỉa các nhánh khỏi cây.

Từ thuật toán xây dựng cây Stern-Brocot, chúng ta có được một thuật toán cho các chuỗi Farey. Bắt đầu với danh sách các phân số $\frac{0}{1}, \frac{1}{0}$. Ở mỗi lần lặp tiếp theo, chỉ chèn trung gian nếu mẫu số không vượt quá $n$. Tại một thời điểm nào đó, danh sách sẽ ngừng thay đổi và chuỗi Farey mong muốn sẽ được tìm thấy.

### Độ dài của dãy Farey (Length of a Farey Sequence) {: #length-of-a-farey-sequence}

Một dãy Farey bậc $n$ chứa tất cả các phần tử của dãy Farey bậc $n-1$ cũng như tất cả các phân số tối giản có mẫu số $n$, nhưng vế sau chỉ là phi hàm Euler $\varphi(n)$. Vì vậy, độ dài $L_n$ của chuỗi Farey thứ tự $n$ là

$$
    L_n = L_{n-1} + \varphi(n)
$$

hoặc tương đương, bằng cách làm sáng tỏ đệ quy chúng ta nhận được

$$
    L_n = 1 + \sum_{k=1}^n \varphi(k).
$$
