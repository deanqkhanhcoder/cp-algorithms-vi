---
title: Xóa khỏi cấu trúc dữ liệu trong O(T(n) log n)
tags:
  - Original
---
# Xóa khỏi cấu trúc dữ liệu trong $O(T(n)\log n)$

Giả sử bạn có một cấu trúc dữ liệu cho phép thêm các phần tử với độ phức tạp **thực sự** là $O(T(n))$.
Bài viết này sẽ mô tả một kỹ thuật cho phép xóa ngoại tuyến (offline) trong $O(T(n)\log n)$.

## Thuật toán

Mỗi phần tử tồn tại trong cấu trúc dữ liệu trong một số đoạn thời gian giữa các lần thêm và xóa.
Hãy xây dựng một cây phân đoạn trên các truy vấn.
Mỗi đoạn thời gian mà một phần tử tồn tại sẽ được chia thành $O(\log n)$ nút của cây.
Hãy đặt mỗi truy vấn khi chúng ta muốn biết điều gì đó về cấu trúc vào lá tương ứng.
Bây giờ, để xử lý tất cả các truy vấn, chúng ta sẽ chạy một thuật toán DFS trên cây phân đoạn.
Khi đi vào một nút, chúng ta sẽ thêm tất cả các phần tử có trong nút này.
Sau đó, chúng ta sẽ đi sâu hơn vào các con của nút này hoặc trả lời các truy vấn (nếu nút là một lá).
Khi rời khỏi nút, chúng ta phải hoàn tác các lần thêm.
Lưu ý rằng nếu chúng ta thay đổi cấu trúc trong $O(T(n))$, chúng ta có thể hoàn tác các thay đổi trong $O(T(n))$ bằng cách giữ một ngăn xếp các thay đổi.
Lưu ý rằng việc hoàn tác sẽ phá vỡ độ phức tạp trừ dần (amortized complexity).

## Ghi chú

Ý tưởng tạo một cây phân đoạn trên các đoạn thời gian khi một cái gì đó tồn tại có thể được sử dụng không chỉ cho các bài toán về cấu trúc dữ liệu.
Xem một số bài toán dưới đây.

## Cài đặt

Việc triển khai này dành cho bài toán [liên thông động](https://en.wikipedia.org/wiki/Dynamic_connectivity).
Nó có thể thêm cạnh, xóa cạnh và đếm số thành phần liên thông.

```{.cpp file=dynamic-conn}
struct dsu_save {
    int v, rnkv, u, rnku;

    dsu_save() {}

    dsu_save(int _v, int _rnkv, int _u, int _rnku)
        : v(_v), rnkv(_rnkv), u(_u), rnku(_rnku) {}
};

struct dsu_with_rollbacks {
    vector<int> p, rnk;
    int comps;
    stack<dsu_save> op;

    dsu_with_rollbacks() {}

    dsu_with_rollbacks(int n) {
        p.resize(n);
        rnk.resize(n);
        for (int i = 0; i < n; i++) {
            p[i] = i;
            rnk[i] = 0;
        }
        comps = n;
    }

    int find_set(int v) {
        return (v == p[v]) ? v : find_set(p[v]);
    }

    bool unite(int v, int u) {
        v = find_set(v);
        u = find_set(u);
        if (v == u)
            return false;
        comps--;
        if (rnk[v] > rnk[u])
            swap(v, u);
        op.push(dsu_save(v, rnk[v], u, rnk[u]));
        p[v] = u;
        if (rnk[u] == rnk[v])
            rnk[u]++;
        return true;
    }

    void rollback() {
        if (op.empty())
            return;
        dsu_save x = op.top();
        op.pop();
        comps++;
        p[x.v] = x.v;
        rnk[x.v] = x.rnkv;
        p[x.u] = x.u;
        rnk[x.u] = x.rnku;
    }
};

struct query {
    int v, u;
    bool united;
    query(int _v, int _u) : v(_v), u(_u) {
    }
};

struct QueryTree {
    vector<vector<query>> t;
    dsu_with_rollbacks dsu;
    int T;

    QueryTree() {}

    QueryTree(int _T, int n) : T(_T) {
        dsu = dsu_with_rollbacks(n);
        t.resize(4 * T + 4);
    }

    void add_to_tree(int v, int l, int r, int ul, int ur, query& q) {
        if (ul > ur)
            return;
        if (l == ul && r == ur) {
            t[v].push_back(q);
            return;
        }
        int mid = (l + r) / 2;
        add_to_tree(2 * v, l, mid, ul, min(ur, mid), q);
        add_to_tree(2 * v + 1, mid + 1, r, max(ul, mid + 1), ur, q);
    }

    void add_query(query q, int l, int r) {
        add_to_tree(1, 0, T - 1, l, r, q);
    }

    void dfs(int v, int l, int r, vector<int>& ans) {
        for (query& q : t[v]) {
            q.united = dsu.unite(q.v, q.u);
        }
        if (l == r)
            ans[l] = dsu.comps;
        else {
            int mid = (l + r) / 2;
            dfs(2 * v, l, mid, ans);
            dfs(2 * v + 1, mid + 1, r, ans);
        }
        for (query q : t[v]) {
            if (q.united)
                dsu.rollback();
        }
    }

    vector<int> solve() {
        vector<int> ans(T);
        dfs(1, 0, T - 1, ans);
        return ans;
    }
};
```

## Các bài toán

- [Codeforces - Connect and Disconnect](https://codeforces.com/gym/100551/problem/A)
- [Codeforces - Addition on Segments](https://codeforces.com/contest/981/problem/E)
- [Codeforces - Extending Set of Points](https://codeforces.com/contest/1140/problem/F)