---
tags:
  - Original
---

# Bài toán chia kẹo Euler

Bài toán chia kẹo Euler (sao và vạch) là một kỹ thuật toán học để giải quyết một số bài toán tổ hợp nhất định.
Nó xuất hiện bất cứ khi nào bạn muốn đếm số cách để nhóm các đối tượng giống hệt nhau.

## Định lý

Số cách để đặt $n$ đối tượng giống hệt nhau vào $k$ hộp có nhãn là

$$\binom{n + k - 1}{n}.$$

Chứng minh liên quan đến việc biến các đối tượng thành các ngôi sao và ngăn cách các hộp bằng các thanh vạch (do đó có tên gọi này).
Ví dụ: chúng ta có thể biểu diễn tình huống sau bằng $\bigstar | \bigstar \bigstar |~| \bigstar \bigstar$:
trong hộp thứ nhất có một vật, trong hộp thứ hai có hai vật, hộp thứ ba trống và trong hộp cuối cùng có hai vật.
Đây là một cách chia 5 vật vào 4 hộp.

Rõ ràng là, mọi phân hoạch đều có thể được biểu diễn bằng $n$ ngôi sao và $k - 1$ thanh vạch và mọi hoán vị sao và vạch sử dụng $n$ ngôi sao và $k - 1$ thanh vạch đều biểu diễn một phân hoạch.
Do đó, số cách để chia $n$ đối tượng giống hệt nhau vào $k$ hộp có nhãn bằng với số hoán vị của $n$ ngôi sao và $k - 1$ thanh vạch.
[Tổ hợp](binomial-coefficients.md) cho chúng ta công thức mong muốn.

## Số nghiệm nguyên không âm

Bài toán này là một ứng dụng trực tiếp của định lý.

Bạn muốn đếm số nghiệm của phương trình 

$$x_1 + x_2 + \dots + x_k = n$$

với $x_i \ge 0$.

Một lần nữa, chúng ta có thể biểu diễn một nghiệm bằng cách sử dụng sao và vạch.
Ví dụ: nghiệm $1 + 3 + 0 = 4$ cho $n = 4$, $k = 3$ có thể được biểu diễn bằng $\bigstar | \bigstar \bigstar \bigstar |$.

Dễ thấy rằng, đây chính xác là định lý sao và vạch.
Do đó, nghiệm là $\binom{n + k - 1}{n}$.

## Số nghiệm nguyên dương

Một định lý thứ hai cung cấp một diễn giải tốt đẹp cho các số nguyên dương. Xét các nghiệm của 

$$x_1 + x_2 + \dots + x_k = n$$

với $x_i \ge 1$.

Chúng ta có thể coi $n$ ngôi sao, nhưng lần này chúng ta có thể đặt nhiều nhất _một vạch_ giữa các ngôi sao, vì hai vạch giữa các ngôi sao sẽ đại diện cho $x_i=0$, tức là một hộp trống. 
Có $n-1$ khoảng trống giữa các ngôi sao để đặt $k-1$ vạch, vì vậy nghiệm là $\binom{n-1}{k-1}$. 

## Số nghiệm nguyên có cận dưới

Điều này có thể dễ dàng được mở rộng cho các tổng số nguyên với các cận dưới khác nhau.
Tức là, chúng ta muốn đếm số nghiệm của phương trình

$$x_1 + x_2 + \dots + x_k = n$$

với $x_i \ge a_i$.

Sau khi thay thế $x_i' := x_i - a_i$, chúng ta nhận được phương trình đã sửa đổi

$$(x_1' + a_i) + (x_2' + a_i) + \dots + (x_k' + a_k) = n$$

$$\Leftrightarrow ~ ~ x_1' + x_2' + \dots + x_k' = n - a_1 - a_2 - \dots - a_k$$

với $x_i' \ge 0$.
Vì vậy, chúng ta đã quy bài toán về trường hợp đơn giản hơn với $x_i' \ge 0$ và một lần nữa có thể áp dụng định lý sao và vạch.

## Số nghiệm nguyên có cận trên

Với một chút trợ giúp của [Nguyên lý Bao hàm-Loại trừ](./inclusion-exclusion.md), bạn cũng có thể hạn chế các số nguyên bằng các cận trên.
Xem phần [Số lượng tổng số nguyên có cận trên](./inclusion-exclusion.md#number-of-upper-bound-integer-sums) trong bài viết tương ứng.

## Bài tập luyện tập

* [Codeforces - Array](https://codeforces.com/contest/57/problem/C)
* [Codeforces - Kyoya and Coloured Balls](https://codeforces.com/problemset/problem/553/A)
* [Codeforces - Colorful Bricks](https://codeforces.com/contest/1081/problem/C)
* [Codeforces - Two Arrays](https://codeforces.com/problemset/problem/1288/C)
* [Codeforces - One-Dimensional Puzzle](https://codeforces.com/contest/1931/problem/G)