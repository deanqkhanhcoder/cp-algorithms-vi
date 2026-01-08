---
tags:
  - Translated
e_maxx_link: circle_line_intersection
---

# Giao điểm đường tròn - đường thẳng (Circle-Line Intersection) {: #circle-line-intersection}

Cho tọa độ của tâm một đường tròn và bán kính của nó, và phương trình của một đường thẳng, bạn được yêu cầu tìm các điểm giao nhau.

## Giải pháp (Solution) {: #solution}

Thay vì giải hệ gồm hai phương trình, chúng ta sẽ tiếp cận bài toán bằng hình học. Theo cách này, chúng ta có được một giải pháp chính xác hơn theo quan điểm về độ ổn định số học.

Chúng ta giả sử không mất tính tổng quát rằng đường tròn có tâm tại gốc tọa độ. Nếu không, chúng ta tịnh tiến nó đến đó và sửa hằng số $C$ trong phương trình đường thẳng. Vì vậy, chúng ta có một đường tròn tâm tại $(0,0)$ bán kính $r$ và một đường thẳng có phương trình $Ax+By+C=0$.

Hãy bắt đầu bằng cách tìm điểm trên đường thẳng gần gốc tọa độ nhất $(x_0, y_0)$. Đầu tiên, nó phải ở khoảng cách

$$ d_0 = \frac{|C|}{\sqrt{A^2+B^2}} $$

Thứ hai, vì vector $(A, B)$ vuông góc với đường thẳng, tọa độ của điểm phải tỷ lệ với tọa độ của vector này. Vì chúng ta biết khoảng cách của điểm đến gốc tọa độ, chúng ta chỉ cần chia tỷ lệ vector $(A, B)$ theo độ dài này, và chúng ta sẽ nhận được:

$$\begin{align}
x_0 &= - \frac{AC}{A^2 + B^2} \\
y_0 &= - \frac{BC}{A^2 + B^2} 
\end{align}$$

Các dấu trừ không quá rõ ràng, nhưng chúng có thể được kiểm chứng dễ dàng bằng cách thay $x_0$ và $y_0$ vào phương trình của đường thẳng.

Ở giai đoạn này chúng ta có thể xác định số lượng giao điểm, và thậm chí tìm giải pháp khi có một hoặc không có điểm nào. Thật vậy, nếu khoảng cách từ $(x_0, y_0)$ đến gốc tọa độ $d_0$ lớn hơn bán kính $r$, câu trả lời là **không có điểm nào**. Nếu $d_0=r$, câu trả lời là **một điểm** $(x_0, y_0)$. Nếu $d_0<r$, có hai điểm giao nhau, và bây giờ chúng ta phải tìm tọa độ của chúng.

Vì vậy, chúng ta biết rằng điểm $(x_0, y_0)$ nằm bên trong đường tròn. Hai điểm giao nhau, $(a_x, a_y)$ và $(b_x, b_y)$, phải thuộc đường thẳng $Ax+By+C=0$ và phải ở cùng khoảng cách $d$ từ $(x_0, y_0)$, và khoảng cách này rất dễ tìm:

$$ d = \sqrt{r^2 - \frac{C^2}{A^2 + B^2}} $$

Lưu ý rằng vector $(-B, A)$ cùng phương với đường thẳng, và do đó chúng ta có thể tìm các điểm đang xét bằng cách cộng và trừ vector $(-B,A)$, được chia tỷ lệ theo độ dài $d$, vào điểm $(x_0, y_0)$.

Cuối cùng, các phương trình của hai giao điểm là:

$$\begin{align}
m &= \sqrt{\frac{d^2}{A^2 + B^2}} \\
a_x &= x_0 + B \cdot m, a_y = y_0 - A \cdot m \\
b_x &= x_0 - B \cdot m, b_y = y_0 + A \cdot m
\end{align}$$

Nếu chúng ta giải hệ phương trình ban đầu bằng các phương pháp đại số, chúng ta có thể nhận được một câu trả lời ở một dạng khác với sai số lớn hơn. Phương pháp hình học được mô tả ở đây trực quan hơn và chính xác hơn.

## Cài đặt (Implementation) {: #implementation}

Như đã chỉ ra ở phần đầu, chúng ta giả sử rằng đường tròn có tâm tại gốc tọa độ, và do đó đầu vào của chương trình là bán kính $r$ của đường tròn và các tham số $A$, $B$ và $C$ của phương trình đường thẳng.

```cpp
double r, a, b, c; // given as input
double x0 = -a*c/(a*a+b*b), y0 = -b*c/(a*a+b*b);
if (c*c > r*r*(a*a+b*b)+EPS)
    puts ("no points");
else if (abs (c*c - r*r*(a*a+b*b)) < EPS) {
    puts ("1 point");
    cout << x0 << ' ' << y0 << '\n';
}
else {
    double d = r*r - c*c/(a*a+b*b);
    double mult = sqrt (d / (a*a+b*b));
    double ax, ay, bx, by;
    ax = x0 + b * mult;
    bx = x0 - b * mult;
    ay = y0 - a * mult;
    by = y0 + a * mult;
    puts ("2 points");
    cout << ax << ' ' << ay << '\n' << bx << ' ' << by << '\n';
}
```

## Bài tập (Practice Problems) {: #practice-problems}

- [CODECHEF: ANDOOR](https://www.codechef.com/problems/ANDOOR)
