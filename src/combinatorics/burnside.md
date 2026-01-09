---
tags:
  - Translated
e_maxx_link: burnside_polya
---

# Bổ đề Burnside / Định lý đếm Pólya (Burnside's lemma / Pólya enumeration theorem) {: #burnsides-lemma-polya-enumeration-theorem}

## Bổ đề Burnside (Burnside's lemma) {: #burnsides-lemma}

**Bổ đề Burnside** được xây dựng và chứng minh bởi **Burnside** vào năm 1897, nhưng về mặt lịch sử nó đã được phát hiện vào năm 1887 bởi **Frobenius**, và thậm chí sớm hơn vào năm 1845 bởi **Cauchy**.
Do đó, nó đôi khi cũng được đặt tên là **bổ đề Cauchy-Frobenius**.

Bổ đề Burnside cho phép chúng ta đếm số lượng các lớp tương đương trong các tập hợp, dựa trên sự đối xứng bên trong.

### Đối tượng và biểu diễn (Objects and representations) {: #objects-and-representations}

Chúng ta phải phân biệt rõ ràng giữa số lượng đối tượng và số lượng biểu diễn.

Các biểu diễn khác nhau có thể tương ứng với cùng một đối tượng, nhưng tất nhiên mọi biểu diễn tương ứng với chính xác một đối tượng.
Do đó, tập hợp các biểu diễn được chia thành các lớp tương đương.
Nhiệm vụ của chúng tôi là tính số lượng đối tượng, hoặc tương đương, số lượng các lớp tương đương.
Ví dụ sau đây sẽ làm cho sự khác biệt giữa đối tượng và biểu diễn rõ ràng hơn.

### Ví dụ: tô màu cây nhị phân (Example: coloring of binary trees) {: #example-coloring-of-binary-trees}

Giả sử chúng ta có bài toán sau.
Chúng ta phải đếm số cách tô màu một cây nhị phân có gốc với $n$ đỉnh bằng hai màu, trong đó tại mỗi đỉnh chúng ta không phân biệt giữa con trái và con phải.

Ở đây tập hợp các đối tượng là tập hợp các cách tô màu khác nhau của cây.

Bây giờ chúng ta xác định tập hợp các biểu diễn.
Một biểu diễn của một cách tô màu là một hàm $f(v)$, gán cho mỗi đỉnh một màu (ở đây chúng ta sử dụng các màu $0$ và $1$).
Tập hợp các biểu diễn là tập hợp chứa tất cả các hàm có thể thuộc loại này, và kích thước của nó rõ ràng bằng $2^n$.

Đồng thời chúng ta giới thiệu một phân hoạch của tập hợp này thành các lớp tương đương.

Ví dụ, giả sử $n = 3$, và cây bao gồm gốc $1$ và hai con của nó $2$ và $3$.
Khi đó các hàm $f_1$ và $f_2$ sau đây được coi là tương đương.

$$\begin{array}{ll}
f_1(1) = 0 & f_2(1) = 0\\
f_1(2) = 1 & f_2(2) = 0\\
f_1(3) = 0 & f_2(3) = 1
\end{array}$$

### Hoán vị bất biến (Invariant permutations) {: #invariant-permutations}

Tại sao hai hàm $f_1$ và $f_2$ này thuộc cùng một lớp tương đương?
Về mặt trực giác, điều này có thể hiểu được - chúng ta có thể sắp xếp lại các con của đỉnh $1$, các đỉnh $2$ và $3$, và sau một phép biến đổi như vậy của hàm $f_1$ nó sẽ trùng với $f_2$.

Nhưng về mặt hình thức, điều này có nghĩa là tồn tại một **hoán vị bất biến** $\pi$ (tức là một hoán vị không thay đổi chính đối tượng, mà chỉ thay đổi biểu diễn của nó), sao cho:

$$f_2 \pi \equiv f_1$$

Vì vậy, bắt đầu từ định nghĩa của các đối tượng, chúng ta có thể tìm thấy tất cả các hoán vị bất biến, tức là tất cả các hoán vị không thay đổi đối tượng khi áp dụng hoán vị cho biểu diễn.
Sau đó, chúng ta có thể kiểm tra xem hai hàm $f_1$ và $f_2$ có tương đương hay không (tức là nếu chúng tương ứng với cùng một đối tượng) bằng cách kiểm tra điều kiện $f_2 \pi \equiv f_1$ cho mỗi hoán vị bất biến (hoặc tương đương $f_1 \pi \equiv f_2$).
Nếu tìm thấy ít nhất một hoán vị mà điều kiện được thỏa mãn, thì $f_1$ và $f_2$ là tương đương, nếu không chúng không tương đương.

Tìm tất cả các hoán vị bất biến như vậy liên quan đến định nghĩa đối tượng là một bước quan trọng cho việc áp dụng cả bổ đề Burnside và định lý đếm Pólya.
Rõ ràng là các hoán vị bất biến này phụ thuộc vào bài toán cụ thể, và việc tìm kiếm chúng là một quá trình heuristic thuần túy dựa trên các cân nhắc trực quan.
Tuy nhiên trong hầu hết các trường hợp, là đủ để tìm thủ công một vài hoán vị "cơ bản", với chúng tất cả các hoán vị khác có thể được tạo ra (và phần công việc này có thể được chuyển sang máy tính).

Không khó để hiểu rằng các hoán vị bất biến tạo thành một **nhóm**, vì tích (hợp thành) của các hoán vị bất biến lại là một hoán vị bất biến.
Chúng tôi ký hiệu **nhóm các hoán vị bất biến** là $G$.

### Phát biểu bổ đề (The statement of the lemma) {: #the-statement-of-the-lemma}

Đối với việc xây dựng bổ đề, chúng ta cần thêm một định nghĩa nữa từ đại số.
Một **điểm bất động** $f$ cho một hoán vị $\pi$ là một phần tử bất biến dưới hoán vị này: $f \equiv f \pi$.
Ví dụ trong ví dụ của chúng ta, các điểm bất động là các hàm $f$, tương ứng với các cách tô màu không thay đổi khi hoán vị $\pi$ được áp dụng cho chúng (tức là chúng không thay đổi theo nghĩa chính thức của sự bằng nhau của các hàm).
Chúng tôi ký hiệu $I(\pi)$ là **số lượng điểm bất động** cho hoán vị $\pi$.

Khi đó **bổ đề Burnside** diễn ra như sau:
số lượng các lớp tương đương bằng tổng số lượng điểm bất động đối với tất cả các hoán vị từ nhóm $G$, chia cho kích thước của nhóm này:

$$|\text{Classes}| = \frac{1}{|G|} \sum_{\pi \in G} I(\pi)$$

Mặc dù bản thân bổ đề Burnside không thuận tiện lắm để sử dụng trong thực tế (không rõ làm thế nào để nhanh chóng tìm kiếm giá trị $I(\pi)$, nó tiết lộ rõ ràng nhất bản chất toán học dựa trên ý tưởng tính toán các lớp tương đương).

### Chứng minh bổ đề Burnside (Proof of Burnside's lemma) {: #proof-of-burnsides-lemma}

Chứng minh bổ đề Burnside mô tả ở đây không quan trọng đối với các ứng dụng thực tế, vì vậy nó có thể được bỏ qua trong lần đọc đầu tiên.

Chứng minh ở đây là đơn giản nhất được biết đến, và không sử dụng lý thuyết nhóm.
Chứng minh được xuất bản bởi Kenneth P. Bogart vào năm 1991.

Chúng ta cần chứng minh tuyên bố sau:

$$|\text{Classes}| \cdot |G| = \sum_{\pi \in G} I(\pi)$$

Giá trị ở phía bên phải không gì khác hơn là số lượng "cặp bất biến" $(f, \pi)$, tức là các cặp sao cho $f \pi \equiv f$.
Rõ ràng là chúng ta có thể thay đổi thứ tự tính tổng.
Chúng ta để tổng lặp qua tất cả các phần tử $f$ và tính tổng qua các giá trị $J(f)$ - số lượng hoán vị mà $f$ là một điểm bất động.

$$|\text{Classes}| \cdot |G| = \sum_{f} J(f)$$

Để chứng minh công thức này, chúng ta sẽ soạn một bảng với các cột được gắn nhãn với tất cả các hàm $f_i$ và các hàng được gắn nhãn với tất cả các hoán vị $\pi_j$.
Và chúng ta điền vào các ô với $f_i \pi_j$.
Nếu chúng ta nhìn vào các cột trong bảng này như các tập hợp, thì một số trong số chúng sẽ trùng nhau, và điều này có nghĩa là các hàm $f$ tương ứng cho các cột này cũng tương đương.
Do đó số lượng các cột khác nhau (như tập hợp) bằng số lượng các lớp.
Tình cờ, từ quan điểm của lý thuyết nhóm, cột được gắn nhãn với $f_i$ là quỹ đạo của phần tử này.
Đối với các phần tử tương đương, các quỹ đạo trùng nhau, và số lượng quỹ đạo cho chính xác số lượng các lớp.

Do đó các cột của bảng phân rã thành các lớp tương đương.
Hãy cố định một lớp, và nhìn vào các cột trong đó.
Thứ nhất, lưu ý rằng các cột này chỉ có thể chứa các phần tử $f_i$ của lớp tương đương (nếu không, một hoán vị $\pi_j$ nào đó đã chuyển một trong các hàm sang một lớp tương đương khác, điều này là không thể vì chúng ta chỉ xem xét các hoán vị bất biến).
Thứ hai, mỗi phần tử $f_i$ sẽ xuất hiện cùng một số lần trong mỗi cột (điều này cũng theo sau từ thực tế là các cột tương ứng với các phần tử tương đương).
Từ đó chúng ta có thể kết luận rằng, tất cả các cột trong cùng một lớp tương đương trùng nhau như đa tập hợp (multisets).

Bây giờ sửa một phần tử tùy ý $f$.
Một mặt, nó xuất hiện trong cột của nó chính xác $J(f)$ lần (theo định nghĩa).
Mặt khác, tất cả các cột trong cùng một lớp tương đương giống nhau như đa tập hợp.
Do đó trong mỗi cột của một lớp tương đương nhất định, bất kỳ phần tử $g$ nào cũng xuất hiện chính xác $J(g)$ lần.

Do đó, nếu chúng ta lấy tùy ý một cột từ mỗi lớp tương đương, và tổng hợp số lượng phần tử trong chúng, chúng ta thu được một mặt $|\text{Classes}| \cdot |G|$ (đơn giản bằng cách nhân số lượng cột với số lượng hàng), và mặt khác tổng của các đại lượng $J(f)$ cho tất cả $f$ (điều này theo sau từ tất cả các lập luận trước đó):

$$|\text{Classes}| \cdot |G| = \sum_{f} J(f)$$

## Định lý đếm Pólya (Pólya enumeration theorem) {: #polya-enumeration-theorem}

Định lý đếm Pólya là một sự tổng quát hóa của bổ đề Burnside, và nó cũng cung cấp một công cụ thuận tiện hơn để tìm số lượng các lớp tương đương.
Cần lưu ý rằng định lý này đã được phát hiện trước Pólya bởi Redfield vào năm 1927, nhưng ấn phẩm của ông không được các nhà toán học chú ý.
Pólya độc lập đi đến cùng kết quả vào năm 1937, và ấn phẩm của ông thành công hơn.

Ở đây chúng tôi chỉ thảo luận về một trường hợp đặc biệt của định lý đếm Pólya, sẽ trở nên rất hữu ích trong thực tế.
Công thức chung của định lý sẽ không được thảo luận.

Chúng tôi ký hiệu $C(\pi)$ là số lượng chu trình trong hoán vị $\pi$.
Khi đó công thức sau (**trường hợp đặc biệt của định lý đếm Pólya**) giữ:

$$|\text{Classes}| = \frac{1}{|G|} \sum_{\pi \in G} k^{C(\pi)}$$

$k$ là số lượng giá trị mà mỗi phần tử biểu diễn có thể nhận, trong trường hợp tô màu cây nhị phân, điều này sẽ là $k = 2$.

### Bằng chứng (Evidence) {: #evidence}

Công thức này là hệ quả trực tiếp của bổ đề Burnside.
Để có được nó, chúng ta chỉ cần tìm một biểu thức rõ ràng cho $I(\pi)$, xuất hiện trong bổ đề.
Hãy nhớ lại, rằng $I(\pi)$ là số lượng điểm bất động trong hoán vị $\pi$.

Do đó, chúng ta xem xét một hoán vị $\pi$ và một số phần tử $f$.
Trong quá trình áp dụng $\pi$, các phần tử trong $f$ di chuyển qua các chu trình trong hoán vị.
Vì kết quả sẽ thu được $f \equiv f \pi$, các phần tử được chạm bởi một chu trình đều phải bằng nhau.
Đồng thời, các chu trình khác nhau là độc lập.
Do đó, đối với mỗi chu trình hoán vị $\pi$, chúng ta có thể chọn một giá trị (trong số $k$ giá trị có thể) và do đó chúng ta nhận được số lượng điểm bất động:

$$I(\pi) = k^{C(\pi)}$$

## Ứng dụng: Tô màu vòng cổ (Application: Coloring necklaces) {: #application-coloring-necklaces}

Bài toán "Vòng cổ" là một trong những bài toán tổ hợp cổ điển.
Nhiệm vụ là đếm số lượng vòng cổ khác nhau từ $n$ hạt, mỗi hạt có thể được sơn bằng một trong $k$ màu.
Khi so sánh hai vòng cổ, chúng có thể được xoay, nhưng không được đảo ngược (tức là cho phép dịch chuyển vòng tròn).

Trong bài toán này, chúng ta có thể tìm ngay nhóm các hoán vị bất biến:

$$\begin{align}
\pi_0 &= 1 2 3 \dots n\\
\pi_1 &= 2 3 \dots n 1\\
\pi_2 &= 3 \dots n 12\\
&\dots\\
\pi_{n-1} &= n 1 2 3\dots\end{align}$$

Hãy tìm một công thức rõ ràng để tính toán $C(\pi_i)$.
Trước tiên chúng ta lưu ý, rằng hoán vị $\pi_i$ có giá trị $i + j$ tại vị trí thứ $j$ (lấy modulo $n$).
Nếu chúng ta kiểm tra cấu trúc chu trình cho $\pi_i$.
Chúng ta thấy rằng $1$ đi đến $1 + i$, $1 + i$ đi đến $1 + 2i$, đi đến $1 + 3i$, v.v., cho đến khi chúng ta đến một số có dạng $1 + k n$.
Các tuyên bố tương tự có thể được thực hiện cho các phần tử còn lại.
Do đó, chúng ta thấy rằng tất cả các chu trình đều có cùng độ dài, cụ thể là $\frac{\text{lcm}(i, n)}{i} = \frac{n}{\gcd(i, n)}$.
Do đó số lượng chu trình trong $\pi_i$ sẽ bằng $\gcd(i, n)$.

Thay các giá trị này vào định lý đếm Pólya, chúng tôi thu được giải pháp:

$$\frac{1}{n} \sum_{i=1}^n k^{\gcd(i, n)}$$

Bạn có thể để công thức này ở dạng này, hoặc bạn có thể đơn giản hóa nó hơn nữa.
Hãy chuyển tổng để nó lặp qua tất cả các ước số của $n$.
Trong tổng ban đầu sẽ có nhiều số hạng tương đương: nếu $i$ không phải là ước số của $n$, thì một ước số như vậy có thể được tìm thấy sau khi tính $\gcd(i, n)$.
Do đó đối với mỗi ước số $d ~|~ n$, số hạng $k^{\gcd(d, n)} = k^d$ của nó sẽ xuất hiện trong tổng nhiều lần, tức là câu trả lời cho bài toán có thể được viết lại thành

$$\frac{1}{n} \sum_{d ~|~ n} C_d k^d,$$

trong đó $C_d$ là số lượng các số $i$ như vậy với $\gcd(i, n) = d$.
Chúng ta có thể tìm thấy một biểu thức rõ ràng cho giá trị này.
Bất kỳ số nào $i$ như vậy đều có dạng $i = d j$ với $\gcd(j, n / d) = 1$ (nếu không $\gcd(i, n) > d$).
Vì vậy chúng ta có thể đếm số lượng $j$ với hành vi này.
[Hàm phi Euler](../algebra/phi-function.md) cho chúng ta kết quả $C_d = \phi(n / d)$, và do đó chúng ta nhận được câu trả lời:

$$\frac{1}{n} \sum_{d ~|~ n} \phi\left(\frac{n}{d}\right) k^d$$

## Ứng dụng: Tô màu hình xuyến (Application: Coloring a torus) {: #application-coloring-a-torus}

Khá thường xuyên chúng ta không thể có được một công thức rõ ràng cho số lượng các lớp tương đương.
Trong nhiều bài toán, số lượng hoán vị trong một nhóm có thể quá lớn để tính toán thủ công và không thể tính toán phân tích số lượng chu trình trong đó.

Trong trường hợp đó, chúng ta nên tìm thủ công một vài hoán vị "cơ bản", để chúng có thể tạo ra toàn bộ nhóm $G$.
Tiếp theo, chúng ta có thể viết một chương trình sẽ tạo ra tất cả các hoán vị của nhóm $G$, đếm số lượng chu trình trong đó, và tính toán câu trả lời bằng công thức.

Xem xét ví dụ về bài toán tô màu hình xuyến.
Có một tờ giấy kẻ ô vuông $n \times m$ ($n < m$), một số ô màu đen.
Sau đó, một hình trụ thu được từ tờ giấy này bằng cách dán hai cạnh có độ dài $m$ lại với nhau.
Sau đó, một hình xuyến thu được từ hình trụ bằng cách dán hai vòng tròn (trên và dưới) lại với nhau mà không xoắn.
Nhiệm vụ là tính số lượng hình xuyến có màu khác nhau, giả sử rằng chúng ta không thể nhìn thấy các đường dán, và hình xuyến có thể được xoay và lật.

Chúng ta lại bắt đầu với một mảnh giấy $n \times m$.
Dễ thấy rằng các loại biến đổi sau đây bảo tồn lớp tương đương:
dịch chuyển vòng các hàng, dịch chuyển vòng các cột, và xoay tờ giấy 180 độ.
Cũng dễ thấy rằng các biến đổi này có thể tạo ra toàn bộ nhóm các biến đổi bất biến.
Nếu chúng ta bằng cách nào đó đánh số các ô của tờ giấy, thì chúng ta có thể viết ba hoán vị $p_1$, $p_2$, $p_3$ tương ứng với các loại biến đổi này.

Tiếp theo chỉ còn lại để tạo ra tất cả các hoán vị thu được như một tích.
Rõ ràng là tất cả các hoán vị như vậy có dạng $p_1^{i_1} p_2^{i_2} p_3^{i_3}$ trong đó $i_1 = 0 \dots m-1$, $i_2 = 0 \dots n-1$, $i_3 = 0 \dots 1$.

Do đó chúng ta có thể viết các cài đặt cho bài toán này.

```cpp
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
## Bài tập luyện tập {: #practice-problems}
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
