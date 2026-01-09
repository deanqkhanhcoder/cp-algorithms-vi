---
tags:
  - Translated
e_maxx_link: strong_connected_components
---

# Thành phần liên thông mạnh và đồ thị nén (Strongly connected components and the condensation graph) {: #strongly-connected-components-and-the-condensation-graph}

## Định nghĩa (Definitions) {: #definitions}

Cho $G=(V,E)$ là một đồ thị có hướng với các đỉnh $V$ và các cạnh $E \subseteq V \times V$. Chúng ta ký hiệu $n=|V|$ là số lượng đỉnh và $m=|E|$ là số lượng cạnh trong $G$. Rất dễ dàng để mở rộng tất cả các định nghĩa trong bài viết này cho đa đồ thị, nhưng chúng ta sẽ không tập trung vào điều đó.

Một tập hợp con các đỉnh $C \subseteq V$ được gọi là một **thành phần liên thông mạnh** nếu các điều kiện sau được thỏa mãn:

- với mọi $u,v\in C$, nếu $u \neq v$ tồn tại một đường đi từ $u$ đến $v$ và một đường đi từ $v$ đến $u$, và
- $C$ là cực đại, theo nghĩa là không có đỉnh nào có thể được thêm vào mà không vi phạm điều kiện trên.

Chúng ta ký hiệu $\text{SCC}(G)$ là tập hợp các thành phần liên thông mạnh của $G$. Các thành phần liên thông mạnh này không giao nhau, và bao phủ tất cả các đỉnh trong đồ thị. Do đó, tập hợp $\text{SCC}(G)$ là một phân hoạch của $V$.

Xem xét đồ thị $G_\text{example}$ này, trong đó các thành phần liên thông mạnh được làm nổi bật:

<center><img src="strongly-connected-components-tikzpicture/graph.svg" alt="drawing" style="width:700px;"/></center>

Ở đây chúng ta có $\text{SCC}(G_\text{example})=\{\{0,7\},\{1,2,3,5,6\},\{4,9\},\{8\}\}.$ Chúng ta có thể xác nhận rằng trong mỗi thành phần liên thông mạnh, tất cả các đỉnh đều có thể truy cập được từ nhau.

Chúng ta định nghĩa **đồ thị nén** (condensation graph) $G^{\text{SCC}}=(V^{\text{SCC}}, E^{\text{SCC}})$ như sau:

- các đỉnh của $G^{\text{SCC}}$ là các thành phần liên thông mạnh của $G$; tức là, $V^{\text{SCC}} = \text{SCC}(G)$, và
- đối với tất cả các đỉnh $C_i,C_j$ của đồ thị nén, có một cạnh từ $C_i$ đến $C_j$ khi và chỉ khi $C_i \neq C_j$ và tồn tại $a\in C_i$ và $b\in C_j$ sao cho có một cạnh từ $a$ đến $b$ trong $G$.

Đồ thị nén của $G_\text{example}$ trông như sau:

<center><img src="strongly-connected-components-tikzpicture/cond_graph.svg" alt="drawing" style="width:600px;"/></center>


Thuộc tính quan trọng nhất của đồ thị nén là nó **không có chu trình** (acyclic). Thật vậy, không có 'vòng tự thân' (self-loops) nào trong đồ thị nén theo định nghĩa, và nếu có một chu trình đi qua hai hoặc nhiều đỉnh (thành phần liên thông mạnh) trong đồ thị nén, thì do tính khả truy, hợp của các thành phần liên thông mạnh này sẽ là một thành phần liên thông mạnh: mâu thuẫn.

Thuật toán được mô tả trong phần tiếp theo tìm tất cả các thành phần liên thông mạnh trong một đồ thị đã cho. Sau đó, đồ thị nén có thể được xây dựng.

## Thuật toán của Kosaraju (Kosaraju's algorithm) {: #kosarajus-algorithm}

### Mô tả thuật toán (Description of the algorithm)

Thuật toán được mô tả đã được đề xuất độc lập bởi Kosaraju và Sharir vào khoảng năm 1980. Nó dựa trên hai loạt [tìm kiếm theo chiều sâu](depth-first-search.md), với thời gian chạy là $O(n + m)$.

Trong bước đầu tiên của thuật toán, chúng ta thực hiện một chuỗi các tìm kiếm theo chiều sâu (`dfs`), thăm toàn bộ đồ thị. Tức là, miễn là vẫn còn các đỉnh chưa được thăm, chúng ta lấy một trong số chúng, và bắt đầu một tìm kiếm theo chiều sâu từ đỉnh đó. Đối với mỗi đỉnh, chúng ta theo dõi *thời gian thoát* (exit time) $t_\text{out}[v]$. Đây là 'dấu thời gian' mà tại đó việc thực thi `dfs` trên đỉnh $v$ kết thúc, tức là thời điểm mà tất cả các đỉnh có thể truy cập từ $v$ đã được thăm và thuật toán quay lại $v$. Bộ đếm dấu thời gian *không* nên được đặt lại giữa các lần gọi liên tiếp đến `dfs`. Thời gian thoát đóng một vai trò quan trọng trong thuật toán, điều này sẽ trở nên rõ ràng khi chúng ta thảo luận về định lý sau.

Đầu tiên, chúng ta định nghĩa thời gian thoát $t_\text{out}[C]$ của một thành phần liên thông mạnh $C$ là giá trị lớn nhất của các giá trị $t_\text{out}[v]$ cho tất cả $v \in C.$ Hơn nữa, trong chứng minh của định lý, chúng ta sẽ đề cập đến *thời gian vào* (entry time) $t_{\text{in}}[v]$ cho mỗi đỉnh $v\in G$. Số $t_{\text{in}}[v]$ đại diện cho 'dấu thời gian' mà tại đó hàm đệ quy `dfs` được gọi trên đỉnh $v$ trong bước đầu tiên của thuật toán. Đối với một thành phần liên thông mạnh $C$, chúng ta định nghĩa $t_{\text{in}}[C]$ là giá trị nhỏ nhất của các giá trị $t_{\text{in}}[v]$ cho tất cả $v \in C$.

!!! info "Định lý"

    Gọi $C$ và $C'$ là hai thành phần liên thông mạnh khác nhau, và giả sử có một cạnh từ $C$ đến $C'$ trong đồ thị nén. Khi đó, $t_\text{out}[C] > t_\text{out}[C']$.

??? note "Chứng minh"

    Có hai trường hợp khác nhau, tùy thuộc vào thành phần nào sẽ được tiếp cận trước bởi tìm kiếm theo chiều sâu:

    - Trường hợp 1: thành phần $C$ được tiếp cận trước (tức là, $t_{\text{in}}[C] < t_{\text{in}}[C']$). Trong trường hợp này, tìm kiếm theo chiều sâu thăm một đỉnh $v \in C$ tại một thời điểm nào đó mà tất cả các đỉnh khác của các thành phần $C$ và $C'$ chưa được thăm. Vì có một cạnh từ $C$ đến $C'$ trong đồ thị nén, không chỉ tất cả các đỉnh khác trong $C$ đều có thể truy cập được từ $v$ trong $G$, mà tất cả các đỉnh trong $C'$ cũng có thể truy cập được. Điều này có nghĩa là việc thực thi `dfs` này, đang chạy từ đỉnh $v$, cũng sẽ thăm tất cả các đỉnh khác của các thành phần $C$ và $C'$ trong tương lai, vì vậy các đỉnh này sẽ là hậu duệ của $v$ trong cây tìm kiếm theo chiều sâu. Điều này ngụ ý rằng đối với mỗi đỉnh $u \in (C \cup C')\setminus \{v\},$ chúng ta có $t_\text{out}[v] > t_\text{out}[u]$. Do đó, $t_\text{out}[C] > t_\text{out}[C']$, hoàn thành trường hợp này của chứng minh.

    - Trường hợp 2: thành phần $C'$ được tiếp cận trước (tức là, $t_{\text{in}}[C] > t_{\text{in}}[C']$). Trong trường hợp này, tìm kiếm theo chiều sâu thăm một đỉnh $v \in C'$ tại một thời điểm nào đó mà tất cả các đỉnh khác của các thành phần $C$ và $C'$ chưa được thăm. Vì có một cạnh từ $C$ đến $C'$ trong đồ thị nén, $C$ không thể tiếp cận được từ $C'$, theo tính chất không có chu trình. Do đó, việc thực thi `dfs` đang chạy từ đỉnh $v$ sẽ không tiếp cận bất kỳ đỉnh nào của $C$, nhưng nó sẽ thăm tất cả các đỉnh của $C'$. Các đỉnh của $C$ sẽ được thăm bởi một số lần thực thi `dfs` sau này trong bước này của thuật toán, vì vậy chúng ta thực sự có $t_\text{out}[C] > t_\text{out}[C']$. Điều này hoàn thành chứng minh.

Định lý đã chứng minh là rất quan trọng để tìm các thành phần liên thông mạnh. Nó có nghĩa là bất kỳ cạnh nào trong đồ thị nén đều đi từ một thành phần có giá trị $t_\text{out}$ lớn hơn đến một thành phần có giá trị nhỏ hơn.

Nếu chúng ta sắp xếp tất cả các đỉnh $v \in V$ theo thứ tự giảm dần của thời gian thoát $t_\text{out}[v]$, thì đỉnh đầu tiên $u$ sẽ thuộc về thành phần liên thông mạnh "gốc", không có cạnh đi vào trong đồ thị nén. Bây giờ chúng ta muốn chạy một loại tìm kiếm nào đó từ đỉnh $u$ này sao cho nó sẽ thăm tất cả các đỉnh trong thành phần liên thông mạnh của nó, nhưng không phải các đỉnh khác. Bằng cách lặp lại việc này, chúng ta có thể dần dần tìm thấy tất cả các thành phần liên thông mạnh: chúng ta loại bỏ tất cả các đỉnh thuộc về thành phần được tìm thấy đầu tiên, sau đó chúng ta tìm đỉnh còn lại tiếp theo với giá trị $t_\text{out}$ lớn nhất, và chạy tìm kiếm này từ nó, và cứ thế. Cuối cùng, chúng ta sẽ tìm thấy tất cả các thành phần liên thông mạnh. Để tìm một phương pháp tìm kiếm hoạt động như chúng ta muốn, chúng ta xem xét định lý sau:

!!! info "Định lý"

    Gọi $G^T$ là *đồ thị chuyển vị* (transpose graph) của $G$, thu được bằng cách đảo ngược hướng cạnh trong $G$. Khi đó, $\text{SCC}(G)=\text{SCC}(G^T)$. Hơn nữa, đồ thị nén của $G^T$ là chuyển vị của đồ thị nén của $G$.

Chứng minh được bỏ qua (nhưng đơn giản). Như một hệ quả của định lý này, sẽ không có cạnh nào từ thành phần "gốc" đến các thành phần khác trong đồ thị nén của $G^T$. Do đó, để thăm toàn bộ thành phần liên thông mạnh "gốc", chứa đỉnh $v$, chúng ta chỉ cần chạy một tìm kiếm theo chiều sâu từ đỉnh $v$ trong đồ thị chuyển vị $G^T$! Điều này sẽ thăm chính xác tất cả các đỉnh của thành phần liên thông mạnh này. Như đã đề cập trước đó, sau đó chúng ta có thể loại bỏ các đỉnh này khỏi đồ thị. Sau đó, chúng ta tìm đỉnh tiếp theo với giá trị cực đại của $t_\text{out}[v]$, và chạy tìm kiếm trong đồ thị chuyển vị bắt đầu từ đỉnh đó để tìm thành phần liên thông mạnh tiếp theo. Lặp lại điều này, chúng ta tìm thấy tất cả các thành phần liên thông mạnh.

Do đó, tóm lại, chúng ta đã thảo luận về thuật toán sau để tìm các thành phần liên thông mạnh:

 - Bước 1. Chạy một chuỗi các tìm kiếm theo chiều sâu trên $G$, sẽ tạo ra một danh sách (ví dụ `order`) các đỉnh, được sắp xếp theo thời gian thoát $t_\text{out}$ tăng dần.

- Bước 2. Xây dựng đồ thị chuyển vị $G^T$, và chạy một loạt các tìm kiếm theo chiều sâu trên các đỉnh theo thứ tự ngược lại (tức là, theo thứ tự giảm dần của thời gian thoát). Mỗi tìm kiếm theo chiều sâu sẽ tạo ra một thành phần liên thông mạnh.

- Bước 3 (tùy chọn). Xây dựng đồ thị nén.

Độ phức tạp thời gian chạy của thuật toán là $O(n + m)$, bởi vì tìm kiếm theo chiều sâu được thực hiện hai lần. Xây dựng đồ thị nén cũng là $O(n+m).$

Cuối cùng, thật thích hợp để đề cập đến [sắp xếp topo](topological-sort.md) ở đây. Trong bước 1, chúng ta tìm các đỉnh theo thứ tự thời gian thoát tăng dần. Nếu $G$ không có chu trình, điều này tương ứng với một sắp xếp topo (ngược) của $G$. Trong bước 2, thuật toán tìm các thành phần liên thông mạnh theo thứ tự giảm dần của thời gian thoát. Do đó, nó tìm các thành phần - các đỉnh của đồ thị nén - theo thứ tự tương ứng với sắp xếp topo của đồ thị nén.

### Cài đặt (Implementation) {: #implementation}
```cpp title="strongly_connected_components"
vector<bool> visited; // theo dõi các đỉnh đã được thăm
 
// chạy tìm kiếm theo chiều sâu bắt đầu tại đỉnh v.
// mỗi đỉnh được thăm được thêm vào vector đầu ra khi dfs rời khỏi nó.
void dfs(int v, vector<vector<int>> const& adj, vector<int> &output) {
    visited[v] = true;
    for (auto u : adj[v])
        if (!visited[u])
            dfs(u, adj, output);
    output.push_back(v);
}
 
// đầu vào: adj -- danh sách kề của G
// đầu ra: components -- các thành phần liên thông mạnh trong G
// đầu ra: adj_cond -- danh sách kề của G^SCC (theo các đỉnh gốc)
void strongly_connected_components(vector<vector<int>> const& adj,
                                  vector<vector<int>> &components,
                                  vector<vector<int>> &adj_cond) {
    int n = adj.size();
    components.clear(), adj_cond.clear();
 
    vector<int> order; // sẽ là danh sách các đỉnh của G được sắp xếp theo thời gian thoát
 
    visited.assign(n, false);
 
    // chuỗi tìm kiếm theo chiều sâu đầu tiên
    for (int i = 0; i < n; i++)
        if (!visited[i])
            dfs(i, adj, order);
 
    // tạo danh sách kề của G^T
    vector<vector<int>> adj_rev(n);
    for (int v = 0; v < n; v++)
        for (int u : adj[v])
            adj_rev[u].push_back(v);
 
    visited.assign(n, false);
    reverse(order.begin(), order.end());
 
    vector<int> roots(n, 0); // cung cấp đỉnh gốc của SCC của một đỉnh
 
    // chuỗi tìm kiếm theo chiều sâu thứ hai
    for (auto v : order)
        if (!visited[v]) {
            std::vector<int> component;
            dfs(v, adj_rev, component);
            components.push_back(component);
            int root = *component.begin();
            for (auto u : component)
                roots[u] = root;
        }
 
    // thêm cạnh vào đồ thị nén
    adj_cond.assign(n, {});
    for (int v = 0; v < n; v++)
        for (auto u : adj[v])
            if (roots[v] != roots[u])
                adj_cond[roots[v]].push_back(roots[u]);
}
```

Hàm `dfs` thực hiện tìm kiếm theo chiều sâu. Nó nhận đầu vào là một danh sách kề và một đỉnh bắt đầu. Nó cũng nhận một tham chiếu đến vector `output`: mỗi đỉnh được thăm sẽ được thêm vào `output` khi `dfs` rời khỏi đỉnh đó.

Lưu ý rằng chúng ta sử dụng hàm `dfs` cả trong bước đầu tiên và bước thứ hai của thuật toán. Trong bước đầu tiên, chúng ta truyền vào danh sách kề của $G$, và trong các lần gọi liên tiếp đến `dfs`, chúng ta tiếp tục truyền vào cùng một 'vector đầu ra' `order`, để cuối cùng chúng ta có được một danh sách các đỉnh theo thứ tự thời gian thoát tăng dần. Trong bước thứ hai, chúng ta truyền vào danh sách kề của $G^T$, và trong mỗi lần gọi, chúng ta truyền vào một 'vector đầu ra' trống `component`, vector này sẽ cung cấp cho chúng ta một thành phần liên thông mạnh tại một thời điểm.

## Thuật toán thành phần liên thông mạnh của Tarjan (Tarjan's strongly connected components algorithm) {: #tarjans-strongly-connected-components-algorithm}

### Mô tả thuật toán (Description of the algorithm)

Thuật toán được mô tả lần đầu tiên được đề xuất bởi Tarjan vào năm 1972.
Nó dựa trên việc thực hiện một chuỗi các cuộc gọi DFS, sử dụng thông tin vốn có trong cấu trúc của nó để xác định các thành phần liên thông mạnh (SCC), với thời gian chạy là $O(n+m)$.

Khi áp dụng DFS trên một đỉnh, chúng ta sẽ duyệt qua danh sách kề của nó, và trong trường hợp chúng ta tìm thấy một đỉnh chưa được thăm, chúng ta sẽ áp dụng đệ quy DFS cho nó.

Hãy xem xét cây được tạo ra bởi chuỗi các cuộc gọi DFS, mà chúng ta sẽ gọi là **cây DFS**.
Khi chúng ta lần đầu tiên gọi một DFS trên một đỉnh từ một SCC, tất cả các đỉnh của SCC đó sẽ được thăm trước khi cuộc gọi này kết thúc, vì tất cả chúng đều có thể truy cập được từ nhau.
Trong cây DFS, đỉnh đầu tiên này sẽ là tổ tiên chung cho tất cả các đỉnh khác của SCC; chúng ta định nghĩa đỉnh này là **gốc của SCC**.

!!! info "Định lý"

    Tất cả các đỉnh của một SCC tạo ra một đồ thị con liên thông của cây DFS.

??? note "Chứng minh"

    Chúng ta đã xác định rằng tất cả các đỉnh của một SCC có một tổ tiên chung, đỉnh đầu tiên được thăm bởi một cuộc gọi DFS.
    Hãy xem xét một đỉnh $v$ và gốc của nó, đỉnh $r$.
    Tất cả các đỉnh trong đường đi từ $r$ đến $v$ thuộc về cùng một SCC. Tất cả các đỉnh này đều có thể truy cập được từ $r$, và tất cả chúng đều tiếp cận được $v$, và vì theo định nghĩa $v$ tiếp cận $r$, tất cả các đỉnh này đều tiếp cận được nhau.
    Vì tất cả các đường đi từ một gốc đến mọi đỉnh khác của SCC thuộc về cùng một SCC, đồ thị con được hình thành là liên thông.

Lưu ý rằng các SCC chia tách cây DFS hoàn hảo thành các đồ thị con liên thông.

Ý tưởng của thuật toán sau đó là như sau:

- Chúng ta thực hiện một chuỗi các cuộc gọi DFS, áp dụng đệ quy chúng cho các đỉnh của danh sách kề.

- Khi chúng ta kết thúc việc duyệt danh sách kề của một đỉnh, chúng ta bằng cách nào đó có thể xác định xem nó có phải là gốc hay không.
Phương pháp này sẽ được giải thích sau.

- Trong trường hợp đỉnh là gốc, chúng ta sau đó sẽ ngay lập tức tìm và xác nhận tất cả các đỉnh của SCC của nó.

Khi tất cả các cuộc gọi kết thúc, tất cả các gốc sẽ được phát hiện và tất cả các đỉnh sẽ được xác nhận là một phần của một số SCC.

Bây giờ chúng ta hãy phân tích các tính chất của DFS khi quy trình xác nhận này được giới thiệu.

!!! info "Định lý"

    Hãy xem xét đỉnh $v$ và giả sử chúng ta vừa hoàn thành việc duyệt danh sách kề của nó.
    Tất cả các đỉnh chưa được xác nhận trong cây con của nó thuộc về cùng một SCC.

??? note "Chứng minh"

    Thuật toán sẽ xác nhận các đỉnh của một SCC khi gốc của nó được tìm thấy.
    Vì danh sách kề của $v$ đã được duyệt, tất cả các cuộc gọi DFS trên cây con của nó đã kết thúc, các gốc đã được phát hiện và các đỉnh thuộc về SCC của chúng đã được xác nhận.
    Gốc của các đỉnh chưa được xác nhận còn lại sẽ là một tổ tiên có quy trình xác nhận chưa được thực thi, vì vậy nó là $v$ hoặc một tổ tiên của $v$.
    Vì $v$ nằm trong đường đi từ tất cả các đỉnh đến gốc của chúng và các SCC phải tạo ra một đồ thị con liên thông của cây, cả $v$ và tất cả các đỉnh còn lại thuộc về cùng một SCC.

!!! info "Định lý"

    Hãy xem xét đỉnh $v$ và giả sử chúng ta đang duyệt danh sách kề của nó, hiện đang xử lý cạnh $(v, u)$.
    Nếu $u$ đã được thăm bởi một số cuộc gọi DFS và vẫn chưa được xác nhận, $v$ và $u$ thuộc về cùng một SCC.

??? note "Chứng minh"

    Có các trường hợp khác nhau tùy thuộc vào loại cạnh:

    - Cạnh cây (Tree-edge): nếu đây là một cạnh cây, đây là lần đầu tiên chúng ta tìm thấy đỉnh $u$. Điều này có nghĩa là trước tiên chúng ta phải áp dụng đệ quy cuộc gọi DFS trên $u$ và xem xét nó sau khi cuộc gọi DFS của nó đã kết thúc. Nếu đỉnh $u$ vẫn chưa được xác nhận, gốc của nó là $v$ hoặc một tổ tiên của $v$, vì vậy chúng phải thuộc về cùng một SCC.

    - Cạnh ngược (Back-edge): đây là trường hợp đơn giản hơn, nếu $u$ là tổ tiên của $v$, chúng có thể truy cập được từ nhau và theo định nghĩa thuộc về cùng một SCC.

    - Cạnh tiến (Forward-edge): trước khi cạnh này được xử lý, đã có một chuỗi các cuộc gọi DFS kết thúc mà không tìm thấy gốc của $u$, đã quay trở lại $v$ mà cuộc gọi DFS của nó đã tiếp tục.
    Gốc của $u$ sau đó sẽ là một tổ tiên mà quy trình xác nhận của nó chưa được thực thi, vì vậy nó là $v$ hoặc một tổ tiên của $v$, vì vậy chúng phải thuộc về cùng một SCC.

    - Cạnh chéo (Cross-edge): tương tự, trước khi cạnh này được xử lý, đã có một chuỗi các cuộc gọi DFS kết thúc mà không tìm thấy gốc của $u$, đã quay trở lại một tổ tiên chung của $u$ và $v$ mà cuộc gọi DFS của nó đã tiếp tục và bắt đầu một chuỗi các cuộc gọi DFS mới dẫn đến một cuộc gọi trên $v$.
    Gốc của $u$ sau đó sẽ là một tổ tiên mà quy trình xác nhận của nó chưa được thực thi, và tất cả các ứng cử viên có thể là tổ tiên chung với $v$.
    Vì gốc của $u$ là tổ tiên của $v$, nó tiếp cận $v$, và vì $v$ bây giờ tiếp cận $u$, chúng phải thuộc về cùng một SCC.

Lưu ý, khi hai đỉnh thuộc về cùng một thành phần, gốc của chúng phải là một tổ tiên chung của cả hai đỉnh.

!!! info "Định lý"

    Cho $v$ là một đỉnh. Các phát biểu sau là tương đương:

    1. Một số đỉnh trong cây con của $v$ tiếp cận một đỉnh chưa được xác nhận bên ngoài cây con.
    2. $v$ không phải là gốc của một SCC.

??? note "Chứng minh"

    - $1. \implies 2.$:
    Giả sử một số đỉnh $u$ trong cây con của $v$ tiếp cận một đỉnh chưa được xác nhận $w$ bên ngoài cây con.
    Chúng ta đã thiết lập rằng $u$ và $w$ thuộc về cùng một SCC và gốc của chúng phải là một tổ tiên chung cho cả hai.
    Tổ tiên chung này nhất thiết phải ở bên ngoài cây con, và nó cũng sẽ là tổ tiên của $v$.
    Vì $v$ nằm trong đường đi từ gốc đến $u$, nó phải thuộc về cùng một SCC, gốc của nó không phải là $v$.

    - $\neg 1. \implies \neg 2.$:
    Giả sử không có đỉnh nào trong cây con của $v$ tiếp cận một đỉnh chưa được xác nhận bên ngoài cây con.
    Điều này có nghĩa là không có đỉnh nào trong cây con của $v$ tiếp cận một tổ tiên của $v$.
    Các cạnh duy nhất có thể đến các đỉnh bên ngoài cây con là các cạnh chéo đến các đỉnh đã được xác nhận;
    các đỉnh này không thể tiếp cận một tổ tiên của $v$, vì nếu chúng làm vậy, chúng sẽ thuộc về cùng một SCC như $v$, điều này là không thể vì SCC của chúng đã được xác định.
    Vì không có tổ tiên nào của $v$ có thể truy cập được từ cây con của nó, gốc của $v$ phải là chính $v$.

Bây giờ, chúng ta phải tìm phương pháp cho phép chúng ta xác định xem một đỉnh có phải là gốc hay không, và các thuộc tính quy trình xác nhận là cần thiết cho sự chính xác của nó.
Để đạt được mục đích này, chúng ta định nghĩa thời gian vào $t_{in}[v]$ cho mỗi đỉnh $v \in G$ tương ứng với 'dấu thời gian' mà tại đó DFS được gọi trên $v$.
Theo định nghĩa, gốc là đỉnh đầu tiên của một SCC được DFS thăm nên nó sẽ có giá trị $t_{in}$ nhỏ nhất của SCC của nó.

Gọi $v$ là một đỉnh và hãy xem xét cây con của nó.
Tại thời điểm chúng ta kết thúc việc duyệt danh sách kề của nó, bất kỳ đỉnh nào đã được DFS thăm bên ngoài cây con sẽ có giá trị $t_{in}$ nhỏ hơn, vì DFS đã được gọi lần đầu tiên trên chúng trước khi nó bắt đầu trên $v$.

Khi xem xét quy trình xác nhận, giá trị $t_{in}$ của tất cả các đỉnh chưa được xác nhận bên ngoài cây con của $v$ nhỏ hơn $t_{in}[v]$.
Bây giờ chúng ta có thể thấy cách sử dụng $t_{in}$ để xác định các gốc.
Chúng ta xem xét giá trị nhỏ nhất của $t_{in}$ của các đỉnh chưa được xác nhận mà chúng ta có thể tiếp cận và chúng ta truyền thông tin này đến các tổ tiên thông qua các cạnh cây.
Chúng ta sẽ gọi giá trị được truyền là $t_{low}$.

Chính thức hơn, chúng ta định nghĩa $t_{low}[v]$ là giá trị thấp nhất của $t_{in}$ mà một đỉnh trong cây con của $v$ có thể tiếp cận thông qua một cạnh trực tiếp.
Do đó, chúng ta có thể phát hiện xem một đỉnh $v$ có phải là gốc hay không bằng cách kiểm tra xem $t_{low}[v] < t_{in}[v]$.

Cuối cùng, để xác nhận các đỉnh, có nhiều cách để thực hiện, chẳng hạn như một thuật toán duyệt đồ thị khác, nhưng cũng có thể sử dụng một cấu trúc dữ liệu đơn giản để theo dõi các đỉnh chưa được xác nhận.
Để xác định cấu trúc dữ liệu từ các nguyên tắc đầu tiên, hãy đi qua các phương thức mà nó phải thực hiện, chỉ có hai:

- Khi chúng ta lần đầu tiên thăm một đỉnh, chúng ta chỉ cần chèn nó vào cấu trúc dữ liệu, vì đỉnh này chưa được xác nhận.

- Khi chúng ta tìm thấy một gốc, chúng ta phải tìm tất cả các đỉnh chưa được xác nhận còn lại trong cây con của nó và loại bỏ chúng khỏi cấu trúc dữ liệu.

Chúng ta có thể tìm một cách thay thế để mô tả thao tác loại bỏ bằng cách nhận thấy rằng ngay sau khi duyệt danh sách kề của một đỉnh $v$, tất cả các đỉnh được đặt trong cấu trúc dữ liệu sau $v$ đều thuộc về cây con của nó.
Nếu $v$ là gốc, tất cả các đỉnh còn lại được chèn sau $v$ phải được loại bỏ.
Vì vậy, thao tác loại bỏ thay vào đó có thể được mô tả là:

- Khi chúng ta tìm thấy một gốc, chúng ta phải tìm và loại bỏ tất cả các đỉnh còn lại được chèn sau nó.

Bây giờ chúng ta có thể thấy rằng điều này có thể được thực hiện với một ngăn xếp (stack):

- Khi chúng ta lần đầu tiên thăm một đỉnh, chúng ta đẩy nó vào ngăn xếp.

- Khi chúng ta tìm thấy một gốc, chúng ta lấy ra tất cả các phần tử cho đến khi chúng ta lấy ra chính gốc đó.

Điều này cuối cùng cho phép chúng ta cài đặt thuật toán.

Độ phức tạp thời gian chạy của chuỗi các cuộc gọi DFS là $O(n + m)$.
Xem xét ngăn xếp, độ phức tạp của nó khấu hao thành $O(n)$ vì mỗi nút chỉ được đẩy và lấy ra một lần.
Do đó, tổng độ phức tạp thời gian chạy là $O(n + m)$.

Như một nhận xét bổ sung, các gốc được tìm thấy theo thứ tự topo ngược.
Trong thuật toán, đỉnh là gốc nếu không có cạnh nào đến các đỉnh chưa được xác nhận bên ngoài cây con của nó, nghĩa là tất cả các thành phần có thể truy cập khác đều nằm trong cây con của nó (và do đó gốc của chúng đã được tìm thấy) hoặc chúng kết nối với các đỉnh đã được xác nhận bên ngoài cây con (mà gốc của chúng cũng đã được tìm thấy).
Vì vậy, tất cả các thành phần có thể truy cập đã được tìm thấy, nghĩa là chúng được giới thiệu theo thứ tự topo ngược hợp lệ của đồ thị nén.

### Cài đặt (Implementation) {: #implementation}
```cpp title="tarjan_scc"
vector<int> st;    // - ngăn xếp chứa các đỉnh chưa được xác nhận
vector<int> roots; // - theo dõi các gốc SCC của các đỉnh
int timer;         // - bộ đếm dấu thời gian dfs
vector<int> t_in;  // - theo dõi dấu thời gian dfs của các đỉnh
vector<int> t_low; // - theo dõi t_in thấp nhất của các đỉnh chưa được xác nhận
                   // có thể truy cập trong cây con
 
// thực hiện thuật toán tarjan cho các thành phần liên thông mạnh
void dfs(int v, vector<vector<int>> const &adj, vector<vector<int>> &components) {
 
  t_low[v] = t_in[v] = timer++;
  st.push_back(v);
 
  for (auto u : adj[v]) {
    if (t_in[u] == -1) { // tree-edge
      dfs(u, adj, components);
      t_low[v] = min(t_low[v], t_low[u]);
    } else if (roots[u] == -1) { // back-edge, cross-edge hoặc forward-edge đến một đỉnh chưa được xác nhận
      t_low[v] = min(t_low[v], t_in[u]);
    }
  }
 
  if (t_low[v] == t_in[v]) { // đỉnh là một gốc
    components.push_back({v}); // khởi tạo một thành phần mới với gốc v
    while (true) {
      int u = st.back();
      st.pop_back();
      roots[u] = v; // xác nhận đỉnh
      if (u == v)
        break;
      components.back().push_back(u); // thêm đỉnh u vào thành phần của v
    }
  }
}
 
// đầu vào: adj -- danh sách kề của G
// đầu ra: components -- các thành phần liên thông mạnh trong G
// đầu ra: adj_cond -- danh sách kề của G^SCC (theo các đỉnh gốc)
void strongly_connected_components(vector<vector<int>> const &adj,
                                   vector<vector<int>> &components,
                                   vector<vector<int>> &adj_cond) {
  components.clear();
  adj_cond.clear();
 
  int n = adj.size();
 
  st.clear();
  roots.assign(n, -1);
  timer = 0;
  t_in.assign(n, -1);
  t_low.assign(n, -1);
 
  // áp dụng thuật toán tarjan cho tất cả các đỉnh
  // thêm các đỉnh vào các thành phần theo thứ tự topo ngược
  for (int v = 0; v < n; v++) {
    if (t_in[v] == -1) {
      dfs(v, adj, components);
    }
  }
 
  // thêm các cạnh vào đồ thị nén
  adj_cond.assign(n, {});
  for (int v = 0; v < n; v++) {
    for (auto u : adj[v])
      if (roots[v] != roots[u])
        adj_cond[roots[v]].push_back(roots[u]);
  }
}
```

Chúng tôi có một [bài nộp được chấp nhận](https://judge.yosupo.jp/submission/334251) với mã này trong Thư viện Kiểm tra (Library Checker).

Như một nhận xét cuối cùng, có một cách thay thế để lặp qua danh sách kề.
Hiện tại, chúng ta đang thực hiện như sau:

```c++
for (auto u : adj[v]) {
  if (t_in[u] == -1) { // tree-edge
    dfs(u, adj);
    t_low[v] = min(t_low[v], t_low[u]);
  } else if (roots[u] == -1) { // back-edge, cross-edge hoặc forward-edge đến một đỉnh chưa được xác nhận
    t_low[v] = min(t_low[v], t_in[u]);
  }
}
```

Ngoài ra, chúng ta có thể làm:

```c++
for (auto u : adj[v]) {
  if (t_in[u] == -1) // đỉnh chưa được thăm
    dfs(u, adj);
  if (roots[u] == -1) // đỉnh chưa được xác nhận
    t_low[v] = min(t_low[v], t_low[u]);
}
```

$t_{low}$ được sử dụng để truyền thông tin đến gốc, và khi chúng ta thực hiện `t_low[v] = min(t_low[v], t_in[u])`, chúng ta biết rằng $u$ và $v$ thuộc về cùng một SCC.
Nếu $t_{low}[u]$ được truyền cho đến gốc của $u$, nó cũng có thể được truyền qua $v$ vì gốc là giống nhau.
Vì $t_{low}[u] \leq t_{in}[u]$, điều này không gây ra bất kỳ xung đột nào, thay vào đó chỉ cải thiện giới hạn trên gốc của $v$.

## Xây dựng Đồ thị Nén (Building the Condensation Graph) {: #building-the-condensation-graph}

Khi xây dựng danh sách kề của đồ thị nén, chúng ta chọn *gốc* của mỗi thành phần làm đỉnh đầu tiên trong danh sách các đỉnh của nó (đây là một lựa chọn tùy ý). Đỉnh gốc này đại diện cho toàn bộ SCC của nó. Đối với mỗi đỉnh `v`, giá trị `roots[v]` chỉ ra đỉnh gốc của SCC mà `v` thuộc về.

Đồ thị nén của chúng ta bây giờ được đưa ra bởi các đỉnh `components` (một thành phần liên thông mạnh tương ứng với một đỉnh trong đồ thị nén), và danh sách kề được đưa ra bởi `adj_cond`, chỉ sử dụng các đỉnh gốc của các thành phần liên thông mạnh. Lưu ý rằng chúng ta tạo một cạnh từ $C$ đến $C'$ trong $G^\text{SCC}$ cho mỗi cạnh từ một số $a\in C$ đến một số $b\in C'$ trong $G$ (nếu $C\neq C'$). Điều này ngụ ý rằng trong cài đặt của chúng ta, chúng ta có thể có nhiều cạnh giữa hai thành phần trong đồ thị nén.

## Tài liệu (Literature) {: #literature}

* Thomas Cormen, Charles Leiserson, Ronald Rivest, Clifford Stein. Introduction to Algorithms [2005].
* M. Sharir. A strong-connectivity algorithm and its applications in data-flow analysis [1979].
* Robert Tarjan. Depth-first search and linear graph algorithms [1972].

## Bài tập (Practice Problems) {: #practice-problems}

* [SPOJ - Good Travels](http://www.spoj.com/problems/GOODA/)
* [SPOJ - Lego](http://www.spoj.com/problems/LEGO/)
* [Codechef - Chef and Round Run](https://www.codechef.com/AUG16/problems/CHEFRRUN)
* [UVA - 11838 - Come and Go](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2938)
* [UVA 247 - Calling Circles](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=183)
* [UVA 13057 - Prove Them All](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=4955)
* [UVA 12645 - Water Supply](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=4393)
* [UVA 11770 - Lighting Away](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2870)
* [UVA 12926 - Trouble in Terrorist Town](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=862&page=show_problem&problem=4805)
* [UVA 11324 - The Largest Clique](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2299)
* [UVA 11709 - Trust groups](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2756)
* [UVA 12745 - Wishmaster](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=4598)
* [SPOJ - True Friends](http://www.spoj.com/problems/TFRIENDS/)
* [SPOJ - Capital City](http://www.spoj.com/problems/CAPCITY/)
* [Codeforces - Scheme](http://codeforces.com/contest/22/problem/E)
* [SPOJ - Ada and Panels](http://www.spoj.com/problems/ADAPANEL/)
* [CSES - Flight Routes Check](https://cses.fi/problemset/task/1682)
* [CSES - Planets and Kingdoms](https://cses.fi/problemset/task/1683)
* [CSES - Coin Collector](https://cses.fi/problemset/task/1686)
* [Codeforces - Checkposts](https://codeforces.com/problemset/problem/427/C)
