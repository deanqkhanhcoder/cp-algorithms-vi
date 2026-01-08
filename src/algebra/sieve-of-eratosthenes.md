---
tags:
  - Translated
e_maxx_link: eratosthenes_sieve
---

# Sàng Eratosthenes (Sieve of Eratosthenes) {: #sieve-of-eratosthenes}

Sàng Eratosthenes là một thuật toán để tìm tất cả các số nguyên tố trong một đoạn $[1;n]$ sử dụng $O(n \log \log n)$ phép toán.

Thuật toán rất đơn giản:
lúc đầu chúng ta viết ra tất cả các số giữa 2 và $n$.
Chúng ta đánh dấu tất cả các bội số thực sự của 2 (vì 2 là số nguyên tố nhỏ nhất) là hợp số.
Một bội số thực sự của một số $x$, là một số lớn hơn $x$ và chia hết cho $x$.
Sau đó chúng ta tìm số tiếp theo chưa được đánh dấu là hợp số, trong trường hợp này là 3.
Điều đó có nghĩa là 3 là số nguyên tố, và chúng ta đánh dấu tất cả các bội số thực sự của 3 là hợp số.
Số chưa được đánh dấu tiếp theo là 5, là số nguyên tố tiếp theo, và chúng ta đánh dấu tất cả các bội số thực sự của nó.
Và chúng ta tiếp tục quy trình này cho đến khi chúng ta đã xử lý tất cả các số trong hàng.

Trong hình ảnh sau, bạn có thể thấy một hình ảnh trực quan của thuật toán để tính toán tất cả các số nguyên tố trong phạm vi $[1; 16]$. Có thể thấy rằng khá thường xuyên chúng ta đánh dấu các số là hợp số nhiều lần.

<div style="text-align: center;">
  <img src="sieve_eratosthenes.png" alt="Sieve of Eratosthenes">
</div>

Ý tưởng đằng sau là thế này:
Một số là số nguyên tố, nếu không có số nguyên tố nhỏ hơn nào chia hết nó.
Vì chúng ta lặp qua các số nguyên tố theo thứ tự, chúng ta đã đánh dấu tất cả các số, chia hết cho ít nhất một trong các số nguyên tố, là chia hết.
Do đó, nếu chúng ta đến một ô và nó chưa được đánh dấu, thì nó không chia hết cho bất kỳ số nguyên tố nhỏ hơn nào và do đó phải là số nguyên tố.

## Cài đặt (Implementation) {: #implementation}

```cpp
int n;
vector<bool> is_prime(n+1, true);
is_prime[0] = is_prime[1] = false;
for (int i = 2; i <= n; i++) {
    if (is_prime[i] && (long long)i * i <= n) {
        for (int j = i * i; j <= n; j += i)
            is_prime[j] = false;
    }
}
```

Mã này đầu tiên đánh dấu tất cả các số ngoại trừ không và một là các số nguyên tố tiềm năng, sau đó nó bắt đầu quá trình sàng lọc các hợp số.
Để làm điều này nó lặp qua tất cả các số từ $2$ đến $n$.
Nếu số hiện tại $i$ là một số nguyên tố, nó đánh dấu tất cả các số là bội của $i$ là hợp số, bắt đầu từ $i^2$.
Đây đã là một sự tối ưu hóa so với cách ngây thơ khi cài đặt nó, và được cho phép vì tất cả các số nhỏ hơn là bội của $i$ nhất thiết cũng có một thừa số nguyên tố nhỏ hơn $i$, vì vậy tất cả chúng đã được sàng lọc trước đó.
Vì $i^2$ có thể dễ dàng tràn kiểu `int`, việc xác minh bổ sung được thực hiện bằng cách sử dụng kiểu `long long` trước vòng lặp lồng nhau thứ hai.

Sử dụng cài đặt như vậy thuật toán tiêu thụ $O(n)$ bộ nhớ (rõ ràng) và thực hiện $O(n \log \log n)$ (xem phần tiếp theo).

## Phân tích tiệm cận (Asymptotic analysis) {: #asymptotic-analysis}

Rất đơn giản để chứng minh thời gian chạy là $O(n \log n)$ mà không cần biết bất cứ điều gì về phân bố của các số nguyên tố - bỏ qua kiểm tra `is_prime`, vòng lặp bên trong chạy (nhiều nhất) $n/i$ lần cho $i = 2, 3, 4, \dots$, dẫn đến tổng số phép toán trong vòng lặp bên trong là một tổng điều hòa như $n(1/2 + 1/3 + 1/4 + \cdots)$, bị giới hạn bởi $O(n \log n)$.

Hãy chứng minh rằng thời gian chạy của thuật toán là $O(n \log \log n)$.
Thuật toán sẽ thực hiện $\frac{n}{p}$ các phép toán cho mỗi số nguyên tố $p \le n$ trong vòng lặp bên trong.
Do đó, chúng ta cần đánh giá biểu thức tiếp theo:

$$\sum_{\substack{p \le n, \\\ p \text{ prime}}} \frac n p = n \cdot \sum_{\substack{p \le n, \\\ p \text{ prime}}} \frac 1 p.$$

Hãy nhớ lại hai sự thật đã biết.

  - Số lượng các số nguyên tố nhỏ hơn hoặc bằng $n$ xấp xỉ $\frac n {\ln n}$.
  - Số nguyên tố thứ $k$ xấp xỉ bằng $k \ln k$ (điều này theo sau từ sự thật trước đó).

Do đó chúng ta có thể viết tổng theo cách sau:

$$\sum_{\substack{p \le n, \\\ p \text{ prime}}} \frac 1 p \approx \frac 1 2 + \sum_{k = 2}^{\frac n {\ln n}} \frac 1 {k \ln k}.$$

Ở đây chúng ta đã trích xuất số nguyên tố đầu tiên 2 từ tổng, bởi vì $k = 1$ trong xấp xỉ $k \ln k$ là $0$ và gây ra phép chia cho số không.

Bây giờ, hãy đánh giá tổng này bằng cách sử dụng tích phân của cùng một hàm trên $k$ từ $2$ đến $\frac n {\ln n}$ (chúng ta có thể thực hiện xấp xỉ như vậy bởi vì, thực tế, tổng liên quan đến tích phân như là xấp xỉ của nó bằng phương pháp hình chữ nhật):

$$\sum_{k = 2}^{\frac n {\ln n}} \frac 1 {k \ln k} \approx \int_2^{\frac n {\ln n}} \frac 1 {k \ln k} dk.$$

Nguyên hàm cho hàm dưới dấu tích phân là $\ln \ln k$. Sử dụng phép thay thế và loại bỏ các số hạng bậc thấp hơn, chúng ta sẽ nhận được kết quả:

$$\int_2^{\frac n {\ln n}} \frac 1 {k \ln k} dk = \ln \ln \frac n {\ln n} - \ln \ln 2 = \ln(\ln n - \ln \ln n) - \ln \ln 2 \approx \ln \ln n.$$

Bây giờ, quay lại tổng ban đầu, chúng ta sẽ nhận được đánh giá xấp xỉ của nó:

$$\sum_{\substack{p \le n, \\\ p\ is\ prime}} \frac n p \approx n \ln \ln n + o(n).$$

Bạn có thể tìm thấy một chứng minh chặt chẽ hơn (mang lại đánh giá chính xác hơn trong phạm vi các hệ số hằng) trong cuốn sách được viết bởi Hardy & Wright "An Introduction to the Theory of Numbers" (tr. 349).

## Các tối ưu hóa khác nhau của Sàng Eratosthenes (Different optimizations of the Sieve of Eratosthenes) {: #different-optimizations-of-the-sieve-of-eratosthenes}

Điểm yếu lớn nhất của thuật toán là, nó "đi bộ" dọc theo bộ nhớ nhiều lần, chỉ thao tác các phần tử đơn lẻ.
Điều này không thân thiện với bộ nhớ cache.
Và vì điều đó, hằng số ẩn trong $O(n \log \log n)$ là khá lớn.

Ngoài ra, bộ nhớ tiêu thụ là một nút thắt cổ chai cho $n$ lớn.

Các phương pháp được trình bày dưới đây cho phép chúng ta giảm số lượng các phép toán được thực hiện, cũng như rút ngắn bộ nhớ tiêu thụ đáng kể.

### Sàng đến căn bậc hai (Sieving till root) {: #sieving-till-root}

Rõ ràng, để tìm tất cả các số nguyên tố cho đến $n$, sẽ là đủ để chỉ thực hiện việc sàng lọc chỉ bằng các số nguyên tố, không vượt quá căn bậc hai của $n$.

```cpp
int n;
vector<bool> is_prime(n+1, true);
is_prime[0] = is_prime[1] = false;
for (int i = 2; i * i <= n; i++) {
    if (is_prime[i]) {
        for (int j = i * i; j <= n; j += i)
            is_prime[j] = false;
    }
}
```

Tối ưu hóa như vậy không ảnh hưởng đến độ phức tạp (thật vậy, bằng cách lặp lại chứng minh được trình bày ở trên chúng ta sẽ nhận được đánh giá $n \ln \ln \sqrt n + o(n)$, là tiệm cận giống nhau theo các tính chất của logarit), mặc dù số lượng các phép toán sẽ giảm đáng kể.

### Chỉ sàng các số lẻ (Sieving by the odd numbers only) {: #sieving-by-the-odd-numbers-only}

Vì tất cả các số chẵn (ngoại trừ $2$) là hợp số, chúng ta có thể ngừng kiểm tra các số chẵn hoàn toàn. Thay vào đó, chúng ta cần hoạt động với các số lẻ thôi.

Thứ nhất, nó sẽ cho phép chúng ta giảm một nửa bộ nhớ cần thiết. Thứ hai, nó sẽ giảm số lượng các phép toán được thực hiện bởi thuật toán xấp xỉ một nửa.

### Tiêu thụ bộ nhớ và tốc độ (Memory consumption and speed of operations) {: #memory-consumption-and-speed-of-operations}

Chúng ta nên nhận thấy, rằng hai cài đặt này của Sàng Eratosthenes sử dụng $n$ bit bộ nhớ bằng cách sử dụng cấu trúc dữ liệu `vector<bool>`.
`vector<bool>` không phải là một container thông thường lưu trữ một loạt các `bool` (như trong hầu hết các kiến trúc máy tính một `bool` chiếm một byte bộ nhớ).
Nó là một chuyên môn hóa tối ưu hóa bộ nhớ của `vector<T>`, chỉ tiêu thụ $\frac{N}{8}$ byte bộ nhớ.

Các kiến trúc bộ xử lý hiện đại làm việc hiệu quả hơn nhiều với byte so với bit vì chúng thường không thể truy cập bit trực tiếp.
Vì vậy bên dưới `vector<bool>` lưu trữ các bit trong một bộ nhớ liên tục lớn, truy cập bộ nhớ trong các khối vài byte, và trích xuất/đặt các bit bằng các phép toán bit như mặt nạ bit và dịch bit.

Vì điều đó có một chi phí nhất định khi bạn đọc hoặc ghi các bit với một `vector<bool>`, và khá thường xuyên sử dụng một `vector<char>` (sử dụng 1 byte cho mỗi mục, vì vậy gấp 8 lần lượng bộ nhớ) là nhanh hơn.

Tuy nhiên, đối với các cài đặt đơn giản của Sàng Eratosthenes sử dụng một `vector<bool>` là nhanh hơn.
Bạn bị giới hạn bởi tốc độ bạn có thể tải dữ liệu vào bộ nhớ cache, và do đó sử dụng ít bộ nhớ hơn mang lại lợi thế lớn.
Một bài kiểm tra điểm chuẩn ([liên kết](https://gist.github.com/jakobkogler/e6359ea9ced24fe304f1a8af3c9bee0e)) cho thấy, rằng sử dụng một `vector<bool>` là nhanh hơn từ 1.4 lần đến 1.7 lần so với sử dụng một `vector<char>`.

Các cân nhắc tương tự cũng áp dụng cho `bitset`.
Nó cũng là một cách hiệu quả để lưu trữ các bit, tương tự như `vector<bool>`, vì vậy nó chỉ mất $\frac{N}{8}$ byte bộ nhớ, nhưng chậm hơn một chút trong việc truy cập các phần tử.
Trong bài kiểm tra điểm chuẩn ở trên `bitset` hoạt động kém hơn một chút so với `vector<bool>`.
Một nhược điểm khác từ `bitset` là bạn cần biết kích thước tại thời điểm biên dịch.

### Sàng phân đoạn (Segmented Sieve) {: #segmented-sieve}

Từ tối ưu hóa "sàng đến căn bậc hai", suy ra rằng không cần thiết phải giữ toàn bộ mảng `is_prime[1...n]` mọi lúc.
Đối với việc sàng lọc là đủ để chỉ giữ các số nguyên tố cho đến căn bậc hai của $n$, tứ là `prime[1... sqrt(n)]`, chia phạm vi hoàn chỉnh thành các khối, và sàng từng khối riêng biệt.

Gọi $s$ là một hằng số xác định kích thước của khối, sau đó chúng ta có $\lceil {\frac n s} \rceil$ khối tất cả, và khối $k$ ($k = 0 ... \lfloor {\frac n s} \rfloor$) chứa các số trong một đoạn $[ks; ks + s - 1]$.
Chúng ta có thể làm việc trên các khối lần lượt, tức là đối với mỗi khối $k$ chúng ta sẽ đi qua tất cả các số nguyên tố (từ $1$ đến $\sqrt n$) và thực hiện sàng lọc sử dụng chúng.
Đáng chú ý là, chúng ta phải sửa đổi chiến lược một chút khi xử lý các số đầu tiên: thứ nhất, tất cả các số nguyên tố từ $[1; \sqrt n]$ không nên loại bỏ chính nó; và thứ hai, các số $0$ và $1$ nên được đánh dấu là số không phải nguyên tố.
Trong khi làm việc trên khối cuối cùng không nên quên rằng số cần thiết cuối cùng $n$ không nhất thiết nằm ở cuối khối.

Như đã thảo luận trước đây, việc cài đặt điển hình của Sàng Eratosthenes bị giới hạn bởi tốc độ tải dữ liệu vào bộ đệm CPU nhanh như thế nào.
Bằng cách chia phạm vi các số nguyên tố tiềm năng $[1; n]$ thành các khối nhỏ hơn, chúng ta không bao giờ phải giữ nhiều khối trong bộ nhớ cùng một lúc, và tất cả các phép toán thân thiện với bộ nhớ cache hơn nhiều.
Khi chúng ta không còn bị giới hạn bởi tốc độ bộ nhớ cache, chúng ta có thể thay thế `vector<bool>` bằng `vector<char>`, và đạt được một số hiệu suất bổ sung vì các bộ xử lý có thể xử lý đọc và ghi với byte trực tiếp và không cần dựa vào các phép toán bit để trích xuất các bit riêng lẻ.
Bài kiểm tra điểm chuẩn ([liên kết](https://gist.github.com/jakobkogler/e6359ea9ced24fe304f1a8af3c9bee0e)) cho thấy, rằng sử dụng một `vector<char>` nhanh hơn khoảng 3 lần trong tình huống này so với sử dụng một `vector<bool>`.
Một lời cảnh báo: những con số đó có thể khác nhau tùy thuộc vào kiến trúc, trình biên dịch và mức độ tối ưu hóa.

Ở đây chúng tôi có một cài đặt đếm số lượng các số nguyên tố nhỏ hơn hoặc bằng $n$ sử dụng sàng khối.

```cpp
int count_primes(int n) {
    const int S = 10000;

    vector<int> primes;
    int nsqrt = sqrt(n);
    vector<char> is_prime(nsqrt + 2, true);
    for (int i = 2; i <= nsqrt; i++) {
        if (is_prime[i]) {
            primes.push_back(i);
            for (int j = i * i; j <= nsqrt; j += i)
                is_prime[j] = false;
        }
    }

    int result = 0;
    vector<char> block(S);
    for (int k = 0; k * S <= n; k++) {
        fill(block.begin(), block.end(), true);
        int start = k * S;
        for (int p : primes) {
            int start_idx = (start + p - 1) / p;
            int j = max(start_idx, p) * p - start;
            for (; j < S; j += p)
                block[j] = false;
        }
        if (k == 0)
            block[0] = block[1] = false;
        for (int i = 0; i < S && start + i <= n; i++) {
            if (block[i])
                result++;
        }
    }
    return result;
}
```

Thời gian chạy của sàng khối giống như đối với sàng Eratosthenes thông thường (trừ khi kích thước của các khối rất nhỏ), nhưng bộ nhớ cần thiết sẽ rút ngắn còn $O(\sqrt{n} + S)$ và chúng ta có kết quả lưu trữ đệm tốt hơn.
Mặt khác, sẽ có một phép chia cho mỗi cặp khối và số nguyên tố từ $[1; \sqrt{n}]$, và điều đó sẽ tồi tệ hơn nhiều đối với kích thước khối nhỏ hơn.
Do đó, cần phải giữ cân bằng khi chọn hằng số $S$.
Chúng tôi đạt được kết quả tốt nhất cho kích thước khối giữa $10^4$ và $10^5$.

## Tìm số nguyên tố trong phạm vi (Find primes in range) {: #find-primes-in-range}

Đôi khi chúng ta cần tìm tất cả các số nguyên tố trong một phạm vi $[L,R]$ kích thước nhỏ (ví dụ $R - L + 1 \approx 1e7$), trong đó $R$ có thể rất lớn (ví dụ $1e12$).

Để giải quyết một vấn đề như vậy, chúng ta có thể sử dụng ý tưởng của Sàng phân đoạn.
Chúng tôi tạo trước tất cả các số nguyên tố lên đến $\sqrt R$, và sử dụng các số nguyên tố đó để đánh dấu tất cả các hợp số trong đoạn $[L, R]$.

```cpp
vector<char> segmentedSieve(long long L, long long R) {
    // generate all primes up to sqrt(R)
    long long lim = sqrt(R);
    vector<char> mark(lim + 1, false);
    vector<long long> primes;
    for (long long i = 2; i <= lim; ++i) {
        if (!mark[i]) {
            primes.emplace_back(i);
            for (long long j = i * i; j <= lim; j += i)
                mark[j] = true;
        }
    }

    vector<char> isPrime(R - L + 1, true);
    for (long long i : primes)
        for (long long j = max(i * i, (L + i - 1) / i * i); j <= R; j += i)
            isPrime[j - L] = false;
    if (L == 1)
        isPrime[0] = false;
    return isPrime;
}
```
Độ phức tạp thời gian của cách tiếp cận này là $O((R - L + 1) \log \log (R) + \sqrt R \log \log \sqrt R)$.

Cũng có thể rằng chúng ta không tạo trước tất cả các số nguyên tố:

```cpp
vector<char> segmentedSieveNoPreGen(long long L, long long R) {
    vector<char> isPrime(R - L + 1, true);
    long long lim = sqrt(R);
    for (long long i = 2; i <= lim; ++i)
        for (long long j = max(i * i, (L + i - 1) / i * i); j <= R; j += i)
            isPrime[j - L] = false;
    if (L == 1)
        isPrime[0] = false;
    return isPrime;
}
```

Rõ ràng, độ phức tạp tồi tệ hơn, đó là $O((R - L + 1) \log (R) + \sqrt R)$. Tuy nhiên, nó vẫn chạy rất nhanh trong thực tế.

## Thay đổi thời gian tuyến tính (Linear time modification) {: #linear-time-modification}

Chúng ta có thể sửa đổi thuật toán theo cách như vậy, sao cho nó chỉ có độ phức tạp thời gian tuyến tính.
Cách tiếp cận này được mô tả trong bài viết [Sàng tuyến tính](prime-sieve-linear.md).
Tuy nhiên, thuật toán này cũng có điểm yếu riêng của nó.

## Bài tập luyện tập {: #practice-problems}

* [Leetcode - Four Divisors](https://leetcode.com/problems/four-divisors/)
* [Leetcode - Count Primes](https://leetcode.com/problems/count-primes/)
* [SPOJ - Printing Some Primes](http://www.spoj.com/problems/TDPRIMES/)
* [SPOJ - A Conjecture of Paul Erdos](http://www.spoj.com/problems/HS08PAUL/)
* [SPOJ - Primal Fear](http://www.spoj.com/problems/VECTAR8/)
* [SPOJ - Primes Triangle (I)](http://www.spoj.com/problems/PTRI/)
* [Codeforces - Almost Prime](http://codeforces.com/contest/26/problem/A)
* [Codeforces - Sherlock And His Girlfriend](http://codeforces.com/contest/776/problem/B)
* [SPOJ - Namit in Trouble](http://www.spoj.com/problems/NGIRL/)
* [SPOJ - Bazinga!](http://www.spoj.com/problems/DCEPC505/)
* [Project Euler - Prime pair connection](https://www.hackerrank.com/contests/projecteuler/challenges/euler134)
* [SPOJ - N-Factorful](http://www.spoj.com/problems/NFACTOR/)
* [SPOJ - Binary Sequence of Prime Numbers](http://www.spoj.com/problems/BSPRIME/)
* [UVA 11353 - A Different Kind of Sorting](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2338)
* [SPOJ - Prime Generator](http://www.spoj.com/problems/PRIME1/)
* [SPOJ - Printing some primes (hard)](http://www.spoj.com/problems/PRIMES2/)
* [Codeforces - Nodbach Problem](https://codeforces.com/problemset/problem/17/A)
* [Codeforces - Colliders](https://codeforces.com/problemset/problem/154/B)

---

## Checklist

- Original lines: 277
- Translated lines: 277
- Code blocks changed? No
- Inline code changed? No
- Technical terms kept in English? Yes
- Headings anchors preserved/added correctly? Yes
- I confirm no character was omitted: YES
