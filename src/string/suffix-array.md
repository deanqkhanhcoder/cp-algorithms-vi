---
tags:
  - Translated
e_maxx_link: suffix_array
---

# Mảng Hậu tố (Suffix Array) {: #suffix-array}

## Định nghĩa (Definition) {: #definition}

Gọi $s$ là chuỗi có độ dài $n$. Hậu tố thứ $i$ của $s$ là chuỗi con $s[i \ldots n - 1]$.

**Mảng hậu tố** sẽ chứa các số nguyên đại diện cho **chỉ số bắt đầu** của tất cả các hậu tố của một chuỗi nhất định, sau khi các hậu tố nói trên được sắp xếp.

Ví dụ hãy xem chuỗi $s = abaab$.
Tất cả các hậu tố như sau

$$\begin{array}{ll}
0. & abaab \\
1. & baab \\
2. & aab \\
3. & ab \\
4. & b
\end{array}$$

Sau khi sắp xếp các chuỗi này:

$$\begin{array}{ll}
2. & aab \\
3. & ab \\
0. & abaab \\
4. & b \\
1. & baab
\end{array}$$

Do đó mảng hậu tố cho $s$ sẽ là $(2,~ 3,~ 0,~ 4,~ 1)$.

Là một cấu trúc dữ liệu, nó được sử dụng rộng rãi trong các lĩnh vực như nén dữ liệu, tin sinh học và nói chung, trong bất kỳ lĩnh vực nào liên quan đến chuỗi và các vấn đề so khớp chuỗi.

## Xây dựng (Construction) {: #construction}

### Tiếp cận $O(n^2 \log n)$ ($O(n^2 \log n)$ approach) {: #on2-log-n-approach}

Đây là cách tiếp cận ngây thơ nhất.
Lấy tất cả các hậu tố và sắp xếp chúng bằng quicksort hoặc mergesort đồng thời giữ lại các chỉ số ban đầu của chúng.
Việc sắp xếp sử dụng $O(n \log n)$ so sánh, và vì so sánh hai chuỗi sẽ mất thêm thời gian $O(n)$, chúng ta đạt được độ phức tạp cuối cùng là $O(n^2 \log n)$.

### Tiếp cận $O(n \log n)$ ($O(n \log n)$ approach) {: #on-log-n-approach}

Nói một cách chính xác, thuật toán sau đây sẽ không sắp xếp các hậu tố, mà là các dịch chuyển vòng (cyclic shifts) của một chuỗi.
Tuy nhiên, chúng ta có thể rất dễ dàng suy ra một thuật toán để sắp xếp các hậu tố từ nó:
chỉ cần thêm một ký tự tùy ý vào cuối chuỗi nhỏ hơn bất kỳ ký tự nào trong chuỗi là đủ.
Sử dụng biểu tượng \$ là phổ biến.
Khi đó thứ tự của các dịch chuyển vòng đã sắp xếp tương đương với thứ tự của các hậu tố đã sắp xếp, như được minh họa ở đây với chuỗi $dabbb$.

$$\begin{array}{lll}
1. & abbb\$d & abbb \\
4. & b\$dabb & b \\
3. & bb\$dab & bb \\
6. & bbb\$da & bbb \\
0. & dabbb\$ & dabbb
\end{array}$$

Vì chúng ta sẽ sắp xếp các dịch chuyển vòng, chúng ta sẽ xem xét **chuỗi con vòng** (**cyclic substrings**).
Chúng ta sẽ sử dụng ký hiệu $s[i \dots j]$ cho chuỗi con của $s$ ngay cả khi $i > j$.
Trong trường hợp này, chúng tôi thực sự có nghĩa là chuỗi $s[i \dots n-1] + s[0 \dots j]$.
Ngoài ra, chúng tôi sẽ lấy tất cả các chỉ số modulo theo độ dài của $s$, và sẽ bỏ qua phép toán modulo cho đơn giản.

Thuật toán chúng tôi thảo luận sẽ thực hiện $\lceil \log n \rceil + 1$ lần lặp.
Trong lần lặp thứ $k$ ($k = 0 \dots \lceil \log n \rceil$), chúng ta sắp xếp $n$ chuỗi con vòng của $s$ có độ dài $2^k$.
Sau lần lặp thứ $\lceil \log n \rceil$, các chuỗi con có độ dài $2^{\lceil \log n \rceil} \ge n$ sẽ được sắp xếp, vì vậy điều này tương đương với việc sắp xếp hoàn toàn các dịch chuyển vòng.

Trong mỗi lần lặp của thuật toán, ngoài hoán vị $p[0 \dots n-1]$, trong đó $p[i]$ là chỉ số của chuỗi con thứ $i$ (bắt đầu tại $i$ và với độ dài $2^k$) theo thứ tự đã sắp xếp, chúng ta cũng sẽ duy trì một mảng $c[0 \dots n-1]$, trong đó $c[i]$ tương ứng với **lớp tương đương** (**equivalence class**) mà chuỗi con thuộc về.
Bởi vì một số chuỗi con sẽ giống hệt nhau và thuật toán cần xử lý chúng như nhau.
Để thuận tiện, các lớp sẽ được dán nhãn bằng các số bắt đầu từ không.
Ngoài ra, các số $c[i]$ sẽ được gán theo cách sao cho chúng bảo toàn thông tin về thứ tự:
nếu một chuỗi con nhỏ hơn chuỗi con kia, thì nó cũng phải có nhãn lớp nhỏ hơn.
Số lượng lớp tương đương sẽ được lưu trữ trong biến $\text{classes}$.

Hãy xem một ví dụ.
Xét chuỗi $s = aaba$.
Các chuỗi con vòng và các mảng tương ứng $p[]$ và $c[]$ được đưa ra cho mỗi lần lặp:

$$\begin{array}{cccc}
0: & (a,~ a,~ b,~ a) & p = (0,~ 1,~ 3,~ 2) & c = (0,~ 0,~ 1,~ 0)\\
1: & (aa,~ ab,~ ba,~ aa) & p = (0,~ 3,~ 1,~ 2) & c = (0,~ 1,~ 2,~ 0)\\
2: & (aaba,~ abaa,~ baaa,~ aaab) & p = (3,~ 0,~ 1,~ 2) & c = (1,~ 2,~ 3,~ 0)\\
\end{array}$$

Điều đáng chú ý là các giá trị của $p[]$ có thể khác nhau.
Ví dụ trong lần lặp thứ $0$, mảng cũng có thể là $p = (3,~ 1,~ 0,~ 2)$ hoặc $p = (3,~ 0,~ 1,~ 2)$.
Tất cả các tùy chọn này hoán vị các chuỗi con thành một thứ tự đã sắp xếp.
Vì vậy, tất cả chúng đều hợp lệ.
Đồng thời mảng $c[]$ là cố định, không thể có sự mơ hồ.

Bây giờ chúng ta hãy tập trung vào việc thực hiện thuật toán.
Chúng ta sẽ viết một hàm nhận chuỗi $s$ và trả về các hoán vị của các dịch chuyển vòng đã sắp xếp.
```cpp title="suffix_array_sort_cyclic1"
vector<int> sort_cyclic_shifts(string const& s) {
    int n = s.size();
    const int alphabet = 256;
```

Khi bắt đầu (trong **lần lặp thứ $0$**), chúng ta phải sắp xếp các chuỗi con vòng có độ dài $1$, nghĩa là chúng ta phải sắp xếp tất cả các ký tự của chuỗi và chia chúng thành các lớp tương đương (cùng một ký hiệu được gán cho cùng một lớp).
Điều này có thể được thực hiện một cách tầm thường, ví dụ, bằng cách sử dụng **sắp xếp đếm** (**counting sort**).
Đối với mỗi ký tự, chúng ta đếm số lần nó xuất hiện trong chuỗi, và sau đó sử dụng thông tin này để tạo mảng $p[]$.
Sau đó, chúng ta đi qua mảng $p[]$ và xây dựng $c[]$ bằng cách so sánh các ký tự liền kề.
```cpp title="suffix_array_sort_cyclic2"
    vector<int> p(n), c(n), cnt(max(alphabet, n), 0);
    for (int i = 0; i < n; i++)
        cnt[s[i]]++;
    for (int i = 1; i < alphabet; i++)
        cnt[i] += cnt[i-1];
    for (int i = 0; i < n; i++)
        p[--cnt[s[i]]] = i;
    c[p[0]] = 0;
    int classes = 1;
    for (int i = 1; i < n; i++) {
        if (s[p[i]] != s[p[i-1]])
            classes++;
        c[p[i]] = classes - 1;
    }
```

Bây giờ chúng ta phải nói về bước lặp.
Giả sử chúng ta đã thực hiện bước $k-1$ và tính toán các giá trị của các mảng $p[]$ và $c[]$ cho nó.
Chúng ta muốn tính toán các giá trị cho bước $k$ trong thời gian $O(n)$.
Vì chúng ta thực hiện bước này $O(\log n)$ lần, nên thuật toán hoàn chỉnh sẽ có độ phức tạp thời gian là $O(n \log n)$.

Để làm điều này, lưu ý rằng các chuỗi con vòng có độ dài $2^k$ bao gồm hai chuỗi con có độ dài $2^{k-1}$ mà chúng ta có thể so sánh với nhau trong $O(1)$ bằng cách sử dụng thông tin từ giai đoạn trước - giá trị của các lớp tương đương $c[]$.
Do đó, đối với hai chuỗi con có độ dài $2^k$ bắt đầu tại vị trí $i$ và $j$, tất cả thông tin cần thiết để so sánh chúng được chứa trong các cặp $(c[i],~ c[i + 2^{k-1}])$ và $(c[j],~ c[j + 2^{k-1}])$.

$$\dots
\overbrace{
\underbrace{s_i \dots s_{i+2^{k-1}-1}}_{\text{length} = 2^{k-1},~ \text{class} = c[i]}
\quad
\underbrace{s_{i+2^{k-1}} \dots s_{i+2^k-1}}_{\text{length} = 2^{k-1},~ \text{class} = c[i + 2^{k-1}]}
}^{\text{length} = 2^k}
\dots
\overbrace{
\underbrace{s_j \dots s_{j+2^{k-1}-1}}_{\text{length} = 2^{k-1},~ \text{class} = c[j]}
\quad
\underbrace{s_{j+2^{k-1}} \dots s_{j+2^k-1}}_{\text{length} = 2^{k-1},~ \text{class} = c[j + 2^{k-1}]}
}^{\text{length} = 2^k}
\dots
$$

Điều này cho chúng ta một giải pháp rất đơn giản:
**sắp xếp** các chuỗi con có độ dài $2^k$ **theo các cặp số này**.
Điều này sẽ cho chúng ta thứ tự $p[]$ cần thiết.
Tuy nhiên, một sắp xếp thông thường chạy trong thời gian $O(n \log n)$, mà chúng ta không hài lòng.
Điều này sẽ chỉ cho chúng ta một thuật toán để xây dựng một mảng hậu tố trong thời gian $O(n \log^2 n)$.

Làm thế nào để chúng ta thực hiện nhanh việc sắp xếp các cặp như vậy?
Vì các phần tử của các cặp không vượt quá $n$, chúng ta có thể sử dụng sắp xếp đếm một lần nữa.
Tuy nhiên, sắp xếp các cặp bằng sắp xếp đếm không phải là hiệu quả nhất.
Để đạt được hằng số ẩn tốt hơn trong độ phức tạp, chúng ta sẽ sử dụng một thủ thuật khác.

Chúng ta sử dụng ở đây kỹ thuật mà **sắp xếp cơ số** (**radix sort**) dựa trên: để sắp xếp các cặp, trước tiên chúng ta sắp xếp chúng theo phần tử thứ hai, và sau đó theo phần tử thứ nhất (với sắp xếp ổn định, tức là sắp xếp không phá vỡ thứ tự tương đối của các phần tử bằng nhau).
Tuy nhiên, các phần tử thứ hai đã được sắp xếp trong lần lặp trước đó.
Do đó, để sắp xếp các cặp theo các phần tử thứ hai, chúng ta chỉ cần trừ $2^{k-1}$ từ các chỉ số trong $p[]$ (ví dụ: nếu chuỗi con nhỏ nhất có độ dài $2^{k-1}$ bắt đầu tại vị trí $i$, thì chuỗi con có độ dài $2^k$ với nửa sau nhỏ nhất bắt đầu tại $i - 2^{k-1}$).

Vì vậy, chỉ bằng các phép trừ đơn giản, chúng ta có thể sắp xếp các phần tử thứ hai của các cặp trong $p[]$.
Bây giờ chúng ta cần thực hiện sắp xếp ổn định theo các phần tử đầu tiên.
Như đã đề cập, điều này có thể được thực hiện bằng sắp xếp đếm.

Điều duy nhất còn lại là tính toán các lớp tương đương $c[]$, nhưng như trước đây, điều này có thể được thực hiện bằng cách lặp qua hoán vị đã sắp xếp $p[]$ và so sánh các cặp lân cận.

Dưới đây là phần cài đặt còn lại.
Chúng tôi sử dụng các mảng tạm thời $pn[]$ và $cn[]$ để lưu trữ hoán vị theo các phần tử thứ hai và các chỉ số lớp tương đương mới.
```cpp title="suffix_array_sort_cyclic3"
    vector<int> pn(n), cn(n);
    for (int h = 0; (1 << h) < n; ++h) {
        for (int i = 0; i < n; i++) {
            pn[i] = p[i] - (1 << h);
            if (pn[i] < 0)
                pn[i] += n;
        }
        fill(cnt.begin(), cnt.begin() + classes, 0);
        for (int i = 0; i < n; i++)
            cnt[c[pn[i]]]++;
        for (int i = 1; i < classes; i++)
            cnt[i] += cnt[i-1];
        for (int i = n-1; i >= 0; i--)
            p[--cnt[c[pn[i]]]] = pn[i];
        cn[p[0]] = 0;
        classes = 1;
        for (int i = 1; i < n; i++) {
            pair<int, int> cur = {c[p[i]], c[(p[i] + (1 << h)) % n]};
            pair<int, int> prev = {c[p[i-1]], c[(p[i-1] + (1 << h)) % n]};
            if (cur != prev)
                ++classes;
            cn[p[i]] = classes - 1;
        }
        c.swap(cn);
    }
    return p;
}
```
Thuật toán yêu cầu thời gian $O(n \log n)$ và bộ nhớ $O(n)$. Để đơn giản, chúng tôi đã sử dụng phạm vi ASCII hoàn chỉnh làm bảng chữ cái.

Nếu biết rằng chuỗi chỉ chứa một tập hợp con các ký tự, ví dụ như chỉ các chữ cái viết thường, thì việc triển khai có thể được tối ưu hóa, nhưng yếu tố tối ưu hóa có thể sẽ không đáng kể, vì kích thước của bảng chữ cái chỉ quan trọng trong lần lặp đầu tiên. Mọi lần lặp khác phụ thuộc vào số lượng các lớp tương đương, có thể nhanh chóng đạt tới $O(n)$ ngay cả khi ban đầu nó là một chuỗi trên bảng chữ cái có kích thước $2$.

Cũng lưu ý rằng, thuật toán này chỉ sắp xếp các dịch chuyển vòng.
Như đã đề cập ở đầu phần này, chúng ta có thể tạo thứ tự sắp xếp của các hậu tố bằng cách thêm một ký tự nhỏ hơn tất cả các ký tự khác của chuỗi và sắp xếp chuỗi kết quả này theo các dịch chuyển vòng, ví dụ: bằng cách sắp xếp các dịch chuyển vòng của $s + \$$.
Điều này rõ ràng sẽ cung cấp mảng hậu tố của $s$, tuy nhiên được thêm vào trước với $|s|$.
```cpp title="suffix_array_construction"
vector<int> suffix_array_construction(string s) {
    s += "$";
    vector<int> sorted_shifts = sort_cyclic_shifts(s);
    sorted_shifts.erase(sorted_shifts.begin());
    return sorted_shifts;
}
```

## Ứng dụng (Applications) {: #applications}

### Tìm dịch chuyển vòng nhỏ nhất (Finding the smallest cyclic shift) {: #finding-the-smallest-cyclic-shift}

Thuật toán trên sắp xếp tất cả các dịch chuyển vòng (không thêm ký tự vào chuỗi), và do đó $p[0]$ cho vị trí của dịch chuyển vòng nhỏ nhất.

### Tìm chuỗi con trong chuỗi (Finding a substring in a string) {: #finding-a-substring-in-a-string}

Nhiệm vụ là tìm một chuỗi $s$ bên trong một văn bản $t$ trực tuyến - chúng ta biết trước văn bản $t$, nhưng không phải chuỗi $s$.
Chúng ta có thể tạo mảng hậu tố cho văn bản $t$ trong thời gian $O(|t| \log |t|)$.
Bây giờ chúng ta có thể tìm kiếm chuỗi con $s$ theo cách sau.
Sự xuất hiện của $s$ phải là tiền tố của một số hậu tố từ $t$.
Vì chúng ta đã sắp xếp tất cả các hậu tố, chúng ta có thể thực hiện tìm kiếm nhị phân cho $s$ trong $p$.
So sánh hậu tố hiện tại và chuỗi con $s$ trong tìm kiếm nhị phân có thể được thực hiện trong thời gian $O(|s|)$, do đó độ phức tạp để tìm chuỗi con là $O(|s| \log |t|)$.
Cũng lưu ý rằng nếu chuỗi con xuất hiện nhiều lần trong $t$, thì tất cả các lần xuất hiện sẽ nằm cạnh nhau trong $p$.
Do đó số lần xuất hiện có thể được tìm thấy bằng tìm kiếm nhị phân thứ hai, và tất cả các lần xuất hiện có thể được in dễ dàng.

### So sánh hai chuỗi con của một chuỗi (Comparing two substrings of a string) {: #comparing-two-substrings-of-a-string}

Chúng ta muốn có thể so sánh hai chuỗi con có cùng độ dài của một chuỗi $s$ đã cho trong thời gian $O(1)$, nghĩa là kiểm tra xem chuỗi con đầu tiên có nhỏ hơn chuỗi con thứ hai không.

Để làm điều này, chúng ta xây dựng mảng hậu tố trong thời gian $O(|s| \log |s|)$ và lưu trữ tất cả các kết quả trung gian của các lớp tương đương $c[]$.

Sử dụng thông tin này, chúng ta có thể so sánh bất kỳ hai chuỗi con nào có độ dài bằng lũy thừa của hai trong O(1):
đối với điều này, chỉ cần so sánh các lớp tương đương của cả hai chuỗi con là đủ.
Bây giờ chúng ta muốn khái quát hóa phương pháp này cho các chuỗi con có độ dài tùy ý.

Hãy so sánh hai chuỗi con có độ dài $l$ với các chỉ số bắt đầu $i$ và $j$.
Chúng ta tìm độ dài lớn nhất của một khối được đặt bên trong một chuỗi con có độ dài này: $k$ lớn nhất sao cho $2^k \le l$.
Sau đó, so sánh hai chuỗi con có thể được thay thế bằng cách so sánh hai khối chồng chéo có độ dài $2^k$:
trước tiên bạn cần so sánh hai khối bắt đầu bằng $i$ và $j$, và nếu chúng bằng nhau thì hãy so sánh hai khối kết thúc ở vị trí $i + l - 1$ và $j + l - 1$:

$$\dots
\overbrace{\underbrace{s_i \dots s_{i+l-2^k} \dots s_{i+2^k-1}}_{2^k} \dots s_{i+l-1}}^{\text{đầu tiên}}
\dots
\overbrace{\underbrace{s_j \dots s_{j+l-2^k} \dots s_{j+2^k-1}}_{2^k} \dots s_{j+l-1}}^{\text{thứ hai}}
\dots$$

$$\dots
\overbrace{s_i \dots \underbrace{s_{i+l-2^k} \dots s_{i+2^k-1} \dots s_{i+l-1}}_{2^k}}^{\text{đầu tiên}}
\dots
\overbrace{s_j \dots \underbrace{s_{j+l-2^k} \dots s_{j+2^k-1} \dots s_{j+l-1}}_{2^k}}^{\text{thứ hai}}
\dots$$

Đây là việc thực hiện so sánh.
Lưu ý rằng người ta cho rằng hàm được gọi với $k$ đã được tính toán.
$k$ có thể được tính bằng $\lfloor \log l \rfloor$, nhưng hiệu quả hơn là tính toán trước tất cả các giá trị $k$ cho mọi $l$.
Xem ví dụ bài viết về [Bảng thưa (Sparse Table)](../data_structures/sparse-table.md), sử dụng một ý tưởng tương tự và tính toán tất cả các giá trị $\log$.

```cpp
int compare(int i, int j, int l, int k) {
    pair<int, int> a = {c[k][i], c[k][(i+l-(1 << k))%n]};
    pair<int, int> b = {c[k][j], c[k][(j+l-(1 << k))%n]};
    return a == b ? 0 : a < b ? -1 : 1;
}
```

### Tiền tố chung dài nhất của hai chuỗi con với bộ nhớ bổ sung (Longest common prefix of two substrings with additional memory) {: #longest-common-prefix-of-two-substrings-with-additional-memory}

Đối với một chuỗi $s$ đã cho, chúng ta muốn tính toán tiền tố chung dài nhất (**LCP**) của hai hậu tố tùy ý với vị trí $i$ và $j$.

Phương pháp được mô tả ở đây sử dụng bộ nhớ bổ sung $O(|s| \log |s|)$.
Một cách tiếp cận hoàn toàn khác sẽ chỉ sử dụng một lượng bộ nhớ tuyến tính được mô tả trong phần tiếp theo.

Chúng ta xây dựng mảng hậu tố trong thời gian $O(|s| \log |s|)$, và ghi nhớ các kết quả trung gian của các mảng $c[]$ từ mỗi lần lặp.

Hãy tính LCP cho hai hậu tố bắt đầu bằng $i$ và $j$.
Chúng ta có thể so sánh bất kỳ hai chuỗi con nào có độ dài bằng lũy thừa của hai trong $O(1)$.
Để làm điều này, chúng ta so sánh các chuỗi theo lũy thừa của hai (từ lũy thừa cao nhất đến thấp nhất) và nếu các chuỗi con có độ dài này giống nhau, thì chúng ta thêm độ dài bằng nhau vào câu trả lời và tiếp tục kiểm tra LCP ở bên phải của phần bằng nhau, tức là $i$ và $j$ được thêm bởi lũy thừa hiện tại của hai.

```cpp
int lcp(int i, int j) {
    int ans = 0;
    for (int k = log_n; k >= 0; k--) {
        if (c[k][i % n] == c[k][j % n]) {
            ans += 1 << k;
            i += 1 << k;
            j += 1 << k;
        }
    }
    return ans;
}
```

Ở đây `log_n` biểu thị một hằng số bằng logarit của $n$ trong cơ số $2$ làm tròn xuống.

### Tiền tố chung dài nhất của hai chuỗi con không có bộ nhớ bổ sung (Longest common prefix of two substrings without additional memory) {: #longest-common-prefix-of-two-substrings-without-additional-memory}

Chúng ta có cùng nhiệm vụ như trong phần trước.
Chúng ta phải tính toán tiền tố chung dài nhất (**LCP**) cho hai hậu tố của một chuỗi $s$.

Không giống như phương pháp trước, phương pháp này sẽ chỉ sử dụng bộ nhớ $O(|s|)$.
Kết quả của quá trình tiền xử lý sẽ là một mảng (bản thân nó là một nguồn thông tin quan trọng về chuỗi, và do đó cũng được sử dụng để giải quyết các tác vụ khác).
Các truy vấn LCP có thể được trả lời bằng cách thực hiện các truy vấn RMQ (truy vấn phạm vi tối thiểu) trong mảng này, vì vậy đối với các triển khai khác nhau, có thể đạt được thời gian truy vấn logarit và thậm chí hằng số.

Cơ sở cho thuật toán này là ý tưởng sau:
chúng ta sẽ tính toán tiền tố chung dài nhất cho mỗi **cặp hậu tố liền kề trong thứ tự đã sắp xếp**.
Nói cách khác, chúng ta xây dựng một mảng $\text{lcp}[0 \dots n-2]$, trong đó $\text{lcp}[i]$ bằng độ dài của tiền tố chung dài nhất của các hậu tố bắt đầu tại $p[i]$ và $p[i+1]$.
Mảng này sẽ cho chúng ta câu trả lời cho bất kỳ hai hậu tố liền kề nào của chuỗi.
Sau đó, câu trả lời cho hai hậu tố tùy ý, không nhất thiết là láng giềng, có thể thu được từ mảng này.
Trong thực tế, hãy để yêu cầu tính toán LCP của các hậu tố $p[i]$ và $p[j]$.
Sau đó câu trả lời cho truy vấn này sẽ là $\min(lcp[i],~ lcp[i+1],~ \dots,~ lcp[j-1])$.

Do đó, nếu chúng ta có một mảng $\text{lcp}$ như vậy, thì vấn đề được giảm xuống [RMQ](../sequences/rmq.md), có rất nhiều giải pháp khác nhau với độ phức tạp khác nhau.

Vì vậy, nhiệm vụ chính là **xây dựng** mảng $\text{lcp}$ này.
Chúng ta sẽ sử dụng **thuật toán Kasai**, có thể tính toán mảng này trong thời gian $O(n)$.

Hãy nhìn vào hai hậu tố liền kề trong thứ tự đã sắp xếp (thứ tự của mảng hậu tố).
Hãy để vị trí bắt đầu của chúng là $i$ và $j$ và $\text{lcp}$ của chúng bằng $k > 0$.
Nếu chúng ta loại bỏ chữ cái đầu tiên của cả hai hậu tố - tức là chúng ta lấy các hậu tố $i+1$ và $j+1$ - thì rõ ràng là $\text{lcp}$ của hai hậu tố này là $k - 1$.
Tuy nhiên, chúng ta không thể sử dụng giá trị này và ghi nó vào mảng $\text{lcp}$, bởi vì hai hậu tố này có thể không nằm cạnh nhau trong thứ tự đã sắp xếp.
Hậu tố $i+1$ tất nhiên sẽ nhỏ hơn hậu tố $j+1$, nhưng có thể có một số hậu tố ở giữa chúng.
Tuy nhiên, vì chúng ta biết rằng LCP giữa hai hậu tố là giá trị nhỏ nhất của tất cả các chuyển đổi, chúng ta cũng biết rằng LCP giữa bất kỳ hai cặp nào trong khoảng đó ít nhất phải là $k-1$, đặc biệt là giữa $i+1$ và hậu tố tiếp theo.
Và có thể nó có thể lớn hơn.

Bây giờ chúng ta đã có thể thực hiện thuật toán.
Chúng ta sẽ lặp qua các hậu tố theo thứ tự độ dài của chúng. Bằng cách này, chúng ta có thể sử dụng lại giá trị cuối cùng $k$, vì đi từ hậu tố $i$ đến hậu tố $i+1$ hoàn toàn giống như loại bỏ chữ cái đầu tiên.
Chúng ta sẽ cần một mảng bổ sung $\text{rank}$, sẽ cung cấp cho chúng ta vị trí của một hậu tố trong danh sách các hậu tố đã sắp xếp.
```cpp title="suffix_array_lcp_construction"
vector<int> lcp_construction(string const& s, vector<int> const& p) {
    int n = s.size();
    vector<int> rank(n, 0);
    for (int i = 0; i < n; i++)
        rank[p[i]] = i;

    int k = 0;
    vector<int> lcp(n-1, 0);
    for (int i = 0; i < n; i++) {
        if (rank[i] == n - 1) {
            k = 0;
            continue;
        }
        int j = p[rank[i] + 1];
        while (i + k < n && j + k < n && s[i+k] == s[j+k])
            k++;
        lcp[rank[i]] = k;
        if (k)
            k--;
    }
    return lcp;
}
```

Rất dễ thấy rằng chúng ta giảm $k$ tối đa $O(n)$ lần (mỗi lần lặp tối đa một lần, ngoại trừ $\text{rank}[i] == n-1$, nơi chúng ta trực tiếp đặt lại nó thành $0$), và LCP giữa hai chuỗi tối đa là $n-1$, chúng ta cũng sẽ tăng $k$ chỉ $O(n)$ lần.
Do đó thuật toán chạy trong thời gian $O(n)$.

### Số lượng chuỗi con khác nhau (Number of different substrings) {: #number-of-different-substrings}

Chúng ta tiền xử lý chuỗi $s$ bằng cách tính toán mảng hậu tố và mảng LCP.
Sử dụng thông tin này, chúng ta có thể tính toán số lượng chuỗi con khác nhau trong chuỗi.

Để làm điều này, chúng ta sẽ suy nghĩ về những chuỗi con **mới** nào bắt đầu tại vị trí $p[0]$, sau đó tại $p[1]$, v.v.
Trong thực tế, chúng ta lấy các hậu tố theo thứ tự đã sắp xếp và xem tiền tố nào cung cấp chuỗi con mới.
Do đó, chúng ta sẽ không vô tình bỏ qua bất kỳ cái nào.

Vì các hậu tố được sắp xếp, nên rõ ràng là hậu tố hiện tại $p[i]$ sẽ cung cấp các chuỗi con mới cho tất cả các tiền tố của nó, ngoại trừ các tiền tố trùng với hậu tố $p[i-1]$.
Do đó, tất cả các tiền tố của nó ngoại trừ tiền tố $\text{lcp}[i-1]$ đầu tiên.
Vì độ dài của hậu tố hiện tại là $n - p[i]$, $n - p[i] - \text{lcp}[i-1]$ tiền tố mới bắt đầu tại $p[i]$.
Tổng kết trên tất cả các hậu tố, chúng ta có câu trả lời cuối cùng:

$$\sum_{i=0}^{n-1} (n - p[i]) - \sum_{i=0}^{n-2} \text{lcp}[i] = \frac{n^2 + n}{2} - \sum_{i=0}^{n-2} \text{lcp}[i]$$

## Bài tập (Practice Problems) {: #practice-problems}

* [Uva 760 - DNA Sequencing](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=701)
* [Uva 1223 - Editor](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=3664)
* [Codechef - Tandem](https://www.codechef.com/problems/TANDEM)
* [Codechef - Substrings and Repetitions](https://www.codechef.com/problems/ANUSAR)
* [Codechef - Entangled Strings](https://www.codechef.com/problems/TANGLED)
* [Codeforces - Martian Strings](http://codeforces.com/problemset/problem/149/E)
* [Codeforces - Little Elephant and Strings](http://codeforces.com/problemset/problem/204/E)
* [SPOJ - Ada and Terramorphing](http://www.spoj.com/problems/ADAPHOTO/)
* [SPOJ - Ada and Substring](http://www.spoj.com/problems/ADASTRNG/)
* [UVA - 1227 - The longest constant gene](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=3668)
* [SPOJ - Longest Common Substring](http://www.spoj.com/problems/LCS/en/)
* [UVA 11512 - GATTACA](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2507)
* [LA 7502 - Suffixes and Palindromes](https://vjudge.net/problem/UVALive-7502)
* [GYM - Por Costel and the Censorship Committee](http://codeforces.com/gym/100923/problem/D)
* [UVA 1254 - Top 10](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3695)
* [UVA 12191 - File Recover](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3343)
* [UVA 12206 - Stammering Aliens](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=3358)
* [Codechef - Jarvis and LCP](https://www.codechef.com/problems/INSQ16F)
* [LA 3943 - Liking's Letter](https://vjudge.net/problem/UVALive-3943)
* [UVA 11107 - Life Forms](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2048)
* [UVA 12974 - Exquisite Strings](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=862&page=show_problem&problem=4853)
* [UVA 10526 - Intellectual Property](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1467)
* [UVA 12338 - Anti-Rhyme Pairs](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=3760)
* [UVA 12191 - File Recover](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3343)
* [SPOJ - Suffix Array](http://www.spoj.com/problems/SARRAY/)
* [LA 4513 - Stammering Aliens](https://vjudge.net/problem/UVALive-4513)
* [SPOJ - LCS2](http://www.spoj.com/problems/LCS2/)
* [Codeforces - Fake News (hard)](http://codeforces.com/contest/802/problem/I)
* [SPOJ - Longest Commong Substring](http://www.spoj.com/problems/LONGCS/)
* [SPOJ - Lexicographical Substring Search](http://www.spoj.com/problems/SUBLEX/)
* [Codeforces - Forbidden Indices](http://codeforces.com/contest/873/problem/F)
* [Codeforces - Tricky and Clever Password](http://codeforces.com/contest/30/problem/E)
* [LA 6856 - Circle of digits](https://vjudge.net/problem/UVALive-6856)
