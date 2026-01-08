---
tags:
    - Translated
e_maxx_link: binary_search
---

# Tìm kiếm nhị phân (Binary search) {: #binary-search}

**Tìm kiếm nhị phân** là một phương pháp cho phép tìm kiếm thứ gì đó nhanh hơn bằng cách chia khoảng tìm kiếm làm hai. Ứng dụng phổ biến nhất của nó là tìm kiếm các giá trị trong các mảng đã phân loại, tuy nhiên ý tưởng chia nhỏ rất quan trọng trong nhiều tác vụ điển hình khác.

## Tìm kiếm trong mảng đã sắp xếp (Search in sorted arrays) {: #search-in-sorted-arrays}

Vấn đề điển hình nhất dẫn đến tìm kiếm nhị phân như sau. Bạn được cho một mảng đã sắp xếp $A_0 \leq A_1 \leq \dots \leq A_{n-1}$, hãy kiểm tra xem $k$ có hiện diện trong chuỗi hay không. Giải pháp đơn giản nhất sẽ là kiểm tra từng phần tử một và so sánh nó với $k$ (cái gọi là tìm kiếm tuyến tính). Cách tiếp cận này hoạt động trong $O(n)$, nhưng không tận dụng thực tế là mảng đã được sắp xếp.

<center>
<img src="https://upload.wikimedia.org/wikipedia/commons/8/83/Binary_Search_Depiction.svg" width="800px">
<br>
<i>Tìm kiếm nhị phân giá trị $7$ trong một mảng</i>.
<br>
<i><a href="https://commons.wikimedia.org/wiki/File:Binary_Search_Depiction.svg">Hình ảnh</a> bởi <a href="https://commons.wikimedia.org/wiki/User:AlwaysAngry">AlwaysAngry</a> được phân phối dưới giấy phép <a href="https://creativecommons.org/licenses/by-sa/4.0/deed.en">CC BY-SA 4.0</a></i>.
</center>

Bây giờ giả sử rằng chúng ta biết hai chỉ số $L < R$ sao cho $A_L \leq k \leq A_R$. Bởi vì mảng được sắp xếp, chúng ta có thể suy luận rằng $k$ hoặc xảy ra giữa $A_L, A_{L+1}, \dots, A_R$ hoặc hoàn toàn không xảy ra trong mảng. Nếu chúng ta chọn một chỉ số $M$ tùy ý sao cho $L < M < R$ và kiểm tra xem $k$ nhỏ hơn hay lớn hơn $A_M$. Chúng tôi có hai trường hợp có thể xảy ra:

1. $A_L \leq k \leq A_M$. Trong trường hợp này, chúng tôi giảm bài toán từ $[L, R]$ xuống $[L, M]$;
1. $A_M \leq k \leq A_R$. Trong trường hợp này, chúng tôi giảm bài toán từ $[L, R]$ xuống $[M, R]$.

Khi không thể chọn $M$, nghĩa là khi $R = L + 1$, chúng ta so sánh trực tiếp $k$ với $A_L$ và $A_R$. Mặt khác, chúng ta muốn chọn $M$ theo cách mà nó làm giảm đoạn hoạt động thành một phần tử duy nhất nhanh nhất có thể _trong trường hợp xấu nhất_.

Vì trong trường hợp xấu nhất, chúng ta sẽ luôn giảm xuống đoạn lớn hơn của $[L, M]$ và $[M, R]$. Do đó, trong kịch bản trường hợp xấu nhất, mức giảm sẽ là từ $R-L$ xuống $\max(M-L, R-M)$. Để giảm thiểu giá trị này, chúng ta nên chọn $M \approx \frac{L+R}{2}$, sau đó

$$
M-L \approx \frac{R-L}{2} \approx R-M.
$$

Nói cách khác, từ góc độ kịch bản trường hợp xấu nhất, tối ưu nhất là luôn chọn $M$ ở giữa $[L, R]$ và chia đôi nó. Do đó, đoạn hoạt động giảm một nửa trên mỗi bước cho đến khi nó có kích thước $1$. Vì vậy, nếu quá trình cần $h$ bước, cuối cùng nó sẽ giảm sự khác biệt giữa $R$ và $L$ từ $R-L$ xuống $\frac{R-L}{2^h} \approx 1$, cho chúng ta phương trình $2^h \approx R-L$.

Lấy $\log_2$ ở cả hai vế, chúng ta nhận được $h \approx \log_2(R-L) \in O(\log n)$.

Số lượng các bước logarit tốt hơn nhiều so với tìm kiếm tuyến tính. Ví dụ, đối với $n \approx 2^{20} \approx 10^6$, bạn sẽ cần thực hiện khoảng một triệu thao tác để tìm kiếm tuyến tính, nhưng chỉ khoảng $20$ thao tác với tìm kiếm nhị phân.

### Cận dưới và cận trên (Lower bound and upper bound) {: #lower-bound-and-upper-bound}

Thường thuận tiện để tìm vị trí của phần tử đầu tiên lớn hơn hoặc bằng $k$ (gọi là cận dưới - **lower bound** của $k$ trong mảng) hoặc vị trí của phần tử đầu tiên lớn hơn $k$ (gọi là cận trên - **upper bound** của $k$) thay vì vị trí chính xác của phần tử.

Cùng với nhau, cận dưới và cận trên tạo ra một nửa khoảng có thể rỗng của các phần tử mảng bằng $k$. Để kiểm tra xem $k$ có hiện diện trong mảng hay không, chỉ cần tìm cận dưới của nó và kiểm tra xem phần tử tương ứng có bằng $k$ hay không.

### Cài đặt (Implementation) {: #implementation}

Lời giải thích ở trên cung cấp một mô tả sơ bộ về thuật toán. Đối với các chi tiết cài đặt, chúng ta cần phải chính xác hơn.

Chúng tôi sẽ duy trì một cặp $L < R$ sao cho $A_L \leq k < A_R$. Có nghĩa là khoảng tìm kiếm đang hoạt động là $[L, R)$. Chúng tôi sử dụng nửa khoảng ở đây thay vì một đoạn $[L, R]$ vì hóa ra nó yêu cầu ít công việc với trường hợp biên hơn.

Khi $R = L+1$, chúng ta có thể suy ra từ các định nghĩa ở trên rằng $R$ là cận trên của $k$. Sẽ thuận tiện khi khởi tạo $R$ với chỉ số ngay sau khi kết thúc, tức là $R=n$ và $L$ với chỉ số ngay trước khi bắt đầu, tức là $L=-1$. Sẽ ổn miễn là chúng ta không bao giờ đánh giá $A_L$ và $A_R$ trong thuật toán của mình trực tiếp, về mặt hình thức coi nó là $A_L = -\infty$ và $A_R = +\infty$.

Cuối cùng, để cụ thể về giá trị của $M$ chúng ta chọn, chúng ta sẽ gắn bó với $M = \lfloor \frac{L+R}{2} \rfloor$.

Sau đó, việc triển khai có thể trông giống như thế này:

```cpp
// mảng đã sắp xếp được lưu trữ dưới dạng a[0], a[1], ..., a[n-1]
int l = -1, r = n;
while (r - l > 1) {
    int m = (l + r) / 2;
    if (k < a[m]) {
        r = m; // a[l] <= k < a[m] <= a[r]
    } else {
        l = m; // a[l] <= a[m] <= k < a[r]
    }
}
```

Trong quá trình thực thi thuật toán, chúng ta không bao giờ đánh giá $A_L$ cũng như $A_R$, vì $L < M < R$. Cuối cùng, $L$ sẽ là chỉ số của phần tử cuối cùng không lớn hơn $k$ (hoặc $-1$ nếu không có phần tử nào như vậy) và $R$ sẽ là chỉ số của phần tử đầu tiên lớn hơn $k$ (hoặc $n$ nếu không có phần tử nào như vậy).

**Lưu ý.** Việc tính toán `m` là `m = (r + l) / 2` có thể dẫn đến tràn số nếu `l` và `r` là hai số nguyên dương, và lỗi này đã tồn tại khoảng 9 năm trong JDK như được mô tả trong [bài đăng trên blog](https://ai.googleblog.com/2006/06/extra-extra-read-all-about-it-nearly.html). Một số cách tiếp cận thay thế bao gồm ví dụ: viết `m = l + (r - l) / 2` luôn hoạt động đối với số nguyên dương `l` và `r`, nhưng vẫn có thể tràn nếu `l` là một số âm. Nếu bạn sử dụng C++20, nó cung cấp một giải pháp thay thế dưới dạng `m = std::midpoint(l, r)` luôn hoạt động chính xác.

## Tìm kiếm trên vị từ tùy ý (Search on arbitrary predicate) {: #search-on-arbitrary-predicate}

Cho $f : \{0,1,\dots, n-1\} \to \{0, 1\}$ là một hàm boolean được xác định trên $0,1,\dots,n-1$ sao cho nó tăng đơn điệu, tức là

$$
f(0) \leq f(1) \leq \dots \leq f(n-1).
$$

Tìm kiếm nhị phân, theo cách được mô tả ở trên, tìm phân hoạch của mảng theo vị từ $f(M)$, giữ giá trị boolean của biểu thức $k < A_M$.
Có thể sử dụng vị từ đơn điệu tùy ý thay vì $k < A_M$. Nó đặc biệt hữu ích khi việc tính toán $f(k)$ đòi hỏi quá nhiều thời gian để thực sự tính toán nó cho mọi giá trị có thể.
Nói cách khác, tìm kiếm nhị phân tìm chỉ số duy nhất $L$ sao cho $f(L) = 0$ và $f(R)=f(L+1)=1$ nếu tồn tại một _điểm chuyển tiếp_ như vậy, hoặc cho chúng ta $L = n-1$ nếu $f(0) = \dots = f(n-1) = 0$ hoặc $L = -1$ nếu $f(0) = \dots = f(n-1) = 1$.

Bằng chứng về tính chính xác giả sử có một điểm chuyển tiếp tồn tại, tức là $f(0)=0$ và $f(n-1)=1$: Việc triển khai duy trì _Bất biến vòng lặp_ (_loop invariant_) $f(l)=0, f(r)=1$. Khi $r - l > 1$, việc chọn $m$ có nghĩa là $r-l$ sẽ luôn giảm. Vòng lặp kết thúc khi $r - l = 1$, cho chúng ta điểm chuyển tiếp mong muốn của mình.

```cpp
// f(i) là một hàm boolean sao cho f(0) <= ... <= f(n-1)
int l = -1, r = n;
while (r - l > 1) {
    int m = (l + r) / 2;
    if (f(m)) {
        r = m; // 0 = f(l) < f(m) = 1
    } else {
        l = m; // 0 = f(m) < f(r) = 1
    }
}
```

### Tìm kiếm nhị phân trên câu trả lời (Binary search on the answer) {: #binary-search-on-the-answer}

Tình huống như vậy thường xảy ra khi chúng ta được yêu cầu tính toán một số giá trị, nhưng chúng ta chỉ có khả năng kiểm tra xem giá trị này có ít nhất là $i$ hay không. Ví dụ, bạn được cho một mảng $a_1,\dots,a_n$ và bạn được yêu cầu tìm tổng trung bình sàn lớn nhất

$$
\left \lfloor \frac{a_l + a_{l+1} + \dots + a_r}{r-l+1} \right\rfloor
$$

trong số tất cả các cặp $l,r$ khả thi sao cho $r-l \geq x$. Một trong những cách đơn giản để giải quyết vấn đề này là kiểm tra xem câu trả lời có ít nhất là $\lambda$ hay không, nghĩa là nếu có một cặp $l, r$ sao cho điều sau đây là đúng:

$$
\frac{a_l + a_{l+1} + \dots + a_r}{r-l+1} \geq \lambda.
$$

Tương đương, nó viết lại thành

$$
(a_l - \lambda) + (a_{l+1} - \lambda) + \dots + (a_r - \lambda) \geq 0,
$$

vì vậy bây giờ chúng ta cần kiểm tra xem có một mảng con của một mảng mới $a_i - \lambda$ có độ dài ít nhất $x+1$ với tổng không âm hay không, điều này có thể thực hiện được với một số tổng tiền tố.

## Tìm kiếm liên tục (Continuous search) {: #continuous-search}

Cho $f : \mathbb R \to \mathbb R$ là một hàm giá trị thực liên tục trên một đoạn $[L, R]$.

Không mất tính tổng quát giả sử rằng $f(L) \leq f(R)$. Từ [định lý giá trị trung gian](https://en.wikipedia.org/wiki/Intermediate_value_theorem) suy ra rằng đối với bất kỳ $y \in [f(L), f(R)]$ đều có $x \in [L, R]$ sao cho $f(x) = y$. Lưu ý rằng, không giống như các đoạn trước, hàm _không_ bắt buộc phải đơn điệu.

Giá trị $x$ có thể được xấp xỉ lên đến $\pm\delta$ trong thời gian $O\left(\log \frac{R-L}{\delta}\right)$ cho bất kỳ giá trị cụ thể nào của $\delta$. Ý tưởng về cơ bản là giống nhau, nếu chúng ta lấy $M \in (L, R)$ thì chúng ta có thể giảm khoảng tìm kiếm xuống còn $[L, M]$ hoặc $[M, R]$ tùy thuộc vào việc $f(M)$ có lớn hơn $y$ hay không. Một ví dụ phổ biến ở đây là tìm nghiệm của đa thức bậc lẻ.

Ví dụ, gọi $f(x)=x^3 + ax^2 + bx + c$. Khi đó $f(L) \to -\infty$ và $f(R) \to +\infty$ với $L \to -\infty$ và $R \to +\infty$. Có nghĩa là luôn luôn có thể tìm thấy $L$ đủ nhỏ và $R$ đủ lớn để $f(L) < 0$ và $f(R) > 0$. Sau đó, có thể tìm thấy bằng tìm kiếm nhị phân khoảng thời gian nhỏ tùy ý chứa $x$ sao cho $f(x)=0$.

## Tìm kiếm với lũy thừa của 2 (Search with powers of 2) {: #search-with-powers-of-2}

Một cách đáng chú ý khác để thực hiện tìm kiếm nhị phân là thay vì duy trì một phân đoạn hoạt động, hãy duy trì con trỏ hiện tại $i$ và lũy thừa hiện tại $k$. Con trỏ bắt đầu tại $i=L$ và sau đó trên mỗi lần lặp, người ta kiểm tra vị từ tại điểm $i+2^k$. Nếu vị từ vẫn là $0$, con trỏ được nâng cao từ $i$ đến $i+2^k$, nếu không nó vẫn giữ nguyên, thì lũy thừa $k$ giảm đi $1$.

Mô hình này được sử dụng rộng rãi trong các nhiệm vụ xung quanh cây, chẳng hạn như tìm tổ tiên chung thấp nhất của hai đỉnh hoặc tìm tổ tiên của một đỉnh cụ thể có chiều cao nhất định. Nó cũng có thể được điều chỉnh để ví dụ: tìm phần tử khác không thứ $k$ trong cây Fenwick.

## Bài tập (Practice Problems) {: #practice-problems}

* [LeetCode -  Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)
* [LeetCode -  Search Insert Position](https://leetcode.com/problems/search-insert-position/)
* [LeetCode -  First Bad Version](https://leetcode.com/problems/first-bad-version/)
* [LeetCode -  Valid Perfect Square](https://leetcode.com/problems/valid-perfect-square/)
* [LeetCode -  Find Peak Element](https://leetcode.com/problems/find-peak-element/)
* [LeetCode -  Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)
* [LeetCode -  Find Right Interval](https://leetcode.com/problems/find-right-interval/)
* [Codeforces - Interesting Drink](https://codeforces.com/problemset/problem/706/B/)
* [Codeforces - Magic Powder - 1](https://codeforces.com/problemset/problem/670/D1)
* [Codeforces - Another Problem on Strings](https://codeforces.com/problemset/problem/165/C)
* [Codeforces - Frodo and pillows](https://codeforces.com/problemset/problem/760/B)
* [Codeforces - GukiZ hates Boxes](https://codeforces.com/problemset/problem/551/C)
* [Codeforces - Enduring Exodus](https://codeforces.com/problemset/problem/645/C)
* [Codeforces - Chip 'n Dale Rescue Rangers](https://codeforces.com/problemset/problem/590/B)
