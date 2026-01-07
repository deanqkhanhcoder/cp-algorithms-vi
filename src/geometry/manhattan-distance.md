---
tags:
  - Original
---

# Khoảng cách Manhattan
	
## Định nghĩa
Đối với các điểm $p$ và $q$ trên một mặt phẳng, chúng ta có thể định nghĩa khoảng cách giữa chúng là tổng của các hiệu giữa các tọa độ $x$ và $y$ của chúng: 

$$d(p,q) = |x_p - x_q| + |y_p - y_q|$$

Được định nghĩa theo cách này, khoảng cách tương ứng với cái gọi là [hình học Manhattan (taxi)](https://en.wikipedia.org/wiki/Taxicab_geometry), trong đó các điểm được coi là các giao lộ trong một thành phố được thiết kế tốt, như Manhattan, nơi bạn chỉ có thể di chuyển trên các đường phố theo chiều ngang hoặc chiều dọc, như được hiển thị trong hình ảnh dưới đây:

<div style="text-align: center;">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/Manhattan_distance.svg/220px-Manhattan_distance.svg.png" alt="Khoảng cách Manhattan">
</div>

Hình ảnh này cho thấy một số đường đi nhỏ nhất từ một điểm đen đến điểm kia, tất cả đều có độ dài $12$.

Có một số thủ thuật và thuật toán thú vị có thể được thực hiện với khoảng cách này, và chúng tôi sẽ trình bày một số trong số chúng ở đây.

## Cặp điểm xa nhất theo khoảng cách Manhattan

Cho $n$ điểm $P$, chúng ta muốn tìm cặp điểm $p,q$ cách xa nhau nhất, tức là, tối đa hóa $|x_p - x_q| + |y_p - y_q|$.

Hãy nghĩ trước tiên trong một chiều, vì vậy $y=0$. Quan sát chính là chúng ta có thể vét cạn nếu $|x_p - x_q|$ bằng $x_p - x_q$ hoặc $-x_p + x_q$, bởi vì nếu chúng ta "bỏ lỡ dấu" của giá trị tuyệt đối, chúng ta sẽ chỉ nhận được một giá trị nhỏ hơn, vì vậy nó không thể ảnh hưởng đến câu trả lời. Về mặt hình thức hơn, nó đúng rằng:

$$|x_p - x_q| = \max(x_p - x_q, -x_p + x_q)$$

Vì vậy, ví dụ, chúng ta có thể cố gắng có $p$ sao cho $x_p$ có dấu cộng, và sau đó $q$ phải có dấu âm. Bằng cách này, chúng ta muốn tìm:

$$\max\limits_{p, q \in P}(x_p + (-x_q)) = \max\limits_{p \in P}(x_p) + \max\limits_{q \in P}( - x_q ).$$

Lưu ý rằng chúng ta có thể mở rộng ý tưởng này hơn nữa cho 2 (hoặc nhiều hơn!) chiều. Đối với $d$ chiều, chúng ta phải vét cạn $2^d$ giá trị có thể có của các dấu. Ví dụ, nếu chúng ta ở trong $2$ chiều và vét cạn rằng $p$ có cả hai dấu cộng, chúng ta muốn tìm: 

$$\max\limits_{p, q \in P} [(x_p + (-x_q)) + (y_p + (-y_q))] = \max\limits_{p \in P}(x_p + y_p) + \max\limits_{q \in P}(-x_q - y_q).$$ 

Vì chúng ta đã làm cho $p$ và $q$ độc lập, bây giờ dễ dàng tìm thấy $p$ và $q$ tối đa hóa biểu thức.

Đoạn mã dưới đây tổng quát hóa điều này cho $d$ chiều và chạy trong $O(n \cdot 2^d \cdot d)$.

```cpp
long long ans = 0;
for (int msk = 0; msk < (1 << d); msk++) {
    long long mx = LLONG_MIN, mn = LLONG_MAX;
    for (int i = 0; i < n; i++) {
        long long cur = 0;
        for (int j = 0; j < d; j++) {
            if (msk & (1 << j)) cur += p[i][j];
            else cur -= p[i][j];
        }
        mx = max(mx, cur);
        mn = min(mn, cur);
    }
    ans = max(ans, mx - mn);
}
```

## Quay các điểm và khoảng cách Chebyshev

Nổi tiếng là, đối với mọi $m, n \in \mathbb{R}$,

$$|m| + |n| = \text{max}(|m + n|, |m - n|).$$ 

Để chứng minh điều này, chúng ta chỉ cần phân tích các dấu của $m$ và $n$. Và nó được để lại như một bài tập.

Chúng ta có thể áp dụng phương trình này cho công thức khoảng cách Manhattan để tìm ra rằng

$$d((x_1, y_1), (x_2, y_2)) = |x_1 - x_2| + |y_1 - y_2| = \text{max}(|(x_1 + y_1) - (x_2 + y_2)|, |(y_1 - x_1) - (y_2 - x_2)|).$$ 

Biểu thức cuối cùng trong phương trình trước đó là [khoảng cách Chebyshev](https://en.wikipedia.org/wiki/Chebyshev_distance) của các điểm $(x_1 + y_1, y_1 - x_1)$ và $(x_2 + y_2, y_2 - x_2)$. Điều này có nghĩa là, sau khi áp dụng phép biến đổi

$$\alpha : (x, y) \to (x + y, y - x),$$ 

khoảng cách Manhattan giữa các điểm $p$ và $q$ biến thành khoảng cách Chebyshev giữa $\alpha(p)$ và $\alpha(q)$.

Ngoài ra, chúng ta có thể nhận ra rằng $\alpha$ là một [phép đồng dạng xoắn ốc](https://en.wikipedia.org/wiki/Spiral_similarity) (phép quay của mặt phẳng theo sau là một phép co giãn về một tâm $O$) với tâm $(0, 0)$, góc quay $45^{\circ}$ theo chiều kim đồng hồ và co giãn bởi $\sqrt{2}$.

Đây là một hình ảnh để giúp hình dung phép biến đổi:

<div style="text-align: center;">
  <img src="chebyshev-transformation.png" alt="Phép biến đổi Chebyshev">
</div>

## Cây khung nhỏ nhất Manhattan

Bài toán Cây khung nhỏ nhất Manhattan bao gồm, cho một số điểm trên mặt phẳng, tìm các cạnh nối tất cả các điểm và có tổng trọng số nhỏ nhất. Trọng số của một cạnh nối hai điểm là khoảng cách Manhattan của chúng. Để đơn giản, chúng ta giả sử rằng tất cả các điểm có vị trí khác nhau.
Ở đây, chúng ta trình bày một cách tìm Cây khung nhỏ nhất trong $O(n \log{n})$ bằng cách tìm cho mỗi điểm láng giềng gần nhất của nó trong mỗi góc phần tám, như được biểu diễn trong hình ảnh dưới đây. Điều này sẽ cho chúng ta $O(n)$ cạnh ứng cử viên, mà, như chúng ta sẽ chỉ ra dưới đây, sẽ đảm bảo rằng chúng chứa Cây khung nhỏ nhất. Bước cuối cùng sau đó là sử dụng một số thuật toán Cây khung nhỏ nhất tiêu chuẩn, ví dụ, [thuật toán Kruskal sử dụng Disjoint Set Union](http://127.0.0.1:8000/graph/mst_kruskal_with_dsu.html).

<div style="text-align: center;">
  <img src="manhattan-mst-octants.png" alt="hình ảnh 8 góc phần tám">
  *8 góc phần tám so với một điểm S*
</div>

Thuật toán được trình bày ở đây lần đầu tiên được trình bày trong một bài báo của [H. Zhou, N. Shenoy, và W. Nichollos (2002)](https://ieeexplore.ieee.org/document/913303). Cũng có một thuật toán khác được biết đến sử dụng cách tiếp cận Chia để trị của [J. Stolfi](https://www.academia.edu/15667173/On_computing_all_north_east_nearest_neighbors_in_the_L1_metric), cũng rất thú vị và chỉ khác ở cách chúng tìm láng giềng gần nhất trong mỗi góc phần tám. Cả hai đều có cùng độ phức tạp, nhưng cái được trình bày ở đây dễ thực hiện hơn và có hệ số hằng số thấp hơn.

Đầu tiên, hãy hiểu tại sao chỉ cần xem xét láng giềng gần nhất trong mỗi góc phần tám là đủ. Ý tưởng là chỉ ra rằng đối với một điểm $s$ và bất kỳ hai điểm nào khác $p$ và $q$ trong cùng một góc phần tám, $d(p, q) < \max(d(s, p), d(s, q))$. Điều này quan trọng, bởi vì nó cho thấy rằng nếu có một Cây khung nhỏ nhất trong đó $s$ được kết nối với cả $p$ và $q$, chúng ta có thể xóa một trong những cạnh này và thêm cạnh $(p,q)$, điều này sẽ giảm tổng chi phí. Để chứng minh điều này, chúng ta giả sử không mất tính tổng quát rằng $p$ và $q$ nằm trong góc phần tám $R_1$, được định nghĩa bởi: $x_s \leq x$ và $x_s - y_s > x -  y$, và sau đó thực hiện một số trường hợp. Hình ảnh dưới đây đưa ra một số trực giác về lý do tại sao điều này đúng.

<div style="text-align: center;">
  <img src="manhattan-mst-uniqueness.png" alt="láng giềng gần nhất duy nhất">
  *Về mặt trực giác, sự giới hạn của góc phần tám làm cho không thể có chuyện cả $p$ và $q$ đều gần $s$ hơn so với nhau*
</div>


Do đó, câu hỏi chính là làm thế nào để tìm hiệu quả láng giềng gần nhất trong mỗi góc phần tám cho mỗi một trong $n$ điểm.

## Láng giềng gần nhất trong mỗi góc phần tám trong O(n log n)

Để đơn giản, chúng ta tập trung vào góc phần tám ĐĐB ($R_1$ trong hình ảnh trên). Tất cả các hướng khác có thể được tìm thấy với cùng một thuật toán bằng cách quay đầu vào.

Chúng ta sẽ sử dụng một cách tiếp cận đường quét. Chúng ta xử lý các điểm từ tây nam đến đông bắc, tức là, theo thứ tự không giảm của $x + y$. Chúng ta cũng giữ một tập hợp các điểm chưa có láng giềng gần nhất của chúng, mà chúng ta gọi là "tập hợp hoạt động". Chúng ta thêm các hình ảnh dưới đây để giúp hình dung thuật toán.

<div style="text-align: center;">
  <img src="manhattan-mst-sweep-line-1.png" alt="quét đường mst manhattan">
  *Màu đen với một mũi tên, bạn có thể thấy hướng của đường quét. Tất cả các điểm dưới đường này đều nằm trong tập hợp hoạt động, và các điểm phía trên vẫn chưa được xử lý. Màu xanh lá cây, chúng ta thấy các điểm nằm trong góc phần tám của điểm đã xử lý. Màu đỏ là các điểm không nằm trong góc phần tám được tìm kiếm.*
</div>

<div style="text-align: center;">
  <img src="manhattan-mst-sweep-line-2.png" alt="quét đường mst manhattan">
  *Trong hình ảnh này, chúng ta thấy tập hợp hoạt động sau khi xử lý điểm $p$. Lưu ý rằng 2 điểm màu xanh lá cây của hình ảnh trước đó có $p$ trong góc phần tám bắc-bắc-đông của chúng và không còn trong tập hợp hoạt động nữa, bởi vì chúng đã tìm thấy láng giềng gần nhất của chúng.*
</div>

Khi chúng ta thêm một điểm mới $p$, đối với mỗi điểm $s$ có nó trong góc phần tám của nó, chúng ta có thể gán $p$ một cách an toàn làm láng giềng gần nhất. Điều này đúng bởi vì khoảng cách của chúng là $d(p,s) = |x_p - x_s| + |y_p - y_s| = (x_p + y_p) - (x_s + y_s)$, bởi vì $p$ nằm trong góc phần tám bắc-bắc-đông. Vì tất cả các điểm tiếp theo sẽ không có giá trị nhỏ hơn của $x + y$ do bước sắp xếp, $p$ được đảm bảo có khoảng cách nhỏ hơn. Sau đó, chúng ta có thể loại bỏ tất cả các điểm như vậy khỏi tập hợp hoạt động, và cuối cùng thêm $p$ vào tập hợp hoạt động.

Câu hỏi tiếp theo là làm thế nào để tìm hiệu quả những điểm $s$ nào có $p$ trong góc phần tám bắc-bắc-đông. Tức là, những điểm $s$ nào thỏa mãn:

- $x_s \leq x_p$
- $x_p - y_p < x_s - y_s$

Bởi vì không có điểm nào trong tập hợp hoạt động nằm trong vùng $R_1$ của một điểm khác, chúng ta cũng có rằng đối với hai điểm $q_1$ và $q_2$ trong tập hợp hoạt động, $x_{q_1} \neq x_{q_2}$ và thứ tự của chúng ngụ ý $x_{q_1} < x_{q_2} \implies x_{q_1} - y_{q_1} \leq x_{q_2} - y_{q_2}$.

Bạn có thể cố gắng hình dung điều này trên các hình ảnh trên bằng cách nghĩ về thứ tự của $x - y$ như một "đường quét" đi từ tây-bắc đến đông-nam, tức là vuông góc với đường được vẽ.

Điều này có nghĩa là nếu chúng ta giữ tập hợp hoạt động được sắp xếp theo $x$, các ứng cử viên $s$ được đặt liên tiếp. Sau đó, chúng ta có thể tìm $x_s \leq x_p$ lớn nhất và xử lý các điểm theo thứ tự giảm dần của $x$ cho đến khi điều kiện thứ hai $x_p - y_p < x_s - y_s$ bị phá vỡ (chúng ta thực sự có thể cho phép $x_p - y_p = x_s - y_s$ và điều đó giải quyết trường hợp các điểm có tọa độ bằng nhau). Lưu ý rằng vì chúng ta xóa khỏi tập hợp ngay sau khi xử lý, điều này sẽ có độ phức tạp trừ dần là $O(n \log(n))$.
	Bây giờ chúng ta đã có điểm gần nhất theo hướng đông bắc, chúng ta quay các điểm và lặp lại. Có thể chỉ ra rằng thực tế chúng ta cũng tìm thấy bằng cách này điểm gần nhất theo hướng tây nam, vì vậy chúng ta có thể lặp lại chỉ 4 lần, thay vì 8.

Tóm lại, chúng ta:

- Sắp xếp các điểm theo $x + y$ theo thứ tự không giảm;
- Đối với mỗi điểm, chúng ta lặp qua tập hợp hoạt động bắt đầu từ điểm có $x$ lớn nhất sao cho $x \leq x_p$, và chúng ta phá vỡ vòng lặp nếu $x_p - y_p \geq x_s - y_s$. Đối với mỗi điểm hợp lệ $s$, chúng ta thêm cạnh $(s,p, d(s,p))$ vào danh sách của mình;
- Chúng ta thêm điểm $p$ vào tập hợp hoạt động;
- Quay các điểm và lặp lại cho đến khi chúng ta lặp qua tất cả các góc phần tám.
- Áp dụng thuật toán Kruskal trong danh sách các cạnh để có được Cây khung nhỏ nhất. 

Dưới đây bạn có thể tìm thấy một triển khai, dựa trên triển khai từ [KACTL](https://github.com/kth-competitive-programming/kactl/blob/main/content/geometry/ManhattanMST.h).

```{.cpp file=manhattan_mst}
struct point {
    long long x, y;
};

// Trả về một danh sách các cạnh ở định dạng (trọng số, u, v). 
// Truyền danh sách này cho thuật toán Kruskal sẽ cho ra Cây khung nhỏ nhất Manhattan.
vector<tuple<long long, int, int>> manhattan_mst_edges(vector<point> ps) {
    vector<int> ids(ps.size());
    iota(ids.begin(), ids.end(), 0);
    vector<tuple<long long, int, int>> edges;
    for (int rot = 0; rot < 4; rot++) { // cho mỗi lần quay
        sort(ids.begin(), ids.end(), [&](int i, int j){
            return (ps[i].x + ps[i].y) < (ps[j].x + ps[j].y);
        });
        map<int, int, greater<int>> active; // (xs, id)
        for (auto i : ids) {
            for (auto it = active.lower_bound(ps[i].x); it != active.end();
            active.erase(it++)) {
                int j = it->second;
                if (ps[i].x - ps[i].y > ps[j].x - ps[j].y) break;
                assert(ps[i].x >= ps[j].x && ps[i].y >= ps[j].y);
                edges.push_back({(ps[i].x - ps[j].x) + (ps[i].y - ps[j].y), i, j});
            }
            active[ps[i].x] = i;
        }
        for (auto &p : ps) { // quay
            if (rot & 1) p.x *= -1;
            else swap(p.x, p.y);
        }
    }
    return edges;
}
```

## Các bài toán
 * [AtCoder Beginner Contest 178E - Dist Max](https://atcoder.jp/contests/abc178/tasks/abc178_e)
 * [CodeForces 1093G - Multidimensional Queries](https://codeforces.com/contest/1093/problem/G)
 * [CodeForces 944F - Game with Tokens](https://codeforces.com/contest/944/problem/F)
 * [AtCoder Code Festival 2017D - Four Coloring](https://atcoder.jp/contests/code-festival-2017-quala/tasks/code_festival_2017_quala_d)
 * [The 2023 ICPC Asia EC Regionals Online Contest (I) - J. Minimum Manhattan Distance](https://codeforces.com/gym/104639/problem/J)
 * [Petrozavodsk Winter Training Camp 2016 Contest 4 - B. Airports](https://codeforces.com/group/eqgxxTNwgd/contest/100959/attachments)