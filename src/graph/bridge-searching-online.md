---
tags:
  - Translated
e_maxx_link: bridge_searching_online
---

# Tìm cầu trực tuyến (Finding Bridges Online) {: #finding-bridges-online}

Chúng ta được cho một đồ thị vô hướng.
Một cầu (bridge) là một cạnh mà việc loại bỏ nó làm cho đồ thị mất liên thông (hoặc, chính xác hơn là làm tăng số lượng các thành phần liên thông).
Nhiệm vụ của chúng ta là tìm tất cả các cầu trong đồ thị đã cho.

Một cách không chính thức, nhiệm vụ này có thể được đặt ra như sau:
chúng ta phải tìm tất cả các con đường "quan trọng" trên bản đồ đường bộ đã cho, tức là những con đường mà việc loại bỏ bất kỳ con đường nào trong số đó sẽ dẫn đến việc một số thành phố không thể tiếp cận được từ những thành phố khác.

Đã có bài viết [Tìm Cầu trong $O(N+M)$](bridge-searching.md) giải quyết nhiệm vụ này bằng cách duyệt [Tìm kiếm theo chiều sâu (DFS)](depth-first-search.md).
Thuật toán này sẽ phức tạp hơn nhiều nhưng nó có một lợi thế lớn:
thuật toán được mô tả trong bài viết này hoạt động trực tuyến (online), có nghĩa là đồ thị đầu vào không cần phải biết trước.
Các cạnh được thêm vào từng cái một, và sau mỗi lần thêm, thuật toán sẽ đếm lại tất cả các cầu trong đồ thị hiện tại.
Nói cách khác, thuật toán được thiết kế để hoạt động hiệu quả trên một đồ thị động, thay đổi.

Nói một cách chính xác hơn, phát biểu của bài toán như sau:
Ban đầu đồ thị rỗng và bao gồm $n$ đỉnh.
Sau đó, chúng ta nhận được các cặp đỉnh $(a, b)$, biểu thị một cạnh được thêm vào đồ thị.
Sau mỗi cạnh nhận được, tức là sau khi thêm mỗi cạnh, hãy xuất ra số lượng cầu hiện tại trong đồ thị.

Cũng có thể duy trì danh sách tất cả các cầu cũng như hỗ trợ rõ ràng các thành phần liên thông 2 cạnh (2-edge-connected components).

Thuật toán được mô tả bên dưới hoạt động trong thời gian $O(n \log n + m)$, trong đó $m$ là số cạnh.
Thuật toán dựa trên cấu trúc dữ liệu [Disjoint Set Union](../data_structures/disjoint_set_union.md).
Tuy nhiên, việc cài đặt trong bài viết này tốn thời gian $O(n \log n + m \log n)$, vì nó sử dụng phiên bản đơn giản hóa của DSU không có Union by Rank (hợp nhất theo hạng).

## Thuật toán (Algorithm) {: #algorithm}

Đầu tiên, hãy định nghĩa thành phần liên thông 2 cạnh (2-edge-connected component):
đó là một thành phần liên thông vẫn giữ nguyên tính liên thông bất cứ khi nào bạn loại bỏ ít hơn $k$ cạnh.

Rất dễ thấy rằng các cầu phân chia đồ thị thành các thành phần liên thông 2 cạnh.
Nếu chúng ta nén mỗi thành phần liên thông 2 cạnh đó thành các đỉnh và chỉ để lại các cầu làm các cạnh trong đồ thị nén, thì chúng ta thu được một đồ thị không có chu trình, tức là một rừng (forest).

Thuật toán được mô tả dưới đây duy trì khu rừng này một cách rõ ràng cũng như các thành phần liên thông 2 cạnh.

Rõ ràng là ban đầu, khi đồ thị rỗng, nó chứa $n$ thành phần liên thông 2 cạnh, bản thân chúng không được kết nối.

Khi thêm cạnh tiếp theo $(a, b)$, có thể xảy ra ba tình huống:

*   Cả hai đỉnh $a$ và $b$ đều nằm trong cùng một thành phần liên thông 2 cạnh - khi đó cạnh này không phải là cầu, và không thay đổi bất cứ điều gì trong cấu trúc rừng, vì vậy chúng ta có thể bỏ qua cạnh này.

    Do đó, trong trường hợp này số lượng cầu không thay đổi.

*   Các đỉnh $a$ và $b$ nằm trong các thành phần liên thông hoàn toàn khác nhau, tức là mỗi đỉnh là một phần của một cây khác nhau.
    Trong trường hợp này, cạnh $(a, b)$ trở thành một cầu mới, và hai cây này được kết hợp thành một (và tất cả các cầu cũ vẫn còn).

    Do đó, trong trường hợp này, số lượng cầu tăng thêm một.

*   Các đỉnh $a$ và $b$ nằm trong một thành phần liên thông, nhưng nằm trong các thành phần liên thông 2 cạnh khác nhau.
    Trong trường hợp này, cạnh này tạo thành một chu trình cùng với một số cầu cũ.
    Tất cả các cầu này kết thúc việc là cầu, và chu trình kết quả phải được nén thành một thành phần liên thông 2 cạnh mới.

    Do đó, trong trường hợp này, số lượng cầu giảm đi một hoặc nhiều hơn.

Do đó, toàn bộ nhiệm vụ được giảm xuống thành việc thực hiện hiệu quả tất cả các thao tác này trên rừng các thành phần liên thông 2 cạnh.

## Cấu trúc dữ liệu để lưu trữ rừng (Data Structures for storing the forest) {: #data-structures-for-storing-the-forest}

Cấu trúc dữ liệu duy nhất mà chúng ta cần là [Disjoint Set Union](../data_structures/disjoint_set_union.md).
Trên thực tế, chúng ta sẽ tạo hai bản sao của cấu trúc này:
một bản sẽ là để duy trì các thành phần liên thông (connected components), bản còn lại để duy trì các thành phần liên thông 2 cạnh (2-edge-connected components).
Và ngoài ra, chúng ta lưu trữ cấu trúc của các cây trong rừng các thành phần liên thông 2 cạnh thông qua các con trỏ:
Mỗi thành phần liên thông 2 cạnh sẽ lưu trữ chỉ số `par[]` của tổ tiên của nó trong cây.

Bây giờ chúng ta sẽ liên tục phân tích mọi thao tác mà chúng ta cần học cách cài đặt:

  * Kiểm tra xem liệu hai đỉnh có nằm trong cùng một thành phần liên thông / liên thông 2 cạnh hay không.
    Nó được thực hiện với thuật toán DSU thông thường, chúng ta chỉ cần tìm và so sánh các đại diện của các DSU.
  
  * Nối hai cây cho một số cạnh $(a, b)$.
    Vì có thể xảy ra trường hợp cả đỉnh $a$ và đỉnh $b$ đều không phải là gốc của cây của chúng, cách duy nhất để kết nối hai cây này là đổi gốc (re-root) một trong hai cây.
    Ví dụ, bạn có thể đổi gốc cây của đỉnh $a$, và sau đó gắn nó vào một cây khác bằng cách đặt tổ tiên của $a$ thành $b$.
  
    Tuy nhiên, câu hỏi về hiệu quả của thao tác đổi gốc nảy sinh:
    để đổi gốc cây với gốc $r$ sang đỉnh $v$, cần phải thăm tất cả các đỉnh trên đường đi giữa $v$ và $r$ và chuyển hướng các con trỏ `par[]` theo hướng ngược lại, và cũng thay đổi các tham chiếu đến các tổ tiên trong DSU chịu trách nhiệm cho các thành phần liên thông.
  
    Do đó, chi phí của việc đổi gốc là $O(h)$, trong đó $h$ là chiều cao của cây.
    Bạn có thể đưa ra một ước tính thậm chí tồi tệ hơn bằng cách nói rằng chi phí là $O(\text{size})$ trong đó $\text{size}$ là số lượng đỉnh trong cây.
    Độ phức tạp cuối cùng sẽ không khác biệt.
  
    Bây giờ chúng ta áp dụng một kỹ thuật tiêu chuẩn: chúng ta đổi gốc cây chứa ít đỉnh hơn.
    Sau đó, theo trực giác, trường hợp xấu nhất là khi hai cây có kích thước xấp xỉ bằng nhau được kết hợp, nhưng sau đó kết quả là một cây có kích thước gấp đôi.
    Điều này không cho phép tình huống này xảy ra nhiều lần.
  
    Nói chung, tổng chi phí có thể được viết dưới dạng truy hồi:
    
    \[ T(n) = \max_{k = 1 \ldots n-1} \left\{ T(k) + T(n - k) + O(\min(k, n - k))\right\} \]
    
    $T(n)$ là số lượng thao tác cần thiết để có được một cây với $n$ đỉnh bằng cách đổi gốc và hợp nhất các cây.
    Một cây có kích thước $n$ có thể được tạo ra bằng cách kết hợp hai cây nhỏ hơn có kích thước $k$ và $n - k$.
    Công thức truy hồi này có lời giải $T(n) = O (n \log n)$.
  
    Do đó, tổng thời gian dành cho tất cả các thao tác đổi gốc sẽ là $O(n \log n)$ nếu chúng ta luôn đổi gốc cây nhỏ hơn trong hai cây.
  
    Chúng ta sẽ phải duy trì kích thước của mỗi thành phần liên thông, nhưng cấu trúc dữ liệu DSU làm cho điều này trở nên khả thi mà không gặp khó khăn gì.
  
  * Tìm kiếm chu trình được hình thành bằng cách thêm một cạnh mới $(a, b)$.
    Vì $a$ và $b$ đã được kết nối trong cây nên chúng ta cần tìm [Tổ tiên chung thấp nhất (LCA)](lca.md) của các đỉnh $a$ và $b$.
    Chu trình sẽ bao gồm các đường đi từ $b$ đến LCA, từ LCA đến $a$ và cạnh $a$ đến $b$.
  
    Sau khi tìm thấy chu trình, chúng ta nén tất cả các đỉnh của chu trình được phát hiện thành một đỉnh.
    Điều này có nghĩa là chúng ta đã có độ phức tạp tỷ lệ thuận với độ dài chu trình, điều đó có nghĩa là chúng ta cũng có thể sử dụng bất kỳ thuật toán LCA nào tỷ lệ thuận với độ dài và không cần phải sử dụng bất kỳ thuật toán nhanh nào.
  
    Vì tất cả thông tin về cấu trúc của cây đều có sẵn trong mảng tổ tiên `par[]`, thuật toán LCA hợp lý duy nhất là như sau:
    đánh dấu các đỉnh $a$ và $b$ là đã thăm, sau đó chúng ta đi đến tổ tiên của chúng `par[a]` và `par[b]` và đánh dấu chúng, sau đó tiến đến tổ tiên của chúng và cứ thế, cho đến khi chúng ta đến một đỉnh đã được đánh dấu.
    Đỉnh này là LCA mà chúng ta đang tìm kiếm, và chúng ta có thể tìm các đỉnh trên chu trình bằng cách duyệt lại đường đi từ $a$ và $b$ đến LCA.
  
    Rõ ràng là độ phức tạp của thuật toán này tỷ lệ thuận với độ dài của chu trình mong muốn.
  
  * Nén chu trình bằng cách thêm một cạnh mới $(a, b)$ trong một cây.
  
    Chúng ta cần tạo một thành phần liên thông 2 cạnh mới, bao gồm tất cả các đỉnh của chu trình được phát hiện (chu trình được phát hiện cũng có thể bao gồm một số thành phần liên thông 2 cạnh, nhưng điều này không thay đổi bất cứ điều gì).
    Ngoài ra, cần phải nén chúng theo cách mà cấu trúc của cây không bị xáo trộn, và tất cả các con trỏ `par[]` và hai DSU vẫn chính xác.
  
    Cách dễ nhất để đạt được điều này là nén tất cả các đỉnh của chu trình vào LCA của chúng.
    Trên thực tế, LCA là đỉnh cao nhất trong số các đỉnh, tức là con trỏ tổ tiên `par[]` của nó vẫn không thay đổi.
    Đối với tất cả các đỉnh khác của vòng lặp, các tổ tiên không cần cập nhật, vì các đỉnh này đơn giản là không còn tồn tại nữa.
    Nhưng trong DSU của các thành phần liên thông 2 cạnh, tất cả các đỉnh này sẽ chỉ trỏ đến LCA.
  
    Chúng ta sẽ cài đặt DSU của các thành phần liên thông 2 cạnh mà không cần tối ưu hóa Union by rank, do đó chúng ta sẽ nhận được độ phức tạp trung bình là $O(\log n)$ cho mỗi truy vấn.
    Để đạt được độ phức tạp trung bình là $O(1)$ cho mỗi truy vấn, chúng ta cần kết hợp các đỉnh của chu trình theo Union by rank, và sau đó gán `par[]` cho phù hợp.

## Cài đặt (Implementation) {: #implementation}

Dưới đây là cài đặt cuối cùng của toàn bộ thuật toán.

Như đã đề cập trước đó, để đơn giản, DSU của các thành phần liên thông 2 cạnh được viết mà không có Union by rank, do đó độ phức tạp kết quả sẽ là trung bình $O(\log n)$.

Ngoài ra trong cài đặt này, bản thân các cầu không được lưu trữ, chỉ có số lượng của chúng `bridges`.
Tuy nhiên, sẽ không khó để tạo một `set` của tất cả các cầu.

Ban đầu bạn gọi hàm `init()`, khởi tạo hai DSU (tạo một tập hợp riêng cho mỗi đỉnh và đặt kích thước bằng một), và đặt các tổ tiên `par`.

Hàm chính là `add_edge(a, b)`, xử lý và thêm một cạnh mới.

```cpp
vector<int> par, dsu_2ecc, dsu_cc, dsu_cc_size;
int bridges;
int lca_iteration;
vector<int> last_visit;
 
void init(int n) {
    par.resize(n);
    dsu_2ecc.resize(n);
    dsu_cc.resize(n);
    dsu_cc_size.resize(n);
    lca_iteration = 0;
    last_visit.assign(n, 0);
    for (int i=0; i<n; ++i) {
        dsu_2ecc[i] = i;
        dsu_cc[i] = i;
        dsu_cc_size[i] = 1;
        par[i] = -1;
    }
    bridges = 0;
}
 
int find_2ecc(int v) {
    if (v == -1)
        return -1;
    return dsu_2ecc[v] == v ? v : dsu_2ecc[v] = find_2ecc(dsu_2ecc[v]);
}
 
int find_cc(int v) {
    v = find_2ecc(v);
    return dsu_cc[v] == v ? v : dsu_cc[v] = find_cc(dsu_cc[v]);
}
 
void make_root(int v) {
    int root = v;
    int child = -1;
    while (v != -1) {
        int p = find_2ecc(par[v]);
        par[v] = child;
        dsu_cc[v] = root;
        child = v;
        v = p;
    }
    dsu_cc_size[root] = dsu_cc_size[child];
}

void merge_path (int a, int b) {
    ++lca_iteration;
    vector<int> path_a, path_b;
    int lca = -1;
    while (lca == -1) {
        if (a != -1) {
            a = find_2ecc(a);
            path_a.push_back(a);
            if (last_visit[a] == lca_iteration){
                lca = a;
                break;
                }
            last_visit[a] = lca_iteration;
            a = par[a];
        }
        if (b != -1) {
            b = find_2ecc(b);
            path_b.push_back(b);
            if (last_visit[b] == lca_iteration){
                lca = b;
                break;
                }
            last_visit[b] = lca_iteration;
            b = par[b];
        }
        
    }

    for (int v : path_a) {
        dsu_2ecc[v] = lca;
        if (v == lca)
            break;
        --bridges;
    }
    for (int v : path_b) {
        dsu_2ecc[v] = lca;
        if (v == lca)
            break;
        --bridges;
    }
}
 
void add_edge(int a, int b) {
    a = find_2ecc(a);
    b = find_2ecc(b);
    if (a == b)
        return;
 
    int ca = find_cc(a);
    int cb = find_cc(b);

    if (ca != cb) {
        ++bridges;
        if (dsu_cc_size[ca] > dsu_cc_size[cb]) {
            swap(a, b);
            swap(ca, cb);
        }
        make_root(a);
        par[a] = dsu_cc[a] = b;
        dsu_cc_size[cb] += dsu_cc_size[a];
    } else {
        merge_path(a, b);
    }
}
```

DSU cho các thành phần liên thông 2 cạnh được lưu trữ trong vector `dsu_2ecc`, và hàm trả về đại diện là `find_2ecc(v)`.
Hàm này được sử dụng nhiều lần trong phần còn lại của mã, vì sau khi nén một số đỉnh thành một, tất cả các đỉnh này không còn tồn tại nữa và thay vào đó chỉ có người lãnh đạo có tổ tiên `par` chính xác trong rừng các thành phần liên thông 2 cạnh.

DSU cho các thành phần liên thông được lưu trữ trong vector `dsu_cc`, và cũng có một vector bổ sung `dsu_cc_size` để lưu trữ kích thước thành phần.
Hàm `find_cc(v)` trả về người lãnh đạo của thành phần liên thông (thực ra là gốc của cây).

Việc đổi gốc của một cây `make_root(v)` hoạt động như mô tả ở trên:
nó đi từ đỉnh $v$ qua các tổ tiên đến đỉnh gốc, mỗi lần chuyển hướng tổ tiên `par` theo hướng ngược lại.
Liên kết đến đại diện của thành phần liên thông `dsu_cc` cũng được cập nhật, để nó trỏ đến đỉnh gốc mới.
Sau khi đổi gốc, chúng ta phải gán cho gốc mới kích thước chính xác của thành phần liên thông.
Ngoài ra, chúng ta phải cẩn thận gọi `find_2ecc()` để lấy các đại diện của thành phần liên thông 2 cạnh, thay vì một số đỉnh khác đã bị nén.

Hàm tìm chu trình và nén `merge_path(a, b)` cũng được thực hiện như mô tả ở trên.
Nó tìm kiếm LCA của $a$ và $b$ bằng cách nâng các nút này song song, cho đến khi chúng ta gặp một đỉnh lần thứ hai.
Vì mục đích hiệu quả, chúng ta chọn một định danh duy nhất cho mỗi cuộc gọi tìm LCA và đánh dấu các đỉnh đã đi qua bằng nó.
Thao tác này hoạt động trong $O(1)$, trong khi các phương pháp khác như sử dụng `set` thực hiện kém hơn.
Các đường dẫn đã qua được lưu trữ trong các vector `path_a` và `path_b`, và chúng ta sử dụng chúng để duyệt qua chúng lần thứ hai lên đến LCA, qua đó thu được tất cả các đỉnh của chu trình.
Tất cả các đỉnh của chu trình được nén bằng cách gắn chúng vào LCA, do đó độ phức tạp trung bình là $O(\log n)$ (vì chúng ta không sử dụng Union by rank).
Tất cả các cạnh chúng ta đi qua đều là các cầu, vì vậy chúng ta trừ 1 cho mỗi cạnh trong chu trình.

Cuối cùng, hàm truy vấn `add_edge(a, b)` xác định các thành phần liên thông mà các đỉnh $a$ và $b$ nằm trong đó.
Nếu chúng nằm trong các thành phần liên thông khác nhau, thì một cây nhỏ hơn sẽ được đổi gốc và sau đó gắn vào cây lớn hơn.
Ngược lại nếu các đỉnh $a$ và $b$ nằm trong một cây, nhưng trong các thành phần liên thông 2 cạnh khác nhau, thì hàm `merge_path(a, b)` được gọi, hàm này sẽ phát hiện chu trình và nén nó thành một thành phần liên thông 2 cạnh.
