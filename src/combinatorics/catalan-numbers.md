---
tags:
  - Translated
e_maxx_link: catalan_numbers
---

# Số Catalan (Catalan Numbers) {: #catalan-numbers}

Số Catalan là một dãy số, được tìm thấy hữu ích trong một số bài toán tổ hợp, thường liên quan đến các đối tượng được định nghĩa đệ quy.

Dãy số này được đặt theo tên của nhà toán học người Bỉ [Catalan](https://en.wikipedia.org/wiki/Eug%C3%A8ne_Charles_Catalan), người sống ở thế kỷ 19. (Trên thực tế, nó đã được biết đến trước đó với Euler, người sống trước Catalan một thế kỷ).

Một số số Catalan đầu tiên $C_n$ (bắt đầu từ số không):

 $1, 1, 2, 5, 14, 42, 132, 429, 1430, \ldots$

### Ứng dụng trong một số bài toán tổ hợp (Application in some combinatorial problems) {: #application-in-some-combinatorial-problems}

Số Catalan $C_n$ là lời giải cho

- Số lượng dãy ngoặc đúng bao gồm $n$ dấu ngoặc mở và $n$ dấu ngoặc đóng.
- Số lượng cây nhị phân đầy đủ có gốc với $n + 1$ lá (các đỉnh không được đánh số). Một cây nhị phân có gốc là đầy đủ nếu mọi đỉnh có hai con hoặc không có con nào.
- Số cách để đặt dấu ngoặc hoàn toàn cho $n + 1$ thừa số.
- Số lượng phân tích của một đa giác lồi có $n + 2$ cạnh thành các tam giác (tức là số lượng phân vùng của đa giác thành các tam giác rời rạc bằng cách sử dụng các đường chéo).
- Số cách để nối $2n$ điểm trên một vòng tròn để tạo thành $n$ dây cung rời rạc.
- Số lượng cây nhị phân đầy đủ [không đẳng cấu](https://en.wikipedia.org/wiki/Graph_isomorphism) với $n$ nút trong (tức là các nút có ít nhất một con trai).
- Số lượng đường đi lưới đơn điệu từ điểm $(0, 0)$ đến điểm $(n, n)$ trong một lưới vuông có kích thước $n \times n$, không đi qua phía trên đường chéo chính (tức là nối $(0, 0)$ với $(n, n)$).
- Số lượng hoán vị có độ dài $n$ có thể được [sắp xếp bằng ngăn xếp](https://en.wikipedia.org/wiki/Stack-sortable_permutation) (tức là có thể chỉ ra rằng sự sắp xếp lại được sắp xếp bằng ngăn xếp khi và chỉ khi không có chỉ số $i < j < k$ sao cho $a_k < a_i < a_j$).
- Số lượng [phân hoạch không chéo](https://en.wikipedia.org/wiki/Noncrossing_partition) của một tập hợp $n$ phần tử.
- Số cách để phủ cái thang $1 \ldots n$ bằng cách sử dụng $n$ hình chữ nhật (Cái thang bao gồm $n$ cột, trong đó cột thứ $i$ có chiều cao $i$).


## Tính toán (Calculations) {: #calculations}

Có hai công thức cho các số Catalan: **Truy hồi và Giải tích**. Vì chúng tôi tin rằng tất cả các bài toán đã đề cập ở trên là tương đương (có cùng một lời giải), để chứng minh các công thức dưới đây, chúng tôi sẽ chọn nhiệm vụ dễ thực hiện nhất.

### Công thức truy hồi (Recursive formula) {: #recursive-formula}
 
$$C_0 = C_1 = 1$$

$$C_n = \sum_{k = 0}^{n-1} C_k C_{n-1-k} , {n} \geq 2$$

Công thức truy hồi có thể dễ dàng suy ra từ bài toán dãy ngoặc đúng.

Dấu ngoặc mở ngoài cùng bên trái $l$ tương ứng với dấu ngoặc đóng nhất định $r$, chia chuỗi thành 2 phần, mỗi phần lần lượt phải là một chuỗi dấu ngoặc đúng. Như vậy công thức cũng được chia thành 2 phần. Nếu chúng ta ký hiệu $k = {r - l - 1}$, thì với $r$ cố định, sẽ có chính xác $C_k C_{n-1-k}$ dãy ngoặc như vậy. Tính tổng này trên tất cả các $k$ chấp nhận được, chúng ta nhận được quan hệ truy hồi trên $C_n$.

Bạn cũng có thể nghĩ theo cách này. Theo định nghĩa, $C_n$ biểu thị số lượng dãy ngoặc đúng. Bây giờ, chuỗi có thể được chia thành 2 phần có độ dài $k$ và ${n - k}$, mỗi phần phải là một dãy ngoặc đúng. Ví dụ :

$( ) ( ( ) )$ có thể được chia thành $( )$ và $( ( ) )$, nhưng không thể chia thành $( ) ($ và $( ) )$. Một lần nữa tính tổng trên tất cả các $k$ chấp nhận được, chúng ta nhận được quan hệ truy hồi trên $C_n$.

#### Cài đặt C++ (C++ implementation) {: #cpp-implementation}

```cpp
const int MOD = ....
const int MAX = ....
int catalan[MAX];
void init() {
    catalan[0] = catalan[1] = 1;
    for (int i=2; i<=n; i++) {
        catalan[i] = 0;
        for (int j=0; j < i; j++) {
            catalan[i] += (catalan[j] * catalan[i-j-1]) % MOD;
            if (catalan[i] >= MOD) {
                catalan[i] -= MOD;
            }
        }
    }
}
```

### Công thức giải tích (Analytical formula) {: #analytical-formula}

$$C_n = \frac{1}{n + 1} {\binom{2n}{n}}$$

(ở đây $\binom{n}{k}$ biểu thị hệ số nhị thức thông thường, tức là số cách để chọn $k$ đối tượng từ tập hợp $n$ đối tượng).

Công thức trên có thể dễ dàng kết luận từ bài toán các đường đi đơn điệu trong lưới vuông. Tổng số đường đi đơn điệu trong lưới kích thước $n \times n$ được cho bởi $\binom{2n}{n}$.

Bây giờ chúng ta đếm số lượng đường đi đơn điệu cắt đường chéo chính. Xem xét các đường đi như vậy cắt đường chéo chính và tìm cạnh đầu tiên trong đó nằm phía trên đường chéo. Phản chiếu đường đi qua đường chéo trên toàn bộ quãng đường, đi sau cạnh này. Kết quả luôn là một đường đi đơn điệu trong lưới $(n - 1) \times (n + 1)$. Mặt khác, mọi đường đi đơn điệu trong lưới $(n - 1) \times (n + 1)$ phải cắt đường chéo. Do đó, chúng ta đã liệt kê tất cả các đường đi đơn điệu cắt đường chéo chính trong lưới $n \times n$.

Số lượng đường đi đơn điệu trong lưới $(n - 1) \times (n + 1)$ là $\binom{2n}{n-1}$. Hãy gọi những con đường như vậy là những con đường "xấu". Kết quả là, để có được số lượng đường đi đơn điệu không cắt đường chéo chính, chúng ta trừ các đường đi "xấu" ở trên, thu được công thức:

$$C_n = \binom{2n}{n} - \binom{2n}{n-1} = \frac{1}{n + 1} \binom{2n}{n} , {n} \geq 0$$

## Tham khảo (Reference) {: #reference}

- [Catalan Number by Tom Davis](http://www.geometer.org/mathcircles/catalan.pdf)

## Bài tập luyện tập {: #practice-problems}
- [Codechef - PANSTACK](https://www.codechef.com/APRIL12/problems/PANSTACK/)
- [Spoj - Skyline](http://www.spoj.com/problems/SKYLINE/)
- [UVA - Safe Salutations](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=932)
- [Codeforces - How many trees?](http://codeforces.com/problemset/problem/9/D)
- [SPOJ - FUNPROB](http://www.spoj.com/problems/FUNPROB/)
* [LOJ - 1170 - Counting Perfect BST](http://lightoj.com/volume_showproblem.php?problem=1170)
* [UVA - 12887 - The Soldier's Dilemma](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=4752)

---

## Checklist

- Original lines: 96
- Translated lines: 96
- Code blocks changed? No
- Inline code changed? No
- Technical terms kept in English? Yes
- Headings anchors preserved/added correctly? Yes
- I confirm no character was omitted: YES
