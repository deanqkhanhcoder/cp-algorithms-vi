---
tags:
  - Translated
e_maxx_link: floyd_warshall_algorithm
---

# Thuật toán Floyd-Warshall (Floyd-Warshall Algorithm) {: #floyd-warshall-algorithm}

Cho một đồ thị có trọng số có hướng hoặc vô hướng $G$ với $n$ đỉnh.
Nhiệm vụ là tìm độ dài của đường đi ngắn nhất $d_{ij}$ giữa mỗi cặp đỉnh $i$ và $j$.

Đồ thị có thể có các cạnh trọng số âm, nhưng không có chu trình trọng số âm.

Nếu có một chu trình âm như vậy, bạn có thể chỉ cần đi qua chu trình này lặp đi lặp lại, trong mỗi lần lặp làm cho chi phí của đường đi nhỏ hơn.
Vì vậy, bạn có thể làm cho một số đường đi nhỏ tùy ý, hoặc nói cách khác là đường đi ngắn nhất không xác định.
Điều đó tự động có nghĩa là một đồ thị vô hướng không thể có bất kỳ cạnh trọng số âm nào, vì một cạnh như vậy đã tạo thành một chu trình âm vì bạn có thể di chuyển qua lại dọc theo cạnh đó bao lâu tùy thích.

Thuật toán này cũng có thể được sử dụng để phát hiện sự hiện diện của các chu trình âm.
Đồ thị có một chu trình âm nếu ở cuối thuật toán, khoảng cách từ một đỉnh $v$ đến chính nó là âm.

Thuật toán này đã được công bố đồng thời trong các bài báo của Robert Floyd và Stephen Warshall vào năm 1962.
Tuy nhiên, vào năm 1959, Bernard Roy đã công bố về cơ bản cùng một thuật toán, nhưng ấn phẩm của ông đã không được chú ý.

## Mô tả thuật toán (Description of the algorithm) {: #description-of-the-algorithm}

Ý tưởng chính của thuật toán là chia quá trình tìm đường đi ngắn nhất giữa bất kỳ hai đỉnh nào thành nhiều pha tăng dần.

Hãy đánh số các đỉnh bắt đầu từ 1 đến $n$.
Ma trận khoảng cách là $d[ ][ ]$.

Trước pha thứ $k$ ($k = 1 \dots n$), $d[i][j]$ cho bất kỳ đỉnh $i$ và $j$ nào lưu trữ độ dài của đường đi ngắn nhất giữa đỉnh $i$ và đỉnh $j$, chỉ chứa các đỉnh $\{1, 2, ..., k-1\}$ làm đỉnh trung gian (internal vertices) trong đường đi.

Nói cách khác, trước pha thứ $k$, giá trị của $d[i][j]$ bằng độ dài của đường đi ngắn nhất từ đỉnh $i$ đến đỉnh $j$, nếu đường đi này chỉ được phép đi vào đỉnh có số nhỏ hơn $k$ (đầu và cuối của đường đi không bị hạn chế bởi thuộc tính này).

Dễ dàng đảm bảo rằng thuộc tính này giữ cho pha đầu tiên. Với $k = 0$, chúng ta có thể điền vào ma trận với $d[i][j] = w_{i j}$ nếu tồn tại một cạnh giữa $i$ và $j$ với trọng số $w_{i j}$ và $d[i][j] = \infty$ nếu không tồn tại cạnh.
Trên thực tế $\infty$ sẽ là một giá trị lớn nào đó.
Như chúng ta sẽ thấy sau này, đây là một yêu cầu cho thuật toán.

Giả sử bây giờ chúng ta đang ở pha thứ $k$, và chúng ta muốn tính toán ma trận $d[ ][ ]$ để nó đáp ứng các yêu cầu cho pha thứ $(k + 1)$.
Chúng ta phải sửa khoảng cách cho một số cặp đỉnh $(i, j)$.
Có hai trường hợp khác nhau về cơ bản:

*   Đường đi ngắn nhất từ đỉnh $i$ đến đỉnh $j$ với các đỉnh trung gian từ tập hợp $\{1, 2, \dots, k\}$ trùng với đường đi ngắn nhất với các đỉnh trung gian từ tập hợp $\{1, 2, \dots, k-1\}$.

    Trong trường hợp này, $d[i][j]$ sẽ không thay đổi trong quá trình chuyển đổi.

*   Đường đi ngắn nhất với các đỉnh trung gian từ $\{1, 2, \dots, k\}$ ngắn hơn.

    Điều này có nghĩa là đường đi mới, ngắn hơn đi qua đỉnh $k$.
    Điều này có nghĩa là chúng ta có thể chia đường đi ngắn nhất giữa $i$ và $j$ thành hai đường đi:
    đường đi giữa $i$ và $k$, và đường đi giữa $k$ và $j$.
    Rõ ràng là cả hai đường đi này chỉ sử dụng các đỉnh trung gian của $\{1, 2, \dots, k-1\}$ và là những đường đi ngắn nhất như vậy trong khía cạnh đó.
    Do đó, chúng ta đã tính toán độ dài của các đường đi đó trước đó, và chúng ta có thể tính toán độ dài của đường đi ngắn nhất giữa $i$ và $j$ là $d[i][k] + d[k][j]$.

Kết hợp hai trường hợp này, chúng ta thấy rằng chúng ta có thể tính toán lại độ dài của tất cả các cặp $(i, j)$ trong pha thứ $k$ theo cách sau:

$$d_{\text{new}}[i][j] = min(d[i][j], d[i][k] + d[k][j])$$

Do đó, tất cả công việc cần thiết trong pha thứ $k$ là lặp qua tất cả các cặp đỉnh và tính toán lại độ dài của đường đi ngắn nhất giữa chúng.
Kết quả là, sau pha thứ $n$, giá trị $d[i][j]$ trong ma trận khoảng cách là độ dài của đường đi ngắn nhất giữa $i$ và $j$, hoặc là $\infty$ nếu đường đi giữa các đỉnh $i$ và $j$ không tồn tại.

Một nhận xét cuối cùng - chúng ta không cần tạo một ma trận khoảng cách riêng biệt $d_{\text{new}}[ ][ ]$ để lưu trữ tạm thời các đường đi ngắn nhất của pha thứ $k$, tức là tất cả các thay đổi có thể được thực hiện trực tiếp trong ma trận $d[ ][ ]$ ở bất kỳ pha nào.
Thực tế là ở bất kỳ pha thứ $k$ nào, chúng ta tối đa là cải thiện khoảng cách của bất kỳ đường đi nào trong ma trận khoảng cách, do đó chúng ta không thể làm xấu đi độ dài của đường đi ngắn nhất cho bất kỳ cặp đỉnh nào sẽ được xử lý trong pha thứ $(k+1)$ hoặc sau đó.

Độ phức tạp thời gian của thuật toán này rõ ràng là $O(n^3)$.

## Cài đặt (Implementation) {: #implementation}

Gọi $d[][]$ là một mảng 2D kích thước $n \times n$, được điền theo pha thứ 0 như giải thích trước đó.
Ngoài ra, chúng ta sẽ đặt $d[i][i] = 0$ cho bất kỳ $i$ nào ở pha thứ 0.

Sau đó thuật toán được cài đặt như sau:

```cpp
for (int k = 0; k < n; ++k) {
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            d[i][j] = min(d[i][j], d[i][k] + d[k][j]); 
        }
    }
}
```

Người ta giả định rằng nếu không có cạnh giữa bất kỳ hai đỉnh $i$ và $j$ nào, thì ma trận tại $d[i][j]$ chứa một số lớn (đủ lớn để nó lớn hơn độ dài của bất kỳ đường đi nào trong đồ thị này).
Khi đó cạnh này sẽ luôn không có lợi để đi, và thuật toán sẽ hoạt động chính xác.

Tuy nhiên, nếu có các cạnh trọng số âm trong đồ thị, các biện pháp đặc biệt phải được thực hiện.
Nếu không, các giá trị kết quả trong ma trận có thể có dạng $\infty - 1$,  $\infty - 2$, v.v., tất nhiên, vẫn chỉ ra rằng giữa các đỉnh tương ứng không tồn tại một đường đi.
Do đó, nếu đồ thị có các cạnh trọng số âm, tốt hơn là viết thuật toán Floyd-Warshall theo cách sau, để nó không thực hiện các chuyển đổi bằng cách sử dụng các đường đi không tồn tại.

```cpp
for (int k = 0; k < n; ++k) {
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (d[i][k] < INF && d[k][j] < INF)
                d[i][j] = min(d[i][j], d[i][k] + d[k][j]); 
        }
    }
}
```

## Khôi phục chuỗi các đỉnh trong đường đi ngắn nhất (Retrieving the sequence of vertices in the shortest path) {: #retrieving-sequence}

Dễ dàng duy trì thông tin bổ sung mà với nó sẽ có thể truy xuất đường đi ngắn nhất giữa bất kỳ hai đỉnh nào được đưa ra dưới dạng một chuỗi các đỉnh.

Để làm điều này, ngoài ma trận khoảng cách $d[ ][ ]$, một ma trận tổ tiên $p[ ][ ]$ phải được duy trì, sẽ chứa số của pha nơi khoảng cách ngắn nhất giữa hai đỉnh được sửa đổi lần cuối.
Rõ ràng là số của pha không là gì khác ngoài một đỉnh ở giữa đường đi ngắn nhất mong muốn.
Bây giờ chúng ta chỉ cần tìm đường đi ngắn nhất giữa các đỉnh $i$ và $p[i][j]$, và giữa $p[i][j]$ và $j$.
Điều này dẫn đến một thuật toán tái tạo đệ quy đơn giản của đường đi ngắn nhất.

## Trường hợp trọng số thực (The case of real weights) {: #case-of-real-weights}

Nếu trọng số của các cạnh không phải là số nguyên mà là số thực, cần phải tính đến các lỗi xảy ra khi làm việc với các kiểu float.

Thuật toán Floyd-Warshall có một hiệu ứng khó chịu, đó là các lỗi tích lũy rất nhanh.
Thực tế là nếu có một lỗi trong pha đầu tiên của $\delta$, lỗi này có thể lan truyền sang lần lặp thứ hai là $2 \delta$, sang lần lặp thứ ba là $4 \delta$, v.v.

Để tránh điều này, thuật toán có thể được sửa đổi để tính đến lỗi (EPS = $\delta$) bằng cách sử dụng so sánh sau:

```cpp
if (d[i][k] + d[k][j] < d[i][j] - EPS)
    d[i][j] = d[i][k] + d[k][j]; 
```

## Trường hợp chu trình âm (The case of negative cycles) {: #case-of-negative-cycles}

Về mặt hình thức, thuật toán Floyd-Warshall không áp dụng cho các đồ thị chứa (các) chu trình trọng số âm.
Nhưng đối với tất cả các cặp đỉnh $i$ và $j$ mà không tồn tại đường đi bắt đầu tại $i$, đi qua một chu trình âm và kết thúc tại $j$, thuật toán vẫn sẽ hoạt động chính xác.

Đối với cặp đỉnh mà câu trả lời không tồn tại (do sự hiện diện của một chu trình âm trong đường đi giữa chúng), thuật toán Floyd sẽ lưu trữ bất kỳ số nào (có thể là âm rất lớn, nhưng không nhất thiết) trong ma trận khoảng cách.
Tuy nhiên, có thể cải thiện thuật toán Floyd-Warshall, để nó xử lý cẩn thận các cặp đỉnh như vậy và xuất chúng, ví dụ như $-\text{INF}$.

Điều này có thể được thực hiện theo cách sau:
hãy chạy thuật toán Floyd-Warshall thông thường cho một đồ thị nhất định.
Khi đó một đường đi ngắn nhất giữa các đỉnh $i$ và $j$ không tồn tại, khi và chỉ khi, có một đỉnh $t$ sao cho, $t$ có thể tiếp cận từ $i$ và $j$ có thể tiếp cận từ $t$, mà $d[t][t] < 0$.

Ngoài ra, khi sử dụng thuật toán Floyd-Warshall cho các đồ thị có chu trình âm, chúng ta nên nhớ rằng các tình huống có thể phát sinh trong đó khoảng cách có thể đi vào số âm nhanh theo cấp số nhân.
Do đó, tràn số nguyên phải được xử lý bằng cách giới hạn khoảng cách tối thiểu bằng một giá trị nào đó (ví dụ: $-\text{INF}$).

Để tìm hiểu thêm về việc tìm các chu trình âm trong đồ thị, xem bài viết riêng [Tìm chu trình âm trong đồ thị](finding-negative-cycle-in-graph.md).

## Bài tập (Practice Problems) {: #practice-problems}
 - [UVA: Page Hopping](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=762)
 - [SPOJ: Possible Friends](http://www.spoj.com/problems/SOCIALNE/)
 - [CODEFORCES: Greg and Graph](http://codeforces.com/problemset/problem/295/B)
 - [SPOJ: CHICAGO - 106 miles to Chicago](http://www.spoj.com/problems/CHICAGO/)
 - [UVA 10724 - Road Construction](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1665)
 - [UVA  117 - The Postal Worker Rings Once](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=53)
 - [Codeforces - Traveling Graph](http://codeforces.com/problemset/problem/21/D)
 - [UVA - 1198 - The Geodetic Set Problem](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=3639)
 - [UVA - 10048 - Audiophobia](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=989)
 - [UVA - 125 - Numbering Paths](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=61)
 - [LOJ - Travel Company](http://lightoj.com/volume_showproblem.php?problem=1221)
 - [UVA 423 - MPI Maelstrom](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=364)
 - [UVA 1416 - Warfare And Logistics](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=4162)
 - [UVA 1233 - USHER](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3674)
 - [UVA 10793 - The Orc Attack](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1734)
 - [UVA 10099 The Tourist Guide](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1040)
 - [UVA 869 - Airline Comparison](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=810)
 - [UVA 13211 - Geonosis](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=5134)
 - [SPOJ - Defend the Rohan](http://www.spoj.com/problems/ROHAAN/)
 - [Codeforces - Roads in Berland](http://codeforces.com/contest/25/problem/C)
 - [Codeforces - String Problem](http://codeforces.com/contest/33/problem/B)
 - [GYM - Manic Moving (C)](http://codeforces.com/gym/101223)
 - [SPOJ - Arbitrage](http://www.spoj.com/problems/ARBITRAG/)
 - [UVA - 12179 - Randomly-priced Tickets](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3331)
 - [LOJ - 1086 - Jogging Trails](http://lightoj.com/volume_showproblem.php?problem=1086)
 - [SPOJ - Ingredients](http://www.spoj.com/problems/INGRED/)
 - [CSES - Shortest Routes II](https://cses.fi/problemset/task/1672)
