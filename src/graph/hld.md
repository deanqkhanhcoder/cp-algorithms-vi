---
tags:
  - Translated
e_maxx_link: heavy_light
---

# Phân rã nặng-nhẹ (Heavy-light decomposition)

**Phân rã nặng-nhẹ** là một kỹ thuật khá tổng quát cho phép chúng ta giải quyết hiệu quả nhiều bài toán quy về **truy vấn trên một cây** .


## Mô tả

Cho một cây $G$ có $n$ đỉnh, với một gốc tùy ý.

Bản chất của việc phân rã cây này là **chia cây thành nhiều đường đi** sao cho chúng ta có thể đến đỉnh gốc từ bất kỳ đỉnh $v$ nào bằng cách duyệt qua nhiều nhất $\log n$ đường đi. Ngoài ra, không có đường đi nào trong số này nên giao nhau với đường đi khác.

Rõ ràng là nếu chúng ta tìm thấy một sự phân rã như vậy cho bất kỳ cây nào, nó sẽ cho phép chúng ta quy các truy vấn đơn lẻ có dạng *“tính toán một cái gì đó trên đường đi từ $a$ đến $b$”* về một số truy vấn có dạng *”tính toán một cái gì đó trên đoạn $[l, r]$ của đường đi thứ $k$”* .


### Thuật toán xây dựng

Chúng ta tính toán cho mỗi đỉnh $v$ kích thước của cây con của nó $s(v)$, tức là số lượng đỉnh trong cây con của đỉnh $v$ bao gồm cả chính nó.

Tiếp theo, xem xét tất cả các cạnh dẫn đến các con của một đỉnh $v$. Chúng ta gọi một cạnh là **nặng** nếu nó dẫn đến một đỉnh $c$ sao cho:

$$
s(c) \ge \frac{s(v)}{2} \iff \text{cạnh }(v, c)\text{ là nặng}
$$

Tất cả các cạnh khác được gán nhãn là **nhẹ**.

Rõ ràng là nhiều nhất một cạnh nặng có thể xuất phát từ một đỉnh đi xuống, bởi vì nếu không thì đỉnh $v$ sẽ có ít nhất hai con có kích thước $\ge \frac{s(v)}{2}$, và do đó kích thước của cây con của $v$ sẽ quá lớn, $s(v) \ge 1 + 2 \frac{s(v)}{2} > s(v)$, điều này dẫn đến một mâu thuẫn.

Bây giờ chúng ta sẽ phân rã cây thành các đường đi không giao nhau. Xem xét tất cả các đỉnh mà từ đó không có cạnh nặng nào đi xuống. Chúng ta sẽ đi lên từ mỗi đỉnh như vậy cho đến khi chúng ta đến gốc của cây hoặc đi qua một cạnh nhẹ. Kết quả là, chúng ta sẽ nhận được một số đường đi được tạo thành từ không hoặc nhiều cạnh nặng cộng với một cạnh nhẹ. Đường đi có một đầu ở gốc là một ngoại lệ cho điều này và sẽ không có một cạnh nhẹ. Hãy gọi những đường đi này là **đường đi nặng** - đây là những đường đi mong muốn của phân rã nặng-nhẹ.


### Chứng minh tính đúng đắn

Đầu tiên, chúng ta lưu ý rằng các đường đi nặng thu được bằng thuật toán sẽ **không giao nhau**. Thực tế, nếu hai đường đi như vậy có một cạnh chung, điều đó sẽ ngụ ý rằng có hai cạnh nặng đi ra từ một đỉnh, điều này là không thể.

Thứ hai, chúng ta sẽ chỉ ra rằng đi xuống từ gốc của cây đến một đỉnh tùy ý, chúng ta sẽ **thay đổi không quá $\log n$ đường đi nặng trên đường đi** . Đi xuống một cạnh nhẹ làm giảm kích thước của cây con hiện tại xuống một nửa hoặc thấp hơn:

$$s(c) < \frac{s(v)}{2} \iff \text{cạnh }(v, c)\text{ là nhẹ}
$$


Do đó, chúng ta có thể đi qua nhiều nhất $\log n$ cạnh nhẹ trước khi kích thước cây con giảm xuống một.

Vì chúng ta chỉ có thể di chuyển từ một đường đi nặng sang một đường đi nặng khác thông qua một cạnh nhẹ (mỗi đường đi nặng, ngoại trừ đường bắt đầu ở gốc, có một cạnh nhẹ), chúng ta không thể thay đổi đường đi nặng nhiều hơn $\log n$ lần trên đường đi từ gốc đến bất kỳ đỉnh nào, như yêu cầu.


Hình ảnh sau đây minh họa sự phân rã của một cây mẫu. Các cạnh nặng dày hơn các cạnh nhẹ. Các đường đi nặng được đánh dấu bằng các đường viền chấm.

<div style="text-align: center;">
  <img src="hld.png" alt="Hình ảnh của HLD">
</div>


## Các bài toán mẫu

Khi giải quyết các bài toán, đôi khi sẽ thuận tiện hơn khi xem xét phân rã nặng-nhẹ như một tập hợp các đường đi **không giao nhau về đỉnh** (thay vì các đường đi không giao nhau về cạnh). Để làm điều này, chỉ cần loại trừ cạnh cuối cùng khỏi mỗi đường đi nặng nếu đó là một cạnh nhẹ, thì không có thuộc tính nào bị vi phạm, nhưng bây giờ mỗi đỉnh thuộc về đúng một đường đi nặng.

Dưới đây chúng ta sẽ xem xét một số nhiệm vụ điển hình có thể được giải quyết với sự trợ giúp của phân rã nặng-nhẹ.

Riêng biệt, đáng chú ý đến bài toán **tổng các số trên đường đi**, vì đây là một ví dụ về một bài toán có thể được giải quyết bằng các kỹ thuật đơn giản hơn.


### Giá trị lớn nhất trên đường đi giữa hai đỉnh

Cho một cây, mỗi đỉnh được gán một giá trị. Có các truy vấn có dạng $(a, b)$, trong đó $a$ và $b$ là hai đỉnh trong cây, và yêu cầu là tìm giá trị lớn nhất trên đường đi giữa các đỉnh $a$ và $b$.

Chúng ta xây dựng trước một phân rã nặng-nhẹ của cây. Trên mỗi đường đi nặng, chúng ta sẽ xây dựng một [cây phân đoạn](../data_structures/segment_tree.md), cho phép chúng ta tìm kiếm một đỉnh có giá trị được gán lớn nhất trong đoạn được chỉ định của đường đi nặng được chỉ định trong $\mathcal{O}(\log n)$. Mặc dù số lượng đường đi nặng trong phân rã nặng-nhẹ có thể lên tới $n - 1$, tổng kích thước của tất cả các đường đi bị giới hạn bởi $\mathcal{O}(n)$, do đó tổng kích thước của các cây phân đoạn cũng sẽ là tuyến tính.

Để trả lời một truy vấn $(a, b)$, chúng ta tìm [tổ tiên chung thấp nhất](https://en.wikipedia.org/wiki/Lowest_common_ancestor) của $a$ và $b$ là $l$, bằng bất kỳ phương pháp ưa thích nào. Bây giờ nhiệm vụ đã được quy về hai truy vấn $(a, l)$ và $(b, l)$, với mỗi truy vấn chúng ta có thể làm như sau: tìm đường đi nặng mà đỉnh thấp hơn nằm trong đó, thực hiện một truy vấn trên đường đi này, di chuyển lên đỉnh của đường đi này, một lần nữa xác định chúng ta đang ở trên đường đi nặng nào và thực hiện một truy vấn trên đó, và cứ thế, cho đến khi chúng ta đến đường đi chứa $l$.

Cần cẩn thận với trường hợp khi, ví dụ, $a$ và $l$ nằm trên cùng một đường đi nặng - thì truy vấn lớn nhất trên đường đi này nên được thực hiện không phải trên bất kỳ tiền tố nào, mà trên đoạn bên trong giữa $a$ và $l$.

Trả lời các truy vấn con $(a, l)$ và $(b, l)$ mỗi truy vấn yêu cầu đi qua $\mathcal{O}(\log n)$ đường đi nặng và đối với mỗi đường đi, một truy vấn lớn nhất được thực hiện trên một số đoạn của đường đi, lại yêu cầu $\mathcal{O}(\log n)$ thao tác trong cây phân đoạn.
Do đó, một truy vấn $(a, b)$ mất thời gian $\mathcal{O}(\log^2 n)$.

Nếu bạn tính toán và lưu trữ thêm các giá trị lớn nhất của tất cả các tiền tố cho mỗi đường đi nặng, thì bạn sẽ có một giải pháp $\mathcal{O}(\log n)$ vì tất cả các truy vấn lớn nhất đều nằm trên các tiền tố ngoại trừ nhiều nhất một lần khi chúng ta đến tổ tiên $l$.


###  Tổng các số trên đường đi giữa hai đỉnh

Cho một cây, mỗi đỉnh được gán một giá trị. Có các truy vấn có dạng $(a, b)$, trong đó $a$ và $b$ là hai đỉnh trong cây, và yêu cầu là tìm tổng các giá trị trên đường đi giữa các đỉnh $a$ và $b$. Một biến thể của nhiệm vụ này có thể có thêm các thao tác cập nhật thay đổi số được gán cho một hoặc nhiều đỉnh.

Nhiệm vụ này có thể được giải quyết tương tự như bài toán trước về các giá trị lớn nhất với sự trợ giúp của phân rã nặng-nhẹ bằng cách xây dựng các cây phân đoạn trên các đường đi nặng. Tổng tiền tố có thể được sử dụng thay thế nếu không có cập nhật. Tuy nhiên, bài toán này có thể được giải quyết bằng các kỹ thuật đơn giản hơn.

Nếu không có cập nhật, thì có thể tìm ra tổng trên đường đi giữa hai đỉnh song song với việc tìm kiếm LCA của hai đỉnh bằng cách [nhảy nhị phân](lca_binary_lifting.md) — để làm điều này, cùng với các tổ tiên thứ $2^k$ của mỗi đỉnh, cũng cần phải lưu trữ tổng trên các đường đi lên đến các tổ tiên đó trong quá trình tiền xử lý.

Có một cách tiếp cận khác về cơ bản cho bài toán này - xem xét [chu trình Euler](https://en.wikipedia.org/wiki/Euler_tour_technique) của cây, và xây dựng một cây phân đoạn trên đó. Thuật toán này được xem xét trong một [bài viết về một bài toán tương tự](tree_painting.md). Một lần nữa, nếu không có cập nhật, việc lưu trữ tổng tiền tố là đủ và không cần cây phân đoạn.

Cả hai phương pháp này đều cung cấp các giải pháp tương đối đơn giản mất $\mathcal{O}(\log n)$ cho một truy vấn.

### Tô lại các cạnh của đường đi giữa hai đỉnh

Cho một cây, mỗi cạnh ban đầu được tô màu trắng. Có các cập nhật có dạng $(a, b, c)$, trong đó $a$ và $b$ là hai đỉnh và $c$ là một màu, hướng dẫn rằng tất cả các cạnh trên đường đi từ $a$ đến $b$ phải được tô lại bằng màu $c$. Sau tất cả các lần tô lại, yêu cầu là báo cáo có bao nhiêu cạnh của mỗi màu đã thu được.

Tương tự như các bài toán trên, giải pháp chỉ đơn giản là áp dụng phân rã nặng-nhẹ và tạo một [cây phân đoạn](../data_structures/segment_tree.md) trên mỗi đường đi nặng.

Mỗi lần tô lại trên đường đi $(a, b)$ sẽ biến thành hai cập nhật $(a, l)$ và $(b, l)$, trong đó $l$ là tổ tiên chung thấp nhất của các đỉnh $a$ và $b$.   
$\mathcal{O}(\log n)$ cho mỗi đường đi với $\mathcal{O}(\log n)$ đường đi dẫn đến độ phức tạp $\mathcal{O}(\log^2 n)$ cho mỗi cập nhật.

## Cài đặt

Một số phần nhất định của phương pháp tiếp cận đã thảo luận ở trên có thể được sửa đổi để làm cho việc triển khai dễ dàng hơn mà không làm mất hiệu quả.

* Định nghĩa của **cạnh nặng** có thể được thay đổi thành **cạnh dẫn đến con có cây con lớn nhất**, với các trường hợp hòa được giải quyết một cách tùy ý. Điều này có thể dẫn đến một số cạnh nhẹ được chuyển đổi thành nặng, có nghĩa là một số đường đi nặng sẽ kết hợp để tạo thành một đường đi duy nhất, nhưng tất cả các đường đi nặng sẽ vẫn không giao nhau. Nó cũng vẫn được đảm bảo rằng việc đi xuống một cạnh nhẹ sẽ làm giảm kích thước cây con xuống một nửa hoặc ít hơn.
* Thay vì xây dựng cây phân đoạn trên mỗi đường đi nặng, một cây phân đoạn duy nhất có thể được sử dụng với các đoạn không giao nhau được phân bổ cho mỗi đường đi nặng.
* Đã đề cập rằng việc trả lời các truy vấn yêu cầu tính toán LCA. Mặc dù LCA có thể được tính toán riêng, cũng có thể tích hợp việc tính toán LCA vào quá trình trả lời các truy vấn.

Để thực hiện phân rã nặng-nhẹ:

```cpp
vector<int> parent, depth, heavy, head, pos;
int cur_pos;

int dfs(int v, vector<vector<int>> const& adj) {
    int size = 1;
    int max_c_size = 0;
    for (int c : adj[v]) {
        if (c != parent[v]) {
            parent[c] = v, depth[c] = depth[v] + 1;
            int c_size = dfs(c, adj);
            size += c_size;
            if (c_size > max_c_size)
                max_c_size = c_size, heavy[v] = c;
        }
    }
    return size;
}

void decompose(int v, int h, vector<vector<int>> const& adj) {
    head[v] = h, pos[v] = cur_pos++;
    if (heavy[v] != -1)
        decompose(heavy[v], h, adj);
    for (int c : adj[v]) {
        if (c != parent[v] && c != heavy[v])
            decompose(c, c, adj);
    }
}

void init(vector<vector<int>> const& adj) {
    int n = adj.size();
    parent = vector<int>(n);
    depth = vector<int>(n);
    heavy = vector<int>(n, -1);
    head = vector<int>(n);
    pos = vector<int>(n);
    cur_pos = 0;

    dfs(0, adj);
    decompose(0, 0, adj);
}
```

Danh sách kề của cây phải được truyền cho hàm `init`, và việc phân rã được thực hiện giả sử đỉnh `0` là gốc.

Hàm `dfs` được sử dụng để tính toán `heavy[v]`, con ở đầu kia của cạnh nặng từ `v`, cho mọi đỉnh `v`. Ngoài ra `dfs` cũng lưu trữ cha và độ sâu của mỗi đỉnh, sẽ hữu ích sau này trong các truy vấn.

Hàm `decompose` gán cho mỗi đỉnh `v` các giá trị `head[v]` và `pos[v]`, tương ứng là đầu của đường đi nặng mà `v` thuộc về và vị trí của `v` trên cây phân đoạn duy nhất bao phủ tất cả các đỉnh.

Để trả lời các truy vấn trên các đường đi, ví dụ truy vấn lớn nhất đã thảo luận, chúng ta có thể làm như sau:

```cpp
int query(int a, int b) {
    int res = 0;
    for (; head[a] != head[b]; b = parent[head[b]]) {
        if (depth[head[a]] > depth[head[b]])
            swap(a, b);
        int cur_heavy_path_max = segment_tree_query(pos[head[b]], pos[b]);
        res = max(res, cur_heavy_path_max);
    }
    if (depth[a] > depth[b])
        swap(a, b);
    int last_heavy_path_max = segment_tree_query(pos[a], pos[b]);
    res = max(res, last_heavy_path_max);
    return res;
}
```

## Bài tập thực hành

- [SPOJ - QTREE - Query on a tree](https://www.spoj.com/problems/QTREE/)
- [CSES - Path Queries II](https://cses.fi/problemset/task/2134)
- [Codeforces - Subway Lines](https://codeforces.com/gym/101908/problem/L)
- [Codeforces - Tree Queries](https://codeforces.com/contest/1254/problem/D)
- [Codeforces - Tree or not Tree](https://codeforces.com/contest/117/problem/E)
- [Codeforces - The Tree](https://codeforces.com/contest/1017/problem/G)
- [Balkan OI 2018 - Min-max tree](https://oj.uz/problem/view/BOI18_minmaxtree)