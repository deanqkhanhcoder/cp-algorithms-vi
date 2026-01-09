---
title: Lowest Common Ancestor - O(sqrt(N)) and O(log N) with O(N) preprocessing
tags:
  - Translated
e_maxx_link: lca
---
# Tổ tiên chung thấp nhất - $O(\sqrt{N})$ và $O(\log N)$ với tiền xử lý $O(N)$ (Lowest Common Ancestor - $O(\sqrt{N})$ and $O(\log N)$ with $O(N)$ preprocessing) {: #lowest-common-ancestor-o-sqrt-n-and-o-log-n-with-o-n-preprocessing}

Cho một cây $G$. Cho các truy vấn có dạng $(v_1, v_2)$, đối với mỗi truy vấn bạn cần tìm tổ tiên chung thấp nhất (hoặc tổ tiên chung nhỏ nhất), tức là một đỉnh $v$ nằm trên đường đi từ gốc đến $v_1$ và đường đi từ gốc đến $v_2$, và đỉnh này phải là thấp nhất. Nói cách khác, đỉnh $v$ mong muốn là tổ tiên gần nhất (most bottom ancestor) của $v_1$ và $v_2$. Rõ ràng là tổ tiên chung thấp nhất của chúng nằm trên đường đi ngắn nhất từ $v_1$ và $v_2$. Ngoài ra, nếu $v_1$ là tổ tiên của $v_2$, thì $v_1$ là tổ tiên chung thấp nhất của chúng.

### Ý tưởng của thuật toán (The Idea of the Algorithm)

Trước khi trả lời các truy vấn, chúng ta cần **tiền xử lý** cây.
Chúng ta thực hiện duyệt [DFS](depth-first-search.md) bắt đầu từ gốc và xây dựng một danh sách $\text{euler}$ lưu trữ thứ tự các đỉnh mà chúng ta thăm (một đỉnh được thêm vào danh sách khi chúng ta lần đầu tiên thăm nó, và sau khi quay lại từ các lần duyệt DFS đến con của nó).
Đây cũng được gọi là một Euler tour của cây.
Rõ ràng kích thước của danh sách này sẽ là $O(N)$.
Chúng ta cũng cần xây dựng một mảng $\text{first}[0..N-1]$ lưu trữ lần xuất hiện đầu tiên của mỗi đỉnh $i$ trong $\text{euler}$.
Nghĩa là, vị trí đầu tiên trong $\text{euler}$ sao cho $\text{euler}[\text{first}[i]] = i$.
Ngoài ra bằng cách sử dụng DFS chúng ta có thể tìm độ cao của mỗi nút (khoảng cách từ gốc đến nó) và lưu trữ nó trong mảng $\text{height}[0..N-1]$.

Vậy làm thế nào chúng ta có thể trả lời các truy vấn bằng cách sử dụng Euler tour và hai mảng bổ sung?
Giả sử truy vấn là một cặp $v_1$ và $v_2$.
Xem xét các đỉnh mà chúng ta thăm trong Euler tour giữa lần thăm đầu tiên của $v_1$ và lần thăm đầu tiên của $v_2$.
Dễ dàng nhận thấy rằng, $\text{LCA}(v_1, v_2)$ là đỉnh có độ cao thấp nhất trên đường đi này.
Chúng ta đã nhận thấy rằng, LCA phải là một phần của đường đi ngắn nhất giữa $v_1$ và $v_2$.
Rõ ràng nó cũng phải là đỉnh có độ cao nhỏ nhất.
Và trong Euler tour chúng ta về cơ bản sử dụng đường đi ngắn nhất, ngoại trừ việc chúng ta thăm thêm tất cả các cây con mà chúng ta tìm thấy trên đường đi.
Nhưng tất cả các đỉnh trong các cây con này đều thấp hơn trong cây so với LCA và do đó có độ cao lớn hơn.
Vì vậy $\text{LCA}(v_1, v_2)$ có thể được xác định duy nhất bằng cách tìm đỉnh có độ cao nhỏ nhất trong Euler tour giữa $\text{first}(v_1)$ và $\text{first}(v_2)$.

Hãy minh họa ý tưởng này.
Xem xét đồ thị sau và Euler tour với các độ cao tương ứng:
<div style="text-align: center;">
  <img src="LCA_Euler.png" alt="LCA_Euler_Tour">
</div>

$$\begin{array}{|l|c|c|c|c|c|c|c|c|c|c|c|c|c|}
\hline
\text{Vertices:}   & 1 & 2 & 5 & 2 & 6 & 2 & 1 & 3 & 1 & 4 & 7 & 4 & 1 \\ \hline
\text{Heights:} & 1 & 2 & 3 & 2 & 3 & 2 & 1 & 2 & 1 & 2 & 3 & 2 & 1 \\ \hline
\end{array}$$

Tour bắt đầu tại đỉnh $6$ và kết thúc tại $4$ chúng ta thăm các đỉnh $[6, 2, 1, 3, 1, 4]$.
Trong số các đỉnh đó, đỉnh $1$ có độ cao thấp nhất, do đó $\text{LCA(6, 4) = 1}$.

Tóm tắt lại:
để trả lời một truy vấn chúng ta chỉ cần **tìm đỉnh có độ cao nhỏ nhất** trong mảng $\text{euler}$ trong phạm vi từ $\text{first}[v_1]$ đến $\text{first}[v_2]$.
Do đó, **bài toán LCA được quy về bài toán RMQ** (tìm giá trị nhỏ nhất trong một phạm vi).

Sử dụng [Phân rã căn bậc hai (Sqrt-Decomposition)](../data_structures/sqrt-decomposition.md), có thể thu được một giải pháp trả lời mỗi truy vấn trong $O(\sqrt{N})$ với tiền xử lý trong thời gian $O(N)$.

Sử dụng [Segment Tree](../data_structures/segment-tree.md) bạn có thể trả lời mỗi truy vấn trong $O(\log N)$ với tiền xử lý trong thời gian $O(N)$.

Vì hầu như sẽ không bao giờ có bất kỳ cập nhật nào cho các giá trị được lưu trữ, [Bảng thưa (Sparse Table)](../data_structures/sparse-table.md) có thể là một lựa chọn tốt hơn, cho phép trả lời truy vấn $O(1)$ với thời gian xây dựng $O(N\log N)$.

### Cài đặt (Implementation) {: #implementation}

Trong cài đặt LCA sau đây, Segment Tree được sử dụng.
```cpp title="lca"
struct LCA {
    vector<int> height, euler, first, segtree;
    vector<bool> visited;
    int n;

    LCA(vector<vector<int>> &adj, int root = 0) {
        n = adj.size();
        height.resize(n);
        first.resize(n);
        euler.reserve(n * 2);
        visited.assign(n, false);
        dfs(adj, root);
        int m = euler.size();
        segtree.resize(m * 4);
        build(1, 0, m - 1);
    }

    void dfs(vector<vector<int>> &adj, int node, int h = 0) {
        visited[node] = true;
        height[node] = h;
        first[node] = euler.size();
        euler.push_back(node);
        for (auto to : adj[node]) {
            if (!visited[to]) {
                dfs(adj, to, h + 1);
                euler.push_back(node);
            }
        }
    }

    void build(int node, int b, int e) {
        if (b == e) {
            segtree[node] = euler[b];
        } else {
            int mid = (b + e) / 2;
            build(node << 1, b, mid);
            build(node << 1 | 1, mid + 1, e);
            int l = segtree[node << 1], r = segtree[node << 1 | 1];
            segtree[node] = (height[l] < height[r]) ? l : r;
        }
    }

    int query(int node, int b, int e, int L, int R) {
        if (b > R || e < L)
            return -1;
        if (b >= L && e <= R)
            return segtree[node];
        int mid = (b + e) >> 1;

        int left = query(node << 1, b, mid, L, R);
        int right = query(node << 1 | 1, mid + 1, e, L, R);
        if (left == -1) return right;
        if (right == -1) return left;
        return height[left] < height[right] ? left : right;
    }

    int lca(int u, int v) {
        int left = first[u], right = first[v];
        if (left > right)
            swap(left, right);
        return query(1, 0, euler.size() - 1, left, right);
    }
};

```

## Bài tập (Practice Problems) {: #practice-problems}

 - [SPOJ: LCA](http://www.spoj.com/problems/LCA/)
 - [SPOJ: DISQUERY](http://www.spoj.com/problems/DISQUERY/)
 - [TIMUS: 1471. Distance in the Tree](http://acm.timus.ru/problem.aspx?space=1&num=1471)
 - [CODEFORCES: Design Tutorial: Inverse the Problem](http://codeforces.com/problemset/problem/472/D)
 - [CODECHEF: Lowest Common Ancestor](https://www.codechef.com/problems/TALCA)
 * [SPOJ - Lowest Common Ancestor](http://www.spoj.com/problems/LCASQ/)
 * [SPOJ - Ada and Orange Tree](http://www.spoj.com/problems/ADAORANG/)
 * [DevSkill - Motoku (archived)](http://web.archive.org/web/20200922005503/https://devskill.com/CodingProblems/ViewProblem/141)
 * [UVA 12655 - Trucks](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=4384)
 * [Codechef - Pishty and Tree](https://www.codechef.com/problems/PSHTTR)
 * [UVA - 12533 - Joining Couples](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=441&page=show_problem&problem=3978)
 * [Codechef - So close yet So Far](https://www.codechef.com/problems/CLOSEFAR)
 * [Codeforces - Drivers Dissatisfaction](http://codeforces.com/contest/733/problem/F)
 * [UVA 11354 - Bond](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2339)
 * [SPOJ - Querry on a tree II](http://www.spoj.com/problems/QTREE2/)
 * [Codeforces - Best Edge Weight](http://codeforces.com/contest/828/problem/F)
 * [Codeforces - Misha, Grisha and Underground](http://codeforces.com/contest/832/problem/D)
 * [SPOJ - Nlogonian Tickets](http://www.spoj.com/problems/NTICKETS/)
 * [Codeforces - Rowena Rawenclaws Diadem](http://codeforces.com/contest/855/problem/D)
