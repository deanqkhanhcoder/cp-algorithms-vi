---
title: Tìm cầu trong đồ thị (Finding bridges in a graph in O(N+M))
tags:
  - Translated
e_maxx_link: bridge_searching
---

# Tìm cầu trong đồ thị $O(N+M)$ (Finding bridges in a graph in $O(N+M)$) {: #finding-bridges-in-a-graph-in-o-n-m}

Chúng ta được cho một đồ thị vô hướng. Một cạnh cầu (bridge) được định nghĩa là một cạnh mà khi bị loại bỏ, làm cho đồ thị mất liên thông (hoặc chính xác hơn là làm tăng số lượng các thành phần liên thông trong đồ thị). Nhiệm vụ là tìm tất cả các cầu trong đồ thị đã cho.

Một cách không chính thức, bài toán được phát biểu như sau: cho một bản đồ các thành phố được kết nối với nhau bằng các con đường, hãy tìm tất cả các con đường "quan trọng", tức là các con đường mà khi bị loại bỏ, sẽ làm mất đi đường đi giữa một cặp thành phố nào đó.

Thuật toán được mô tả ở đây dựa trên [tìm kiếm theo chiều sâu](depth-first-search.md) và có độ phức tạp $O(N+M)$, trong đó $N$ là số lượng đỉnh và $M$ là số lượng cạnh trong đồ thị.

Lưu ý rằng cũng có bài viết [Tìm Cầu Online](bridge-searching-online.md) - không giống như thuật toán offline được mô tả ở đây, thuật toán online có thể duy trì danh sách tất cả các cầu trong một đồ thị đang thay đổi (với giả định rằng loại thay đổi duy nhất là thêm các cạnh mới).

## Thuật toán (Algorithm) {: #algorithm}

Chọn một đỉnh bất kỳ của đồ thị làm $root$ và chạy [tìm kiếm theo chiều sâu](depth-first-search.md) từ nó. Lưu ý thực tế sau đây (dễ dàng chứng minh):

- Giả sử chúng ta đang ở trong DFS, xem xét các cạnh bắt đầu từ đỉnh $v$. Cạnh hiện tại $(v, to)$ là một cầu khi và chỉ khi không có đỉnh nào trong số các đỉnh $to$ và các hậu duệ của nó trong cây duyệt DFS có cạnh ngược (back-edge) đến đỉnh $v$ hoặc bất kỳ tổ tiên nào của nó. Thật vậy, điều kiện này có nghĩa là không có cách nào khác từ $v$ đến $to$ ngoại trừ cạnh $(v, to)$.

Bây giờ chúng ta phải học cách kiểm tra thực tế này cho mỗi đỉnh một cách hiệu quả. Chúng ta sẽ sử dụng "thời gian vào nút" (time of entry into node) được tính toán bởi tìm kiếm theo chiều sâu.

Vì vậy, hãy để $\mathtt{tin}[v]$ biểu thị thời gian vào nút $v$. Chúng ta giới thiệu một mảng $\mathtt{low}$ cho phép chúng ta lưu trữ thời gian vào sớm nhất của nút được tìm thấy trong tìm kiếm DFS mà một nút $v$ có thể truy cập với một cạnh duy nhất từ chính nó hoặc các hậu duệ của nó. $\mathtt{low}[v]$ là giá trị nhỏ nhất của $\mathtt{tin}[v]$, thời gian vào $\mathtt{tin}[p]$ cho mỗi nút $p$ được kết nối với nút $v$ thông qua một cạnh ngược $(v, p)$ và các giá trị của $\mathtt{low}[to]$ cho mỗi đỉnh $to$ là hậu duệ trực tiếp của $v$ trong cây DFS:

$$\mathtt{low}[v] = \min \left\{ 
    \begin{array}{l}
    \mathtt{tin}[v] \\ 
    \mathtt{tin}[p]  &\text{ cho tất cả }p\text{ mà }(v, p)\text{ là một cạnh ngược} \\ 
    \mathtt{low}[to] &\text{ cho tất cả }to\text{ mà }(v, to)\text{ là một cạnh cây}
    \end{array}
\right\}$$

Bây giờ, có một cạnh ngược từ đỉnh $v$ hoặc một trong những hậu duệ của nó đến một trong những tổ tiên của nó khi và chỉ khi đỉnh $v$ có một đứa con $to$ mà $\mathtt{low}[to] \leq \mathtt{tin}[v]$. Nếu $\mathtt{low}[to] = \mathtt{tin}[v]$, cạnh ngược đi trực tiếp đến $v$, ngược lại nó đi đến một trong các tổ tiên của $v$.

Do đó, cạnh hiện tại $(v, to)$ trong cây DFS là một cầu khi và chỉ khi $\mathtt{low}[to] > \mathtt{tin}[v]$.

## Cài đặt (Implementation) {: #implementation}

Cài đặt cần phân biệt ba trường hợp: khi chúng ta đi xuống cạnh trong cây DFS, khi chúng ta tìm thấy một cạnh ngược đến tổ tiên của đỉnh và khi chúng ta quay trở lại cha của đỉnh. Đây là các trường hợp:

- $\mathtt{visited}[to] = false$ - cạnh là một phần của cây DFS;
- $\mathtt{visited}[to] = true$ && $to \neq parent$ - cạnh là cạnh ngược đến một trong các tổ tiên;
- $to = parent$ - cạnh dẫn quay lại cha trong cây DFS.

Để cài đặt điều này, chúng ta cần một hàm tìm kiếm theo chiều sâu chấp nhận đỉnh cha của nút hiện tại.

Đối với các trường hợp đa cạnh (multiple edges), chúng ta cần cẩn thận khi bỏ qua cạnh từ cha. Để giải quyết vấn đề này, chúng ta có thể thêm một cờ `parent_skipped` để đảm bảo chúng ta chỉ bỏ qua cha một lần.

```{.cpp file=bridge_searching_offline}
void IS_BRIDGE(int v,int to); // một số hàm để xử lý cầu được tìm thấy
int n; // số lượng nút
vector<vector<int>> adj; // danh sách kề của đồ thị

vector<bool> visited;
vector<int> tin, low;
int timer;
 
void dfs(int v, int p = -1) {
    visited[v] = true;
    tin[v] = low[v] = timer++;
    bool parent_skipped = false;
    for (int to : adj[v]) {
        if (to == p && !parent_skipped) {
            parent_skipped = true;
            continue;
        }
        if (visited[to]) {
            low[v] = min(low[v], tin[to]);
        } else {
            dfs(to, v);
            low[v] = min(low[v], low[to]);
            if (low[to] > tin[v])
                IS_BRIDGE(v, to);
        }
    }
}
 
void find_bridges() {
    timer = 0;
    visited.assign(n, false);
    tin.assign(n, -1);
    low.assign(n, -1);
    for (int i = 0; i < n; ++i) {
        if (!visited[i])
            dfs(i);
    }
}
```

Hàm chính là `find_bridges`; nó thực hiện khởi tạo cần thiết và bắt đầu tìm kiếm theo chiều sâu trong mỗi thành phần liên thông của đồ thị.

Hàm `IS_BRIDGE(a, b)` là một số hàm sẽ xử lý thực tế rằng cạnh $(a, b)$ là một cầu, ví dụ, in nó ra.

Lưu ý rằng cài đặt này hoạt động sai nếu đồ thị có đa cạnh, vì nó bỏ qua chúng. Tất nhiên, đa cạnh sẽ không bao giờ là một phần của câu trả lời, vì vậy `IS_BRIDGE` có thể kiểm tra thêm rằng cầu được báo cáo không phải là đa cạnh. Ngoài ra, có thể chuyển cho `dfs` chỉ số của cạnh được sử dụng để vào đỉnh thay vì đỉnh cha (và lưu trữ chỉ số của tất cả các đỉnh).

## Bài tập (Practice Problems) {: #practice-problems}

- [UVA #796 "Critical Links"](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=737) [difficulty: low]
- [UVA #610 "Street Directions"](http://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=551) [difficulty: medium]
- [Case of the Computer Network (Codeforces Round #310 Div. 1 E)](http://codeforces.com/problemset/problem/555/E) [difficulty: hard]
* [UVA 12363 - Hedge Mazes](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=3785)
* [UVA 315 - Network](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=251)
* [GYM - Computer Network (J)](http://codeforces.com/gym/100114)
* [SPOJ - King Graffs Defense](http://www.spoj.com/problems/GRAFFDEF/)
* [SPOJ - Critical Edges](http://www.spoj.com/problems/EC_P/)
* [Codeforces - Break Up](http://codeforces.com/contest/700/problem/C)
* [Codeforces - Tourist Reform](http://codeforces.com/contest/732/problem/F)
* [Codeforces - Non-academic problem](https://codeforces.com/contest/1986/problem/F)
