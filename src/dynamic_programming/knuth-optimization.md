---
tags:
  - Translated
---

# Tối ưu hóa Knuth (Knuth's Optimization) {: #knuths-optimization}

Tối ưu hóa Knuth (Knuth's Optimization), còn được gọi là Tăng tốc Knuth-Yao (Knuth-Yao Speedup), là một trường hợp đặc biệt của quy hoạch động trên các khoảng, có thể tối ưu hóa độ phức tạp thời gian của các giải pháp bằng một hệ số tuyến tính, từ $O(n^3)$ đối với DP khoảng thông thường xuống $O(n^2)$.

## Các điều kiện (Conditions) {: #conditions}

Tăng tốc được áp dụng cho các chuyển đổi có dạng

$$dp(i, j) = \min_{i \leq k < j} [ dp(i, k) + dp(k+1, j) + C(i, j) ].$$

Tương tự như [DP chia để trị](divide-and-conquer-dp.md), gọi $opt(i, j)$ là giá trị $k$ tối đa giúp giảm thiểu biểu thức trong quá trình chuyển đổi ($opt$ được gọi là "điểm chia tối ưu" trong nửa sau bài viết này). Việc tối ưu hóa yêu cầu điều sau đây phải được thỏa mãn:

$$opt(i, j-1) \leq opt(i, j) \leq opt(i+1, j).$$

Chúng ta có thể chỉ ra rằng nó đúng khi hàm chi phí $C$ thỏa mãn các điều kiện sau với $a \leq b \leq c \leq d$:

1. $C(b, c) \leq C(a, d)$;

2. $C(a, c) + C(b, d) \leq C(a, d) + C(b, c)$ (bất đẳng thức tứ giác [QI]).

Kết quả này được chứng minh thêm ở bên dưới.

## Thuật toán (Algorithm) {: #algorithm}

Hãy xử lý các trạng thái dp theo cách mà chúng ta tính $dp(i, j-1)$ và $dp(i+1, j)$ trước $dp(i, j)$, và khi làm như vậy chúng ta cũng tính $opt(i, j-1)$ và $opt(i+1, j)$. Khi đó để tính $opt(i, j)$, thay vì kiểm tra các giá trị của $k$ từ $i$ đến $j-1$, chúng ta chỉ cần kiểm tra từ $opt(i, j-1)$ đến $opt(i+1, j)$. Để xử lý các cặp $(i,j)$ theo thứ tự này, chỉ cần sử dụng các vòng lặp for lồng nhau trong đó $i$ đi từ giá trị lớn nhất đến giá trị nhỏ nhất và $j$ đi từ $i+1$ đến giá trị lớn nhất.

### Cài đặt chung (Generic implementation) {: #generic-implementation}

Mặc dù việc cài đặt thay đổi, đây là một ví dụ khá chung. Cấu trúc của mã gần giống với DP Khoảng (Range DP).
```cpp title="knuth_optimization"

int solve() {
    int N;
    ... // read N and input
    int dp[N][N], opt[N][N];

    auto C = [&](int i, int j) {
        ... // Implement cost function C.
    };

    for (int i = 0; i < N; i++) {
        opt[i][i] = i;
        ... // Initialize dp[i][i] according to the problem
    }

    for (int i = N-2; i >= 0; i--) {
        for (int j = i+1; j < N; j++) {
            int mn = INT_MAX;
            int cost = C(i, j);
            for (int k = opt[i][j-1]; k <= min(j-1, opt[i+1][j]); k++) {
                if (mn >= dp[i][k] + dp[k+1][j] + cost) {
                    opt[i][j] = k; 
                    mn = dp[i][k] + dp[k+1][j] + cost; 
                }
            }
            dp[i][j] = mn; 
        }
    }

    return dp[0][N-1];
}
```

### Độ phức tạp (Complexity) {: #complexity}

Độ phức tạp của thuật toán có thể được ước tính bằng tổng sau:

$$
\sum\limits_{i=1}^N \sum\limits_{j=i+1}^N [opt(i+1,j)-opt(i,j-1)] =
\sum\limits_{i=1}^N \sum\limits_{j=i}^{N-1} [opt(i+1,j+1)-opt(i,j)].
$$

Như bạn thấy, hầu hết các số hạng trong biểu thức này triệt tiêu lẫn nhau, ngoại trừ các số hạng dương với $j=N-1$ và các số hạng âm với $i=1$. Do đó, toàn bộ tổng có thể được ước tính là

$$
\sum\limits_{k=1}^N[opt(k,N)-opt(1,k)] = O(n^2),
$$

thay vì $O(n^3)$ nếu chúng ta sử dụng DP khoảng thông thường.

### Về thực hành (On practice) {: #on-practice}

Ứng dụng phổ biến nhất của Tối ưu hóa Knuth là trong Range DP, với chuyển đổi đã cho. Khó khăn duy nhất là chứng minh rằng hàm chi phí thỏa mãn các điều kiện đã cho. Trường hợp đơn giản nhất là khi hàm chi phí $C(i, j)$ chỉ đơn giản là tổng các phần tử của mảng con $S[i, i+1, ..., j]$ cho một mảng nào đó (tùy thuộc vào câu hỏi). Tuy nhiên, đôi khi chúng có thể phức tạp hơn.

Lưu ý rằng hơn các điều kiện về chuyển đổi dp và hàm chi phí, chìa khóa cho sự tối ưu hóa này là bất đẳng thức trên điểm chia tối ưu. Trong một số bài toán, chẳng hạn như bài toán cây tìm kiếm nhị phân tối ưu (tình cờ là bài toán gốc mà tối ưu hóa này được phát triển), các chuyển đổi và hàm chi phí sẽ ít rõ ràng hơn, tuy nhiên, người ta vẫn có thể chứng minh rằng $opt(i, j-1) \leq opt(i, j) \leq opt(i+1, j)$, và do đó, sử dụng tối ưu hóa này.

### Chứng minh tính đúng đắn (Proof of correctness) {: #proof-of-correctness}

Để chứng minh tính đúng đắn của thuật toán này dưới các điều kiện của $C(i,j)$, đủ để chứng minh rằng

$$
opt(i, j-1) \leq opt(i, j) \leq opt(i+1, j)
$$

giả sử các điều kiện đã cho được thỏa mãn.

!!! lemma "Bổ đề"
    $dp(i, j)$ cũng thỏa mãn bất đẳng thức tứ giác, với điều kiện các điều kiện của bài toán được thỏa mãn.

??? hint "Chứng minh"
    Chứng minh cho bổ đề này sử dụng quy nạp mạnh. Nó được lấy từ bài báo <a href="https://dl.acm.org/doi/pdf/10.1145/800141.804691">Efficient Dynamic Programming Using Quadrangle Inequalities</a>, được viết bởi F. Frances Yao, người đã giới thiệu Tăng tốc Knuth-Yao (mệnh đề cụ thể này là Bổ đề 2.1 trong bài báo). Ý tưởng là quy nạp dựa trên độ dài $l = d - a$. Trường hợp $l = 1$ là tầm thường. Đối với $l > 1$ xem xét 2 trường hợp:

    1. $b = c$
    Bất đẳng thức rút gọn thành $dp(a, b) + dp(b, d) \leq dp(a, d)$ (Điều này giả sử rằng $dp(i, i) = 0$ cho mọi $i$, đây là trường hợp cho tất cả các bài toán sử dụng tối ưu hóa này). Gọi $opt(a,d) = z$.

        - Nếu $z < j$,
        Lưu ý rằng
        
            $$
            dp(a, b) \leq dp_{z}(a, b) = dp(a, z) + dp(z+1, b) + C(a, b).
            $$
            
            Do đó,
            
            $$
            dp(a, b) + dp(b, d) \leq dp(a, z) + dp(z+1, b) + dp(b, d) + C(a, b)
            $$

            Từ giả thuyết quy nạp, $dp(z+1, b) + dp(b, d) \leq dp(z+1, d)$. Ngoài ra, nó được cho là $C(a, b) \leq C(a, d)$. Kết hợp 2 thực tế này với bất đẳng thức trên mang lại kết quả mong muốn.

        - Nếu $z \geq j$, bằng chứng của trường hợp này đối xứng với trường hợp trước.

    2. $b < c$
    Gọi $opt(b, c) = z$ và $opt(a, d) = y$.
        
        - Nếu $z \leq y$,
        
            $$
            dp(a, c) + dp(b, d) \leq dp_{z}(a, c) + dp_{y}(b, d)
            $$

            trong đó

            $$
            dp_{z}(a, c) + dp_{y}(b, d) = C(a, c) + C(b, d) + dp(a, z) + dp(z+1, c) + dp(b, y) + dp(y+1, d).
            $$

            Sử dụng QI trên $C$ và trên trạng thái dp cho các chỉ số $z+1 \leq y+1 \leq c \leq d$ (từ giả thuyết quy nạp) mang lại kết quả mong muốn.
        
        - Nếu $z > y$, bằng chứng của trường hợp này đối xứng với trường hợp trước.

    Điều này hoàn thành việc chứng minh bổ đề.

Bây giờ, xem xét thiết lập sau. Chúng ta có 2 chỉ số $i \leq p \leq q < j$. Đặt $dp_{k} = C(i, j) + dp(i, k) + dp(k+1, j)$.

Giả sử chúng ta chỉ ra rằng

$$
dp_{p}(i, j-1) \geq dp_{q}(i, j-1) \implies dp_{p}(i, j) \geq dp_{q}(i, j).
$$

Đặt $q = opt(i, j-1)$, theo định nghĩa, $dp_{p}(i, j-1) \geq dp_{q}(i, j-1)$. Do đó, áp dụng bất đẳng thức cho tất cả $i \leq p \leq q$, chúng ta có thể suy ra rằng $opt(i, j)$ ít nhất bằng $opt(i, j-1)$, chứng minh nửa đầu của bất đẳng thức.

Bây giờ, sử dụng QI trên một số chỉ số $p+1 \leq q+1 \leq j-1 \leq j$, chúng ta nhận được

$$\begin{align}
&dp(p+1, j-1) + dp(q+1, j) ≤ dp(q+1, j-1) + dp(p+1, j) \\
\implies& (dp(i, p) + dp(p+1, j-1) + C(i, j-1)) + (dp(i, q) + dp(q+1, j) + C(i, j)) \\  
\leq& (dp(i, q) + dp(q+1, j-1) + C(i, j-1)) + (dp(i, p) + dp(p+1, j) + C(i, j)) \\  
\implies& dp_{p}(i, j-1) + dp_{q}(i, j) ≤ dp_{p}(i, j) + dp_{q}(i, j-1) \\
\implies& dp_{p}(i, j-1) - dp_{q}(i, j-1) ≤ dp_{p}(i, j) - dp_{q}(i, j) \\
\end{align}$$

Cuối cùng,

$$\begin{align}
&dp_{p}(i, j-1) \geq dp_{q}(i, j-1) \\
&\implies 0 \leq dp_{p}(i, j-1) - dp_{q}(i, j-1) \leq dp_{p}(i, j) - dp_{q}(i, j) \\
&\implies dp_{p}(i, j) \geq dp_{q}(i, j)
\end{align}$$

Điều này chứng minh phần đầu tiên của bất đẳng thức, tức là, $opt(i, j-1) \leq opt(i, j)$. Phần thứ hai $opt(i, j) \leq opt(i+1, j)$ có thể được chỉ ra với cùng ý tưởng, bắt đầu với bất đẳng thức
$dp(i, p) + dp(i+1, q) ≤ dp(i+1, p) + dp(i, q)$.

Điều này hoàn thành việc chứng minh.

## Bài tập (Practice Problems) {: #practice-problems}

- [UVA - Cutting Sticks](https://onlinejudge.org/external/100/10003.pdf)
- [UVA - Prefix Codes](https://onlinejudge.org/external/120/12057.pdf)
- [SPOJ - Breaking String](https://www.spoj.com/problems/BRKSTRNG/)
- [UVA - Optimal Binary Search Tree](https://onlinejudge.org/external/103/10304.pdf)

## Tài liệu tham khảo (References) {: #references}

- [Geeksforgeeks Article](https://www.geeksforgeeks.org/knuths-optimization-in-dynamic-programming/)
- [Doc on DP Speedups](https://home.cse.ust.hk/~golin/COMP572/Notes/DP_speedup.pdf)
- [Efficient Dynamic Programming Using Quadrangle Inequalities](https://dl.acm.org/doi/pdf/10.1145/800141.804691)
