---
tags:
  - Translated
e_maxx_link: circles_intersection
---

# Giao của hai đường tròn

Bạn được cho hai đường tròn trên một mặt phẳng 2D, mỗi đường tròn được mô tả bằng tọa độ tâm và bán kính của nó. Tìm các điểm giao của chúng (các trường hợp có thể: một hoặc hai điểm, không giao nhau hoặc các đường tròn trùng nhau).

## Giải pháp

Hãy quy bài toán này về [bài toán giao của đường tròn và đường thẳng](circle-line-intersection.md).

Không mất tính tổng quát, giả sử đường tròn thứ nhất có tâm ở gốc tọa độ (nếu điều này không đúng, chúng ta có thể di chuyển gốc tọa độ đến tâm của đường tròn thứ nhất và điều chỉnh tọa độ của các điểm giao tương ứng tại thời điểm xuất ra). Chúng ta có một hệ hai phương trình:

$$x^2+y^2=r_1^2$$

$$(x - x_2)^2 + (y - y_2)^2 = r_2^2$$

Trừ phương trình thứ nhất khỏi phương trình thứ hai để loại bỏ các lũy thừa bậc hai của các biến:

$$x^2+y^2=r_1^2$$

$$x \cdot (-2x_2) + y \cdot (-2y_2) + (x_2^2+y_2^2+r_1^2-r_2^2) = 0$$

Do đó, chúng ta đã quy bài toán ban đầu về bài toán tìm giao điểm của đường tròn thứ nhất và một đường thẳng:

$$Ax + By + C = 0$$

$$\begin{align}
 A &= -2x_2 \\ B &= -2y_2 \\ C &= x_2^2+y_2^2+r_1^2-r_2^2
\end{align}$$

Và bài toán này có thể được giải quyết như được mô tả trong [bài viết tương ứng](circle-line-intersection.md).

Trường hợp suy biến duy nhất chúng ta cần xem xét riêng là khi tâm của các đường tròn trùng nhau. Trong trường hợp này $x_2=y_2=0$, và phương trình đường thẳng sẽ là $C = r_1^2-r_2^2 = 0$. Nếu bán kính của các đường tròn bằng nhau, có vô số điểm giao, nếu chúng khác nhau, không có giao điểm nào.

## Bài tập thực hành

- [RadarFinder](https://community.topcoder.com/stat?c=problem_statement&pm=7766)
- [Runaway to a shadow - Codeforces Round #357](http://codeforces.com/problemset/problem/681/E)
- [ASC 1 Problem F "Get out!"](http://codeforces.com/gym/100199/problem/F)
- [SPOJ: CIRCINT](http://www.spoj.com/problems/CIRCINT/)
- [UVA - 10301 - Rings and Glue](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1242)
- [Codeforces 933C A Colorful Prospect](https://codeforces.com/problemset/problem/933/C)
- [TIMUS 1429 Biscuits](https://acm.timus.ru/problem.aspx?space=1&num=1429)