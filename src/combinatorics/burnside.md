---
tags:
  - Translated
e_maxx_link: burnside_polya
---

# Bổ đề Burnside / Định lý liệt kê Pólya

## Bổ đề Burnside

**Bổ đề Burnside** được **Burnside** phát biểu và chứng minh vào năm 1897, nhưng trong lịch sử, nó đã được **Frobenius** phát hiện vào năm 1887, và thậm chí sớm hơn vào năm 1845 bởi **Cauchy**.
Do đó, đôi khi nó còn được gọi là **bổ đề Cauchy-Frobenius**.

Bổ đề Burnside cho phép chúng ta đếm số lớp tương đương trong các tập hợp, dựa trên đối xứng bên trong.

### Đối tượng và biểu diễn

Chúng ta phải phân biệt rõ ràng giữa số lượng đối tượng và số lượng biểu diễn.

Các biểu diễn khác nhau có thể tương ứng với cùng một đối tượng, nhưng tất nhiên bất kỳ biểu diễn nào cũng tương ứng với chính xác một đối tượng.
Do đó, tập hợp tất cả các biểu diễn được chia thành các lớp tương đương.
Nhiệm vụ của chúng ta là tính toán số lượng đối tượng, hoặc tương đương, số lượng các lớp tương đương.
Ví dụ sau sẽ làm rõ sự khác biệt giữa đối tượng và biểu diễn.

### Ví dụ: tô màu cây nhị phân

Giả sử chúng ta có bài toán sau.
Chúng ta phải đếm số cách tô màu một cây nhị phân có gốc với $n$ đỉnh bằng hai màu, trong đó tại mỗi đỉnh chúng ta không phân biệt giữa con trái và con gái phải.

Ở đây, tập hợp các đối tượng là tập hợp các cách tô màu khác nhau của cây.

Bây giờ chúng ta định nghĩa tập hợp các biểu diễn.
Một biểu diễn của một cách tô màu là một hàm $f(v)$, gán cho mỗi đỉnh một màu (ở đây chúng ta sử dụng các màu $0$ và $1$).
Tập hợp các biểu diễn là tập hợp chứa tất cả các hàm có thể có của loại này, và kích thước của nó rõ ràng là bằng $2^n$.

Đồng thời, chúng ta giới thiệu một phân hoạch của tập hợp này thành các lớp tương đương.

Ví dụ, giả sử $n = 3$, và cây bao gồm gốc $1$ và hai con của nó là $2$ và $3$.
Khi đó, các hàm $f_1$ và $f_2$ sau đây được coi là tương đương.

$$\begin{array}{ll}
 f_1(1) = 0 & f_2(1) = 0\\
f_1(2) = 1 & f_2(2) = 0\\
f_1(3) = 0 & f_2(3) = 1
\end{array}$$

### Hoán vị bất biến

Tại sao hai hàm $f_1$ và $f_2$ này thuộc cùng một lớp tương đương?
Về mặt trực giác, điều này có thể hiểu được - chúng ta có thể sắp xếp lại các con của đỉnh $1$, các đỉnh $2$ và $3$, và sau một phép biến đổi như vậy của hàm $f_1$, nó sẽ trùng với $f_2$.

Nhưng về mặt hình thức, điều này có nghĩa là tồn tại một **hoán vị bất biến** $\pi$ (tức là một hoán vị không làm thay đổi chính đối tượng, mà chỉ là biểu diễn của nó), sao cho:

$$f_2 \pi \equiv f_1$$

Vì vậy, bắt đầu từ định nghĩa của các đối tượng, chúng ta có thể tìm tất cả các hoán vị bất biến, tức là tất cả các hoán vị không làm thay đổi đối tượng khi áp dụng hoán vị cho biểu diễn.
Sau đó, chúng ta có thể kiểm tra xem hai hàm $f_1$ và $f_2$ có tương đương không (tức là nếu chúng tương ứng với cùng một đối tượng) bằng cách kiểm tra điều kiện $f_2 \pi \equiv f_1$ cho mỗi hoán vị bất biến (hoặc tương đương $f_1 \pi \equiv f_2$).
Nếu tìm thấy ít nhất một hoán vị mà điều kiện được thỏa mãn, thì $f_1$ và $f_2$ là tương đương, nếu không thì chúng không tương đương.

Việc tìm tất cả các hoán vị bất biến như vậy đối với định nghĩa đối tượng là một bước quan trọng để áp dụng cả bổ đề Burnside và định lý liệt kê Pólya.
Rõ ràng là các hoán vị bất biến này phụ thuộc vào bài toán cụ thể, và việc tìm kiếm chúng là một quá trình heuristic thuần túy dựa trên các cân nhắc trực quan.
Tuy nhiên, trong hầu hết các trường hợp, chỉ cần tìm thủ công một số hoán vị "cơ bản", mà từ đó tất cả các hoán vị khác có thể được tạo ra (và phần công việc này có thể được chuyển cho máy tính).

Không khó để hiểu rằng các hoán vị bất biến tạo thành một **nhóm**, vì tích (phép hợp) của các hoán vị bất biến lại là một hoán vị bất biến.
Chúng ta ký hiệu **nhóm các hoán vị bất biến** là $G$.

### Phát biểu của bổ đề

Để phát biểu bổ đề, chúng ta cần một định nghĩa nữa từ đại số.
Một **điểm bất động** $f$ đối với một hoán vị $\pi$ là một phần tử không đổi dưới hoán vị này: $f \equiv f \pi$.
Ví dụ, trong ví dụ của chúng ta, các điểm bất động là các hàm $f$, tương ứng với các cách tô màu không thay đổi khi áp dụng hoán vị $\pi$ cho chúng (tức là chúng không thay đổi theo nghĩa hình thức của sự bằng nhau của các hàm).
Chúng ta ký hiệu $I(\pi)$ là **số lượng các điểm bất động** cho hoán vị $\pi$.

Khi đó, **bổ đề Burnside** được phát biểu như sau:
số lượng các lớp tương đương bằng tổng số lượng các điểm bất động đối với tất cả các hoán vị từ nhóm $G$, chia cho kích thước của nhóm này:

$$|\text{Các lớp}| = \frac{1}{|G|} \sum_{\pi \in G} I(\pi)$$

Mặc dù bản thân bổ đề Burnside không tiện lợi để sử dụng trong thực tế (không rõ làm thế nào để nhanh chóng tìm ra giá trị $I(\pi)$), nó thể hiện rõ nhất bản chất toán học mà ý tưởng tính toán các lớp tương đương dựa trên đó.

### Chứng minh bổ đề Burnside

Chứng minh bổ đề Burnside được mô tả ở đây không quan trọng đối với các ứng dụng thực tế, vì vậy có thể bỏ qua trong lần đọc đầu tiên.

Chứng minh ở đây là chứng minh đơn giản nhất được biết đến, và không sử dụng lý thuyết nhóm.
Chứng minh được Kenneth P. Bogart công bố vào năm 1991.

Chúng ta cần chứng minh mệnh đề sau:

$$|\text{Các lớp}| \cdot |G| = \sum_{\pi \in G} I(\pi)$$

Giá trị ở vế phải không gì khác hơn là số lượng các "cặp bất biến" $(f, \pi)$, tức là các cặp sao cho $f \pi \equiv f$.
Rõ ràng là chúng ta có thể thay đổi thứ tự của phép tổng.
Chúng ta để tổng lặp qua tất cả các phần tử $f$ và tổng trên các giá trị $J(f)$ - số lượng các hoán vị mà $f$ là một điểm bất động.

$$|\text{Các lớp}| \cdot |G| = \sum_{f} J(f)$$

Để chứng minh công thức này, chúng ta sẽ lập một bảng với các cột được gán nhãn bằng tất cả các hàm $f_i$ và các hàng được gán nhãn bằng tất cả các hoán vị $\pi_j$.
Và chúng ta điền vào các ô bằng $f_i \pi_j$.
Nếu chúng ta xem xét các cột trong bảng này như các tập hợp, thì một số trong chúng sẽ trùng nhau, và điều này có nghĩa là các hàm $f$ tương ứng cho các cột này cũng tương đương.
Do đó, số lượng các cột khác nhau (như các tập hợp) bằng số lượng các lớp.
Tình cờ, từ quan điểm của lý thuyết nhóm, cột được gán nhãn $f_i$ là quỹ đạo của phần tử này.
Đối với các phần tử tương đương, các quỹ đạo trùng nhau, và số lượng các quỹ đạo chính xác cho ra số lượng các lớp.

Do đó, các cột của bảng phân rã thành các lớp tương đương.
Hãy cố định một lớp, và xem xét các cột trong đó.
Đầu tiên, lưu ý rằng các cột này chỉ có thể chứa các phần tử $f_i$ của lớp tương đương (nếu không, một hoán vị $\pi_j$ nào đó đã di chuyển một trong các hàm vào một lớp tương đương khác, điều này là không thể vì chúng ta chỉ xem xét các hoán vị bất biến).
Thứ hai, mỗi phần tử $f_i$ sẽ xuất hiện cùng một số lần trong mỗi cột (điều này cũng xuất phát từ thực tế là các cột tương ứng với các phần tử tương đương).
Từ đó, chúng ta có thể kết luận rằng tất cả các cột trong cùng một lớp tương đương đều trùng nhau như các đa tập.

Bây giờ hãy cố định một phần tử tùy ý $f$.
Một mặt, nó xuất hiện trong cột của nó chính xác $J(f)$ lần (theo định nghĩa).
Mặt khác, tất cả các cột trong cùng một lớp tương đương đều giống nhau như các đa tập.
Do đó, trong mỗi cột của một lớp tương đương đã cho, bất kỳ phần tử $g$ nào cũng xuất hiện chính xác $J(g)$ lần.

Do đó, nếu chúng ta lấy một cột tùy ý từ mỗi lớp tương đương, và cộng số lượng các phần tử trong chúng, chúng ta có được một mặt là $|\text{Các lớp}| \cdot |G|$ (chỉ bằng cách nhân số cột với số hàng), và mặt khác là tổng của các đại lượng $J(f)$ cho tất cả các $f$ (điều này xuất phát từ tất cả các lập luận trước đó):

$$|\text{Các lớp}| \cdot |G| = \sum_{f} J(f)$$

## Định lý liệt kê Pólya

Định lý liệt kê Pólya là một sự tổng quát hóa của bổ đề Burnside, và nó cũng cung cấp một công cụ tiện lợi hơn để tìm số lượng các lớp tương đương.
Cần lưu ý rằng định lý này đã được Redfield phát hiện trước Pólya vào năm 1927, nhưng công bố của ông đã không được các nhà toán học chú ý.
Pólya độc lập đi đến những kết quả tương tự vào năm 1937, và công bố của ông đã thành công hơn.

Ở đây chúng ta chỉ thảo luận về một trường hợp đặc biệt của định lý liệt kê Pólya, điều này sẽ rất hữu ích trong thực tế.
Công thức tổng quát của định lý sẽ không được thảo luận.

Chúng ta ký hiệu $C(\pi)$ là số chu trình trong hoán vị $\pi$.
Khi đó công thức sau (một **trường hợp đặc biệt của định lý liệt kê Pólya**) đúng:

$$|\text{Các lớp}| = \frac{1}{|G|} \sum_{\pi \in G} k^{C(\pi)}$$

$k$ là số lượng các giá trị mà mỗi phần tử biểu diễn có thể nhận, trong trường hợp tô màu một cây nhị phân, đây sẽ là $k = 2$.

### Bằng chứng

Công thức này là một hệ quả trực tiếp của bổ đề Burnside.
Để có được nó, chúng ta chỉ cần tìm một biểu thức tường minh cho $I(\pi)$, xuất hiện trong bổ đề.
Nhớ lại rằng $I(\pi)$ là số lượng các điểm bất động trong hoán vị $\pi$.

Do đó, chúng ta xét một hoán vị $\pi$ và một phần tử $f$ nào đó.
Trong quá trình áp dụng $\pi$, các phần tử trong $f$ di chuyển thông qua các chu trình trong hoán vị.
Vì kết quả phải thu được $f \equiv f \pi$, các phần tử bị ảnh hưởng bởi một chu trình phải đều bằng nhau.
Đồng thời các chu trình khác nhau là độc lập.
Do đó, đối với mỗi chu trình hoán vị $\pi$, chúng ta có thể chọn một giá trị (trong số $k$ giá trị có thể) và do đó chúng ta có được số lượng các điểm bất động:

$$I(\pi) = k^{C(\pi)}$$

## Ứng dụng: Tô màu vòng cổ

Bài toán "Vòng cổ" là một trong những bài toán tổ hợp cổ điển.
Nhiệm vụ là đếm số lượng các vòng cổ khác nhau từ $n$ hạt, mỗi hạt có thể được sơn bằng một trong $k$ màu.
Khi so sánh hai vòng cổ, chúng có thể được xoay, nhưng không thể lật (tức là cho phép dịch chuyển vòng tròn).

Trong bài toán này, chúng ta có thể ngay lập tức tìm thấy nhóm các hoán vị bất biến:

$$\begin{align}
 \pi_0 &= 1 2 3 \dots n\\
 \pi_1 &= 2 3 \dots n 1\\
 \pi_2 &= 3 \dots n 12\\
 &\dots\\
 \pi_{n-1} &= n 1 2 3\dots
\end{align}$$

Hãy tìm một công thức tường minh để tính $C(\pi_i)$.
Đầu tiên, chúng ta lưu ý rằng hoán vị $\pi_i$ ở vị trí thứ $j$ có giá trị $i + j$ (lấy modulo $n$).
Nếu chúng ta kiểm tra cấu trúc chu trình cho $\pi_i$.
Chúng ta thấy rằng $1$ đi đến $1 + i$, $1 + i$ đi đến $1 + 2i$, đi đến $1 + 3i$, v.v., cho đến khi chúng ta đến một số có dạng $1 + k n$.
Các mệnh đề tương tự có thể được đưa ra cho các phần tử còn lại.
Do đó, chúng ta thấy rằng tất cả các chu trình đều có cùng độ dài, cụ thể là $\frac{\text{lcm}(i, n)}{i} = \frac{n}{\gcd(i, n)}$.
Do đó, số chu trình trong $\pi_i$ sẽ bằng $\gcd(i, n)$.

Thay thế các giá trị này vào định lý liệt kê Pólya, chúng ta có được nghiệm:

$$\frac{1}{n} \sum_{i=1}^n k^{\gcd(i, n)}$$

Bạn có thể để công thức này ở dạng này, hoặc bạn có thể đơn giản hóa nó hơn nữa.
Hãy chuyển tổng để nó lặp qua tất cả các ước của $n$.
Trong tổng ban đầu sẽ có nhiều số hạng tương đương: nếu $i$ không phải là ước của $n$, thì một ước như vậy có thể được tìm thấy sau khi tính $\gcd(i, n)$.
Do đó, đối với mỗi ước $d ~|~ n$, số hạng $k^{\gcd(d, n)} = k^d$ của nó sẽ xuất hiện trong tổng nhiều lần, tức là câu trả lời cho bài toán có thể được viết lại là

$$\frac{1}{n} \sum_{d ~|~ n} C_d k^d,$$

trong đó $C_d$ là số lượng các số $i$ như vậy với $\gcd(i, n) = d$.
Chúng ta có thể tìm một biểu thức tường minh cho giá trị này.
Bất kỳ số $i$ nào như vậy đều có dạng $i = d j$ với $\gcd(j, n / d) = 1$ (nếu không thì $\gcd(i, n) > d$).
Vì vậy, chúng ta có thể đếm số lượng $j$ có hành vi này.
[Hàm phi Euler](../algebra/phi-function.md) cho chúng ta kết quả $C_d = \phi(n / d)$, và do đó chúng ta có được câu trả lời:

$$\frac{1}{n} \sum_{d ~|~ n} \phi\left(\frac{n}{d}\right) k^d$$

## Ứng dụng: Tô màu hình xuyến

Khá thường xuyên chúng ta không thể có được một công thức tường minh cho số lượng các lớp tương đương.
Trong nhiều bài toán, số lượng các hoán vị trong một nhóm có thể quá lớn để tính toán thủ công và không thể tính toán phân tích số chu trình trong chúng.

Trong trường hợp đó, chúng ta nên tìm thủ công một số hoán vị "cơ bản", để chúng có thể tạo ra toàn bộ nhóm $G$.
Tiếp theo, chúng ta có thể viết một chương trình sẽ tạo ra tất cả các hoán vị của nhóm $G$, đếm số chu trình trong chúng và tính toán câu trả lời bằng công thức.

Xét ví dụ về bài toán tô màu một hình xuyến.
Có một tờ giấy kẻ ô $n \times m$ ($n < m$), một số ô màu đen.
Sau đó, một hình trụ được tạo ra từ tờ giấy này bằng cách dán hai cạnh có độ dài $m$.
Sau đó, một hình xuyến được tạo ra từ hình trụ bằng cách dán hai vòng tròn (trên và dưới) mà không xoắn.
Nhiệm vụ là tính toán số lượng các hình xuyến được tô màu khác nhau, giả sử rằng chúng ta không thể nhìn thấy các đường dán, và hình xuyến có thể được xoay và lật.

Chúng ta lại bắt đầu với một tờ giấy $n \times m$.
Dễ dàng thấy rằng các loại biến đổi sau đây bảo toàn lớp tương đương:
một dịch chuyển vòng của các hàng, một dịch chuyển vòng của các cột, và một phép quay của tờ giấy 180 độ.
Cũng dễ dàng thấy rằng các biến đổi này có thể tạo ra toàn bộ nhóm các biến đổi bất biến.
Nếu chúng ta đánh số các ô của tờ giấy bằng cách nào đó, thì chúng ta có thể viết ba hoán vị $p_1$, $p_2$, $p_3$ tương ứng với các loại biến đổi này.

Tiếp theo chỉ còn lại việc tạo ra tất cả các hoán vị thu được dưới dạng một tích.
Rõ ràng là tất cả các hoán vị như vậy đều có dạng $p_1^{i_1} p_2^{i_2} p_3^{i_3}$ trong đó $i_1 = 0 \dots m-1$, $i_2 = 0 \dots n-1$, $i_3 = 0 \dots 1$.

Do đó, chúng ta có thể viết các triển khai cho bài toán này.

```{.cpp file=burnside_tori}
using Permutation = vector<int>;

void operator*=(Permutation& p, Permutation const& q) {
    Permutation copy = p;
    for (int i = 0; i < p.size(); i++)
        p[i] = copy[q[i]];
}

int count_cycles(Permutation p) {
    int cnt = 0;
    for (int i = 0; i < p.size(); i++) {
        if (p[i] != -1) {
            cnt++;
            for (int j = i; p[j] != -1;) {
                int next = p[j];
                p[j] = -1;
                j = next;
            }
        }
    }
    return cnt;
}

int solve(int n, int m) {
    Permutation p(n*m), p1(n*m), p2(n*m), p3(n*m);
    for (int i = 0; i < n*m; i++) {
        p[i] = i;
        p1[i] = (i % n + 1) % n + i / n * n;
        p2[i] = (i / n + 1) % m * n + i % n;
        p3[i] = (m - 1 - i / n) * n + (n - 1 - i % n);
    }

    set<Permutation> s;
    for (int i1 = 0; i1 < n; i1++) {
        for (int i2 = 0; i2 < m; i2++) {
            for (int i3 = 0; i3 < 2; i3++) {
                s.insert(p);
                p *= p3;
            }
            p *= p2;
        }
        p *= p1;
    }

    int sum = 0;
    for (Permutation const& p : s) {
        sum += 1 << count_cycles(p);
    }
    return sum / s.size();
}
```
## Bài tập luyện tập
* [CSES - Counting Necklaces](https://cses.fi/problemset/task/2209)
* [CSES - Counting Grids](https://cses.fi/problemset/task/2210)
* [Codeforces - Buildings](https://codeforces.com/gym/101873/problem/B)
* [CS Academy - Cube Coloring](https://csacademy.com/contest/beta-round-8/task/cube-coloring/)
* [Codeforces - Side Transmutations](https://codeforces.com/contest/1065/problem/E)
* [LightOJ - Necklace](https://vjudge.net/problem/LightOJ-1419)
* [POJ - Necklace of Beads](http://poj.org/problem?id=1286)
* [CodeChef - Lucy and Flowers](https://www.codechef.com/problems/DECORATE)
* [HackerRank - Count the Necklaces](https://www.hackerrank.com/contests/infinitum12/challenges/count-the-necklaces)
* [POJ - Magic Bracelet](http://poj.org/problem?id=2888)
* [SPOJ - Sorting Machine](https://www.spoj.com/problems/SRTMACH/)
* [Project Euler - Pizza Toppings](https://projecteuler.net/problem=281)
* [ICPC 2011 SERCP - Alphabet Soup](https://basecamp.eolymp.com/tr/problems/3064)
* [GCPC 2017 - Buildings](https://basecamp.eolymp.com/en/problems/11615)

```