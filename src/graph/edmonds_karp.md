---
tags:
  - Translated
e_maxx_link: edmonds_karp
---

# Luồng cực đại - Ford-Fulkerson và Edmonds-Karp

Thuật toán Edmonds-Karp là một cách triển khai của phương pháp Ford-Fulkerson để tính toán một luồng cực đại trong một mạng luồng.

## Mạng luồng

Đầu tiên, hãy định nghĩa một **mạng luồng**, một **luồng**, và một **luồng cực đại** là gì.

Một **mạng** là một đồ thị có hướng $G$ với các đỉnh $V$ và các cạnh $E$ kết hợp với một hàm $c$, gán cho mỗi cạnh $e \in E$ một giá trị nguyên không âm, **khả năng thông qua** của $e$.
Một mạng như vậy được gọi là **mạng luồng**, nếu chúng ta còn gán nhãn cho hai đỉnh, một là **nguồn** và một là **đích**.

Một **luồng** trong một mạng luồng là một hàm $f$, lại gán cho mỗi cạnh $e$ một giá trị nguyên không âm, cụ thể là luồng.
Hàm này phải thỏa mãn hai điều kiện sau:

Luồng của một cạnh không thể vượt quá khả năng thông qua của nó.

$$f(e) \le c(e)$$

Và tổng của luồng vào của một đỉnh $u$ phải bằng tổng của luồng ra của $u$ ngoại trừ ở các đỉnh nguồn và đích.

$$\sum_{(v, u) \in E} f((v, u)) = \sum_{(u, v) \in E} f((u, v))$$

Đỉnh nguồn $s$ chỉ có luồng ra, và đỉnh đích $t$ chỉ có luồng vào.

Dễ thấy rằng phương trình sau đây đúng:

$$\sum_{(s, u) \in E} f((s, u)) = \sum_{(u, t) \in E} f((u, t))$$

Một sự tương tự tốt cho một mạng luồng là sự hình dung sau đây:
Chúng ta biểu diễn các cạnh như các đường ống nước, khả năng thông qua của một cạnh là lượng nước tối đa có thể chảy qua đường ống mỗi giây, và luồng của một cạnh là lượng nước hiện đang chảy qua đường ống mỗi giây.
Điều này thúc đẩy điều kiện luồng đầu tiên. Không thể có nhiều nước chảy qua một đường ống hơn khả năng thông qua của nó.
Các đỉnh hoạt động như các điểm giao, nơi nước ra khỏi một số đường ống, và sau đó, các đỉnh này phân phối nước theo một cách nào đó đến các đường ống khác.
Điều này cũng thúc đẩy điều kiện luồng thứ hai.
Tất cả nước vào phải được phân phối đến các đường ống khác trong mỗi điểm giao.
Nó không thể biến mất hoặc xuất hiện một cách kỳ diệu.
Nguồn $s$ là nguồn gốc của tất cả nước, và nước chỉ có thể thoát ra ở đích $t$.

Hình ảnh sau đây cho thấy một mạng luồng.
Giá trị đầu tiên của mỗi cạnh biểu thị luồng, ban đầu là 0, và giá trị thứ hai biểu thị khả năng thông qua.
<div style="text-align: center;">
  <img src="Flow1.png" alt="Mạng luồng">
</div>

Giá trị của luồng của một mạng là tổng của tất cả các luồng được tạo ra ở nguồn $s$, hoặc tương đương với tổng của tất cả các luồng được tiêu thụ bởi đích $t$.
Một **luồng cực đại** là một luồng có giá trị lớn nhất có thể.
Tìm luồng cực đại này của một mạng luồng là bài toán mà chúng ta muốn giải quyết.

Trong hình dung với các đường ống nước, bài toán có thể được phát biểu theo cách sau:
chúng ta có thể đẩy bao nhiêu nước qua các đường ống từ nguồn đến đích?

Hình ảnh sau đây cho thấy luồng cực đại trong mạng luồng.
<div style="text-align: center;">
  <img src="Flow9.png" alt="Luồng cực đại">
</div>

## Phương pháp Ford-Fulkerson

Hãy định nghĩa thêm một điều nữa.
Một **khả năng thông qua còn dư** của một cạnh có hướng là khả năng thông qua trừ đi luồng.
Cần lưu ý rằng nếu có một luồng dọc theo một cạnh có hướng $(u, v)$, thì cạnh ngược lại có khả năng thông qua là 0 và chúng ta có thể định nghĩa luồng của nó là $f((v, u)) = -f((u, v))$.
Điều này cũng định nghĩa khả năng thông qua còn dư cho tất cả các cạnh ngược.
Chúng ta có thể tạo ra một **mạng còn dư** từ tất cả các cạnh này, chỉ là một mạng có cùng các đỉnh và cạnh, nhưng chúng ta sử dụng các khả năng thông qua còn dư làm khả năng thông qua.

Phương pháp Ford-Fulkerson hoạt động như sau.
Đầu tiên, chúng ta đặt luồng của mỗi cạnh về không.
Sau đó, chúng ta tìm kiếm một **đường tăng luồng** từ $s$ đến $t$.
Một đường tăng luồng là một đường đi đơn giản trong đồ thị còn dư nơi khả năng thông qua còn dư là dương cho tất cả các cạnh dọc theo đường đi đó.
Nếu một đường đi như vậy được tìm thấy, thì chúng ta có thể tăng luồng dọc theo các cạnh này.
Chúng ta tiếp tục tìm kiếm các đường tăng luồng và tăng luồng.
Một khi một đường tăng luồng không còn tồn tại, luồng là cực đại.

Hãy chỉ rõ hơn, việc tăng luồng dọc theo một đường tăng luồng có nghĩa là gì.
Gọi $C$ là khả năng thông qua còn dư nhỏ nhất của các cạnh trong đường đi.
Khi đó chúng ta tăng luồng theo cách sau:
chúng ta cập nhật $f((u, v)) ~\text{+=}~ C$ và $f((v, u)) ~\text{-=}~ C$ cho mỗi cạnh $(u, v)$ trong đường đi.

Đây là một ví dụ để minh họa phương pháp.
Chúng ta sử dụng cùng một mạng luồng như trên.
Ban đầu chúng ta bắt đầu với một luồng là 0.
<div style="text-align: center;">
  <img src="Flow1.png" alt="Mạng luồng">
</div>

Chúng ta có thể tìm thấy đường đi $s - A - B - t$ với các khả năng thông qua còn dư là 7, 5, và 8.
Giá trị nhỏ nhất của chúng là 5, do đó chúng ta có thể tăng luồng dọc theo đường đi này thêm 5.
Điều này cho một luồng là 5 cho mạng.
<div style="text-align: center;">
  <img src="Flow2.png" alt="Đường đi đầu tiên">
  <img src="Flow3.png" alt="Mạng sau đường đi đầu tiên">
</div>

Một lần nữa chúng ta tìm kiếm một đường tăng luồng, lần này chúng ta tìm thấy $s - D - A - C - t$ với các khả năng thông qua còn dư là 4, 3, 3, và 5.
Do đó chúng ta có thể tăng luồng thêm 3 và chúng ta có một luồng là 8 cho mạng.
<div style="text-align: center;">
  <img src="Flow4.png" alt="Đường đi thứ hai">
  <img src="Flow5.png" alt="Mạng sau đường đi thứ hai">
</div>

Lần này chúng ta tìm thấy đường đi $s - D - C - B - t$ với các khả năng thông qua còn dư là 1, 2, 3, và 3, và do đó, chúng ta tăng luồng thêm 1.
<div style="text-align: center;">
  <img src="Flow6.png" alt="Đường đi thứ ba">
  <img src="Flow7.png" alt="Mạng sau đường đi thứ ba">
</div>

Lần này chúng ta tìm thấy đường tăng luồng $s - A - D - C - t$ với các khả năng thông qua còn dư là 2, 3, 1, và 2.
Chúng ta có thể tăng luồng thêm 1.
Nhưng đường đi này rất thú vị.
Nó bao gồm cạnh ngược $(A, D)$.
Trong mạng luồng ban đầu, chúng ta không được phép gửi bất kỳ luồng nào từ $A$ đến $D$.
Nhưng vì chúng ta đã có một luồng là 3 từ $D$ đến $A$, điều này là có thể.
Trực giác của nó là như sau:
Thay vì gửi một luồng là 3 từ $D$ đến $A$, chúng ta chỉ gửi 2 và bù lại bằng cách gửi một luồng bổ sung là 1 từ $s$ đến $A$, điều này cho phép chúng ta gửi một luồng bổ sung là 1 dọc theo đường đi $D - C - t$.
<div style="text-align: center;">
  <img src="Flow8.png" alt="Đường đi thứ tư">
  <img src="Flow9.png" alt="Mạng sau đường đi thứ tư">
</div>

Bây giờ, không thể tìm thấy một đường tăng luồng giữa $s$ và $t$, do đó luồng này là $10$ là luồng cực đại có thể có.
Chúng ta đã tìm thấy luồng cực đại.

Cần lưu ý rằng, phương pháp Ford-Fulkerson không chỉ định một phương pháp tìm kiếm đường tăng luồng.
Các cách tiếp cận có thể là sử dụng [DFS](depth-first-search.md) hoặc [BFS](breadth-first-search.md) đều hoạt động trong $O(E)$.
Nếu tất cả các khả năng thông qua của mạng là số nguyên, thì với mỗi đường tăng luồng, luồng của mạng tăng ít nhất 1 (để biết thêm chi tiết, xem [định lý luồng nguyên](#integral-theorem)).
Do đó, độ phức tạp của Ford-Fulkerson là $O(E F)$, trong đó $F$ là luồng cực đại của mạng.
Trong trường hợp khả năng thông qua là số hữu tỉ, thuật toán cũng sẽ kết thúc, nhưng độ phức tạp không bị giới hạn.
Trong trường hợp khả năng thông qua là số vô tỉ, thuật toán có thể không bao giờ kết thúc, và thậm chí có thể không hội tụ về luồng cực đại.

## Thuật toán Edmonds-Karp

Thuật toán Edmonds-Karp chỉ là một cách triển khai của phương pháp Ford-Fulkerson sử dụng [BFS](breadth-first-search.md) để tìm các đường tăng luồng.
Thuật toán lần đầu tiên được Yefim Dinitz công bố vào năm 1970, và sau đó được Jack Edmonds và Richard Karp công bố độc lập vào năm 1972.

Độ phức tạp có thể được đưa ra độc lập với luồng cực đại.
Thuật toán chạy trong thời gian $O(V E^2)$, ngay cả với các khả năng thông qua là số vô tỉ.
Trực giác là, mỗi lần chúng ta tìm thấy một đường tăng luồng, một trong các cạnh trở nên bão hòa, và khoảng cách từ cạnh đó đến $s$ sẽ dài hơn nếu nó xuất hiện lại sau này trong một đường tăng luồng.
Độ dài của các đường đi đơn giản bị giới hạn bởi $V$.

### Cài đặt

Ma trận `capacity` lưu trữ khả năng thông qua cho mọi cặp đỉnh.
`adj` là danh sách kề của **đồ thị vô hướng**, vì chúng ta cũng phải sử dụng các cạnh ngược của các cạnh có hướng khi chúng ta tìm kiếm các đường tăng luồng.

Hàm `maxflow` sẽ trả về giá trị của luồng cực đại.
Trong quá trình thuật toán, ma trận `capacity` thực sự sẽ lưu trữ khả năng thông qua còn dư của mạng.
Giá trị của luồng trong mỗi cạnh thực sự sẽ không được lưu trữ, nhưng rất dễ dàng để mở rộng việc triển khai - bằng cách sử dụng một ma trận bổ sung - để cũng lưu trữ luồng và trả về nó.

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

## Định lý luồng nguyên ## { #integral-theorem}

Định lý nói rằng, nếu mọi khả năng thông qua trong mạng là một số nguyên, thì kích thước của luồng cực đại là một số nguyên, và có một luồng cực đại sao cho luồng trong mỗi cạnh cũng là một số nguyên. Cụ thể, phương pháp Ford-Fulkerson tìm thấy một luồng như vậy.

## Định lý luồng cực đại - lát cắt tối thiểu

Một **$s$-$t$-cắt** là một sự phân hoạch các đỉnh của một mạng luồng thành hai tập, sao cho một tập bao gồm nguồn $s$ và tập còn lại bao gồm đích $t$.
Khả năng thông qua của một $s$-$t$-cắt được định nghĩa là tổng các khả năng thông qua của các cạnh từ phía nguồn đến phía đích.

Rõ ràng, chúng ta không thể gửi nhiều luồng hơn từ $s$ đến $t$ so với khả năng thông qua của bất kỳ $s$-$t$-cắt nào.
Do đó, luồng cực đại bị giới hạn bởi khả năng thông qua của lát cắt tối thiểu.

Định lý luồng cực đại - lát cắt tối thiểu thậm chí còn đi xa hơn.
Nó nói rằng khả năng thông qua của luồng cực đại phải bằng khả năng thông qua của lát cắt tối thiểu.

Trong hình ảnh sau, bạn có thể thấy lát cắt tối thiểu của mạng luồng mà chúng ta đã sử dụng trước đó.
Nó cho thấy rằng khả năng thông qua của lát cắt {s, A, D} và {B, C, t} là $5 + 3 + 2 = 10$, bằng với luồng cực đại mà chúng ta đã tìm thấy.
Các lát cắt khác sẽ có khả năng thông qua lớn hơn, như khả năng thông qua giữa {s, A} và {B, C, D, t} là $4 + 3 + 5 = 12$.
<div style="text-align: center;">
  <img src="Cut.png" alt="Lát cắt tối thiểu">
</div>

Một lát cắt tối thiểu có thể được tìm thấy sau khi thực hiện một phép tính luồng cực đại bằng phương pháp Ford-Fulkerson.
Một lát cắt tối thiểu có thể là như sau:
tập hợp tất cả các đỉnh có thể đến được từ $s$ trong đồ thị còn dư (sử dụng các cạnh có khả năng thông qua còn dư dương), và tập hợp tất cả các đỉnh khác.
Sự phân hoạch này có thể được tìm thấy dễ dàng bằng cách sử dụng [DFS](depth-first-search.md) bắt đầu tại $s$.

## Bài tập thực hành
- [Codeforces - Array and Operations](https://codeforces.com/contest/498/problem/c)
- [Codeforces - Red-Blue Graph](https://codeforces.com/contest/1288/problem/f)
- [CSES - Download Speed](https://cses.fi/problemset/task/1694)
- [CSES - Police Chase](https://cses.fi/problemset/task/1695)
- [CSES - School Dance](https://cses.fi/problemset/task/1696)
- [CSES - Distinct Routes](https://cses.fi/problemset/task/1711)

```