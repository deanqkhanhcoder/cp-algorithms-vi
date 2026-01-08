---
tags:
  - Translated
e_maxx_link: tree_painting
---

# Tô màu các cạnh của cây (Paint the edges of the tree) {: #paint-the-edges-of-the-tree}

Đây là một nhiệm vụ khá phổ biến. Cho một cây $G$ với $N$ đỉnh. Có hai loại truy vấn: truy vấn đầu tiên là tô màu một cạnh, truy vấn thứ hai là truy vấn số lượng cạnh được tô màu giữa hai đỉnh.

Ở đây chúng ta sẽ mô tả một giải pháp khá đơn giản (sử dụng [segment tree](../data_structures/segment_tree.md)) sẽ trả lời mỗi truy vấn trong thời gian $O(\log N)$.
Bước tiền xử lý sẽ mất thời gian $O(N)$.

## Thuật toán (Algorithm) {: #algorithm}

Đầu tiên, chúng ta cần tìm [LCA](lca.md) để giảm mỗi truy vấn loại thứ hai $(i,j)$ thành hai truy vấn $(l,i)$ và $(l,j)$, trong đó $l$ là LCA của $i$ và $j$.
Câu trả lời của truy vấn $(i,j)$ sẽ là tổng của cả hai truy vấn con.
Cả hai truy vấn này đều có cấu trúc đặc biệt, đỉnh đầu tiên là tổ tiên của đỉnh thứ hai.
Trong phần còn lại của bài viết, chúng ta sẽ chỉ nói về loại truy vấn đặc biệt này.

Chúng ta sẽ bắt đầu bằng cách mô tả bước **tiền xử lý**.
Chạy tìm kiếm theo chiều sâu (DFS) từ gốc của cây và ghi lại Euler tour của tìm kiếm theo chiều sâu này (mỗi đỉnh được thêm vào danh sách khi tìm kiếm thăm nó lần đầu tiên và mỗi lần chúng ta quay lại từ một trong các con của nó).
Kỹ thuật tương tự có thể được sử dụng trong tiền xử lý LCA.

Danh sách này sẽ chứa mỗi cạnh (theo nghĩa là nếu $i$ và $j$ là các đầu của cạnh, thì sẽ có một chỗ trong danh sách mà $i$ và $j$ là hàng xóm trong danh sách), và nó xuất hiện chính xác hai lần: theo hướng thuận (từ $i$ đến $j$, trong đó đỉnh $i$ gần gốc hơn đỉnh $j$) và theo hướng ngược lại (từ $j$ đến $i$).

Chúng ta sẽ xây dựng hai danh sách cho các cạnh này.
Danh sách đầu tiên sẽ lưu trữ màu của tất cả các cạnh theo hướng thuận, và danh sách thứ hai lưu trữ màu của tất cả các cạnh theo hướng ngược lại.
Chúng ta sẽ sử dụng $1$ nếu cạnh được tô màu, và $0$ nếu ngược lại.
Trên hai danh sách này, chúng ta sẽ xây dựng mỗi danh sách một cây phân đoạn (segment tree) (cho tổng với một sửa đổi đơn lẻ), hãy gọi chúng là $T1$ và $T2$.

Hãy để chúng tôi trả lời một truy vấn có dạng $(i,j)$, trong đó $i$ là tổ tiên của $j$.
Chúng ta cần xác định có bao nhiêu cạnh được tô màu trên đường đi giữa $i$ và $j$.
Hãy tìm $i$ và $j$ trong Euler tour lần đầu tiên, giả sử đó là các vị trí $p$ và $q$ (việc này có thể được thực hiện trong $O(1)$ nếu chúng ta tính toán các vị trí này trước trong quá trình tiền xử lý).
Khi đó **câu trả lời** cho truy vấn là tổng $T1[p..q-1]$ trừ đi tổng $T2[p..q-1]$.

**Tại sao?**
Xem xét đoạn $[p;q]$ trong Euler tour.
Nó chứa tất cả các cạnh của đường đi chúng ta cần từ $i$ đến $j$ nhưng cũng chứa một tập hợp các cạnh nằm trên các đường đi khác từ $i$.
Tuy nhiên, có một sự khác biệt lớn giữa các cạnh chúng ta cần và các cạnh còn lại: các cạnh chúng ta cần sẽ chỉ được liệt kê một lần theo hướng thuận, và tất cả các cạnh khác xuất hiện hai lần: một lần theo hướng thuận và một lần theo hướng ngược lại.
Do đó, hiệu $T1[p..q-1] - T2[p..q-1]$ sẽ cho chúng ta câu trả lời chính xác (trừ một là cần thiết vì nếu không, chúng ta sẽ bắt thêm một cạnh đi ra từ đỉnh $j$).
Truy vấn tổng trong segment tree được thực hiện trong $O(\log N)$.

Trả lời **loại truy vấn đầu tiên** (tô màu một cạnh) thậm chí còn dễ dàng hơn - chúng ta chỉ cần cập nhật $T1$ và $T2$, cụ thể là thực hiện một bản cập nhật duy nhất của phần tử tương ứng với cạnh của chúng ta (tìm cạnh trong danh sách, một lần nữa, là có thể trong $O(1)$, nếu bạn thực hiện tìm kiếm này trong quá trình tiền xử lý).
Một sửa đổi đơn lẻ trong segment tree được thực hiện trong $O(\log N)$.

## Cài đặt (Implementation) {: #implementation}

Dưới đây là cài đặt đầy đủ của giải pháp, bao gồm cả tính toán LCA:

```cpp
const int INF = 1000 * 1000 * 1000;

typedef vector<vector<int>> graph;

vector<int> dfs_list;
vector<int> edges_list;
vector<int> h;

void dfs(int v, const graph& g, const graph& edge_ids, int cur_h = 1) {
    h[v] = cur_h;
    dfs_list.push_back(v);
    for (size_t i = 0; i < g[v].size(); ++i) {
        if (h[g[v][i]] == -1) {
            edges_list.push_back(edge_ids[v][i]);
            dfs(g[v][i], g, edge_ids, cur_h + 1);
            edges_list.push_back(edge_ids[v][i]);
            dfs_list.push_back(v);
        }
    }
}

vector<int> lca_tree;
vector<int> first;

void lca_tree_build(int i, int l, int r) {
    if (l == r) {
        lca_tree[i] = dfs_list[l];
    } else {
        int m = (l + r) >> 1;
        lca_tree_build(i + i, l, m);
        lca_tree_build(i + i + 1, m + 1, r);
        int lt = lca_tree[i + i], rt = lca_tree[i + i + 1];
        lca_tree[i] = h[lt] < h[rt] ? lt : rt;
    }
}

void lca_prepare(int n) {
    lca_tree.assign(dfs_list.size() * 8, -1);
    lca_tree_build(1, 0, (int)dfs_list.size() - 1);

    first.assign(n, -1);
    for (int i = 0; i < (int)dfs_list.size(); ++i) {
        int v = dfs_list[i];
        if (first[v] == -1)
            first[v] = i;
    }
}

int lca_tree_query(int i, int tl, int tr, int l, int r) {
    if (tl == l && tr == r)
        return lca_tree[i];
    int m = (tl + tr) >> 1;
    if (r <= m)
        return lca_tree_query(i + i, tl, m, l, r);
    if (l > m)
        return lca_tree_query(i + i + 1, m + 1, tr, l, r);
    int lt = lca_tree_query(i + i, tl, m, l, m);
    int rt = lca_tree_query(i + i + 1, m + 1, tr, m + 1, r);
    return h[lt] < h[rt] ? lt : rt;
}

int lca(int a, int b) {
    if (first[a] > first[b])
        swap(a, b);
    return lca_tree_query(1, 0, (int)dfs_list.size() - 1, first[a], first[b]);
}

vector<int> first1, first2;
vector<char> edge_used;
vector<int> tree1, tree2;

void query_prepare(int n) {
    first1.resize(n - 1, -1);
    first2.resize(n - 1, -1);
    for (int i = 0; i < (int)edges_list.size(); ++i) {
        int j = edges_list[i];
        if (first1[j] == -1)
            first1[j] = i;
        else
            first2[j] = i;
    }

    edge_used.resize(n - 1);
    tree1.resize(edges_list.size() * 8);
    tree2.resize(edges_list.size() * 8);
}

void sum_tree_update(vector<int>& tree, int i, int l, int r, int j, int delta) {
    tree[i] += delta;
    if (l < r) {
        int m = (l + r) >> 1;
        if (j <= m)
            sum_tree_update(tree, i + i, l, m, j, delta);
        else
            sum_tree_update(tree, i + i + 1, m + 1, r, j, delta);
    }
}

int sum_tree_query(const vector<int>& tree, int i, int tl, int tr, int l, int r) {
    if (l > r || tl > tr)
        return 0;
    if (tl == l && tr == r)
        return tree[i];
    int m = (tl + tr) >> 1;
    if (r <= m)
        return sum_tree_query(tree, i + i, tl, m, l, r);
    if (l > m)
        return sum_tree_query(tree, i + i + 1, m + 1, tr, l, r);
    return sum_tree_query(tree, i + i, tl, m, l, m) +
           sum_tree_query(tree, i + i + 1, m + 1, tr, m + 1, r);
}

int query(int v1, int v2) {
    return sum_tree_query(tree1, 1, 0, (int)edges_list.size() - 1, first[v1], first[v2] - 1) -
           sum_tree_query(tree2, 1, 0, (int)edges_list.size() - 1, first[v1], first[v2] - 1);
}

int main() {
    // reading the graph
    int n;
    scanf("%d", &n);
    graph g(n), edge_ids(n);
    for (int i = 0; i < n - 1; ++i) {
        int v1, v2;
        scanf("%d%d", &v1, &v2);
        --v1, --v2;
        g[v1].push_back(v2);
        g[v2].push_back(v1);
        edge_ids[v1].push_back(i);
        edge_ids[v2].push_back(i);
    }

    h.assign(n, -1);
    dfs(0, g, edge_ids);
    lca_prepare(n);
    query_prepare(n);

    for (;;) {
        if () {
            // request for painting edge x;
            // if start = true, then the edge is painted, otherwise the painting
            // is removed
            edge_used[x] = start;
            sum_tree_update(tree1, 1, 0, (int)edges_list.size() - 1, first1[x],
                            start ? 1 : -1);
            sum_tree_update(tree2, 1, 0, (int)edges_list.size() - 1, first2[x],
                            start ? 1 : -1);
        } else {
            // query the number of colored edges on the path between v1 and v2
            int l = lca(v1, v2);
            int result = query(l, v1) + query(l, v2);
            // result - the answer to the request
        }
    }
}
```
