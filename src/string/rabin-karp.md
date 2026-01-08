---
tags:
  - Translated
e_maxx_link: rabin_karp
---

# Thuật toán Rabin-Karp cho việc so khớp chuỗi (Rabin-Karp Algorithm for string matching) {: #rabin-karp-algorithm-for-string-matching}

Thuật toán này dựa trên khái niệm băm, vì vậy nếu bạn không quen thuộc với băm chuỗi, hãy tham khảo bài viết [băm chuỗi](string-hashing.md).
 
Thuật toán này được tác giả bởi Rabin và Karp vào năm 1987.

Bài toán: Cho hai chuỗi - một mẫu $s$ và một văn bản $t$, xác định xem mẫu có xuất hiện trong văn bản hay không và nếu có, liệt kê tất cả các lần xuất hiện của nó trong thời gian $O(|s| + |t|)$.

Thuật toán: Tính toán băm cho mẫu $s$.
Tính toán các giá trị băm cho tất cả các tiền tố của văn bản $t$.
Bây giờ, chúng ta có thể so sánh một chuỗi con có độ dài $|s|$ với $s$ trong thời gian hằng số bằng cách sử dụng các giá trị băm đã tính toán.
Vì vậy, hãy so sánh từng chuỗi con có độ dài $|s|$ với mẫu. Điều này sẽ mất tổng thời gian là $O(|t|)$.
Do đó, độ phức tạp cuối cùng của thuật toán là $O(|t| + |s|)$: $O(|s|)$ được yêu cầu để tính toán băm của mẫu và $O(|t|)$ để so sánh mỗi chuỗi con có độ dài $|s|$ với mẫu.

## Cài đặt (Implementation) {: #implementation}

```{.cpp file=rabin_karp}
vector<int> rabin_karp(string const& s, string const& t) {
    const int p = 31; 
    const int m = 1e9 + 9;
    int S = s.size(), T = t.size();

    vector<long long> p_pow(max(S, T)); 
    p_pow[0] = 1; 
    for (int i = 1; i < (int)p_pow.size(); i++) 
        p_pow[i] = (p_pow[i-1] * p) % m;

    vector<long long> h(T + 1, 0); 
    for (int i = 0; i < T; i++)
        h[i+1] = (h[i] + (t[i] - 'a' + 1) * p_pow[i]) % m; 
    long long h_s = 0; 
    for (int i = 0; i < S; i++) 
        h_s = (h_s + (s[i] - 'a' + 1) * p_pow[i]) % m; 

    vector<int> occurrences;
    for (int i = 0; i + S - 1 < T; i++) {
        long long cur_h = (h[i+S] + m - h[i]) % m;
        if (cur_h == h_s * p_pow[i] % m)
            occurrences.push_back(i);
    }
    return occurrences;
}
```

## Bài tập (Practice Problems) {: #practice-problems}

* [SPOJ - Pattern Find](http://www.spoj.com/problems/NAJPF/)
* [Codeforces - Good Substrings](http://codeforces.com/problemset/problem/271/D)
* [Codeforces - Palindromic characteristics](https://codeforces.com/problemset/problem/835/D)
* [Leetcode - Longest Duplicate Substring](https://leetcode.com/problems/longest-duplicate-substring/)
