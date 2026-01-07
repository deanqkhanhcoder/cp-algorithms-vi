--- 
tags:
  - Translated
e_maxx_link: games_on_graphs
---

# Trò chơi trên đồ thị bất kỳ

Giả sử một trò chơi được chơi bởi hai người chơi trên một đồ thị bất kỳ $G$.
Tức là, trạng thái hiện tại của trò chơi là một đỉnh nào đó.
Các người chơi thực hiện các nước đi lần lượt, và di chuyển từ đỉnh hiện tại đến một đỉnh kề bằng cách sử dụng một cạnh nối.
Tùy thuộc vào trò chơi, người không thể di chuyển sẽ thua hoặc thắng trò chơi.

Chúng ta xem xét trường hợp tổng quát nhất, trường hợp của một đồ thị có hướng bất kỳ có chu trình.
Nhiệm vụ của chúng ta là xác định, cho một trạng thái ban đầu, ai sẽ thắng trò chơi nếu cả hai người chơi đều chơi với chiến lược tối ưu hoặc xác định rằng kết quả của trò chơi sẽ là hòa.

Chúng ta sẽ giải quyết bài toán này rất hiệu quả.
Chúng ta sẽ tìm ra giải pháp cho tất cả các đỉnh bắt đầu có thể có của đồ thị trong thời gian tuyến tính đối với số cạnh: $O(m)$. 

## Mô tả thuật toán

Chúng ta sẽ gọi một đỉnh là đỉnh thắng, nếu người chơi bắt đầu ở trạng thái này sẽ thắng trò chơi, nếu họ chơi tối ưu (bất kể người chơi kia thực hiện nước đi nào).
Tương tự, chúng ta sẽ gọi một đỉnh là đỉnh thua, nếu người chơi bắt đầu ở đỉnh này sẽ thua trò chơi, nếu đối thủ chơi tối ưu.

Đối với một số đỉnh của đồ thị, chúng ta đã biết trước rằng chúng là các đỉnh thắng hoặc thua: cụ thể là tất cả các đỉnh không có cạnh đi ra.

Chúng ta cũng có các **quy tắc** sau:

- nếu một đỉnh có một cạnh đi ra dẫn đến một đỉnh thua, thì chính đỉnh đó là một đỉnh thắng.
- nếu tất cả các cạnh đi ra của một đỉnh nào đó đều dẫn đến các đỉnh thắng, thì chính đỉnh đó là một đỉnh thua.
- nếu tại một thời điểm nào đó vẫn còn các đỉnh chưa được xác định, và không đỉnh nào phù hợp với quy tắc thứ nhất hoặc thứ hai, thì mỗi đỉnh này, khi được sử dụng làm đỉnh bắt đầu, sẽ dẫn đến một trận hòa nếu cả hai người chơi đều chơi tối ưu.

Do đó, chúng ta có thể định nghĩa một thuật toán chạy ngay trong thời gian $O(n m)$.
Chúng ta đi qua tất cả các đỉnh và cố gắng áp dụng quy tắc thứ nhất hoặc thứ hai, và lặp lại.

Tuy nhiên, chúng ta có thể tăng tốc thủ tục này, và giảm độ phức tạp xuống còn $O(m)$.

Chúng ta sẽ đi qua tất cả các đỉnh, mà ban đầu chúng ta biết là trạng thái thắng hay thua.
Đối với mỗi đỉnh đó, chúng ta bắt đầu một [tìm kiếm theo chiều sâu](../graph/depth-first-search.md).
DFS này sẽ di chuyển ngược lại trên các cạnh đảo ngược.
Trước hết, nó sẽ không đi vào các đỉnh đã được xác định là đỉnh thắng hoặc thua.
Và xa hơn nữa, nếu tìm kiếm đi từ một đỉnh thua đến một đỉnh chưa được xác định, thì chúng ta đánh dấu đỉnh này là một đỉnh thắng, và tiếp tục DFS bằng cách sử dụng đỉnh mới này.
Nếu chúng ta đi từ một đỉnh thắng đến một đỉnh chưa được xác định, thì chúng ta phải kiểm tra xem tất cả các cạnh từ đỉnh này có dẫn đến các đỉnh thắng không.
Chúng ta có thể thực hiện kiểm tra này trong $O(1)$ bằng cách lưu trữ số lượng các cạnh dẫn đến một đỉnh thắng cho mỗi đỉnh.
Vì vậy, nếu chúng ta đi từ một đỉnh thắng đến một đỉnh chưa được xác định, thì chúng ta tăng bộ đếm, và kiểm tra xem số này có bằng số cạnh đi ra không.
Nếu đúng như vậy, chúng ta có thể đánh dấu đỉnh này là một đỉnh thua, và tiếp tục DFS từ đỉnh này.
Nếu không, chúng ta vẫn chưa biết, liệu đỉnh này là đỉnh thắng hay thua, và do đó không có ý nghĩa gì khi tiếp tục DFS bằng cách sử dụng nó.

Tổng cộng chúng ta truy cập mọi đỉnh thắng và mọi đỉnh thua chính xác một lần (các đỉnh chưa được xác định không được truy cập), và chúng ta cũng đi qua mỗi cạnh nhiều nhất một lần.
Do đó, độ phức tạp là $O(m)$.

## Cài đặt

Đây là việc triển khai của một DFS như vậy.
Chúng ta giả định rằng biến `adj_rev` lưu trữ danh sách kề cho đồ thị ở dạng **đảo ngược**, tức là thay vì lưu trữ cạnh $(i, j)$ của đồ thị, chúng ta lưu trữ $(j, i)$.
Ngoài ra, đối với mỗi đỉnh, chúng ta giả định rằng bậc ra đã được tính toán.

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

## Ví dụ: "Cảnh sát và tên trộm"

Đây là một ví dụ cụ thể của một trò chơi như vậy.

Có một bàn cờ $m \times n$.
Một số ô không thể đi vào.
Tọa độ ban đầu của viên cảnh sát và của tên trộm đã được biết.
Một trong các ô là lối ra.
Nếu viên cảnh sát và tên trộm ở cùng một ô vào bất kỳ thời điểm nào, viên cảnh sát thắng.
Nếu tên trộm ở ô lối ra (mà không có viên cảnh sát cũng ở trên ô đó), thì tên trộm thắng.
Viên cảnh sát có thể đi theo cả 8 hướng, tên trộm chỉ đi theo 4 hướng (dọc theo các trục tọa độ).
Cả viên cảnh sát và tên trộm sẽ lần lượt di chuyển.
Tuy nhiên, họ cũng có thể bỏ qua một lượt nếu muốn.
Nước đi đầu tiên được thực hiện bởi viên cảnh sát.

Bây giờ chúng ta sẽ **xây dựng đồ thị**.
Để làm điều này, chúng ta phải hình thức hóa các quy tắc của trò chơi.
Trạng thái hiện tại của trò chơi được xác định bởi tọa độ của viên cảnh sát $P$, tọa độ của tên trộm $T$, và cũng bởi lượt đi của ai, hãy gọi biến này là $P_{\text{turn}}$ (đúng khi đến lượt của viên cảnh sát).
Do đó, một đỉnh của đồ thị được xác định bởi bộ ba $(P, T, P_{\text{turn}})$
Đồ thị sau đó có thể được xây dựng dễ dàng, chỉ cần tuân theo các quy tắc của trò chơi.

Tiếp theo, chúng ta cần xác định các đỉnh nào là đỉnh thắng và đỉnh nào là đỉnh thua ban đầu.
Có một **điểm tinh tế** ở đây.
Các đỉnh thắng / thua phụ thuộc, ngoài tọa độ, còn vào $P_{\text{turn}}$ - lượt đi của ai.
Nếu đến lượt của viên cảnh sát, thì đỉnh đó là một đỉnh thắng, nếu tọa độ của viên cảnh sát và tên trộm trùng nhau, và đỉnh đó là một đỉnh thua nếu nó không phải là một đỉnh thắng và tên trộm đang ở ô lối ra.
Nếu đến lượt của tên trộm, thì một đỉnh là một đỉnh thua, nếu tọa độ của hai người chơi trùng nhau, và nó là một đỉnh thắng nếu nó không phải là một đỉnh thua, và tên trộm đang ở ô lối ra.

Điểm duy nhất trước khi triển khai không phải là, bạn cần quyết định xem bạn muốn xây dựng đồ thị **một cách tường minh** hay chỉ xây dựng nó **trong lúc chạy**.
Một mặt, việc xây dựng đồ thị một cách tường minh sẽ dễ dàng hơn nhiều và có ít cơ hội mắc lỗi hơn.
Mặt khác, nó sẽ làm tăng lượng mã và thời gian chạy sẽ chậm hơn so với việc bạn xây dựng đồ thị trong lúc chạy.

Việc triển khai sau đây sẽ xây dựng đồ thị một cách tường minh:

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
        cout << "Cảnh sát bắt được tên trộm"  << endl;
    } else if (losing[P_st][T_st][true]) {
        cout << "Tên trộm đã trốn thoát" << endl;
    } else {
        cout << "Hòa" << endl;
    }
}
```