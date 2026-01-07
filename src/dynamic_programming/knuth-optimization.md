---
tags:
  - Original
---

# Tối ưu hóa Knuth

Tối ưu hóa Knuth, còn được gọi là Tăng tốc Knuth-Yao, là một trường hợp đặc biệt của quy hoạch động trên đoạn, có thể tối ưu hóa độ phức tạp thời gian của các giải pháp theo một hệ số tuyến tính, từ $O(n^3)$ đối với DP đoạn tiêu chuẩn xuống $O(n^2)$.

## Các điều kiện

Kỹ thuật tăng tốc này được áp dụng cho các bước chuyển trạng thái có dạng

$$dp(i, j) = \min_{i \leq k < j} [ dp(i, k) + dp(k+1, j) + C(i, j) ].$$

Tương tự như [quy hoạch động chia để trị](./divide-and-conquer-dp.md), gọi $opt(i, j)$ là giá trị lớn nhất của $k$ để tối thiểu hóa biểu thức trong công thức chuyển ($opt$ được gọi là "điểm chia tối ưu" trong phần tiếp theo của bài viết này). Việc tối ưu hóa yêu cầu điều kiện sau phải thỏa mãn:

$$opt(i, j-1) \leq opt(i, j) \leq opt(i+1, j).$$

Chúng ta có thể chỉ ra rằng điều này đúng khi hàm chi phí $C$ thỏa mãn các điều kiện sau với $a \leq b \leq c \leq d$:

1. $C(b, c) \leq C(a, d)$;

2. $C(a, c) + C(b, d) \leq C(a, d) + C(b, c)$ (bất đẳng thức tứ giác [QI]).

Kết quả này được chứng minh ở phần dưới.

## Thuật toán

Hãy xử lý các trạng thái DP theo cách sao cho chúng ta tính $dp(i, j-1)$ và $dp(i+1, j)$ trước $dp(i, j)$, và trong khi làm vậy, chúng ta cũng tính $opt(i, j-1)$ và $opt(i+1, j)$. Khi đó, để tính $opt(i, j)$, thay vì thử các giá trị của $k$ từ $i$ đến $j-1$, chúng ta chỉ cần thử từ $opt(i, j-1)$ đến $opt(i+1, j)$. Để xử lý các cặp $(i,j)$ theo thứ tự này, chỉ cần sử dụng các vòng lặp for lồng nhau, trong đó $i$ chạy từ giá trị lớn nhất về giá trị nhỏ nhất và $j$ chạy từ $i+1$ đến giá trị lớn nhất.

### Cài đặt tổng quát

Mặc dù cách cài đặt có thể khác nhau, dưới đây là một ví dụ khá tổng quát. Cấu trúc mã nguồn gần như giống hệt với Quy hoạch động đoạn (Range DP).

```{.cpp file=knuth_optimization}

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

### Độ phức tạp

Độ phức tạp của thuật toán có thể được ước tính bằng tổng sau:

$$
\sum\limits_{i=1}^N \sum\limits_{j=i+1}^N [opt(i+1,j)-opt(i,j-1)] =
\sum\limits_{i=1}^N \sum\limits_{j=i}^{N-1} [opt(i+1,j+1)-opt(i,j)].
$$

Như bạn thấy, hầu hết các số hạng trong biểu thức này triệt tiêu lẫn nhau, ngoại trừ các số hạng dương với $j=N-1$ và các số hạng âm với $i=1$. Do đó, toàn bộ tổng có thể được ước tính là

$$
\sum\limits_{k=1}^N[opt(k,N)-opt(1,k)] = O(n^2),
$$

thay vì $O(n^3)$ như khi sử dụng quy hoạch động đoạn thông thường.

### Trong thực tế

Ứng dụng phổ biến nhất của tối ưu hóa Knuth là trong Quy hoạch động đoạn, với công thức chuyển trạng thái đã cho. Khó khăn duy nhất là chứng minh hàm chi phí thỏa mãn các điều kiện đã cho. Trường hợp đơn giản nhất là khi hàm chi phí $C(i, j)$ chỉ đơn giản là tổng các phần tử của mảng con $S[i, i+1, ..., j]$ của một mảng nào đó (tùy thuộc vào đề bài). Tuy nhiên, đôi khi chúng có thể phức tạp hơn.

Lưu ý rằng quan trọng hơn các điều kiện về công thức chuyển DP và hàm chi phí, chìa khóa của sự tối ưu hóa này là bất đẳng thức về điểm chia tối ưu. Trong một số bài toán, chẳng hạn như bài toán cây tìm kiếm nhị phân tối ưu (tình cờ thay, đây chính là bài toán gốc mà từ đó tối ưu hóa này được phát triển), các bước chuyển và hàm chi phí sẽ ít rõ ràng hơn, tuy nhiên, ta vẫn có thể chứng minh rằng $opt(i, j-1) \leq opt(i, j) \leq opt(i+1, j)$, và do đó, sử dụng được tối ưu hóa này.


### Chứng minh tính đúng đắn

Để chứng minh tính đúng đắn của thuật toán này xét theo các điều kiện của $C(i,j)$, ta chỉ cần chứng minh rằng

$$
opt(i, j-1) \leq opt(i, j) \leq opt(i+1, j)
$$

với giả định các điều kiện đã cho được thỏa mãn.

!!! lemma "Bổ đề"
    $dp(i, j)$ cũng thỏa mãn bất đẳng thức tứ giác, với điều kiện các yêu cầu của bài toán được thỏa mãn.

??? hint "Chứng minh"
    Chứng minh cho bổ đề này sử dụng quy nạp mạnh. Nó được lấy từ bài báo <a href="https://dl.acm.org/doi/pdf/10.1145/800141.804691">Efficient Dynamic Programming Using Quadrangle Inequalities</a>, tác giả F. Frances Yao, người đã giới thiệu Tăng tốc Knuth-Yao (phát biểu cụ thể này là Bổ đề 2.1 trong bài báo). Ý tưởng là quy nạp theo độ dài $l = d - a$. Trường hợp $l = 1$ là hiển nhiên. Với $l > 1$ xét 2 trường hợp:

    1. $b = c$  
    Bất đẳng thức rút gọn thành $dp(a, b) + dp(b, d) \leq dp(a, d)$ (Điều này giả định rằng $dp(i, i) = 0$ với mọi $i$, đây là trường hợp đúng cho mọi bài toán sử dụng tối ưu hóa này). Gọi $opt(a,d) = z$.

        - Nếu $z < j$,  
        Lưu ý rằng
        
            $$
            dp(a, b) \leq dp_{z}(a, b) = dp(a, z) + dp(z+1, b) + C(a, b).
            $$
            
            Do đó,  
            
            $$
            dp(a, b) + dp(b, d) \leq dp(a, z) + dp(z+1, b) + dp(b, d) + C(a, b)
            $$

            Từ giả thiết quy nạp, $dp(z+1, b) + dp(b, d) \leq dp(z+1, d)$. Ngoài ra, giả thiết đã cho $C(a, b) \leq C(a, d)$. Kết hợp 2 thực tế này với bất đẳng thức trên sẽ thu được kết quả mong muốn.

        - Nếu $z \geq j$, chứng minh cho trường hợp này đối xứng với trường hợp trước.

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

            Sử dụng bất đẳng thức tứ giác (QI) trên $C$ và trên trạng thái DP cho các chỉ số $z+1 \leq y+1 \leq c \leq d$ (từ giả thiết quy nạp) sẽ thu được kết quả mong muốn.
        
        - Nếu $z > y$, chứng minh cho trường hợp này đối xứng với trường hợp trước.

    Điều này hoàn tất việc chứng minh bổ đề.

Bây giờ, hãy xem xét thiết lập sau. Ta có 2 chỉ số $i \leq p \leq q < j$. Đặt $dp_{k} = C(i, j) + dp(i, k) + dp(k+1, j)$.

Giả sử ta chỉ ra được rằng

$$
dp_{p}(i, j-1) \geq dp_{q}(i, j-1) \implies dp_{p}(i, j) \geq dp_{q}(i, j).
$$

Đặt $q = opt(i, j-1)$, theo định nghĩa, $dp_{p}(i, j-1) \geq dp_{q}(i, j-1)$. Do đó, áp dụng bất đẳng thức cho mọi $i \leq p \leq q$, ta có thể suy ra rằng $opt(i, j)$ ít nhất cũng lớn bằng $opt(i, j-1)$, chứng minh được nửa đầu của bất đẳng thức.

Bây giờ, sử dụng QI trên các chỉ số $p+1 \leq q+1 \leq j-1 \leq j$, ta có

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

Điều này chứng minh phần đầu tiên của bất đẳng thức, tức là $opt(i, j-1) \leq opt(i, j)$. Phần thứ hai $opt(i, j) \leq opt(i+1, j)$ có thể được chỉ ra với cùng ý tưởng, bắt đầu từ bất đẳng thức 
$dp(i, p) + dp(i+1, q) ≤ dp(i+1, p) + dp(i, q)$.

Điều này hoàn tất chứng minh.

## Bài tập thực hành
- [UVA - Cutting Sticks](https://onlinejudge.org/external/100/10003.pdf)
- [UVA - Prefix Codes](https://onlinejudge.org/external/120/12057.pdf)
- [SPOJ - Breaking String](https://www.spoj.com/problems/BRKSTRNG/)
- [UVA - Optimal Binary Search Tree](https://onlinejudge.org/external/103/10304.pdf)


## Tài liệu tham khảo
- [Bài viết trên Geeksforgeeks](https://www.geeksforgeeks.org/knuths-optimization-in-dynamic-programming/)
- [Tài liệu về các kỹ thuật tăng tốc DP](https://home.cse.ust.hk/~golin/COMP572/Notes/DP_speedup.pdf)
- [Efficient Dynamic Programming Using Quadrangle Inequalities](https://dl.acm.org/doi/pdf/10.1145/800141.804691)
