---
tags:
  - Original
---

# Đường tròn bao nhỏ nhất

Xét bài toán sau:

!!! example "[Library Checker - Minimum Enclosing Circle](https://judge.yosupo.jp/problem/minimum_enclosing_circle)"

    Bạn được cho $n \leq 10^5$ điểm $p_i=(x_i, y_i)$.

    Đối với mỗi $p_i$, hãy tìm xem nó có nằm trên chu vi của đường tròn bao nhỏ nhất của $\{p_1,\dots,p_n\}$ không.

Ở đây, bằng đường tròn bao nhỏ nhất (MEC), chúng tôi muốn nói đến một đường tròn có bán kính nhỏ nhất có thể chứa tất cả $n$ điểm, bên trong đường tròn hoặc trên biên của nó. Bài toán này có một giải pháp ngẫu nhiên đơn giản, thoạt nhìn có vẻ sẽ chạy trong $O(n^3)$, nhưng thực tế hoạt động trong thời gian kỳ vọng $O(n)$.

Để hiểu rõ hơn về lý luận dưới đây, chúng ta nên lưu ý ngay rằng nghiệm của bài toán là duy nhất:

??? question "Tại sao MEC là duy nhất?"

    Hãy xem xét thiết lập sau: Đặt $r$ là bán kính của MEC. Chúng ta vẽ một đường tròn bán kính $r$ quanh mỗi điểm $p_1,\dots,p_n$. Về mặt hình học, tâm của các đường tròn có bán kính $r$ và bao phủ tất cả các điểm $p_1,\dots,p_n$ tạo thành giao của tất cả $n$ đường tròn.

    Bây giờ, nếu giao chỉ là một điểm duy nhất, điều này đã chứng tỏ rằng nó là duy nhất. Nếu không, giao là một hình có diện tích khác không, vì vậy chúng ta có thể giảm $r$ một chút, và vẫn có giao không rỗng, điều này mâu thuẫn với giả định rằng $r$ là bán kính nhỏ nhất có thể của đường tròn bao.

    Với một logic tương tự, chúng ta cũng có thể chỉ ra tính duy nhất của MEC nếu chúng ta yêu cầu thêm rằng nó đi qua một điểm cụ thể đã cho $p_i$ hoặc hai điểm $p_i$ và $p_j$ (nó cũng là duy nhất vì bán kính của nó xác định nó một cách duy nhất).

    Ngoài ra, chúng ta cũng có thể giả định rằng có hai MEC, và sau đó nhận thấy rằng giao của chúng (đã chứa các điểm $p_1,\dots,p_n$) phải có đường kính nhỏ hơn các đường tròn ban đầu, và do đó có thể được bao phủ bằng một đường tròn nhỏ hơn.

## Thuật toán của Welzl

Để ngắn gọn, hãy ký hiệu $\operatorname{mec}(p_1,\dots,p_n)$ là MEC của $\{p_1,\dots,p_n\}$, và đặt $P_i = \{p_1,\dots,p_i\}$.

Thuật toán, ban đầu được [đề xuất](https://doi.org/10.1007/BFb0038202) bởi Welzl vào năm 1991, diễn ra như sau:

1. Áp dụng một hoán vị ngẫu nhiên cho dãy điểm đầu vào.
2. Duy trì ứng cử viên hiện tại là MEC $C$, bắt đầu với $C = \operatorname{mec}(p_1, p_2)$.
3. Lặp qua $i=3..n$ và kiểm tra xem $p_i \in C$.
    1. Nếu $p_i \in C$ điều đó có nghĩa là $C$ là MEC của $P_i$.
    2. Nếu không, gán $C = \operatorname{mec}(p_i, p_1)$ và lặp qua $j=2..i$ và kiểm tra xem $p_j \in C$.
        1. Nếu $p_j \in C$, thì $C$ là MEC của $P_j$ trong số các đường tròn đi qua $p_i$.
        2. Nếu không, gán $C=\operatorname{mec}(p_i, p_j)$ và lặp qua $k=1..j$ và kiểm tra xem $p_k \in C$.
            1. Nếu $p_k \in C$, thì $C$ là MEC của $P_k$ trong số các đường tròn đi qua $p_i$ và $p_j$.
            2. Nếu không, $C=\operatorname{mec}(p_i,p_j,p_k)$ là MEC của $P_k$ trong số các đường tròn đi qua $p_i$ và $p_j$.

Chúng ta có thể thấy rằng mỗi cấp độ lồng nhau ở đây có một bất biến để duy trì (rằng $C$ là MEC trong số các đường tròn cũng đi qua $0$, $1$ hoặc $2$ điểm đã cho bổ sung), và bất cứ khi nào vòng lặp bên trong đóng lại, bất biến của nó trở nên tương đương với bất biến của lần lặp hiện tại của vòng lặp cha của nó. Điều này, đến lượt nó, đảm bảo tính _đúng đắn_ của toàn bộ thuật toán.

Bỏ qua một số chi tiết kỹ thuật, bây giờ, toàn bộ thuật toán có thể được triển khai trong C++ như sau:

```cpp
struct point {...};

// Được biểu diễn bằng 2 hoặc 3 điểm trên chu vi của nó
struct mec {...};

bool inside(mec const& C, point p) {
    return ...;
}

// Chọn một trình tạo ngẫu nhiên tốt cho việc xáo trộn
mt19937_64 gen(...);
mec enclosing_circle(vector<point> &p) {
    int n = p.size();
    ranges::shuffle(p, gen);
    auto C = mec{p[0], p[1]};
    for(int i = 0; i < n; i++) {
        if(!inside(C, p[i])) {
            C = mec{p[i], p[0]};
            for(int j = 0; j < i; j++) {
                if(!inside(C, p[j])) {
                    C = mec{p[i], p[j]};
                    for(int k = 0; k < j; k++) {
                        if(!inside(C, p[k])) {
                            C = mec{p[i], p[j], p[k]};
                        }
                    }
                }
            }
        }
    }
    return C;
}
```

Bây giờ, có thể mong đợi rằng việc kiểm tra xem một điểm $p_i$ có nằm trong MEC của $2$ hoặc $3$ điểm hay không có thể được thực hiện trong $O(1)$ (chúng ta sẽ thảo luận điều này sau). Nhưng ngay cả khi đó, thuật toán trên có vẻ như sẽ mất $O(n^3)$ trong trường hợp xấu nhất chỉ vì tất cả các vòng lặp lồng nhau. Vậy, tại sao chúng ta lại tuyên bố thời gian chạy kỳ vọng là tuyến tính? Hãy tìm hiểu!

### Phân tích độ phức tạp

Đối với vòng lặp trong cùng nhất (trên $k$), rõ ràng thời gian chạy kỳ vọng của nó là $O(j)$ phép toán. Còn vòng lặp trên $j$ thì sao?

Nó chỉ kích hoạt vòng lặp tiếp theo nếu $p_j$ nằm trên biên của MEC của $P_j$ cũng đi qua điểm $i$, _và việc loại bỏ $p_j$ sẽ làm cho đường tròn co lại hơn nữa_. Trong tất cả các điểm trong $P_j$, chỉ có thể có nhiều nhất $2$ điểm có thuộc tính như vậy, bởi vì nếu có nhiều hơn $2$ điểm từ $P_j$ trên biên, điều đó có nghĩa là sau khi loại bỏ bất kỳ điểm nào trong số chúng, vẫn sẽ có ít nhất $3$ điểm trên biên, đủ để xác định duy nhất đường tròn.

Nói cách khác, sau khi xáo trộn ngẫu nhiên ban đầu, có xác suất nhiều nhất là $\frac{2}{j}$ để chúng ta nhận được một trong số nhiều nhất hai điểm không may mắn là $p_j$. Tổng hợp lại trên tất cả các $j$ từ $1$ đến $i$, chúng ta có thời gian chạy kỳ vọng là

$$
\sum\limits_{j=1}^i \frac{2}{j} \cdot O(j) = O(i).
$$

Theo cách tương tự, bây giờ chúng ta cũng có thể chứng minh rằng vòng lặp ngoài cùng có thời gian chạy kỳ vọng là $O(n)$.

### Kiểm tra một điểm có nằm trong MEC của 2 hoặc 3 điểm không

Bây giờ hãy tìm hiểu chi tiết triển khai của `point` và `mec`. Trong bài toán này, hóa ra việc sử dụng [std::complex](https://codeforces.com/blog/entry/22175) làm một lớp cho các điểm đặc biệt hữu ích:

```cpp
using ftype = int64_t;
using point = complex<ftype>;
```

Để nhắc lại, một số phức là một số có dạng $x+yi$, trong đó $i^2=-1$ và $x, y \in \mathbb R$. Trong C++, một số phức như vậy được biểu diễn bằng một điểm 2 chiều $(x, y)$. Các số phức đã triển khai các phép toán tuyến tính theo thành phần cơ bản (cộng, nhân với một số thực), nhưng phép nhân và phép chia của chúng cũng mang một ý nghĩa hình học nhất định.

Không đi vào quá nhiều chi tiết, chúng ta sẽ lưu ý đến thuộc tính quan trọng nhất cho nhiệm vụ cụ thể này: Nhân hai số phức cộng các góc cực của chúng (được đếm từ $Ox$ ngược chiều kim đồng hồ), và lấy liên hợp (tức là thay đổi $z=x+yi$ thành $\overline{z} = x-yi$) nhân góc cực với $-1$. Điều này cho phép chúng ta xây dựng một số tiêu chí rất đơn giản để biết một điểm $z$ có nằm trong MEC của $2$ hoặc $3$ điểm cụ thể hay không.

#### MEC của 2 điểm

Đối với $2$ điểm $a$ và $b$, MEC của chúng chỉ đơn giản là đường tròn có tâm tại $\frac{a+b}{2}$ với bán kính $\frac{|a-b|}{2}$, nói cách khác là đường tròn có $ab$ làm đường kính. Để kiểm tra xem $z$ có nằm trong đường tròn này hay không, chúng ta chỉ cần kiểm tra xem góc giữa $za$ và $zb$ có phải là góc nhọn hay không.

<center>
<img src="https://upload.wikimedia.org/wikipedia/commons/8/8e/Diameter_angles.svg">
<br>
<i>Các góc bên trong là góc tù, các góc bên ngoài là góc nhọn và các góc trên chu vi là góc vuông</i>
</center>

Tương đương, chúng ta cần kiểm tra xem

$$
I_0=(b-z)\overline{(a-z)}
$$

không có tọa độ thực dương (tương ứng với các điểm có góc cực từ $-90^\circ$ đến $90^\circ$).

#### MEC của 3 điểm

Thêm $z$ vào tam giác $abc$ sẽ tạo thành một tứ giác. Xét biểu thức sau:

$$
\angle azb + \angle bca
$$

Trong một [tứ giác nội tiếp](https://en.wikipedia.org/wiki/Cyclic_quadrilateral), nếu $c$ và $z$ ở cùng một phía của $ab$, thì các góc bằng nhau, và sẽ cộng lại thành $0^\circ$ khi cộng có dấu (tức là dương nếu ngược chiều kim đồng hồ và âm nếu theo chiều kim đồng hồ). Tương ứng, nếu $c$ và $z$ ở hai phía đối diện, các góc sẽ cộng lại thành $180^\circ$.

<center>
<img src="https://upload.wikimedia.org/wikipedia/commons/3/30/Opposing_inscribed_angles.svg">
<br>
<i>Các góc nội tiếp kề nhau bằng nhau, các góc đối diện bù nhau đến 180 độ</i>
</center>

Về mặt số phức, chúng ta có thể lưu ý rằng $\angle azb$ là góc cực của $(b-z)\overline{(a-z)}$ và $\angle bca$ là góc cực của $(a-c)\overline{(b-c)}$. Do đó, chúng ta có thể kết luận rằng $\angle azb + \angle bca$ là góc cực của

$$
I_1 = (b-z) \overline{(a-z)} (a-c) \overline{(b-c)}
$$

Nếu góc là $0^\circ$ hoặc $180^\circ$, điều đó có nghĩa là phần ảo của $I_1$ là $0$, nếu không, chúng ta có thể suy ra liệu $z$ ở bên trong hay bên ngoài đường tròn ngoại tiếp của $abc$ bằng cách kiểm tra dấu của phần ảo của $I_1$. Phần ảo dương tương ứng với các góc dương, và phần ảo âm tương ứng với các góc âm.

Nhưng cái nào trong số chúng có nghĩa là $z$ ở bên trong hay bên ngoài đường tròn? Như chúng ta đã nhận thấy, việc có $z$ bên trong đường tròn thường làm tăng độ lớn của $\angle azb$, trong khi việc có nó bên ngoài đường tròn làm giảm nó. Như vậy, chúng ta có 4 trường hợp sau:

1. $\angle bca > 0^\circ$, $c$ ở cùng phía của $ab$ với $z$. Khi đó, $\angle azb < 0^\circ$, và $\angle azb + \angle bca < 0^\circ$ đối với các điểm bên trong đường tròn.
3. $\angle bca < 0^\circ$, $c$ ở cùng phía của $ab$ với $z$. Khi đó, $\angle azb > 0^\circ$, và $\angle azb + \angle bca > 0^\circ$ đối với các điểm bên trong đường tròn.
2. $\angle bca > 0^\circ$, $c$ ở phía đối diện của $ab$ so với $z$. Khi đó, $\angle azb > 0^\circ$ và $\angle azb + \angle bca > 180^\circ$ đối với các điểm bên trong đường tròn.
4. $\angle bca < 0^\circ$, $c$ ở phía đối diện của $ab$ so với $z$. Khi đó, $\angle azb < 0^\circ$ và $\angle azb + \angle bca < 180^\circ$ đối với các điểm bên trong đường tròn.

Nói cách khác, nếu $\angle bca$ là dương, các điểm bên trong đường tròn sẽ có $\angle azb + \angle bca < 0^\circ$, nếu không, chúng sẽ có $\angle azb + \angle bca > 0^\circ$, giả sử rằng chúng ta chuẩn hóa các góc trong khoảng từ $-180^\circ$ đến $180^\circ$. Điều này, đến lượt nó, có thể được kiểm tra bằng dấu của các phần ảo của $I_2=(a-c)\overline{(b-c)}$ và $I_1 = I_0 I_2$.

**Lưu ý**: Khi chúng ta nhân bốn số phức để có được $I_1$, các hệ số trung gian có thể lớn tới $O(A^4)$, trong đó $A$ là độ lớn tọa độ lớn nhất trong đầu vào. Về mặt tích cực, nếu đầu vào là số nguyên, cả hai kiểm tra trên đều có thể được thực hiện hoàn toàn bằng số nguyên.

#### Cài đặt

Bây giờ, để thực sự triển khai việc kiểm tra, trước tiên chúng ta nên quyết định cách biểu diễn MEC. Vì các tiêu chí của chúng ta hoạt động trực tiếp với các điểm, một cách tự nhiên và hiệu quả để làm điều này là nói rằng MEC được biểu diễn trực tiếp dưới dạng một cặp hoặc một bộ ba điểm xác định nó:

```cpp
using mec = variant<
    array<point, 2>,
    array<point, 3>
>;
```

Bây giờ, chúng ta có thể sử dụng `std::visit` để xử lý hiệu quả cả hai trường hợp theo các tiêu chí trên:

```cpp
/* I < 0 nếu z bên trong C,
   I > 0 nếu z bên ngoài C,
   I = 0 nếu z trên chu vi của C */
ftype indicator(mec const& C, point z) {
    return visit([&](auto &&C) {
        point a = C[0], b = C[1];
        point I0 = (b - z) * conj(a - z);
        if constexpr (size(C) == 2) {
            return real(I0);
        } else {
            point c = C[2];
            point I2 = (a - c) * conj(b - c);
            point I1 = I0 * I2;
            return imag(I2) < 0 ? -imag(I1) : imag(I1);
        }
    }, C);
}

bool inside(mec const& C, point p) {
    return indicator(C, p) <= 0;
}

```

Bây giờ, cuối cùng chúng ta có thể đảm bảo rằng mọi thứ hoạt động bằng cách nộp bài toán cho Library Checker: [#308668](https://judge.yosupo.jp/submission/308668).

## Các bài toán thực hành

- [Library Checker - Minimum Enclosing Circle](https://judge.yosupo.jp/problem/minimum_enclosing_circle)
- [BOI 2002 - Aliens](https://www.spoj.com/problems/ALIENS)