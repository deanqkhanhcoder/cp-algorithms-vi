---
tags:
  - Translated
e_maxx_link: lca_linear
---

# Tổ tiên chung thấp nhất - Thuật toán Farach-Colton và Bender (Lowest Common Ancestor - Farach-Colton and Bender Algorithm) {: #lowest-common-ancestor-farach-colton-and-bender-algorithm}

Cho $G$ là một cây.
Đối với mỗi truy vấn có dạng $(u, v)$ chúng ta muốn tìm tổ tiên chung thấp nhất của các nút $u$ và $v$, tức là chúng ta muốn tìm một nút $w$ nằm trên đường đi từ $u$ đến nút gốc, nằm trên đường đi từ $v$ đến nút gốc, và nếu có nhiều nút như vậy, chúng ta chọn nút xa nút gốc nhất.
Nói cách khác, nút $w$ mong muốn là tổ tiên thấp nhất của $u$ và $v$.
Đặc biệt nếu $u$ là tổ tiên của $v$, thì $u$ là tổ tiên chung thấp nhất của chúng.

Thuật toán sẽ được mô tả trong bài viết này được phát triển bởi Farach-Colton và Bender.
Nó là tối ưu tiệm cận.

## Thuật toán (Algorithm) {: #algorithm}

Chúng ta sử dụng phép quy giản cổ điển của bài toán LCA về bài toán RMQ.
Chúng ta duyệt tất cả các nút của cây bằng [DFS](depth-first-search.md) và giữ một mảng với tất cả các nút đã thăm và độ cao của các nút này.
LCA của hai nút $u$ và $v$ là nút nằm giữa các lần xuất hiện của $u$ và $v$ trong hành trình (tour), có độ cao nhỏ nhất.

Trong hình dưới đây, bạn có thể thấy một Euler-Tour có thể có của một đồ thị và trong danh sách bên dưới, bạn có thể thấy các nút đã thăm và độ cao của chúng.

<div style="text-align: center;">
  <img src="LCA_Euler.png" alt="LCA_Euler_Tour">
</div>

$$\begin{array}{|l|c|c|c|c|c|c|c|c|c|c|c|c|c|}
\hline
\text{Nodes:}   & 1 & 2 & 5 & 2 & 6 & 2 & 1 & 3 & 1 & 4 & 7 & 4 & 1 \\ \hline
\text{Heights:} & 1 & 2 & 3 & 2 & 3 & 2 & 1 & 2 & 1 & 2 & 3 & 2 & 1 \\ \hline
\end{array}$$

Bạn có thể đọc thêm về sự quy giản này trong bài viết [Tổ tiên chung thấp nhất](lca.md).
Trong bài viết đó, giá trị nhỏ nhất của một phạm vi được tìm thấy bằng phân rã căn bậc hai trong $O(\sqrt{N})$ hoặc trong $O(\log N)$ sử dụng Segment tree.
Trong bài viết này, chúng ta xem xét cách chúng ta có thể giải quyết các truy vấn giá trị nhỏ nhất trong phạm vi đã cho trong thời gian $O(1)$, trong khi vẫn chỉ mất thời gian $O(N)$ để tiền xử lý.

Lưu ý rằng bài toán RMQ được quy giản rất cụ thể:
bất kỳ hai phần tử liền kề nào trong mảng đều khác nhau chính xác một đơn vị (vì các phần tử của mảng không gì khác hơn là độ cao của các nút được thăm theo thứ tự duyệt, và chúng ta hoặc đi đến một hậu duệ, trong trường hợp đó phần tử tiếp theo lớn hơn một, hoặc quay lại tổ tiên, trong trường hợp đó phần tử tiếp theo nhỏ hơn một).
Thuật toán Farach-Colton và Bender mô tả một giải pháp cho chính xác bài toán RMQ chuyên biệt này.

Gọi $A$ là mảng mà chúng ta muốn thực hiện các truy vấn giá trị nhỏ nhất trong phạm vi.
Và $N$ sẽ là kích thước của $A$.

Có một cấu trúc dữ liệu dễ dàng mà chúng ta có thể sử dụng để giải quyết bài toán RMQ với tiền xử lý $O(N \log N)$ và $O(1)$ cho mỗi truy vấn: [Bảng thưa (Sparse Table)](../data_structures/sparse-table.md).
Chúng ta tạo một bảng $T$ trong đó mỗi phần tử $T[i][j]$ bằng giá trị nhỏ nhất của $A$ trong khoảng $[i, i + 2^j - 1]$.
Rõ ràng $0 \leq j \leq \lceil \log N \rceil$, và do đó kích thước của Bảng thưa sẽ là $O(N \log N)$.
Bạn có thể xây dựng bảng dễ dàng trong $O(N \log N)$ bằng cách lưu ý rằng $T[i][j] = \min(T[i][j-1], T[i+2^{j-1}][j-1])$.

Làm thế nào chúng ta có thể trả lời một truy vấn RMQ trong $O(1)$ sử dụng cấu trúc dữ liệu này?
Giả sử truy vấn nhận được là $[l, r]$, thì câu trả lời là $\min(T[l][\text{sz}], T[r-2^{\text{sz}}+1][\text{sz}])$, trong đó $\text{sz}$ là số mũ lớn nhất sao cho $2^{\text{sz}}$ không lớn hơn độ dài phạm vi $r-l+1$.
Thật vậy, chúng ta có thể lấy phạm vi $[l, r]$ và phủ nó bằng hai đoạn có độ dài $2^{\text{sz}}$ - một đoạn bắt đầu từ $l$ và đoạn kia kết thúc tại $r$.
Các đoạn này chồng chéo lên nhau, nhưng điều này không ảnh hưởng đến việc tính toán của chúng ta.
Để thực sự đạt được độ phức tạp thời gian là $O(1)$ cho mỗi truy vấn, chúng ta cần biết các giá trị của $\text{sz}$ cho tất cả các độ dài có thể từ $1$ đến $N$.
Nhưng điều này có thể dễ dàng được tính toán trước.

Bây giờ chúng ta muốn cải thiện độ phức tạp của quá trình tiền xử lý xuống còn $O(N)$.

Chúng ta chia mảng $A$ thành các khối có kích thước $K = 0.5 \log N$ với $\log$ là logarit cơ số 2.
Đối với mỗi khối, chúng ta tính toán phần tử nhỏ nhất và lưu trữ chúng trong một mảng $B$.
$B$ có kích thước $\frac{N}{K}$.
Chúng ta xây dựng một bảng thưa từ mảng $B$.
Kích thước và độ phức tạp thời gian của nó sẽ là:

$$\frac{N}{K}\log\left(\frac{N}{K}\right) = \frac{2N}{\log(N)} \log\left(\frac{2N}{\log(N)}\right) =$$

$$= \frac{2N}{\log(N)} \left(1 + \log\left(\frac{N}{\log(N)}\right)\right) \leq \frac{2N}{\log(N)} + 2N = O(N)$$

Bây giờ chúng ta chỉ phải học cách trả lời nhanh các truy vấn giá trị nhỏ nhất trong phạm vi bên trong mỗi khối.
Trên thực tế, nếu truy vấn giá trị nhỏ nhất trong phạm vi nhận được là $[l, r]$ và $l$ và $r$ nằm trong các khối khác nhau thì câu trả lời là giá trị nhỏ nhất của ba giá trị sau:
giá trị nhỏ nhất của phần hậu tố của khối của $l$ bắt đầu tại $l$, giá trị nhỏ nhất của phần tiền tố của khối của $r$ kết thúc tại $r$, và giá trị nhỏ nhất của các khối nằm giữa chúng.
Giá trị nhỏ nhất của các khối ở giữa có thể được trả lời trong $O(1)$ bằng cách sử dụng Bảng thưa.
Vì vậy, điều này chỉ để lại cho chúng ta các truy vấn giá trị nhỏ nhất trong phạm vi bên trong các khối.

Ở đây chúng ta sẽ khai thác tính chất của mảng.
Hãy nhớ rằng các giá trị trong mảng - vốn chỉ là các giá trị độ cao trong cây - sẽ luôn khác nhau một đơn vị.
Nếu chúng ta loại bỏ phần tử đầu tiên của một khối, và trừ nó khỏi mọi phần tử khác trong khối, mỗi khối có thể được xác định bởi một chuỗi có độ dài $K - 1$ bao gồm số $+1$ và $-1$.
Bởi vì các khối này quá nhỏ, chỉ có một vài chuỗi khác nhau có thể xảy ra.
Số lượng chuỗi có thể là:

$$2^{K-1} = 2^{0.5 \log(N) - 1} = 0.5 \left(2^{\log(N)}\right)^{0.5} = 0.5 \sqrt{N}$$

Do đó số lượng các khối khác nhau là $O(\sqrt{N})$, và do đó chúng ta có thể tính toán trước kết quả của các truy vấn giá trị nhỏ nhất trong phạm vi bên trong tất cả các khối khác nhau trong thời gian $O(\sqrt{N} K^2) = O(\sqrt{N} \log^2(N)) = O(N)$.
Để cài đặt, chúng ta có thể đặc trưng hóa một khối bằng một bitmask có độ dài $K-1$ (sẽ vừa trong một int tiêu chuẩn) và lưu trữ chỉ số của giá trị nhỏ nhất trong một mảng $\text{block}[\text{mask}][l][r]$ có kích thước $O(\sqrt{N} \log^2(N))$.

Vì vậy, chúng ta đã học cách tính toán trước các truy vấn giá trị nhỏ nhất trong phạm vi bên trong mỗi khối, cũng như các truy vấn giá trị nhỏ nhất trong phạm vi trên một phạm vi các khối, tất cả trong $O(N)$.
Với các tính toán trước này, chúng ta có thể trả lời mỗi truy vấn trong $O(1)$, bằng cách sử dụng tối đa bốn giá trị được tính toán trước: giá trị nhỏ nhất của khối chứa `l`, giá trị nhỏ nhất của khối chứa `r`, và hai giá trị nhỏ nhất của các đoạn chồng chéo của các khối giữa chúng.

## Cài đặt (Implementation) {: #implementation}

```cpp
int n;
vector<vector<int>> adj;

int block_size, block_cnt;
vector<int> first_visit;
vector<int> euler_tour;
vector<int> height;
vector<int> log_2;
vector<vector<int>> st;
vector<vector<vector<int>>> blocks;
vector<int> block_mask;

void dfs(int v, int p, int h) {
    first_visit[v] = euler_tour.size();
    euler_tour.push_back(v);
    height[v] = h;
    
    for (int u : adj[v]) {
        if (u == p)
            continue;
        dfs(u, v, h + 1);
        euler_tour.push_back(v);
    }
}

int min_by_h(int i, int j) {
    return height[euler_tour[i]] < height[euler_tour[j]] ? i : j;
}

void precompute_lca(int root) {
    // lấy euler tour & chỉ số của lần xuất hiện đầu tiên
    first_visit.assign(n, -1);
    height.assign(n, 0);
    euler_tour.reserve(2 * n);
    dfs(root, -1, 0);

    // tính toán trước tất cả các giá trị log
    int m = euler_tour.size();
    log_2.reserve(m + 1);
    log_2.push_back(-1);
    for (int i = 1; i <= m; i++)
        log_2.push_back(log_2[i / 2] + 1);

    block_size = max(1, log_2[m] / 2);
    block_cnt = (m + block_size - 1) / block_size;

    // tính toán trước giá trị nhỏ nhất của mỗi khối và xây dựng bảng thưa
    st.assign(block_cnt, vector<int>(log_2[block_cnt] + 1));
    for (int i = 0, j = 0, b = 0; i < m; i++, j++) {
        if (j == block_size)
            j = 0, b++;
        if (j == 0 || min_by_h(i, st[b][0]) == i)
            st[b][0] = i;
    }
    for (int l = 1; l <= log_2[block_cnt]; l++) {
        for (int i = 0; i < block_cnt; i++) {
            int ni = i + (1 << (l - 1));
            if (ni >= block_cnt)
                st[i][l] = st[i][l-1];
            else
                st[i][l] = min_by_h(st[i][l-1], st[ni][l-1]);
        }
    }

    // tính toán trước mask cho mỗi khối
    block_mask.assign(block_cnt, 0);
    for (int i = 0, j = 0, b = 0; i < m; i++, j++) {
        if (j == block_size)
            j = 0, b++;
        if (j > 0 && (i >= m || min_by_h(i - 1, i) == i - 1))
            block_mask[b] += 1 << (j - 1);
    }

    // tính toán trước RMQ cho mỗi khối duy nhất
    int possibilities = 1 << (block_size - 1);
    blocks.resize(possibilities);
    for (int b = 0; b < block_cnt; b++) {
        int mask = block_mask[b];
        if (!blocks[mask].empty())
            continue;
        blocks[mask].assign(block_size, vector<int>(block_size));
        for (int l = 0; l < block_size; l++) {
            blocks[mask][l][l] = l;
            for (int r = l + 1; r < block_size; r++) {
                blocks[mask][l][r] = blocks[mask][l][r - 1];
                if (b * block_size + r < m)
                    blocks[mask][l][r] = min_by_h(b * block_size + blocks[mask][l][r], 
                            b * block_size + r) - b * block_size;
            }
        }
    }
}

int lca_in_block(int b, int l, int r) {
    return blocks[block_mask[b]][l][r] + b * block_size;
}

int lca(int v, int u) {
    int l = first_visit[v];
    int r = first_visit[u];
    if (l > r)
        swap(l, r);
    int bl = l / block_size;
    int br = r / block_size;
    if (bl == br)
        return euler_tour[lca_in_block(bl, l % block_size, r % block_size)];
    int ans1 = lca_in_block(bl, l % block_size, block_size - 1);
    int ans2 = lca_in_block(br, 0, r % block_size);
    int ans = min_by_h(ans1, ans2);
    if (bl + 1 < br) {
        int l = log_2[br - bl - 1];
        int ans3 = st[bl+1][l];
        int ans4 = st[br - (1 << l)][l];
        ans = min_by_h(ans, min_by_h(ans3, ans4));
    }
    return euler_tour[ans];
}
```
