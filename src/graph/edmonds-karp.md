---
tags:
  - Translated
e_maxx_link: edmonds_karp
---

# Luồng cực đại - Ford-Fulkerson và Edmonds-Karp (Maximum flow - Ford-Fulkerson and Edmonds-Karp) {: #maximum-flow-ford-fulkerson-and-edmonds-karp}

Thuật toán Edmonds-Karp là một cài đặt của phương pháp Ford-Fulkerson để tính toán luồng cực đại trong một mạng luồng.

## Mạng luồng (Flow network) {: #flow-network}

Đầu tiên hãy định nghĩa **mạng luồng**, **luồng**, và **luồng cực đại** là gì.

Một **mạng** là một đồ thị có hướng $G$ với các đỉnh $V$ và các cạnh $E$ kết hợp với một hàm $c$, gán cho mỗi cạnh $e \in E$ một giá trị nguyên không âm, là **dung lượng** của $e$.
Một mạng như vậy được gọi là **mạng luồng**, nếu chúng ta gán nhãn thêm cho hai đỉnh, một là **nguồn** (source) và một là **đích** (sink).

Một **luồng** trong mạng luồng là hàm $f$, hàm này lại gán cho mỗi cạnh $e$ một giá trị nguyên không âm, cụ thể là luồng.
Hàm này phải thỏa mãn hai điều kiện sau:

Luồng của một cạnh không được vượt quá dung lượng.

$$f(e) \le c(e)$$

Và tổng luồng đi vào của một đỉnh $u$ phải bằng tổng luồng đi ra của $u$ ngoại trừ các đỉnh nguồn và đích.

$$\sum_{(v, u) \in E} f((v, u)) = \sum_{(u, v) \in E} f((u, v))$$

Đỉnh nguồn $s$ chỉ có luồng đi ra, và đỉnh đích $t$ chỉ có luồng đi vào.

Dễ dàng thấy rằng phương trình sau đây đúng:

$$\sum_{(s, u) \in E} f((s, u)) = \sum_{(u, t) \in E} f((u, t))$$

Một sự tương tự tốt cho mạng luồng là hình ảnh trực quan sau:
Chúng ta biểu diễn các cạnh như các đường ống nước, dung lượng của một cạnh là lượng nước tối đa có thể chảy qua đường ống mỗi giây, và luồng của một cạnh là lượng nước hiện đang chảy qua đường ống mỗi giây.
Điều này thúc đẩy điều kiện luồng đầu tiên. Nước chảy qua một đường ống không thể nhiều hơn dung lượng của nó.
Các đỉnh đóng vai trò là các điểm nối, nơi nước chảy ra từ một số đường ống, và sau đó, các đỉnh này phân phối nước theo một cách nào đó đến các đường ống khác.
Điều này cũng thúc đẩy điều kiện luồng thứ hai.
Tất cả nước đi vào phải được phân phối đến các đường ống khác trong mỗi điểm nối.
Nó không thể biến mất hoặc xuất hiện một cách kỳ diệu.
Nguồn $s$ là nguồn gốc của tất cả nước, và nước chỉ có thể thoát ra ở đích $t$.

Hình ảnh sau đây cho thấy một mạng luồng.
Giá trị đầu tiên của mỗi cạnh biểu thị luồng, ban đầu là 0, và giá trị thứ hai biểu thị dung lượng.
<div style="text-align: center;">
  <img src="Flow1.png" alt="Flow network">
</div>

Giá trị của luồng của một mạng là tổng của tất cả các luồng được tạo ra trong nguồn $s$, hoặc tương đương với tổng của tất cả các luồng được tiêu thụ bởi đích $t$.
Một **luồng cực đại** là một luồng có giá trị lớn nhất có thể.
Tìm luồng cực đại này của một mạng luồng là bài toán mà chúng ta muốn giải quyết.

Trong hình ảnh trực quan với các đường ống nước, bài toán có thể được phát biểu theo cách sau:
chúng ta có thể đẩy bao nhiêu nước qua các đường ống từ nguồn đến đích?

Hình ảnh sau đây cho thấy luồng cực đại trong mạng luồng.
<div style="text-align: center;">
  <img src="Flow9.png" alt="Maximal flow">
</div>

## Phương pháp Ford-Fulkerson (Ford-Fulkerson method) {: #ford-fulkerson-method}

Hãy định nghĩa thêm một điều nữa.
**Dung lượng dư** (residual capacity) của một cạnh có hướng là dung lượng trừ đi luồng.
Cần lưu ý rằng nếu có một luồng dọc theo một cạnh có hướng nào đó $(u, v)$, thì cạnh ngược lại có dung lượng 0 và chúng ta có thể định nghĩa luồng của nó là $f((v, u)) = -f((u, v))$.
Điều này cũng định nghĩa dung lượng dư cho tất cả các cạnh ngược lại.
Chúng ta có thể tạo một **mạng dư** (residual network) từ tất cả các cạnh này, đó chỉ là một mạng với cùng các đỉnh và cạnh, nhưng chúng ta sử dụng dung lượng dư làm dung lượng.

Phương pháp Ford-Fulkerson hoạt động như sau.
Đầu tiên, chúng ta đặt luồng của mỗi cạnh bằng 0.
Sau đó chúng ta tìm kiếm một **đường tăng luồng** (augmenting path) từ $s$ đến $t$.
Đường tăng luồng là một đường đi đơn trong đồ thị dư trong đó dung lượng dư là dương đối với tất cả các cạnh dọc theo đường đi đó.
Nếu tìm thấy một đường đi như vậy, thì chúng ta có thể tăng luồng dọc theo các cạnh này.
Chúng ta tiếp tục tìm kiếm các đường tăng luồng và tăng luồng.
Khi đường tăng luồng không còn tồn tại nữa, luồng là cực đại.

Hãy xác định chi tiết hơn, việc tăng luồng dọc theo một đường tăng luồng nghĩa là gì.
Gọi $C$ là dung lượng dư nhỏ nhất của các cạnh trong đường đi.
Sau đó chúng ta tăng luồng theo cách sau:
chúng ta cập nhật $f((u, v)) ~\text{+=}~ C$ và $f((v, u)) ~\text{-=}~ C$ cho mỗi cạnh $(u, v)$ trong đường đi.

Dưới đây là một ví dụ để chứng minh phương pháp.
Chúng ta sử dụng cùng một mạng luồng như trên.
Ban đầu chúng ta bắt đầu với luồng bằng 0.
<div style="text-align: center;">
  <img src="Flow1.png" alt="Flow network">
</div>

Chúng ta có thể tìm thấy đường đi $s - A - B - t$ với các dung lượng dư 7, 5, và 8.
Giá trị nhỏ nhất của chúng là 5, do đó chúng ta có thể tăng luồng dọc theo đường đi này thêm 5.
Điều này mang lại luồng bằng 5 cho mạng.
<div style="text-align: center;">
  <img src="Flow2.png" alt="First path">
  <img src="Flow3.png" alt="Network after first path">
</div>

Một lần nữa chúng ta tìm kiếm một đường tăng luồng, lần này chúng ta tìm thấy $s - D - A - C - t$ với các dung lượng dư 4, 3, 3, và 5.
Do đó chúng ta có thể tăng luồng thêm 3 và chúng ta nhận được luồng bằng 8 cho mạng.
<div style="text-align: center;">
  <img src="Flow4.png" alt="Second path">
  <img src="Flow5.png" alt="Network after second path">
</div>

Lần này chúng ta tìm thấy đường đi $s - D - C - B - t$ với các dung lượng dư 1, 2, 3, và 3, và do đó, chúng ta tăng luồng thêm 1.
<div style="text-align: center;">
  <img src="Flow6.png" alt="Third path">
  <img src="Flow7.png" alt="Network after third path">
</div>

Lần này chúng ta tìm thấy đường tăng luồng $s - A - D - C - t$ với các dung lượng dư 2, 3, 1, và 2.
Chúng ta có thể tăng luồng thêm 1.
Nhưng đường đi này rất thú vị.
Nó bao gồm cạnh ngược $(A, D)$.
Trong mạng luồng ban đầu, chúng ta không được phép gửi bất kỳ luồng nào từ $A$ đến $D$.
Nhưng vì chúng ta đã có luồng bằng 3 từ $D$ đến $A$, điều này là có thể.
Trực giác của nó là như sau:
Thay vì gửi luồng bằng 3 từ $D$ đến $A$, chúng ta chỉ gửi 2 và bù đắp điều này bằng cách gửi thêm luồng bằng 1 từ $s$ đến $A$, điều này cho phép chúng ta gửi thêm luồng bằng 1 dọc theo đường đi $D - C - t$.
<div style="text-align: center;">
  <img src="Flow8.png" alt="Fourth path">
  <img src="Flow9.png" alt="Network after fourth path">
</div>

Bây giờ, không thể tìm thấy đường tăng luồng nào giữa $s$ và $t$, do đó luồng $10$ này là lớn nhất có thể.
Chúng ta đã tìm thấy luồng cực đại.

Cần lưu ý rằng, phương pháp Ford-Fulkerson không chỉ định phương pháp tìm đường tăng luồng.
Các cách tiếp cận có thể là sử dụng [DFS](depth-first-search.md) hoặc [BFS](breadth-first-search.md), cả hai đều hoạt động trong $O(E)$.
Nếu tất cả các dung lượng của mạng là số nguyên, thì đối với mỗi đường tăng luồng, luồng của mạng tăng ít nhất 1 (để biết thêm chi tiết xem [Định lý luồng nguyên](#integral-theorem)).
Do đó, độ phức tạp của Ford-Fulkerson là $O(E F)$, trong đó $F$ là luồng cực đại của mạng.
Trong trường hợp dung lượng là số hữu tỉ, thuật toán cũng sẽ kết thúc, nhưng độ phức tạp không bị chặn.
Trong trường hợp dung lượng là số vô tỉ, thuật toán có thể không bao giờ kết thúc, và thậm chí có thể không hội tụ về luồng cực đại.

## Thuật toán Edmonds-Karp (Edmonds-Karp algorithm) {: #edmonds-karp-algorithm}

Thuật toán Edmonds-Karp chỉ là một cài đặt của phương pháp Ford-Fulkerson sử dụng [BFS](breadth-first-search.md) để tìm các đường tăng luồng.
Thuật toán được xuất bản lần đầu tiên bởi Yefim Dinitz vào năm 1970, và sau đó được xuất bản độc lập bởi Jack Edmonds và Richard Karp vào năm 1972.

Độ phức tạp có thể được đưa ra độc lập với luồng cực đại.
Thuật toán chạy trong thời gian $O(V E^2)$, ngay cả đối với dung lượng vô tỉ.
Trực giác là, mỗi khi chúng ta tìm thấy một đường tăng luồng, một trong các cạnh trở nên bão hòa, và khoảng cách từ cạnh đến $s$ sẽ dài hơn nếu nó xuất hiện lại sau này trong một đường tăng luồng.
Độ dài của các đường đi đơn bị chặn bởi $V$.

### Cài đặt (Implementation) {: #implementation}

Ma trận `capacity` lưu trữ dung lượng cho mọi cặp đỉnh.
`adj` là danh sách kề của **đồ thị vô hướng**, vì chúng ta cũng phải sử dụng cạnh ngược của các cạnh có hướng khi chúng ta đang tìm kiếm các đường tăng luồng.

Hàm `maxflow` sẽ trả về giá trị của luồng cực đại.
Trong thuật toán, ma trận `capacity` thực sự sẽ lưu trữ dung lượng dư của mạng.
Giá trị của luồng trong mỗi cạnh thực sự sẽ không được lưu trữ, nhưng rất dễ để mở rộng cài đặt - bằng cách sử dụng một ma trận bổ sung - để cũng lưu trữ luồng và trả về nó.

```cpp
int n;
vector<vector<int>> capacity;
vector<vector<int>> adj;

int bfs(int s, int t, vector<int>& parent) {
    fill(parent.begin(), parent.end(), -1);
    parent[s] = -2;
    queue<pair<int, int>> q;
    q.push({s, INF});

    while (!q.empty()) {
        int cur = q.front().first;
        int flow = q.front().second;
        q.pop();

        for (int next : adj[cur]) {
            if (parent[next] == -1 && capacity[cur][next]) {
                parent[next] = cur;
                int new_flow = min(flow, capacity[cur][next]);
                if (next == t)
                    return new_flow;
                q.push({next, new_flow});
            }
        }
    }

    return 0;
}

int maxflow(int s, int t) {
    int flow = 0;
    vector<int> parent(n);
    int new_flow;

    while (new_flow = bfs(s, t, parent)) {
        flow += new_flow;
        int cur = t;
        while (cur != s) {
            int prev = parent[cur];
            capacity[prev][cur] -= new_flow;
            capacity[cur][prev] += new_flow;
            cur = prev;
        }
    }

    return flow;
}
```

## Định lý luồng nguyên (Integral flow theorem) {: #integral-theorem}

Định lý nói rằng, nếu mọi dung lượng trong mạng là một số nguyên, thì kích thước của luồng cực đại là một số nguyên, và có một luồng cực đại sao cho luồng trong mỗi cạnh cũng là một số nguyên. Đặc biệt, phương pháp Ford-Fulkerson tìm thấy một luồng như vậy.

## Định lý Luồng cực đại lát cắt cực tiểu (Max-flow min-cut theorem) {: #max-flow-min-cut-theorem}

Một **lát cắt $s$-$t$** là một phân hoạch các đỉnh của một mạng luồng thành hai tập hợp, sao cho một tập hợp bao gồm nguồn $s$ và tập hợp kia bao gồm đích $t$.
Dung lượng của một lát cắt $s$-$t$ được định nghĩa là tổng dung lượng của các cạnh từ phía nguồn đến phía đích.

Rõ ràng, chúng ta không thể gửi nhiều luồng từ $s$ đến $t$ hơn dung lượng của bất kỳ lát cắt $s$-$t$ nào.
Do đó, luồng cực đại bị chặn bởi dung lượng lát cắt cực tiểu.

Định lý luồng cực đại lát cắt cực tiểu thậm chí còn đi xa hơn.
Nó nói rằng dung lượng của luồng cực đại phải bằng dung lượng của lát cắt cực tiểu.

Trong hình ảnh sau đây, bạn có thể thấy lát cắt cực tiểu của mạng luồng chúng ta đã sử dụng trước đó.
Nó cho thấy dung lượng của lát cắt $\{s, A, D\}$ và $\{B, C, t\}$ là $5 + 3 + 2 = 10$, bằng với luồng cực đại mà chúng ta đã tìm thấy.
Các lát cắt khác sẽ có dung lượng lớn hơn, như dung lượng giữa $\{s, A\}$ và $\{B, C, D, t\}$ là $4 + 3 + 5 = 12$.
<div style="text-align: center;">
  <img src="Cut.png" alt="Minimum cut">
</div>

Lát cắt cực tiểu có thể được tìm thấy sau khi thực hiện tính toán luồng cực đại bằng phương pháp Ford-Fulkerson.
Một lát cắt cực tiểu có thể là như sau:
tập hợp tất cả các đỉnh có thể đến được từ $s$ trong đồ thị dư (sử dụng các cạnh có dung lượng dư dương), và tập hợp tất cả các đỉnh khác.
Phân vùng này có thể dễ dàng tìm thấy bằng cách sử dụng [DFS](depth-first-search.md) bắt đầu tại $s$.

## Bài tập (Practice Problems) {: #practice-problems}
- [Codeforces - Array and Operations](https://codeforces.com/contest/498/problem/c)
- [Codeforces - Red-Blue Graph](https://codeforces.com/contest/1288/problem/f)
- [CSES - Download Speed](https://cses.fi/problemset/task/1694)
- [CSES - Police Chase](https://cses.fi/problemset/task/1695)
- [CSES - School Dance](https://cses.fi/problemset/task/1696)
- [CSES - Distinct Routes](https://cses.fi/problemset/task/1711)
