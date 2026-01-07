---
tags:
  - Translated
e_maxx_link: bipartite_checking
---

# Kiểm tra xem một đồ thị có phải là đồ thị hai phía không

Đồ thị hai phía là một đồ thị mà các đỉnh của nó có thể được chia thành hai tập hợp không giao nhau sao cho mọi cạnh nối hai đỉnh từ các tập hợp khác nhau (tức là không có cạnh nào nối các đỉnh từ cùng một tập hợp). Các tập hợp này thường được gọi là các phía.

Bạn được cho một đồ thị vô hướng. Kiểm tra xem nó có phải là đồ thị hai phía không, và nếu có, hãy xuất ra các phía của nó.

## Thuật toán

Có một định lý cho rằng một đồ thị là hai phía khi và chỉ khi tất cả các chu trình của nó có độ dài chẵn. Tuy nhiên, trong thực tế, việc sử dụng một định nghĩa khác sẽ thuận tiện hơn: một đồ thị là hai phía khi và chỉ khi nó có thể được tô màu bằng hai màu.

Hãy sử dụng một chuỗi các [tìm kiếm theo chiều rộng](breadth-first-search.md), bắt đầu từ mỗi đỉnh chưa được thăm. Trong mỗi lần tìm kiếm, gán đỉnh mà chúng ta bắt đầu vào phía 1. Mỗi khi chúng ta thăm một đỉnh kề chưa được thăm của một đỉnh được gán cho một phía, chúng ta gán nó cho phía còn lại. Khi chúng ta cố gắng đi đến một đỉnh kề của một đỉnh được gán cho một phía mà đã được thăm, chúng ta kiểm tra xem nó đã được gán cho phía kia chưa; nếu nó đã được gán cho cùng một phía, chúng ta kết luận rằng đồ thị không phải là đồ thị hai phía. Khi chúng ta đã thăm tất cả các đỉnh và gán chúng vào các phía một cách thành công, chúng ta biết rằng đồ thị là hai phía và chúng ta đã xây dựng được phân hoạch của nó.

## Cài đặt

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

### Bài tập thực hành:

- [SPOJ - BUGLIFE](http://www.spoj.com/problems/BUGLIFE/)
- [Codeforces - Graph Without Long Directed Paths](https://codeforces.com/contest/1144/problem/F)
- [Codeforces - String Coloring (easy version)](https://codeforces.com/contest/1296/problem/E1)
- [CSES : Building Teams](https://cses.fi/problemset/task/1668)