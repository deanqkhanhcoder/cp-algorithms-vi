---
tags:
  - Translated
e_maxx_link: min_cost_flow
---

# Luồng chi phí nhỏ nhất - Thuật toán đường đi ngắn nhất liên tiếp (Minimum-cost flow - Successive shortest path algorithm) {: #minimum-cost-flow-successive-shortest-path-algorithm}

Cho một mạng $G$ bao gồm $n$ đỉnh và $m$ cạnh.
Đối với mỗi cạnh (nói chung là các cạnh có hướng, nhưng xem bên dưới), dung lượng (một số nguyên không âm) và chi phí trên một đơn vị luồng dọc theo cạnh này (một số nguyên nào đó) được đưa ra.
Nguồn $s$ và đích $t$ cũng được đánh dấu.

Với một giá trị $K$ cho trước, chúng ta phải tìm một luồng có lượng này, và trong số tất cả các luồng có lượng này, chúng ta phải chọn luồng có chi phí thấp nhất.
Nhiệm vụ này được gọi là **bài toán luồng chi phí nhỏ nhất** (minimum-cost flow problem).

Đôi khi nhiệm vụ được đưa ra hơi khác một chút:
bạn muốn tìm luồng cực đại, và trong số tất cả các luồng cực đại, chúng ta muốn tìm luồng có chi phí thấp nhất.
Đây được gọi là **bài toán luồng cực đại chi phí nhỏ nhất** (minimum-cost maximum-flow problem).

Cả hai bài toán này đều có thể được giải quyết hiệu quả bằng thuật toán đường đi ngắn nhất liên tiếp.

## Thuật toán (Algorithm) {: #algorithm}

Thuật toán này rất giống với [Edmonds-Karp](edmonds-karp.md) để tính toán luồng cực đại.

### Trường hợp đơn giản nhất (Simplest case) {: #simplest-case}

Trước tiên, chúng ta chỉ xem xét trường hợp đơn giản nhất, trong đó đồ thị có hướng và có tối đa một cạnh giữa bất kỳ cặp đỉnh nào (ví dụ: nếu $(i, j)$ là một cạnh trong đồ thị, thì $(j, i)$ cũng không thể là một phần trong đó).

Gọi $U_{i j}$ là dung lượng của một cạnh $(i, j)$ nếu cạnh này tồn tại.
Và gọi $C_{i j}$ là chi phí trên một đơn vị luồng dọc theo cạnh này $(i, j)$.
Và cuối cùng gọi $F_{i, j}$ là luồng dọc theo cạnh $(i, j)$.
Ban đầu tất cả các giá trị luồng là số không.

Chúng ta **sửa đổi** mạng như sau:
đối với mỗi cạnh $(i, j)$ chúng ta thêm **cạnh ngược** $(j, i)$ vào mạng với dung lượng $U_{j i} = 0$ và chi phí $C_{j i} = -C_{i j}$.
Vì, theo các hạn chế của chúng tôi, cạnh $(j, i)$ không có trong mạng trước đó, nên chúng ta vẫn có một mạng không phải là đa đồ thị (đồ thị có nhiều cạnh).
Ngoài ra chúng ta sẽ luôn giữ điều kiện $F_{j i} = -F_{i j}$ đúng trong các bước của thuật toán.

Chúng ta định nghĩa **mạng dư** (residual network) cho một luồng cố định $F$ như sau (giống như trong thuật toán Ford-Fulkerson):
mạng dư chỉ chứa các cạnh chưa bão hòa (tức là các cạnh trong đó $F_{i j} < U_{i j}$), và dung lượng dư của mỗi cạnh như vậy là $R_{i j} = U_{i j} - F_{i j}$.

Bây giờ chúng ta có thể nói về **thuật toán** để tính toán luồng chi phí nhỏ nhất.
Ở mỗi lần lặp của thuật toán, chúng ta tìm đường đi ngắn nhất trong đồ thị dư từ $s$ đến $t$.
Ngược lại với Edmonds-Karp, chúng ta tìm kiếm đường đi ngắn nhất theo chi phí của đường đi thay vì số lượng cạnh.
Nếu không tồn tại đường đi nào nữa, thì thuật toán kết thúc, và luồng $F$ là luồng mong muốn.
Nếu một đường đi được tìm thấy, chúng ta tăng luồng dọc theo nó nhiều nhất có thể (tức là chúng ta tìm dung lượng dư tối thiểu $R$ của đường đi, và tăng luồng theo nó, và giảm các cạnh ngược một lượng tương tự).
Nếu tại một thời điểm nào đó luồng đạt đến giá trị $K$, thì chúng ta dừng thuật toán (lưu ý rằng trong lần lặp cuối cùng của thuật toán, cần tăng luồng chỉ bằng một lượng sao cho giá trị luồng cuối cùng không vượt quá $K$).

Không khó để thấy rằng, nếu chúng ta đặt $K$ thành vô cùng, thì thuật toán sẽ tìm thấy luồng cực đại chi phí nhỏ nhất.
Vì vậy, cả hai biến thể của bài toán đều có thể được giải quyết bằng cùng một thuật toán.

### Đồ thị vô hướng / đa đồ thị (Undirected graphs / multigraphs) {: #undirected-graphs-multigraphs}

Trường hợp đồ thị vô hướng hoặc đa đồ thị không khác biệt về mặt khái niệm so với thuật toán trên.
Thuật toán cũng sẽ hoạt động trên các đồ thị này.
Tuy nhiên, việc cài đặt nó trở nên khó khăn hơn một chút.

Một **cạnh vô hướng** $(i, j)$ thực sự giống như hai cạnh có hướng $(i, j)$ và $(j, i)$ có cùng dung lượng và giá trị.
Vì thuật toán luồng chi phí nhỏ nhất được mô tả ở trên tạo ra một cạnh ngược cho mỗi cạnh có hướng, nên nó chia cạnh vô hướng thành $4$ cạnh có hướng, và chúng ta thực sự nhận được một **đa đồ thị**.

Làm thế nào để chúng ta đối phó với **nhiều cạnh**?
Thứ nhất, luồng cho mỗi cạnh trong số nhiều cạnh phải được giữ riêng biệt.
Thứ hai, khi tìm kiếm đường đi ngắn nhất, cần phải tính đến việc cạnh nào trong số nhiều cạnh được sử dụng trong đường đi là quan trọng.
Do đó, thay vì mảng tổ tiên thông thường, chúng ta phải lưu trữ thêm số cạnh mà từ đó chúng ta đến cùng với tổ tiên.
Thứ ba, khi luồng tăng dọc theo một cạnh nhất định, cần phải giảm luồng dọc theo cạnh ngược lại.
Vì chúng ta có nhiều cạnh, chúng ta phải lưu trữ số cạnh cho cạnh đảo ngược cho mỗi cạnh.

Không có trở ngại nào khác với đồ thị vô hướng hoặc đa đồ thị.

### Độ phức tạp (Complexity) {: #complexity}

Thuật toán ở đây nói chung là số mũ theo kích thước của đầu vào. Cụ thể hơn, trong trường hợp xấu nhất, nó có thể chỉ đẩy nhiều nhất là $1$ đơn vị luồng trên mỗi lần lặp, mất $O(F)$ lần lặp để tìm một luồng chi phí tối thiểu có kích thước $F$, làm cho tổng thời gian chạy là $O(F \cdot T)$, trong đó $T$ là thời gian cần thiết để tìm đường đi ngắn nhất từ nguồn đến đích.

Nếu thuật toán [Bellman-Ford](bellman-ford.md) được sử dụng cho việc này, nó làm cho thời gian chạy là $O(F mn)$. Cũng có thể sửa đổi [thuật toán Dijkstra](dijkstra.md), để nó cần $O(nm)$ tiền xử lý như một bước đầu tiên và sau đó hoạt động trong $O(m \log n)$ mỗi lần lặp, làm cho tổng thời gian chạy chung là $O(mn + F m \log n)$. [Tại đây](http://web.archive.org/web/20211009144446/https://min-25.hatenablog.com/entry/2018/03/19/235802) là một bộ tạo đồ thị, trên đó thuật toán như vậy sẽ yêu cầu thời gian $O(2^{n/2} n^2 \log n)$.

Thuật toán Dijkstra sửa đổi sử dụng cái gọi là thế năng từ [thuật toán Johnson](https://en.wikipedia.org/wiki/Johnson%27s_algorithm). Có thể kết hợp các ý tưởng của thuật toán này và thuật toán Dinic để giảm số lần lặp từ $F$ xuống $\min(F, nC)$, trong đó $C$ là chi phí tối đa được tìm thấy giữa các cạnh. Bạn có thể đọc thêm về thế năng và sự kết hợp của chúng với thuật toán Dinic [tại đây](https://codeforces.com/blog/entry/105658).

## Cài đặt (Implementation) {: #implementation}

Dưới đây là một cài đặt sử dụng thuật toán [SPFA](bellman-ford.md) cho trường hợp đơn giản nhất.

```cpp
struct Edge
{
    int from, to, capacity, cost;
};

vector<vector<int>> adj, cost, capacity;

const int INF = 1e9;

void shortest_paths(int n, int v0, vector<int>& d, vector<int>& p) {
    d.assign(n, INF);
    d[v0] = 0;
    vector<bool> inq(n, false);
    queue<int> q;
    q.push(v0);
    p.assign(n, -1);

    while (!q.empty()) {
        int u = q.front();
        q.pop();
        inq[u] = false;
        for (int v : adj[u]) {
            if (capacity[u][v] > 0 && d[v] > d[u] + cost[u][v]) {
                d[v] = d[u] + cost[u][v];
                p[v] = u;
                if (!inq[v]) {
                    inq[v] = true;
                    q.push(v);
                }
            }
        }
    }
}

int min_cost_flow(int N, vector<Edge> edges, int K, int s, int t) {
    adj.assign(N, vector<int>());
    cost.assign(N, vector<int>(N, 0));
    capacity.assign(N, vector<int>(N, 0));
    for (Edge e : edges) {
        adj[e.from].push_back(e.to);
        adj[e.to].push_back(e.from);
        cost[e.from][e.to] = e.cost;
        cost[e.to][e.from] = -e.cost;
        capacity[e.from][e.to] = e.capacity;
    }

    int flow = 0;
    int cost = 0;
    vector<int> d, p;
    while (flow < K) {
        shortest_paths(N, s, d, p);
        if (d[t] == INF)
            break;
        
        // find max flow on that path
        int f = K - flow;
        int cur = t;
        while (cur != s) {
            f = min(f, capacity[p[cur]][cur]);
            cur = p[cur];
        }

        // apply flow
        flow += f;
        cost += f * d[t];
        cur = t;
        while (cur != s) {
            capacity[p[cur]][cur] -= f;
            capacity[cur][p[cur]] += f;
            cur = p[cur];
        }
    }

    if (flow < K)
        return -1;
    else
        return cost;
}
```

## Bài tập (Practice Problems) {: #practice-problems}

* [CSES - Task Assignment](https://cses.fi/problemset/task/2129)
* [CSES - Grid Puzzle II](https://cses.fi/problemset/task/2131)
* [AtCoder - Dream Team](https://atcoder.jp/contests/abc247/tasks/abc247_g)
