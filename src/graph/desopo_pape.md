---
tags:
  - Translated
e_maxx_link: levit_algorithm
---

# Thuật toán D´Esopo-Pape

Cho một đồ thị có $n$ đỉnh và $m$ cạnh với trọng số $w_i$ và một đỉnh bắt đầu $v_0$.
Nhiệm vụ là tìm đường đi ngắn nhất từ đỉnh $v_0$ đến mọi đỉnh khác.

Thuật toán của D´Esopo-Pape sẽ hoạt động nhanh hơn thuật toán [Dijkstra](dijkstra.md) và thuật toán [Bellman-Ford](bellman_ford.md) trong hầu hết các trường hợp, và cũng sẽ hoạt động với các cạnh có trọng số âm.
Tuy nhiên, không hoạt động với các chu trình âm.

## Mô tả

Gọi mảng $d$ chứa độ dài đường đi ngắn nhất, tức là $d_i$ là độ dài hiện tại của đường đi ngắn nhất từ đỉnh $v_0$ đến đỉnh $i$.
Ban đầu mảng này được điền với vô cùng cho mỗi đỉnh, ngoại trừ $d_{v_0} = 0$.
Sau khi thuật toán kết thúc, mảng này sẽ chứa các khoảng cách ngắn nhất.

Gọi mảng $p$ chứa các tổ tiên hiện tại, tức là $p_i$ là tổ tiên trực tiếp của đỉnh $i$ trên đường đi ngắn nhất hiện tại từ $v_0$ đến $i$.
Giống như mảng $d$, mảng $p$ thay đổi dần dần trong quá trình thuật toán và cuối cùng nhận các giá trị cuối cùng.

Bây giờ đến thuật toán.
Tại mỗi bước, ba tập hợp các đỉnh được duy trì:

- $M_0$ - các đỉnh, mà khoảng cách đã được tính toán (mặc dù nó có thể không phải là khoảng cách cuối cùng)
- $M_1$ - các đỉnh, mà khoảng cách hiện đang được tính toán
- $M_2$ - các đỉnh, mà khoảng cách chưa được tính toán

Các đỉnh trong tập $M_1$ được lưu trữ trong một hàng đợi hai đầu (deque).

Tại mỗi bước của thuật toán, chúng ta lấy một đỉnh từ tập $M_1$ (từ đầu hàng đợi).
Gọi $u$ là đỉnh được chọn.
Chúng ta đặt đỉnh $u$ này vào tập $M_0$.
Sau đó, chúng ta lặp qua tất cả các cạnh đi ra từ đỉnh này.
Gọi $v$ là đầu kia của cạnh hiện tại, và $w$ là trọng số của nó.

- Nếu $v$ thuộc $M_2$, thì $v$ được chèn vào tập $M_1$ bằng cách chèn nó vào cuối hàng đợi.
$d_v$ được đặt thành $d_u + w$.
- Nếu $v$ thuộc $M_1$, thì chúng ta cố gắng cải thiện giá trị của $d_v$: $d_v = \min(d_v, d_u + w)$.
Vì $v$ đã có trong $M_1$, chúng ta không cần chèn nó vào $M_1$ và hàng đợi.
- Nếu $v$ thuộc $M_0$, và nếu $d_v$ có thể được cải thiện $d_v > d_u + w$, thì chúng ta cải thiện $d_v$ và chèn đỉnh $v$ trở lại vào tập $M_1$, đặt nó ở đầu hàng đợi.

Và tất nhiên, với mỗi lần cập nhật trong mảng $d$, chúng ta cũng phải cập nhật phần tử tương ứng trong mảng $p$.

## Cài đặt

Chúng ta sẽ sử dụng một mảng $m$ để lưu trữ tập hợp mà mỗi đỉnh hiện đang thuộc về.

```cpp
struct Edge {
    int to, w;
};

int n;
vector<vector<Edge>> adj;

const int INF = 1e9;

void shortest_paths(int v0, vector<int>& d, vector<int>& p) {
    d.assign(n, INF);
    d[v0] = 0;
    vector<int> m(n, 2);
    deque<int> q;
    q.push_back(v0);
    p.assign(n, -1);

    while (!q.empty()) {
        int u = q.front();
        q.pop_front();
        m[u] = 0;
        for (Edge e : adj[u]) {
            if (d[e.to] > d[u] + e.w) {
                d[e.to] = d[u] + e.w;
                p[e.to] = u;
                if (m[e.to] == 2) {
                    m[e.to] = 1;
                    q.push_back(e.to);
                } else if (m[e.to] == 0) {
                    m[e.to] = 1;
                    q.push_front(e.to);
                }
            }
        }
    }
}
```

## Độ phức tạp

Thuật toán thường hoạt động khá nhanh - trong hầu hết các trường hợp, thậm chí còn nhanh hơn thuật toán của Dijkstra.
Tuy nhiên, có những trường hợp mà thuật toán mất thời gian theo cấp số nhân, làm cho nó không phù hợp trong trường hợp xấu nhất. Xem các cuộc thảo luận trên [Stack Overflow](https://stackoverflow.com/a/67642821) và [Codeforces](https://codeforces.com/blog/entry/3793) để tham khảo.