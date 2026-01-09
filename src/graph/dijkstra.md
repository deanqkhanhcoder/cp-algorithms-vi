---
tags:
  - Translated
e_maxx_link: dijkstra
---

# Thuật toán Dijkstra (Dijkstra Algorithm) {: #dijkstra-algorithm}

Bạn được cho một đồ thị có trọng số có hướng hoặc vô hướng với $n$ đỉnh và $m$ cạnh. Trọng số của tất cả các cạnh là không âm. Bạn cũng được cho một đỉnh bắt đầu $s$. Bài viết này thảo luận về việc tìm độ dài của các đường đi ngắn nhất từ một đỉnh bắt đầu $s$ đến tất cả các đỉnh khác, và đưa ra chính các đường đi ngắn nhất.

Bài toán này cũng được gọi là **bài toán đường đi ngắn nhất từ một nguồn đơn** (**single-source shortest paths problem**).

## Thuật toán (Algorithm) {: #algorithm}

Dưới đây là một thuật toán được mô tả bởi nhà khoa học máy tính người Hà Lan Edsger W. Dijkstra vào năm 1959.

Hãy tạo một mảng $d[]$ trong đó với mỗi đỉnh $v$ chúng ta lưu trữ độ dài hiện tại của đường đi ngắn nhất từ $s$ đến $v$ trong $d[v]$.
Ban đầu $d[s] = 0$, và đối với tất cả các đỉnh khác, độ dài này bằng vô cùng.
Trong cài đặt, một số đủ lớn (được đảm bảo lớn hơn bất kỳ độ dài đường đi nào có thể) được chọn làm vô cùng.

$$d[v] = \infty,~ v \ne s$$

Ngoài ra, chúng ta duy trì một mảng Boolean $u[]$ lưu trữ cho mỗi đỉnh $v$ xem nó đã được đánh dấu hay chưa. Ban đầu tất cả các đỉnh đều chưa được đánh dấu:

$$u[v] = {\rm false}$$

Thuật toán Dijkstra chạy trong $n$ lần lặp. Tại mỗi lần lặp, một đỉnh $v$ được chọn là đỉnh chưa được đánh dấu có giá trị $d[v]$ nhỏ nhất:

Rõ ràng, trong lần lặp đầu tiên, đỉnh bắt đầu $s$ sẽ được chọn.

Đỉnh $v$ được chọn sẽ được đánh dấu. Tiếp theo, từ đỉnh $v$, các thao tác **nới lỏng** (relaxations) được thực hiện: tất cả các cạnh có dạng $(v,\text{to})$ được xem xét, và đối với mỗi đỉnh $\text{to}$, thuật toán cố gắng cải thiện giá trị $d[\text{to}]$. Nếu độ dài của cạnh hiện tại bằng $len$, mã cho thao tác nới lỏng là:

$$d[\text{to}] = \min (d[\text{to}], d[v] + len)$$

Sau khi tất cả các cạnh như vậy được xem xét, lần lặp hiện tại kết thúc. Cuối cùng, sau $n$ lần lặp, tất cả các đỉnh sẽ được đánh dấu, và thuật toán kết thúc. Chúng tôi khẳng định rằng các giá trị tìm được $d[v]$ là độ dài của các đường đi ngắn nhất từ $s$ đến tất cả các đỉnh $v$.

Lưu ý rằng nếu một số đỉnh không thể đến được từ đỉnh bắt đầu $s$, các giá trị $d[v]$ cho chúng sẽ vẫn là vô cùng. Rõ ràng, vài lần lặp cuối cùng của thuật toán sẽ chọn những đỉnh đó, nhưng sẽ không có công việc hữu ích nào được thực hiện cho chúng. Do đó, thuật toán có thể dừng lại ngay khi đỉnh được chọn có khoảng cách đến nó là vô cùng.

### Khôi phục đường đi ngắn nhất (Restoring Shortest Paths) {: #restoring-shortest-paths}

Thông thường người ta cần biết không chỉ độ dài của các đường đi ngắn nhất mà còn cả bản thân các đường đi ngắn nhất. Hãy xem cách duy trì thông tin đủ để khôi phục đường đi ngắn nhất từ $s$ đến bất kỳ đỉnh nào. Chúng ta sẽ duy trì một mảng các tiền bối (predecessors) $p[]$ trong đó đối với mỗi đỉnh $v \ne s$, $p[v]$ là đỉnh áp chót trong đường đi ngắn nhất từ $s$ đến $v$. Ở đây chúng ta sử dụng thực tế là nếu chúng ta lấy đường đi ngắn nhất đến một đỉnh $v$ nào đó và loại bỏ $v$ khỏi đường đi này, chúng ta sẽ nhận được một đường đi kết thúc tại đỉnh $p[v]$, và đường đi này sẽ là ngắn nhất cho đỉnh $p[v]$. Mảng các tiền bối này có thể được sử dụng để khôi phục đường đi ngắn nhất đến bất kỳ đỉnh nào: bắt đầu với $v$, liên tục lấy tiền bối của đỉnh hiện tại cho đến khi chúng ta đến đỉnh bắt đầu $s$ để nhận được đường đi ngắn nhất cần thiết với các đỉnh được liệt kê theo thứ tự ngược lại. Vì vậy, đường đi ngắn nhất $P$ đến đỉnh $v$ bằng:

$$P = (s, \ldots, p[p[p[v]]], p[p[v]], p[v], v)$$

Việc xây dựng mảng các tiền bối này rất đơn giản: đối với mỗi lần nới lỏng thành công, tức là khi đối với một số đỉnh đã chọn $v$, có sự cải thiện về khoảng cách đến một số đỉnh $\text{to}$, chúng ta cập nhật đỉnh tiền bối cho $\text{to}$ bằng đỉnh $v$:

$$p[\text{to}] = v$$

## Chứng minh (Proof) {: #proof}

Khẳng định chính mà tính đúng đắn của thuật toán Dijkstra dựa trên đó là:

**Sau khi bất kỳ đỉnh $v$ nào được đánh dấu, khoảng cách hiện tại đến nó $d[v]$ là ngắn nhất, và sẽ không thay đổi nữa.**

Chứng minh được thực hiện bằng quy nạp. Đối với lần lặp đầu tiên, phát biểu này là hiển nhiên: đỉnh duy nhất được đánh dấu là $s$, và khoảng cách đến là $d[s] = 0$ thực sự là độ dài của đường đi ngắn nhất đến $s$. Bây giờ giả sử phát biểu này đúng cho tất cả các lần lặp trước, tức là cho tất cả các đỉnh đã được đánh dấu; hãy chứng minh rằng nó không bị vi phạm sau khi lần lặp hiện tại hoàn thành. Gọi $v$ là đỉnh được chọn trong lần lặp hiện tại, tức là $v$ là đỉnh mà thuật toán sẽ đánh dấu. Bây giờ chúng ta phải chứng minh rằng $d[v]$ thực sự bằng độ dài của đường đi ngắn nhất đến nó $l[v]$.

Xem xét đường đi ngắn nhất $P$ đến đỉnh $v$. Đường đi này có thể được chia thành hai phần: $P_1$ chỉ bao gồm các nút được đánh dấu (ít nhất là đỉnh bắt đầu $s$ là một phần của $P_1$), và phần còn lại của đường đi $P_2$ (nó có thể bao gồm một đỉnh được đánh dấu, nhưng nó luôn bắt đầu bằng một đỉnh chưa được đánh dấu). Hãy ký hiệu đỉnh đầu tiên của đường đi $P_2$ là $p$, và đỉnh cuối cùng của đường đi $P_1$ là $q$.

Đầu tiên chúng ta chứng minh phát biểu của mình cho đỉnh $p$, tức là hãy chứng minh rằng $d[p] = l[p]$.
Điều này gần như hiển nhiên: trong một trong những lần lặp trước đó, chúng ta đã chọn đỉnh $q$ và thực hiện nới lỏng từ nó.
Vì (theo lựa chọn đỉnh $p$) đường đi ngắn nhất đến $p$ là đường đi ngắn nhất đến $q$ cộng với cạnh $(p,q)$, việc nới lỏng từ $q$ đặt giá trị của $d[p]$ thành độ dài của đường đi ngắn nhất $l[p]$.

Vì trọng số của các cạnh là không âm, độ dài của đường đi ngắn nhất $l[p]$ (mà chúng ta vừa chứng minh bằng $d[p]$) không vượt quá độ dài $l[v]$ của đường đi ngắn nhất đến đỉnh $v$. Cho rằng $l[v] \le d[v]$ (bởi vì thuật toán Dijkstra không thể tìm thấy một cách ngắn hơn cách ngắn nhất có thể), chúng ta nhận được bất đẳng thức:

$$d[p] = l[p] \le l[v] \le d[v]$$

Mặt khác, vì cả hai đỉnh $p$ và $v$ đều chưa được đánh dấu, và lần lặp hiện tại đã chọn đỉnh $v$, chứ không phải $p$, chúng ta nhận được một bất đẳng thức khác:

$$d[p] \ge d[v]$$

Từ hai bất đẳng thức này, chúng ta kết luận rằng $d[p] = d[v]$, và sau đó từ các phương trình đã tìm thấy trước đó, chúng ta nhận được:

$$d[v] = l[v]$$

Q.E.D.

## Cài đặt (Implementation) {: #implementation}

Thuật toán Dijkstra thực hiện $n$ lần lặp. Trong mỗi lần lặp, nó chọn một đỉnh chưa được đánh dấu $v$ với giá trị thấp nhất $d[v]$, đánh dấu nó và kiểm tra tất cả các cạnh $(v, \text{to})$ cố gắng cải thiện giá trị $d[\text{to}]$.

Thời gian chạy của thuật toán bao gồm:

* $n$ lần tìm kiếm một đỉnh có giá trị nhỏ nhất $d[v]$ trong số $O(n)$ đỉnh chưa được đánh dấu
* $m$ lần thử nới lỏng

Đối với cách cài đặt đơn giản nhất của các thao tác này, trên mỗi lần lặp, tìm kiếm đỉnh yêu cầu $O(n)$ thao tác, và mỗi lần nới lỏng có thể được thực hiện trong $O(1)$. Do đó, hành vi tiệm cận kết quả của thuật toán là:

$$O(n^2+m)$$

Độ phức tạp này là tối ưu cho đồ thị dày, tức là khi $m \approx n^2$.
Tuy nhiên, trong các đồ thị thưa, khi $m$ nhỏ hơn nhiều so với số lượng cạnh tối đa $n^2$, bài toán có thể được giải quyết với độ phức tạp $O(n \log n + m)$. Thuật toán và cài đặt có thể được tìm thấy trong bài viết [Dijkstra trên đồ thị thưa](dijkstra-sparse.md).
```cpp title="dijkstra_dense"
const int INF = 1000000000;
vector<vector<pair<int, int>>> adj;

void dijkstra(int s, vector<int> & d, vector<int> & p) {
    int n = adj.size();
    d.assign(n, INF);
    p.assign(n, -1);
    vector<bool> u(n, false);

    d[s] = 0;
    for (int i = 0; i < n; i++) {
        int v = -1;
        for (int j = 0; j < n; j++) {
            if (!u[j] && (v == -1 || d[j] < d[v]))
                v = j;
        }
        
        if (d[v] == INF)
            break;
        
        u[v] = true;
        for (auto edge : adj[v]) {
            int to = edge.first;
            int len = edge.second;
            
            if (d[v] + len < d[to]) {
                d[to] = d[v] + len;
                p[to] = v;
            }
        }
    }
}
```

Ở đây đồ thị $\text{adj}$ được lưu trữ dưới dạng danh sách kề: đối với mỗi đỉnh $v$, $\text{adj}[v]$ chứa danh sách các cạnh đi từ đỉnh này, tức là danh sách `pair<int,int>` trong đó phần tử đầu tiên trong cặp là đỉnh ở đầu kia của cạnh, và phần tử thứ hai là trọng số cạnh.

Hàm nhận đỉnh bắt đầu $s$ và hai vector sẽ được sử dụng làm giá trị trả về.

Trước hết, mã khởi tạo các mảng: khoảng cách $d[]$, nhãn $u[]$ và tiền bối $p[]$. Sau đó nó thực hiện $n$ lần lặp. Tại mỗi lần lặp, đỉnh $v$ được chọn có khoảng cách nhỏ nhất $d[v]$ trong số tất cả các đỉnh chưa được đánh dấu. Nếu khoảng cách đến đỉnh đã chọn $v$ bằng vô cùng, thuật toán dừng lại. Ngược lại, đỉnh được đánh dấu và tất cả các cạnh đi ra từ đỉnh này được kiểm tra. Nếu việc nới lỏng dọc theo cạnh là có thể (tức là khoảng cách $d[\text{to}]$ có thể được cải thiện), khoảng cách $d[\text{to}]$ và tiền bối $p[\text{to}]$ được cập nhật.

Sau khi thực hiện tất cả các lần lặp, mảng $d[]$ lưu trữ độ dài của các đường đi ngắn nhất đến tất cả các đỉnh, và mảng $p[]$ lưu trữ các tiền bối của tất cả các đỉnh (ngoại trừ đỉnh bắt đầu $s$). Đường đi đến bất kỳ đỉnh $t$ nào cũng có thể được khôi phục theo cách sau:
```cpp title="dijkstra_restore_path"
vector<int> restore_path(int s, int t, vector<int> const& p) {
    vector<int> path;

    for (int v = t; v != s; v = p[v])
        path.push_back(v);
    path.push_back(s);

    reverse(path.begin(), path.end());
    return path;
}
```

## Tham khảo (References) {: #references}

* Edsger Dijkstra. A note on two problems in connexion with graphs [1959]
* Thomas Cormen, Charles Leiserson, Ronald Rivest, Clifford Stein. Introduction to Algorithms [2005]

## Bài tập (Practice Problems) {: #practice-problems}
* [Timus - Ivan's Car](http://acm.timus.ru/problem.aspx?space=1&num=1930) [Difficulty:Medium]
* [Timus - Sightseeing Trip](http://acm.timus.ru/problem.aspx?space=1&num=1004)
* [SPOJ - SHPATH](http://www.spoj.com/problems/SHPATH/) [Difficulty:Easy]
* [Codeforces - Dijkstra?](http://codeforces.com/problemset/problem/20/C) [Difficulty:Easy]
* [Codeforces - Shortest Path](http://codeforces.com/problemset/problem/59/E)
* [Codeforces - Jzzhu and Cities](http://codeforces.com/problemset/problem/449/B)
* [Codeforces - The Classic Problem](http://codeforces.com/problemset/problem/464/E)
* [Codeforces - President and Roads](http://codeforces.com/problemset/problem/567/E)
* [Codeforces - Complete The Graph](http://codeforces.com/problemset/problem/715/B)
* [TopCoder - SkiResorts](https://community.topcoder.com/stat?c=problem_statement&pm=12468)
* [TopCoder - MaliciousPath](https://community.topcoder.com/stat?c=problem_statement&pm=13596)
* [SPOJ - Ada and Trip](http://www.spoj.com/problems/ADATRIP/)
* [LA - 3850 - Here We Go(relians) Again](https://vjudge.net/problem/UVALive-3850)
* [GYM - Destination Unknown (D)](http://codeforces.com/gym/100625)
* [UVA 12950 - Even Obsession](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=4829)
* [GYM - Journey to Grece (A)](http://codeforces.com/gym/100753)
* [UVA 13030 - Brain Fry](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=866&page=show_problem&problem=4918)
* [UVA 1027 - Toll](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=3468)
* [UVA 11377 - Airport Setup](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=2372)
* [Codeforces - Dynamic Shortest Path](http://codeforces.com/problemset/problem/843/D)
* [UVA 11813 - Shopping](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2913)
* [UVA 11833 - Route Change](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=226&page=show_problem&problem=2933)
* [SPOJ - Easy Dijkstra Problem](http://www.spoj.com/problems/EZDIJKST/en/)
* [LA - 2819 - Cave Raider](https://vjudge.net/problem/UVALive-2819)
* [UVA 12144 - Almost Shortest Path](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=3296)
* [UVA 12047 - Highest Paid Toll](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3198)
* [UVA 11514 - Batman](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=2509)
* [Codeforces - Team Rocket Rises Again](http://codeforces.com/contest/757/problem/F)
* [UVA - 11338 - Minefield](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2313)
* [UVA 11374 - Airport Express](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2369)
* [UVA 11097 - Poor My Problem](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2038)
* [UVA 13172 - The music teacher](https://uva.onlinejudge.org/index.php?option=onlinejudge&Itemid=8&page=show_problem&problem=5083)
* [Codeforces - Dirty Arkady's Kitchen](http://codeforces.com/contest/827/problem/F)
* [SPOJ - Delivery Route](http://www.spoj.com/problems/DELIVER/)
* [SPOJ - Costly Chess](http://www.spoj.com/problems/CCHESS/)
* [CSES - Shortest Routes 1](https://cses.fi/problemset/task/1671)
* [CSES - Flight Discount](https://cses.fi/problemset/task/1195)
* [CSES - Flight Routes](https://cses.fi/problemset/task/1196)
