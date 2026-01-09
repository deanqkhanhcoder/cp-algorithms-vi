---
tags:
  - Translated
e_maxx_link: dinic
---

# Luồng cực đại - Thuật toán Dinic (Maximum flow - Dinic's algorithm) {: #maximum-flow-dinics-algorithm}

Thuật toán Dinic giải quyết bài toán luồng cực đại trong $O(V^2E)$. Bài toán luồng cực đại được định nghĩa trong bài viết này [Luồng cực đại - Ford-Fulkerson và Edmonds-Karp](edmonds-karp.md). Thuật toán này được phát hiện bởi Yefim Dinitz vào năm 1970.

## Định nghĩa (Definitions) {: #definitions}

Một **mạng dư** (residual network) $G^R$ của mạng $G$ là một mạng chứa hai cạnh cho mỗi cạnh $(v, u)\in G$:<br>

- $(v, u)$ với dung lượng $c_{vu}^R = c_{vu} - f_{vu}$
- $(u, v)$ với dung lượng $c_{uv}^R = f_{vu}$

Một **luồng chắn** (blocking flow) của một mạng nào đó là một luồng sao cho mọi đường đi từ $s$ đến $t$ chứa ít nhất một cạnh bị bão hòa bởi luồng này. Lưu ý rằng một luồng chắn không nhất thiết phải là cực đại.

Một **mạng phân lớp** (layered network) của một mạng $G$ là một mạng được xây dựng theo cách sau. Đầu tiên, đối với mỗi đỉnh $v$, chúng ta tính toán $level[v]$ - đường đi ngắn nhất (không trọng số) từ $s$ đến đỉnh này chỉ sử dụng các cạnh có dung lượng dương. Sau đó chúng ta chỉ giữ lại những cạnh $(v, u)$ mà $level[v] + 1 = level[u]$. Rõ ràng, mạng này là không có chu trình.

## Thuật toán (Algorithm) {: #algorithm}

Thuật toán bao gồm nhiều pha. Ở mỗi pha, chúng ta xây dựng mạng phân lớp của mạng dư của $G$. Sau đó chúng ta tìm một luồng chắn bất kỳ trong mạng phân lớp và thêm nó vào luồng hiện tại.

## Chứng minh tính đúng đắn (Proof of correctness) {: #proof-of-correctness}

Hãy chỉ ra rằng nếu thuật toán kết thúc, nó tìm thấy luồng cực đại.

Nếu thuật toán đã kết thúc, nó không thể tìm thấy một luồng chắn trong mạng phân lớp. Điều đó có nghĩa là mạng phân lớp không có bất kỳ đường đi nào từ $s$ đến $t$. Điều đó có nghĩa là mạng dư không có bất kỳ đường đi nào từ $s$ đến $t$. Điều đó có nghĩa là luồng là cực đại.

## Số lượng pha (Number of phases) {: #number-of-phases}

Thuật toán kết thúc trong ít hơn $V$ pha. Để chứng minh điều này, chúng ta phải chứng minh trước hai bổ đề.

**Bổ đề 1.** Khoảng cách từ $s$ đến mỗi đỉnh không giảm sau mỗi lần lặp, tức là $level_{i+1}[v] \ge level_i[v]$.

**Chứng minh.** Cố định một pha $i$ và một đỉnh $v$. Phân tích một đường đi ngắn nhất bất kỳ $P$ từ $s$ đến $v$ trong $G_{i+1}^R$. Độ dài của $P$ bằng $level_{i+1}[v]$. Lưu ý rằng $G_{i+1}^R$ chỉ có thể chứa các cạnh từ $G_i^R$ và các cạnh ngược cho các cạnh từ $G_i^R$. Nếu $P$ không có cạnh ngược nào cho $G_i^R$, thì $level_{i+1}[v] \ge level_i[v]$ vì $P$ cũng là một đường đi trong $G_i^R$. Bây giờ, giả sử rằng $P$ có ít nhất một cạnh ngược. Gọi cạnh đầu tiên như vậy là $(u, w)$. Khi đó $level_{i+1}[u] \ge level_i[u]$ (do trường hợp đầu tiên). Cạnh $(u, w)$ không thuộc về $G_i^R$, vì vậy cạnh $(w, u)$ đã bị ảnh hưởng bởi luồng chắn ở lần lặp trước. Điều đó có nghĩa là $level_i[u] = level_i[w] + 1$. Ngoài ra, $level_{i+1}[w] = level_{i+1}[u] + 1$. Từ hai phương trình này và $level_{i+1}[u] \ge level_i[u]$ chúng ta thu được $level_{i+1}[w] \ge level_i[w] + 2$. Bây giờ chúng ta có thể sử dụng ý tưởng tương tự cho phần còn lại của đường đi.

**Bổ đề 2.** $level_{i+1}[t] > level_i[t]$

**Chứng minh.** Từ bổ đề trước, $level_{i+1}[t] \ge level_i[t]$. Giả sử rằng $level_{i+1}[t] = level_i[t]$. Lưu ý rằng $G_{i+1}^R$ chỉ có thể chứa các cạnh từ $G_i^R$ và các cạnh ngược cho các cạnh từ $G_i^R$. Điều đó có nghĩa là có một đường đi ngắn nhất trong $G_i^R$ mà không bị chặn bởi luồng chắn. Đó là một mâu thuẫn.

Từ hai bổ đề này, chúng ta kết luận rằng có ít hơn $V$ pha vì $level[t]$ tăng, nhưng nó không thể lớn hơn $V - 1$.

## Tìm luồng chắn (Finding blocking flow) {: #finding-blocking-flow}

để tìm luồng chắn trên mỗi lần lặp, chúng ta có thể đơn giản thử đẩy luồng bằng DFS từ $s$ đến $t$ trong mạng phân lớp trong khi nó có thể được đẩy. Để thực hiện nhanh hơn, chúng ta phải loại bỏ các cạnh không thể được sử dụng để đẩy nữa. Để làm điều này chúng ta có thể giữ một con trỏ trong mỗi đỉnh trỏ đến cạnh tiếp theo có thể được sử dụng.

Một lần chạy DFS duy nhất mất thời gian $O(k+V)$, trong đó $k$ là số lần di chuyển con trỏ trong lần chạy này. Tổng cộng trên tất cả các lần chạy, số lần di chuyển con trỏ không thể vượt quá $E$. Mặt khác, tổng số lần chạy sẽ không vượt quá $E$, vì mỗi lần chạy làm bão hòa ít nhất một cạnh. Bằng cách này, tổng thời gian chạy để tìm một luồng chắn là $O(VE)$.

## Độ phức tạp (Complexity) {: #complexity}

Có ít hơn $V$ pha, vì vậy tổng độ phức tạp là $O(V^2E)$.

## Mạng đơn vị (Unit networks) {: #unit-networks}

Một **mạng đơn vị** là một mạng trong đó đối với bất kỳ đỉnh nào ngoại trừ $s$ và $t$, **cạnh đi vào hoặc cạnh đi ra là duy nhất và có dung lượng đơn vị**. Đó chính xác là trường hợp với mạng chúng ta xây dựng để giải quyết bài toán ghép cặp cực đại bằng luồng.

Trên các mạng đơn vị, thuật toán Dinic hoạt động trong $O(E\sqrt{V})$. Hãy chứng minh điều này.

Thứ nhất, mỗi pha bây giờ hoạt động trong $O(E)$ vì mỗi cạnh sẽ được xem xét tối đa một lần.

Thứ hai, giả sử đã có $\sqrt{V}$ pha. Khi đó tất cả các đường tăng luồng có độ dài $\le\sqrt{V}$ đã được tìm thấy. Gọi $f$ là luồng hiện tại, $f'$ là luồng cực đại. Xét hiệu của chúng $f' - f$. Nó là một luồng trong $G^R$ có giá trị $|f'| - |f|$ và trên mỗi cạnh nó hoặc là $0$ hoặc là $1$. Nó có thể được phân tách thành $|f'| - |f|$ đường đi từ $s$ đến $t$ và có thể là các chu trình. Vì mạng là đơn vị, chúng không thể có các đỉnh chung, vì vậy tổng số đỉnh là $\ge (|f'| - |f|)\sqrt{V}$, nhưng nó cũng $\le V$, vì vậy trong $\sqrt{V}$ lần lặp nữa chúng ta chắc chắn sẽ tìm thấy luồng cực đại.

### Mạng dung lượng đơn vị (Unit capacities networks) {: #unit-capacities-networks}

Trong một cài đặt tổng quát hơn khi tất cả các cạnh có dung lượng đơn vị, _nhưng số lượng cạnh đi vào và đi ra là không bị chặn_, các đường đi không thể có các cạnh chung thay vì các đỉnh chung. Theo một cách tương tự, nó cho phép chứng minh giới hạn của $\sqrt E$ về số lần lặp, do đó thời gian chạy của thuật toán Dinic trên các mạng như vậy tối đa là $O(E \sqrt E)$.

Cuối cùng, cũng có thể chứng minh rằng số lượng pha trên các mạng dung lượng đơn vị không vượt quá $O(V^{2/3})$, cung cấp một ước tính thay thế là $O(EV^{2/3})$ trên các mạng có số lượng cạnh đặc biệt lớn.

## Cài đặt (Implementation) {: #implementation}

```cpp
struct FlowEdge {
    int v, u;
    long long cap, flow = 0;
    FlowEdge(int v, int u, long long cap) : v(v), u(u), cap(cap) {}
};

struct Dinic {
    const long long flow_inf = 1e18;
    vector<FlowEdge> edges;
    vector<vector<int>> adj;
    int n, m = 0;
    int s, t;
    vector<int> level, ptr;
    queue<int> q;

    Dinic(int n, int s, int t) : n(n), s(s), t(t) {
        adj.resize(n);
        level.resize(n);
        ptr.resize(n);
    }

    void add_edge(int v, int u, long long cap) {
        edges.emplace_back(v, u, cap);
        edges.emplace_back(u, v, 0);
        adj[v].push_back(m);
        adj[u].push_back(m + 1);
        m += 2;
    }

    bool bfs() {
        while (!q.empty()) {
            int v = q.front();
            q.pop();
            for (int id : adj[v]) {
                if (edges[id].cap == edges[id].flow)
                    continue;
                if (level[edges[id].u] != -1)
                    continue;
                level[edges[id].u] = level[v] + 1;
                q.push(edges[id].u);
            }
        }
        return level[t] != -1;
    }

    long long dfs(int v, long long pushed) {
        if (pushed == 0)
            return 0;
        if (v == t)
            return pushed;
        for (int& cid = ptr[v]; cid < (int)adj[v].size(); cid++) {
            int id = adj[v][cid];
            int u = edges[id].u;
            if (level[v] + 1 != level[u])
                continue;
            long long tr = dfs(u, min(pushed, edges[id].cap - edges[id].flow));
            if (tr == 0)
                continue;
            edges[id].flow += tr;
            edges[id ^ 1].flow -= tr;
            return tr;
        }
        return 0;
    }

    long long flow() {
        long long f = 0;
        while (true) {
            fill(level.begin(), level.end(), -1);
            level[s] = 0;
            q.push(s);
            if (!bfs())
                break;
            fill(ptr.begin(), ptr.end(), 0);
            while (long long pushed = dfs(s, flow_inf)) {
                f += pushed;
            }
        }
        return f;
    }
};
```

## Bài tập (Practice Problems) {: #practice-problems}

* [SPOJ: FASTFLOW](https://www.spoj.com/problems/FASTFLOW/)