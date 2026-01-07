---
tags:
  - Translated
e_maxx_link: longest_increasing_subseq_log
---

# Dãy con tăng dài nhất

Cho một mảng gồm $n$ số: $a[0 \dots n-1]$.
Nhiệm vụ là tìm dãy con tăng chặt (strictly increasing) dài nhất trong $a$.

Một cách chính thức ta tìm dãy chỉ số dài nhất $i_1, \dots, i_k$ sao cho

$$i_1 < i_2 < \dots < i_k,\quad
a[i_1] < a[i_2] < \dots < a[i_k]$$

Bài viết này sẽ thảo luận nhiều thuật toán để giải bài toán này, và đồng thời đề cập đến một số bài toán khác có thể quy về bài toán này.

## Giải pháp $O(n^2)$ bằng quy hoạch động {data-toc-label="Solution in O(n^2) with dynamic programming"}

Quy hoạch động là một kỹ thuật rất tổng quát cho phép giải một lớp lớn các bài toán.
Ở đây chúng ta áp dụng kỹ thuật này cho bài toán cụ thể.

Trước hết ta chỉ tìm **độ dài** của dãy con tăng dài nhất, sau đó mới học cách phục hồi chính dãy con.

### Tìm độ dài

Để làm việc này, định nghĩa mảng $d[0 \dots n-1]$, trong đó $d[i]$ là độ dài của dãy con tăng dài nhất kết thúc tại phần tử có chỉ số $i$.

!!! example

    $$\begin{array}{ll}
    a &= \{8, 3, 4, 6, 5, 2, 0, 7, 9, 1\} \\
    d &= \{1, 1, 2, 3, 3, 1, 1, 4, 5, 2\}
    \end{array}$$

    Dãy con tăng dài nhất kết thúc tại chỉ số 4 là $\{3, 4, 5\}$ có độ dài 3; dãy dài nhất kết thúc tại chỉ số 8 có thể là $\{3, 4, 5, 7, 9\}$ hoặc $\{3, 4, 6, 7, 9\}$, đều có độ dài 5; còn dãy dài nhất kết thúc tại chỉ số 9 là $\{0, 1\}$ có độ dài 2.

Ta sẽ tính mảng này dần dần: trước tiên $d[0]$, rồi $d[1]$, v.v.
Sau khi mảng $d[]$ được tính xong, đáp án là giá trị lớn nhất trong mảng $d[]$.

Gọi chỉ số hiện tại là $i$.
Tức là ta cần tính $d[i]$ và tất cả các giá trị $d[0], \dots, d[i-1]$ đã biết.
Khi đó có hai trường hợp:

-   $d[i] = 1$: dãy cần tìm chỉ gồm phần tử $a[i]$.

-   $d[i] > 1$: Dãy con sẽ kết thúc tại $a[i]$, và phần tử đứng ngay trước nó là một số $a[j]$ với $j < i$ và $a[j] < a[i]$.

    Rõ ràng dãy con kết thúc tại $a[j]$ là một trong các dãy con tăng dài nhất kết thúc tại $a[j]$.
    Số $a[i]$ chỉ mở rộng dãy đó thêm một phần tử.

    Do đó ta chỉ cần duyệt tất cả $j < i$ sao cho $a[j] < a[i]$, và lấy dãy dài nhất thu được bằng cách nối $a[i]$ vào dãy dài nhất kết thúc ở $a[j]$.
    Dãy dài nhất kết thúc ở $a[j]$ có độ dài $d[j]$, thêm một phần tử cho được $d[j] + 1$.
  
    $$d[i] = \max_{\substack{j < i \\\\ a[j] < a[i]}} \left(d[j] + 1\right)$$

Kết hợp hai trường hợp trên ta có:

$$d[i] = \max\left(1, \max_{\substack{j < i \\\\ a[j] < a[i]}} \left(d[j] + 1\right)\right)$$

### Cài đặt

Đây là hiện thực của thuật toán trên, tính độ dài dãy con tăng dài nhất:

```{.cpp file=lis_n2}
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

### Phục hồi dãy con

Cho tới giờ ta mới biết cách tìm độ dài, chưa biết cách lấy chính dãy con.

Để phục hồi dãy con, ta sinh thêm mảng phụ $p[0 \dots n-1]$ tính cùng lúc với $d[]$.
$p[i]$ là chỉ số $j$ của phần tử đứng trước cuối cùng trong dãy tăng dài nhất kết thúc tại $i$.
Nói cách khác, $p[i]$ chính là chỉ số $j$ tại đó giá trị lớn nhất $d[i]$ được tạo ra.
Mảng $p[]$ phần nào giống con trỏ đến tổ tiên.

Để lấy dãy con, ta bắt đầu tại chỉ số $i$ có $d[i]$ lớn nhất, rồi theo các con trỏ tổ tiên cho đến khi tới phần tử có $d[i] = 1$.

### Cài đặt phục hồi

Chúng ta sửa chút mã ở phần trước: tính $p[]$ cùng với $d[]$, sau đó xây dãy con.

Ban đầu khởi $p[i] = -1$.
Với các phần tử có $d[i] = 1$, giá trị tổ tiên vẫn là $-1$, điều này tiện cho việc phục hồi.

```{.cpp file=lis_n2_restore}
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

### Cách thay thế để phục hồi dãy con

Cũng có thể phục hồi dãy con mà không dùng mảng phụ $p[]$.
Ta chỉ cần tính lại giá trị hiện thời của $d[i]$ và xác định cách giá trị tối đa đó được tạo ra.

Cách này mã dài hơn một chút, nhưng tiết kiệm bộ nhớ.

## Giải pháp $O(n \log n)$ bằng quy hoạch động và tìm kiếm nhị phân {data-toc-label="Solution in O(n log n) with dynamic programming and binary search"}

Để có lời giải nhanh hơn, ta xây một phương pháp quy hoạch động khác ban đầu chạy như $O(n^2)$ rồi cải tiến lên $O(n \log n)$.

Ta dùng mảng quy hoạch động $d[0 \dots n]$.
Lần này $d[l]$ không tương ứng với một phần tử $a[i]$ hay prefix của mảng.
$d[l]$ là phần tử nhỏ nhất mà một dãy tăng độ dài $l$ có thể kết thúc tại đó.

Ban đầu đặt $d[0] = -\infty$ và với mọi $l > 0$ đặt $d[l] = \infty$.

Ta xử lý từng phần tử $a[i]$ theo thứ tự, và tại mỗi bước giữ cho mảng $d[]$ luôn đúng.

!!! example

    Với mảng $a = \{8, 3, 4, 6, 5, 2, 0, 7, 9, 1\}$, dưới đây là các prefix và mảng quy hoạch động tương ứng.

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

Khi xử lý $a[i]$, ta xét điều kiện để ghi $a[i]$ vào mảng $d[0 \dots n]$.

Gánh ý: ta đặt $d[l] = a[i]$ nếu tồn tại dãy tăng dài $l$ kết thúc tại $a[i]$, và không tồn tại dãy tăng cùng độ dài $l$ kết thúc tại số nhỏ hơn.
Tương tự như trước, nếu bỏ $a[i]$ ra khỏi dãy tăng dài $l$, ta được một dãy tăng dài $l-1$.
Vì vậy ta muốn mở rộng một dãy dài $l-1$ bằng $a[i]$, và dãy dài $l-1$ có phần tử kết thúc nhỏ nhất (tức $d[l-1]$) là lựa chọn tốt nhất.

Có thể mở rộng dãy dài $l-1$ bằng $a[i]$ khi và chỉ khi $d[l-1] < a[i]$.
Vậy ta duyệt các $l$ và kiểm tra điều kiện trên.

Thêm nữa, cần kiểm tra nếu trước đó đã tìm được dãy dài $l$ có phần tử kết thúc nhỏ hơn, nên chỉ cập nhật khi $a[i] < d[l]$.

Sau khi xử lý tất cả phần tử, độ dài đáp án là $l$ lớn nhất sao cho $d[l] < \infty$.

```{.cpp file=lis_method2_n2}
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

Ta có hai quan sát quan trọng:

1.  Mảng $d$ luôn được sắp tăng: $d[l-1] < d[l]$ với mọi $l = 1 \dots n$.

    Điều này rõ ràng: bỏ phần tử cuối của dãy dài $l$ ta được dãy dài $l-1$ có phần tử kết thúc nhỏ hơn.

2.  Phần tử $a[i]$ chỉ có thể cập nhật tối đa một giá trị $d[l]$.

    Điều này suy ra từ cài đặt trên: chỉ có một vị trí thỏa $d[l-1] < a[i] < d[l]$.

Do đó ta có thể tìm vị trí cần cập nhật trong mảng $d[]$ bằng cách dùng tìm kiếm nhị phân ([binary search](../num_methods/binary_search.md)) trong $O(\log n)$.
Trên thực tế ta tìm phần tử đầu tiên lớn hơn $a[i]$ trong $d[]$ và cập nhật như trước.

### Cài đặt

Đây là hiện thực $O(n \log n)$:

```{.cpp file=lis_method2_nlogn}
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

### Phục hồi dãy con

Cũng có thể phục hồi dãy con với phương pháp này.
Lần này cần duy trì hai mảng phụ: một mảng lưu chỉ số các phần tử trong $d[]$, và một mảng "tổ tiên" $p[i]$ (chỉ vị trí phần tử trước đó trong dãy tốt nhất kết thúc tại $i$).

Có thể cập nhật hai mảng này song song khi duyệt $a[]$ và sau đó dễ dàng phục hồi dãy con cần thiết.

## Giải pháp $O(n \log n)$ bằng cấu trúc dữ liệu {data-toc-label="Solution in O(n log n) with data structures"}

Thay vì phương pháp ở trên, ta có thể dùng các cấu trúc dữ liệu đơn giản để giải bài toán này.

Quay lại phương pháp đầu tiên: nhớ rằng $d[i]$ là $d[j] + 1$ với $j < i$ và $a[j] < a[i]$.

Nếu định nghĩa mảng phụ $t[]$ sao cho

$$t[a[i]] = d[i],$$

thì bài toán tính $d[i]$ tương đương với tìm **giá trị lớn nhất trên một prefix** của mảng $t[]$:

$$d[i] = \max\left(t[0 \dots a[i] - 1] + 1\right)$$

Bài toán tìm giá trị lớn nhất trên prefix của một mảng động là tiêu chuẩn và có thể giải bằng nhiều cấu trúc dữ liệu, ví dụ [Segment tree](../data_structures/segment_tree.md) hoặc [Fenwick tree](../data_structures/fenwick.md).

Cách này có **nhược điểm**: về độ dài và độ phức tạp cài đặt sẽ tệ hơn so với phương pháp tìm kiếm nhị phân; nếu các $a[i]$ lớn thì cần nén tọa độ (coordinate compression) hoặc dùng segment tree động để tránh tốn bộ nhớ.
Tuy nhiên có **ưu điểm**: không cần phải vận dụng các tính chất khó hiểu của thuật toán trước, và dễ dàng tổng quát hóa bài toán.

## Bài toán liên quan

Dưới đây là một số bài toán liên quan chặt chẽ với LIS.

### Dãy con không giảm dài nhất

Về bản chất gần như giống hệt, nhưng cho phép các phần tử bằng nhau xuất hiện trong dãy con.
Giải pháp tương tự, chỉ thay đổi dấu bất đẳng thức và sửa tìm kiếm nhị phân tương ứng.

### Số lượng dãy con tăng dài nhất

Có thể sử dụng phương pháp $O(n^2)$ hoặc phương pháp dùng cấu trúc dữ liệu; ta cần lưu thêm số lượng cách để đạt được dãy con dài nhất kết thúc tại mỗi vị trí $d[i]$.
Số cách để tạo dãy dài nhất kết thúc tại $a[i]$ là tổng số cách của tất cả các $j$ sao cho $d[j]$ đạt giá trị tối đa trước $i$.
Dùng segment tree ta có thể đạt $O(n \log n)$ cho bài toán này. (Không thể dùng cách tìm kiếm nhị phân đơn giản.)

### Số nhỏ nhất các dãy không tăng cần để bao phủ một dãy

Cho mảng $a[0 \dots n-1]$, ta muốn tô màu các phần tử bằng ít màu nhất sao cho mỗi màu tạo thành một dãy không tăng.
Ta nhận thấy số màu tối thiểu bằng độ dài của dãy tăng dài nhất.

**Chứng minh**: Gọi $x$ độ dài LIS và $y$ là số dãy không tăng ít nhất để bao phủ.
Rõ ràng $y < x$ không thể xảy ra, vì $x$ phần tử tăng chặt thì không thể có hai phần tử thuộc cùng một dãy không tăng, nên $y \ge x$.
Nếu $y > x$, lấy một tập tối ưu gồm $y$ dãy không tăng; ta có thể biến đổi theo thuật toán mô tả để thu được $y$ số khởi đầu tạo thành một dãy tăng độ dài $y$, mâu thuẫn. Vì vậy $y = x$.

**Phục hồi phân hoạch**: Có thể làm tham lam: duyệt từ trái sang phải và gán số hiện tại vào dãy có phần tử kết thúc nhỏ nhất mà vẫn lớn hơn hoặc bằng số hiện tại.

## Bài tập thực hành

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
