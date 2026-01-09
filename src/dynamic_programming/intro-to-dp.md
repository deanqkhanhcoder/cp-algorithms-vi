---
tags:
  - Translated
---

# Giới thiệu về Quy hoạch động (Introduction to Dynamic Programming) {: #gioi-thieu-ve-quy-hoach-dong}

Bản chất của quy hoạch động (dynamic programming) là tránh tính toán lặp lại. Thông thường, các bài toán quy hoạch động thường có thể giải quyết một cách tự nhiên bằng đệ quy. Trong những trường hợp như vậy, cách dễ nhất là viết giải pháp đệ quy, sau đó lưu lại các trạng thái lặp lại trong một bảng tra cứu (lookup table). Quá trình này được gọi là quy hoạch động từ trên xuống (top-down) với ghi nhớ (memoization).

Một trong những ví dụ cơ bản, kinh điển nhất của quá trình này là dãy Fibonacci. Công thức đệ quy của nó là $f(n) = f(n-1) + f(n-2)$ với $n \ge 2$ và $f(0)=0$ và $f(1)=1$. Trong C++, điều này sẽ được biểu thị như sau:

```cpp
int f(int n) {
    if (n == 0) return 0;
    if (n == 1) return 1;
    return f(n - 1) + f(n - 2);
}
```

Thời gian chạy của hàm đệ quy này là cấp số mũ - xấp xỉ $O(2^n)$ vì một lệnh gọi hàm ($f(n)$) dẫn đến 2 lệnh gọi hàm có kích thước tương tự ($f(n-1)$ và $f(n-2)$).

## Tăng tốc Fibonacci với Quy hoạch động (Ghi nhớ) (Speeding up Fibonacci with Dynamic Programming (Memoization)) {: #speeding-up-fibonacci-with-dynamic-programming-memoization}

Hàm đệ quy của chúng ta hiện giải quyết Fibonacci trong thời gian cấp số mũ. Điều này có nghĩa là chúng ta chỉ có thể xử lý các giá trị đầu vào nhỏ trước khi bài toán trở nên quá khó khăn. Ví dụ, $f(29)$ dẫn đến *hơn 1 triệu* lệnh gọi hàm!

Để tăng tốc độ, chúng ta nhận ra rằng số lượng bài toán con chỉ là $O(n)$. Tức là, để tính $f(n)$, chúng ta chỉ cần biết $f(n-1),f(n-2), \dots ,f(0)$. Do đó, thay vì tính toán lại các bài toán con này, chúng ta giải chúng một lần và sau đó lưu kết quả vào bảng tra cứu. Các lệnh gọi tiếp theo sẽ sử dụng bảng tra cứu này và trả về kết quả ngay lập tức, do đó loại bỏ công việc theo cấp số mũ!

Mỗi lệnh gọi đệ quy sẽ kiểm tra bảng tra cứu xem giá trị đã được tính toán chưa. Điều này được thực hiện trong thời gian $O(1)$. Nếu chúng ta đã tính toán nó trước đó, hãy trả về kết quả, ngược lại, chúng ta tính toán hàm một cách bình thường. Thời gian chạy tổng thể là $O(n)$. Đây là một sự cải thiện to lớn so với thuật toán thời gian cấp số mũ trước đây của chúng ta!

```cpp
const int MAXN = 100;
bool found[MAXN];
int memo[MAXN];

int f(int n) {
    if (found[n]) return memo[n];
    if (n == 0) return 0;
    if (n == 1) return 1;

    found[n] = true;
    return memo[n] = f(n - 1) + f(n - 2);
}
```

Với hàm đệ quy đã được ghi nhớ mới của chúng ta, $f(29)$, vốn từng dẫn đến *hơn 1 triệu cuộc gọi*, giờ đây chỉ dẫn đến *57 cuộc gọi*, ít hơn gần *20.000 lần*! Trớ trêu thay, bây giờ chúng ta bị giới hạn bởi kiểu dữ liệu của chúng ta. $f(46)$ là số Fibonacci cuối cùng có thể vừa với một số nguyên 32 bit có dấu.

Thông thường, chúng ta cố gắng lưu các trạng thái trong mảng, nếu có thể, vì thời gian tra cứu là $O(1)$ với chi phí tối thiểu. Tuy nhiên, tổng quát hơn, chúng ta có thể lưu các trạng thái theo bất kỳ cách nào chúng ta muốn. Các ví dụ khác bao gồm cây tìm kiếm nhị phân (`map` trong C++) hoặc bảng băm (`unordered_map` trong C++).

Một ví dụ về điều này có thể là:

```cpp
unordered_map<int, int> memo;
int f(int n) {
    if (memo.count(n)) return memo[n];
    if (n == 0) return 0;
    if (n == 1) return 1;

    return memo[n] = f(n - 1) + f(n - 2);
}
```

Hoặc tương tự:

```cpp
map<int, int> memo;
int f(int n) {
    if (memo.count(n)) return memo[n];
    if (n == 0) return 0;
    if (n == 1) return 1;

    return memo[n] = f(n - 1) + f(n - 2);
}
```

Cả hai cách này hầu như sẽ luôn chậm hơn phiên bản dựa trên mảng đối với một hàm đệ quy được ghi nhớ chung.
Các cách lưu trạng thái thay thế này chủ yếu hữu ích khi lưu các vectơ hoặc chuỗi như một phần của không gian trạng thái.

Cách phân tích thời gian chạy của một hàm đệ quy được ghi nhớ là:

$$\text{công việc trên mỗi bài toán con} * \text{số lượng bài toán con}$$

Sử dụng cây tìm kiếm nhị phân (map trong C++) để lưu các trạng thái về mặt kỹ thuật sẽ dẫn đến $O(n \log n)$ vì mỗi lần tra cứu và chèn sẽ mất $O(\log n)$ công việc và với $O(n)$ bài toán con duy nhất, chúng ta có thời gian $O(n \log n)$.

Cách tiếp cận này được gọi là từ trên xuống (top-down), vì chúng ta có thể gọi hàm với một giá trị truy vấn và việc tính toán bắt đầu đi từ trên (giá trị được truy vấn) xuống dưới (các trường hợp cơ sở của đệ quy), và thực hiện các đường tắt thông qua ghi nhớ trên đường đi.

## Quy hoạch động từ dưới lên (Bottom-up Dynamic Programming) {: #bottom-up-dynamic-programming}

Cho đến nay, bạn chỉ mới thấy quy hoạch động từ trên xuống với ghi nhớ. Tuy nhiên, chúng ta cũng có thể giải quyết các bài toán bằng quy hoạch động từ dưới lên (bottom-up).
Bottom-up hoàn toàn đối lập với top-down, bạn bắt đầu từ dưới cùng (các trường hợp cơ sở của đệ quy), và mở rộng nó sang ngày càng nhiều giá trị.

Để tạo ra một cách tiếp cận từ dưới lên cho các số Fibonacci, chúng ta khởi tạo các trường hợp cơ sở trong một mảng. Sau đó, chúng ta chỉ cần sử dụng định nghĩa đệ quy trên mảng:

```cpp
const int MAXN = 100;
int fib[MAXN];

int f(int n) {
    fib[0] = 0;
    fib[1] = 1;
    for (int i = 2; i <= n; i++) fib[i] = fib[i - 1] + fib[i - 2];

    return fib[n];
}
```

Tất nhiên, như đã viết, điều này hơi ngớ ngẩn vì hai lý do:
Thứ nhất, chúng ta thực hiện công việc lặp lại nếu chúng ta gọi hàm nhiều hơn một lần.
Thứ hai, chúng ta chỉ cần sử dụng hai giá trị trước đó để tính toán phần tử hiện tại. Do đó, chúng ta có thể giảm bộ nhớ từ $O(n)$ xuống $O(1)$.

Một ví dụ về giải pháp quy hoạch động từ dưới lên cho Fibonacci sử dụng bộ nhớ $O(1)$ có thể là:

```cpp
const int MAX_SAVE = 3;
int fib[MAX_SAVE];

int f(int n) {
    fib[0] = 0;
    fib[1] = 1;
    for (int i = 2; i <= n; i++)
        fib[i % MAX_SAVE] = fib[(i - 1) % MAX_SAVE] + fib[(i - 2) % MAX_SAVE];

    return fib[n % MAX_SAVE];
}
```

Lưu ý rằng chúng ta đã thay đổi hằng số từ `MAXN` SANG `MAX_SAVE`. Điều này là do tổng số phần tử chúng ta cần truy cập chỉ là 3. Nó không còn tỷ lệ với kích thước đầu vào và theo định nghĩa là bộ nhớ $O(1)$. Ngoài ra, chúng ta sử dụng một thủ thuật phổ biến (sử dụng toán tử modulo) chỉ duy trì các giá trị mà chúng ta cần.

Đó là tất cả. Đó là những điều cơ bản của quy hoạch động: Đừng lặp lại công việc bạn đã làm trước đó.

Một trong những thủ thuật để làm tốt hơn về quy hoạch động là nghiên cứu một số ví dụ kinh điển.

## Các bài toán Quy hoạch động kinh điển (Classic Dynamic Programming Problems) {: #classic-dynamic-programming-problems}

| Tên | Mô tả/Ví dụ |
| :--- | :--- |
| [Cái túi 0-1 (0-1 Knapsack)](knapsack.md) | Cho $N$ vật phẩm với trọng lượng $w_i$ và giá trị $v_i$ và trọng lượng tối đa $W$, giá trị lớn nhất $\sum_{i=1}^{k} v_i$ cho mỗi tập con các vật phẩm có kích thước $k$ ($1 \le k \le N$) trong khi đảm bảo $\sum_{i=1}^{k} w_i \le W$ là bao nhiêu? |
| Tổng tập con (Subset Sum) | Cho $N$ số nguyên và $T$, xác định xem có tồn tại một tập con của tập hợp đã cho có tổng các phần tử bằng $T$ hay không. |
| [Dãy con tăng dài nhất (LIS)](longest-increasing-subsequence.md) | Bạn được cho một mảng chứa $N$ số nguyên. Nhiệm vụ của bạn là xác định LIS trong mảng, tức là một dãy con mà mỗi phần tử đều lớn hơn phần tử trước đó. |
| Đếm đường đi trong mảng 2D (Counting Paths in a 2D Array) | Cho $N$ và $M$, đếm tất cả các đường đi riêng biệt có thể từ $(1,1)$ đến $(N, M)$, trong đó mỗi bước là từ $(i,j)$ đến $(i+1,j)$ hoặc $(i,j+1)$. |
| Dãy con chung dài nhất (Longest Common Subsequence) | Bạn được cho các chuỗi $s$ và $t$. Tìm độ dài của chuỗi dài nhất là dãy con của cả $s$ và $t$. |
| Đường đi dài nhất trong đồ thị có hướng không chu trình (DAG) | Tìm đường đi dài nhất trong DAG. |
| Dãy con Palindrome dài nhất (Longest Palindromic Subsequence) | Tìm Dãy con Palindrome dài nhất (LPS) của một chuỗi nhất định. |
| Cắt thanh (Rod Cutting) | Cho một thanh có độ dài $n$ đơn vị, Cho một mảng số nguyên cuts trong đó cuts[i] biểu thị một vị trí bạn nên thực hiện cắt. Chi phí của một lần cắt là chiều dài của thanh cần cắt. Tổng chi phí cắt nhỏ nhất là bao nhiêu. |
| Khoảng cách chỉnh sửa (Edit Distance) | Khoảng cách chỉnh sửa giữa hai chuỗi là số lượng thao tác tối thiểu cần thiết để biến đổi chuỗi này thành chuỗi kia. Các thao tác là ["Thêm", "Xóa", "Thay thế"] |

## Các chủ đề liên quan (Related Topics) {: #related-topics}

*   [Quy hoạch động Bitmask (Bitmask Dynamic Programming)](profile-dynamics.md)
*   Quy hoạch động chữ số (Digit Dynamic Programming)
*   Quy hoạch động trên cây (Dynamic Programming on Trees)

Tất nhiên, thủ thuật quan trọng nhất là thực hành.

## Bài tập (Practice Problems) {: #practice-problems}

*   [LeetCode - 1137. N-th Tribonacci Number](https://leetcode.com/problems/n-th-tribonacci-number/description/)
*   [LeetCode - 118. Pascal's Triangle](https://leetcode.com/problems/pascals-triangle/description/)
*   [LeetCode - 1025. Divisor Game](https://leetcode.com/problems/divisor-game/description/)
*   [Codeforces - Vacations](https://codeforces.com/problemset/problem/699/C)
*   [Codeforces - Hard problem](https://codeforces.com/problemset/problem/706/C)
*   [Codeforces - Zuma](https://codeforces.com/problemset/problem/607/b)
*   [LeetCode - 221. Maximal Square](https://leetcode.com/problems/maximal-square/description/)
*   [LeetCode - 1039. Minimum Score Triangulation of Polygon](https://leetcode.com/problems/minimum-score-triangulation-of-polygon/description/)

## Các cuộc thi DP (DP Contests) {: #dp-contests}

*   [Atcoder - Educational DP Contest](https://atcoder.jp/contests/dp/tasks)
*   [CSES - Dynamic Programming](https://cses.fi/problemset/list/)
