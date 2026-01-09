---
tags:
  - Translated
e_maxx_link: games_on_graphs
---

# Trò chơi trên đồ thị bất kỳ (Games on arbitrary graphs) {: #games-on-arbitrary-graphs}

Giả sử một trò chơi được chơi bởi hai người chơi trên một đồ thị bất kỳ $G$.
Tức là trạng thái hiện tại của trò chơi là một đỉnh nhất định.
Các người chơi thực hiện các nước đi theo lượt, và di chuyển từ đỉnh hiện tại đến một đỉnh kề bằng cách sử dụng một cạnh nối.
Tùy thuộc vào trò chơi, người không thể di chuyển sẽ thua hoặc thắng trò chơi.

Chúng ta xem xét trường hợp tổng quát nhất, trường hợp của một đồ thị có hướng bất kỳ có chu trình.
Nhiệm vụ của chúng ta là xác định, với một trạng thái ban đầu, ai sẽ thắng trò chơi nếu cả hai người chơi chơi với các chiến lược tối ưu hoặc xác định rằng kết quả của trò chơi sẽ là hòa.

Chúng ta sẽ giải quyết bài toán này rất hiệu quả.
Chúng ta sẽ tìm giải pháp cho tất cả các đỉnh bắt đầu có thể có của đồ thị trong thời gian tuyến tính đối với số lượng cạnh: $O(m)$.

## Mô tả thuật toán (Description of the algorithm) {: #description-of-the-algorithm}

Chúng ta sẽ gọi một đỉnh là đỉnh thắng (winning vertex), nếu người chơi bắt đầu tại trạng thái này sẽ thắng trò chơi, nếu họ chơi tối ưu (bất kể người chơi kia thực hiện các lượt đi nào).
Tương tự, chúng ta sẽ gọi một đỉnh là đỉnh thua (losing vertex), nếu người chơi bắt đầu tại đỉnh này sẽ thua trò chơi, nếu đối thủ chơi tối ưu.

Đối với một số đỉnh của đồ thị, chúng ta đã biết trước rằng chúng là đỉnh thắng hay thua: cụ thể là tất cả các đỉnh không có cạnh ra.

Ngoài ra chúng ta có các **quy tắc** sau:

-   nếu một đỉnh có một cạnh ra dẫn đến một đỉnh thua, thì chính đỉnh đó là một đỉnh thắng.
-   nếu tất cả các cạnh ra của một đỉnh nhất định dẫn đến các đỉnh thắng, thì chính đỉnh đó là một đỉnh thua.
-   nếu tại một thời điểm nào đó vẫn còn các đỉnh chưa xác định, và không đỉnh nào phù hợp với quy tắc thứ nhất hoặc thứ hai, thì mỗi đỉnh này, khi được sử dụng làm đỉnh bắt đầu, sẽ dẫn đến kết quả hòa nếu cả hai người chơi chơi tối ưu.

Do đó, chúng ta có thể định nghĩa một thuật toán chạy trong thời gian $O(n m)$ ngay lập tức.
Chúng ta đi qua tất cả các đỉnh và cố gắng áp dụng quy tắc thứ nhất hoặc thứ hai, và lặp lại.

Tuy nhiên, chúng ta có thể tăng tốc quy trình này, và giảm độ phức tạp xuống $O(m)$.

Chúng ta sẽ đi qua tất cả các đỉnh, mà chúng ta ban đầu biết nếu chúng là trạng thái thắng hoặc thua.
Đối với mỗi đỉnh trong số chúng, chúng ta bắt đầu một [tìm kiếm theo chiều sâu (DFS)](../graph/depth-first-search.md).
DFS này sẽ di chuyển ngược lại qua các cạnh đảo ngược (reversed edges).
Trước hết, nó sẽ không đi vào các đỉnh đã được xác định là đỉnh thắng hoặc thua.
Và xa hơn nữa, nếu tìm kiếm đi từ một đỉnh thua đến một đỉnh chưa xác định, thì chúng ta đánh dấu đỉnh này là một đỉnh thắng, và tiếp tục DFS sử dụng đỉnh mới này.
Nếu chúng ta đi từ một đỉnh thắng đến một đỉnh chưa xác định, thì chúng ta phải kiểm tra xem tất cả các cạnh từ đỉnh này có dẫn đến các đỉnh thắng hay không.
Chúng ta có thể thực hiện kiểm tra này trong $O(1)$ bằng cách lưu trữ số lượng cạnh dẫn đến một đỉnh thắng cho mỗi đỉnh.
Vì vậy, nếu chúng ta đi từ một đỉnh thắng đến một đỉnh chưa xác định, thì chúng ta tăng bộ đếm, và kiểm tra xem số này có bằng số lượng cạnh ra hay không.
Nếu đúng như vậy, chúng ta có thể đánh dấu đỉnh này là một đỉnh thua, và tiếp tục DFS từ đỉnh này.
Ngược lại, chúng ta chưa biết liệu đỉnh này là đỉnh thắng hay thua, và do đó không có ý nghĩa gì khi tiếp tục DFS sử dụng nó.

Tổng cộng chúng ta thăm mọi đỉnh thắng và mọi đỉnh thua chính xác một lần (các đỉnh chưa xác định không được thăm), và chúng ta cũng đi qua mỗi cạnh tối đa một lần.
Do đó độ phức tạp là $O(m)$.

## Cài đặt (Implementation) {: #implementation}

Dưới đây là việc cài đặt của một DFS như vậy.
Chúng ta giả sử rằng biến `adj_rev` lưu trữ danh sách kề cho đồ thị ở dạng **đảo ngược**, tức là thay vì lưu trữ cạnh $(i, j)$ của đồ thị, chúng ta lưu trữ $(j, i)$.
Ngoài ra đối với mỗi đỉnh, chúng ta giả sử rằng bậc ra (outgoing degree) đã được tính toán.

```cpp 
vector<vector<int>> adj_rev;

vector<bool> winning;
vector<bool> losing;
vector<bool> visited;
vector<int> degree;

void dfs(int v) {
    visited[v] = true;
    for (int u : adj_rev[v]) {
        if (!visited[u]) {
            if (losing[v])
                winning[u] = true;
            else if (--degree[u] == 0)
                losing[u] = true;
            else
                continue;
            dfs(u);
        }
    }
}
```

## Ví dụ: "Cảnh sát và tên trộm" (Example: "Policeman and thief") {: #example-policeman-and-thief}

Dưới đây là một ví dụ cụ thể về một trò chơi như vậy.

Có bảng $m \times n$.
Một số ô không thể đi vào.
Tọa độ ban đầu của cảnh sát và tên trộm được biết.
Một trong các ô là lối ra.
Nếu cảnh sát và tên trộm ở cùng một ô tại bất kỳ thời điểm nào, cảnh sát thắng.
Nếu tên trộm ở ô lối ra (mà không có cảnh sát cũng ở trên ô đó), thì tên trộm thắng.
Cảnh sát có thể đi bộ theo tất cả 8 hướng, tên trộm chỉ theo 4 hướng (theo trục tọa độ).
Cả cảnh sát và tên trộm sẽ lần lượt di chuyển.
Tuy nhiên họ cũng có thể bỏ qua một lượt nếu họ muốn.
Nước đi đầu tiên được thực hiện bởi cảnh sát.

Bây giờ chúng ta sẽ **xây dựng đồ thị**.
Để làm điều này chúng ta phải chính thức hóa các quy tắc của trò chơi.
Trạng thái hiện tại của trò chơi được xác định bởi tọa độ của cảnh sát $P$, tọa độ của tên trộm $T$, và cũng bởi lượt của ai, hãy gọi biến này là $P_{\text{turn}}$ (là true khi đến lượt của cảnh sát).
Do đó, một đỉnh của đồ thị được xác định bởi bộ ba $(P, T, P_{\text{turn}})$
Sau đó, đồ thị có thể được xây dựng dễ dàng, đơn giản bằng cách tuân theo các quy tắc của trò chơi.

Tiếp theo, chúng ta cần xác định đỉnh nào là thắng và đỉnh nào là thua ban đầu.
Có một **điểm tinh tế** ở đây.
Các đỉnh thắng / thua phụ thuộc, ngoài tọa độ, còn vào $P_{\text{turn}}$ - lượt của ai.
Nếu đến lượt của cảnh sát, thì đỉnh là đỉnh thắng, nếu tọa độ của cảnh sát và tên trộm trùng nhau, và đỉnh là đỉnh thua nếu nó không phải là đỉnh thắng và tên trộm đang ở lối ra.
Nếu đến lượt của tên trộm, thì một đỉnh là đỉnh thua, nếu tọa độ của hai người chơi trùng nhau, và nó là đỉnh thắng nếu nó không phải là đỉnh thua, và tên trộm đang ở lối ra.

Điểm duy nhất trước khi cài đặt là bạn cần quyết định xem bạn muốn xây dựng đồ thị **một cách tường minh** hay chỉ xây dựng nó **ngay trong quá trình chạy (on the fly)**.
Một mặt, việc xây dựng đồ thị một cách tường minh sẽ dễ dàng hơn nhiều và ít có khả năng mắc lỗi hơn.
Mặt khác, nó sẽ làm tăng lượng mã và thời gian chạy sẽ chậm hơn so với khi bạn xây dựng đồ thị ngay trong quá trình chạy.

Việc cài đặt sau đây sẽ xây dựng đồ thị một cách tường minh:

```cpp
struct State {
    int P, T;
    bool Pstep;
};

vector<State> adj_rev[100][100][2]; // [P][T][Pstep]
bool winning[100][100][2];
bool losing[100][100][2];
bool visited[100][100][2];
int degree[100][100][2];

void dfs(State v) {
    visited[v.P][v.T][v.Pstep] = true;
    for (State u : adj_rev[v.P][v.T][v.Pstep]) {
        if (!visited[u.P][u.T][u.Pstep]) {
            if (losing[v.P][v.T][v.Pstep])
                winning[u.P][u.T][u.Pstep] = true;
            else if (--degree[u.P][u.T][u.Pstep] == 0)
                losing[u.P][u.T][u.Pstep] = true;
            else
                continue;
            dfs(u);
        }
    }
}

int main() {
    int n, m;
    cin >> n >> m;
    vector<string> a(n);
    for (int i = 0; i < n; i++)
        cin >> a[i];

    for (int P = 0; P < n*m; P++) {
        for (int T = 0; T < n*m; T++) {
            for (int Pstep = 0; Pstep <= 1; Pstep++) {
                int Px = P/m, Py = P%m, Tx = T/m, Ty = T%m;
                if (a[Px][Py]=='*' || a[Tx][Ty]=='*')
                    continue;
                
                bool& win = winning[P][T][Pstep];
                bool& lose = losing[P][T][Pstep];
                if (Pstep) {
                    win = Px==Tx && Py==Ty;
                    lose = !win && a[Tx][Ty] == 'E';
                } else {
                    lose = Px==Tx && Py==Ty;
                    win = !lose && a[Tx][Ty] == 'E';
                }
                if (win || lose)
                    continue;

                State st = {P,T,!Pstep};
                adj_rev[P][T][Pstep].push_back(st);
                st.Pstep = Pstep;
                degree[P][T][Pstep]++;
                
                const int dx[] = {-1, 0, 1, 0, -1, -1, 1, 1};
                const int dy[] = {0, 1, 0, -1, -1, 1, -1, 1};
                for (int d = 0; d < (Pstep ? 8 : 4); d++) {
                    int PPx = Px, PPy = Py, TTx = Tx, TTy = Ty;
                    if (Pstep) {
                        PPx += dx[d];
                        PPy += dy[d];
                    } else {
                        TTx += dx[d];
                        TTy += dy[d];
                    }

                    if (PPx >= 0 && PPx < n && PPy >= 0 && PPy < m && a[PPx][PPy] != '*' &&
                        TTx >= 0 && TTx < n && TTy >= 0 && TTy < m && a[TTx][TTy] != '*')
                    {
                        adj_rev[PPx*m+PPy][TTx*m+TTy][!Pstep].push_back(st);
                        ++degree[P][T][Pstep];
                    }
                }
            }
        }
    }

    for (int P = 0; P < n*m; P++) {
        for (int T = 0; T < n*m; T++) {
            for (int Pstep = 0; Pstep <= 1; Pstep++) {
                if ((winning[P][T][Pstep] || losing[P][T][Pstep]) && !visited[P][T][Pstep])
                    dfs({P, T, (bool)Pstep});
            }
        }
    }

    int P_st, T_st;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (a[i][j] == 'P')
                P_st = i*m+j;
            else if (a[i][j] == 'T')
                T_st = i*m+j;
        }
    }

    if (winning[P_st][T_st][true]) {
        cout << "Police catches the thief"  << endl;
    } else if (losing[P_st][T_st][true]) {
        cout << "The thief escapes" << endl;
    } else {
        cout << "Draw" << endl;
    }
}
```
