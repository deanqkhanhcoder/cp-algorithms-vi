---
tags:
  - Translated
e_maxx_link: mst_prim
---

# Cây khung nhỏ nhất - Thuật toán Prim (Minimum spanning tree - Prim's algorithm) {: #minimum-spanning-tree-prims-algorithm}

Cho một đồ thị vô hướng có trọng số $G$ với $n$ đỉnh và $m$ cạnh.
Bạn muốn tìm một cây khung (spanning tree) của đồ thị này kết nối tất cả các đỉnh và có trọng số nhỏ nhất (tức là tổng trọng số của các cạnh là nhỏ nhất).
Một cây khung là một tập hợp các cạnh sao cho bất kỳ đỉnh nào cũng có thể đến bất kỳ đỉnh nào khác bằng chính xác một đường đi đơn giản.
Cây khung có trọng số nhỏ nhất được gọi là cây khung nhỏ nhất (minimum spanning tree - MST).

Trong hình bên trái bạn có thể thấy một đồ thị vô hướng có trọng số, và trong hình bên phải bạn có thể thấy cây khung nhỏ nhất tương ứng.

<div style="text-align: center;">
  <img src="MST_before.png" alt="Random graph">
  <img src="MST_after.png" alt="MST of this graph">
</div>

Dễ dàng thấy rằng bất kỳ cây khung nào cũng nhất thiết chứa $n-1$ cạnh.

Bài toán này xuất hiện khá tự nhiên trong rất nhiều bài toán.
Ví dụ trong bài toán sau:
có $n$ thành phố và với mỗi cặp thành phố chúng ta được cho chi phí để xây dựng một con đường giữa chúng (hoặc chúng ta biết rằng về mặt vật lý là không thể xây dựng một con đường giữa chúng).
Chúng ta phải xây dựng các con đường, sao cho chúng ta có thể đi từ mỗi thành phố đến mọi thành phố khác, và chi phí để xây dựng tất cả các con đường là nhỏ nhất.

## Thuật toán Prim (Prim's Algorithm) {: #prims-algorithm}

Thuật toán này ban đầu được phát hiện bởi nhà toán học người Séc Vojtěch Jarník vào năm 1930.
Tuy nhiên thuật toán này chủ yếu được biết đến với tên gọi thuật toán Prim theo tên nhà toán học người Mỹ Robert Clay Prim, người đã phát hiện lại và xuất bản nó vào năm 1957.
Ngoài ra Edsger Dijkstra đã xuất bản thuật toán này vào năm 1959.

### Mô tả thuật toán (Algorithm description)

Ở đây chúng tôi mô tả thuật toán ở dạng đơn giản nhất của nó.
Cây khung nhỏ nhất được xây dựng dần dần bằng cách thêm từng cạnh một.
Ban đầu cây khung chỉ bao gồm một đỉnh duy nhất (được chọn tùy ý).
Sau đó cạnh có trọng số nhỏ nhất đi ra từ đỉnh này được chọn và thêm vào cây khung.
Sau đó cây khung đã bao gồm hai đỉnh.
Bây giờ chọn và thêm cạnh có trọng số nhỏ nhất có một đầu ở một đỉnh đã chọn (tức là một đỉnh đã là một phần của cây khung), và đầu kia ở một đỉnh chưa được chọn.
Và cứ thế, tức là mỗi lần chúng ta chọn và thêm cạnh với trọng số nhỏ nhất nối một đỉnh đã chọn với một đỉnh chưa chọn.
Quá trình này được lặp lại cho đến khi cây khung chứa tất cả các đỉnh (hoặc tương đương cho đến khi chúng ta có $n - 1$ cạnh).

Cuối cùng cây khung được xây dựng sẽ là nhỏ nhất.
Nếu đồ thị ban đầu không liên thông, thì không tồn tại cây khung, vì vậy số lượng cạnh được chọn sẽ ít hơn $n - 1$.

### Chứng minh (Proof)

Giả sử đồ thị $G$ liên thông, tức là câu trả lời tồn tại.
Chúng tôi ký hiệu $T$ là đồ thị kết quả được tìm thấy bởi thuật toán Prim, và $S$ là cây khung nhỏ nhất.
Rõ ràng $T$ thực sự là một cây khung và một đồ thị con của $G$.
Chúng ta chỉ cần chỉ ra rằng trọng số của $S$ và $T$ trùng nhau.

Hãy xem xét lần đầu tiên trong thuật toán khi chúng ta thêm một cạnh vào $T$ mà không phải là một phần của $S$.
Hãy ký hiệu cạnh này là $e$, các đầu của nó là $a$ và $b$, và tập hợp các đỉnh đã được chọn là $V$ ($a \in V$ và $b \notin V$, hoặc ngược lại).

Trong cây khung nhỏ nhất $S$ các đỉnh $a$ và $b$ được kết nối bởi một đường đi $P$ nào đó.
Trên đường đi này, chúng ta có thể tìm thấy một cạnh $f$ sao cho một đầu của $f$ nằm trong $V$ và đầu kia thì không.
Vì thuật toán đã chọn $e$ thay vì $f$, điều đó có nghĩa là trọng số của $f$ lớn hơn hoặc bằng trọng số của $e$.

Chúng ta thêm cạnh $e$ vào cây khung nhỏ nhất $S$ và loại bỏ cạnh $f$.
Bằng cách thêm $e$ chúng ta đã tạo ra một chu trình, và vì $f$ cũng là một phần của chu trình duy nhất đó, bằng cách loại bỏ nó, đồ thị kết quả lại không có chu trình.
Và bởi vì chúng ta chỉ loại bỏ một cạnh khỏi một chu trình, đồ thị kết quả vẫn liên thông.

Cây khung kết quả không thể có tổng trọng số lớn hơn, vì trọng số của $e$ không lớn hơn trọng số của $f$, và nó cũng không thể có trọng số nhỏ hơn vì $S$ là một cây khung nhỏ nhất.
Điều này có nghĩa là bằng cách thay thế cạnh $f$ bằng $e$ chúng ta đã tạo ra một cây khung nhỏ nhất khác.
Và $e$ phải có cùng trọng số với $f$.

Do đó, tất cả các cạnh chúng ta chọn trong thuật toán Prim đều có trọng số giống như các cạnh của bất kỳ cây khung nhỏ nhất nào, điều đó có nghĩa là thuật toán Prim thực sự tạo ra một cây khung nhỏ nhất.

## Cài đặt (Implementation) {: #implementation}

Độ phức tạp của thuật toán phụ thuộc vào cách chúng ta tìm kiếm cạnh nhỏ nhất tiếp theo trong số các cạnh thích hợp.
Có nhiều cách tiếp cận dẫn đến độ phức tạp khác nhau và các cách cài đặt khác nhau.

### Cài đặt tầm thường: $O(n m)$ và $O(n^2 + m \log n)$ (Trivial implementations: $O(n m)$ and $O(n^2 + m \log n)$)

Nếu chúng ta tìm kiếm cạnh bằng cách lặp qua tất cả các cạnh có thể, thì mất $O(m)$ thời gian để tìm cạnh có trọng số nhỏ nhất.
Tổng độ phức tạp sẽ là $O(n m)$.
Trong trường hợp xấu nhất, đây là $O(n^3)$, thực sự chậm.

Thuật toán này có thể được cải thiện nếu chúng ta chỉ nhìn vào một cạnh từ mỗi đỉnh đã được chọn.
Ví dụ, chúng ta có thể sắp xếp các cạnh từ mỗi đỉnh theo thứ tự tăng dần của trọng số của chúng, và lưu trữ một con trỏ đến cạnh hợp lệ đầu tiên (tức là một cạnh đi đến một đỉnh chưa được chọn).
Sau đó, sau khi tìm và chọn cạnh nhỏ nhất, chúng ta cập nhật các con trỏ.
Điều này đưa ra độ phức tạp là $O(n^2 + m)$, và để sắp xếp các cạnh thêm $O(m \log n)$, đưa ra độ phức tạp $O(n^2 \log n)$ trong trường hợp xấu nhất.

Dưới đây chúng tôi xem xét hai thuật toán hơi khác nhau, một cho đồ thị dày và một cho đồ thị thưa, cả hai đều có độ phức tạp tốt hơn.

### Đồ thị dày: $O(n^2)$ (Dense graphs: $O(n^2)$)

Chúng ta tiếp cận vấn đề này từ một góc độ khác:
đối với mỗi đỉnh chưa được chọn, chúng ta sẽ lưu trữ cạnh nhỏ nhất đến một đỉnh đã được chọn.

Sau đó, trong một bước, chúng ta chỉ phải nhìn vào các cạnh có trọng số nhỏ nhất này, sẽ có độ phức tạp là $O(n)$.

Sau khi thêm một cạnh, một số con trỏ cạnh nhỏ nhất phải được tính toán lại.
Lưu ý rằng trọng số chỉ có thể giảm, tức là cạnh có trọng số nhỏ nhất của mỗi đỉnh chưa được chọn có thể giữ nguyên, hoặc nó sẽ được cập nhật bởi một cạnh đến đỉnh mới được chọn.
Do đó giai đoạn này cũng có thể được thực hiện trong $O(n)$.

Do đó chúng ta nhận được một phiên bản của thuật toán Prim với độ phức tạp $O(n^2)$.

Đặc biệt việc cài đặt này rất thuận tiện cho bài toán Cây khung nhỏ nhất Euclide:
chúng ta có $n$ điểm trên một mặt phẳng và khoảng cách giữa mỗi cặp điểm là khoảng cách Euclide giữa chúng, và chúng ta muốn tìm một cây khung nhỏ nhất cho đồ thị đầy đủ này.
Nhiệm vụ này có thể được giải quyết bằng thuật toán được mô tả với thời gian $O(n^2)$ và bộ nhớ $O(n)$, điều này không thể thực hiện được với [thuật toán Kruskal](mst_kruskal.md).

```cpp
int n;
vector<vector<int>> adj; // ma trận kề của đồ thị
const int INF = 1000000000; // trọng số INF có nghĩa là không có cạnh

struct Edge {
    int w = INF, to = -1;
};

void prim() {
    int total_weight = 0;
    vector<bool> selected(n, false);
    vector<Edge> min_e(n);
    min_e[0].w = 0;

    for (int i=0; i<n; ++i) {
        int v = -1;
        for (int j = 0; j < n; ++j) {
            if (!selected[j] && (v == -1 || min_e[j].w < min_e[v].w))
                v = j;
        }

        if (min_e[v].w == INF) {
            cout << "No MST!" << endl;
            exit(0);
        }

        selected[v] = true;
        total_weight += min_e[v].w;
        if (min_e[v].to != -1)
            cout << v << " " << min_e[v].to << endl;

        for (int to = 0; to < n; ++to) {
            if (adj[v][to] < min_e[to].w)
                min_e[to] = {adj[v][to], v};
        }
    }

    cout << total_weight << endl;
}
```

Ma trận kề `adj[][]` có kích thước $n \times n$ lưu trữ trọng số của các cạnh, và nó sử dụng trọng số `INF` nếu không tồn tại cạnh giữa hai đỉnh.
Thuật toán sử dụng hai mảng: cờ `selected[]`, cho biết đỉnh nào chúng ta đã chọn, và mảng `min_e[]` lưu trữ cạnh với trọng số nhỏ nhất đến một đỉnh đã chọn cho mỗi đỉnh chưa được chọn (nó lưu trữ trọng số và đỉnh đích).
Thuật toán thực hiện $n$ bước, trong mỗi lần lặp, đỉnh có trọng số cạnh nhỏ nhất được chọn, và `min_e[]` của tất cả các đỉnh khác được cập nhật.

### Đồ thị thưa: $O(m \log n)$ (Sparse graphs: $O(m \log n)$)

Trong thuật toán được mô tả ở trên, có thể diễn giải các thao tác tìm kiếm giá trị nhỏ nhất và sửa đổi một số giá trị là các thao tác tập hợp.
Hai thao tác cổ điển này được hỗ trợ bởi nhiều cấu trúc dữ liệu, ví dụ như bởi `set` trong C++ (được cài đặt thông qua cây đỏ-đen).

Thuật toán chính vẫn giữ nguyên, nhưng bây giờ chúng ta có thể tìm cạnh nhỏ nhất trong thời gian $O(\log n)$.
Mặt khác, việc tính toán lại các con trỏ bây giờ sẽ mất $O(n \log n)$ thời gian, tệ hơn so với thuật toán trước đó.

Nhưng khi chúng ta xem xét rằng chúng ta chỉ cần cập nhật tổng cộng $O(m)$ lần, và thực hiện $O(n)$ tìm kiếm cạnh nhỏ nhất, thì tổng độ phức tạp sẽ là $O(m \log n)$.
Đối với đồ thị thưa, điều này tốt hơn thuật toán trên, nhưng đối với đồ thị dày, điều này sẽ chậm hơn.

```cpp
const int INF = 1000000000;

struct Edge {
    int w = INF, to = -1;
    bool operator<(Edge const& other) const {
        return make_pair(w, to) < make_pair(other.w, other.to);
    }
};

int n;
vector<vector<Edge>> adj;

void prim() {
    int total_weight = 0;
    vector<Edge> min_e(n);
    min_e[0].w = 0;
    set<Edge> q;
    q.insert({0, 0});
    vector<bool> selected(n, false);
    for (int i = 0; i < n; ++i) {
        if (q.empty()) {
            cout << "No MST!" << endl;
            exit(0);
        }

        int v = q.begin()->to;
        selected[v] = true;
        total_weight += q.begin()->w;
        q.erase(q.begin());

        if (min_e[v].to != -1)
            cout << v << " " << min_e[v].to << endl;

        for (Edge e : adj[v]) {
            if (!selected[e.to] && e.w < min_e[e.to].w) {
                q.erase({min_e[e.to].w, e.to});
                min_e[e.to] = {e.w, v};
                q.insert({e.w, e.to});
            }
        }
    }

    cout << total_weight << endl;
}
```

Ở đây đồ thị được biểu diễn thông qua một danh sách kề `adj[]`, trong đó `adj[v]` chứa tất cả các cạnh (dưới dạng cặp trọng số và đích) cho đỉnh `v`.
`min_e[v]` sẽ lưu trữ trọng số của cạnh nhỏ nhất từ đỉnh `v` đến một đỉnh đã được chọn (một lần nữa dưới dạng cặp trọng số và đích).
Ngoài ra hàng đợi `q` được điền với tất cả các đỉnh chưa được chọn theo thứ tự trọng số `min_e` tăng dần.
Thuật toán thực hiện `n` bước, trên mỗi bước nó chọn đỉnh `v` có trọng số `min_e` nhỏ nhất (bằng cách trích xuất nó từ đầu hàng đợi), và sau đó xem qua tất cả các cạnh từ đỉnh này và cập nhật các giá trị trong `min_e` (trong quá trình cập nhật, chúng ta cũng cần loại bỏ cạnh cũ khỏi hàng đợi `q` và đưa vào cạnh mới).
