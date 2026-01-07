---
tags:
  - Translated
e_maxx_link: eratosthenes_sieve
---

# Sàng Eratosthenes

Sàng Eratosthenes là một thuật toán để tìm tất cả các số nguyên tố trong một đoạn $[1;n]$ sử dụng $O(n \log \log n)$ phép toán.

Thuật toán rất đơn giản:
ban đầu chúng ta viết ra tất cả các số từ 2 đến $n$.
Chúng ta đánh dấu tất cả các bội số thực sự của 2 (vì 2 là số nguyên tố nhỏ nhất) là hợp số.
Một bội số thực sự của một số $x$, là một số lớn hơn $x$ và chia hết cho $x$.
Sau đó, chúng ta tìm số tiếp theo chưa được đánh dấu là hợp số, trong trường hợp này là 3.
Điều đó có nghĩa là 3 là số nguyên tố, và chúng ta đánh dấu tất cả các bội số thực sự của 3 là hợp số.
Số chưa được đánh dấu tiếp theo là 5, là số nguyên tố tiếp theo, và chúng ta đánh dấu tất cả các bội số thực sự của nó.
Và chúng ta tiếp tục thủ tục này cho đến khi chúng ta đã xử lý tất cả các số trong hàng.

Trong hình ảnh sau, bạn có thể thấy một hình dung về thuật toán để tính tất cả các số nguyên tố trong phạm vi $[1; 16]$. Có thể thấy, chúng ta thường đánh dấu các số là hợp số nhiều lần.

<div style="text-align: center;">
  <img src="sieve_eratosthenes.png" alt="Sàng Eratosthenes">
</div>

Ý tưởng đằng sau là thế này:
Một số là số nguyên tố, nếu không có số nguyên tố nào nhỏ hơn chia hết cho nó.
Vì chúng ta lặp qua các số nguyên tố theo thứ tự, chúng ta đã đánh dấu tất cả các số, chia hết cho ít nhất một trong các số nguyên tố, là hợp số.
Do đó, nếu chúng ta đến một ô và nó không được đánh dấu, thì nó không chia hết cho bất kỳ số nguyên tố nào nhỏ hơn và do đó phải là số nguyên tố.

## Cài đặt

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

Đoạn mã này đầu tiên đánh dấu tất cả các số ngoại trừ không và một là các số nguyên tố tiềm năng, sau đó nó bắt đầu quá trình sàng các hợp số.
Để làm điều này, nó lặp qua tất cả các số từ $2$ đến $n$.
Nếu số hiện tại $i$ là một số nguyên tố, nó đánh dấu tất cả các số là bội số của $i$ là hợp số, bắt đầu từ $i^2$.
Đây đã là một sự tối ưu hóa so với cách triển khai ngây thơ, và được cho phép vì tất cả các số nhỏ hơn là bội số của $i$ cần thiết cũng có một thừa số nguyên tố nhỏ hơn $i$, vì vậy tất cả chúng đã được sàng lọc trước đó.
Vì $i^2$ có thể dễ dàng tràn kiểu `int`, việc xác minh bổ sung được thực hiện bằng cách sử dụng kiểu `long long` trước vòng lặp lồng thứ hai.

Sử dụng một triển khai như vậy, thuật toán tiêu thụ $O(n)$ bộ nhớ (rõ ràng) và thực hiện $O(n \log \log n)$ (xem phần tiếp theo).

## Phân tích tiệm cận

Dễ dàng chứng minh thời gian chạy là $O(n \log n)$ mà không cần biết gì về sự phân bố của các số nguyên tố - bỏ qua việc kiểm tra `is_prime`, vòng lặp bên trong chạy (nhiều nhất) $n/i$ lần cho $i = 2, 3, 4, \dots$, dẫn đến tổng số phép toán trong vòng lặp bên trong là một tổng hài hòa như $n(1/2 + 1/3 + 1/4 + \cdots)$, được giới hạn bởi $O(n \log n)$.

Hãy chứng minh rằng thời gian chạy của thuật toán là $O(n \log \log n)$.
Thuật toán sẽ thực hiện $\frac{n}{p}$ phép toán cho mỗi số nguyên tố $p \le n$ trong vòng lặp bên trong.
Do đó, chúng ta cần đánh giá biểu thức sau:

$$\sum_{\substack{p \le n, \\ p \text{ là số nguyên tố}}} \frac n p = n \cdot \sum_{\substack{p \le n, \\ p \text{ là số nguyên tố}}} \frac 1 p.$$

Hãy nhớ lại hai sự thật đã biết.

  - Số lượng số nguyên tố nhỏ hơn hoặc bằng $n$ xấp xỉ $\frac n {\ln n}$.
  - Số nguyên tố thứ $k$ xấp xỉ bằng $k \ln k$ (điều này xuất phát từ sự thật trước đó).

Do đó, chúng ta có thể viết tổng theo cách sau:

$$\sum_{\substack{p \le n, \\ p \text{ là số nguyên tố}}} \frac 1 p \approx \frac 1 2 + \sum_{k = 2}^{\frac n {\ln n}} \frac 1 {k \ln k}.$$ 

Ở đây chúng ta đã tách số nguyên tố đầu tiên 2 ra khỏi tổng, vì $k = 1$ trong phép xấp xỉ $k \ln k$ là $0$ và gây ra phép chia cho không.

Bây giờ, hãy đánh giá tổng này bằng cách sử dụng tích phân của một hàm tương tự trên $k$ từ $2$ đến $\frac n {\ln n}$ (chúng ta có thể thực hiện phép xấp xỉ như vậy vì, trên thực tế, tổng có liên quan đến tích phân như là phép xấp xỉ của nó bằng phương pháp hình chữ nhật):

$$\sum_{k = 2}^{\frac n {\ln n}} \frac 1 {k \ln k} \approx \int_2^{\frac n {\ln n}} \frac 1 {k \ln k} dk.$$

Nguyên hàm của hàm số bị tích phân là $\ln \ln k$. Sử dụng một phép thay thế và loại bỏ các số hạng bậc thấp hơn, chúng ta sẽ có được kết quả:

$$\int_2^{\frac n {\ln n}} \frac 1 {k \ln k} dk = \ln \ln \frac n {\ln n} - \ln \ln 2 = \ln(\ln n - \ln \ln n) - \ln \ln 2 \approx \ln \ln n.$$

Bây giờ, quay trở lại tổng ban đầu, chúng ta sẽ có được đánh giá gần đúng của nó:

$$\sum_{\substack{p \le n, \\ p\ là\ số\ nguyên\ tố}} \frac n p \approx n \ln \ln n + o(n).$$ 

Bạn có thể tìm thấy một chứng minh chặt chẽ hơn (cung cấp đánh giá chính xác hơn trong phạm vi các hệ số hằng) trong cuốn sách của Hardy & Wright "An Introduction to the Theory of Numbers" (tr. 349).

## Các tối ưu hóa khác nhau của Sàng Eratosthenes

Điểm yếu lớn nhất của thuật toán là nó "đi bộ" dọc theo bộ nhớ nhiều lần, chỉ thao tác các phần tử đơn lẻ.
Điều này không thân thiện với bộ đệm.
Và vì thế, hằng số ẩn trong $O(n \log \log n)$ tương đối lớn.

Bên cạnh đó, bộ nhớ tiêu thụ là một nút thắt cổ chai đối với $n$ lớn.

Các phương pháp được trình bày dưới đây cho phép chúng ta giảm số lượng các phép toán được thực hiện, cũng như rút ngắn đáng kể bộ nhớ tiêu thụ.

### Sàng đến căn bậc hai

Rõ ràng, để tìm tất cả các số nguyên tố cho đến $n$, chỉ cần thực hiện sàng lọc bằng các số nguyên tố không vượt quá căn bậc hai của $n$ là đủ.

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

Một tối ưu hóa như vậy không ảnh hưởng đến độ phức tạp (thật vậy, bằng cách lặp lại chứng minh được trình bày ở trên, chúng ta sẽ có được đánh giá $n \ln \ln \sqrt n + o(n)$, tiệm cận giống nhau theo các thuộc tính của logarit), mặc dù số lượng các phép toán sẽ giảm đáng kể.

### Chỉ sàng các số lẻ

Vì tất cả các số chẵn (ngoại trừ $2$) là hợp số, chúng ta có thể ngừng kiểm tra các số chẵn hoàn toàn. Thay vào đó, chúng ta chỉ cần thao tác với các số lẻ.

Đầu tiên, nó sẽ cho phép chúng ta giảm một nửa bộ nhớ cần thiết. Thứ hai, nó sẽ giảm số lượng các phép toán được thực hiện bởi thuật toán khoảng một nửa.

### Tiêu thụ bộ nhớ và tốc độ hoạt động

Chúng ta nên lưu ý rằng hai triển khai này của Sàng Eratosthenes sử dụng $n$ bit bộ nhớ bằng cách sử dụng cấu trúc dữ liệu `vector<bool>`.
`vector<bool>` không phải là một container thông thường lưu trữ một chuỗi các `bool` (vì trong hầu hết các kiến trúc máy tính, một `bool` chiếm một byte bộ nhớ).
Đó là một chuyên biệt hóa tối ưu hóa bộ nhớ của `vector<T>`, chỉ tiêu thụ $\frac{N}{8}$ byte bộ nhớ.

Các kiến trúc bộ xử lý hiện đại hoạt động hiệu quả hơn nhiều với các byte hơn là với các bit vì chúng thường không thể truy cập trực tiếp các bit.
Vì vậy, bên dưới `vector<bool>` lưu trữ các bit trong một bộ nhớ liên tục lớn, truy cập bộ nhớ theo các khối gồm một vài byte và trích xuất/đặt các bit bằng các phép toán bit như mặt nạ bit và dịch chuyển bit.

Vì thế, có một chi phí nhất định khi bạn đọc hoặc ghi các bit bằng `vector<bool>`, và khá thường xuyên việc sử dụng `vector<char>` (sử dụng 1 byte cho mỗi mục, do đó gấp 8 lần dung lượng bộ nhớ) lại nhanh hơn.

Tuy nhiên, đối với các triển khai đơn giản của Sàng Eratosthenes, việc sử dụng `vector<bool>` lại nhanh hơn.
Bạn bị giới hạn bởi tốc độ bạn có thể tải dữ liệu vào bộ đệm, và do đó việc sử dụng ít bộ nhớ hơn mang lại một lợi thế lớn.
Một bài kiểm tra hiệu năng ([link](https://gist.github.com/jakobkogler/e6359ea9ced24fe304f1a8af3c9bee0e)) cho thấy, việc sử dụng `vector<bool>` nhanh hơn từ 1,4 đến 1,7 lần so với việc sử dụng `vector<char>`.

Những cân nhắc tương tự cũng áp dụng cho `bitset`.
Đó cũng là một cách hiệu quả để lưu trữ các bit, tương tự như `vector<bool>`, vì vậy nó chỉ chiếm $\frac{N}{8}$ byte bộ nhớ, nhưng chậm hơn một chút trong việc truy cập các phần tử.
Trong bài kiểm tra hiệu năng ở trên, `bitset` hoạt động kém hơn một chút so với `vector<bool>`.
Một nhược điểm khác của `bitset` là bạn cần biết kích thước tại thời điểm biên dịch.

### Sàng phân đoạn

Từ tối ưu hóa "sàng đến căn bậc hai" suy ra rằng không cần phải giữ toàn bộ mảng `is_prime[1...n]` mọi lúc.
Để sàng, chỉ cần giữ các số nguyên tố cho đến căn bậc hai của $n$, tức là `prime[1... sqrt(n)]`, chia toàn bộ phạm vi thành các khối, và sàng từng khối riêng biệt.

Đặt $s$ là một hằng số xác định kích thước của khối, khi đó chúng ta có tổng cộng $\lceil {\frac n s} \rceil$ khối, và khối $k$ ($k = 0 ... \lfloor {\frac n s} \rfloor$) chứa các số trong một đoạn $[ks; ks + s - 1]$.
Chúng ta có thể làm việc trên các khối lần lượt, tức là đối với mỗi khối $k$, chúng ta sẽ đi qua tất cả các số nguyên tố (từ $1$ đến $\sqrt n$) và thực hiện sàng lọc bằng cách sử dụng chúng.
Đáng chú ý là chúng ta phải sửa đổi một chút chiến lược khi xử lý các số đầu tiên: thứ nhất, tất cả các số nguyên tố từ $[1; \sqrt n]$ không nên loại bỏ chính chúng; và thứ hai, các số $0$ và $1$ nên được đánh dấu là không phải số nguyên tố.
Trong khi làm việc trên khối cuối cùng, không nên quên rằng số cần thiết cuối cùng $n$ không nhất thiết phải nằm ở cuối khối.

Như đã thảo luận trước đó, việc triển khai điển hình của Sàng Eratosthenes bị giới hạn bởi tốc độ bạn có thể tải dữ liệu vào bộ đệm của CPU.
Bằng cách chia phạm vi các số nguyên tố tiềm năng $[1; n]$ thành các khối nhỏ hơn, chúng ta không bao giờ phải giữ nhiều khối trong bộ nhớ cùng một lúc, và tất cả các hoạt động đều thân thiện với bộ đệm hơn nhiều.
Vì chúng ta không còn bị giới hạn bởi tốc độ bộ đệm nữa, chúng ta có thể thay thế `vector<bool>` bằng `vector<char>`, và đạt được một số hiệu suất bổ sung vì các bộ xử lý có thể xử lý việc đọc và ghi trực tiếp bằng byte và không cần dựa vào các phép toán bit để trích xuất các bit riêng lẻ.
Bài kiểm tra hiệu năng ([link](https://gist.github.com/jakobkogler/e6359ea9ced24fe304f1a8af3c9bee0e)) cho thấy, việc sử dụng `vector<char>` nhanh hơn khoảng 3 lần trong tình huống này so với việc sử dụng `vector<bool>`.
Một lời cảnh báo: những con số đó có thể khác nhau tùy thuộc vào kiến trúc, trình biên dịch và mức độ tối ưu hóa.

Ở đây chúng ta có một triển khai đếm số lượng số nguyên tố nhỏ hơn hoặc bằng $n$ bằng cách sử dụng sàng khối.

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

Thời gian chạy của sàng khối giống như sàng Eratosthenes thông thường (trừ khi kích thước của các khối rất nhỏ), nhưng bộ nhớ cần thiết sẽ rút ngắn xuống còn $O(\sqrt{n} + S)$ và chúng ta có kết quả bộ đệm tốt hơn.
Mặt khác, sẽ có một phép chia cho mỗi cặp một khối và một số nguyên tố từ $[1; \sqrt{n}]$, và điều đó sẽ tệ hơn nhiều đối với các kích thước khối nhỏ hơn.
Do đó, cần phải giữ cân bằng khi chọn hằng số $S$.
Chúng tôi đã đạt được kết quả tốt nhất cho các kích thước khối từ $10^4$ đến $10^5$.

## Tìm số nguyên tố trong một khoảng

Đôi khi chúng ta cần tìm tất cả các số nguyên tố trong một khoảng $[L,R]$ có kích thước nhỏ (ví dụ: $R - L + 1 \approx 1e7$), trong đó $R$ có thể rất lớn (ví dụ: $1e12$).

Để giải quyết một vấn đề như vậy, chúng ta có thể sử dụng ý tưởng của sàng phân đoạn.
Chúng ta tiền tạo tất cả các số nguyên tố lên đến $\sqrt R$, và sử dụng các số nguyên tố đó để đánh dấu tất cả các hợp số trong đoạn $[L, R]$.

```cpp
vector<char> segmentedSieve(long long L, long long R) {
    // tạo tất cả các số nguyên tố lên đến sqrt(R)
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
Độ phức tạp thời gian của phương pháp này là $O((R - L + 1) \log \log (R) + \sqrt R \log \log \sqrt R)$.

Cũng có thể chúng ta không tiền tạo tất cả các số nguyên tố:

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

Rõ ràng, độ phức tạp tệ hơn, là $O((R - L + 1) \log (R) + \sqrt R)$. Tuy nhiên, nó vẫn chạy rất nhanh trong thực tế.

## Sửa đổi thời gian tuyến tính

Chúng ta có thể sửa đổi thuật toán theo cách mà nó chỉ có độ phức tạp thời gian tuyến tính.
Cách tiếp cận này được mô tả trong bài viết [Sàng tuyến tính](prime-sieve-linear.md).
Tuy nhiên, thuật toán này cũng có những điểm yếu riêng.

## Bài tập luyện tập

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