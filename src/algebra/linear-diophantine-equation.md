---
tags:
  - Translated
e_maxx_link: diofant_2_equation
---

# Phương trình Diophantine tuyến tính

Một phương trình Diophantine tuyến tính (hai biến) là một phương trình có dạng tổng quát:

$$ax + by = c$$

trong đó $a$, $b$, $c$ là các số nguyên đã cho, và $x$, $y$ là các số nguyên chưa biết.

Trong bài viết này, chúng ta xem xét một số bài toán cổ điển về các phương trình này:

* tìm một nghiệm
* tìm tất cả các nghiệm
* tìm số lượng nghiệm và chính các nghiệm đó trong một khoảng cho trước
* tìm nghiệm có giá trị nhỏ nhất của $x + y$

## Trường hợp suy biến

Một trường hợp suy biến cần được quan tâm là khi $a = b = 0$. Dễ dàng thấy rằng chúng ta hoặc không có nghiệm hoặc có vô số nghiệm, tùy thuộc vào việc $c = 0$ hay không. Trong phần còn lại của bài viết này, chúng ta sẽ bỏ qua trường hợp này.

## Giải pháp giải tích

Khi $a \neq 0$ và $b \neq 0$, phương trình $ax+by=c$ có thể được coi tương đương với một trong các phương trình sau:

\begin{align}
ax &\equiv c \pmod b \\
by &\equiv c \pmod a
\end{align}

Không mất tính tổng quát, giả sử $b \neq 0$ và xét phương trình đầu tiên. Khi $a$ và $b$ nguyên tố cùng nhau, nghiệm của nó được cho là

$$x \equiv ca^{-1} \pmod b,$$ 

trong đó $a^{-1}$ là [nghịch đảo modular](module-inverse.md) của $a$ modulo $b$.

Khi $a$ và $b$ không nguyên tố cùng nhau, các giá trị của $ax$ modulo $b$ đối với mọi số nguyên $x$ đều chia hết cho $g=\gcd(a, b)$, vì vậy nghiệm chỉ tồn tại khi $c$ chia hết cho $g$. Trong trường hợp này, một trong các nghiệm có thể được tìm thấy bằng cách rút gọn phương trình cho $g$:

$$(a/g) x \equiv (c/g) \pmod{b/g}.$$ 

Theo định nghĩa của $g$, các số $a/g$ và $b/g$ là nguyên tố cùng nhau, vì vậy nghiệm được cho một cách tường minh là

$$\begin{cases}
x \equiv (c/g)(a/g)^{-1}\pmod{b/g},\\y = \frac{c-ax}{b}.
\end{cases}$$ 

## Giải pháp thuật toán

**Bổ đề Bézout** (còn gọi là đồng nhất thức Bézout) là một kết quả hữu ích có thể được sử dụng để hiểu giải pháp sau. 

> Đặt $g = \gcd(a,b)$. Khi đó tồn tại các số nguyên $x,y$ sao cho $ax + by = g$. 
> 
> Hơn nữa, $g$ là số nguyên dương nhỏ nhất có thể được viết dưới dạng $ax + by$; tất cả các số nguyên có dạng $ax + by$ đều là bội của $g$. 

Để tìm một nghiệm của phương trình Diophantine với 2 ẩn, bạn có thể sử dụng [Thuật toán Euclid mở rộng](extended-euclid-algorithm.md). Đầu tiên, giả sử rằng $a$ và $b$ không âm. Khi chúng ta áp dụng thuật toán Euclid mở rộng cho $a$ và $b$, chúng ta có thể tìm thấy ước chung lớn nhất $g$ của chúng và 2 số $x_g$ và $y_g$ sao cho:

$$a x_g + b y_g = g$$ 

Nếu $c$ chia hết cho $g = \gcd(a, b)$, thì phương trình Diophantine đã cho có nghiệm, nếu không thì nó không có nghiệm nào. Chứng minh rất đơn giản: một tổ hợp tuyến tính của hai số chia hết cho ước chung của chúng.

Bây giờ giả sử rằng $c$ chia hết cho $g$, thì chúng ta có:

$$a \cdot x_g \cdot \frac{c}{g} + b \cdot y_g \cdot \frac{c}{g} = c$$ 

Do đó một trong các nghiệm của phương trình Diophantine là:

$$x_0 = x_g \cdot \frac{c}{g},$$ 

$$y_0 = y_g \cdot \frac{c}{g}.$$ 

Ý tưởng trên vẫn hoạt động khi $a$ hoặc $b$ hoặc cả hai đều âm. Chúng ta chỉ cần thay đổi dấu của $x_0$ và $y_0$ khi cần thiết.

Cuối cùng, chúng ta có thể triển khai ý tưởng này như sau (lưu ý rằng mã này không xét trường hợp $a = b = 0$):

```{.cpp file=linear_diophantine_any}
int gcd(int a, int b, int& x, int& y) {
    if (b == 0) {
        x = 1;
        y = 0;
        return a;
    }
    int x1, y1;
    int d = gcd(b, a % b, x1, y1);
    x = y1;
    y = x1 - y1 * (a / b);
    return d;
}

bool find_any_solution(int a, int b, int c, int &x0, int &y0, int &g) {
    g = gcd(abs(a), abs(b), x0, y0);
    if (c % g) {
        return false;
    }

    x0 *= c / g;
    y0 *= c / g;
    if (a < 0) x0 = -x0;
    if (b < 0) y0 = -y0;
    return true;
}
```

## Tìm tất cả các nghiệm

Từ một nghiệm $(x_0, y_0)$, chúng ta có thể thu được tất cả các nghiệm của phương trình đã cho.

Đặt $g = \gcd(a, b)$ và đặt $x_0, y_0$ là các số nguyên thỏa mãn:

$$a \cdot x_0 + b \cdot y_0 = c$$ 

Bây giờ, chúng ta nên thấy rằng việc cộng $b / g$ vào $x_0$, và đồng thời trừ $a / g$ khỏi $y_0$ sẽ không phá vỡ đẳng thức:

$$a \cdot \left(x_0 + \frac{b}{g}\right) + b \cdot \left(y_0 - \frac{a}{g}\right) = a \cdot x_0 + b \cdot y_0 + a \cdot \frac{b}{g} - b \cdot \frac{a}{g} = c$$ 

Rõ ràng, quá trình này có thể được lặp lại, vì vậy tất cả các số có dạng:

$$x = x_0 + k \cdot \frac{b}{g}$$ 

$$y = y_0 - k \cdot \frac{a}{g}$$ 

đều là nghiệm của phương trình Diophantine đã cho.

Vì phương trình là tuyến tính, tất cả các nghiệm nằm trên cùng một đường thẳng, và theo định nghĩa của $g$, đây là tập hợp tất cả các nghiệm có thể có của phương trình Diophantine đã cho.

## Tìm số lượng nghiệm và các nghiệm trong một khoảng cho trước

Từ phần trước, rõ ràng là nếu chúng ta không áp đặt bất kỳ hạn chế nào đối với các nghiệm, sẽ có vô số nghiệm. Vì vậy, trong phần này, chúng ta thêm một số hạn chế về khoảng của $x$ và $y$, và chúng ta sẽ cố gắng đếm và liệt kê tất cả các nghiệm.

Đặt có hai khoảng: $[min_x; max_x]$ và $[min_y; max_y]$ và giả sử chúng ta chỉ muốn tìm các nghiệm trong hai khoảng này.

Lưu ý rằng nếu $a$ hoặc $b$ bằng $0$, thì bài toán chỉ có một nghiệm. Chúng ta không xét trường hợp này ở đây.

Đầu tiên, chúng ta có thể tìm một nghiệm có giá trị nhỏ nhất của $x$, sao cho $x \ge min_x$. Để làm điều này, trước tiên chúng ta tìm một nghiệm bất kỳ của phương trình Diophantine. Sau đó, chúng ta dịch chuyển nghiệm này để có được $x \ge min_x$ (sử dụng những gì chúng ta biết về tập hợp tất cả các nghiệm trong phần trước). Điều này có thể được thực hiện trong $O(1)$.
Đồng ký hiệu giá trị nhỏ nhất này của $x$ là $l_{x1}$.

Tương tự, chúng ta có thể tìm giá trị lớn nhất của $x$ thỏa mãn $x \le max_x$. Ký hiệu giá trị lớn nhất này của $x$ là $r_{x1}$.

Tương tự, chúng ta có thể tìm giá trị nhỏ nhất của $y$ $(y \ge min_y)$ và giá trị lớn nhất của $y$ $(y \le max_y)$. Ký hiệu các giá trị tương ứng của $x$ là $l_{x2}$ và $r_{x2}$.

Nghiệm cuối cùng là tất cả các nghiệm với x trong giao của $[l_{x1}, r_{x1}]$ và $[l_{x2}, r_{x2}]$. Đặt giao này là $[l_x, r_x]$.

Sau đây là đoạn mã thực hiện ý tưởng này.
Lưu ý rằng chúng ta chia $a$ và $b$ ở đầu cho $g$.
Vì phương trình $a x + b y = c$ tương đương với phương trình $\frac{a}{g} x + \frac{b}{g} y = \frac{c}{g}$, chúng ta có thể sử dụng phương trình này thay thế và có $\gcd(\frac{a}{g}, \frac{b}{g}) = 1$, điều này đơn giản hóa các công thức.

```{.cpp file=linear_diophantine_all}
void shift_solution(int & x, int & y, int a, int b, int cnt) {
    x += cnt * b;
    y -= cnt * a;
}

int find_all_solutions(int a, int b, int c, int minx, int maxx, int miny, int maxy) {
    int x, y, g;
    if (!find_any_solution(a, b, c, x, y, g))
        return 0;
    a /= g;
    b /= g;

    int sign_a = a > 0 ? +1 : -1;
    int sign_b = b > 0 ? +1 : -1;

    shift_solution(x, y, a, b, (minx - x) / b);
    if (x < minx)
        shift_solution(x, y, a, b, sign_b);
    if (x > maxx)
        return 0;
    int lx1 = x;

    shift_solution(x, y, a, b, (maxx - x) / b);
    if (x > maxx)
        shift_solution(x, y, a, b, -sign_b);
    int rx1 = x;

    shift_solution(x, y, a, b, -(miny - y) / a);
    if (y < miny)
        shift_solution(x, y, a, b, -sign_a);
    if (y > maxy)
        return 0;
    int lx2 = x;

    shift_solution(x, y, a, b, -(maxy - y) / a);
    if (y > maxy)
        shift_solution(x, y, a, b, sign_a);
    int rx2 = x;

    if (lx2 > rx2)
        swap(lx2, rx2);
    int lx = max(lx1, lx2);
    int rx = min(rx1, rx2);

    if (lx > rx)
        return 0;
    return (rx - lx) / abs(b) + 1;
}
```

Khi chúng ta có $l_x$ và $r_x$, việc liệt kê tất cả các nghiệm cũng rất đơn giản. Chỉ cần lặp qua $x = l_x + k \cdot \frac{b}{g}$ với mọi $k \ge 0$ cho đến khi $x = r_x$, và tìm các giá trị $y$ tương ứng bằng cách sử dụng phương trình $a x + b y = c$.

## Tìm nghiệm có giá trị nhỏ nhất của $x + y$ { data-toc-label='Find the solution with minimum value of <script type="math/tex">x + y</script>' }

Ở đây, $x$ và $y$ cũng cần được đưa ra một số hạn chế, nếu không, câu trả lời có thể trở thành vô cực âm.

Ý tưởng tương tự như phần trước: Chúng ta tìm một nghiệm bất kỳ của phương trình Diophantine, và sau đó dịch chuyển nghiệm để thỏa mãn một số điều kiện.

Cuối cùng, sử dụng kiến thức về tập hợp tất cả các nghiệm để tìm giá trị nhỏ nhất:

$$x' = x + k \cdot \frac{b}{g},$$ 

$$y' = y - k \cdot \frac{a}{g}.$$ 

Lưu ý rằng $x + y$ thay đổi như sau:

$$x' + y' = x + y + k \cdot \left(\frac{b}{g} - \frac{a}{g}\right) = x + y + k \cdot \frac{b-a}{g}$$ 

Nếu $a < b$, chúng ta cần chọn giá trị nhỏ nhất có thể của $k$. Nếu $a > b$, chúng ta cần chọn giá trị lớn nhất có thể của $k$. Nếu $a = b$, tất cả các nghiệm sẽ có cùng tổng $x + y$.

## Bài tập luyện tập

* [Spoj - Crucial Equation](http://www.spoj.com/problems/CEQU/)
* [SGU 106](http://codeforces.com/problemsets/acmsguru/problem/99999/106)
* [Codeforces - Ebony and Ivory](http://codeforces.com/contest/633/problem/A)
* [Codechef - Get AC in one go](https://www.codechef.com/problems/COPR16G)
* [LightOj - Solutions to an equation](http://www.lightoj.com/volume_showproblem.php?problem=1306)
* [Atcoder - F - S = 1](https://atcoder.jp/contests/abc340/tasks/abc340_f)