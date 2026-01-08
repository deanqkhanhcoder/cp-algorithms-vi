---
tags:
  - Translated
e_maxx_link: bipartite_checking
---

# Kiểm tra xem đồ thị có phải là hai phía (bipartite) không {: #check-whether-a-graph-is-bipartite}

Một đồ thị hai phía là một đồ thị mà các đỉnh của nó có thể được chia thành hai tập hợp rời nhau sao cho mỗi cạnh nối hai đỉnh từ các tập hợp khác nhau (tức là không có cạnh nào nối các đỉnh từ cùng một tập hợp). Các tập hợp này thường được gọi là các phía (sides).

Bạn được cho một đồ thị vô hướng. Kiểm tra xem nó có phải là hai phía hay không, và nếu có, hãy xuất ra các phía của nó.

## Thuật toán (Algorithm) {: #algorithm}

Có một định lý khẳng định rằng một đồ thị là hai phía khi và chỉ khi tất cả các chu trình của nó có độ dài chẵn. Tuy nhiên, trong thực tế, thuận tiện hơn khi sử dụng một công thức khác của định nghĩa: một đồ thị là hai phía khi và chỉ khi nó có thể tô bằng hai màu (two-colorable).

Hãy sử dụng một loạt các [tìm kiếm theo chiều rộng](breadth-first-search.md), bắt đầu từ mỗi đỉnh chưa được thăm. Trong mỗi lần tìm kiếm, gán đỉnh mà chúng ta bắt đầu cho phía 1. Mỗi khi chúng ta thăm một hàng xóm chưa được thăm của một đỉnh được gán cho một phía, chúng ta gán nó cho phía kia. Khi chúng ta cố gắng đi đến một hàng xóm của một đỉnh được gán cho một phía mà đã được thăm, chúng ta kiểm tra xem nó đã được gán cho phía kia hay chưa; nếu nó đã được gán cho cùng một phía, chúng ta kết luận rằng đồ thị không phải là hai phía. Khi chúng ta đã thăm tất cả các đỉnh và gán thành công chúng cho các phía, chúng ta biết rằng đồ thị là hai phía và chúng ta đã xây dựng phân hoạch của nó.

## Cài đặt (Implementation) {: #implementation}

```cpp
int n;
vector<vector<int>> adj;

vector<int> side(n, -1);
bool is_bipartite = true;
queue<int> q;
for (int st = 0; st < n; ++st) {
    if (side[st] == -1) {
        q.push(st);
        side[st] = 0;
        while (!q.empty()) {
            int v = q.front();
            q.pop();
            for (int u : adj[v]) {
                if (side[u] == -1) {
                    side[u] = side[v] ^ 1;
                    q.push(u);
                } else {
                    is_bipartite &= side[u] != side[v];
                }
            }
        }
    }
}

cout << (is_bipartite ? "YES" : "NO") << endl;
```

### Bài tập (Practice problems) {: #practice-problems}

- [SPOJ - BUGLIFE](http://www.spoj.com/problems/BUGLIFE/)
- [Codeforces - Graph Without Long Directed Paths](https://codeforces.com/contest/1144/problem/F)
- [Codeforces - String Coloring (easy version)](https://codeforces.com/contest/1296/problem/E1)
- [CSES : Building Teams](https://cses.fi/problemset/task/1668)
