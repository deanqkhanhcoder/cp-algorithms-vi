---
tags:
  - Original
---

# Giới thiệu về Quy hoạch động

Bản chất của quy hoạch động là tránh việc tính toán lặp lại. Thường thì các bài toán quy hoạch động có thể được giải một cách tự nhiên bằng đệ quy. Trong những trường hợp như vậy, dễ nhất là viết lời giải đệ quy rồi lưu các trạng thái bị lặp lại vào một bảng tra cứu. Quá trình này được gọi là quy hoạch động theo hướng từ trên xuống (top-down) với kỹ thuật *memoization*. Lưu ý đọc là "memoization" (như viết vào sổ ghi chú), không phải "memorization" (ghi nhớ).

Một trong những ví dụ cơ bản và kinh điển của quá trình này là dãy Fibonacci. Biểu thức đệ quy của nó là $f(n) = f(n-1) + f(n-2)$ với $n \ge 2$ và $f(0)=0$, $f(1)=1$. Trong C++, điều này được biểu diễn như sau:

```cpp
int f(int n) {
    if (n == 0) return 0;
    if (n == 1) return 1;
    return f(n - 1) + f(n - 2);
}
```

Độ phức tạp thời gian của hàm đệ quy này là cấp số nhân - xấp xỉ $O(2^n)$ vì một lời gọi hàm ($f(n)$) dẫn tới 2 lời gọi hàm tương tự có kích thước nhỏ hơn ($f(n-1)$ và $f(n-2)$).

## Tăng tốc Fibonacci bằng Quy hoạch động (Memoization)

Hàm đệ quy hiện tại giải Fibonacci theo thời gian cấp số nhân. Điều này có nghĩa là chúng ta chỉ xử lý được các giá trị đầu vào nhỏ trước khi bài toán trở nên quá khó. Ví dụ, $f(29)$ dẫn đến *hơn 1 triệu* lời gọi hàm!

Để tăng tốc, ta nhận ra rằng số lượng bài toán con chỉ là $O(n)$. Tức là, để tính $f(n)$ ta chỉ cần biết $f(n-1), f(n-2), \dots, f(0)$. Do đó, thay vì tính lại các bài toán con này nhiều lần, ta giải chúng một lần rồi lưu kết quả vào bảng tra cứu. Các lời gọi sau đó sẽ sử dụng bảng tra cứu này và trả về kết quả ngay lập tức, từ đó loại bỏ công việc cấp số nhân!

Mỗi lời gọi đệ quy sẽ kiểm tra bảng tra cứu xem giá trị đã được tính hay chưa. Việc này thực hiện trong $O(1)$ thời gian. Nếu trước đó ta đã tính, trả về kết quả; ngược lại, ta tính như bình thường. Tổng thời gian chạy là $O(n)$. Đây là một cải thiện rất lớn so với thuật toán cấp số nhân trước đó!

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

Với hàm đệ quy có memo hóa này, $f(29)$, vốn trước đây dẫn đến *hơn 1 triệu lời gọi*, giờ chỉ dẫn đến *chỉ 57* lời gọi, gần như *ít hơn 20.000 lần*! Trớ trêu thay, giờ ta bị giới hạn bởi kiểu dữ liệu. $f(46)$ là số Fibonacci cuối cùng có thể vừa trong một số nguyên 32-bit có dấu.

Thông thường, ta cố gắng lưu trạng thái trong mảng nếu có thể, vì thời gian tra cứu là $O(1)$ với chi phí thấp. Tuy nhiên, nói chung, ta có thể lưu trạng thái theo nhiều cách khác nhau. Ví dụ khác bao gồm cây tìm kiếm nhị phân (`map` trong C++) hoặc bảng băm (`unordered_map` trong C++).

Một ví dụ như sau:

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

Cả hai cách này hầu như luôn chậm hơn phiên bản dùng mảng cho các hàm đệ quy có memo hóa chung. Những cách lưu trạng thái này hữu ích khi ta cần lưu vector hoặc chuỗi như một phần của không gian trạng thái.

Cách hiểu đơn giản để phân tích thời gian chạy của hàm đệ quy có memo là:

$$\text{công việc trên mỗi bài toán con} * \text{số lượng bài toán con}$$

Việc sử dụng cây tìm kiếm nhị phân (map trong C++) để lưu trạng thái về mặt kỹ thuật sẽ dẫn đến $O(n \log n)$ vì mỗi thao tác tra cứu và chèn tốn $O(\log n)$ và với $O(n)$ bài toán con duy nhất ta có $O(n \log n)$ thời gian.

Cách tiếp cận này gọi là từ trên xuống (top-down), vì ta có thể gọi hàm với một giá trị truy vấn và quá trình tính toán bắt đầu từ trên (giá trị truy vấn) đi xuống dưới (các trường hợp cơ sở của đệ quy), đồng thời rút ngắn nhờ memoization trên đường đi.

## Quy hoạch động từ dưới lên (Bottom-up)

Cho đến giờ bạn chỉ thấy quy hoạch động từ trên xuống với memoization. Tuy nhiên, ta cũng có thể giải bài toán bằng quy hoạch động từ dưới lên.
Bottom-up hoàn toàn ngược lại với top-down: bắt đầu từ dưới (các trường hợp cơ sở của đệ quy), rồi mở rộng tới các giá trị lớn hơn.

Để tạo phương pháp bottom-up cho số Fibonacci, ta khởi tạo các trường hợp cơ sở trong một mảng. Sau đó, ta đơn giản áp dụng công thức đệ quy lên mảng:

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

Tất nhiên, như đã viết, đoạn mã trên hơi lãng phí vì hai lý do:
Thứ nhất, ta làm việc lặp lại nếu gọi hàm nhiều hơn một lần.
Thứ hai, ta chỉ cần hai giá trị trước đó để tính phần tử hiện tại. Do đó, ta có thể giảm bộ nhớ từ $O(n)$ xuống $O(1)$.

Một ví dụ của lời giải bottom-up cho Fibonacci sử dụng bộ nhớ $O(1)$ có thể như sau:

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

Lưu ý rằng ta đã đổi hằng từ `MAXN` sang `MAX_SAVE`. Lý do là tổng số phần tử cần truy cập chỉ là 3. Nó không còn tỉ lệ theo kích thước đầu vào nữa và theo định nghĩa là bộ nhớ $O(1)$. Thêm vào đó, ta sử dụng mẹo phổ biến (dùng toán tử modulo) để chỉ giữ các giá trị cần thiết.

Đó là cơ bản của quy hoạch động: đừng lặp lại công việc bạn đã làm trước đó.

Một trong những mẹo để tiến bộ về quy hoạch động là học các ví dụ kinh điển.

## Các bài toán Quy hoạch động kinh điển
| Tên                                            | Mô tả / Ví dụ                                                                                                                                                                                                                  |
| ---------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Balo 0-1 (0-1 Knapsack)](../dynamic_programming/knapsack.md)                                   | Cho $N$ vật với trọng lượng $w_i$ và giá trị $v_i$ và trọng lượng tối đa $W$, giá trị tối đa $\sum_{i=1}^{k} v_i$ cho mỗi tập con gồm $k$ vật ($1 \le k \le N$) sao cho $\sum_{i=1}^{k} w_i \le W$ là bao nhiêu?                  |
| Subset Sum (Tổng con)                          | Cho $N$ số nguyên và $T$, xác định xem có tồn tại một tập con của các phần tử đã cho mà tổng bằng $T$ hay không.                                                                                                         |
| [Dãy con tăng dài nhất (LIS)](../dynamic_programming/longest_increasing_subsequence.md)           | Cho một mảng gồm $N$ số nguyên. Nhiệm vụ của bạn là tìm dãy con tăng dài nhất (LIS) trong mảng, tức là một dãy con mà mỗi phần tử lớn hơn phần tử trước nó.                                                       |
| Đếm đường đi trong mảng 2D                      | Cho $N$ và $M$, đếm tất cả các đường đi phân biệt từ $(1,1)$ đến $(N, M)$, trong đó mỗi bước là từ $(i,j)$ đến $(i+1,j)$ hoặc $(i,j+1)$.                                                                               |
| Dãy con chung dài nhất                          | Cho hai chuỗi $s$ và $t$. Tìm độ dài của chuỗi dài nhất là dãy con chung của cả $s$ và $t$.                                                                                                            |
| Đường đi dài nhất trong DAG                     | Tìm đường đi dài nhất trong đồ thị có hướng acyclic (DAG).                                                                                                                                                                      |
| Dãy con đối xứng dài nhất (LPS)                 | Tìm dãy con đối xứng dài nhất (LPS) của một chuỗi cho trước.                                                                                                                                                           |
| Bài toán cắt thanh                              | Cho một thanh có độ dài $n$, và một mảng số nguyên `cuts` trong đó `cuts[i]` là vị trí cần cắt. Chi phí cho mỗi lần cắt là độ dài của đoạn thanh bị cắt. Hỏi chi phí tối thiểu để thực hiện các lần cắt là bao nhiêu. |
| Khoảng cách chỉnh sửa (Edit Distance)          | Khoảng cách chỉnh sửa giữa hai chuỗi là số thao tác tối thiểu cần để biến chuỗi này thành chuỗi kia. Các thao tác là ["Add", "Remove", "Replace"]                                                         |

## Các chủ đề liên quan
* [Quy hoạch động bằng bitmask](../dynamic_programming/profile-dynamics.md)
* Quy hoạch động theo chữ số
* Quy hoạch động trên cây

Tất nhiên, mẹo quan trọng nhất là luyện tập.

## Bài tập thực hành
* [LeetCode - 1137. N-th Tribonacci Number](https://leetcode.com/problems/n-th-tribonacci-number/description/)
* [LeetCode - 118. Pascal's Triangle](https://leetcode.com/problems/pascals-triangle/description/)
* [LeetCode - 1025. Divisor Game](https://leetcode.com/problems/divisor-game/description/)
* [Codeforces - Vacations](https://codeforces.com/problemset/problem/699/C)
* [Codeforces - Hard problem](https://codeforces.com/problemset/problem/706/C)
* [Codeforces - Zuma](https://codeforces.com/problemset/problem/607/b)
* [LeetCode - 221. Maximal Square](https://leetcode.com/problems/maximal-square/description/)
* [LeetCode - 1039. Minimum Score Triangulation of Polygon](https://leetcode.com/problems/minimum-score-triangulation-of-polygon/description/)

## Các cuộc thi DP
* [Atcoder - Educational DP Contest](https://atcoder.jp/contests/dp/tasks)
* [CSES - Dynamic Programming](https://cses.fi/problemset/list/)

