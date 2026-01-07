---
title: Kiểm tra đồ thị có chu trình hay không và tìm chu trình trong O(M)
tags:
  - Translated
e_maxx_link: finding_cycle
---
# Kiểm tra đồ thị có chu trình hay không và tìm chu trình trong $O(M)$

Xét một đồ thị có hướng hoặc vô hướng không có vòng lặp và cạnh bội. Chúng ta phải kiểm tra xem nó có phải là không có chu trình hay không, và nếu không, thì tìm bất kỳ chu trình nào.

Chúng ta có thể giải quyết vấn đề này bằng cách sử dụng [Tìm kiếm theo chiều sâu](depth-first-search.md) trong $O(M)$ trong đó $M$ là số cạnh.

## Thuật toán

Chúng ta sẽ chạy một loạt các DFS trong đồ thị. Ban đầu, tất cả các đỉnh được tô màu trắng (0). Từ mỗi đỉnh chưa được thăm (màu trắng), bắt đầu DFS, đánh dấu nó là màu xám (1) khi vào và đánh dấu nó là màu đen (2) khi thoát. Nếu DFS di chuyển đến một đỉnh màu xám, thì chúng ta đã tìm thấy một chu trình (nếu đồ thị là vô hướng, cạnh đến cha không được xem xét).
Chu trình có thể được tái tạo bằng mảng cha.

## Cài đặt

Đây là một cách triển khai cho đồ thị có hướng.

```cpp
int n;
vector<vector<int>> adj;
vector<char> color;
vector<int> parent;
int cycle_start, cycle_end;

bool dfs(int v) {
    color[v] = 1;
    for (int u : adj[v]) {
        if (color[u] == 0) {
            parent[u] = v;
            if (dfs(u))
                return true;
        } else if (color[u] == 1) {
            cycle_end = v;
            cycle_start = u;
            return true;
        }
    }
    color[v] = 2;
    return false;
}

void find_cycle() {
    color.assign(n, 0);
    parent.assign(n, -1);
    cycle_start = -1;

    for (int v = 0; v < n; v++) {
        if (color[v] == 0 && dfs(v))
            break;
    }

    if (cycle_start == -1) {
        cout << "Acyclic" << endl;
    } else {
        vector<int> cycle;
        cycle.push_back(cycle_start);
        for (int v = cycle_end; v != cycle_start; v = parent[v])
            cycle.push_back(v);
        cycle.push_back(cycle_start);
        reverse(cycle.begin(), cycle.end());

        cout << "Cycle found: ";
        for (int v : cycle)
            cout << v << " ";
        cout << endl;
    }
}
```

Đây là một cách triển khai cho đồ thị vô hướng.
Lưu ý rằng trong phiên bản vô hướng, nếu một đỉnh `v` được tô màu đen, nó sẽ không bao giờ được thăm lại bởi DFS.
Điều này là do chúng ta đã khám phá tất cả các cạnh được kết nối của `v` khi chúng ta lần đầu tiên thăm nó.
Thành phần liên thông chứa `v` (sau khi loại bỏ cạnh giữa `v` và cha của nó) phải là một cây, nếu DFS đã hoàn thành xử lý `v` mà không tìm thấy chu trình.
Vì vậy, chúng ta thậm chí không cần phải phân biệt giữa các trạng thái xám và đen.
Do đó, chúng ta có thể chuyển vector char `color` thành một vector boolean `visited`.

```cpp
int n;
vector<vector<int>> adj;
vector<bool> visited;
vector<int> parent;
int cycle_start, cycle_end;

bool dfs(int v, int par) { // truyền đỉnh và đỉnh cha của nó
    visited[v] = true;
    for (int u : adj[v]) {
        if(u == par) continue; // bỏ qua cạnh đến đỉnh cha
        if (visited[u]) {
            cycle_end = v;
            cycle_start = u;
            return true;
        }
        parent[u] = v;
        if (dfs(u, parent[u]))
            return true;
    }
    return false;
}

void find_cycle() {
    visited.assign(n, false);
    parent.assign(n, -1);
    cycle_start = -1;

    for (int v = 0; v < n; v++) {
        if (!visited[v] && dfs(v, parent[v]))
            break;
    }

    if (cycle_start == -1) {
        cout << "Acyclic" << endl;
    } else {
        vector<int> cycle;
        cycle.push_back(cycle_start);
        for (int v = cycle_end; v != cycle_start; v = parent[v])
            cycle.push_back(v);
        cycle.push_back(cycle_start);

        cout << "Cycle found: ";
        for (int v : cycle)
            cout << v << " ";
        cout << endl;
    }
}
```
### Bài tập thực hành:

- [AtCoder : Reachability in Functional Graph](https://atcoder.jp/contests/abc357/tasks/abc357_e)
- [CSES : Round Trip](https://cses.fi/problemset/task/1669)
- [CSES : Round Trip II](https://cses.fi/problemset/task/1678/)