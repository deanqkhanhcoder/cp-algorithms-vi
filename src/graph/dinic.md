---
tags:
  - Translated
e_maxx_link: dinic
---

# Luồng cực đại - Thuật toán của Dinic

Thuật toán của Dinic giải quyết bài toán luồng cực đại trong $O(V^2E)$. Bài toán luồng cực đại được định nghĩa trong bài viết này [Luồng cực đại - Ford-Fulkerson và Edmonds-Karp](edmonds_karp.md). Thuật toán này được Yefim Dinitz phát hiện vào năm 1970.

## Các định nghĩa

Một **mạng còn dư** $G^R$ của mạng $G$ là một mạng chứa hai cạnh cho mỗi cạnh $(v, u)\in G$ của $G$ ban đầu:<br>

- $(v, u)$ với khả năng thông qua $c_{vu}^R = c_{vu} - f_{vu}$
- $(u, v)$ với khả năng thông qua $c_{uv}^R = f_{vu}$

Một **luồng chặn** của một mạng nào đó là một luồng sao cho mọi đường đi từ $s$ đến $t$ đều chứa ít nhất một cạnh bị bão hòa bởi luồng này. Lưu ý rằng một luồng chặn không nhất thiết phải là luồng cực đại.

Một **mạng phân lớp** của một mạng $G$ là một mạng được xây dựng theo cách sau. Đầu tiên, với mỗi đỉnh $v$, chúng ta tính $level[v]$ - đường đi ngắn nhất (không trọng số) từ $s$ đến đỉnh này chỉ sử dụng các cạnh có khả năng thông qua dương. Sau đó, chúng ta chỉ giữ lại những cạnh $(v, u)$ mà $level[v] + 1 = level[u]$. Rõ ràng, mạng này không có chu trình.

## Thuật toán

Thuật toán bao gồm nhiều giai đoạn. Trong mỗi giai đoạn, chúng ta xây dựng mạng phân lớp của mạng còn dư của $G$. Sau đó, chúng ta tìm một luồng chặn bất kỳ trong mạng phân lớp và cộng nó vào luồng hiện tại.

## Chứng minh tính đúng đắn

Hãy chứng tỏ rằng nếu thuật toán kết thúc, nó sẽ tìm thấy luồng cực đại.

Nếu thuật toán kết thúc, nó không thể tìm thấy một luồng chặn trong mạng phân lớp. Điều đó có nghĩa là mạng phân lớp không có bất kỳ đường đi nào từ $s$ đến $t$. Điều đó có nghĩa là mạng còn dư không có bất kỳ đường đi nào từ $s$ đến $t$. Điều đó có nghĩa là luồng là cực đại.

## Số lượng giai đoạn

Thuật toán kết thúc sau ít hơn $V$ giai đoạn. Để chứng minh điều này, trước tiên chúng ta phải chứng minh hai bổ đề.

**Bổ đề 1.** Khoảng cách từ $s$ đến mỗi đỉnh không giảm sau mỗi lần lặp, tức là $level_{i+1}[v] \ge level_i[v]$.

**Chứng minh.** Cố định một giai đoạn $i$ và một đỉnh $v$. Xét một đường đi ngắn nhất bất kỳ $P$ từ $s$ đến $v$ trong $G_{i+1}^R$. Độ dài của $P$ bằng $level_{i+1}[v]$. Lưu ý rằng $G_{i+1}^R$ chỉ có thể chứa các cạnh từ $G_i^R$ và các cạnh ngược cho các cạnh từ $G_i^R$. Nếu $P$ không có cạnh ngược nào cho $G_i^R$, thì $level_{i+1}[v] \ge level_i[v]$ vì $P$ cũng là một đường đi trong $G_i^R$. Bây giờ, giả sử rằng $P$ có ít nhất một cạnh ngược. Gọi cạnh đầu tiên như vậy là $(u, w)$. Khi đó $level_{i+1}[u] \ge level_i[u]$ (vì trường hợp đầu tiên). Cạnh $(u, w)$ không thuộc $G_i^R$, vì vậy cạnh $(w, u)$ đã bị ảnh hưởng bởi luồng chặn trong lần lặp trước. Điều đó có nghĩa là $level_i[u] = level_i[w] + 1$. Ngoài ra, $level_{i+1}[w] = level_{i+1}[u] + 1$. Từ hai phương trình này và $level_{i+1}[u] \ge level_i[u]$, chúng ta thu được $level_{i+1}[w] \ge level_i[w] + 2$. Bây giờ chúng ta có thể sử dụng cùng một ý tưởng cho phần còn lại của đường đi.

**Bổ đề 2.** $level_{i+1}[t] > level_i[t]$

**Chứng minh.** Từ bổ đề trước, $level_{i+1}[t] \ge level_i[t]$. Giả sử rằng $level_{i+1}[t] = level_i[t]$. Lưu ý rằng $G_{i+1}^R$ chỉ có thể chứa các cạnh từ $G_i^R$ và các cạnh ngược cho các cạnh từ $G_i^R$. Điều đó có nghĩa là có một đường đi ngắn nhất trong $G_i^R$ không bị chặn bởi luồng chặn. Đây là một mâu thuẫn.

Từ hai bổ đề này, chúng ta kết luận rằng có ít hơn $V$ giai đoạn vì $level[t]$ tăng lên, nhưng nó không thể lớn hơn $V - 1$.

## Tìm luồng chặn

Để tìm luồng chặn trong mỗi lần lặp, chúng ta có thể chỉ cần thử đẩy luồng bằng DFS từ $s$ đến $t$ trong mạng phân lớp trong khi nó có thể được đẩy. Để làm điều đó nhanh hơn, chúng ta phải loại bỏ các cạnh không thể được sử dụng để đẩy nữa. Để làm điều này, chúng ta có thể giữ một con trỏ trong mỗi đỉnh trỏ đến cạnh tiếp theo có thể được sử dụng.

Một lần chạy DFS duy nhất mất thời gian $O(k+V)$, trong đó $k$ là số lần tiến con trỏ trong lần chạy này. Tổng cộng trên tất cả các lần chạy, số lần tiến con trỏ không thể vượt quá $E$. Mặt khác, tổng số lần chạy sẽ không vượt quá $E$, vì mỗi lần chạy làm bão hòa ít nhất một cạnh. Bằng cách này, tổng thời gian chạy của việc tìm một luồng chặn là $O(VE)$.

## Độ phức tạp

Có ít hơn $V$ giai đoạn, vì vậy tổng độ phức tạp là $O(V^2E)$.

## Mạng đơn vị

Một **mạng đơn vị** là một mạng trong đó với mọi đỉnh ngoại trừ $s$ và $t$, **hoặc cạnh vào hoặc cạnh ra là duy nhất và có khả năng thông qua đơn vị**. Đó chính xác là trường hợp với mạng chúng ta xây dựng để giải bài toán ghép cặp cực đại bằng luồng.

Trên các mạng đơn vị, thuật toán của Dinic hoạt động trong $O(E\sqrt{V})$. Hãy chứng minh điều này.

Thứ nhất, mỗi giai đoạn bây giờ hoạt động trong $O(E)$ vì mỗi cạnh sẽ được xem xét nhiều nhất một lần.

Thứ hai, giả sử đã có $\sqrt{V}$ giai đoạn. Khi đó tất cả các đường tăng luồng có độ dài $\le\sqrt{V}$ đã được tìm thấy. Gọi $f$ là luồng hiện tại, $f'$ là luồng cực đại. Xét sự khác biệt của chúng $f' - f$. Nó là một luồng trong $G^R$ có giá trị $|f'| - |f|$ và trên mỗi cạnh, nó là $0$ hoặc $1$. Nó có thể được phân tách thành $|f'| - |f|$ đường đi từ $s$ đến $t$ và có thể là các chu trình. Vì mạng là đơn vị, chúng không thể có các đỉnh chung, vì vậy tổng số đỉnh là $\ge (|f'| - |f|)\sqrt{V}$, nhưng nó cũng $\le V$, vì vậy trong $\sqrt{V}$ lần lặp nữa, chúng ta chắc chắn sẽ tìm thấy luồng cực đại.

### Mạng có khả năng thông qua đơn vị

Trong một cài đặt tổng quát hơn khi tất cả các cạnh có khả năng thông qua đơn vị, _nhưng số lượng cạnh vào và ra không bị giới hạn_, các đường đi không thể có các cạnh chung thay vì các đỉnh chung. Theo một cách tương tự, nó cho phép chứng minh giới hạn $\sqrt E$ về số lần lặp, do đó thời gian chạy của thuật toán Dinic trên các mạng như vậy nhiều nhất là $O(E \sqrt E)$.

Cuối cùng, cũng có thể chứng minh rằng số lượng giai đoạn trên các mạng có khả năng thông qua đơn vị không vượt quá $O(V^{2/3})$, cung cấp một ước tính thay thế là $O(EV^{2/3})$ trên các mạng có số lượng cạnh đặc biệt lớn.

## Cài đặt

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

## Bài tập thực hành

* [SPOJ: FASTFLOW](https://www.spoj.com/problems/FASTFLOW/)
