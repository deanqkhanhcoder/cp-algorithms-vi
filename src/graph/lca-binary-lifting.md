---
tags:
  - Translated
e_maxx_link: lca_simpler
---

# Tổ tiên chung thấp nhất - Nâng nhị phân (Lowest Common Ancestor - Binary Lifting) {: #lowest-common-ancestor-binary-lifting}

Cho $G$ là một cây.
Đối với mỗi truy vấn có dạng `(u, v)`, chúng ta muốn tìm tổ tiên chung thấp nhất của các nút `u` và `v`, tức là chúng ta muốn tìm một nút `w` nằm trên đường đi từ `u` đến nút gốc, nằm trên đường đi từ `v` đến nút gốc, và nếu có nhiều nút như vậy, chúng ta chọn nút xa nút gốc nhất.
Nói cách khác, nút `w` mong muốn là tổ tiên thấp nhất của `u` và `v`.
Đặc biệt nếu `u` là tổ tiên của `v`, thì `u` là tổ tiên chung thấp nhất của chúng.

Thuật toán được mô tả trong bài viết này sẽ cần $O(N \log N)$ để tiền xử lý cây, và sau đó $O(\log N)$ cho mỗi truy vấn LCA.

## Thuật toán (Algorithm) {: #algorithm}

Đối với mỗi nút, chúng ta sẽ tính toán trước tổ tiên bên trên nó, tổ tiên hai nút bên trên, tổ tiên bốn nút bên trên, v.v.
Hãy lưu trữ chúng trong mảng `up`, tức là `up[i][j]` là tổ tiên thứ `2^j` bên trên nút `i` với `i=1...N`, `j=0...ceil(log(N))`.
Thông tin này cho phép chúng ta nhảy từ bất kỳ nút nào đến bất kỳ tổ tiên nào bên trên nó trong thời gian $O(\log N)$.
Chúng ta có thể tính toán mảng này bằng cách sử dụng duyệt [DFS](depth-first-search.md) trên cây.

Đối với mỗi nút, chúng ta cũng sẽ ghi nhớ thời gian thăm đầu tiên của nút này (tức là thời gian DFS khám phá nút), và thời gian khi chúng ta rời khỏi nó (tức là sau khi chúng ta thăm tất cả các con và thoát khỏi hàm DFS).
Chúng ta có thể sử dụng thông tin này để xác định trong thời gian hằng số nếu một nút là tổ tiên của một nút khác.

Giả sử bây giờ chúng ta nhận được một truy vấn `(u, v)`.
Chúng ta có thể kiểm tra ngay lập tức xem một nút có phải là tổ tiên của nút kia hay không.
Trong trường hợp này, nút này đã là LCA.
Nếu `u` không phải là tổ tiên của `v`, và `v` không phải là tổ tiên của `u`, chúng ta leo lên các tổ tiên của `u` cho đến khi chúng ta tìm thấy nút cao nhất (tức là gần gốc nhất), mà không phải là tổ tiên của `v` (tức là một nút `x`, sao cho `x` không phải là tổ tiên của `v`, nhưng `up[x][0]` thì phải).
Chúng ta có thể tìm thấy nút `x` này trong thời gian $O(\log N)$ bằng cách sử dụng mảng `up`.

Chúng tôi sẽ mô tả quá trình này chi tiết hơn.
Gọi `L = ceil(log(N))`.
Giả sử trước tiên rằng `i = L`.
Nếu `up[u][i]` không phải là tổ tiên của `v`, thì chúng ta có thể gán `u = up[u][i]` và giảm `i`.
Nếu `up[u][i]` là một tổ tiên, thì chúng ta chỉ cần giảm `i`.
Rõ ràng sau khi thực hiện việc này cho tất cả các `i` không âm, nút `u` sẽ là nút mong muốn - tức là `u` vẫn không phải là tổ tiên của `v`, nhưng `up[u][0]` thì phải.

Bây giờ, rõ ràng, câu trả lời cho LCA sẽ là `up[u][0]` - tức là, nút nhỏ nhất trong số các tổ tiên của nút `u`, mà cũng là một tổ tiên của `v`.

Vì vậy, việc trả lời một truy vấn LCA sẽ lặp `i` từ `ceil(log(N))` đến `0` và kiểm tra trong mỗi lần lặp xem một nút có phải là tổ tiên của nút kia hay không.
Do đó, mỗi truy vấn có thể được trả lời trong $O(\log N)$.

## Cài đặt (Implementation) {: #implementation}

```cpp
int n, l;
vector<vector<int>> adj;

int timer;
vector<int> tin, tout;
vector<vector<int>> up;

void dfs(int v, int p)
{
    tin[v] = ++timer;
    up[v][0] = p;
    for (int i = 1; i <= l; ++i)
        up[v][i] = up[up[v][i-1]][i-1];

    for (int u : adj[v]) {
        if (u != p)
            dfs(u, v);
    }

    tout[v] = ++timer;
}

bool is_ancestor(int u, int v)
{
    return tin[u] <= tin[v] && tout[u] >= tout[v];
}

int lca(int u, int v)
{
    if (is_ancestor(u, v))
        return u;
    if (is_ancestor(v, u))
        return v;
    for (int i = l; i >= 0; --i) {
        if (!is_ancestor(up[u][i], v))
            u = up[u][i];
    }
    return up[u][0];
}

void preprocess(int root) {
    tin.resize(n);
    tout.resize(n);
    timer = 0;
    l = ceil(log2(n));
    up.assign(n, vector<int>(l + 1));
    dfs(root, root);
}
```
## Bài tập (Practice Problems) {: #practice-problems}

* [LeetCode -  Kth Ancestor of a Tree Node](https://leetcode.com/problems/kth-ancestor-of-a-tree-node)
* [Codechef - Longest Good Segment](https://www.codechef.com/problems/LGSEG)
* [HackerEarth - Optimal Connectivity](https://www.hackerearth.com/practice/algorithms/graphs/graph-representation/practice-problems/algorithm/optimal-connectivity-c6ae79ca/)
