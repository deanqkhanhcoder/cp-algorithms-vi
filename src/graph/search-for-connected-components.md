---
tags:
  - Translated
e_maxx_link: connected_components
---

# Tìm các thành phần liên thông trong đồ thị (Search for connected components in a graph) {: #search-for-connected-components-in-a-graph}

Cho một đồ thị vô hướng $G$ với $n$ nút và $m$ cạnh. Chúng ta được yêu cầu tìm trong đó tất cả các thành phần liên thông, tức là, một vài nhóm đỉnh sao cho trong một nhóm mỗi đỉnh có thể đến được từ đỉnh khác và không có đường đi nào tồn tại giữa các nhóm khác nhau.

## Một thuật toán giải quyết bài toán (An algorithm for solving the problem) {: #an-algorithm-for-solving-the-problem}

* Để giải quyết bài toán, chúng ta có thể sử dụng Tìm kiếm theo chiều sâu (Depth First Search) hoặc Tìm kiếm theo chiều rộng (Breadth First Search).

* Trên thực tế, chúng ta sẽ thực hiện một loạt các vòng DFS: Vòng đầu tiên sẽ bắt đầu từ nút đầu tiên và tất cả các nút trong thành phần liên thông đầu tiên sẽ được duyệt (tìm thấy). Sau đó, chúng ta tìm nút chưa được thăm đầu tiên trong các nút còn lại, và chạy Tìm kiếm theo chiều sâu trên nó, do đó tìm thấy một thành phần liên thông thứ hai. Và cứ thế, cho đến khi tất cả các nút đều được thăm.

* Tổng thời gian chạy tiệm cận của thuật toán này là $O(n + m)$: Sự thật là, thuật toán này sẽ không chạy trên cùng một đỉnh hai lần, điều đó có nghĩa là mỗi cạnh sẽ được nhìn thấy chính xác hai lần (ở đầu này và đầu kia).

## Cài đặt (Implementation) {: #implementation}

``` cpp
int n;
vector<vector<int>> adj;
vector<bool> used;
vector<int> comp;

void dfs(int v) {
    used[v] = true;
    comp.push_back(v);
    for (int u : adj[v]) {
        if (!used[u])
            dfs(u);
    }
}

void find_comps() {
    used.assign(n, false);
    for (int v = 0; v < n; ++v) {
        if (!used[v]) {
            comp.clear();
            dfs(v);
            cout << "Component:" ;
            for (int u : comp)
                cout << ' ' << u;
            cout << endl ;
        }
    }
}
```

* Hàm quan trọng nhất được sử dụng là `find_comps()` tìm và hiển thị các thành phần liên thông của đồ thị.

* Đồ thị được lưu trữ trong biểu diễn danh sách kề, tức là `adj[v]` chứa danh sách các đỉnh có cạnh từ đỉnh `v`.

* Vector `comp` chứa danh sách các nút trong thành phần liên thông hiện tại.

## Cài đặt lặp của mã (Iterative implementation of the code) {: #iterative-implementation-of-the-code}

Các hàm đệ quy sâu nói chung là tệ.
Mỗi cuộc gọi đệ quy sẽ yêu cầu một chút bộ nhớ trong stack, và theo mặc định các chương trình chỉ có một lượng không gian stack hạn chế.
Vì vậy, khi bạn thực hiện DFS đệ quy trên một đồ thị liên thông với hàng triệu nút, bạn có thể gặp phải lỗi tràn stack (stack overflows).

Luôn có thể chuyển đổi một chương trình đệ quy thành một chương trình lặp, bằng cách duy trì thủ công một cấu trúc dữ liệu stack.
Vì cấu trúc dữ liệu này được cấp phát trên heap, sẽ không xảy ra tràn stack.

```cpp
int n;
vector<vector<int>> adj;
vector<bool> used;
vector<int> comp;

void dfs(int v) {
    stack<int> st;
    st.push(v);
    
    while (!st.empty()) {
        int curr = st.top();
        st.pop();
        if (!used[curr]) {
            used[curr] = true;
            comp.push_back(curr);
            for (int i = adj[curr].size() - 1; i >= 0; i--) {
                st.push(adj[curr][i]);
            }
        }
    }
}

void find_comps() {
    used.assign(n, false);
    for (int v = 0; v < n ; ++v) {
        if (!used[v]) {
            comp.clear();
            dfs(v);
            cout << "Component:" ;
            for (int u : comp)
                cout << ' ' << u;
            cout << endl ;
        }
    }
}
```

## Bài tập (Practice Problems) {: #practice-problems}
 - [SPOJ: CT23E](http://www.spoj.com/problems/CT23E/)
 - [CODECHEF: GERALD07](https://www.codechef.com/MARCH14/problems/GERALD07)
 - [CSES : Building Roads](https://cses.fi/problemset/task/1666)
