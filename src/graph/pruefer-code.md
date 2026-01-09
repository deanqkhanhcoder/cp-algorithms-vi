---
tags:
  - Translated
e_maxx_link: prufer_code_cayley_formula
---

# Mã Prüfer (Prüfer code) {: #prufer-code}

Trong bài viết này, chúng ta sẽ tìm hiểu về cái gọi là **mã Prüfer** (hoặc chuỗi Prüfer), một cách mã hóa một cây có nhãn thành một dãy số theo một cách duy nhất.

Với sự trợ giúp của mã Prüfer, chúng ta sẽ chứng minh **Công thức Cayley** (xác định số lượng cây khung trong một đồ thị đầy đủ).
Chúng tôi cũng chỉ ra giải pháp cho bài toán đếm số cách thêm các cạnh vào một đồ thị để làm cho nó liên thông.

**Lưu ý**, chúng tôi sẽ không xem xét các cây bao gồm một đỉnh duy nhất - đây là một trường hợp đặc biệt mà nhiều phát biểu bị xung đột.

## Mã Prüfer (Prüfer code) {: #pruefer-code}

Mã Prüfer là một cách mã hóa một cây có nhãn với $n$ đỉnh bằng cách sử dụng một dãy gồm $n - 2$ số nguyên trong khoảng $[0; n-1]$.
Cách mã hóa này cũng hoạt động như một **song ánh** (bijection) giữa tất cả các cây khung của một đồ thị đầy đủ và các dãy số.

Mặc dù sử dụng mã Prüfer để lưu trữ và thao tác trên cây là không thực tế do đặc điểm kỹ thuật của biểu diễn, mã Prüfer được sử dụng thường xuyên: chủ yếu trong việc giải quyết các bài toán tổ hợp.

Người phát minh - Heinz Prüfer - đã đề xuất mã này vào năm 1918 như một chứng minh cho công thức Cayley.

### Xây dựng mã Prüfer cho một cây đã cho (Building the Prüfer code for a given tree)

Mã Prüfer được xây dựng như sau.
Chúng ta sẽ lặp lại quy trình sau $n - 2$ lần:
chúng ta chọn lá của cây có số nhỏ nhất, loại bỏ nó khỏi cây và ghi lại số của đỉnh đã được kết nối với nó.
Sau $n - 2$ lần lặp sẽ chỉ còn lại $2$ đỉnh, và thuật toán kết thúc.

Do đó, mã Prüfer cho một cây đã cho là một dãy gồm $n - 2$ số, trong đó mỗi số là số của đỉnh được kết nối, tức là số này nằm trong khoảng $[0, n-1]$.

Thuật toán tính toán mã Prüfer có thể được cài đặt dễ dàng với độ phức tạp thời gian $O(n \log n)$, đơn giản bằng cách sử dụng cấu trúc dữ liệu để trích xuất giá trị nhỏ nhất (ví dụ: `set` hoặc `priority_queue` trong C++), chứa danh sách tất cả các lá hiện tại.
```cpp title="pruefer_code_slow"
vector<vector<int>> adj;

vector<int> pruefer_code() {
    int n = adj.size();
    set<int> leafs;
    vector<int> degree(n);
    vector<bool> killed(n, false);
    for (int i = 0; i < n; i++) {
        degree[i] = adj[i].size();
        if (degree[i] == 1)
            leafs.insert(i);
    }

    vector<int> code(n - 2);
    for (int i = 0; i < n - 2; i++) {
        int leaf = *leafs.begin();
        leafs.erase(leafs.begin());
        killed[leaf] = true;

        int v;
        for (int u : adj[leaf]) {
            if (!killed[u])
                v = u;
        }

        code[i] = v;
        if (--degree[v] == 1)
            leafs.insert(v);
    }

    return code;
}
```

Tuy nhiên, việc xây dựng cũng có thể được thực hiện trong thời gian tuyến tính.
Cách tiếp cận như vậy được mô tả trong phần tiếp theo.

### Xây dựng mã Prüfer cho một cây đã cho trong thời gian tuyến tính (Building the Prüfer code for a given tree in linear time)

Bản chất của thuật toán là sử dụng một **con trỏ di chuyển**, con trỏ này sẽ luôn trỏ đến đỉnh lá hiện tại mà chúng ta muốn loại bỏ.

Thoạt nhìn điều này có vẻ không thể, bởi vì trong quá trình xây dựng mã Prüfer, số lá có thể tăng và giảm.
Tuy nhiên, sau khi xem xét kỹ hơn, điều này thực sự không đúng.
Số lượng lá sẽ không tăng. Số lượng giảm đi một (chúng ta loại bỏ một đỉnh lá và không nhận được đỉnh mới nào), hoặc giữ nguyên (chúng ta loại bỏ một đỉnh lá và nhận được một đỉnh khác).
Trong trường hợp đầu tiên, không có cách nào khác ngoài việc tìm kiếm đỉnh lá nhỏ nhất tiếp theo.
Tuy nhiên, trong trường hợp thứ hai, chúng ta có thể quyết định trong thời gian $O(1)$, liệu chúng ta có thể tiếp tục sử dụng đỉnh đã trở thành đỉnh lá mới hay không, hay chúng ta phải tìm kiếm đỉnh lá nhỏ nhất tiếp theo.
Và trong khá nhiều lần chúng ta có thể tiếp tục với đỉnh lá mới.

Để làm điều này, chúng ta sẽ sử dụng một biến $\text{ptr}$, biến này sẽ chỉ ra rằng trong tập hợp các đỉnh giữa $0$ và $\text{ptr}$ tối đa có một đỉnh lá, cụ thể là đỉnh hiện tại.
Tất cả các đỉnh khác trong phạm vi đó hoặc đã bị loại bỏ khỏi cây, hoặc vẫn có nhiều hơn một đỉnh kề.
Đồng thời chúng ta cũng nói rằng, chúng ta chưa loại bỏ bất kỳ đỉnh lá nào lớn hơn $\text{ptr}$.

Biến này đã rất hữu ích trong trường hợp đầu tiên.
Sau khi loại bỏ nút lá hiện tại, chúng ta biết rằng không thể có một nút lá giữa $0$ và $\text{ptr}$, do đó chúng ta có thể bắt đầu tìm kiếm nút tiếp theo trực tiếp tại $\text{ptr} + 1$, và chúng ta không phải bắt đầu tìm kiếm lại tại đỉnh $0$.
Và trong trường hợp thứ hai, chúng ta có thể phân biệt thêm hai trường hợp:
Hoặc đỉnh lá mới nhận được nhỏ hơn $\text{ptr}$, thì đây phải là đỉnh lá tiếp theo, vì chúng ta biết rằng không có đỉnh nào khác nhỏ hơn $\text{ptr}$.
Hoặc đỉnh lá mới nhận được lớn hơn.
Nhưng sau đó chúng ta cũng biết rằng nó phải lớn hơn $\text{ptr}$, và có thể bắt đầu tìm kiếm lại tại $\text{ptr} + 1$.

Mặc dù chúng ta có thể phải thực hiện nhiều tìm kiếm tuyến tính cho đỉnh lá tiếp theo, con trỏ $\text{ptr}$ chỉ tăng lên và do đó tổng độ phức tạp thời gian là $O(n)$.
```cpp title="pruefer_code_fast"
vector<vector<int>> adj;
vector<int> parent;

void dfs(int v) {
    for (int u : adj[v]) {
        if (u != parent[v]) {
            parent[u] = v;
            dfs(u);
        }
    }
}

vector<int> pruefer_code() {
    int n = adj.size();
    parent.resize(n);
    parent[n-1] = -1;
    dfs(n-1);

    int ptr = -1;
    vector<int> degree(n);
    for (int i = 0; i < n; i++) {
        degree[i] = adj[i].size();
        if (degree[i] == 1 && ptr == -1)
            ptr = i;
    }

    vector<int> code(n - 2);
    int leaf = ptr;
    for (int i = 0; i < n - 2; i++) {
        int next = parent[leaf];
        code[i] = next;
        if (--degree[next] == 1 && next < ptr) {
            leaf = next;
        } else {
            ptr++;
            while (degree[ptr] != 1)
                ptr++;
            leaf = ptr;
        }
    }

    return code;
}
```

Trong mã, trước tiên chúng ta tìm tổ tiên `parent[i]` cho mỗi đỉnh, tức là tổ tiên mà đỉnh này sẽ có khi chúng ta loại bỏ nó khỏi cây.
Chúng ta có thể tìm thấy tổ tiên này bằng cách chọn gốc cây tại đỉnh $n-1$.
Điều này là có thể vì đỉnh $n-1$ sẽ không bao giờ bị xóa khỏi cây.
Chúng ta cũng tính toán bậc cho mỗi đỉnh.
`ptr` là con trỏ chỉ ra kích thước tối thiểu của các đỉnh lá còn lại (ngoại trừ đỉnh hiện tại `leaf`).
Chúng ta sẽ gán đỉnh lá hiện tại bằng `next`, nếu đỉnh này cũng là đỉnh lá và nó nhỏ hơn `ptr`, hoặc chúng ta bắt đầu tìm kiếm tuyến tính cho đỉnh lá nhỏ nhất bằng cách tăng con trỏ.

Có thể dễ dàng thấy rằng, mã này có độ phức tạp $O(n)$.

### Một số tính chất của mã Prüfer (Some properties of the Prüfer code) {: #some-properties-of-the-pruefer-code}

- Sau khi xây dựng mã Prüfer, hai đỉnh sẽ còn lại.
  Một trong số chúng là đỉnh cao nhất $n-1$, nhưng không thể nói gì khác về đỉnh còn lại.
- Mỗi đỉnh xuất hiện trong mã Prüfer chính xác một số lần cố định - bậc của nó trừ đi một.
  Điều này có thể được kiểm tra dễ dàng, vì bậc sẽ nhỏ hơn mỗi lần chúng ta ghi lại nhãn của nó trong mã, và chúng ta loại bỏ nó khi bậc là $1$.
  Đối với hai đỉnh còn lại, thực tế này cũng đúng.

### Khôi phục cây bằng mã Prüfer (Restoring the tree using the Prüfer code) {: #restoring-the-tree-using-the-pruefer-code}

Để khôi phục cây, chỉ cần tập trung vào thuộc tính được thảo luận trong phần trước.
Chúng ta đã biết bậc của tất cả các đỉnh trong cây mong muốn.
Do đó, chúng ta có thể tìm thấy tất cả các đỉnh lá, và cả lá đầu tiên bị loại bỏ trong bước đầu tiên (nó phải là lá nhỏ nhất).
Đỉnh lá này được kết nối với đỉnh tương ứng với số trong ô đầu tiên của mã Prüfer.

Do đó, chúng ta đã tìm thấy cạnh đầu tiên bị loại bỏ bởi khi đó mã Prüfer được tạo ra.
Chúng ta có thể thêm cạnh này vào câu trả lời và giảm bậc ở cả hai đầu của cạnh.

Chúng ta sẽ lặp lại thao tác này cho đến khi chúng ta sử dụng hết tất cả các số của mã Prüfer:
chúng ta tìm đỉnh nhỏ nhất có bậc bằng $1$, kết nối nó với đỉnh tiếp theo từ mã Prüfer, và giảm bậc.

Cuối cùng chúng ta chỉ còn lại hai đỉnh có bậc bằng $1$.
Đây là những đỉnh không bị loại bỏ bởi quy trình mã Prüfer.
Chúng ta kết nối chúng để có được cạnh cuối cùng của cây.
Một trong số chúng sẽ luôn là đỉnh $n-1$.

Thuật toán này có thể được **cài đặt** dễ dàng trong $O(n \log n)$: chúng ta sử dụng cấu trúc dữ liệu hỗ trợ trích xuất giá trị nhỏ nhất (ví dụ: `set<>` hoặc `priority_queue<>` trong C++) để lưu trữ tất cả các đỉnh lá.

Cài đặt sau đây trả về danh sách các cạnh tương ứng với cây.
```cpp title="pruefer_decode_slow"
vector<pair<int, int>> pruefer_decode(vector<int> const& code) {
    int n = code.size() + 2;
    vector<int> degree(n, 1);
    for (int i : code)
        degree[i]++;

    set<int> leaves;
    for (int i = 0; i < n; i++) {
        if (degree[i] == 1)
            leaves.insert(i);
    }

    vector<pair<int, int>> edges;
    for (int v : code) {
        int leaf = *leaves.begin();
        leaves.erase(leaves.begin());

        edges.emplace_back(leaf, v);
        if (--degree[v] == 1)
            leaves.insert(v);
    }
    edges.emplace_back(*leaves.begin(), n-1);
    return edges;
}
```

### Khôi phục cây bằng mã Prüfer trong thời gian tuyến tính (Restoring the tree using the Prüfer code in linear time) {: #restoring-the-tree-using-the-pruefer-code-in-linear-time}

Để có được cây trong thời gian tuyến tính, chúng ta có thể áp dụng kỹ thuật tương tự được sử dụng để lấy mã Prüfer trong thời gian tuyến tính.

Chúng ta không cần cấu trúc dữ liệu để trích xuất giá trị nhỏ nhất.
Thay vào đó, chúng ta có thể nhận thấy rằng, sau khi xử lý cạnh hiện tại, chỉ có một đỉnh trở thành lá.
Do đó, chúng ta có thể tiếp tục với đỉnh này, hoặc chúng ta tìm một đỉnh nhỏ hơn bằng tìm kiếm tuyến tính bằng cách di chuyển một con trỏ.
```cpp title="pruefer_decode_fast"
vector<pair<int, int>> pruefer_decode(vector<int> const& code) {
    int n = code.size() + 2;
    vector<int> degree(n, 1);
    for (int i : code)
        degree[i]++;

    int ptr = 0;
    while (degree[ptr] != 1)
        ptr++;
    int leaf = ptr;

    vector<pair<int, int>> edges;
    for (int v : code) {
        edges.emplace_back(leaf, v);
        if (--degree[v] == 1 && v < ptr) {
            leaf = v;
        } else {
            ptr++;
            while (degree[ptr] != 1)
                ptr++;
            leaf = ptr;
        }
    }
    edges.emplace_back(leaf, n-1);
    return edges;
}
```

### Song ánh giữa cây và mã Prüfer (Bijection between trees and Prüfer codes) {: #bijection-between-trees-and-pruefer-codes}

Đối với mỗi cây, tồn tại một mã Prüfer tương ứng với nó.
Và đối với mỗi mã Prüfer, chúng ta có thể khôi phục cây ban đầu.

Điều đó đi theo việc mỗi mã Prüfer (tức là một dãy gồm $n-2$ số trong khoảng $[0; n - 1]$) cũng tương ứng với một cây.

Do đó tất cả các cây và tất cả các mã Prüfer tạo thành một song ánh (một **sự tương ứng 1-1**).

## Công thức Cayley (Cayley's formula) {: #cayleys-formula}

Công thức Cayley nói rằng **số lượng cây khung trong một đồ thị đầy đủ có nhãn** với $n$ đỉnh bằng:

$$n^{n-2}$$

Có nhiều chứng minh cho công thức này.
Sử dụng khái niệm mã Prüfer, phát biểu này đến mà không có bất kỳ sự ngạc nhiên nào.

Trên thực tế, bất kỳ mã Prüfer nào với $n-2$ số từ khoảng $[0; n-1]$ tương ứng với một cây nào đó với $n$ đỉnh.
Vì vậy, chúng ta có $n^{n-2}$ mã Prüfer khác nhau như vậy.
Vì mỗi cây như vậy là một cây khung của một đồ thị đầy đủ với $n$ đỉnh, số lượng cây khung như vậy cũng là $n^{n-2}$.

## Số cách để làm cho đồ thị liên thông (Number of ways to make a graph connected) {: #number-of-ways-to-make-a-graph-connected}

Khái niệm về mã Prüfer thậm chí còn mạnh mẽ hơn.
Nó cho phép tạo ra nhiều công thức tổng quát hơn so với công thức Cayley.

Trong bài toán này, chúng ta được cho một đồ thị với $n$ đỉnh và $m$ cạnh.
Đồ thị hiện có $k$ thành phần.
Chúng ta muốn tính số cách thêm $k-1$ cạnh sao cho đồ thị trở nên liên thông (rõ ràng $k-1$ là số lượng tối thiểu cần thiết để làm cho đồ thị liên thông).

Hãy để chúng tôi tìm ra một công thức để giải quyết bài toán này.

Chúng ta sử dụng $s_1, \dots, s_k$ cho kích thước của các thành phần liên thông trong đồ thị.
Chúng ta không thể thêm các cạnh trong một thành phần liên thông.
Do đó, hóa ra bài toán này rất giống với việc tìm kiếm số lượng cây khung của một đồ thị đầy đủ với $k$ đỉnh.
Sự khác biệt duy nhất là mỗi đỉnh thực sự có kích thước $s_i$: mỗi cạnh kết nối đỉnh $i$, thực sự nhân câu trả lời với $s_i$.

Do đó, để tính số cách có thể, điều quan trọng là phải đếm tần suất mỗi đỉnh trong số $k$ đỉnh được sử dụng trong cây kết nối.
Để có được một công thức cho bài toán, cần phải tính tổng câu trả lời trên tất cả các bậc có thể.

Gọi $d_1, \dots, d_k$ là bậc của các đỉnh trong cây sau khi kết nối các đỉnh.
Tổng của các bậc gấp đôi số cạnh:

$$\sum_{i=1}^k d_i = 2k - 2$$

Nếu đỉnh $i$ có bậc $d_i$, thì nó xuất hiện $d_i - 1$ lần trong mã Prüfer.
Mã Prüfer cho một cây có $k$ đỉnh có độ dài $k-2$.
Vì vậy, số cách chọn một mã có $k-2$ số trong đó số $i$ xuất hiện chính xác $d_i - 1$ lần bằng với **hệ số đa thức**

$$\binom{k-2}{d_1-1, d_2-1, \dots, d_k-1} = \frac{(k-2)!}{(d_1-1)! (d_2-1)! \cdots (d_k-1)!}.$$

Thực tế là mỗi cạnh kề với đỉnh $i$ nhân câu trả lời với $s_i$, chúng ta nhận được câu trả lời, giả sử rằng bậc của các đỉnh là $d_1, \dots, d_k$:

$$s_1^{d_1} \cdot s_2^{d_2} \cdots s_k^{d_k} \cdot \binom{k-2}{d_1-1, d_2-1, \dots, d_k-1}$$

Để có được câu trả lời cuối cùng, chúng ta cần tính tổng số này cho tất cả các cách chọn bậc có thể:

$$\sum_{\substack{d_i \ge 1 \\\\ \sum_{i=1}^k d_i = 2k -2}} s_1^{d_1} \cdot s_2^{d_2} \cdots s_k^{d_k} \cdot \binom{k-2}{d_1-1, d_2-1, \dots, d_k-1}$$

Hiện tại điều này trông giống như một câu trả lời thực sự kinh khủng, tuy nhiên chúng ta có thể sử dụng **định lý đa thức**, trong đó nói rằng:

$$(x_1 + \dots + x_m)^p = \sum_{\substack{c_i \ge 0 \\\\ \sum_{i=1}^m c_i = p}} x_1^{c_1} \cdot x_2^{c_2} \cdots x_m^{c_m} \cdot \binom{p}{c_1, c_2, \dots c_m}$$

Điều này trông khá giống nhau.
Để sử dụng nó, chúng ta chỉ cần thay thế với $e_i = d_i - 1$:

$$\sum_{\substack{e_i \ge 0 \\\\ \sum_{i=1}^k e_i = k - 2}} s_1^{e_1+1} \cdot s_2^{e_2+1} \cdots s_k^{e_k+1} \cdot \binom{k-2}{e_1, e_2, \dots, e_k}$$

Sau khi áp dụng định lý đa thức, chúng ta nhận được **câu trả lời cho bài toán**:

$$s_1 \cdot s_2 \cdots s_k \cdot (s_1 + s_2 + \dots + s_k)^{k-2} = s_1 \cdot s_2 \cdots s_k \cdot n^{k-2}$$

Thật tình cờ, công thức này cũng đúng với $k = 1$.

## Bài tập (Practice problems) {: #practice-problems}

- [UVA #10843 - Anne's game](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=20&page=show_problem&problem=1784)
- [Timus #1069 - Prufer Code](http://acm.timus.ru/problem.aspx?space=1&num=1069)
- [Codeforces - Clues](http://codeforces.com/contest/156/problem/D)
- [Topcoder - TheCitiesAndRoadsDivTwo](https://community.topcoder.com/stat?c=problem_statement&pm=10774&rd=14146)
