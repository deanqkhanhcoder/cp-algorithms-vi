---
tags:
  - Translated
e_maxx_link: 2_sat
---

# 2-SAT 

SAT (bài toán thỏa mãn logic Boole) là bài toán gán các giá trị Boole cho các biến để thỏa mãn một công thức Boole cho trước.
Công thức Boole thường được cho ở dạng CNF (dạng chuẩn hội), là một phép hội của nhiều mệnh đề, trong đó mỗi mệnh đề là một phép tuyển của các literal (biến hoặc phủ định của biến).
2-SAT (2-satisfiability) là một sự giới hạn của bài toán SAT, trong 2-SAT mỗi mệnh đề có đúng hai literal.
Đây là một ví dụ về một bài toán 2-SAT như vậy.
Tìm một phép gán của $a, b, c$ sao cho công thức sau là đúng:

$$(a \lor \lnot b) \land (\lnot a \lor b) \land (\lnot a \lor \lnot b) \land (a \lor \lnot c)$$

SAT là NP-đầy đủ, không có giải pháp hiệu quả nào được biết đến cho nó.
Tuy nhiên 2SAT có thể được giải quyết hiệu quả trong $O(n + m)$ trong đó $n$ là số lượng biến và $m$ là số lượng mệnh đề.

## Thuật toán:

Đầu tiên, chúng ta cần chuyển đổi bài toán sang một dạng khác, được gọi là dạng chuẩn suy ra (implicative normal form).
Lưu ý rằng biểu thức $a \lor b$ tương đương với $\lnot a \Rightarrow b \land \lnot b \Rightarrow a$ (nếu một trong hai biến là sai, thì biến còn lại phải là đúng).

Bây giờ chúng ta xây dựng một đồ thị có hướng của những phép suy ra này:
với mỗi biến $x$ sẽ có hai đỉnh $v_x$ và $v_{\lnot x}$.
Các cạnh sẽ tương ứng với các phép suy ra.

Hãy xem xét ví dụ ở dạng 2-CNF:

$$(a \lor \lnot b) \land (\lnot a \lor b) \land (\lnot a \lor \lnot b) \land (a \lor \lnot c)$$

Đồ thị có hướng sẽ chứa các đỉnh và cạnh sau:

$$\begin{array}{cccc}
\lnot a \Rightarrow \lnot b & a \Rightarrow b & a \Rightarrow \lnot b & \lnot a \Rightarrow \lnot c\
b \Rightarrow a & \lnot b \Rightarrow \lnot a & b \Rightarrow \lnot a & c \Rightarrow a
\end{array}$$

Bạn có thể thấy đồ thị suy ra trong hình ảnh sau:

<div style="text-align: center;">
  <img src="2SAT.png" alt="Đồ thị suy ra của ví dụ 2-SAT">
</div>

Điều đáng chú ý là tính chất của đồ thị suy ra:
nếu có một cạnh $a \Rightarrow b$, thì cũng có một cạnh $\lnot b \Rightarrow \lnot a$.

Cũng lưu ý rằng, nếu $x$ có thể đến được từ $\lnot x$, và $\lnot x$ có thể đến được từ $x$, thì bài toán không có giải pháp.
Bất kể giá trị nào chúng ta chọn cho biến $x$, nó sẽ luôn kết thúc trong một mâu thuẫn - nếu $x$ được gán là $\text{true}$ thì phép suy ra cho chúng ta biết rằng $\lnot x$ cũng phải là $\text{true}$ và ngược lại.
Hóa ra, điều kiện này không chỉ cần thiết mà còn đủ.
Chúng ta sẽ chứng minh điều này trong vài đoạn tiếp theo.
Đầu tiên hãy nhớ lại, nếu một đỉnh có thể đến được từ một đỉnh thứ hai, và đỉnh thứ hai có thể đến được từ đỉnh thứ nhất, thì hai đỉnh này nằm trong cùng một thành phần liên thông mạnh.
Do đó, chúng ta có thể phát biểu tiêu chí cho sự tồn tại của một giải pháp như sau:

Để bài toán 2-SAT này có một giải pháp, điều kiện cần và đủ là với bất kỳ biến $x$ nào, các đỉnh $x$ và $\lnot x$ nằm trong các thành phần liên thông mạnh khác nhau của đồ thị suy ra.

Tiêu chí này có thể được kiểm tra trong thời gian $O(n + m)$ bằng cách tìm tất cả các thành phần liên thông mạnh.

Hình ảnh sau đây cho thấy tất cả các thành phần liên thông mạnh của ví dụ.
Như chúng ta có thể dễ dàng kiểm tra, không có thành phần nào trong bốn thành phần chứa một đỉnh $x$ và phủ định của nó $\lnot x$, do đó ví dụ này có một giải pháp.
Chúng ta sẽ học trong các đoạn tiếp theo cách tính toán một phép gán hợp lệ, nhưng chỉ để minh họa, giải pháp $a = \text{false}$, $b = \text{false}$, $c = \text{false}$ được đưa ra.

<div style="text-align: center;">
  <img src="2SAT_SCC.png" alt="Các thành phần liên thông mạnh của ví dụ 2-SAT">
</div>

Bây giờ chúng ta xây dựng thuật toán để tìm giải pháp của bài toán 2-SAT với giả định rằng giải pháp tồn tại.

Lưu ý rằng, mặc dù giải pháp tồn tại, có thể xảy ra trường hợp $\lnot x$ có thể đến được từ $x$ trong đồ thị suy ra, hoặc (nhưng không đồng thời) $x$ có thể đến được từ $\lnot x$.
Trong trường hợp đó, việc chọn $\text{true}$ hoặc $\text{false}$ cho $x$ sẽ dẫn đến mâu thuẫn, trong khi việc chọn giá trị còn lại sẽ không.
Hãy học cách chọn một giá trị sao cho chúng ta không tạo ra mâu thuẫn.

Hãy sắp xếp các thành phần liên thông mạnh theo thứ tự tô pô (tức là $\text{comp}[v] \le \text{comp}[u]$ nếu có đường đi từ $v$ đến $u$) và gọi $\text{comp}[v]$ là chỉ số của thành phần liên thông mạnh mà đỉnh $v$ thuộc về.
Khi đó, nếu $\text{comp}[x] < \text{comp}[\lnot x]$ chúng ta gán $x$ là $\text{false}$ và ngược lại là $\text{true}$.

Hãy chứng minh rằng với phép gán các biến này, chúng ta không đi đến mâu thuẫn.
Giả sử $x$ được gán là $\text{true}$.
Trường hợp còn lại có thể được chứng minh tương tự.

Đầu tiên chúng ta chứng minh rằng đỉnh $x$ không thể đến được đỉnh $\lnot x$.
Bởi vì chúng ta đã gán $\text{true}$, điều kiện phải là chỉ số của thành phần liên thông mạnh của $x$ lớn hơn chỉ số của thành phần của $\lnot x$.
Điều này có nghĩa là $\lnot x$ nằm ở bên trái của thành phần chứa $x$, và đỉnh sau không thể đến được đỉnh đầu.

Thứ hai, chúng ta chứng minh rằng không tồn tại một biến $y$, sao cho các đỉnh $y$ và $\lnot y$ đều có thể đến được từ $x$ trong đồ thị suy ra.
Điều này sẽ gây ra mâu thuẫn, vì $x = \text{true}$ suy ra $y = \text{true}$ và $\lnot y = \text{true}$.
Hãy chứng minh điều này bằng phản chứng.
Giả sử rằng $y$ và $\lnot y$ đều có thể đến được từ $x$, thì theo tính chất của đồ thị suy ra, $\lnot x$ có thể đến được từ cả $y$ và $\lnot y$.
Bằng tính bắc cầu, điều này dẫn đến $\lnot x$ có thể đến được từ $x$, điều này mâu thuẫn với giả định.

Vì vậy, chúng ta đã xây dựng một thuật toán tìm các giá trị cần thiết của các biến với giả định rằng với bất kỳ biến $x$ nào, các đỉnh $x$ và $\lnot x$ nằm trong các thành phần liên thông mạnh khác nhau.
Phần trên đã cho thấy tính đúng đắn của thuật toán này.
Do đó, chúng ta đồng thời đã chứng minh tiêu chí trên cho sự tồn tại của một giải pháp.

## Cài đặt:

Bây giờ chúng ta có thể triển khai toàn bộ thuật toán.
Đầu tiên, chúng ta xây dựng đồ thị suy ra và tìm tất cả các thành phần liên thông mạnh.
Điều này có thể được thực hiện bằng thuật toán của Kosaraju trong thời gian $O(n + m)$.
Trong lần duyệt thứ hai của đồ thị, thuật toán của Kosaraju thăm các thành phần liên thông mạnh theo thứ tự tô pô, do đó dễ dàng tính toán $\text{comp}[v]$ cho mỗi đỉnh $v$.

Sau đó, chúng ta có thể chọn phép gán của $x$ bằng cách so sánh $\text{comp}[x]$ và $\text{comp}[\lnot x]$. 
Nếu $\text{comp}[x] = \text{comp}[\lnot x]$ chúng ta trả về $\text{false}$ để chỉ ra rằng không tồn tại một phép gán hợp lệ thỏa mãn bài toán 2-SAT.

Dưới đây là việc triển khai giải pháp của bài toán 2-SAT cho đồ thị suy ra đã được xây dựng $adj$ và đồ thị chuyển vị $adj^{\intercal}$ (trong đó hướng của mỗi cạnh được đảo ngược).
Trong đồ thị, các đỉnh có chỉ số $2k$ và $2k+1$ là hai đỉnh tương ứng với biến $k$ với $2k+1$ tương ứng với biến bị phủ định.

```cpp
struct TwoSatSolver {
    int n_vars;
    int n_vertices;
    vector<vector<int>> adj, adj_t;
    vector<bool> used;
    vector<int> order, comp;
    vector<bool> assignment;

    TwoSatSolver(int _n_vars) : n_vars(_n_vars), n_vertices(2 * n_vars), adj(n_vertices), adj_t(n_vertices), used(n_vertices), order(), comp(n_vertices, -1), assignment(n_vars) {
        order.reserve(n_vertices);
    }
    void dfs1(int v) {
        used[v] = true;
        for (int u : adj[v]) {
            if (!used[u])
                dfs1(u);
        }
        order.push_back(v);
    }

    void dfs2(int v, int cl) {
        comp[v] = cl;
        for (int u : adj_t[v]) {
            if (comp[u] == -1)
                dfs2(u, cl);
        }
    }

    bool solve_2SAT() {
        order.clear();
        used.assign(n_vertices, false);
        for (int i = 0; i < n_vertices; ++i) {
            if (!used[i])
                dfs1(i);
        }

        comp.assign(n_vertices, -1);
        for (int i = 0, j = 0; i < n_vertices; ++i) {
            int v = order[n_vertices - i - 1];
            if (comp[v] == -1)
                dfs2(v, j++);
        }

        assignment.assign(n_vars, false);
        for (int i = 0; i < n_vertices; i += 2) {
            if (comp[i] == comp[i + 1])
                return false;
            assignment[i / 2] = comp[i] > comp[i + 1];
        }
        return true;
    }

    void add_disjunction(int a, bool na, int b, bool nb) {
        // na và nb biểu thị liệu a và b có bị phủ định hay không 
        a = 2 * a ^ na;
        b = 2 * b ^ nb;
        int neg_a = a ^ 1;
        int neg_b = b ^ 1;
        adj[neg_a].push_back(b);
        adj[neg_b].push_back(a);
        adj_t[b].push_back(neg_a);
        adj_t[a].push_back(neg_b);
    }

    static void example_usage() {
        TwoSatSolver solver(3); // a, b, c
        solver.add_disjunction(0, false, 1, true);  //     a  v  not b
        solver.add_disjunction(0, true, 1, true);   // not a  v  not b
        solver.add_disjunction(1, false, 2, false); //     b  v      c
        solver.add_disjunction(0, false, 0, false); //     a  v      a
        assert(solver.solve_2SAT() == true);
        auto expected = vector<bool>{{true, false, true}};
        assert(solver.assignment == expected);
    }
};
```

## Bài tập thực hành
 * [Codeforces: The Door Problem](http://codeforces.com/contest/776/problem/D)
 * [Kattis: Illumination](https://open.kattis.com/problems/illumination)
 * [UVA: Rectangles](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3081)
 * [Codeforces : Radio Stations](https://codeforces.com/problemset/problem/1215/F)
 * [CSES : Giant Pizza](https://cses.fi/problemset/task/1684)
 * [Codeforces: +-1](https://codeforces.com/contest/1971/problem/H)
 * [Gym: (C) Colorful Village](https://codeforces.com/gym/104772/problem/C)
 * [POI: Renovation](https://szkopul.edu.pl/problemset/problem/xNjwUvwdHQoQTFBrmyG8vD1O/site/?key=statement)