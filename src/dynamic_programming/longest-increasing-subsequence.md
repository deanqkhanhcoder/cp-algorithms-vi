---
tags:
  - Translated
e_maxx_link: longest_increasing_subseq_log
---

# Dãy con tăng dài nhất (Longest increasing subsequence) {: #longest-increasing-subsequence}

Chúng ta được cho một mảng với $n$ số: $a[0 \dots n-1]$.
Nhiệm vụ là tìm dãy con tăng nghiêm ngặt dài nhất trong $a$.

Một cách chính thức, chúng ta tìm kiếm dãy các chỉ số dài nhất $i_1, \dots i_k$ sao cho

$$i_1 < i_2 < \dots < i_k,\quad
a[i_1] < a[i_2] < \dots < a[i_k]$$

Trong bài viết này, chúng ta thảo luận về nhiều thuật toán để giải quyết nhiệm vụ này.
Ngoài ra, chúng ta sẽ thảo luận về một số bài toán khác, có thể được quy về bài toán này.

## Giải pháp trong $O(n^2)$ với quy hoạch động (Solution in O(n^2) with dynamic programming) {: #solution-in-o-n-2-with-dynamic-programming data-toc-label="Solution in O(n^2) with dynamic programming"}

Quy hoạch động (Dynamic programming) là một kỹ thuật rất tổng quát cho phép giải quyết một lớp bài toán khổng lồ.
Ở đây chúng ta áp dụng kỹ thuật cho nhiệm vụ cụ thể của mình.

Đầu tiên, chúng ta sẽ chỉ tìm kiếm **độ dài** của dãy con tăng dài nhất, và chỉ sau đó tìm hiểu cách khôi phục chính dãy con đó.

### Tìm độ dài (Finding the length) {: #finding-the-length}

Để hoàn thành nhiệm vụ này, chúng ta định nghĩa một mảng $d[0 \dots n-1]$, trong đó $d[i]$ là độ dài của dãy con tăng dài nhất kết thúc tại phần tử ở chỉ số $i$.

!!! example "Ví dụ"

    $$\begin{array}{ll}
    a &= \{8, 3, 4, 6, 5, 2, 0, 7, 9, 1\} \\
    d &= \{1, 1, 2, 3, 3, 1, 1, 4, 5, 2\}
    \end{array}$$

    Dãy con tăng dài nhất kết thúc tại chỉ số 4 là $\{3, 4, 5\}$ với độ dài là 3, dãy dài nhất kết thúc tại chỉ số 8 là $\{3, 4, 5, 7, 9\}$ hoặc $\{3, 4, 6, 7, 9\}$, cả hai đều có độ dài 5, và dãy dài nhất kết thúc tại chỉ số 9 là $\{0, 1\}$ có độ dài 2.

Chúng ta sẽ tính toán mảng này dần dần: đầu tiên $d[0]$, sau đó $d[1]$, v.v.
Sau khi mảng này được tính toán, câu trả lời cho bài toán sẽ là giá trị lớn nhất trong mảng $d[]$.

Vì vậy, hãy để chỉ số hiện tại là $i$.
Tức là chúng ta muốn tính giá trị $d[i]$ và tất cả các giá trị trước đó $d[0], \dots, d[i-1]$ đã được biết.
Sau đó, có hai tùy chọn:

-   $d[i] = 1$: dãy con yêu cầu chỉ bao gồm phần tử $a[i]$.

-   $d[i] > 1$: Dãy con sẽ kết thúc tại $a[i]$, và ngay trước nó sẽ là một số $a[j]$ với $j < i$ và $a[j] < a[i]$.

    Dễ thấy rằng, dãy con kết thúc trong $a[j]$ chính nó sẽ là một trong những dãy con tăng dài nhất kết thúc trong $a[j]$.
    Số $a[i]$ chỉ mở rộng dãy con tăng dài nhất đó thêm một số.

    Do đó, chúng ta có thể chỉ cần lặp lại tất cả $j < i$ với $a[j] < a[i]$, và lấy dãy dài nhất mà chúng ta nhận được bằng cách thêm $a[i]$ vào dãy con tăng dài nhất kết thúc trong $a[j]$.
    Dãy con tăng dài nhất kết thúc trong $a[j]$ có độ dài $d[j]$, mở rộng nó thêm một cho độ dài $d[j] + 1$.
  
    $$d[i] = \max_{\substack{j < i \\\\ a[j] < a[i]}} \left(d[j] + 1\right)$$

Nếu chúng ta kết hợp hai trường hợp này, chúng ta nhận được câu trả lời cuối cùng cho $d[i]$:

$$d[i] = \max\left(1, \max_{\substack{j < i \\\\ a[j] < a[i]}} \left(d[j] + 1\right)\right)$$

### Cài đặt (Implementation) {: #implementation}

Dưới đây là một cài đặt của thuật toán được mô tả ở trên, tính toán độ dài của dãy con tăng dài nhất.
```cpp title="lis_n2"
int lis(vector<int> const& a) {
    int n = a.size();
    vector<int> d(n, 1);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < i; j++) {
            if (a[j] < a[i])
                d[i] = max(d[i], d[j] + 1);
        }
    }

    int ans = d[0];
    for (int i = 1; i < n; i++) {
        ans = max(ans, d[i]);
    }
    return ans;
}
```

### Khôi phục dãy con (Restoring the subsequence) {: #restoring-the-subsequence}

Cho đến nay, chúng ta chỉ học cách tìm độ dài của dãy con, nhưng không biết cách tìm chính dãy con đó.

Để có thể khôi phục dãy con, chúng ta tạo thêm một mảng phụ $p[0 \dots n-1]$ mà chúng ta sẽ tính toán cùng với mảng $d[]$.
$p[i]$ sẽ là chỉ số $j$ của phần tử đứng thứ hai từ cuối lên trong dãy con tăng dài nhất kết thúc bằng $i$.
Nói cách khác, chỉ số $p[i]$ chính là chỉ số $j$ mà tại đó giá trị cao nhất $d[i]$ đã đạt được.
Mảng phụ $p[]$ này theo một nghĩa nào đó trỏ đến các tổ tiên.

Sau đó, để suy ra dãy con, chúng ta chỉ cần bắt đầu tại chỉ số $i$ với $d[i]$ cực đại, và đi theo các tổ tiên cho đến khi chúng ta suy ra toàn bộ dãy con, tức là cho đến khi chúng ta đạt đến phần tử có $d[i] = 1$.

### Cài đặt việc khôi phục (Implementation of restoring) {: #implementation-of-restoring}

Chúng ta sẽ thay đổi mã từ các phần trước một chút.
Chúng ta sẽ tính toán mảng $p[]$ cùng với $d[]$, và sau đó tính toán dãy con.

Để thuận tiện, ban đầu chúng ta gán các tổ tiên với $p[i] = -1$.
Đối với các phần tử có $d[i] = 1$, giá trị tổ tiên sẽ vẫn là $-1$, điều này sẽ thuận tiện hơn một chút để khôi phục dãy con.
```cpp title="lis_n2_restore"
vector<int> lis(vector<int> const& a) {
    int n = a.size();
    vector<int> d(n, 1), p(n, -1);
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < i; j++) {
            if (a[j] < a[i] && d[i] < d[j] + 1) {
                d[i] = d[j] + 1;
                p[i] = j;
            }
        }
    }

    int ans = d[0], pos = 0;
    for (int i = 1; i < n; i++) {
        if (d[i] > ans) {
            ans = d[i];
            pos = i;
        }
    }

    vector<int> subseq;
    while (pos != -1) {
        subseq.push_back(a[pos]);
        pos = p[pos];
    }
    reverse(subseq.begin(), subseq.end());
    return subseq;
}
```

### Cách thay thế để khôi phục dãy con (Alternative way of restoring the subsequence) {: #alternative-way-of-restoring-the-subsequence}

Cũng có thể khôi phục dãy con mà không cần mảng phụ $p[]$.
Chúng ta có thể đơn giản tính toán lại giá trị hiện tại của $d[i]$ và cũng xem mức tối đa đã đạt được như thế nào.

Phương pháp này dẫn đến mã dài hơn một chút, nhưng đổi lại chúng ta tiết kiệm được một số bộ nhớ.

## Giải pháp trong $O(n \log n)$ với quy hoạch động và tìm kiếm nhị phân (Solution in O(n log n) with dynamic programming and binary search) {: #solution-in-o-n-log-n-with-dynamic-programming-and-binary-search data-toc-label="Solution in O(n log n) with dynamic programming and binary search"}

Để có được giải pháp nhanh hơn cho bài toán, chúng ta xây dựng một giải pháp quy hoạch động khác chạy trong $O(n^2)$, và sau đó cải thiện nó thành $O(n \log n)$.

Chúng ta sẽ sử dụng mảng quy hoạch động $d[0 \dots n]$.
Lần này $d[l]$ không tương ứng với phần tử $a[i]$ hoặc tiền tố của mảng.
$d[l]$ sẽ là phần tử nhỏ nhất mà tại đó một dãy con tăng có độ dài $l$ kết thúc.

Ban đầu chúng ta giả sử $d[0] = -\infty$ và đối với tất cả các độ dài khác $d[l] = \infty$.

Chúng ta sẽ lại xử lý dần dần các số, đầu tiên $a[0]$, sau đó $a[1]$, v.v., và trong mỗi bước duy trì mảng $d[]$ sao cho nó được cập nhật.

!!! example "Ví dụ"

    Cho mảng $a = \{8, 3, 4, 6, 5, 2, 0, 7, 9, 1\}$, đây là tất cả các tiền tố của chúng và mảng quy hoạch động của chúng.
    Lưu ý rằng các giá trị của mảng không phải lúc nào cũng thay đổi ở cuối.

    $$
    \begin{array}{ll}
    \text{prefix} = \{\} &\quad d = \{-\infty, \infty, \dots\}\\
    \text{prefix} = \{8\} &\quad d = \{-\infty, 8, \infty, \dots\}\\
    \text{prefix} = \{8, 3\} &\quad d = \{-\infty, 3, \infty, \dots\}\\
    \text{prefix} = \{8, 3, 4\} &\quad d = \{-\infty, 3, 4, \infty, \dots\}\\
    \text{prefix} = \{8, 3, 4, 6\} &\quad d = \{-\infty, 3, 4, 6, \infty, \dots\}\\
    \text{prefix} = \{8, 3, 4, 6, 5\} &\quad d = \{-\infty, 3, 4, 5, \infty, \dots\}\\
    \text{prefix} = \{8, 3, 4, 6, 5, 2\} &\quad d = \{-\infty, 2, 4, 5, \infty, \dots \}\\
    \text{prefix} = \{8, 3, 4, 6, 5, 2, 0\} &\quad d = \{-\infty, 0, 4, 5, \infty, \dots \}\\
    \text{prefix} = \{8, 3, 4, 6, 5, 2, 0, 7\} &\quad d = \{-\infty, 0, 4, 5, 7, \infty, \dots \}\\
    \text{prefix} = \{8, 3, 4, 6, 5, 2, 0, 7, 9\} &\quad d = \{-\infty, 0, 4, 5, 7, 9, \infty, \dots \}\\
    \text{prefix} = \{8, 3, 4, 6, 5, 2, 0, 7, 9, 1\} &\quad d = \{-\infty, 0, 1, 5, 7, 9, \infty, \dots \}\\
    \end{array}
    $$

Khi chúng ta xử lý $a[i]$, chúng ta có thể tự hỏi.
Các điều kiện phải là gì, để chúng ta viết số hiện tại $a[i]$ vào mảng $d[0 \dots n]$?

Chúng ta đặt $d[l] = a[i]$, nếu có một dãy con tăng dài nhất có độ dài $l$ kết thúc bằng $a[i]$, và không có dãy con tăng dài nhất nào có độ dài $l$ kết thúc bằng một số nhỏ hơn.
Tương tự như cách tiếp cận trước, nếu chúng ta xóa số $a[i]$ khỏi dãy trình tăng dài nhất có độ dài $l$, chúng ta nhận được một dãy con tăng dài nhất khác có độ dài $l -1$.
Vì vậy, chúng ta muốn mở rộng một dãy con tăng dài nhất có độ dài $l - 1$ bằng số $a[i]$, và rõ ràng dãy con tăng dài nhất có độ dài $l - 1$ kết thúc bằng phần tử nhỏ nhất sẽ hoạt động tốt nhất, nói cách khác dãy có độ dài $l-1$ kết thúc ở phần tử $d[l-1]$.

Có một dãy con tăng dài nhất có độ dài $l - 1$ mà chúng ta có thể mở rộng bằng số $a[i]$, chính xác nếu $d[l-1] < a[i]$.
Vì vậy, chúng ta có thể chỉ cần lặp lại từng độ dài $l$, và kiểm tra xem chúng ta có thể mở rộng một dãy con tăng dài nhất có độ dài $l - 1$ hay không bằng cách kiểm tra các tiêu chí.

Ngoài ra, chúng ta cũng cần kiểm tra, xem liệu chúng ta có thể đã tìm thấy một dãy con tăng dài nhất có độ dài $l$ với một số nhỏ hơn ở cuối hay không.
Vì vậy, chúng ta chỉ cập nhật nếu $a[i] < d[l]$.

Sau khi xử lý tất cả các phần tử của $a[]$, độ dài của dãy con mong muốn là $l$ lớn nhất với $d[l] < \infty$.
```cpp title="lis_method2_n2"
int lis(vector<int> const& a) {
    int n = a.size();
    const int INF = 1e9;
    vector<int> d(n+1, INF);
    d[0] = -INF;

    for (int i = 0; i < n; i++) {
        for (int l = 1; l <= n; l++) {
            if (d[l-1] < a[i] && a[i] < d[l])
                d[l] = a[i];
        }
    }

    int ans = 0;
    for (int l = 0; l <= n; l++) {
        if (d[l] < INF)
            ans = l;
    }
    return ans;
}
```

Bây giờ chúng ta thực hiện hai quan sát quan trọng.

1.  Mảng $d$ sẽ luôn được sắp xếp:
    $d[l-1] < d[l]$ với mọi $i = 1 \dots n$.

    Điều này là tầm thường, vì bạn chỉ cần xóa phần tử cuối cùng khỏi dãy con tăng có độ dài $l$, và bạn nhận được một dãy con tăng có độ dài $l-1$ với số kết thúc nhỏ hơn.

2.  Phần tử $a[i]$ sẽ chỉ cập nhật tối đa một giá trị $d[l]$.

    Điều này theo ngay lập tức từ việc cài đặt ở trên.
    Chỉ có thể có một vị trí trong mảng với $d[l-1] < a[i] < d[l]$.

Do đó, chúng ta có thể tìm phần tử này trong mảng $d[]$ bằng cách sử dụng [tìm kiếm nhị phân](../num_methods/binary-search.md) trong $O(\log n)$.
Trên thực tế, chúng ta có thể chỉ cần tìm trong mảng $d[]$ số đầu tiên lớn hơn hẳn $a[i]$, và chúng ta cố gắng cập nhật phần tử này theo cách tương tự như cài đặt ở trên.

### Cài đặt (Implementation) {: #implementation-1}

Điều này mang lại cho chúng ta cài đặt $O(n \log n)$ cải tiến:
```cpp title="lis_method2_nlogn"
int lis(vector<int> const& a) {
    int n = a.size();
    const int INF = 1e9;
    vector<int> d(n+1, INF);
    d[0] = -INF;

    for (int i = 0; i < n; i++) {
        int l = upper_bound(d.begin(), d.end(), a[i]) - d.begin();
        if (d[l-1] < a[i] && a[i] < d[l])
            d[l] = a[i];
    }

    int ans = 0;
    for (int l = 0; l <= n; l++) {
        if (d[l] < INF)
            ans = l;
    }
    return ans;
}
```

### Khôi phục dãy con (Restoring the subsequence) {: #restoring-the-subsequence-1}

Cũng có thể khôi phục dãy con bằng phương pháp này.
Lần này chúng ta phải duy trì hai mảng phụ.
Một mảng cho chúng ta biết chỉ số của các phần tử trong $d[]$.
Và một lần nữa chúng ta phải tạo một mảng các "tổ tiên" $p[i]$.
$p[i]$ sẽ là chỉ số của phần tử trước đó cho dãy con tối ưu kết thúc bằng phần tử $i$.

Dễ dàng duy trì hai mảng này trong quá trình lặp qua mảng $a[]$ cùng với các tính toán của $d[]$.
Và cuối cùng, không khó để khôi phục dãy con mong muốn bằng cách sử dụng các mảng này.

## Giải pháp trong $O(n \log n)$ với cấu trúc dữ liệu (Solution in O(n log n) with data structures) {: #solution-in-o-n-log-n-with-data-structures data-toc-label="Solution in O(n log n) with data structures"}

Thay vì phương pháp trên để tính dãy con tăng dài nhất trong $O(n \log n)$, chúng ta cũng có thể giải quyết bài toán theo một cách khác: sử dụng một số cấu trúc dữ liệu đơn giản.

Hãy quay lại phương pháp đầu tiên.
Hãy nhớ rằng $d[i]$ là giá trị $d[j] + 1$ với $j < i$ và $a[j] < a[i]$.

Do đó nếu chúng ta định nghĩa thêm một mảng $t[]$ sao cho

$$t[a[i]] = d[i],$$

thì bài toán tính giá trị $d[i]$ tương đương với việc tìm **giá trị lớn nhất trong một tiền tố** của mảng $t[]$:

$$d[i] = \max\left(t[0 \dots a[i] - 1] + 1\right)$$

Bài toán tìm giá trị lớn nhất của một tiền tố của một mảng (thay đổi) là một bài toán tiêu chuẩn có thể được giải quyết bằng nhiều cấu trúc dữ liệu khác nhau.
Ví dụ: chúng ta có thể sử dụng [Segment tree](../data_structures/segment-tree.md) hoặc [Fenwick tree](../data_structures/fenwick.md).

Phương pháp này rõ ràng có một số **nhược điểm**:
về độ dài và độ phức tạp của việc cài đặt, cách tiếp cận này sẽ tệ hơn phương pháp sử dụng tìm kiếm nhị phân.
Ngoài ra, nếu các số đầu vào $a[i]$ đặc biệt lớn, thì chúng ta sẽ phải sử dụng một số thủ thuật, như nén số (tức là đánh số lại chúng từ $0$ đến $n-1$), hoặc sử dụng segment tree động (chỉ tạo các nhánh của cây quan trọng).
Nếu không mức tiêu thụ bộ nhớ sẽ quá cao.

Mặt khác phương pháp này cũng có một số **ưu điểm**:
với phương pháp này bạn không phải suy nghĩ về bất kỳ tính chất phức tạp nào trong giải pháp quy hoạch động.
Và cách tiếp cận này cho phép chúng ta khái quát hóa bài toán rất dễ dàng (xem bên dưới).

## Các nhiệm vụ liên quan (Related tasks) {: #related-tasks}

Dưới đây là một vài bài toán liên quan chặt chẽ đến bài toán tìm dãy con tăng dài nhất.

### Dãy con không giảm dài nhất (Longest non-decreasing subsequence) {: #longest-non-decreasing-subsequence}

Đây thực tế gần như là cùng một bài toán.
Chỉ bây giờ người ta cho phép sử dụng các số giống nhau trong dãy con.

Giải pháp về cơ bản cũng gần giống nhau.
Chúng ta chỉ cần thay đổi các dấu bất đẳng thức, và sửa đổi một chút tìm kiếm nhị phân.

### Số lượng các dãy con tăng dài nhất (Number of longest increasing subsequences) {: #number-of-longest-increasing-subsequences}

Chúng ta có thể sử dụng phương pháp đầu tiên được thảo luận, hoặc phiên bản $O(n^2)$ hoặc phiên bản sử dụng cấu trúc dữ liệu.
Chúng ta chỉ phải lưu trữ thêm có bao nhiêu cách chúng ta có thể nhận được các dãy con tăng dài nhất kết thúc bằng các giá trị $d[i]$.

Số cách để tạo thành một dãy con tăng dài nhất kết thúc trong $a[i]$ là tổng của tất cả các cách cho tất cả các dãy con tăng dài nhất kết thúc trong $j$ trong đó $d[j]$ là cực đại.
Có thể có nhiều $j$ như vậy, vì vậy chúng ta cần tính tổng tất cả chúng.

Sử dụng Segment tree, cách tiếp cận này cũng có thể được triển khai trong $O(n \log n)$.

Không thể sử dụng phương pháp tìm kiếm nhị phân cho nhiệm vụ này.

### Số lượng nhỏ nhất các dãy con không tăng bao phủ một dãy (Smallest number of non-increasing subsequences covering a sequence) {: #smallest-number-of-non-increasing-subsequences-covering-a-sequence}

Cho một mảng nhất định với $n$ số $a[0 \dots n - 1]$, chúng ta phải tô màu các số bằng số lượng màu nhỏ nhất, sao cho mỗi màu tạo thành một dãy con không tăng.

Để giải quyết vấn đề này, chúng ta nhận thấy rằng số lượng màu tối thiểu cần thiết bằng với độ dài của dãy con tăng dài nhất.

**Chứng minh**:
Chúng ta cần chứng minh **tính đối ngẫu** của hai bài toán này.

Hãy ký hiệu $x$ là độ dài của dãy con tăng dài nhất và $y$ là số lượng ít nhất các dãy con không tăng tạo thành một lớp phủ.
Chúng ta cần chứng minh rằng $x = y$.

Rõ ràng là $y < x$ là không thể, bởi vì nếu chúng ta có $x$ phần tử tăng nghiêm ngặt, thì không có hai phần tử nào có thể là một phần của cùng một dãy con không tăng.
Do đó chúng ta có $y \ge x$.

Bây giờ chúng ta chỉ ra rằng $y > x$ là không thể bằng cách phản chứng.
Giả sử rằng $y > x$.
Sau đó, chúng ta xem xét bất kỳ tập hợp tối ưu nào của $y$ dãy con không tăng.
Chúng ta biến đổi tập hợp này theo cách sau:
miễn là có hai dãy con như vậy sao cho dãy đầu tiên bắt đầu trước dãy con thứ hai, và dãy đầu tiên bắt đầu bằng một số lớn hơn hoặc bằng dãy thứ hai, thì chúng ta tháo số bắt đầu này và gắn nó vào đầu của dãy thứ hai.
Sau một số hữu hạn các bước, chúng ta có $y$ dãy con, và các số bắt đầu của chúng sẽ tạo thành một dãy con tăng có độ dài $y$.
Vì chúng ta đã giả định rằng $y > x$, chúng ta đã đạt được một mâu thuẫn.

Do đó suy ra rằng $y = x$.

**Khôi phục các dãy**:
Phân vùng mong muốn của dãy thành các dãy con có thể được thực hiện một cách tham lam.
Tức là đi từ trái sang phải và gán số hiện tại hoặc dãy con đó kết thúc bằng số nhỏ nhất lớn hơn hoặc bằng số hiện tại.

## Bài tập (Practice Problems) {: #practice-problems}

- [ACMSGURU - "North-East"](http://codeforces.com/problemsets/acmsguru/problem/99999/521)
- [Codeforces - LCIS](http://codeforces.com/problemset/problem/10/D)
- [Codeforces - Tourist](http://codeforces.com/contest/76/problem/F)
- [SPOJ - DOSA](https://www.spoj.com/problems/DOSA/)
- [SPOJ - HMLIS](https://www.spoj.com/problems/HMLIS/)
- [SPOJ - ONEXLIS](https://www.spoj.com/problems/ONEXLIS/)
- [SPOJ - SUPPER](http://www.spoj.com/problems/SUPPER/)
- [Topcoder - AutoMarket](https://community.topcoder.com/stat?c=problem_statement&pm=3937&rd=6532)
- [Topcoder - BridgeArrangement](https://community.topcoder.com/stat?c=problem_statement&pm=2967&rd=5881)
- [Topcoder - IntegerSequence](https://community.topcoder.com/stat?c=problem_statement&pm=5922&rd=8075)
- [UVA - Back To Edit Distance](https://onlinejudge.org/external/127/12747.pdf)
- [UVA - Happy Birthday](https://onlinejudge.org/external/120/12002.pdf)
- [UVA - Tiling Up Blocks](https://onlinejudge.org/external/11/1196.pdf)
