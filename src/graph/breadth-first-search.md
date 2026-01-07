---
tags:
  - Translated
e_maxx_link: bfs
---

# Tìm kiếm theo chiều rộng (BFS)

Tìm kiếm theo chiều rộng (Breadth-first search - BFS) là một trong những thuật toán tìm kiếm cơ bản và thiết yếu trên đồ thị.

Do cách hoạt động của thuật toán, đường đi được tìm thấy bởi BFS đến bất kỳ đỉnh nào cũng là đường đi ngắn nhất đến đỉnh đó, tức là đường đi chứa số cạnh ít nhất trong các đồ thị không có trọng số.

Thuật toán hoạt động trong thời gian $O(n + m)$, trong đó $n$ là số đỉnh và $m$ là số cạnh.

## Mô tả thuật toán

Thuật toán nhận đầu vào là một đồ thị không có trọng số và ID của đỉnh nguồn $s$. Đồ thị đầu vào có thể là đồ thị có hướng hoặc vô hướng, điều này không ảnh hưởng đến thuật toán.

Thuật toán có thể được hiểu như một đám cháy lan trên đồ thị: ở bước thứ không, chỉ có đỉnh nguồn $s$ bị cháy. Ở mỗi bước, ngọn lửa đang cháy tại mỗi đỉnh sẽ lan sang tất cả các đỉnh kề của nó. Trong một lần lặp của thuật toán, "vòng lửa" được mở rộng ra một đơn vị chiều rộng (do đó có tên của thuật toán).

Chính xác hơn, thuật toán có thể được phát biểu như sau: Tạo một hàng đợi $q$ chứa các đỉnh cần xử lý và một mảng Boolean $used[]$ cho biết mỗi đỉnh đã được đốt cháy (hoặc đã được thăm) hay chưa.

Ban đầu, đẩy đỉnh nguồn $s$ vào hàng đợi và đặt $used[s] = true$, và với tất cả các đỉnh $v$ khác, đặt $used[v] = false$.
Sau đó, lặp cho đến khi hàng đợi rỗng và trong mỗi lần lặp, lấy một đỉnh ra khỏi đầu hàng đợi. Lặp qua tất cả các cạnh đi ra từ đỉnh này và nếu một số cạnh này đi đến các đỉnh chưa bị cháy, hãy đốt cháy chúng và đặt chúng vào hàng đợi.

Kết quả là, khi hàng đợi rỗng, "vòng lửa" chứa tất cả các đỉnh có thể đến được từ nguồn $s$, với mỗi đỉnh được đến theo cách ngắn nhất có thể.
Bạn cũng có thể tính độ dài của các đường đi ngắn nhất (chỉ cần duy trì một mảng độ dài đường đi $d[]$) cũng như lưu thông tin để khôi phục tất cả các đường đi ngắn nhất này (đối với điều này, cần duy trì một mảng "cha" $p[]$, lưu trữ cho mỗi đỉnh đỉnh mà chúng ta đã đến từ đó).

## Cài đặt

Chúng tôi viết mã cho thuật toán được mô tả bằng C++ và Java.

=== "C++"
    ```cpp
    vector<vector<int>> adj;  // biểu diễn bằng danh sách kề
    int n; // số đỉnh
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
    ArrayList<ArrayList<Integer>> adj = new ArrayList<>(); // biểu diễn bằng danh sách kề
        
    int n; // số đỉnh
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
    
Nếu chúng ta phải khôi phục và hiển thị đường đi ngắn nhất từ nguồn đến một đỉnh $u$ nào đó, có thể thực hiện như sau:
    
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
    
## Ứng dụng của BFS

* Tìm đường đi ngắn nhất từ một đỉnh nguồn đến các đỉnh khác trong một đồ thị không có trọng số.

* Tìm tất cả các thành phần liên thông trong một đồ thị vô hướng trong thời gian $O(n + m)$:
Để làm điều này, chúng ta chỉ cần chạy BFS bắt đầu từ mỗi đỉnh, ngoại trừ các đỉnh đã được thăm từ các lần chạy trước.
Do đó, chúng ta thực hiện BFS bình thường từ mỗi đỉnh, nhưng không đặt lại mảng $used[]$ mỗi khi chúng ta có một thành phần liên thông mới, và tổng thời gian chạy vẫn sẽ là $O(n + m)$ (thực hiện nhiều BFS trên đồ thị mà không đặt lại mảng $used []$ được gọi là một chuỗi các tìm kiếm theo chiều rộng).

* Tìm giải pháp cho một bài toán hoặc một trò chơi với số lần di chuyển ít nhất, nếu mỗi trạng thái của trò chơi có thể được biểu diễn bằng một đỉnh của đồ thị, và các chuyển đổi từ trạng thái này sang trạng thái khác là các cạnh của đồ thị.

* Tìm đường đi ngắn nhất trong một đồ thị có trọng số 0 hoặc 1:
Điều này chỉ cần một sửa đổi nhỏ cho tìm kiếm theo chiều rộng thông thường: Thay vì duy trì mảng $used[]$, bây giờ chúng ta sẽ kiểm tra xem khoảng cách đến đỉnh có ngắn hơn khoảng cách hiện tại đã tìm thấy hay không, sau đó nếu cạnh hiện tại có trọng số bằng không, chúng ta thêm nó vào đầu hàng đợi, nếu không chúng ta thêm nó vào cuối hàng đợi. Sửa đổi này được giải thích chi tiết hơn trong bài viết [0-1 BFS](01_bfs.md).

* Tìm chu trình ngắn nhất trong một đồ thị có hướng không có trọng số:
Bắt đầu một tìm kiếm theo chiều rộng từ mỗi đỉnh.
Ngay khi chúng ta cố gắng đi từ đỉnh hiện tại trở lại đỉnh nguồn, chúng ta đã tìm thấy chu trình ngắn nhất chứa đỉnh nguồn.
Tại thời điểm này, chúng ta có thể dừng BFS và bắt đầu một BFS mới từ đỉnh tiếp theo.
Từ tất cả các chu trình như vậy (tối đa một chu trình từ mỗi BFS), chọn chu trình ngắn nhất.

* Tìm tất cả các cạnh nằm trên bất kỳ đường đi ngắn nhất nào giữa một cặp đỉnh cho trước $(a, b)$.
Để làm điều này, chạy hai tìm kiếm theo chiều rộng:
một từ $a$ và một từ $b$.
Gọi $d_a []$ là mảng chứa các khoảng cách ngắn nhất thu được từ BFS đầu tiên (từ $a$) và $d_b []$ là mảng chứa các khoảng cách ngắn nhất thu được từ BFS thứ hai từ $b$.
Bây giờ với mọi cạnh $(u, v)$, dễ dàng kiểm tra xem cạnh đó có nằm trên bất kỳ đường đi ngắn nhất nào giữa $a$ và $b$ hay không:
tiêu chí là điều kiện $d_a [u] + 1 + d_b [v] = d_a [b]$.

* Tìm tất cả các đỉnh trên bất kỳ đường đi ngắn nhất nào giữa một cặp đỉnh cho trước $(a, b)$.
Để thực hiện điều đó, chạy hai tìm kiếm theo chiều rộng:
một từ $a$ và một từ $b$.
Gọi $d_a []$ là mảng chứa các khoảng cách ngắn nhất thu được từ BFS đầu tiên (từ $a$) và $d_b []$ là mảng chứa các khoảng cách ngắn nhất thu được từ BFS thứ hai (từ $b$).
Bây giờ với mỗi đỉnh, dễ dàng kiểm tra xem nó có nằm trên bất kỳ đường đi ngắn nhất nào giữa $a$ và $b$ hay không:
tiêu chí là điều kiện $d_a [v] + d_b [v] = d_a [b]$.

* Tìm đường đi bộ (walk) ngắn nhất có độ dài chẵn từ một đỉnh nguồn $s$ đến một đỉnh đích $t$ trong một đồ thị không có trọng số:
Để làm điều này, chúng ta phải xây dựng một đồ thị phụ, có các đỉnh là trạng thái $(v, c)$, trong đó $v$ - đỉnh hiện tại, $c = 0$ hoặc $c = 1$ - tính chẵn lẻ hiện tại.
Bất kỳ cạnh nào $(u, v)$ của đồ thị gốc trong cột mới này sẽ biến thành hai cạnh $((u, 0), (v, 1))$ và $((u, 1), (v, 0))$.
Sau đó, chúng ta chạy một BFS để tìm đường đi bộ ngắn nhất từ đỉnh bắt đầu $(s, 0)$ đến đỉnh cuối $(t, 0)$.<br>**Lưu ý**: Mục này sử dụng thuật ngữ "_đường đi bộ_" (walk) thay vì "_đường đi_" (path) vì một lý do, vì các đỉnh có thể lặp lại trong đường đi bộ được tìm thấy để làm cho độ dài của nó chẵn. Bài toán tìm _đường đi_ ngắn nhất có độ dài chẵn là NP-Complete trong đồ thị có hướng, và [có thể giải quyết trong thời gian tuyến tính](https://onlinelibrary.wiley.com/doi/abs/10.1002/net.3230140403) trong đồ thị vô hướng, nhưng với một cách tiếp cận phức tạp hơn nhiều.

## Bài tập thực hành

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