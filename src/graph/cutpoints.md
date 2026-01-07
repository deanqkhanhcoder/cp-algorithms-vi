--- 
title: Tìm điểm khớp trong đồ thị trong O(N+M)
tags:
  - Translated
e_maxx_link: cutpoints
---
# Tìm điểm khớp trong đồ thị trong $O(N+M)$

Chúng ta được cho một đồ thị vô hướng. Một điểm khớp (hoặc đỉnh cắt) được định nghĩa là một đỉnh mà khi loại bỏ cùng với các cạnh liên quan, làm cho đồ thị bị ngắt kết nối (hoặc chính xác hơn, làm tăng số lượng thành phần liên thông trong đồ thị). Nhiệm vụ là tìm tất cả các điểm khớp trong đồ thị đã cho.

Thuật toán được mô tả ở đây dựa trên [tìm kiếm theo chiều sâu](depth-first-search.md) và có độ phức tạp $O(N+M)$, trong đó $N$ là số đỉnh và $M$ là số cạnh trong đồ thị.

## Thuật toán

Chọn một đỉnh tùy ý của đồ thị $root$ và chạy [tìm kiếm theo chiều sâu](depth-first-search.md) từ nó. Lưu ý thực tế sau đây (dễ chứng minh):

- Giả sử chúng ta đang ở trong DFS, xem qua các cạnh bắt đầu từ đỉnh $v\ne root$.
Nếu cạnh hiện tại $(v, to)$ sao cho không có đỉnh nào trong số $to$ hoặc các hậu duệ của nó trong cây duyệt DFS có một cạnh ngược đến bất kỳ tổ tiên nào của $v$, thì $v$ là một điểm khớp. Ngược lại, $v$ không phải là một điểm khớp.

- Hãy xem xét trường hợp còn lại của $v=root$.
Đỉnh này sẽ là điểm khớp khi và chỉ khi đỉnh này có nhiều hơn một con trong cây DFS.

Bây giờ chúng ta phải học cách kiểm tra thực tế này cho mỗi đỉnh một cách hiệu quả. Chúng ta sẽ sử dụng "thời gian vào nút" được tính toán bởi tìm kiếm theo chiều sâu.

Vì vậy, gọi $tin[v]$ là thời gian vào nút $v$. Chúng ta giới thiệu một mảng $low[v]$ sẽ cho phép chúng ta kiểm tra thực tế này cho mỗi đỉnh $v$. $low[v]$ là giá trị nhỏ nhất của $tin[v]$, thời gian vào $tin[p]$ cho mỗi nút $p$ được kết nối với nút $v$ thông qua một cạnh ngược $(v, p)$ và các giá trị của $low[to]$ cho mỗi đỉnh $to$ là một hậu duệ trực tiếp của $v$ trong cây DFS:

$$low[v] = \min \begin{cases} tin[v] \\ tin[p] &\text{ cho tất cả }p\text{ mà }(v, p)\text{ là một cạnh ngược} \\ low[to]& \text{ cho tất cả }to\text{ mà }(v, to)\text{ là một cạnh cây} \end{cases}$$

Bây giờ, có một cạnh ngược từ đỉnh $v$ hoặc một trong các hậu duệ của nó đến một trong các tổ tiên của nó khi và chỉ khi đỉnh $v$ có một con $to$ mà $low[to] < tin[v]$. Nếu $low[to] = tin[v]$, cạnh ngược đi trực tiếp đến $v$, nếu không nó sẽ đến một trong các tổ tiên của $v$.

Do đó, đỉnh $v$ trong cây DFS là một điểm khớp khi và chỉ khi $low[to] \geq tin[v]$.

## Cài đặt

Việc triển khai cần phân biệt ba trường hợp: khi chúng ta đi xuống cạnh trong cây DFS, khi chúng ta tìm thấy một cạnh ngược đến một tổ tiên của đỉnh và khi chúng ta trở về cha của một đỉnh. Đây là các trường hợp:

- $visited[to] = false$ - cạnh là một phần của cây DFS;
- $visited[to] = true$ && $to \neq parent$ - cạnh là cạnh ngược đến một trong các tổ tiên;
- $to = parent$ - cạnh dẫn trở lại cha trong cây DFS.

Để thực hiện điều này, chúng ta cần một hàm tìm kiếm theo chiều sâu chấp nhận đỉnh cha của nút hiện tại.

```cpp
int n; // số nút
vector<vector<int>> adj; // danh sách kề của đồ thị

vector<bool> visited;
vector<int> tin, low;
int timer;
 
void dfs(int v, int p = -1) {
    visited[v] = true;
    tin[v] = low[v] = timer++;
    int children=0;
    for (int to : adj[v]) {
        if (to == p) continue;
        if (visited[to]) {
            low[v] = min(low[v], tin[to]);
        } else {
            dfs(to, v);
            low[v] = min(low[v], low[to]);
            if (low[to] >= tin[v] && p!=-1)
                IS_CUTPOINT(v);
            ++children;
        }
    }
    if(p == -1 && children > 1)
        IS_CUTPOINT(v);
}
 
void find_cutpoints() {
    timer = 0;
    visited.assign(n, false);
    tin.assign(n, -1);
    low.assign(n, -1);
    for (int i = 0; i < n; ++i) {
        if (!visited[i])
            dfs (i);
    }
}
```

Hàm chính là `find_cutpoints`; nó thực hiện khởi tạo cần thiết và bắt đầu tìm kiếm theo chiều sâu trong mỗi thành phần liên thông của đồ thị.

Hàm `IS_CUTPOINT(a)` là một hàm nào đó sẽ xử lý việc đỉnh $a$ là một điểm khớp, ví dụ, in nó ra (Cảnh báo rằng hàm này có thể được gọi nhiều lần cho một đỉnh).

## Bài tập thực hành

- [UVA #10199 "Tourist Guide"](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=13&page=show_problem&problem=1140) [độ khó: thấp]
- [UVA #315 "Network"](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=5&page=show_problem&problem=251) [độ khó: thấp]
- [SPOJ - Submerging Islands](http://www.spoj.com/problems/SUBMERGE/)
- [Codeforces - Cutting Figure](https://codeforces.com/problemset/problem/193/A)