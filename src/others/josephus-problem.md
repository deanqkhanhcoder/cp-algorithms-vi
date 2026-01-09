---
tags:
  - Translated
e_maxx_link: joseph_problem
---

# Bài toán Josephus (Josephus Problem) {: #josephus-problem}

## Đề bài (Statement) {: #statement}

Chúng ta được cho các số tự nhiên $n$ và $k$.
Tất cả các số tự nhiên từ $1$ đến $n$ được viết theo một vòng tròn. 
Đầu tiên, đếm số thứ $k$ bắt đầu từ số đầu tiên và xóa nó.
Sau đó $k$ số được đếm bắt đầu từ số tiếp theo và số thứ $k$ lại bị loại bỏ, v.v.
Quá trình dừng lại khi còn lại một số.
Yêu cầu tìm số cuối cùng.

Nhiệm vụ này được đặt ra bởi **Flavius Josephus** vào thế kỷ thứ 1 (mặc dù trong một công thức hẹp hơn một chút: đối với $k = 2$).

Bài toán này có thể được giải quyết bằng cách mô hình hóa thủ tục.
Mô hình hóa Brute force sẽ hoạt động $O(n^{2})$. Sử dụng [Segment Tree](../data_structures/segment-tree.md), chúng ta có thể cải thiện nó lên $O(n \log n)$.
Tuy nhiên, chúng tôi muốn một cái gì đó tốt hơn.

## Mô hình hóa giải pháp $O(n)$ (Modeling a $O(n)$ solution) {: #modeling-a-o-n-solution}

Chúng tôi sẽ cố gắng tìm một mẫu biểu thị câu trả lời cho bài toán $J_{n, k}$ thông qua giải pháp của các bài toán trước đó.

Sử dụng mô hình hóa brute force, chúng ta có thể xây dựng một bảng giá trị, ví dụ, như sau:

$$\begin{array}{ccccccccccc}
n\setminus k & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 & 10 \\
1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 \\
2 & 2 & 1 & 2 & 1 & 2 & 1 & 2 & 1 & 2 & 1 \\
3 & 3 & 3 & 2 & 2 & 1 & 1 & 3 & 3 & 2 & 2 \\
4 & 4 & 1 & 1 & 2 & 2 & 3 & 2 & 3 & 3 & 4 \\
5 & 5 & 3 & 4 & 1 & 2 & 4 & 4 & 1 & 2 & 4 \\
6 & 6 & 5 & 1 & 5 & 1 & 4 & 5 & 3 & 5 & 2 \\
7 & 7 & 7 & 4 & 2 & 6 & 3 & 5 & 4 & 7 & 5 \\
8 & 8 & 1 & 7 & 6 & 3 & 1 & 4 & 4 & 8 & 7 \\
9 & 9 & 3 & 1 & 1 & 8 & 7 & 2 & 3 & 8 & 8 \\
10 & 10 & 5 & 4 & 5 & 3 & 3 & 9 & 1 & 7 & 8 \\
\end{array}$$

Và ở đây chúng ta có thể thấy rõ ràng **mẫu** sau:

$$J_{n,k} = \left( (J_{n-1,k} + k - 1) \bmod n \right) + 1$$

$$J_{1,k} = 1$$

Ở đây, chỉ mục bắt đầu từ 1 tạo ra một công thức hơi lộn xộn; nếu thay vào đó bạn đánh số các vị trí từ 0, bạn sẽ nhận được một công thức rất thanh lịch:

$$J_{n,k} = (J_{n-1,k} + k) \bmod n$$

Vì vậy, chúng tôi đã tìm thấy một giải pháp cho bài toán Josephus, hoạt động trong $O(n)$ phép toán.

## Cài đặt (Implementation) {: #implementation}

**Cài đặt đệ quy** đơn giản (trong chỉ mục bắt đầu từ 1)
```cpp title="josephus_rec"
int josephus(int n, int k) {
    return n > 1 ? (josephus(n-1, k) + k - 1) % n + 1 : 1;
}
```

**Dạng không đệ quy** :
```cpp title="josephus_iter"
int josephus(int n, int k) {
    int res = 0;
    for (int i = 1; i <= n; ++i)
  	  res = (res + k) % i;
    return res + 1;
}
```

Công thức này cũng có thể được tìm thấy bằng giải tích.
Một lần nữa ở đây chúng ta giả sử chỉ mục bắt đầu từ 0.
Sau khi chúng tôi xóa số đầu tiên, chúng tôi còn lại $n-1$ số.
Khi chúng tôi lặp lại thủ tục, chúng tôi sẽ bắt đầu với số ban đầu có chỉ số $k \bmod n$.
$J_{n-1, k}$ sẽ là câu trả lời cho vòng tròn còn lại, nếu chúng ta bắt đầu đếm tại $0$, nhưng vì chúng ta thực sự bắt đầu với $k$ nên chúng ta có $J_{n, k} = (J_{n-1,k} + k) \ \bmod n$.

## Mô hình hóa giải pháp $O(k \log n)$ (Modeling a $O(k \log n)$ solution) {: #modeling-a-o-k-log-n-solution}

Đối với $k$ tương đối nhỏ, chúng ta có thể đưa ra giải pháp tốt hơn giải pháp đệ quy ở trên trong $O(n)$.
Nếu $k$ nhỏ hơn nhiều so với $n$, thì chúng ta có thể xóa nhiều số ($\lfloor \frac{n}{k} \rfloor$) trong một lần chạy mà không cần lặp lại.
Sau đó, chúng ta còn lại $n - \lfloor \frac{n}{k} \rfloor$ số, và chúng ta bắt đầu với số thứ $(\lfloor \frac{n}{k} \rfloor \cdot k)$.
Vì vậy, chúng ta phải dịch chuyển từng đó.
Chúng ta có thể nhận thấy rằng $\lfloor \frac{n}{k} \rfloor \cdot k$ chỉ đơn giản là $-n \bmod k$.
Và bởi vì chúng ta đã xóa mọi số thứ $k$, chúng ta phải thêm số lượng các số mà chúng ta đã xóa trước chỉ mục kết quả.
Cái mà chúng ta có thể tính toán bằng cách chia chỉ mục kết quả cho $k - 1$.

Ngoài ra, chúng ta cần xử lý trường hợp khi $n$ trở nên nhỏ hơn $k$. Trong trường hợp này, tối ưu hóa ở trên sẽ gây ra một vòng lặp vô hạn.

**Cài đặt** (để thuận tiện trong chỉ mục bắt đầu từ 0):
```cpp title="josephus_fast0"
int josephus(int n, int k) {
    if (n == 1)
        return 0;
    if (k == 1)
        return n-1;
    if (k > n)
        return (josephus(n-1, k) + k) % n;
    int cnt = n / k;
    int res = josephus(n - cnt, k);
    res -= n % k;
    if (res < 0)
        res += n;
    else
        res += res / (k - 1);
    return res;
}
```

Hãy ước tính **độ phức tạp** của thuật toán này. Lưu ý ngay rằng trường hợp $n < k$ được phân tích bằng giải pháp cũ, sẽ hoạt động trong trường hợp này cho $O(k)$. Bây giờ hãy xem xét chính thuật toán. Trên thực tế, sau mỗi lần lặp, thay vì $n$ số, chúng ta còn lại $n \left( 1 - \frac{1}{k} \right)$ số, vì vậy tổng số lần lặp $x$ của thuật toán có thể được tìm thấy gần đúng từ phương trình sau:

$$ n \left(1 - \frac{1}{k} \right) ^ x = 1, $$

lấy logarit ở cả hai vế, chúng ta thu được:

$$\ln n + x \ln \left(1 - \frac{1}{k} \right) = 0,$$ 
$$x = - \frac{\ln n}{\ln \left(1 - \frac{1}{k} \right)},$$

sử dụng khai triển của logarit thành chuỗi Taylor, chúng ta thu được ước tính gần đúng:

$$x \approx k \ln n$$

Do đó, độ phức tạp của thuật toán thực sự là $O (k \log n)$.

## Giải pháp giải tích cho $k = 2$ (Analytical solution for $k = 2$) {: #analytical-solution-for-k-2}

Trong trường hợp cụ thể này (trong đó nhiệm vụ này được đặt ra bởi Josephus Flavius), vấn đề được giải quyết dễ dàng hơn nhiều.

Trong trường hợp $n$ chẵn, chúng ta nhận được rằng tất cả các số chẵn sẽ bị gạch bỏ, và sau đó sẽ còn lại một vấn đề cho $\frac{n}{2}$, sau đó câu trả lời cho $n$ sẽ thu được từ câu trả lời cho $\frac{n}{2}$ bằng cách nhân với hai và trừ đi một (bằng cách dịch chuyển vị trí):

$$ J_{2n, 2} = 2 J_{n, 2} - 1 $$

Tương tự, trong trường hợp $n$ lẻ, tất cả các số chẵn sẽ bị gạch bỏ, sau đó là số đầu tiên, và vấn đề cho $\frac{n-1}{2}$ sẽ vẫn còn, và tính đến sự dịch chuyển vị trí, chúng ta thu được công thức thứ hai:

$$J_{2n+1,2} = 2 J_{n, 2} + 1 $$

Chúng ta có thể sử dụng phụ thuộc hồi quy này trực tiếp trong quá trình triển khai của mình. Mẫu này có thể được dịch sang một dạng khác: $J_{n, 2}$ đại diện cho một chuỗi tất cả các số lẻ, "khởi động lại" từ một bất cứ khi nào $n$ trở thành lũy thừa của hai. Điều này có thể được viết dưới dạng một công thức duy nhất:

$$J_{n, 2} = 1 + 2 \left(n-2^{\lfloor \log_2 n \rfloor} \right)$$

## Giải pháp giải tích cho $k > 2$ (Analytical solution for $k > 2$) {: #analytical-solution-for-k-2_1}

Mặc dù dạng bài toán đơn giản và có một số lượng lớn các bài báo về vấn đề này và các vấn đề liên quan, nhưng cho đến nay vẫn chưa tìm thấy một biểu diễn giải tích đơn giản nào cho giải pháp của bài toán Josephus. Đối với $k$ nhỏ, một số công thức được đưa ra, nhưng dường như tất cả chúng đều khó áp dụng trong thực tế (ví dụ, xem Halbeisen, Hungerbuhler "The Josephus Problem" và Odlyzko, Wilf "Functional iteration and the Josephus problem").
