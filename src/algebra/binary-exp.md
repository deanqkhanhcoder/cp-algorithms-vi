---
tags:
  - Translated
e_maxx_link: binary_pow
---

# Lũy thừa nhị phân {: #binary-exponentiation}

Lũy thừa nhị phân (còn được gọi là lũy thừa bằng cách bình phương - exponentiation by squaring) là một thủ thuật cho phép tính $a^n$ chỉ sử dụng $O(\log n)$ phép nhân (thay vì $O(n)$ phép nhân theo cách tiếp cận ngây thơ).

Nó cũng có những ứng dụng quan trọng trong nhiều bài toán không liên quan đến số học, vì nó
có thể được sử dụng với bất kỳ phép toán nào có tính chất **kết hợp** (associativity):

$$(X \cdot Y) \cdot Z = X \cdot (Y \cdot Z)$$

Rõ ràng nhất điều này áp dụng cho phép nhân modulo, nhân ma trận và
các bài toán khác mà chúng ta sẽ thảo luận bên dưới.

## Thuật toán {: #algorithm}

Nâng $a$ lên lũy thừa $n$ được biểu diễn một cách ngây thơ là nhân $a$ với chính nó $n - 1$ lần:
$a^{n} = a \cdot a \cdot \ldots \cdot a$. Tuy nhiên, cách tiếp cận này không thực tế với $a$ hoặc $n$ lớn.

$a^{b+c} = a^b \cdot a^c$ và $a^{2b} = a^b \cdot a^b = (a^b)^2$.

Ý tưởng của lũy thừa nhị phân là, chúng ta chia nhỏ công việc bằng cách sử dụng biểu diễn nhị phân của số mũ.

Hãy viết $n$ trong hệ cơ số 2, ví dụ:

$$3^{13} = 3^{1101_2} = 3^8 \cdot 3^4 \cdot 3^1$$

Vì số $n$ có chính xác $\lfloor \log_2 n \rfloor + 1$ chữ số trong hệ cơ số 2, chúng ta chỉ cần thực hiện $O(\log n)$ phép nhân, nếu chúng ta biết các lũy thừa $a^1, a^2, a^4, a^8, \dots, a^{2^{\lfloor \log_2 n \rfloor}}$.

Vì vậy chúng ta chỉ cần biết cách nhanh chóng để tính chúng.
May mắn thay điều này rất dễ dàng, vì một phần tử trong dãy chỉ là bình phương của phần tử trước đó.

$$\begin{align}
3^1 &= 3 \\
3^2 &= \left(3^1\right)^2 = 3^2 = 9 \\
3^4 &= \left(3^2\right)^2 = 9^2 = 81 \\
3^8 &= \left(3^4\right)^2 = 81^2 = 6561
\end{align}$$

Vì vậy để có được kết quả cuối cùng cho $3^{13}$, chúng ta chỉ cần nhân ba trong số chúng (bỏ qua $3^2$ vì bit tương ứng trong $n$ không bật):
$3^{13} = 6561 \cdot 81 \cdot 3 = 1594323$

Độ phức tạp cuối cùng của thuật toán này là $O(\log n)$: chúng ta phải tính $\log n$ lũy thừa của $a$, và sau đó phải thực hiện tối đa $\log n$ phép nhân để có được kết quả cuối cùng từ chúng.

Cách tiếp cận đệ quy sau đây thể hiện cùng một ý tưởng:

$$a^n = \begin{cases}
1 &\text{if } n == 0 \\
\left(a^{\frac{n}{2}}\right)^2 &\text{if } n > 0 \text{ and } n \text{ even}\\
\left(a^{\frac{n - 1}{2}}\right)^2 \cdot a &\text{if } n > 0 \text{ and } n \text{ odd}\\
\end{cases}$$

## Cài đặt {: #implementation}

Đầu tiên là cách tiếp cận đệ quy, là bản dịch trực tiếp của công thức đệ quy:

```cpp
long long binpow(long long a, long long b) {
    if (b == 0)
        return 1;
    long long res = binpow(a, b / 2);
    if (b % 2)
        return res * res * a;
    else
        return res * res;
}
```

Cách tiếp cận thứ hai hoàn thành cùng một nhiệm vụ mà không cần đệ quy.
Nó tính toán tất cả các lũy thừa trong một vòng lặp, và nhân những cái có bit được bật tương ứng trong $n$.
Mặc dù độ phức tạp của cả hai cách tiếp cận là như nhau, cách tiếp cận này sẽ nhanh hơn trong thực tế vì chúng ta không tốn chi phí cho các lời gọi đệ quy.

```cpp
long long binpow(long long a, long long b) {
    long long res = 1;
    while (b > 0) {
        if (b & 1)
            res = res * a;
        a = a * a;
        b >>= 1;
    }
    return res;
}
```

## Ứng dụng {: #applications}

### Tính hiệu quả lũy thừa lớn theo modulo một số {: #effective-computation-of-large-exponents-modulo-a-number}

**Bài toán:**
Tính $x^n \bmod m$.
Đây là một thao tác rất phổ biến. Ví dụ nó được sử dụng trong việc tính [nghịch đảo nhân modulo](module-inverse.md).

**Lời giải:**
Vì chúng ta biết rằng toán tử modulo không ảnh hưởng đến phép nhân ($a \cdot b \equiv (a \bmod m) \cdot (b \bmod m) \pmod m$), chúng ta có thể trực tiếp sử dụng cùng một đoạn code, và chỉ cần thay thế mỗi phép nhân bằng một phép nhân modulo:

```cpp
long long binpow(long long a, long long b, long long m) {
    a %= m;
    long long res = 1;
    while (b > 0) {
        if (b & 1)
            res = res * a % m;
        a = a * a % m;
        b >>= 1;
    }
    return res;
}
```

**Lưu ý:**
Có thể tăng tốc thuật toán này cho $b >> m$ lớn.
Nếu $m$ là số nguyên tố $x^n \equiv x^{n \bmod (m-1)} \pmod{m}$ với $m$ nguyên tố, và $x^n \equiv x^{n \bmod{\phi(m)}} \pmod{m}$ với $m$ hợp số.
Điều này suy ra trực tiếp từ định lý nhỏ Fermat và định lý Euler, xem bài viết về [Nghịch đảo Modulo](module-inverse.md#fermat-euler) để biết thêm chi tiết.

### Tính hiệu quả số Fibonacci {: #effective-computation-of-fibonacci-numbers}

**Bài toán:** Tính số Fibonacci thứ $n$, $F_n$.

**Lời giải:** Để biết thêm chi tiết, xem [bài viết về Số Fibonacci](fibonacci-numbers.md).
Chúng tôi sẽ chỉ trình bày tổng quan về thuật toán.
Để tính số Fibonacci tiếp theo, chỉ cần hai số trước đó, vì $F_n = F_{n-1} + F_{n-2}$.
Chúng ta có thể xây dựng một ma trận $2 \times 2$ mô tả phép biến đổi này:
việc chuyển đổi từ $F_i$ và $F_{i+1}$ sang $F_{i+1}$ và $F_{i+2}$.
Ví dụ, áp dụng phép biến đổi này cho cặp $F_0$ và $F_1$ sẽ thay đổi nó thành $F_1$ và $F_2$.
Do đó, chúng ta có thể nâng ma trận biến đổi này lên lũy thừa $n$ để tìm $F_n$ trong độ phức tạp thời gian $O(\log n)$.

### Áp dụng hoán vị $k$ lần {: #applying-a-permutation-k-times data-toc-label='Áp dụng hoán vị <script type="math/tex">k</script> lần' }

**Bài toán:** Bạn được cho một dãy độ dài $n$. Áp dụng một hoán vị cho trước $k$ lần lên nó.

**Lời giải:** Đơn giản là nâng hoán vị lên lũy thừa $k$ bằng cách sử dụng lũy thừa nhị phân, và sau đó áp dụng nó cho dãy. Điều này sẽ cho bạn độ phức tạp thời gian $O(n \log k)$.

```cpp
vector<int> applyPermutation(vector<int> sequence, vector<int> permutation) {
    vector<int> newSequence(sequence.size());
    for(int i = 0; i < sequence.size(); i++) {
        newSequence[i] = sequence[permutation[i]];
    }
    return newSequence;
}

vector<int> permute(vector<int> sequence, vector<int> permutation, long long k) {
    while (k > 0) {
        if (k & 1) {
            sequence = applyPermutation(sequence, permutation);
        }
        permutation = applyPermutation(permutation, permutation);
        k >>= 1;
    }
    return sequence;
}
```

**Lưu ý:** Bài toán này có thể được giải quyết hiệu quả hơn trong thời gian tuyến tính bằng cách xây dựng đồ thị hoán vị và xem xét từng chu trình một cách độc lập. Sau đó bạn có thể tính $k$ modulo kích thước của chu trình và tìm vị trí cuối cùng cho mỗi số là một phần của chu trình này.

### Áp dụng nhanh tập hợp các phép biến đổi hình học vào tập hợp các điểm {: #fast-application-of-a-set-of-geometric-operations-to-a-set-of-points}

**Bài toán:** Cho $n$ điểm $p_i$, áp dụng $m$ phép biến đổi cho mỗi điểm này. Mỗi phép biến đổi có thể là dịch chuyển, tỉ lệ hoặc xoay quanh một trục cho trước một góc cho trước. Ngoài ra còn có một phép toán "lặp" áp dụng một danh sách các phép biến đổi $k$ lần (phép toán "lặp" có thể lồng nhau). Bạn nên áp dụng tất cả các phép biến đổi nhanh hơn $O(n \cdot length)$, trong đó $length$ là tổng số phép biến đổi cần áp dụng (sau khi mở rộng các phép toán "lặp").

**Lời giải:** Hãy xem các loại phép biến đổi khác nhau thay đổi tọa độ như thế nào:

* Phép dịch chuyển: cộng một hằng số khác nhau vào mỗi tọa độ.
* Phép tỉ lệ: nhân mỗi tọa độ với một hằng số khác nhau.
* Phép xoay: phép biến đổi phức tạp hơn (chúng tôi sẽ không đi sâu vào chi tiết ở đây), nhưng mỗi tọa độ mới vẫn có thể được biểu diễn dưới dạng tổ hợp tuyến tính của các tọa độ cũ.

Như bạn có thể thấy, mỗi phép biến đổi có thể được biểu diễn dưới dạng một phép toán tuyến tính trên các tọa độ. Do đó, một phép biến đổi có thể được viết dưới dạng ma trận $4 \times 4$ dạng:

$$\begin{pmatrix}
a_{11} & a_ {12} & a_ {13} & a_ {14} \\
a_{21} & a_ {22} & a_ {23} & a_ {24} \\
a_{31} & a_ {32} & a_ {33} & a_ {34} \\
a_{41} & a_ {42} & a_ {43} & a_ {44}
\end{pmatrix}$$

khi nhân với một vector với các tọa độ cũ và một đơn vị sẽ cho ra một vector mới với các tọa độ mới và một đơn vị:

$$\begin{pmatrix} x & y & z & 1 \end{pmatrix} \cdot
\begin{pmatrix}
a_{11} & a_ {12} & a_ {13} & a_ {14} \\
a_{21} & a_ {22} & a_ {23} & a_ {24} \\
a_{31} & a_ {32} & a_ {33} & a_ {34} \\
a_{41} & a_ {42} & a_ {43} & a_ {44}
\end{pmatrix}
 = \begin{pmatrix} x' & y' & z' & 1 \end{pmatrix}$$

(Tại sao lại đưa vào tọa độ thứ tư giả định, bạn hỏi? Đó là vẻ đẹp của [tọa độ đồng nhất](https://en.wikipedia.org/wiki/Homogeneous_coordinates), tìm thấy ứng dụng tuyệt vời trong đồ họa máy tính. Nếu không có điều này, sẽ không thể thực hiện các phép toán affine như phép dịch chuyển dưới dạng một phép nhân ma trận đơn lẻ, vì nó yêu cầu chúng ta _cộng_ một hằng số vào các tọa độ. Phép biến đổi affine trở thành phép biến đổi tuyến tính trong chiều cao hơn!)

Dưới đây là một số ví dụ về cách các phép biến đổi được biểu diễn dưới dạng ma trận:

* Phép dịch chuyển: dịch chuyển tọa độ $x$ đi $5$, tọa độ $y$ đi $7$ và tọa độ $z$ đi $9$.

$$\begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
5 & 7 & 9 & 1
\end{pmatrix}$$

* Phép tỉ lệ: tỉ lệ tọa độ $x$ gấp $10$ và hai tọa độ kia gấp $5$.

$$\begin{pmatrix}
10 & 0 & 0 & 0 \\
0 & 5 & 0 & 0 \\
0 & 0 & 5 & 0 \\
0 & 0 & 0 & 1
\end{pmatrix}$$

* Phép xoay: xoay $\theta$ độ quanh trục $x$ theo quy tắc bàn tay phải (ngược chiều kim đồng hồ).

$$\begin{pmatrix}
1 & 0 & 0 & 0 \\
0 & \cos \theta & -\sin \theta & 0 \\
0 & \sin \theta & \cos \theta & 0 \\
0 & 0 & 0 & 1
\end{pmatrix}$$

Bây giờ, khi mỗi phép biến đổi được mô tả như một ma trận, chuỗi các phép biến đổi có thể được mô tả như một tích của các ma trận này, và một "vòng lặp" $k$ lần có thể được mô tả như ma trận được nâng lên lũy thừa $k$ (có thể được tính bằng lũy thừa nhị phân trong $O(\log{k})$). Bằng cách này, ma trận đại diện cho tất cả các phép biến đổi có thể được tính trước trong $O(m \log{k})$, và sau đó nó có thể được áp dụng cho mỗi trong số $n$ điểm trong $O(n)$ với tổng độ phức tạp là $O(n + m \log{k})$.


### Số đường đi độ dài $k$ trong đồ thị {: #number-of-paths-of-length-k-in-a-graph data-toc-label='Số đường đi độ dài <script type="math/tex">k</script> trong đồ thị' }

**Bài toán:** Cho một đồ thị có hướng không trọng số gồm $n$ đỉnh, tìm số đường đi có độ dài $k$ từ bất kỳ đỉnh $u$ nào đến bất kỳ đỉnh $v$ nào khác.

**Lời giải:** Bài toán này được xem xét chi tiết hơn trong [một bài viết riêng](../graph/fixed-length-paths.md). Thuật toán bao gồm việc nâng ma trận kề $M$ của đồ thị (một ma trận mà $m_{ij} = 1$ nếu có cạnh từ $i$ đến $j$, hoặc $0$ nếu ngược lại) lên lũy thừa $k$. Bây giờ $m_{ij}$ sẽ là số đường đi có độ dài $k$ từ $i$ đến $j$. Độ phức tạp thời gian của giải pháp này là $O(n^3 \log k)$.

**Lưu ý:** Trong cùng bài viết đó, một biến thể khác của bài toán này cũng được xem xét: khi các cạnh có trọng số và yêu cầu tìm đường đi có trọng số nhỏ nhất chứa chính xác $k$ cạnh. Như đã trình bày trong bài viết đó, bài toán này cũng được giải quyết bằng cách lũy thừa ma trận kề. Ma trận sẽ có trọng số của cạnh từ $i$ đến $j$, hoặc $\infty$ nếu không có cạnh nào như vậy.
Thay vì phép nhân hai ma trận thông thường, một phép toán sửa đổi nên được sử dụng:
thay vì nhân, cả hai giá trị được cộng, và thay vì tính tổng, lấy giá trị nhỏ nhất.
Tức là: $result_{ij} = \min\limits_{1\ \leq\ k\ \leq\ n}(a_{ik} + b_{kj})$.

### Biến thể của lũy thừa nhị phân: nhân hai số theo modulo $m$ {: #variation-of-binary-exponentiation-multiplying-two-numbers-modulo-m data-toc-label='Biến thể của lũy thừa nhị phân: nhân hai số theo modulo <script type="math/tex">m</script>' }

**Bài toán:** Nhân hai số $a$ và $b$ theo modulo $m$. $a$ và $b$ vừa với các kiểu dữ liệu tích hợp sẵn, nhưng tích của chúng quá lớn để vừa với một số nguyên 64-bit. Ý tưởng là tính $a \cdot b \pmod m$ mà không sử dụng số học bignum.

**Lời giải:** Chúng ta chỉ đơn giản áp dụng thuật toán xây dựng nhị phân được mô tả ở trên, chỉ thực hiện phép cộng thay vì phép nhân. Nói cách khác, chúng ta đã "mở rộng" phép nhân hai số thành $O (\log m)$ phép tính cộng và nhân với hai (về bản chất là một phép cộng).

$$a \cdot b = \begin{cases}
0 &\text{if }a = 0 \\
2 \cdot \frac{a}{2} \cdot b &\text{if }a > 0 \text{ and }a \text{ even} \\
2 \cdot \frac{a-1}{2} \cdot b + b &\text{if }a > 0 \text{ and }a \text{ odd}
\end{cases}$$

**Lưu ý:** Bạn có thể giải quyết nhiệm vụ này theo một cách khác bằng cách sử dụng các phép toán dấu phẩy động. Đầu tiên tính biểu thức $\frac{a \cdot b}{m}$ sử dụng số dấu phẩy động và ép kiểu nó sang số nguyên không dấu $q$. Trừ $q \cdot m$ khỏi $a \cdot b$ sử dụng số học số nguyên không dấu và lấy nó theo modulo $m$ để tìm câu trả lời. Giải pháp này trông khá không đáng tin cậy, nhưng nó rất nhanh và rất dễ cài đặt. Xem [tại đây](https://cs.stackexchange.com/questions/77016/modular-multiplication) để biết thêm thông tin.

## Bài tập luyện tập {: #practice-problems}

* [UVa 1230 - MODEX](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=3671)
* [UVa 374 - Big Mod](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=310)
* [UVa 11029 - Leading and Trailing](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1970)
* [Codeforces - Parking Lot](http://codeforces.com/problemset/problem/630/I)
* [leetcode - Count good numbers](https://leetcode.com/problems/count-good-numbers/)
* [Codechef - Chef and Riffles](https://www.codechef.com/JAN221B/problems/RIFFLES)
* [Codeforces - Decoding Genome](https://codeforces.com/contest/222/problem/E)
* [Codeforces - Neural Network Country](https://codeforces.com/contest/852/problem/B)
* [Codeforces - Magic Gems](https://codeforces.com/problemset/problem/1117/D)
* [SPOJ - The last digit](http://www.spoj.com/problems/LASTDIG/)
* [SPOJ - Locker](http://www.spoj.com/problems/LOCKER/)
* [LA - 3722 Jewel-eating Monsters](https://vjudge.net/problem/UVALive-3722)
* [SPOJ - Just add it](http://www.spoj.com/problems/ZSUM/)
* [Codeforces - Stairs and Lines](https://codeforces.com/contest/498/problem/E)
