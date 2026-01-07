---
tags:
  - Translated
e_maxx_link: bridge_searching_online
---

# Tìm cầu trực tuyến

Chúng ta được cho một đồ thị vô hướng.
Một cầu là một cạnh mà việc loại bỏ nó làm cho đồ thị bị mất tính liên thông (hay chính xác hơn, làm tăng số lượng thành phần liên thông).
Nhiệm vụ của chúng ta là tìm tất cả các cầu trong đồ thị đã cho.

Một cách không chính thức, nhiệm vụ này có thể được phát biểu như sau:
chúng ta phải tìm tất cả các con đường "quan trọng" trên bản đồ đường bộ đã cho, tức là những con đường mà việc loại bỏ bất kỳ con đường nào trong số đó sẽ dẫn đến việc một số thành phố không thể đến được từ các thành phố khác.

Đã có bài viết [Tìm cầu trong $O(N+M)$](bridge-searching.md) giải quyết nhiệm vụ này bằng một duyệt [Tìm kiếm theo chiều sâu](depth-first-search.md).
Thuật toán này sẽ phức tạp hơn nhiều, nhưng nó có một ưu điểm lớn:
thuật toán được mô tả trong bài viết này hoạt động trực tuyến, có nghĩa là đồ thị đầu vào không cần phải được biết trước.
Các cạnh được thêm vào một lần tại một thời điểm, và sau mỗi lần thêm, thuật toán đếm lại tất cả các cầu trong đồ thị hiện tại.
Nói cách khác, thuật toán được thiết kế để hoạt động hiệu quả trên một đồ thị động, thay đổi.

Nghiêm ngặt hơn, phát biểu của bài toán như sau:
Ban đầu đồ thị trống và bao gồm $n$ đỉnh.
Sau đó, chúng ta nhận được các cặp đỉnh $(a, b)$, biểu thị một cạnh được thêm vào đồ thị.
Sau mỗi cạnh nhận được, tức là sau khi thêm mỗi cạnh, xuất ra số lượng cầu hiện tại trong đồ thị.

Cũng có thể duy trì một danh sách tất cả các cầu cũng như hỗ trợ rõ ràng các thành phần liên thông 2 cạnh.

Thuật toán được mô tả dưới đây hoạt động trong thời gian $O(n \log n + m)$, trong đó $m$ là số lượng cạnh.
Thuật toán dựa trên cấu trúc dữ liệu [Disjoint Set Union](../data_structures/disjoint_set_union.md).
Tuy nhiên, việc triển khai trong bài viết này mất thời gian $O(n \log n + m \log n)$, vì nó sử dụng phiên bản đơn giản hóa của DSU mà không có Hợp nhất theo Hạng (Union by Rank).

## Thuật toán

Đầu tiên, hãy định nghĩa một thành phần liên thông $k$ cạnh:
đó là một thành phần liên thông vẫn còn liên thông bất cứ khi nào bạn loại bỏ ít hơn $k$ cạnh.

Rất dễ thấy rằng các cầu phân chia đồ thị thành các thành phần liên thông 2 cạnh.
Nếu chúng ta nén mỗi thành phần liên thông 2 cạnh đó thành các đỉnh và chỉ để lại các cầu làm các cạnh trong đồ thị nén, thì chúng ta sẽ thu được một đồ thị không có chu trình, tức là một rừng.

Thuật toán được mô tả dưới đây duy trì rõ ràng rừng này cũng như các thành phần liên thông 2 cạnh.

Rõ ràng là ban đầu, khi đồ thị trống, nó chứa $n$ thành phần liên thông 2 cạnh, mà bản thân chúng không liên thông.

Khi thêm cạnh tiếp theo $(a, b)$ có thể xảy ra ba tình huống:

*   Cả hai đỉnh $a$ và $b$ đều nằm trong cùng một thành phần liên thông 2 cạnh - thì cạnh này không phải là cầu, và không thay đổi gì trong cấu trúc rừng, vì vậy chúng ta có thể bỏ qua cạnh này.

    Do đó, trong trường hợp này, số lượng cầu không thay đổi.

*   Các đỉnh $a$ và $b$ nằm trong các thành phần liên thông hoàn toàn khác nhau, tức là mỗi đỉnh là một phần của một cây khác nhau.
    Trong trường hợp này, cạnh $(a, b)$ trở thành một cầu mới, và hai cây này được kết hợp thành một (và tất cả các cầu cũ vẫn còn).

    Do đó, trong trường hợp này, số lượng cầu tăng thêm một.

*   Các đỉnh $a$ và $b$ nằm trong một thành phần liên thông, nhưng trong các thành phần liên thông 2 cạnh khác nhau.
    Trong trường hợp này, cạnh này tạo thành một chu trình cùng với một số cầu cũ.
    Tất cả các cầu này không còn là cầu nữa, và chu trình kết quả phải được nén thành một thành phần liên thông 2 cạnh mới.

    Do đó, trong trường hợp này, số lượng cầu giảm đi một hoặc nhiều.

Do đó, toàn bộ nhiệm vụ được quy về việc triển khai hiệu quả tất cả các thao tác này trên rừng các thành phần liên thông 2 cạnh.

## Cấu trúc dữ liệu để lưu trữ rừng

Cấu trúc dữ liệu duy nhất mà chúng ta cần là [Disjoint Set Union](../data_structures/disjoint_set_union.md).
Thực tế, chúng ta sẽ tạo hai bản sao của cấu trúc này:
một bản sẽ để duy trì các thành phần liên thông, bản kia để duy trì các thành phần liên thông 2 cạnh.
Và ngoài ra, chúng ta lưu trữ cấu trúc của các cây trong rừng các thành phần liên thông 2 cạnh thông qua các con trỏ:
Mỗi thành phần liên thông 2 cạnh sẽ lưu trữ chỉ số `par[]` của tổ tiên của nó trong cây.

Bây giờ chúng ta sẽ phân tích tuần tự mọi thao tác mà chúng ta cần học để triển khai:

  * Kiểm tra xem hai đỉnh có nằm trong cùng một thành phần liên thông / liên thông 2 cạnh hay không.
    Nó được thực hiện với thuật toán DSU thông thường, chúng ta chỉ cần tìm và so sánh các đại diện của các DSU.
  
  * Nối hai cây cho một cạnh nào đó $(a, b)$.
    Vì có thể xảy ra trường hợp cả đỉnh $a$ và đỉnh $b$ đều không phải là gốc của cây của chúng, cách duy nhất để kết nối hai cây này là thay đổi gốc của một trong số chúng.
    Ví dụ, bạn có thể thay đổi gốc của cây của đỉnh $a$, và sau đó gắn nó vào một cây khác bằng cách đặt tổ tiên của $a$ là $b$.
  
    Tuy nhiên, câu hỏi về tính hiệu quả của thao tác thay đổi gốc nảy sinh:
    để thay đổi gốc của cây có gốc $r$ thành đỉnh $v$, cần phải duyệt qua tất cả các đỉnh trên đường đi giữa $v$ và $r$ và chuyển hướng các con trỏ `par[]` theo hướng ngược lại, và cũng thay đổi các tham chiếu đến các tổ tiên trong DSU chịu trách nhiệm cho các thành phần liên thông.
  
    Do đó, chi phí của việc thay đổi gốc là $O(h)$, trong đó $h$ là chiều cao của cây.
    Bạn có thể đưa ra một ước tính thậm chí còn tệ hơn bằng cách nói rằng chi phí là $O(\text{size})$ trong đó $\text{size}$ là số lượng đỉnh trong cây.
    Độ phức tạp cuối cùng sẽ không khác.
  
    Bây giờ chúng ta áp dụng một kỹ thuật tiêu chuẩn: chúng ta thay đổi gốc của cây chứa ít đỉnh hơn.
    Khi đó, trực giác rõ ràng là trường hợp xấu nhất là khi hai cây có kích thước xấp xỉ bằng nhau được kết hợp, nhưng sau đó kết quả là một cây có kích thước gấp đôi.
    Điều này không cho phép tình huống này xảy ra nhiều lần.
  
    Nói chung, tổng chi phí có thể được viết dưới dạng một công thức đệ quy:
    
    \[ T(n) = \max_{k = 1 \ldots n-1} \left\{ T(k) + T(n - k) + O(\min(k, n - k))\right\} \]
    
    $T(n)$ là số lượng thao tác cần thiết để có được một cây có $n$ đỉnh bằng cách thay đổi gốc và hợp nhất các cây.
    Một cây có kích thước $n$ có thể được tạo bằng cách kết hợp hai cây nhỏ hơn có kích thước $k$ và $n - k$.
    Công thức đệ quy này có nghiệm là $T(n) = O (n \log n)$.
  
    Do đó, tổng thời gian dành cho tất cả các thao tác thay đổi gốc sẽ là $O(n \log n)$ nếu chúng ta luôn thay đổi gốc của cây nhỏ hơn trong hai cây.
  
    Chúng ta sẽ phải duy trì kích thước của mỗi thành phần liên thông, nhưng cấu trúc dữ liệu DSU giúp điều này có thể thực hiện được mà không gặp khó khăn.
  
  * Tìm kiếm chu trình được hình thành bằng cách thêm một cạnh mới $(a, b)$.
    Vì $a$ và $b$ đã được kết nối trong cây, chúng ta cần tìm [Tổ tiên chung thấp nhất](lca.md) của các đỉnh $a$ và $b$.
    Chu trình sẽ bao gồm các đường đi từ $b$ đến LCA, từ LCA đến $a$ và cạnh $a$ đến $b$.
  
    Sau khi tìm thấy chu trình, chúng ta nén tất cả các đỉnh của chu trình được phát hiện thành một đỉnh.
    Điều này có nghĩa là chúng ta đã có độ phức tạp tỷ lệ với độ dài chu trình, có nghĩa là chúng ta cũng có thể sử dụng bất kỳ thuật toán LCA nào tỷ lệ với độ dài, và không cần phải sử dụng bất kỳ thuật toán nhanh nào.
  
    Vì tất cả thông tin về cấu trúc của cây đều có sẵn trong mảng tổ tiên `par[]`, thuật toán LCA hợp lý duy nhất là như sau:
    đánh dấu các đỉnh $a$ và $b$ là đã được thăm, sau đó chúng ta đi đến tổ tiên của chúng `par[a]` và `par[b]` và đánh dấu chúng, sau đó tiến đến tổ tiên của chúng và cứ thế, cho đến khi chúng ta đến một đỉnh đã được đánh dấu.
    Đỉnh này là LCA mà chúng ta đang tìm kiếm, và chúng ta có thể tìm thấy các đỉnh trên chu trình bằng cách duyệt lại đường đi từ $a$ và $b$ đến LCA.
  
    Rõ ràng là độ phức tạp của thuật toán này tỷ lệ với độ dài của chu trình mong muốn.
  
  * Nén chu trình bằng cách thêm một cạnh mới $(a, b)$ vào một cây.
  
    Chúng ta cần tạo một thành phần liên thông 2 cạnh mới, sẽ bao gồm tất cả các đỉnh của chu trình được phát hiện (cũng có thể chu trình được phát hiện tự nó bao gồm một số thành phần liên thông 2 cạnh, nhưng điều này không thay đổi gì).
    Ngoài ra, cần phải nén chúng sao cho cấu trúc của cây không bị xáo trộn, và tất cả các con trỏ `par[]` và hai DSU vẫn chính xác.
  
    Cách dễ nhất để đạt được điều này là nén tất cả các đỉnh của chu trình vào LCA của chúng.
    Thực tế, LCA là đỉnh cao nhất trong số các đỉnh, tức là con trỏ tổ tiên `par[]` của nó không thay đổi.
    Đối với tất cả các đỉnh khác của vòng lặp, các tổ tiên không cần phải được cập nhật, vì các đỉnh này đơn giản là không còn tồn tại.
    Nhưng trong DSU của các thành phần liên thông 2 cạnh, tất cả các đỉnh này sẽ chỉ trỏ đến LCA.
  
    Chúng ta sẽ triển khai DSU của các thành phần liên thông 2 cạnh mà không có tối ưu hóa Hợp nhất theo hạng, do đó chúng ta sẽ có độ phức tạp trung bình $O(\log n)$ cho mỗi truy vấn.
    Để đạt được độ phức tạp trung bình $O(1)$ cho mỗi truy vấn, chúng ta cần kết hợp các đỉnh của chu trình theo Hợp nhất theo hạng, và sau đó gán `par[]` tương ứng.

## Cài đặt

Đây là việc triển khai cuối cùng của toàn bộ thuật toán.

Như đã đề cập trước đó, để đơn giản, DSU của các thành phần liên thông 2 cạnh được viết mà không có Hợp nhất theo hạng, do đó độ phức tạp kết quả sẽ là $O(\log n)$ trung bình.

Cũng trong việc triển khai này, các cầu không được lưu trữ, chỉ có số lượng của chúng `bridges`.
Tuy nhiên, sẽ không khó để tạo một `set` chứa tất cả các cầu.

Ban đầu, bạn gọi hàm `init()`, hàm này khởi tạo hai DSU (tạo một tập hợp riêng cho mỗi đỉnh và đặt kích thước bằng một), và đặt các tổ tiên `par`.

Hàm chính là `add_edge(a, b)`, hàm này xử lý và thêm một cạnh mới.

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

DSU cho các thành phần liên thông 2 cạnh được lưu trong vector `dsu_2ecc`, và hàm trả về đại diện là `find_2ecc(v)`.
Hàm này được sử dụng nhiều lần trong phần còn lại của mã, vì sau khi nén nhiều đỉnh thành một, tất cả các đỉnh này không còn tồn tại, và thay vào đó chỉ có đỉnh đại diện mới có tổ tiên `par` chính xác trong rừng các thành phần liên thông 2 cạnh.

DSU cho các thành phần liên thông được lưu trong vector `dsu_cc`, và cũng có một vector bổ sung `dsu_cc_size` để lưu trữ kích thước thành phần.
Hàm `find_cc(v)` trả về đỉnh đại diện của thành phần liên thông (thực chất là gốc của cây).

Việc thay đổi gốc của một cây `make_root(v)` hoạt động như đã mô tả ở trên:
nó duyệt từ đỉnh $v$ qua các tổ tiên đến đỉnh gốc, mỗi lần chuyển hướng tổ tiên `par` theo hướng ngược lại.
Liên kết đến đại diện của thành phần liên thông `dsu_cc` cũng được cập nhật, để nó trỏ đến đỉnh gốc mới.
Sau khi thay đổi gốc, chúng ta phải gán cho gốc mới kích thước chính xác của thành phần liên thông.
Chúng ta cũng phải cẩn thận rằng chúng ta gọi `find_2ecc()` để có được đại diện của thành phần liên thông 2 cạnh, thay vì một số đỉnh khác đã được nén.

Hàm tìm và nén chu trình `merge_path(a, b)` cũng được triển khai như đã mô tả ở trên.
Nó tìm kiếm LCA của $a$ và $b$ bằng cách đi lên từ các nút này song song, cho đến khi chúng ta gặp một đỉnh lần thứ hai.
Để đạt hiệu quả, chúng ta chọn một mã định danh duy nhất cho mỗi lần gọi tìm LCA, và đánh dấu các đỉnh đã duyệt bằng nó.
Điều này hoạt động trong $O(1)$, trong khi các cách tiếp cận khác như sử dụng `set` hoạt động kém hơn.
Các đường đi đã qua được lưu trữ trong các vector `path_a` và `path_b`, và chúng ta sử dụng chúng để đi qua chúng một lần nữa đến LCA, do đó có được tất cả các đỉnh của chu trình.
Tất cả các đỉnh của chu trình được nén bằng cách gắn chúng vào LCA, do đó độ phức tạp trung bình là $O(\log n)$ (vì chúng ta không sử dụng Hợp nhất theo hạng).
Tất cả các cạnh chúng ta đi qua đã là cầu, vì vậy chúng ta trừ đi 1 cho mỗi cạnh trong chu trình.

Cuối cùng, hàm truy vấn `add_edge(a, b)` xác định các thành phần liên thông mà các đỉnh $a$ và $b$ nằm trong đó.
Nếu chúng nằm trong các thành phần liên thông khác nhau, thì một cây nhỏ hơn sẽ được thay đổi gốc và sau đó gắn vào cây lớn hơn.
Ngược lại, nếu các đỉnh $a$ và $b$ nằm trong một cây, nhưng trong các thành phần liên thông 2 cạnh khác nhau, thì hàm `merge_path(a, b)` được gọi, hàm này sẽ phát hiện chu trình và nén nó thành một thành phần liên thông 2 cạnh. 

```