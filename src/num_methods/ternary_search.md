---
tags:
  - Translated
e_maxx_link: ternary_search
---	

# Tìm kiếm tam phân (Ternary Search) {: #ternary-search}

Chúng ta được cho một hàm $f(x)$ đơn mode (unimodal) trên một khoảng $[l, r]$. Hàm đơn mode có nghĩa là hàm có một trong hai hành vi sau:

1. Hàm tăng nghiêm ngặt trước, đạt cực đại (tại một điểm hoặc trên một khoảng), và sau đó giảm nghiêm ngặt.

2. Hàm giảm nghiêm ngặt trước, đạt cực tiểu, và sau đó tăng nghiêm ngặt.

Trong bài viết này, chúng tôi sẽ giả định kịch bản đầu tiên.
Kịch bản thứ hai hoàn toàn đối xứng với kịch bản đầu tiên.

Nhiệm vụ là tìm giá trị lớn nhất của hàm $f(x)$ trên khoảng $[l, r]$.

## Thuật toán (Algorithm) {: #algorithm}

Xem xét bất kỳ 2 điểm $m_1$, và $m_2$ trong khoảng này: $l < m_1 < m_2 < r$. Chúng ta đánh giá hàm tại $m_1$ và $m_2$, tức là tìm các giá trị của $f(m_1)$ và $f(m_2)$. Bây giờ, chúng ta nhận được một trong ba tùy chọn:

-   $f(m_1) < f(m_2)$

    Cực đại mong muốn không thể nằm ở phía bên trái của $m_1$, tức là trên khoảng $[l, m_1]$, vì cả hai điểm $m_1$ và $m_2$ hoặc chỉ $m_1$ thuộc về khu vực mà hàm tăng. Trong cả hai trường hợp, điều này có nghĩa là chúng ta phải tìm kiếm cực đại trong đoạn $[m_1, r]$.

-   $f(m_1) > f(m_2)$

    Tình huống này đối xứng với tình huống trước: cực đại không thể nằm ở phía bên phải của $m_2$, tức là trên khoảng $[m_2, r]$, và không gian tìm kiếm giảm xuống đoạn $[l, m_2]$.

-   $f(m_1) = f(m_2)$

    Chúng ta có thể thấy rằng hoặc cả hai điểm này thuộc về khu vực mà giá trị của hàm được tối đa hóa, hoặc $m_1$ nằm trong khu vực có giá trị tăng và $m_2$ nằm trong khu vực có giá trị giảm (ở đây chúng ta đã sử dụng tính nghiêm ngặt của hàm tăng/giảm). Do đó, không gian tìm kiếm giảm xuống còn $[m_1, m_2]$. Để đơn giản hóa mã, trường hợp này có thể được kết hợp với bất kỳ trường hợp nào trước đó.

Do đó, dựa trên so sánh các giá trị trong hai điểm bên trong, chúng ta có thể thay thế khoảng hiện tại $[l, r]$ bằng một khoảng mới, ngắn hơn $[l^\prime, r^\prime]$. Áp dụng lặp đi lặp lại quy trình được mô tả cho khoảng, chúng ta có thể nhận được một khoảng ngắn tùy ý. Cuối cùng, độ dài của nó sẽ nhỏ hơn một hằng số được xác định trước nhất định (độ chính xác) và quá trình có thể dừng lại. Đây là một phương pháp số, vì vậy chúng ta có thể giả định rằng sau đó hàm đạt cực đại tại tất cả các điểm của khoảng cuối cùng $[l, r]$. Không mất tính tổng quát, chúng ta có thể lấy $f(l)$ làm giá trị trả về.

Chúng tôi đã không áp đặt bất kỳ hạn chế nào đối với việc chọn điểm $m_1$ và $m_2$. Lựa chọn này sẽ xác định tốc độ hội tụ và độ chính xác của việc triển khai. Cách phổ biến nhất là chọn các điểm sao cho chúng chia khoảng $[l, r]$ thành ba phần bằng nhau. Vì vậy, chúng ta có

$$m_1 = l + \frac{(r - l)}{3}$$

$$m_2 = r - \frac{(r - l)}{3}$$ 

Nếu $m_1$ và $m_2$ được chọn gần nhau hơn, tốc độ hội tụ sẽ tăng nhẹ.

### Phân tích thời gian chạy (Run time analysis) {: #run-time-analysis}

$$T(n) = T({2n}/{3}) + O(1) = \Theta(\log n)$$

Nó có thể được hình dung như sau: mỗi lần sau khi đánh giá hàm tại các điểm $m_1$ và $m_2$, về cơ bản chúng ta đang bỏ qua khoảng một phần ba khoảng, bên trái hoặc bên phải. Do đó, kích thước của không gian tìm kiếm là ${2n}/{3}$ so với ban đầu.

Áp dụng [Định lý Thợ](https://en.wikipedia.org/wiki/Master_theorem_(analysis_of_algorithms)), chúng ta nhận được ước tính độ phức tạp mong muốn.

### Trường hợp đối số nguyên (The case of the integer arguments) {: #the-case-of-the-integer-arguments}

Nếu $f(x)$ nhận tham số nguyên, khoảng $[l, r]$ trở nên rời rạc. Vì chúng tôi không áp đặt bất kỳ hạn chế nào đối với việc lựa chọn điểm $m_1$ và $m_2$, tính chính xác của thuật toán không bị ảnh hưởng. $m_1$ và $m_2$ vẫn có thể được chọn để chia $[l, r]$ thành 3 phần xấp xỉ bằng nhau.

Sự khác biệt xảy ra trong tiêu chí dừng của thuật toán. Tìm kiếm tam phân sẽ phải dừng khi $(r - l) < 3$, bởi vì trong trường hợp đó chúng ta không thể chọn $m_1$ và $m_2$ khác nhau cũng như khác với $l$ và $r$, và điều này có thể gây ra vòng lặp vô hạn. Khi $(r - l) < 3$, nhóm điểm ứng cử viên còn lại $(l, l + 1, \ldots, r)$ cần được kiểm tra để tìm điểm tạo ra giá trị cực đại $f(x)$.

### Tìm kiếm tỷ lệ vàng (Golden section search) {: #golden-section-search}

Trong một số trường hợp, tính toán $f(x)$ có thể khá chậm, nhưng việc giảm số lần lặp là không khả thi do các vấn đề về độ chính xác. May mắn thay, có thể chỉ tính toán $f(x)$ một lần ở mỗi lần lặp (ngoại trừ lần đầu tiên).

Để xem cách thực hiện việc này, hãy xem lại phương pháp lựa chọn cho $m_1$ và $m_2$. Giả sử rằng chúng ta chọn $m_1$ và $m_2$ trên $[l, r]$ theo cách mà $\frac{r - l}{r - m_1} = \frac{r - l}{m_2 - l} = \varphi$ trong đó $\varphi$ là một hằng số nào đó. Để giảm lượng tính toán, chúng tôi muốn chọn $\varphi$ sao cho trong lần lặp tiếp theo, một trong các điểm đánh giá mới $m_1'$, $m_2'$ sẽ trùng với $m_1$ hoặc $m_2$, để chúng ta có thể sử dụng lại giá trị hàm đã tính toán.

Bây giờ giả sử rằng sau lần lặp hiện tại, chúng ta đặt $l = m_1$. Khi đó điểm $m_1'$ sẽ thỏa mãn $\frac{r - m_1}{r - m_1'} = \varphi$. Chúng tôi muốn điểm này trùng với $m_2$, nghĩa là $\frac{r - m_1}{r - m_2} = \varphi$.

Nhân cả hai vế của $\frac{r - m_1}{r - m_2} = \varphi$ với $\frac{r - m_2}{r - l}$ chúng ta thu được $\frac{r - m_1}{r - l} = \varphi\frac{r - m_2}{r - l}$. Lưu ý rằng $\frac{r - m_1}{r - l} = \frac{1}{\varphi}$ và $\frac{r - m_2}{r - l} = \frac{r - l + l - m_2}{r - l} = 1 - \frac{1}{\varphi}$. Thay thế và nhân với $\varphi$, chúng ta thu được phương trình sau:

$\varphi^2 - \varphi - 1 = 0$

Đây là một phương trình tỷ lệ vàng nổi tiếng. Giải nó mang lại $\frac{1 \pm \sqrt{5}}{2}$. Vì $\varphi$ phải dương, chúng ta thu được $\varphi = \frac{1 + \sqrt{5}}{2}$. Bằng cách áp dụng cùng một logic cho trường hợp khi chúng ta đặt $r = m_2$ và muốn $m_2'$ trùng với $m_1$, chúng ta cũng thu được cùng một giá trị của $\varphi$. Vì vậy, nếu chúng ta chọn $m_1 = l + \frac{r - l}{1 + \varphi}$ và $m_2 = r - \frac{r - l}{1 + \varphi}$, trên mỗi lần lặp, chúng ta có thể sử dụng lại một trong các giá trị $f(x)$ được tính toán trong lần lặp trước đó.

## Cài đặt (Implementation) {: #implementation}

```cpp
double ternary_search(double l, double r) {
	double eps = 1e-9;				//đặt giới hạn sai số ở đây
	while (r - l > eps) {
		double m1 = l + (r - l) / 3;
		double m2 = r - (r - l) / 3;
		double f1 = f(m1);		//đánh giá hàm tại m1
		double f2 = f(m2);		//đánh giá hàm tại m2
		if (f1 < f2)
			l = m1;
		else
			r = m2;
	}
	return f(l);					//trả về cực đại của f(x) trong [l, r]
}
```

Ở đây `eps` thực tế là sai số tuyệt đối (không tính đến sai số do tính toán không chính xác của hàm).

Thay vì tiêu chí `r - l > eps`, chúng ta có thể chọn một số không đổi lần lặp làm tiêu chí dừng. Số lần lặp nên được chọn để đảm bảo độ chính xác cần thiết. Thông thường, trong hầu hết các thử thách lập trình, giới hạn sai số là ${10}^{-6}$ và do đó 200 - 300 lần lặp là đủ. Ngoài ra, số lần lặp không phụ thuộc vào các giá trị của $l$ và $r$, vì vậy số lần lặp tương ứng với sai số tương đối cần thiết.

## Bài tập (Practice Problems) {: #practice-problems}

- [Codeforces - New Bakery](https://codeforces.com/problemset/problem/1978/B)
- [Codechef - Race time](https://www.codechef.com/problems/AMCS03)
- [Hackerearth - Rescuer](https://www.hackerearth.com/problem/algorithm/rescuer-2d2495cb/)
- [Spoj - Building Construction](http://www.spoj.com/problems/KOPC12A/)
- [Codeforces - Weakness and Poorness](http://codeforces.com/problemset/problem/578/C)
* [LOJ - Closest Distance](http://lightoj.com/volume_showproblem.php?problem=1146)
* [GYM - Dome of Circus (D)](http://codeforces.com/gym/101309)
* [UVA - Galactic Taxes](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=4898)
* [GYM - Chasing the Cheetahs (A)](http://codeforces.com/gym/100829)
* [UVA - 12197 - Trick or Treat](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3349)
* [SPOJ - Building Construction](http://www.spoj.com/problems/KOPC12A/)
* [Codeforces - Devu and his Brother](https://codeforces.com/problemset/problem/439/D)
* [Codechef - Is This JEE ](https://www.codechef.com/problems/ICM2003)
* [Codeforces - Restorer Distance](https://codeforces.com/contest/1355/problem/E)
* [TIMUS 1058 Chocolate](https://acm.timus.ru/problem.aspx?space=1&num=1058)
* [TIMUS 1436 Billboard](https://acm.timus.ru/problem.aspx?space=1&num=1436)
* [TIMUS 1451 Beerhouse Tale](https://acm.timus.ru/problem.aspx?space=1&num=1451)
* [TIMUS 1719 Kill the Shaitan-Boss](https://acm.timus.ru/problem.aspx?space=1&num=1719)
* [TIMUS 1913 Titan Ruins: Alignment of Forces](https://acm.timus.ru/problem.aspx?space=1&num=1913)
