---
tags:
  - Translated
e_maxx_link: bishops_arrangement
---

# Đặt các quân tượng trên bàn cờ (Placing Bishops on a Chessboard) {: #placing-bishops-on-a-chessboard}

Tìm số cách đặt $K$ quân tượng trên bàn cờ $N \times N$ sao cho không có hai quân tượng nào tấn công lẫn nhau.

## Thuật toán (Algorithm) {: #algorithm}

Bài toán này có thể được giải bằng quy hoạch động.

Hãy liệt kê các đường chéo của bàn cờ như sau: các đường chéo đen có chỉ số lẻ, các đường chéo trắng có chỉ số chẵn, và các đường chéo được đánh số theo thứ tự không giảm của số lượng ô vuông trong chúng. Đây là một ví dụ cho bàn cờ $5 \times 5$.

$$\begin{matrix}
\bf{1} & 2 & \bf{5} & 6 & \bf{9} \\\
2 & \bf{5} & 6 & \bf{9} & 8 \\\
\bf{5} & 6 & \bf{9} & 8 & \bf{7} \\\
6 & \bf{9} & 8 & \bf{7} & 4 \\\
\bf{9} & 8 & \bf{7} & 4 & \bf{3} \\\
\end{matrix}$$

Gọi `D[i][j]` biểu thị số cách đặt `j` quân tượng trên các đường chéo có chỉ số lên đến `i` có cùng màu với đường chéo `i`.
Khi đó `i = 1...2N-1` và `j = 0...K`.

Chúng ta có thể tính `D[i][j]` chỉ bằng cách sử dụng các giá trị của `D[i-2]` (chúng ta trừ 2 vì chúng ta chỉ xem xét các đường chéo cùng màu với $i$).
Có hai cách để có được `D[i][j]`.
Hoặc chúng ta đặt tất cả `j` quân tượng trên các đường chéo trước đó: khi đó có `D[i-2][j]` cách để đạt được điều này.
Hoặc chúng ta đặt một quân tượng trên đường chéo `i` và `j-1` quân tượng trên các đường chéo trước đó.
Số cách để làm điều này bằng số lượng ô trên đường chéo `i` trừ đi `j-1`, vì mỗi `j-1` quân tượng được đặt trên các đường chéo trước đó sẽ chặn một ô trên đường chéo hiện tại.
Số lượng ô trên đường chéo `i` có thể được tính như sau:

```cpp
int squares (int i) {
    if (i & 1)
        return i / 4 * 2 + 1;
    else
        return (i - 1) / 4 * 2 + 2;
}
```

Trường hợp cơ sở rất đơn giản: `D[i][0] = 1`, `D[1][1] = 1`.

Một khi chúng ta đã tính tất cả các giá trị của `D[i][j]`, câu trả lời có thể thu được như sau:
xem xét tất cả các số lượng quân tượng có thể được đặt trên các đường chéo đen `i=0...K`, với số lượng quân tượng tương ứng trên các đường chéo trắng `K-i`.
Các quân tượng được đặt trên các đường chéo đen và trắng không bao giờ tấn công lẫn nhau, vì vậy việc đặt có thể được thực hiện độc lập.
Chỉ số của đường chéo đen cuối cùng là `2N-1`, chỉ số của đường chéo trắng cuối cùng là `2N-2`.
Đối với mỗi `i` chúng ta thêm `D[2N-1][i] * D[2N-2][K-i]` vào câu trả lời.

## Cài đặt (Implementation) {: #implementation}

```cpp
int bishop_placements(int N, int K)
{
    if (K > 2 * N - 1)
        return 0;

    vector<vector<int>> D(N * 2, vector<int>(K + 1));
    for (int i = 0; i < N * 2; ++i)
        D[i][0] = 1;
    D[1][1] = 1;
    for (int i = 2; i < N * 2; ++i)
        for (int j = 1; j <= K; ++j)
            D[i][j] = D[i-2][j] + D[i-2][j-1] * (squares(i) - j + 1);

    int ans = 0;
    for (int i = 0; i <= K; ++i)
        ans += D[N*2-1][i] * D[N*2-2][K-i];
    return ans;
}
```
