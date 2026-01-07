---
tags:
  - Translated
e_maxx_link: negative_cycle
---

# Tìm chu trình âm trong đồ thị

Bạn được cho một đồ thị có hướng có trọng số $G$ với $N$ đỉnh và $M$ cạnh. Tìm bất kỳ chu trình nào có trọng số âm trong đó, nếu một chu trình như vậy tồn tại.

Trong một biến thể khác của bài toán, bạn phải tìm tất cả các cặp đỉnh có đường đi có trọng số nhỏ tùy ý giữa chúng.

Sử dụng các thuật toán khác nhau để giải quyết hai biến thể này của bài toán sẽ thuận tiện hơn, vì vậy chúng ta sẽ thảo luận cả hai ở đây.

## Sử dụng thuật toán Bellman-Ford

Thuật toán Bellman-Ford cho phép bạn kiểm tra xem có tồn tại một chu trình có trọng số âm trong đồ thị hay không, và nếu có, hãy tìm một trong những chu trình này.

Chi tiết của thuật toán được mô tả trong bài viết về thuật toán [Bellman-Ford](bellman_ford.md).
Ở đây chúng ta sẽ chỉ mô tả ứng dụng của nó cho bài toán này.

Việc triển khai tiêu chuẩn của Bellman-Ford tìm kiếm một chu trình âm có thể đến được từ một đỉnh bắt đầu nào đó $v$ ; tuy nhiên, thuật toán có thể được sửa đổi để chỉ tìm kiếm bất kỳ chu trình âm nào trong đồ thị.
Để làm điều này, chúng ta cần đặt tất cả khoảng cách  $d[i]$  về không chứ không phải vô cùng — như thể chúng ta đang tìm kiếm đường đi ngắn nhất từ tất cả các đỉnh đồng thời; tính hợp lệ của việc phát hiện một chu trình âm không bị ảnh hưởng.

Thực hiện $N$ lần lặp của thuật toán Bellman-Ford. Nếu không có thay đổi nào trong lần lặp cuối cùng, không có chu trình có trọng số âm trong đồ thị. Ngược lại, lấy một đỉnh mà khoảng cách đến nó đã thay đổi, và đi từ nó qua các tổ tiên của nó cho đến khi tìm thấy một chu trình. Chu trình này sẽ là chu trình có trọng số âm mong muốn.

### Cài đặt

```cpp
struct Edge {
    int a, b, cost;
};
 
int n;
vector<Edge> edges;
const int INF = 1000000000;
 
void solve() {
    vector<int> d(n, 0);
    vector<int> p(n, -1);
    int x;
 
    for (int i = 0; i < n; ++i) {
        x = -1;
        for (Edge e : edges) {
            if (d[e.a] + e.cost < d[e.b]) {
                d[e.b] = max(-INF, d[e.a] + e.cost);
                p[e.b] = e.a;
                x = e.b;
            }
        }
    }
 
    if (x == -1) {
        cout << "No negative cycle found.";
    } else {
        for (int i = 0; i < n; ++i)
            x = p[x];
 
        vector<int> cycle;
        for (int v = x;; v = p[v]) {
            cycle.push_back(v);
            if (v == x && cycle.size() > 1)
                break;
        }
        reverse(cycle.begin(), cycle.end());
 
        cout << "Negative cycle: ";
        for (int v : cycle)
            cout << v << ' ';
        cout << endl;
    }
}
```

## Sử dụng thuật toán Floyd-Warshall

Thuật toán Floyd-Warshall cho phép giải quyết biến thể thứ hai của bài toán - tìm tất cả các cặp đỉnh $(i, j)$ không có đường đi ngắn nhất giữa chúng (tức là tồn tại một đường đi có trọng số nhỏ tùy ý).

Một lần nữa, chi tiết có thể được tìm thấy trong bài viết về [Floyd-Warshall](all-pair-shortest-path-floyd-warshall.md), và ở đây chúng ta chỉ mô tả ứng dụng của nó.

Chạy thuật toán Floyd-Warshall trên đồ thị.
Ban đầu $d[v][v] = 0$ cho mỗi $v$.
Nhưng sau khi chạy thuật toán, $d[v][v]$ sẽ nhỏ hơn $0$ nếu tồn tại một đường đi có độ dài âm từ $v$ đến $v$.
Chúng ta có thể sử dụng điều này để cũng tìm tất cả các cặp đỉnh không có đường đi ngắn nhất giữa chúng.
Chúng ta lặp qua tất cả các cặp đỉnh $(i, j)$ và với mỗi cặp, chúng ta kiểm tra xem chúng có đường đi ngắn nhất giữa chúng hay không.
Để làm điều này, hãy thử tất cả các khả năng cho một đỉnh trung gian $t$.
$(i, j)$ không có đường đi ngắn nhất, nếu một trong các đỉnh trung gian $t$ có $d[t][t] < 0$ (tức là $t$ là một phần của một chu trình có trọng số âm), $t$ có thể đến được từ $i$ và $j$ có thể đến được từ $t$.
Khi đó đường đi từ $i$ đến $j$ có thể có trọng số nhỏ tùy ý.
Chúng ta sẽ ký hiệu điều này bằng `-INF`.

### Cài đặt

```cpp
for (int i = 0; i < n; ++i) {
    for (int j = 0; j < n; ++j) {
        for (int t = 0; t < n; ++t) {
            if (d[i][t] < INF && d[t][t] < 0 && d[t][j] < INF)
                d[i][j] = - INF; 
        }
    }
}
```

## Bài tập thực hành

- [UVA: Wormholes](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=499)
- [SPOJ: Alice in Amsterdam, I mean Wonderland](http://www.spoj.com/problems/UCV2013B/)
- [SPOJ: Johnsons Algorithm](http://www.spoj.com/problems/JHNSN/)