---
tags:
  - Translated
e_maxx_link: lca_linear_offline
---

# Tổ tiên chung thấp nhất - Thuật toán off-line của Tarjan (Lowest Common Ancestor - Tarjan's off-line algorithm) {: #lowest-common-ancestor-tarjans-off-line-algorithm}

Chúng ta có một cây $G$ với $n$ nút và chúng ta có $m$ truy vấn có dạng $(u, v)$.
Đối với mỗi truy vấn $(u, v)$ chúng ta muốn tìm tổ tiên chung thấp nhất của các đỉnh $u$ và $v$, tức là nút là tổ tiên của cả $u$ và $v$ và có độ sâu lớn nhất trong cây.
Nút $v$ cũng là tổ tiên của $v$, vì vậy LCA cũng có thể là một trong hai nút.

Trong bài viết này, chúng ta sẽ giải quyết bài toán off-line, tức là chúng ta giả định rằng tất cả các truy vấn đều được biết trước, và do đó chúng ta trả lời các truy vấn theo bất kỳ thứ tự nào chúng ta muốn.
Thuật toán sau đây cho phép trả lời tất cả $m$ truy vấn trong tổng thời gian $O(n + m)$, tức là với $m$ đủ lớn trong $O(1)$ cho mỗi truy vấn.

## Thuật toán (Algorithm) {: #algorithm}

Thuật toán được đặt theo tên của Robert Tarjan, người đã phát hiện ra nó vào năm 1979 và cũng có nhiều đóng góp khác cho cấu trúc dữ liệu [Disjoint Set Union](../data_structures/disjoint-set-union.md), vốn sẽ được sử dụng rất nhiều trong thuật toán này.

Thuật toán trả lời tất cả các truy vấn bằng một lần duyệt [DFS](depth-first-search.md) trên cây.
Cụ thể, một truy vấn $(u, v)$ được trả lời tại nút $u$, nếu nút $v$ đã được thăm trước đó, hoặc ngược lại.

Vì vậy, giả sử chúng ta hiện đang ở nút $v$, chúng ta đã thực hiện các lệnh gọi DFS đệ quy, và cũng đã thăm nút thứ hai $u$ từ truy vấn $(u, v)$.
Chúng ta hãy tìm hiểu cách tìm LCA của hai nút này.

Lưu ý rằng $\text{LCA}(u, v)$ là nút $v$ hoặc một trong các tổ tiên của nó.
Vì vậy, chúng ta cần tìm nút thấp nhất trong số các tổ tiên của $v$ (bao gồm cả $v$), mà nút $u$ là hậu duệ của nó.
Cũng lưu ý rằng đối với một $v$ cố định, các nút đã thăm của cây chia thành một tập hợp các tập hợp rời rạc.
Mỗi tổ tiên $p$ của nút $v$ có tập hợp riêng chứa nút này và tất cả các cây con có gốc trong số các con của nó không phải là một phần của đường đi từ $v$ đến gốc của cây.
Tập hợp chứa nút $u$ xác định $\text{LCA}(u, v)$:
LCA là đại diện của tập hợp, cụ thể là nút nằm trên đường đi giữa $v$ và gốc của cây.

Chúng ta chỉ cần học cách duy trì hiệu quả tất cả các tập hợp này.
Cho mục đích này, chúng ta áp dụng cấu trúc dữ liệu DSU.
Để có thể áp dụng Union by rank, chúng ta lưu trữ đại diện thực (giá trị trên đường đi giữa $v$ và gốc của cây) của mỗi tập hợp trong mảng `ancestor`.

Chúng ta hãy thảo luận về việc cài đặt DFS.
Giả sử chúng ta đang thăm nút $v$.
Chúng ta đặt nút vào một tập hợp mới trong DSU, `ancestor[v] = v`.
Như thường lệ chúng ta xử lý tất cả các con của $v$.
Để làm điều này, trước tiên chúng ta phải gọi đệ quy DFS từ nút đó, và sau đó thêm nút này cùng với tất cả cây con của nó vào tập hợp của $v$.
Điều này có thể được thực hiện với hàm `union_sets` và phép gán sau `ancestor[find_set(v)] = v` (điều này là cần thiết, vì `union_sets` có thể thay đổi đại diện của tập hợp).

Cuối cùng sau khi xử lý tất cả các con, chúng ta có thể trả lời tất cả các truy vấn có dạng $(u, v)$ mà $u$ đã được thăm.
Câu trả lời cho truy vấn, tức là LCA của $u$ và $v$, sẽ là nút `ancestor[find_set(u)]`.
Dễ dàng thấy rằng một truy vấn sẽ chỉ được trả lời một lần.

Chúng ta hãy xác định độ phức tạp thời gian của thuật toán này.
Đầu tiên chúng ta có $O(n)$ vì DFS.
Thứ hai chúng ta có các lệnh gọi hàm của `union_sets` xảy ra $n$ lần, cũng dẫn đến $O(n)$.
Và thứ ba chúng ta có các lệnh gọi `find_set` cho mỗi truy vấn, điều này mang lại $O(m)$.
Vì vậy, tổng độ phức tạp thời gian là $O(n + m)$, có nghĩa là với $m$ đủ lớn, điều này tương ứng với $O(1)$ để trả lời một truy vấn.

## Cài đặt (Implementation) {: #implementation}

Dưới đây là một cài đặt của thuật toán này.
Việc cài đặt DSU đã không được bao gồm, vì nó có thể được sử dụng mà không cần sửa đổi gì.

```cpp
vector<vector<int>> adj;
vector<vector<int>> queries;
vector<int> ancestor;
vector<bool> visited;

void dfs(int v)
{
    visited[v] = true;
    ancestor[v] = v;
    for (int u : adj[v]) {
        if (!visited[u]) {
            dfs(u);
            union_sets(v, u);
            ancestor[find_set(v)] = v;
        }
    }
    for (int other_node : queries[v]) {
        if (visited[other_node])
            cout << "LCA of " << v << " and " << other_node
                 << " is " << ancestor[find_set(other_node)] << ".\n";
    }
}

void compute_LCAs() {
    // khởi tạo n, adj và DSU
    // for (each query (u, v)) {
    //    queries[u].push_back(v);
    //    queries[v].push_back(u);
    // }

    ancestor.resize(n);
    visited.assign(n, false);
    dfs(0);
}
```
