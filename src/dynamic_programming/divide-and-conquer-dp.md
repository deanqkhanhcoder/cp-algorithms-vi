---
tags:
  - Original
---

# Quy hoạch động Chia để trị

Chia để trị là một phương pháp tối ưu hóa quy hoạch động.

### Điều kiện tiên quyết
Một số bài toán quy hoạch động có công thức truy hồi dạng sau:

$$
dp(i, j) = \min_{0 \leq k \leq j} \\{ dp(i - 1, k - 1) + C(k, j) \\}
$$

trong đó $C(k, j)$ là hàm chi phí và $dp(i, j) = 0$ khi $j \lt 0$.

Giả sử $0 \leq i \lt m$ và $0 \leq j \lt n$, và việc tính $C$ mất thời gian $O(1)$. Khi đó, việc tính toán trực tiếp công thức truy hồi trên mất $O(m n^2)$. Có $m \times n$ trạng thái, và $n$ chuyển đổi cho mỗi trạng thái.

Gọi $opt(i, j)$ là giá trị của $k$ để biểu thức trên đạt cực tiểu. Giả sử rằng hàm chi phí thỏa mãn bất đẳng thức tứ giác, ta có thể chứng minh rằng $opt(i, j) \leq opt(i, j + 1)$ với mọi $i, j$. Điều này được gọi là _điều kiện đơn điệu_. Khi đó, ta có thể áp dụng quy hoạch động chia để trị. "Điểm chia" tối ưu cho một $i$ cố định sẽ tăng khi $j$ tăng.

Điều này cho phép ta giải quyết tất cả các trạng thái hiệu quả hơn. Giả sử ta tính $opt(i, j)$ cho $i$ và $j$ cố định nào đó. Khi đó với mọi $j' < j$, ta biết rằng $opt(i, j') \leq opt(i, j)$. Điều này có nghĩa là khi tính $opt(i, j')$, ta không cần phải xem xét nhiều điểm chia như trước!

Để tối thiểu hóa thời gian chạy, ta áp dụng ý tưởng của chia để trị. Đầu tiên, tính $opt(i, n / 2)$. Sau đó, tính $opt(i, n / 4)$, biết rằng nó nhỏ hơn hoặc bằng $opt(i, n / 2)$, và tính $opt(i, 3 n / 4)$, biết rằng nó lớn hơn hoặc bằng $opt(i, n / 2)$. Bằng cách đệ quy và theo dõi các cận dưới và cận trên của $opt$, ta đạt được thời gian chạy $O(m n \log n)$. Mỗi giá trị có thể của $opt(i, j)$ chỉ xuất hiện trong $\log n$ nút khác nhau.

Lưu ý rằng việc $opt(i, j)$ có "cân bằng" hay không không quan trọng. Trên một tầng cố định, mỗi giá trị của $k$ được sử dụng tối đa hai lần, và có tối đa $\log n$ tầng.

## Cài đặt tổng quát

Mặc dù việc cài đặt thay đổi tùy theo bài toán, dưới đây là một mẫu khá tổng quát.
Hàm `compute` tính một hàng $i$ các trạng thái `dp_cur`, dựa trên hàng trước đó $i-1$ các trạng thái `dp_before`.
Hàm này phải được gọi với `compute(0, n-1, 0, n-1)`. Hàm `solve` tính toán `m` hàng và trả về kết quả.

```{.cpp file=divide_and_conquer_dp}
int m, n;
vector<long long> dp_before, dp_cur;

long long C(int i, int j);

// compute dp_cur[l], ... dp_cur[r] (inclusive)
void compute(int l, int r, int optl, int optr) {
    if (l > r)
        return;

    int mid = (l + r) >> 1;
    pair<long long, int> best = {LLONG_MAX, -1};

    for (int k = optl; k <= min(mid, optr); k++) {
        best = min(best, {(k ? dp_before[k - 1] : 0) + C(k, mid), k});
    }

    dp_cur[mid] = best.first;
    int opt = best.second;

    compute(l, mid - 1, optl, opt);
    compute(mid + 1, r, opt, optr);
}

long long solve() {
    dp_before.assign(n,0);
    dp_cur.assign(n,0);

    for (int i = 0; i < n; i++)
        dp_before[i] = C(0, i);

    for (int i = 1; i < m; i++) {
        compute(0, n - 1, 0, n - 1);
        dp_before = dp_cur;
    }

    return dp_before[n - 1];
}
```

### Những điều cần lưu ý

Khó khăn lớn nhất với các bài toán quy hoạch động Chia để trị là chứng minh tính đơn điệu của $opt$. Một trường hợp đặc biệt mà điều này đúng là khi hàm chi phí thỏa mãn bất đẳng thức tứ giác, tức là $C(a, c) + C(b, d) \leq C(a, d) + C(b, c)$ với mọi $a \leq b \leq c \leq d$.
Nhiều bài toán quy hoạch động Chia để trị cũng có thể giải được bằng kỹ thuật Bao lồi (Convex Hull trick) hoặc ngược lại. Việc biết và hiểu cả hai là rất hữu ích!

## Bài tập thực hành
- [AtCoder - Yakiniku Restaurants](https://atcoder.jp/contests/arc067/tasks/arc067_d)
- [CodeForces - Ciel and Gondolas](https://codeforces.com/contest/321/problem/E) (Hãy cẩn thận với I/O!)
- [CodeForces - Levels And Regions](https://codeforces.com/problemset/problem/673/E)
- [CodeForces - Partition Game](https://codeforces.com/contest/1527/problem/E)
- [CodeForces - The Bakery](https://codeforces.com/problemset/problem/834/D)
- [CodeForces - Yet Another Minimization Problem](https://codeforces.com/contest/868/problem/F)
- [Codechef - CHEFAOR](https://www.codechef.com/problems/CHEFAOR)
- [CodeForces - GUARDS](https://codeforces.com/gym/103536/problem/A) (Đây chính xác là bài toán trong bài viết này.)
- [Hackerrank - Guardians of the Lunatics](https://www.hackerrank.com/contests/ioi-2014-practice-contest-2/challenges/guardians-lunatics-ioi14)
- [Hackerrank - Mining](https://www.hackerrank.com/contests/world-codesprint-5/challenges/mining)
- [Kattis - Money (ACM ICPC World Finals 2017)](https://open.kattis.com/problems/money)
- [SPOJ - ADAMOLD](https://www.spoj.com/problems/ADAMOLD/)
- [SPOJ - LARMY](https://www.spoj.com/problems/LARMY/)
- [SPOJ - NKLEAVES](https://www.spoj.com/problems/NKLEAVES/)
- [Timus - Bicolored Horses](https://acm.timus.ru/problem.aspx?space=1&num=1167)
- [USACO - Circular Barn](https://usaco.org/index.php?page=viewproblem2&cpid=626)
- [UVA - Arranging Heaps](https://onlinejudge.org/external/125/12524.pdf)
- [UVA - Naming Babies](https://onlinejudge.org/external/125/12594.pdf)



## Tham khảo
- [Câu trả lời trên Quora của Michael Levin](https://www.quora.com/What-is-divide-and-conquer-optimization-in-dynamic-programming)
- [Video hướng dẫn bởi "Sothe" the Algorithm Wolf](