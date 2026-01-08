---
tags:
  - Translated
e_maxx_link: gray_code
---

# Mã Gray (Gray code) {: #gray-code}

Mã Gray là một hệ thống số nhị phân trong đó hai giá trị liên tiếp chỉ khác nhau ở một bit.

Ví dụ, dãy mã Gray cho các số 3-bit là: 000, 001, 011, 010, 110, 111, 101, 100, vì vậy $G(4) = 6$.

Mã này được phát minh bởi Frank Gray vào năm 1953.

## Tìm mã Gray (Finding Gray code) {: #finding-gray-code}

Hãy xem xét các bit của số $n$ và các bit của số $G(n)$. Lưu ý rằng bit thứ $i$ của $G(n)$ bằng 1 chỉ khi bit thứ $i$ của $n$ bằng 1 và bit thứ $i + 1$ bằng 0 hoặc ngược lại (bit thứ $i$ bằng 0 và bit thứ $i + 1$ bằng 1). Do đó, $G(n) = n \oplus (n >> 1)$:  

```cpp
int g (int n) {
    return n ^ (n >> 1);
}
```

## Tìm mã Gray ngược (Finding inverse Gray code) {: #finding-inverse-gray-code}

Cho mã Gray $g$, khôi phục số ban đầu $n$.

Chúng ta sẽ di chuyển từ các bit quan trọng nhất (most significant bits) đến các bit ít quan trọng nhất (least significant bits) (bit ít quan trọng nhất có chỉ số 1 và bit quan trọng nhất có chỉ số $k$). Quan hệ giữa các bit $n_i$ của số $n$ và các bit $g_i$ của số $g$:

$$\begin{align}
  n_k &= g_k, \\
  n_{k-1} &= g_{k-1} \oplus n_k = g_k \oplus g_{k-1}, \\
  n_{k-2} &= g_{k-2} \oplus n_{k-1} = g_k \oplus g_{k-1} \oplus g_{k-2}, \\
  n_{k-3} &= g_{k-3} \oplus n_{k-2} = g_k \oplus g_{k-1} \oplus g_{k-2} \oplus g_{k-3},
  \vdots
\end{align}$$

Cách dễ nhất để viết nó trong mã là:

```cpp
int rev_g (int g) {
  int n = 0;
  for (; g; g >>= 1)
    n ^= g;
  return n;
}
```

## Các ứng dụng thực tế (Practical applications) {: #practical-applications}
Mã Gray có một số ứng dụng hữu ích, đôi khi khá bất ngờ:

*   Mã Gray của $n$ bit tạo thành một chu trình Hamilton trên một siêu lập phương (hypercube), trong đó mỗi bit tương ứng với một chiều. 

*   Mã Gray được sử dụng để giảm thiểu lỗi trong chuyển đổi tín hiệu số sang tương tự (ví dụ, trong các cảm biến). 

*   Mã Gray có thể được sử dụng để giải bài toán Tháp Hà Nội.
    Gọi $n$ là số lượng đĩa. Bắt đầu với mã Gray có độ dài $n$ bao gồm tất cả các số không ($G(0)$) và di chuyển giữa các mã Gray liên tiếp (từ $G(i)$ đến $G(i+1)$).
    Gọi bit thứ $i$ của mã Gray hiện tại đại diện cho đĩa thứ $n$ 
    (bit ít quan trọng nhất tương ứng với đĩa nhỏ nhất và bit quan trọng nhất với đĩa lớn nhất). 
    Vì chính xác một bit thay đổi trong mỗi bước, chúng ta có thể coi việc thay đổi bit thứ $i$ là di chuyển đĩa thứ $i$.
    Lưu ý rằng có chính xác một tùy chọn di chuyển cho mỗi đĩa (ngoại trừ đĩa nhỏ nhất) trong mỗi bước (ngoại trừ vị trí bắt đầu và kết thúc).
    Luôn có hai tùy chọn di chuyển cho đĩa nhỏ nhất nhưng có một chiến lược sẽ luôn dẫn đến câu trả lời:
    nếu $n$ là lẻ thì chuỗi các lần di chuyển đĩa nhỏ nhất trông giống như $f \to t \to r \to f \to t \to r \to ...$
    trong đó $f$ là cọc ban đầu, $t$ là cọc đích và $r$ là cọc còn lại), và 
    nếu $n$ là chẵn: $f \to r \to t \to f \to r \to t \to ...$.

*   Mã Gray cũng được sử dụng trong lý thuyết thuật toán di truyền.


## Bài tập luyện tập {: #practice-problems}
*   <a href="https://cses.fi/problemset/task/2205">Gray Code &nbsp;&nbsp;&nbsp;&nbsp; [Difficulty: easy]</a>
*   <a href="http://codeforces.com/problemsets/acmsguru/problem/99999/249">SGU #249 <b>"Matrix"</b> &nbsp;&nbsp;&nbsp;&nbsp; [Difficulty: medium]</a>

---

## Checklist

- Original lines: 75
- Translated lines: 75
- Code blocks changed? No
- Inline code changed? No
- Technical terms kept in English? Yes
- Headings anchors preserved/added correctly? Yes
- I confirm no character was omitted: YES
