--- 
tags:
  - Translated
  - Vietnamese
e_maxx_link: dijkstra
---

# Thuật toán Dijkstra

Bạn được cho một đồ thị có hướng hoặc vô hướng có trọng số với $n$ đỉnh và $m$ cạnh. Trọng số của tất cả các cạnh là không âm. Bạn cũng được cho một đỉnh bắt đầu $s$. Bài viết này thảo luận về việc tìm độ dài của các đường đi ngắn nhất từ một đỉnh bắt đầu $s$ đến tất cả các đỉnh khác, và xuất ra các đường đi ngắn nhất đó.

Bài toán này còn được gọi là **bài toán đường đi ngắn nhất từ một nguồn**.

## Thuật toán

Đây là một thuật toán được mô tả bởi nhà khoa học máy tính người Hà Lan Edsger W. Dijkstra vào năm 1959.

Hãy tạo một mảng $d[]$ trong đó với mỗi đỉnh $v$, chúng ta lưu trữ độ dài hiện tại của đường đi ngắn nhất từ $s$ đến $v$ trong $d[v]$.
Ban đầu $d[s] = 0$, và với tất cả các đỉnh khác, độ dài này bằng vô cùng.
Trong việc triển khai, một số đủ lớn (được đảm bảo lớn hơn bất kỳ độ dài đường đi nào có thể) được chọn làm vô cùng.

$$d[v] = \infty,~ v \ne s$$

Ngoài ra, chúng ta duy trì một mảng Boolean $u[]$ lưu trữ cho mỗi đỉnh $v$ xem nó có được đánh dấu hay không. Ban đầu tất cả các đỉnh đều chưa được đánh dấu:

$$u[v] = \rm false$$

Thuật toán của Dijkstra chạy trong $n$ lần lặp. Ở mỗi lần lặp, một đỉnh $v$ được chọn làm đỉnh chưa được đánh dấu có giá trị $d[v]$ nhỏ nhất:

Rõ ràng, trong lần lặp đầu tiên, đỉnh bắt đầu $s$ sẽ được chọn.

Đỉnh được chọn $v$ được đánh dấu. Tiếp theo, từ đỉnh $v$ thực hiện các **sự nới lỏng (relaxations)**: tất cả các cạnh có dạng $(v,\text{to})$ được xem xét, và với mỗi đỉnh $\text{to}$, thuật toán cố gắng cải thiện giá trị $d[\text{to}]$. Nếu độ dài của cạnh hiện tại bằng $len$, mã cho sự nới lỏng là:

$$d[\text{to}] = \min (d[\text{to}], d[v] + len)$$

Sau khi tất cả các cạnh như vậy được xem xét, lần lặp hiện tại kết thúc. Cuối cùng, sau $n$ lần lặp, tất cả các đỉnh sẽ được đánh dấu, và thuật toán kết thúc. Chúng tôi khẳng định rằng các giá trị $d[v]$ được tìm thấy là độ dài của các đường đi ngắn nhất từ $s$ đến tất cả các đỉnh $v$.

Lưu ý rằng nếu một số đỉnh không thể đến được từ đỉnh bắt đầu $s$, các giá trị $d[v]$ cho chúng sẽ vẫn là vô cùng. Rõ ràng, một vài lần lặp cuối cùng của thuật toán sẽ chọn các đỉnh đó, nhưng không có công việc hữu ích nào được thực hiện cho chúng. Do đó, thuật toán có thể được dừng lại ngay khi đỉnh được chọn có khoảng cách vô cùng đến nó.

### Khôi phục đường đi ngắn nhất 

Thường thì người ta cần biết không chỉ độ dài của các đường đi ngắn nhất mà còn cả các đường đi ngắn nhất đó. Hãy xem cách duy trì đủ thông tin để khôi phục đường đi ngắn nhất từ $s$ đến bất kỳ đỉnh nào. Chúng ta sẽ duy trì một mảng các đỉnh tiền nhiệm $p[]$ trong đó với mỗi đỉnh $v \ne s$, $p[v]$ là đỉnh áp chót trong đường đi ngắn nhất từ $s$ đến $v$. Ở đây chúng ta sử dụng thực tế là nếu chúng ta lấy đường đi ngắn nhất đến một đỉnh $v$ nào đó và loại bỏ $v$ khỏi đường đi này, chúng ta sẽ có một đường đi kết thúc tại đỉnh $p[v]$, và đường đi này sẽ là đường đi ngắn nhất cho đỉnh $p[v]$. Mảng các đỉnh tiền nhiệm này có thể được sử dụng để khôi phục đường đi ngắn nhất đến bất kỳ đỉnh nào: bắt đầu từ $v$, lặp đi lặp lại việc lấy đỉnh tiền nhiệm của đỉnh hiện tại cho đến khi chúng ta đến đỉnh bắt đầu $s$ để có được đường đi ngắn nhất cần thiết với các đỉnh được liệt kê theo thứ tự ngược lại. Vì vậy, đường đi ngắn nhất $P$ đến đỉnh $v$ bằng:

$$P = (s, \ldots, p[p[p[v]]], p[p[v]], p[v], v)$$

Xây dựng mảng các đỉnh tiền nhiệm này rất đơn giản: với mỗi lần nới lỏng thành công, tức là khi với một đỉnh $v$ được chọn nào đó, có sự cải thiện về khoảng cách đến một đỉnh $\text{to}$ nào đó, chúng ta cập nhật đỉnh tiền nhiệm cho $\text{to}$ bằng đỉnh $v$:

$$p[\text{to}] = v$$

## Chứng minh

Khẳng định chính mà tính đúng đắn của thuật toán Dijkstra dựa vào là như sau:

**Sau khi bất kỳ đỉnh $v$ nào được đánh dấu, khoảng cách hiện tại đến nó $d[v]$ là ngắn nhất, và sẽ không thay đổi nữa.**

Chứng minh được thực hiện bằng quy nạp. Đối với lần lặp đầu tiên, khẳng định này là rõ ràng: đỉnh được đánh dấu duy nhất là $s$, và khoảng cách đến nó là $d[s] = 0$ thực sự là độ dài của đường đi ngắn nhất đến $s$. Bây giờ giả sử khẳng định này đúng cho tất cả các lần lặp trước đó, tức là cho tất cả các đỉnh đã được đánh dấu; hãy chứng minh rằng nó không bị vi phạm sau khi lần lặp hiện tại hoàn thành. Gọi $v$ là đỉnh được chọn trong lần lặp hiện tại, tức là $v$ là đỉnh mà thuật toán sẽ đánh dấu. Bây giờ chúng ta phải chứng minh rằng $d[v]$ thực sự bằng độ dài của đường đi ngắn nhất đến nó $l[v]$.

Xét đường đi ngắn nhất $P$ đến đỉnh $v$. Đường đi này có thể được chia thành hai phần: $P_1$ chỉ bao gồm các nút đã được đánh dấu (ít nhất là đỉnh bắt đầu $s$ là một phần của $P_1$), và phần còn lại của đường đi $P_2$ (nó có thể bao gồm một đỉnh đã được đánh dấu, nhưng nó luôn bắt đầu bằng một đỉnh chưa được đánh dấu). Hãy ký hiệu đỉnh đầu tiên của đường đi $P_2$ là $p$, và đỉnh cuối cùng của đường đi $P_1$ là $q$.

Đầu tiên chúng ta chứng minh khẳng định của chúng ta cho đỉnh $p$, tức là hãy chứng minh rằng $d[p] = l[p]$.
Điều này gần như là rõ ràng: trong một trong các lần lặp trước đó, chúng ta đã chọn đỉnh $q$ và thực hiện nới lỏng từ nó.
Vì (nhờ việc chọn đỉnh $p$) đường đi ngắn nhất đến $p$ là đường đi ngắn nhất đến $q$ cộng với cạnh $(p,q)$, việc nới lỏng từ $q$ đã đặt giá trị của $d[p]$ thành độ dài của đường đi ngắn nhất $l[p]$.

Vì trọng số của các cạnh là không âm, độ dài của đường đi ngắn nhất $l[p]$ (mà chúng ta vừa chứng minh là bằng $d[p]$) không vượt quá độ dài $l[v]$ của đường đi ngắn nhất đến đỉnh $v$. Với việc $l[v] \le d[v]$ (vì thuật toán của Dijkstra không thể tìm thấy một đường đi ngắn hơn đường đi ngắn nhất có thể), chúng ta có được bất đẳng thức:

$$d[p] = l[p] \le l[v] \le d[v]$$

Mặt khác, vì cả hai đỉnh $p$ và $v$ đều chưa được đánh dấu, và lần lặp hiện tại đã chọn đỉnh $v$, không phải $p$, chúng ta có một bất đẳng thức khác:

$$d[p] \ge d[v]$$

Từ hai bất đẳng thức này, chúng ta kết luận rằng $d[p] = d[v]$, và sau đó từ các phương trình đã tìm thấy trước đó, chúng ta có:

$$d[v] = l[v]$$

Q.E.D.

## Cài đặt

Thuật toán của Dijkstra thực hiện $n$ lần lặp. Ở mỗi lần lặp, nó chọn một đỉnh chưa được đánh dấu $v$ có giá trị $d[v]$ nhỏ nhất, đánh dấu nó và kiểm tra tất cả các cạnh $(v, \text{to})$ cố gắng cải thiện giá trị $d[\text{to}]$.

Thời gian chạy của thuật toán bao gồm:

* $n$ lần tìm kiếm một đỉnh có giá trị $d[v]$ nhỏ nhất trong số $O(n)$ đỉnh chưa được đánh dấu
* $m$ lần thử nới lỏng

Đối với việc triển khai đơn giản nhất, ở mỗi lần lặp, việc tìm kiếm đỉnh yêu cầu $O(n)$ thao tác, và mỗi lần nới lỏng có thể được thực hiện trong $O(1)$. Do đó, độ phức tạp tiệm cận kết quả của thuật toán là:

$$O(n^2+m)$$

Độ phức tạp này là tối ưu cho đồ thị dày đặc, tức là khi $m \approx n^2$.
Tuy nhiên, trong các đồ thị thưa, khi $m$ nhỏ hơn nhiều so với số cạnh tối đa $n^2$, bài toán có thể được giải quyết với độ phức tạp $O(n \log n + m)$. Thuật toán và việc triển khai có thể được tìm thấy trong bài viết [Dijkstra trên đồ thị thưa](dijkstra_sparse.md).


```cpp
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

Ở đây đồ thị $\text{adj}$ được lưu trữ dưới dạng danh sách kề: với mỗi đỉnh $v$, $\text{adj}[v]$ chứa danh sách các cạnh đi ra từ đỉnh này, tức là danh sách `pair<int,int>` trong đó phần tử đầu tiên trong cặp là đỉnh ở đầu kia của cạnh, và phần tử thứ hai là trọng số cạnh.

Hàm nhận đỉnh bắt đầu $s$ và hai vector sẽ được sử dụng làm giá trị trả về.

Đầu tiên, mã khởi tạo các mảng: khoảng cách $d[]$, nhãn $u[]$ và các đỉnh tiền nhiệm $p[]$. Sau đó, nó thực hiện $n$ lần lặp. Ở mỗi lần lặp, đỉnh $v$ được chọn là đỉnh có khoảng cách $d[v]$ nhỏ nhất trong số tất cả các đỉnh chưa được đánh dấu. Nếu khoảng cách đến đỉnh được chọn $v$ bằng vô cùng, thuật toán dừng lại. Ngược lại, đỉnh được đánh dấu, và tất cả các cạnh đi ra từ đỉnh này được kiểm tra. Nếu có thể nới lỏng dọc theo cạnh (tức là khoảng cách $d[\text{to}]$ có thể được cải thiện), khoảng cách $d[\text{to}]$ và đỉnh tiền nhiệm $p[\text{to}]$ được cập nhật.

Sau khi thực hiện tất cả các lần lặp, mảng $d[]$ lưu trữ độ dài của các đường đi ngắn nhất đến tất cả các đỉnh, và mảng $p[]$ lưu trữ các đỉnh tiền nhiệm của tất cả các đỉnh (ngoại trừ đỉnh bắt đầu $s$). Đường đi đến bất kỳ đỉnh $t$ nào có thể được khôi phục theo cách sau:

```cpp
vector<int> restore_path(int s, int t, vector<int> const& p) {
    vector<int> path;

    for (int v = t; v != s; v = p[v])
        path.push_back(v);
    path.push_back(s);

    reverse(path.begin(), path.end());
    return path;
}
```

## Tài liệu tham khảo

*Edsger Dijkstra. A note on two problems in connexion with graphs [1959]
* Thomas Cormen, Charles Leiserson, Ronald Rivest, Clifford Stein. Introduction to Algorithms [2005]

## Bài tập thực hành
* [Timus - Ivan's Car](http://acm.timus.ru/problem.aspx?space=1&num=1930) [Độ khó: Trung bình]
* [Timus - Sightseeing Trip](http://acm.timus.ru/problem.aspx?space=1&num=1004)
* [SPOJ - SHPATH](http://www.spoj.com/problems/SHPATH/) [Độ khó: Dễ]
* [Codeforces - Dijkstra?](http://codeforces.com/problemset/problem/20/C) [Độ khó: Dễ]
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