---
tags:
  - Original
---

# Phương pháp Ngôi sao và Vách ngăn (Stars and bars) {: #stars-and-bars}

Phương pháp Ngôi sao và Vách ngăn là một kỹ thuật toán học để giải quyết một số bài toán tổ hợp nhất định.
Nó xuất hiện bất cứ khi nào bạn muốn đếm số cách để nhóm các đối tượng giống hệt nhau.

## Định lý (Theorem) {: #theorem}

Số cách để đặt $n$ đối tượng giống hệt nhau vào $k$ hộp có nhãn là

$$\binom{n + k - 1}{n}.$$

Chứng minh liên quan đến việc biến đổi các đối tượng thành các ngôi sao và ngăn cách các hộp bằng cách sử dụng các vách ngăn (do đó có tên gọi này).
Ví dụ: chúng ta có thể biểu diễn tình huống sau với $\bigstar | \bigstar \bigstar |~| \bigstar \bigstar$:
trong hộp đầu tiên là một đối tượng, trong hộp thứ hai là hai đối tượng, hộp thứ ba rỗng và trong hộp cuối cùng là hai đối tượng.
Đây là một cách chia 5 đối tượng vào 4 hộp.

Khá rõ ràng rằng, mọi phân hoạch đều có thể được biểu diễn bằng cách sử dụng $n$ ngôi sao và $k - 1$ vách ngăn và mọi hoán vị của các ngôi sao và vách ngăn sử dụng $n$ ngôi sao và $k - 1$ vách ngăn đại diện cho một phân hoạch.
Do đó số cách chia $n$ đối tượng giống hệt nhau vào $k$ hộp có nhãn là cùng một số lượng hoán vị của $n$ ngôi sao và $k - 1$ vách ngăn.
[Hệ số nhị thức](binomial-coefficients.md) cung cấp cho chúng ta công thức mong muốn.

## Số lượng nghiệm nguyên không âm (Number of non-negative integer sums) {: #number-of-non-negative-integer-sums}

Bài toán này là một ứng dụng trực tiếp của định lý.

Bạn muốn đếm số lượng nghiệm của phương trình

$$x_1 + x_2 + \dots + x_k = n$$

với $x_i \ge 0$.

Một lần nữa chúng ta có thể biểu diễn một nghiệm bằng cách sử dụng các ngôi sao và vách ngăn.
Ví dụ: nghiệm $1 + 3 + 0 = 4$ cho $n = 4$, $k = 3$ có thể được biểu diễn bằng $\bigstar | \bigstar \bigstar \bigstar |$.

Dễ thấy rằng, đây chính xác là định lý ngôi sao và vách ngăn.
Do đó nghiệm là $\binom{n + k - 1}{n}$.

## Số lượng nghiệm nguyên dương (Number of positive integer sums) {: #number-of-positive-integer-sums}

Một định lý thứ hai cung cấp một cách giải thích thú vị cho các số nguyên dương. Xem xét các nghiệm cho

$$x_1 + x_2 + \dots + x_k = n$$

với $x_i \ge 1$.

Chúng ta có thể xem xét $n$ ngôi sao, nhưng lần này chúng ta có thể đặt tối đa _một vách ngăn_ giữa các ngôi sao, vì hai vách ngăn giữa các ngôi sao sẽ đại diện cho $x_i=0$, tức là một hộp rỗng.
Có $n-1$ khoảng trống giữa các ngôi sao để đặt $k-1$ vách ngăn, vì vậy nghiệm là $\binom{n-1}{k-1}$.

## Số lượng nghiệm nguyên có cận dưới (Number of lower-bound integer sums) {: #number-of-lower-bound-integer-sums}

Điều này có thể dễ dàng được mở rộng cho các tổng số nguyên với các cận dưới khác nhau.
Tức là chúng ta muốn đếm số lượng nghiệm cho phương trình

$$x_1 + x_2 + \dots + x_k = n$$

với $x_i \ge a_i$.

Sau khi thay thế $x_i' := x_i - a_i$ chúng ta nhận được phương trình đã sửa đổi

$$(x_1' + a_i) + (x_2' + a_i) + \dots + (x_k' + a_k) = n$$

$$\Leftrightarrow ~ ~ x_1' + x_2' + \dots + x_k' = n - a_1 - a_2 - \dots - a_k$$

với $x_i' \ge 0$.
Vì vậy, chúng ta đã giảm bài toán về trường hợp đơn giản hơn với $x_i' \ge 0$ và một lần nữa có thể áp dụng định lý ngôi sao và vách ngăn.

## Số lượng nghiệm nguyên có cận trên (Number of upper-bound integer sums) {: #number-of-upper-bound-integer-sums}

Với một chút trợ giúp của [Nguyên lý bao hàm-loại trừ](./inclusion-exclusion.md), bạn cũng có thể hạn chế các số nguyên với các cận trên.
Xem phần [Số lượng nghiệm nguyên có cận trên](./inclusion-exclusion.md#number-of-upper-bound-integer-sums) trong bài viết tương ứng.

## Bài tập luyện tập {: #practice-problems}

* [Codeforces - Array](https://codeforces.com/contest/57/problem/C)
* [Codeforces - Kyoya and Coloured Balls](https://codeforces.com/problemset/problem/553/A)
* [Codeforces - Colorful Bricks](https://codeforces.com/contest/1081/problem/C)
* [Codeforces - Two Arrays](https://codeforces.com/problemset/problem/1288/C)
* [Codeforces - One-Dimensional Puzzle](https://codeforces.com/contest/1931/problem/G)

---

## Checklist

- Original lines: 83
- Translated lines: 83
- Code blocks changed? No
- Inline code changed? No
- Technical terms kept in English? Yes
- Headings anchors preserved/added correctly? Yes
- I confirm no character was omitted: YES
