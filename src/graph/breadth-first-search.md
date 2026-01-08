---
tags:
  - Translated
e_maxx_link: bfs
---

# Tìm kiếm theo chiều rộng (Breadth-first search) {: #breadth-first-search}

Tìm kiếm theo chiều rộng (Breadth first search - BFS) là một trong những thuật toán tìm kiếm cơ bản và thiết yếu trên đồ thị.

Do cách hoạt động của thuật toán, đường đi được tìm thấy bởi tìm kiếm theo chiều rộng đến bất kỳ nút nào là đường đi ngắn nhất đến nút đó, tức là đường đi chứa số lượng cạnh nhỏ nhất trong đồ thị không trọng số.

Thuật toán hoạt động trong thời gian $O(n + m)$, trong đó $n$ là số lượng đỉnh và $m$ là số lượng cạnh.

## Mô tả thuật toán (Description of the algorithm) {: #description-of-the-algorithm}

Thuật toán nhận đầu vào là một đồ thị không trọng số và id của đỉnh nguồn $s$. Đồ thị đầu vào có thể là có hướng hoặc vô hướng, điều đó không quan trọng đối với thuật toán.

Thuật toán có thể được hiểu như một ngọn lửa lan truyền trên đồ thị: ở bước thứ 0, chỉ có nguồn $s$ bị cháy. Ở mỗi bước, ngọn lửa đang cháy tại mỗi đỉnh lan sang tất cả các hàng xóm của nó. Trong một lần lặp của thuật toán, "vòng lửa" được mở rộng theo chiều rộng thêm một đơn vị (do đó có tên gọi của thuật toán).

Chính xác hơn, thuật toán có thể được phát biểu như sau: Tạo một hàng đợi $q$ sẽ chứa các đỉnh cần được xử lý và một mảng Boolean $used[]$ chỉ ra cho mỗi đỉnh, nếu nó đã được thắp sáng (hoặc đã thăm) hay chưa.

Ban đầu, đẩy nguồn $s$ vào hàng đợi và đặt $used[s] = true$, và đối với tất cả các đỉnh khác $v$ đặt $used[v] = false$.
Sau đó, lặp lại cho đến khi hàng đợi trống và trong mỗi lần lặp, lấy ra một đỉnh từ đầu hàng đợi. Duyệt qua tất cả các cạnh đi ra khỏi đỉnh này và nếu một số cạnh này đi đến các đỉnh chưa được thắp sáng, hãy thắp sáng chúng và đặt chúng vào hàng đợi.

Kết quả là, khi hàng đợi trống, "vòng lửa" chứa tất cả các đỉnh có thể đến được từ nguồn $s$, với mỗi đỉnh được tiếp cận theo cách ngắn nhất có thể.
Bạn cũng có thể tính toán độ dài của các đường đi ngắn nhất (chỉ cần duy trì một mảng độ dài đường đi $d[]$) cũng như lưu thông tin để khôi phục tất cả các đường đi ngắn nhất này (để làm điều này, cần duy trì một mảng các "cha" $p[]$, lưu trữ cho mỗi đỉnh đỉnh mà từ đó chúng ta đã đến nó).

## Cài đặt (Implementation) {: #implementation}

Chúng tôi viết mã cho thuật toán được mô tả bằng C++ và Java.

=== "C++"
    ```cpp
    vector<vector<int>> adj;  // biểu diễn danh sách kề
    int n; // số lượng nút
    int s; // đỉnh nguồn

    queue<int> q;
    vector<bool> used(n);
    vector<int> d(n), p(n);

    q.push(s);
    used[s] = true;
    p[s] = -1;
    while (!q.empty()) {
        int v = q.front();
        q.pop();
        for (int u : adj[v]) {
            if (!used[u]) {
                used[u] = true;
                q.push(u);
                d[u] = d[v] + 1;
                p[u] = v;
            }
        }
    }
    ```
=== "Java"
    ```java
    ArrayList<ArrayList<Integer>> adj = new ArrayList<>(); // biểu diễn danh sách kề
        
    int n; // số lượng nút
    int s; // đỉnh nguồn


    LinkedList<Integer> q = new LinkedList<Integer>();
    boolean used[] = new boolean[n];
    int d[] = new int[n];
    int p[] = new int[n];

    q.push(s);
    used[s] = true;
    p[s] = -1;
    while (!q.isEmpty()) {
        int v = q.pop();
        for (int u : adj.get(v)) {
            if (!used[u]) {
                used[u] = true;
                q.push(u);
                d[u] = d[v] + 1;
                p[u] = v;
            }
        }
    }
    ```
    
Nếu chúng ta phải khôi phục và hiển thị đường đi ngắn nhất từ nguồn đến một đỉnh $u$ nào đó, nó có thể được thực hiện theo cách sau:
    
=== "C++"
    ```cpp
    if (!used[u]) {
        cout << "No path!";
    } else {
        vector<int> path;
        for (int v = u; v != -1; v = p[v])
            path.push_back(v);
        reverse(path.begin(), path.end());
        cout << "Path: ";
        for (int v : path)
            cout << v << " ";
    }
    ```
=== "Java"
    ```java
    if (!used[u]) {
        System.out.println("No path!");
    } else {
        ArrayList<Integer> path = new ArrayList<Integer>();
        for (int v = u; v != -1; v = p[v])
            path.add(v);
        Collections.reverse(path);
        for(int v : path)
            System.out.println(v);
    }
    ```
    
## Ứng dụng của BFS (Applications of BFS) {: #applications-of-bfs}

* Tìm đường đi ngắn nhất từ một nguồn đến các đỉnh khác trong một đồ thị không trọng số.

* Tìm tất cả các thành phần liên thông trong một đồ thị vô hướng trong thời gian $O(n + m)$:
Để làm điều này, chúng ta chỉ cần chạy BFS bắt đầu từ mỗi đỉnh, ngoại trừ các đỉnh đã được thăm từ các lần chạy trước.
Do đó, chúng ta thực hiện BFS bình thường từ mỗi đỉnh, nhưng không đặt lại mảng $used[]$ mỗi khi chúng ta nhận được một thành phần liên thông mới, và tổng thời gian chạy vẫn sẽ là $O(n + m)$ (việc thực hiện nhiều BFS trên đồ thị mà không đặt lại mảng $used []$ được gọi là một loạt các tìm kiếm theo chiều rộng).

* Tìm lời giải cho một bài toán hoặc một trò chơi với số bước đi ít nhất, nếu mỗi trạng thái của trò chơi có thể được biểu diễn bằng một đỉnh của đồ thị, và các chuyển đổi từ trạng thái này sang trạng thái khác là các cạnh của đồ thị.

* Tìm đường đi ngắn nhất trong đồ thị có trọng số 0 hoặc 1:
Điều này chỉ yêu cầu một chút sửa đổi đối với tìm kiếm theo chiều rộng thông thường: Thay vì duy trì mảng $used[]$, bây giờ chúng ta sẽ kiểm tra xem khoảng cách đến đỉnh có ngắn hơn khoảng cách được tìm thấy hiện tại hay không, sau đó nếu cạnh hiện tại có trọng số bằng 0, chúng ta thêm nó vào đầu hàng đợi, ngược lại chúng ta thêm nó vào cuối hàng đợi. Sửa đổi này được giải thích chi tiết hơn trong bài viết [0-1 BFS](01_bfs.md).

* Tìm chu trình ngắn nhất trong đồ thị có hướng không trọng số:
Bắt đầu tìm kiếm theo chiều rộng từ mỗi đỉnh.
Ngay khi chúng ta cố gắng đi từ đỉnh hiện tại trở lại đỉnh nguồn, chúng ta đã tìm thấy chu trình ngắn nhất chứa đỉnh nguồn.
Tại thời điểm này, chúng ta có thể dừng BFS và bắt đầu BFS mới từ đỉnh tiếp theo.
Từ tất cả các chu trình như vậy (tối đa một từ mỗi BFS), chọn chu trình ngắn nhất.

* Tìm tất cả các cạnh nằm trên bất kỳ đường đi ngắn nhất nào giữa một cặp đỉnh $(a, b)$ cho trước.
Để làm điều này, hãy chạy hai tìm kiếm theo chiều rộng:
một từ $a$ và một từ $b$.
Giả sử $d_a []$ là mảng chứa khoảng cách ngắn nhất thu được từ BFS đầu tiên (từ $a$) và $d_b []$ là mảng chứa khoảng cách ngắn nhất thu được từ BFS thứ hai từ $b$.
Bây giờ đối với mọi cạnh $(u, v)$, thật dễ dàng để kiểm tra xem cạnh đó có nằm trên bất kỳ đường đi ngắn nhất nào giữa $a$ và $b$ hay không:
tiêu chí là điều kiện $d_a [u] + 1 + d_b [v] = d_a [b]$.

* Tìm tất cả các đỉnh trên bất kỳ đường đi ngắn nhất nào giữa một cặp đỉnh $(a, b)$ cho trước.
Để thực hiện điều đó, hãy chạy hai tìm kiếm theo chiều rộng:
một từ $a$ và một từ $b$.
Giả sử $d_a []$ là mảng chứa khoảng cách ngắn nhất thu được từ BFS đầu tiên (từ $a$) và $d_b []$ là mảng chứa khoảng cách ngắn nhất thu được từ BFS thứ hai (từ $b$).
Bây giờ đối với mỗi đỉnh, thật dễ dàng để kiểm tra xem nó có nằm trên bất kỳ đường đi ngắn nhất nào giữa $a$ và $b$ hay không:
tiêu chí là điều kiện $d_a [v] + d_b [v] = d_a [b]$.

* Tìm hành trình (walk) ngắn nhất có độ dài chẵn từ một đỉnh nguồn $s$ đến một đỉnh đích $t$ trong một đồ thị không trọng số:
Để làm điều này, chúng ta phải xây dựng một đồ thị phụ trợ, có các đỉnh là trạng thái $(v, c)$, trong đó $v$ - nút hiện tại, $c = 0$ hoặc $c = 1$ - tính chẵn lẻ hiện tại.
Bất kỳ cạnh $(u, v)$ nào của đồ thị ban đầu trong cột mới này sẽ biến thành hai cạnh $((u, 0), (v, 1))$ và $((u, 1), (v, 0))$.
Sau đó, chúng ta chạy một BFS để tìm hành trình ngắn nhất từ đỉnh bắt đầu $(s, 0)$ đến đỉnh kết thúc $(t, 0)$.<br>**Lưu ý**: Mục này sử dụng thuật ngữ "_hành trình_" ("_walk_") thay vì "_đường đi_" ("_path_") vì một lý do, vì các đỉnh có thể lặp lại trong hành trình tìm thấy để làm cho độ dài của nó chẵn. Bài toán tìm _đường đi_ (path) ngắn nhất có độ dài chẵn là NP-Complete trong các đồ thị có hướng, và [có thể giải quyết trong thời gian tuyến tính](https://onlinelibrary.wiley.com/doi/abs/10.1002/net.3230140403) trong các đồ thị vô hướng, nhưng với một cách tiếp cận phức tạp hơn nhiều.

## Bài tập (Practice Problems) {: #practice-problems}

* [SPOJ: AKBAR](http://spoj.com/problems/AKBAR)
* [SPOJ: NAKANJ](http://www.spoj.com/problems/NAKANJ/)
* [SPOJ: WATER](http://www.spoj.com/problems/WATER)
* [SPOJ: MICE AND MAZE](http://www.spoj.com/problems/MICEMAZE/)
* [Timus: Caravans](http://acm.timus.ru/problem.aspx?space=1&num=2034)
* [DevSkill - Holloween Party (archived)](http://web.archive.org/web/20200930162803/http://www.devskill.com/CodingProblems/ViewProblem/60)
* [DevSkill - Ohani And The Link Cut Tree (archived)](http://web.archive.org/web/20170216192002/http://devskill.com:80/CodingProblems/ViewProblem/150)
* [SPOJ - Spiky Mazes](http://www.spoj.com/problems/SPIKES/)
* [SPOJ - Four Chips (hard)](http://www.spoj.com/problems/ADV04F1/)
* [SPOJ - Inversion Sort](http://www.spoj.com/problems/INVESORT/)
* [Codeforces - Shortest Path](http://codeforces.com/contest/59/problem/E)
* [SPOJ - Yet Another Multiple Problem](http://www.spoj.com/problems/MULTII/)
* [UVA 11392 - Binary 3xType Multiple](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2387)
* [UVA 10968 - KuPellaKeS](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1909)
* [Codeforces - Police Stations](http://codeforces.com/contest/796/problem/D)
* [Codeforces - Okabe and City](http://codeforces.com/contest/821/problem/D)
* [SPOJ - Find the Treasure](http://www.spoj.com/problems/DIGOKEYS/)
* [Codeforces - Bear and Forgotten Tree 2](http://codeforces.com/contest/653/problem/E)
* [Codeforces - Cycle in Maze](http://codeforces.com/contest/769/problem/C)
* [UVA - 11312 - Flipping Frustration](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2287)
* [SPOJ - Ada and Cycle](http://www.spoj.com/problems/ADACYCLE/)
* [CSES - Labyrinth](https://cses.fi/problemset/task/1193)
* [CSES - Message Route](https://cses.fi/problemset/task/1667/)
* [CSES - Monsters](https://cses.fi/problemset/task/1194)
