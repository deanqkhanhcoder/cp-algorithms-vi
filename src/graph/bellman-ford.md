---
tags:
  - Translated
e_maxx_link: ford_bellman
---

# Thuật toán Bellman-Ford (Bellman-Ford Algorithm) {: #bellman-ford-algorithm}

**Đường đi ngắn nhất từ một nguồn đơn với các cạnh có trọng số âm**

Giả sử rằng chúng ta được cho một đồ thị có hướng có trọng số $G$ với $n$ đỉnh và $m$ cạnh, và một đỉnh $v$ được chỉ định. Bạn muốn tìm độ dài của các đường đi ngắn nhất từ đỉnh $v$ đến mọi đỉnh khác.

Không giống như thuật toán Dijkstra, thuật toán này cũng có thể được áp dụng cho các đồ thị chứa các cạnh có trọng số âm. Tuy nhiên, nếu đồ thị chứa một chu trình âm, thì rõ ràng, đường đi ngắn nhất đến một số đỉnh có thể không tồn tại (do thực tế là trọng số của đường đi ngắn nhất phải bằng âm vô cùng); tuy nhiên, thuật toán này có thể được sửa đổi để báo hiệu sự hiện diện của một chu trình có trọng số âm, hoặc thậm chí suy ra chu trình này.

Thuật toán mang tên của hai nhà khoa học người Mỹ: Richard Bellman và Lester Ford. Ford thực sự đã phát minh ra thuật toán này vào năm 1956 trong quá trình nghiên cứu một bài toán toán học khác, cuối cùng quy về một bài toán con của việc tìm đường đi ngắn nhất trong đồ thị, và Ford đã đưa ra một phác thảo của thuật toán để giải quyết vấn đề này. Bellman vào năm 1958 đã xuất bản một bài báo dành riêng cho bài toán tìm đường đi ngắn nhất, và trong bài báo này, ông đã trình bày rõ ràng thuật toán dưới dạng mà nó được biết đến với chúng ta hiện nay.

## Mô tả thuật toán (Description of the algorithm) {: #description-of-the-algorithm}

Hãy giả sử rằng đồ thị không chứa chu trình trọng số âm. Trường hợp có sự hiện diện của chu trình trọng số âm sẽ được thảo luận bên dưới trong một phần riêng biệt.

Chúng ta sẽ tạo một mảng khoảng cách $d[0 \ldots n-1]$, sau khi thực hiện thuật toán sẽ chứa câu trả lời cho bài toán. Ban đầu, chúng ta điền nó như sau: $d[v] = 0$, và tất cả các phần tử $d[ ]$ khác bằng vô cùng $\infty$.

Thuật toán bao gồm nhiều pha. Mỗi pha quét qua tất cả các cạnh của đồ thị, và thuật toán cố gắng thực hiện **nới lỏng** (relaxation) dọc theo mỗi cạnh $(a,b)$ có trọng số $c$. Nới lỏng dọc theo các cạnh là một nỗ lực để cải thiện giá trị $d[b]$ bằng cách sử dụng giá trị $d[a] + c$. Trên thực tế, điều đó có nghĩa là chúng ta đang cố gắng cải thiện câu trả lời cho đỉnh này bằng cách sử dụng cạnh $(a,b)$ và câu trả lời hiện tại cho đỉnh $a$.

Người ta khẳng định rằng $n-1$ pha của thuật toán là đủ để tính toán chính xác độ dài của tất cả các đường đi ngắn nhất trong đồ thị (một lần nữa, chúng tôi tin rằng các chu trình trọng số âm không tồn tại). Đối với các đỉnh không thể tiếp cận, khoảng cách $d[ ]$ sẽ vẫn bằng vô cùng $\infty$.

## Cài đặt (Implementation) {: #implementation}

Không giống như nhiều thuật toán đồ thị khác, đối với thuật toán Bellman-Ford, thuận tiện hơn khi biểu diễn đồ thị bằng cách sử dụng một danh sách duy nhất của tất cả các cạnh (thay vì $n$ danh sách các cạnh - các cạnh từ mỗi đỉnh). Chúng ta bắt đầu việc cài đặt với một cấu trúc $\rm edge$ để biểu diễn các cạnh. Đầu vào cho thuật toán là các số $n$, $m$, danh sách $e$ các cạnh và đỉnh bắt đầu $v$. Tất cả các đỉnh được đánh số từ $0$ đến $n - 1$.

### Cài đặt đơn giản nhất

Hằng số $\rm INF$ biểu thị số "vô cùng" — nó nên được chọn sao cho nó lớn hơn tất cả các độ dài đường đi có thể.

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

Việc kiểm tra `if (d[e.a] < INF)` chỉ cần thiết nếu đồ thị chứa các cạnh trọng số âm: nếu không có xác minh như vậy sẽ dẫn đến việc nới lỏng từ các đỉnh mà đường đi chưa được tìm thấy, và khoảng cách không chính xác, kiểu như $\infty - 1$, $\infty - 2$ v.v. sẽ xuất hiện.

### Một cài đặt tốt hơn

Thuật toán này có thể được tăng tốc phần nào: thường thì chúng ta đã nhận được câu trả lời trong một vài pha và không có công việc hữu ích nào được thực hiện trong các pha còn lại, chỉ lãng phí khi ghé thăm tất cả các cạnh.
Vì vậy, hãy giữ cờ, để cho biết liệu có gì thay đổi trong pha hiện tại hay không, và nếu bất kỳ pha nào, không có gì thay đổi, thuật toán có thể dừng lại. (Tối ưu hóa này không cải thiện hành vi tiệm cận, tức là, một số đồ thị vẫn sẽ cần tất cả $n-1$ pha, nhưng tăng tốc đáng kể hành vi của thuật toán "trên trung bình", tức là, trên các đồ thị ngẫu nhiên.)

Với tối ưu hóa này, thường không cần thiết phải giới hạn thủ công số lượng các pha của thuật toán thành $n-1$ — thuật toán sẽ dừng lại sau số lượng pha mong muốn.

```cpp
void solve()
{
    vector<int> d(n, INF);
    d[v] = 0;
    for (;;) {
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

### Khôi phục đường đi (Retrieving Path) {: #retrieving-path}

Bây giờ hãy xem xét cách sửa đổi thuật toán để nó không chỉ tìm độ dài của các đường đi ngắn nhất, mà còn cho phép khôi phục lại các đường đi ngắn nhất.

Để làm điều đó, hãy tạo một mảng khác $p[0 \ldots n-1]$, trong đó đối với mỗi đỉnh chúng ta lưu trữ "tiền bối" (predecessor) của nó, tức là đỉnh áp chót trong đường đi ngắn nhất dẫn đến nó. Trên thực tế, đường đi ngắn nhất đến bất kỳ đỉnh $a$ nào là đường đi ngắn nhất đến một đỉnh $p[a]$ nào đó, mà chúng ta đã thêm $a$ vào cuối đường đi.

Lưu ý rằng thuật toán hoạt động trên cùng một logic: nó giả định rằng khoảng cách ngắn nhất đến một đỉnh đã được tính toán, và cố gắng cải thiện khoảng cách ngắn nhất đến các đỉnh khác từ đỉnh đó. Do đó, tại thời điểm cải thiện, chúng ta chỉ cần nhớ $p[ ]$, tức là, đỉnh mà từ đó sự cải thiện này đã xảy ra.

Sau đây là một cài đặt của Bellman-Ford với việc truy xuất đường đi ngắn nhất đến một nút $t$ nhất định:

```cpp
void solve()
{
    vector<int> d(n, INF);
    d[v] = 0;
    vector<int> p(n, -1);

    for (;;) {
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

Ở đây bắt đầu từ đỉnh $t$, chúng ta đi qua các tiền bối cho đến khi chúng ta đến đỉnh bắt đầu không có tiền bối, và lưu trữ tất cả các đỉnh trong đường đi trong danh sách $\rm path$. Danh sách này là một đường đi ngắn nhất từ $v$ đến $t$, nhưng theo thứ tự ngược lại, vì vậy chúng ta gọi hàm $\rm reverse()$ trên $\rm path$ và sau đó xuất ra đường đi.

## Chứng minh thuật toán (The proof of the algorithm) {: #the-proof-of-the-algorithm}

Đầu tiên, lưu ý rằng đối với tất cả các đỉnh không thể tiếp cận $u$, thuật toán sẽ hoạt động chính xác, nhãn $d[u]$ sẽ vẫn bằng vô cùng (bởi vì thuật toán Bellman-Ford sẽ tìm một số cách đến tất cả các đỉnh có thể truy cập từ đỉnh bắt đầu $v$, và việc nới lỏng cho tất cả các đỉnh còn lại khác sẽ không bao giờ xảy ra).

Bây giờ chúng ta hãy chứng minh khẳng định sau: Sau khi thực hiện pha thứ $i$, thuật toán Bellman-Ford tìm chính xác tất cả các đường đi ngắn nhất có số lượng cạnh không vượt quá $i$.

Nói cách khác, đối với bất kỳ đỉnh $a$ nào, hãy gọi $k$ là số cạnh trong đường đi ngắn nhất đến nó (nếu có một số đường đi như vậy, bạn có thể lấy bất kỳ đường đi nào). Theo phát biểu này, thuật toán đảm bảo rằng sau pha thứ $k$, đường đi ngắn nhất cho đỉnh $a$ sẽ được tìm thấy.

**Chứng minh**:
Xem xét một đỉnh $a$ tùy ý có đường đi từ đỉnh bắt đầu $v$, và xem xét một đường đi ngắn nhất đến nó $(p_0=v, p_1, \ldots, p_k=a)$. Trước pha đầu tiên, đường đi ngắn nhất đến đỉnh $p_0 = v$ đã được tìm thấy chính xác. Trong pha đầu tiên, cạnh $(p_0,p_1)$ đã được thuật toán kiểm tra, và do đó, khoảng cách đến đỉnh $p_1$ đã được tính toán chính xác sau pha đầu tiên. Lặp lại phát biểu này $k$ lần, chúng ta thấy rằng sau pha thứ $k$, khoảng cách đến đỉnh $p_k = a$ được tính toán chính xác, đó là điều chúng ta muốn chứng minh.

Điều cuối cùng cần lưu ý là bất kỳ đường đi ngắn nhất nào cũng không thể có nhiều hơn $n - 1$ cạnh. Do đó, thuật toán về cơ bản đi đến pha thứ $(n-1)$. Sau đó, đảm bảo rằng không có sự nới lỏng nào sẽ cải thiện khoảng cách đến một số đỉnh.

## Trường hợp chu trình âm (The case of a negative cycle) {: #the-case-of-a-negative-cycle}

Ở mọi nơi trên chúng ta đã xem xét rằng không có chu trình âm nào trong đồ thị (chính xác là, chúng ta quan tâm đến một chu trình âm có thể tiếp cận từ đỉnh bắt đầu $v$, và, đối với các chu trình không thể tiếp cận, không có gì trong thuật toán trên thay đổi). Khi có (các) chu trình âm, có thêm các biến chứng liên quan đến thực tế là khoảng cách đến tất cả các đỉnh trong chu trình này, cũng như khoảng cách đến các đỉnh có thể truy cập từ chu trình này không được xác định — chúng phải bằng âm vô cùng $(- \infty)$.

Dễ thấy rằng thuật toán Bellman-Ford có thể thực hiện nới lỏng vô tận giữa tất cả các đỉnh của chu trình này và các đỉnh có thể truy cập từ nó. Do đó, nếu bạn không giới hạn số lượng pha thành $n - 1$, thuật toán sẽ chạy vô thời hạn, liên tục cải thiện khoảng cách từ các đỉnh này (giảm xuống âm vô cùng).

Do đó chúng ta thu được **tiêu chí cho sự hiện diện của một chu trình trọng số âm có thể tiếp cận từ đỉnh nguồn $v$**: sau pha thứ $(n-1)$, nếu chúng ta chạy thuật toán thêm một pha nữa, và nó thực hiện ít nhất một lần nới lỏng nữa, thì đồ thị chứa một chu trình trọng số âm có thể tiếp cận từ $v$; ngược lại, một chu trình như vậy không tồn tại.

Hơn nữa, nếu một chu trình như vậy được tìm thấy, thuật toán Bellman-Ford có thể được sửa đổi để nó truy xuất chu trình này như một chuỗi các đỉnh chứa trong nó. Để làm điều này, chỉ cần nhớ đỉnh cuối cùng $x$ mà tại đó có sự nới lỏng trong pha thứ $n$. Đỉnh này sẽ nằm trên một chu trình trọng số âm, hoặc có thể tiếp cận từ nó. Để có được các đỉnh được đảm bảo nằm trên một chu trình âm, bắt đầu từ đỉnh $x$, đi qua các tiền bối $n$ lần. Bằng cách này, chúng ta sẽ đến đỉnh $y$, được đảm bảo nằm trên một chu trình âm. Chúng ta phải đi từ đỉnh này, qua các tiền bối, cho đến khi chúng ta quay trở lại cùng một đỉnh $y$ (và nó sẽ xảy ra, bởi vì sự nới lỏng trong một chu trình trọng số âm xảy ra theo cách tròn).

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

Do sự hiện diện của một chu trình âm, đối với $n$ lần lặp của thuật toán, khoảng cách có thể đi xa vào phạm vi âm (đến các số âm theo bậc $-n m W$, trong đó $W$ là giá trị tuyệt đối tối đa của bất kỳ trọng số nào trong đồ thị). Do đó trong mã, chúng ta đã áp dụng các biện pháp bổ sung chống tràn số nguyên như sau:

```cpp
d[e.b] = max(-INF, d[e.a] + e.cost);
```

Cài đặt trên tìm kiếm một chu trình âm có thể tiếp cận từ một số đỉnh bắt đầu $v$; tuy nhiên, thuật toán có thể được sửa đổi để chỉ tìm kiếm bất kỳ chu trình âm nào trong đồ thị.
Để làm điều này, chúng ta cần đặt tất cả khoảng cách $d[i]$ thành 0 và không phải vô cùng — như thể chúng ta đang tìm kiếm đường đi ngắn nhất từ tất cả các đỉnh cùng một lúc; tính hợp lệ của việc phát hiện chu trình âm không bị ảnh hưởng.

Để biết thêm về chủ đề này — xem bài viết riêng, [Tìm chu trình âm trong đồ thị](finding-negative-cycle-in-graph.md).

## Thuật toán Shortest Path Faster (SPFA) {: #shortest-path-faster-algorithm-spfa}

SPFA là một cải tiến của thuật toán Bellman-Ford tận dụng thực tế là không phải tất cả các nỗ lực nới lỏng sẽ hoạt động.
Ý tưởng chính là tạo ra một hàng đợi chỉ chứa các đỉnh đã được nới lỏng nhưng vẫn có thể nới lỏng thêm các hàng xóm của chúng.
Và bất cứ khi nào bạn có thể nới lỏng một số hàng xóm, bạn nên đưa anh ta vào hàng đợi. Thuật toán này cũng có thể được sử dụng để phát hiện chu trình âm như Bellman-Ford.

Trường hợp xấu nhất của thuật toán này bằng với $O(n m)$ của Bellman-Ford, nhưng trong thực tế nó hoạt động nhanh hơn nhiều và một số [người khẳng định rằng nó hoạt động ngay cả trong $O(m)$ trên trung bình](https://en.wikipedia.org/wiki/Shortest_Path_Faster_Algorithm#Average-case_performance). Tuy nhiên hãy cẩn thận, bởi vì thuật toán này là xác định và rất dễ tạo ra các ví dụ phản chứng làm cho thuật toán chạy trong $O(n m)$.

Cần lưu ý một số điều trong cài đặt, chẳng hạn như thực tế là thuật toán tiếp tục mãi mãi nếu có một chu trình âm.
Để tránh điều này, có thể tạo một bộ đếm lưu trữ số lần một đỉnh đã được nới lỏng và dừng thuật toán ngay khi một số đỉnh được nới lỏng lần thứ $n$.
Lưu ý, cũng không có lý do gì để đưa một đỉnh vào hàng đợi nếu nó đã ở trong đó.
```cpp title="spfa"
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
                        return false;  // negative cycle
                }
            }
        }
    }
    return true;
}
```


## Các bài toán liên quan (Related problems in online judges) {: #related-problems-in-online-judges}

Danh sách các bài tập có thể được giải quyết bằng thuật toán Bellman-Ford:

* [E-OLYMP #1453 "Ford-Bellman" [difficulty: low]](https://www.e-olymp.com/en/problems/1453)
* [UVA #423 "MPI Maelstrom" [difficulty: low]](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=364)
* [UVA #534 "Frogger" [difficulty: medium]](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=7&page=show_problem&problem=475)
* [UVA #10099 "The Tourist Guide" [difficulty: medium]](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=12&page=show_problem&problem=1040)
* [UVA #515 "King" [difficulty: medium]](http://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=456)
* [UVA 12519 - The Farnsworth Parabox](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3964)

Xem thêm danh sách bài tập trong bài viết [Tìm chu trình âm trong đồ thị](finding-negative-cycle-in-graph.md).
* [CSES - High Score](https://cses.fi/problemset/task/1673)
* [CSES - Cycle Finding](https://cses.fi/problemset/task/1197)
