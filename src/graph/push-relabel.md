---
tags:
  - Translated
e_maxx_link: preflow_push
---

# Luồng cực đại - Thuật toán Push-relabel (Maximum flow - Push-relabel algorithm) {: #maximum-flow-push-relabel-algorithm}

Thuật toán Push-relabel (hay còn được gọi là thuật toán Preflow-push) là một thuật toán để tính toán luồng cực đại của một mạng luồng.
Định nghĩa chính xác của bài toán mà chúng ta muốn giải quyết có thể được tìm thấy trong bài viết [Luồng cực đại - Ford-Fulkerson và Edmonds-Karp](edmonds-karp.md).

Trong bài viết này, chúng ta sẽ xem xét giải quyết bài toán bằng cách đẩy một luồng tiền (preflow) qua mạng, thuật toán sẽ chạy trong thời gian $O(V^4)$, hoặc chính xác hơn là trong $O(V^2 E)$.
Thuật toán được thiết kế bởi Andrew Goldberg và Robert Tarjan vào năm 1985.

## Định nghĩa (Definitions) {: #definitions}

Trong quá trình thuật toán, chúng ta sẽ phải xử lý một **luồng tiền** (preflow) - tức là một hàm $f$ tương tự như hàm luồng, nhưng không nhất thiết phải thỏa mãn ràng buộc bảo toàn luồng.
Đối với nó chỉ cần các ràng buộc sau:

$$0 \le f(e) \le c(e)$$

và

$$\sum_{(v, u) \in E} f((v, u)) \ge \sum_{(u, v) \in E} f((u, v))$$

phải được thỏa mãn.

Vì vậy, một số đỉnh có thể nhận nhiều luồng hơn nó phân phối.
Chúng ta nói rằng đỉnh này có một lượng luồng dư thừa nào đó, và định nghĩa lượng dư thừa đó bằng hàm **dư thừa** (excess) $x(u) =\sum_{(v, u) \in E} f((v, u)) - \sum_{(u, v) \in E} f((u, v))$.

Theo cách tương tự như với hàm luồng, chúng ta có thể định nghĩa các dung lượng dư và đồ thị dư với hàm luồng tiền.

Thuật toán sẽ bắt đầu với một luồng tiền ban đầu (một số đỉnh có dư thừa), và trong quá trình thực thi, luồng tiền sẽ được xử lý và sửa đổi.
Tiết lộ một số chi tiết, thuật toán sẽ chọn một đỉnh có dư thừa và đẩy phần dư thừa sang các đỉnh lân cận.
Nó sẽ lặp lại điều này cho đến khi tất cả các đỉnh, ngoại trừ nguồn và đích, không còn dư thừa.
Dễ dàng thấy rằng, một luồng tiền không có dư thừa là một luồng hợp lệ.
Điều này làm cho thuật toán kết thúc với một luồng thực tế.

Vẫn còn hai vấn đề mà chúng ta phải giải quyết.
Thứ nhất, làm thế nào chúng ta đảm bảo rằng điều này thực sự kết thúc?
Và thứ hai, làm thế nào để chúng ta đảm bảo rằng điều này sẽ thực sự mang lại cho chúng ta một luồng cực đại, chứ không chỉ là bất kỳ luồng ngẫu nhiên nào?

Để giải quyết những vấn đề này, chúng ta cần sự trợ giúp của một hàm khác, cụ thể là hàm **gán nhãn** (labeling) $h$, thường được gọi là hàm **độ cao** (height), gán cho mỗi đỉnh một số nguyên.
Chúng ta gọi một cách gán nhãn là hợp lệ, nếu $h(s) = |V|$, $h(t) = 0$, và $h(u) \le h(v) + 1$ nếu có một cạnh $(u, v)$ trong đồ thị dư - tức là cạnh $(u, v)$ có dung lượng dương trong đồ thị dư.
Nói cách khác, nếu có thể tăng luồng từ $u$ đến $v$, thì độ cao của $v$ có thể nhỏ hơn độ cao của $u$ tối đa là một, nhưng nó có thể bằng hoặc thậm chí cao hơn.

Điều quan trọng cần lưu ý là nếu tồn tại một hàm gán nhãn hợp lệ, thì không tồn tại một đường tăng luồng từ $s$ đến $t$ trong đồ thị dư.
Bởi vì một đường đi như vậy sẽ có độ dài tối đa là $|V| - 1$ cạnh, và mỗi cạnh chỉ có thể làm giảm độ cao tối đa là một, điều này là không thể nếu độ cao đầu tiên là $h(s) = |V|$ và độ cao cuối cùng là $h(t) = 0$.

Sử dụng hàm gán nhãn này, chúng ta có thể nêu chiến lược của thuật toán push-relabel:
Chúng ta bắt đầu với một luồng tiền hợp lệ và một hàm gán nhãn hợp lệ.
Trong mỗi bước, chúng ta đẩy một số dư thừa giữa các đỉnh, và cập nhật nhãn của các đỉnh.
Chúng ta phải đảm bảo rằng, sau mỗi bước, luồng tiền và cách gán nhãn vẫn hợp lệ.
Nếu sau đó thuật toán xác định, luồng tiền là một luồng hợp lệ.
Và bởi vì chúng ta cũng có một cách gán nhãn hợp lệ, nên không tồn tại đường đi giữa $s$ và $t$ trong đồ thị dư, điều này có nghĩa là luồng thực sự là luồng cực đại.

Nếu chúng ta so sánh thuật toán Ford-Fulkerson với thuật toán push-relabel, có vẻ như các thuật toán là đối ngẫu của nhau.
Thuật toán Ford-Fulkerson giữ một luồng hợp lệ mọi lúc và cải thiện nó cho đến khi không còn tồn tại đường tăng luồng nào nữa, trong khi trong thuật toán push-relabel, không tồn tại đường tăng luồng nào vào bất kỳ lúc nào, và chúng ta sẽ cải thiện luồng tiền cho đến khi nó là một luồng hợp lệ.

## Thuật toán (Algorithm) {: #algorithm}

Đầu tiên chúng ta phải khởi tạo đồ thị với một luồng tiền hợp lệ và hàm gán nhãn hợp lệ.

Sử dụng luồng tiền rỗng - giống như được thực hiện trong thuật toán Ford-Fulkerson - là không thể, bởi vì sau đó sẽ có một đường tăng luồng và điều này ngụ ý rằng không tồn tại một cách gán nhãn hợp lệ.
Do đó, chúng ta sẽ khởi tạo mỗi cạnh đi ra từ $s$ với dung lượng tối đa của nó: $f((s, u)) = c((s, u))$.
Và tất cả các cạnh khác với không.
Trong trường hợp này tồn tại một cách gán nhãn hợp lệ, cụ thể là $h(s) = |V|$ cho đỉnh nguồn và $h(u) = 0$ cho tất cả các đỉnh khác.

Bây giờ hãy mô tả hai thao tác chi tiết hơn.

Với thao tác `push` (đẩy), chúng ta cố gắng đẩy càng nhiều luồng dư thừa từ một đỉnh $u$ sang một đỉnh lân cận $v$.
Chúng ta có một quy tắc: chúng ta chỉ được phép đẩy luồng từ $u$ sang $v$ nếu $h(u) = h(v) + 1$.
Theo thuật ngữ thông thường, luồng dư thừa phải chảy xuống dưới, nhưng không quá dốc.
Tất nhiên chúng ta chỉ có thể đẩy $\min(x(u), c((u, v)) - f((u, v)))$ luồng.

Nếu một đỉnh có dư thừa, nhưng không thể đẩy phần dư thừa sang bất kỳ đỉnh liền kề nào, thì chúng ta cần tăng độ cao của đỉnh này.
Chúng ta gọi thao tác này là `relabel` (gán lại nhãn).
Chúng ta sẽ tăng nó nhiều nhất có thể, trong khi vẫn duy trì tính hợp lệ của việc gán nhãn.

Tóm lại, thuật toán vắn tắt là:
Chúng ta khởi tạo một luồng tiền hợp lệ và một cách gán nhãn hợp lệ.
Trong khi chúng ta có thể thực hiện các thao tác push hoặc relabel, chúng ta thực hiện chúng.
Sau đó, luồng tiền thực sự là một luồng và chúng ta trả về nó.

## Độ phức tạp (Complexity) {: #complexity}

Dễ dàng chỉ ra rằng, nhãn cực đại của một đỉnh là $2|V| - 1$.
Tại thời điểm này, tất cả dư thừa còn lại có thể và sẽ được đẩy ngược lại nguồn.
Điều này mang lại tối đa $O(V^2)$ thao tác relabel.

Cũng có thể chỉ ra rằng, sẽ có tối đa $O(V E)$ lần đẩy bão hòa (một lần đẩy mà tổng dung lượng của cạnh được sử dụng) và tối đa $O(V^2 E)$ lần đẩy không bão hòa (một lần đẩy mà dung lượng của một cạnh không được sử dụng hết) được thực hiện.
Nếu chúng ta chọn một cấu trúc dữ liệu cho phép chúng ta tìm đỉnh tiếp theo có dư thừa trong thời gian $O(1)$, thì tổng độ phức tạp của thuật toán là $O(V^2 E)$.

## Cài đặt (Implementation) {: #implementation}

```cpp
const int inf = 1000000000;

int n;
vector<vector<int>> capacity, flow;
vector<int> height, excess, seen;
queue<int> excess_vertices;

void push(int u, int v) {
    int d = min(excess[u], capacity[u][v] - flow[u][v]);
    flow[u][v] += d;
    flow[v][u] -= d;
    excess[u] -= d;
    excess[v] += d;
    if (d && excess[v] == d)
        excess_vertices.push(v);
}

void relabel(int u) {
    int d = inf;
    for (int i = 0; i < n; i++) {
        if (capacity[u][i] - flow[u][i] > 0)
            d = min(d, height[i]);
    }
    if (d < inf)
        height[u] = d + 1;
}

void discharge(int u) {
    while (excess[u] > 0) {
        if (seen[u] < n) {
            int v = seen[u];
            if (capacity[u][v] - flow[u][v] > 0 && height[u] > height[v])
                push(u, v);
            else 
                seen[u]++;
        } else {
            relabel(u);
            seen[u] = 0;
        }
    }
}

int max_flow(int s, int t) {
    height.assign(n, 0);
    height[s] = n;
    flow.assign(n, vector<int>(n, 0));
    excess.assign(n, 0);
    excess[s] = inf;
    for (int i = 0; i < n; i++) {
    	if (i != s)
	        push(s, i);
    }
    seen.assign(n, 0);

    while (!excess_vertices.empty()) {
        int u = excess_vertices.front();
        excess_vertices.pop();
        if (u != s && u != t)
            discharge(u);
    }

    int max_flow = 0;
    for (int i = 0; i < n; i++)
        max_flow += flow[i][t];
    return max_flow;
}
```

Ở đây chúng ta sử dụng hàng đợi `excess_vertices` để lưu trữ tất cả các đỉnh hiện đang có dư thừa.
Theo cách đó, chúng ta có thể chọn đỉnh tiếp theo cho thao tác push hoặc relabel trong thời gian hằng số.

Và để đảm bảo rằng chúng ta không dành quá nhiều thời gian để tìm đỉnh liền kề mà chúng ta có thể đẩy tới, chúng ta sử dụng một cấu trúc dữ liệu được gọi là **cung hiện tại** (current-arc).
Về cơ bản, chúng ta sẽ lặp qua các cạnh theo thứ tự vòng tròn và luôn lưu trữ cạnh cuối cùng mà chúng ta đã sử dụng.
Theo cách này, đối với một giá trị nhãn nhất định, chúng ta sẽ chỉ chuyển đổi cạnh hiện tại $O(n)$ lần.
Và vì relabel đã mất thời gian $O(n)$, chúng ta không làm cho độ phức tạp tồi tệ hơn.
