---
tags:
  - Translated
e_maxx_link: ford_bellman
---

# Thuật toán Bellman-Ford

**Đường đi ngắn nhất từ một nguồn với các cạnh có trọng số âm**

Giả sử chúng ta được cho một đồ thị có hướng có trọng số $G$ với $n$ đỉnh và $m$ cạnh, và một đỉnh được chỉ định $v$. Bạn muốn tìm độ dài của các đường đi ngắn nhất từ đỉnh $v$ đến mọi đỉnh khác.

Không giống như thuật toán Dijkstra, thuật toán này cũng có thể được áp dụng cho các đồ thị chứa các cạnh có trọng số âm. Tuy nhiên, nếu đồ thị chứa một chu trình âm, thì rõ ràng, đường đi ngắn nhất đến một số đỉnh có thể không tồn tại (do thực tế là trọng số của đường đi ngắn nhất phải bằng âm vô cùng); tuy nhiên, thuật toán này có thể được sửa đổi để báo hiệu sự hiện diện của một chu trình có trọng số âm, hoặc thậm chí suy ra chu trình này.

Thuật toán mang tên của hai nhà khoa học người Mỹ: Richard Bellman và Lester Ford. Ford thực sự đã phát minh ra thuật toán này vào năm 1956 trong quá trình nghiên cứu một bài toán toán học khác, cuối cùng đã giảm xuống một bài toán con là tìm đường đi ngắn nhất trong đồ thị, và Ford đã đưa ra một phác thảo của thuật toán để giải quyết vấn đề này. Bellman vào năm 1958 đã xuất bản một bài báo dành riêng cho vấn đề tìm đường đi ngắn nhất, và trong bài báo này, ông đã trình bày rõ ràng thuật toán dưới dạng mà chúng ta biết đến ngày nay.

## Mô tả thuật toán

Giả sử rằng đồ thị không chứa chu trình trọng số âm. Trường hợp có chu trình trọng số âm sẽ được thảo luận dưới đây trong một phần riêng.

Chúng ta sẽ tạo một mảng khoảng cách $d[0 … n-1]$, sau khi thực hiện thuật toán sẽ chứa câu trả lời cho bài toán. Ban đầu, chúng ta điền nó như sau: $d[v] = 0$, và tất cả các phần tử khác $d[ ]$ bằng vô cùng $\infty$.

Thuật toán bao gồm nhiều giai đoạn. Mỗi giai đoạn quét qua tất cả các cạnh của đồ thị, và thuật toán cố gắng thực hiện **sự nới lỏng (relaxation)** dọc theo mỗi cạnh $(a,b)$ có trọng số $c$. Sự nới lỏng dọc theo các cạnh là một nỗ lực để cải thiện giá trị $d[b]$ bằng cách sử dụng giá trị $d[a] + c$. Thực tế, điều đó có nghĩa là chúng ta đang cố gắng cải thiện câu trả lời cho đỉnh này bằng cách sử dụng cạnh $(a,b)$ và câu trả lời hiện tại cho đỉnh $a$.

Người ta cho rằng $n-1$ giai đoạn của thuật toán là đủ để tính toán chính xác độ dài của tất cả các đường đi ngắn nhất trong đồ thị (một lần nữa, chúng ta tin rằng các chu trình có trọng số âm không tồn tại). Đối với các đỉnh không thể đến được, khoảng cách $d[ ]$ sẽ vẫn bằng vô cùng $\infty$.

## Cài đặt

Không giống như nhiều thuật toán đồ thị khác, đối với thuật toán Bellman-Ford, việc biểu diễn đồ thị bằng một danh sách duy nhất gồm tất cả các cạnh sẽ thuận tiện hơn (thay vì $n$ danh sách các cạnh - các cạnh từ mỗi đỉnh). Chúng tôi bắt đầu việc triển khai với một cấu trúc $\rm edge$ để biểu diễn các cạnh. Đầu vào của thuật toán là các số $n$, $m$, danh sách $e$ gồm các cạnh và đỉnh bắt đầu $v$. Tất cả các đỉnh được đánh số từ $0$ đến $n - 1$.

### Cài đặt đơn giản nhất

Hằng số $\rm INF$ biểu thị số "vô cùng" — nó phải được chọn sao cho lớn hơn tất cả các độ dài đường đi có thể có.

```cpp
struct Edge {
    int a, b, cost;
};

int n, m, v;
vector<Edge> edges;
const int INF = 1000000000;

void solve()
{
    vector<int> d(n, INF);
    d[v] = 0;
    for (int i = 0; i < n - 1; ++i)
        for (Edge e : edges)
            if (d[e.a] < INF)
                d[e.b] = min(d[e.b], d[e.a] + e.cost);
    // hiển thị d, ví dụ, trên màn hình
}
```

Việc kiểm tra `if (d[e.a] < INF)` chỉ cần thiết nếu đồ thị chứa các cạnh có trọng số âm: không có sự xác minh nào như vậy sẽ dẫn đến sự nới lỏng từ các đỉnh mà đường đi chưa được tìm thấy, và khoảng cách không chính xác, thuộc loại $\infty - 1$, $\infty - 2$ v.v. sẽ xuất hiện.

### Cài đặt tốt hơn

Thuật toán này có thể được tăng tốc một chút: thường thì chúng ta đã có câu trả lời sau một vài giai đoạn và không có công việc hữu ích nào được thực hiện trong các giai đoạn còn lại, chỉ lãng phí việc duyệt qua tất cả các cạnh. Vì vậy, hãy giữ một cờ, để biết liệu có gì thay đổi trong giai đoạn hiện tại hay không, và nếu bất kỳ giai đoạn nào, không có gì thay đổi, thuật toán có thể được dừng lại. (Tối ưu hóa này không cải thiện độ phức tạp tiệm cận, tức là, một số đồ thị vẫn sẽ cần tất cả $n-1$ giai đoạn, nhưng tăng tốc đáng kể hành vi của thuật toán "trung bình", tức là, trên các đồ thị ngẫu nhiên.)

Với tối ưu hóa này, nói chung không cần thiết phải giới hạn thủ công số lượng giai đoạn của thuật toán thành $n-1$ — thuật toán sẽ dừng lại sau số lượng giai đoạn mong muốn.

```cpp
void solve()
{
    vector<int> d(n, INF);
    d[v] = 0;
    for (;;)
    {
        bool any = false;

        for (Edge e : edges)
            if (d[e.a] < INF)
                if (d[e.b] > d[e.a] + e.cost) {
                    d[e.b] = d[e.a] + e.cost;
                    any = true;
                }

        if (!any)
            break;
    }
    // hiển thị d, ví dụ, trên màn hình
}
```

### Truy xuất đường đi

Bây giờ chúng ta hãy xem xét làm thế nào để sửa đổi thuật toán để nó không chỉ tìm thấy độ dài của các đường đi ngắn nhất, mà còn cho phép tái tạo lại các đường đi ngắn nhất.

Để làm điều đó, hãy tạo một mảng khác $p[0 … n-1]$, trong đó với mỗi đỉnh, chúng ta lưu trữ "đỉnh tiền nhiệm" của nó, tức là đỉnh áp chót trong đường đi ngắn nhất dẫn đến nó. Thực tế, đường đi ngắn nhất đến bất kỳ đỉnh $a$ nào là một đường đi ngắn nhất đến một đỉnh $p[a]$, mà chúng ta đã thêm $a$ vào cuối đường đi.

Lưu ý rằng thuật toán hoạt động theo cùng một logic: nó giả định rằng khoảng cách ngắn nhất đến một đỉnh đã được tính toán, và, cố gắng cải thiện khoảng cách ngắn nhất đến các đỉnh khác từ đỉnh đó. Do đó, tại thời điểm cải thiện, chúng ta chỉ cần nhớ $p[ ]$, tức là, đỉnh mà từ đó sự cải thiện này đã xảy ra.

Sau đây là một triển khai của Bellman-Ford với việc truy xuất đường đi ngắn nhất đến một nút $t$ đã cho:

```cpp
void solve()
{
    vector<int> d(n, INF);
    d[v] = 0;
    vector<int> p(n, -1);

    for (;;)
    {
        bool any = false;
        for (Edge e : edges)
            if (d[e.a] < INF)
                if (d[e.b] > d[e.a] + e.cost) {
                    d[e.b] = d[e.a] + e.cost;
                    p[e.b] = e.a;
                    any = true;
                }
        if (!any)
            break;
    }

    if (d[t] == INF)
        cout << "No path from " << v << " to " << t << ".";
    else {
        vector<int> path;
        for (int cur = t; cur != -1; cur = p[cur])
            path.push_back(cur);
        reverse(path.begin(), path.end());

        cout << "Path from " << v << " to " << t << ": ";
        for (int u : path)
            cout << u << ' ';
    }
}
```

Ở đây bắt đầu từ đỉnh $t$, chúng ta đi qua các đỉnh tiền nhiệm cho đến khi chúng ta đến đỉnh bắt đầu không có đỉnh tiền nhiệm, và lưu trữ tất cả các đỉnh trong đường đi trong danh sách $\rm path$. Danh sách này là một đường đi ngắn nhất từ $v$ đến $t$, nhưng theo thứ tự ngược lại, vì vậy chúng ta gọi hàm $\rm reverse()$ trên $\rm path$ và sau đó xuất đường đi.

## Chứng minh thuật toán

Đầu tiên, lưu ý rằng đối với tất cả các đỉnh không thể đến được $u$, thuật toán sẽ hoạt động chính xác, nhãn $d[u]$ sẽ vẫn bằng vô cùng (vì thuật toán Bellman-Ford sẽ tìm một số đường đến tất cả các đỉnh có thể đến được từ đỉnh bắt đầu $v$, và sự nới lỏng cho tất cả các đỉnh còn lại khác sẽ không bao giờ xảy ra).

Bây giờ chúng ta hãy chứng minh khẳng định sau: Sau khi thực hiện giai đoạn thứ $i$, thuật toán Bellman-Ford tìm thấy chính xác tất cả các đường đi ngắn nhất có số cạnh không vượt quá $i$.

Nói cách khác, đối với bất kỳ đỉnh $a$ nào, hãy ký hiệu $k$ là số cạnh trong đường đi ngắn nhất đến nó (nếu có nhiều đường đi như vậy, bạn có thể lấy bất kỳ đường nào). Theo khẳng định này, thuật toán đảm bảo rằng sau giai đoạn thứ $k$, đường đi ngắn nhất cho đỉnh $a$ sẽ được tìm thấy.

**Chứng minh**:
Xét một đỉnh $a$ tùy ý mà có đường đi từ đỉnh bắt đầu $v$, và xét một đường đi ngắn nhất đến nó $(p_0=v, p_1, …, p_k=a)$. Trước giai đoạn đầu tiên, đường đi ngắn nhất đến đỉnh $p_0 = v$ đã được tìm thấy một cách chính xác. Trong giai đoạn đầu tiên, cạnh $(p_0,p_1)$ đã được thuật toán kiểm tra, và do đó, khoảng cách đến đỉnh $p_1$ đã được tính toán chính xác sau giai đoạn đầu tiên. Lặp lại khẳng định này $k$ lần, chúng ta thấy rằng sau giai đoạn thứ $k$, khoảng cách đến đỉnh $p_k = a$ được tính toán chính xác, điều mà chúng ta muốn chứng minh.

Điều cuối cùng cần chú ý là bất kỳ đường đi ngắn nhất nào cũng không thể có nhiều hơn $n - 1$ cạnh. Do đó, thuật toán đủ để đi đến giai đoạn thứ $(n-1)$. Sau đó, được đảm bảo rằng không có sự nới lỏng nào sẽ cải thiện khoảng cách đến một số đỉnh.

## Trường hợp chu trình âm

Ở khắp mọi nơi ở trên, chúng ta đã xem xét rằng không có chu trình âm trong đồ thị (chính xác, chúng ta quan tâm đến một chu trình âm có thể đến được từ đỉnh bắt đầu $v$, và, đối với một chu trình không thể đến được, không có gì trong thuật toán trên thay đổi). Khi có (các) chu trình âm, có những phức tạp hơn liên quan đến thực tế là khoảng cách đến tất cả các đỉnh trong chu trình này, cũng như khoảng cách đến các đỉnh có thể đến được từ chu trình này không được xác định — chúng phải bằng âm vô cùng $(- \infty)$.

Dễ thấy rằng thuật toán Bellman-Ford có thể thực hiện sự nới lỏng vô tận giữa tất cả các đỉnh của chu trình này và các đỉnh có thể đến được từ nó. Do đó, nếu bạn không giới hạn số lượng giai đoạn thành $n - 1$, thuật toán sẽ chạy vô thời hạn, liên tục cải thiện khoảng cách từ các đỉnh này.

Do đó, chúng ta có được **tiêu chí cho sự hiện diện của một chu trình có trọng số âm có thể đến được từ đỉnh nguồn $v$**: sau giai đoạn thứ $(n-1)$, nếu chúng ta chạy thuật toán thêm một giai đoạn nữa, và nó thực hiện ít nhất một sự nới lỏng nữa, thì đồ thị chứa một chu trình trọng số âm có thể đến được từ $v$; ngược lại, một chu trình như vậy không tồn tại.

Hơn nữa, nếu một chu trình như vậy được tìm thấy, thuật toán Bellman-Ford có thể được sửa đổi để nó truy xuất chu trình này dưới dạng một chuỗi các đỉnh chứa trong nó. Để làm điều này, đủ để nhớ đỉnh cuối cùng $x$ mà đã có một sự nới lỏng trong giai đoạn thứ $n$. Đỉnh này sẽ nằm trên một chu trình trọng số âm, hoặc có thể đến được từ nó. Để có được các đỉnh được đảm bảo nằm trên một chu trình âm, bắt đầu từ đỉnh $x$, đi qua các đỉnh tiền nhiệm $n$ lần. Bằng cách này, chúng ta sẽ đến được đỉnh $y$, được đảm bảo nằm trên một chu trình âm. Chúng ta phải đi từ đỉnh này, qua các đỉnh tiền nhiệm, cho đến khi chúng ta trở lại cùng một đỉnh $y$ (và điều đó sẽ xảy ra, vì sự nới lỏng trong một chu trình trọng số âm xảy ra theo một cách tuần hoàn).

### Cài đặt:

```cpp
void solve()
{
    vector<int> d(n, INF);
    d[v] = 0;
    vector<int> p(n, -1);
    int x;
    for (int i = 0; i < n; ++i) {
        x = -1;
        for (Edge e : edges)
            if (d[e.a] < INF)
                if (d[e.b] > d[e.a] + e.cost) {
                    d[e.b] = max(-INF, d[e.a] + e.cost);
                    p[e.b] = e.a;
                    x = e.b;
                }
    }

    if (x == -1)
        cout << "No negative cycle from " << v;
    else {
        int y = x;
        for (int i = 0; i < n; ++i)
            y = p[y];

        vector<int> path;
        for (int cur = y;; cur = p[cur]) {
            path.push_back(cur);
            if (cur == y && path.size() > 1)
                break;
        }
        reverse(path.begin(), path.end());

        cout << "Negative cycle: ";
        for (int u : path)
            cout << u << ' ';
    }
}
```

Do sự hiện diện của một chu trình âm, trong $n$ lần lặp của thuật toán, khoảng cách có thể đi vào vùng âm rất xa (đến các số âm có bậc là $-n m W$, trong đó $W$ là giá trị tuyệt đối lớn nhất của bất kỳ trọng số nào trong đồ thị). Do đó, trong mã, chúng tôi đã áp dụng các biện pháp bổ sung chống tràn số nguyên như sau:

```cpp
d[e.b] = max(-INF, d[e.a] + e.cost);
```

Việc triển khai ở trên tìm kiếm một chu trình âm có thể đến được từ một đỉnh bắt đầu nào đó $v$; tuy nhiên, thuật toán có thể được sửa đổi để chỉ tìm kiếm bất kỳ chu trình âm nào trong đồ thị. Để làm điều này, chúng ta cần đặt tất cả các khoảng cách $d[i]$ về không chứ không phải vô cùng — như thể chúng ta đang tìm kiếm đường đi ngắn nhất từ tất cả các đỉnh đồng thời; tính hợp lệ của việc phát hiện một chu trình âm không bị ảnh hưởng.

Để biết thêm về chủ đề này — hãy xem bài viết riêng, [Tìm một chu trình âm trong đồ thị](finding-negative-cycle-in-graph.md).

## Thuật toán Shortest Path Faster (SPFA)

SPFA là một cải tiến của thuật toán Bellman-Ford, tận dụng thực tế là không phải tất cả các nỗ lực nới lỏng đều sẽ thành công.
Ý tưởng chính là tạo một hàng đợi chỉ chứa các đỉnh đã được nới lỏng nhưng vẫn có thể nới lỏng thêm các đỉnh kề của chúng.
Và bất cứ khi nào bạn có thể nới lỏng một đỉnh kề nào đó, bạn nên đưa nó vào hàng đợi. Thuật toán này cũng có thể được sử dụng để phát hiện các chu trình âm như Bellman-Ford.

Trường hợp xấu nhất của thuật toán này bằng với $O(n m)$ của Bellman-Ford, nhưng trong thực tế, nó hoạt động nhanh hơn nhiều và một số [người cho rằng nó thậm chí hoạt động trong $O(m)$ trung bình](https://en.wikipedia.org/wiki/Shortest_Path_Faster_Algorithm#Average-case_performance). Tuy nhiên, hãy cẩn thận, vì thuật toán này là tất định và dễ dàng tạo ra các trường hợp phản ví dụ làm cho thuật toán chạy trong $O(n m)$.

Có một số điều cần lưu ý trong việc triển khai, chẳng hạn như thực tế là thuật toán sẽ tiếp tục mãi mãi nếu có một chu trình âm.
Để tránh điều này, có thể tạo một bộ đếm lưu trữ số lần một đỉnh đã được nới lỏng và dừng thuật toán ngay khi một đỉnh nào đó được nới lỏng lần thứ $n$.
Lưu ý, cũng không có lý do gì để đưa một đỉnh vào hàng đợi nếu nó đã có trong đó.

```cpp
const int INF = 1000000000;
vector<vector<pair<int, int>>> adj;

bool spfa(int s, vector<int>& d) {
    int n = adj.size();
    d.assign(n, INF);
    vector<int> cnt(n, 0);
    vector<bool> inqueue(n, false);
    queue<int> q;

    d[s] = 0;
    q.push(s);
    inqueue[s] = true;
    while (!q.empty()) {
        int v = q.front();
        q.pop();
        inqueue[v] = false;

        for (auto edge : adj[v]) {
            int to = edge.first;
            int len = edge.second;

            if (d[v] + len < d[to]) {
                d[to] = d[v] + len;
                if (!inqueue[to]) {
                    q.push(to);
                    inqueue[to] = true;
                    cnt[to]++;
                    if (cnt[to] > n)
                        return false;  // chu trình âm
                }
            }
        }
    }
    return true;
}
```


## Các bài toán liên quan trong các kỳ thi trực tuyến

Danh sách các bài toán có thể được giải bằng thuật toán Bellman-Ford:

* [E-OLYMP #1453 "Ford-Bellman" [độ khó: thấp]](https://www.e-olymp.com/en/problems/1453)
* [UVA #423 "MPI Maelstrom" [độ khó: thấp]](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=364)
* [UVA #534 "Frogger" [độ khó: trung bình]](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=7&page=show_problem&problem=475)
* [UVA #10099 "The Tourist Guide" [độ khó: trung bình]](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=12&page=show_problem&problem=1040)
* [UVA #515 "King" [độ khó: trung bình]](http://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=456)
* [UVA 12519 - The Farnsworth Parabox](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3964)

Xem thêm danh sách bài toán trong bài viết [Tìm chu trình âm trong đồ thị](finding-negative-cycle-in-graph.md).
* [CSES - High Score](https://cses.fi/problemset/task/1673)
* [CSES - Cycle Finding](https://cses.fi/problemset/task/1197)