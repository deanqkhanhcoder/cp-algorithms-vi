---
tags:
  - Translated
---
# BFS 0-1 (0-1 BFS) {: #0-1-bfs}

Việc tìm đường đi ngắn nhất giữa một nguồn đơn và tất cả các đỉnh khác trong $O(|E|)$ bằng cách sử dụng [Tìm kiếm theo chiều rộng](breadth-first-search.md) trong **đồ thị không trọng số** đã rất nổi tiếng, tức là khoảng cách là số lượng cạnh tối thiểu bạn cần để đi từ nguồn đến đỉnh khác.
Chúng ta cũng có thể hiểu đồ thị như vậy là đồ thị có trọng số, trong đó mỗi cạnh có trọng số là $1$.
Nếu không phải tất cả các cạnh trong đồ thị đều có cùng trọng số, thì chúng ta cần một thuật toán tổng quát hơn, như [Dijkstra](dijkstra.md) chạy trong thời gian $O(|V|^2 + |E|)$ hoặc $O(|E| \log |V|)$.

Tuy nhiên, nếu trọng số bị hạn chế hơn, chúng ta thường có thể làm tốt hơn.
Trong bài viết này, chúng tôi trình bày cách chúng ta có thể sử dụng BFS để giải quyết bài toán SSSP (đường đi ngắn nhất từ một nguồn đơn) trong $O(|E|)$, nếu trọng số của mỗi cạnh là $0$ hoặc $1$.

## Thuật toán (Algorithm) {: #algorithm}

Chúng ta có thể phát triển thuật toán bằng cách nghiên cứu kỹ thuật toán Dijkstra và suy nghĩ về những hậu quả mà đồ thị đặc biệt của chúng ta mang lại.
Dạng chung của thuật toán Dijkstra là (ở đây `set` được sử dụng cho hàng đợi ưu tiên):

```cpp
d.assign(n, INF);
d[s] = 0;
set<pair<int, int>> q;
q.insert({0, s});
while (!q.empty()) {
    int v = q.begin()->second;
    q.erase(q.begin());

    for (auto edge : adj[v]) {
        int u = edge.first;
        int w = edge.second;

        if (d[v] + w < d[u]) {
            q.erase({d[u], u});
            d[u] = d[v] + w;
            q.insert({d[u], u});
        }
    }
}
```

Chúng ta có thể nhận thấy rằng sự khác biệt về khoảng cách giữa nguồn `s` và hai đỉnh khác trong hàng đợi sai khác nhau nhiều nhất là một.
Đặc biệt, chúng ta biết rằng $d[v] \le d[u] \le d[v] + 1$ cho mỗi $u \in Q$.
Lý do cho điều này là, chúng ta chỉ thêm các đỉnh có khoảng cách bằng nhau hoặc khoảng cách cộng một vào hàng đợi trong mỗi lần lặp.
Giả sử tồn tại một $u$ trong hàng đợi với $d[u] - d[v] > 1$, thì $u$ phải được chèn vào hàng đợi thông qua một đỉnh khác $t$ với $d[t] \ge d[u] - 1 > d[v]$.
Tuy nhiên điều này là không thể, vì thuật toán Dijkstra lặp qua các đỉnh theo thứ tự tăng dần.

Điều này có nghĩa là, thứ tự của hàng đợi trông như sau:

$$Q = \underbrace{v}_{d[v]}, \dots, \underbrace{u}_{d[v]}, \underbrace{m}_{d[v]+1} \dots \underbrace{n}_{d[v]+1}$$

Cấu trúc này đơn giản đến mức chúng ta không cần một hàng đợi ưu tiên thực sự, tức là sử dụng cây nhị phân cân bằng sẽ là quá mức cần thiết.
Chúng ta có thể chỉ cần sử dụng một hàng đợi bình thường, và thêm các đỉnh mới vào đầu nếu cạnh tương ứng có trọng số $0$, tức là nếu $d[u] = d[v]$, hoặc vào cuối nếu cạnh có trọng số $1$, tức là nếu $d[u] = d[v] + 1$.
Bằng cách này, hàng đợi vẫn được sắp xếp mọi lúc.

```cpp
vector<int> d(n, INF);
d[s] = 0;
deque<int> q;
q.push_front(s);
while (!q.empty()) {
    int v = q.front();
    q.pop_front();
    for (auto edge : adj[v]) {
        int u = edge.first;
        int w = edge.second;
        if (d[v] + w < d[u]) {
            d[u] = d[v] + w;
            if (w == 1)
                q.push_back(u);
            else
                q.push_front(u);
        }
    }
}
```

## Thuật toán Dial (Dial's algorithm) {: #dials-algorithm}

Chúng ta có thể mở rộng điều này hơn nữa nếu chúng ta cho phép trọng số của các cạnh lớn hơn.
Nếu mọi cạnh trong đồ thị có trọng số $\le k$, thì khoảng cách của các đỉnh trong hàng đợi sẽ khác biệt nhiều nhất là $k$ so với khoảng cách từ $v$ đến nguồn.
Vì vậy, chúng ta có thể giữ $k + 1$ bucket cho các đỉnh trong hàng đợi, và bất cứ khi nào bucket tương ứng với khoảng cách nhỏ nhất trống, chúng ta thực hiện một dịch chuyển vòng để lấy bucket có khoảng cách cao hơn tiếp theo.
Mở rộng này được gọi là **thuật toán Dial**.

## Bài tập (Practice problems) {: #practice-problems}

- [CodeChef - Chef and Reversing](https://www.codechef.com/problems/REVERSE)
- [Labyrinth](https://codeforces.com/contest/1063/problem/B)
- [KATHTHI](http://www.spoj.com/problems/KATHTHI/)
- [DoNotTurn](https://community.topcoder.com/stat?c=problem_statement&pm=10337)
- [Ocean Currents](https://onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=2620)
- [Olya and Energy Drinks](https://codeforces.com/problemset/problem/877/D)
- [Three States](https://codeforces.com/problemset/problem/590/C)
- [Colliding Traffic](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2621)
- [CHamber of Secrets](https://codeforces.com/problemset/problem/173/B)
- [Spiral Maximum](https://codeforces.com/problemset/problem/173/C)
- [Minimum Cost to Make at Least One Valid Path in a Grid](https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid)
