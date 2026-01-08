---
tags:
  - Translated
e_maxx_link: topological_sort
---

# Sắp xếp Topo (Topological Sorting) {: #topological-sorting}

Bạn được cho một đồ thị có hướng với $n$ đỉnh và $m$ cạnh.
Bạn phải tìm một **thứ tự của các đỉnh**, sao cho mọi cạnh đều dẫn từ đỉnh có chỉ số nhỏ hơn đến đỉnh có chỉ số lớn hơn.

Nói cách khác, bạn muốn tìm một hoán vị của các đỉnh (**thứ tự topo**) tương ứng với thứ tự được xác định bởi tất cả các cạnh của đồ thị.

Dưới đây là một đồ thị đã cho cùng với thứ tự topo của nó:

<div style="text-align: center;">
  <img src="topological_1.png" alt="example directed graph">
  <img src="topological_2.png" alt="one topological order">
</div>

Thứ tự topo có thể là **không duy nhất** (ví dụ, nếu tồn tại ba đỉnh $a$, $b$, $c$ mà có các đường đi từ $a$ đến $b$ và từ $a$ đến $c$ nhưng không có đường đi từ $b$ đến $c$ hoặc từ $c$ đến $b$).
Đồ thị ví dụ cũng có nhiều thứ tự topo, thứ tự topo thứ hai như sau:
<div style="text-align: center;">
  <img src="topological_3.png" alt="second topological order">
</div>

Thứ tự topo có thể **không tồn tại** chút nào.
Nó chỉ tồn tại nếu đồ thị có hướng không chứa chu trình.
Ngược lại, có một mâu thuẫn: nếu có một chu trình chứa các đỉnh $a$ và $b$, thì $a$ cần có chỉ số nhỏ hơn $b$ (vì bạn có thể tiếp cận $b$ từ $a$) và cũng lớn hơn (vì bạn có thể tiếp cận $a$ từ $b$).
Thuật toán được mô tả trong bài viết này cũng cho thấy bằng cách xây dựng, rằng mọi đồ thị có hướng không có chu trình (DAG) đều chứa ít nhất một thứ tự topo.

Một bài toán phổ biến trong đó sắp xếp topo xảy ra là như sau. Có $n$ biến với các giá trị chưa biết. Đối với một số biến, chúng ta biết rằng biến này nhỏ hơn biến kia. Bạn phải kiểm tra xem các ràng buộc này có mâu thuẫn hay không, và nếu không, hãy xuất ra các biến theo thứ tự tăng dần (nếu có thể có nhiều câu trả lời, hãy xuất ra bất kỳ câu trả lời nào). Dễ dàng nhận thấy rằng đây chính xác là bài toán tìm thứ tự topo của một đồ thị với $n$ đỉnh.

## Thuật toán (The Algorithm) {: #the-algorithm}

Để giải quyết bài toán này, chúng ta sẽ sử dụng [tìm kiếm theo chiều sâu](depth-first-search.md).

Giả sử rằng đồ thị không có chu trình. Tìm kiếm theo chiều sâu làm gì?

Khi bắt đầu từ một đỉnh $v$ nào đó, DFS cố gắng đi qua tất cả các cạnh đi ra từ $v$.
Nó dừng lại ở các cạnh mà các đầu của chúng đã được thăm trước đó, và đi qua các cạnh còn lại và tiếp tục đệ quy tại các đầu của chúng.

Do đó, vào thời điểm lệnh gọi hàm $\text{dfs}(v)$ kết thúc, tất cả các đỉnh có thể truy cập từ $v$ đã được thăm trực tiếp (thông qua một cạnh) hoặc gián tiếp bởi tìm kiếm.

Hãy thêm đỉnh $v$ vào một danh sách, khi chúng ta kết thúc $\text{dfs}(v)$. Vì tất cả các đỉnh có thể truy cập đã được thăm, chúng sẽ nằm trong danh sách khi chúng ta thêm $v$.
Hãy làm điều này cho mọi đỉnh trong đồ thị, với một hoặc nhiều lần chạy tìm kiếm theo chiều sâu.
Đối với mỗi cạnh có hướng $v \rightarrow u$ trong đồ thị, $u$ sẽ xuất hiện sớm hơn trong danh sách này so với $v$, bởi vì $u$ có thể truy cập được từ $v$.
Vì vậy, nếu chúng ta chỉ đánh dấu các đỉnh trong danh sách này với $n-1, n-2, \dots, 1, 0$, chúng ta đã tìm thấy một thứ tự topo của đồ thị.
Nói cách khác, danh sách đại diện cho thứ tự topo bị đảo ngược.

Những giải thích này cũng có thể được trình bày dưới dạng thời gian thoát (exit times) của thuật toán DFS.
Thời gian thoát cho đỉnh $v$ là thời gian mà lệnh gọi hàm $\text{dfs}(v)$ kết thúc (thời gian có thể được đánh số từ $0$ đến $n-1$).
Dễ hiểu là thời gian thoát của bất kỳ đỉnh $v$ nào luôn lớn hơn thời gian thoát của bất kỳ đỉnh nào có thể truy cập từ nó (vì chúng đã được thăm trước khi gọi $\text{dfs}(v)$ hoặc trong quá trình đó). Do đó, thứ tự topo mong muốn là các đỉnh theo thứ tự giảm dần của thời gian thoát của chúng.

## Cài đặt (Implementation) {: #implementation}

Dưới đây là một cài đặt giả định rằng đồ thị không có chu trình, tức là thứ tự topo mong muốn tồn tại. Nếu cần thiết, bạn có thể dễ dàng kiểm tra xem đồ thị có không có chu trình hay không, như được mô tả trong bài viết về [tìm kiếm theo chiều sâu](depth-first-search.md).

```cpp
int n; // số lượng đỉnh
vector<vector<int>> adj; // danh sách kề của đồ thị
vector<bool> visited;
vector<int> ans;

void dfs(int v) {
    visited[v] = true;
    for (int u : adj[v]) {
        if (!visited[u]) {
            dfs(u);
        }
    }
    ans.push_back(v);
}

void topological_sort() {
    visited.assign(n, false);
    ans.clear();
    for (int i = 0; i < n; ++i) {
        if (!visited[i]) {
            dfs(i);
        }
    }
    reverse(ans.begin(), ans.end());
}
```

Hàm chính của giải pháp là `topological_sort`, khởi tạo các biến DFS, khởi chạy DFS và nhận câu trả lời trong vector `ans`. Cần lưu ý rằng khi đồ thị không phải là không có chu trình (tức là có chu trình), kết quả `topological_sort` vẫn sẽ có ý nghĩa ở một khía cạnh nào đó là nếu một đỉnh $u$ có thể truy cập từ đỉnh $v$, nhưng không ngược lại (not vice versa), thì đỉnh $v$ sẽ luôn đi trước trong mảng kết quả. Thuộc tính này của cài đặt được cung cấp được sử dụng trong [thuật toán Kosaraju](./strongly-connected-components.md) để trích xuất các thành phần liên thông mạnh và sắp xếp topo của chúng trong một đồ thị có hướng có chu trình.

## Bài tập (Practice Problems) {: #practice-problems}

- [SPOJ TOPOSORT - Topological Sorting [difficulty: easy]](http://www.spoj.com/problems/TOPOSORT/)
- [UVA 10305 - Ordering Tasks [difficulty: easy]](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1246)
- [UVA 124 - Following Orders [difficulty: easy]](https://onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=60)
- [UVA 200 - Rare Order [difficulty: easy]](https://onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=136)
- [Codeforces 510C - Fox and Names [difficulty: easy]](http://codeforces.com/problemset/problem/510/C)
- [SPOJ RPLA - Answer the boss!](https://www.spoj.com/problems/RPLA/)
- [CSES - Course Schedule](https://cses.fi/problemset/task/1679)
- [CSES - Longest Flight Route](https://cses.fi/problemset/task/1680)
- [CSES - Game Routes](https://cses.fi/problemset/task/1681)
