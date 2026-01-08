---
tags:
  - Translated
e_maxx_link: counting_connected_graphs
---

# Đếm đồ thị có nhãn (Counting labeled graphs) {: #counting-labeled-graphs}

## Đồ thị có nhãn (Labeled graphs) {: #labeled-graphs}

Gọi số đỉnh trong một đồ thị là $n$.
Chúng ta phải tính số $G_n$ các đồ thị có nhãn với $n$ đỉnh (có nhãn có nghĩa là các đỉnh được đánh dấu bằng các số từ $1$ đến $n$).
Các cạnh của đồ thị được coi là vô hướng, và các vòng lặp (loops) và đa cạnh (multiple edges) bị cấm.

Chúng ta xem xét tập hợp tất cả các cạnh có thể của đồ thị.
Đối với mỗi cạnh $(i, j)$ chúng ta có thể giả định rằng $i < j$ (vì đồ thị là vô hướng, và không có vòng lặp).
Do đó tập hợp tất cả các cạnh có lực lượng $\binom{n}{2}$, tức là $\frac{n(n-1)}{2}$.

Vì bất kỳ đồ thị có nhãn nào cũng được xác định duy nhất bởi các cạnh của nó, số lượng đồ thị có nhãn với $n$ đỉnh bằng:

$$G_n = 2^{\frac{n(n-1)}{2}}$$

## Đồ thị có nhãn liên thông (Connected labeled graphs) {: #connected-labeled-graphs}

Ở đây, chúng ta áp đặt thêm hạn chế rằng đồ thị phải liên thông.

Hãy ký hiệu số lượng đồ thị liên thông cần thiết với $n$ đỉnh là $C_n$.

Đầu tiên chúng ta sẽ thảo luận xem có bao nhiêu đồ thị **không liên thông** tồn tại.
Khi đó số lượng đồ thị liên thông sẽ là $G_n$ trừ đi số lượng đồ thị không liên thông.
Thậm chí nhiều hơn, chúng ta sẽ đếm số lượng **đồ thị không liên thông, có gốc**. Một đồ thị có gốc là một đồ thị, trong đó chúng ta nhấn mạnh một đỉnh bằng cách dán nhãn nó là gốc.
Rõ ràng chúng ta có $n$ khả năng để root một đồ thị với $n$ đỉnh có nhãn, do đó chúng ta sẽ cần chia số lượng đồ thị không liên thông có gốc cho $n$ ở cuối để có được số lượng đồ thị không liên thông.

Đỉnh gốc sẽ xuất hiện trong một thành phần liên thông có kích thước $1, \dots n-1$.
Có $k \binom{n}{k} C_k G_{n-k}$ đồ thị sao cho đỉnh gốc nằm trong một thành phần liên thông với $k$ đỉnh (có $\binom{n}{k}$ cách để chọn $k$ đỉnh cho thành phần, những đỉnh này được kết nối theo một trong $C_k$ cách, đỉnh gốc có thể là bất kỳ đỉnh nào trong số $k$ đỉnh, và $n-k$ đỉnh còn lại có thể được kết nối/không kết nối theo bất kỳ cách nào, điều này mang lại một yếu tố $G_{n-k}$).
Do đó số lượng đồ thị không liên thông với $n$ đỉnh là:

$$\frac{1}{n} \sum_{k=1}^{n-1} k \binom{n}{k} C_k G_{n-k}$$

Và cuối cùng số lượng đồ thị liên thông là:

$$C_n = G_n - \frac{1}{n} \sum_{k=1}^{n-1} k \binom{n}{k} C_k G_{n-k}$$

## Đồ thị có nhãn với $k$ thành phần liên thông (Labeled graphs with $k$ connected components) {: #labeled-graphs-with-k-connected-components data-toc-label="Labeled graphs with k connected components"}

Dựa trên công thức từ phần trước, chúng ta sẽ học cách đếm số lượng đồ thị có nhãn với $n$ đỉnh và $k$ thành phần liên thông.

Số này có thể được tính bằng cách sử dụng quy hoạch động.
Chúng ta sẽ tính $D[i][j]$ - số lượng đồ thị có nhãn với $i$ đỉnh và $j$ thành phần - cho mỗi $i \le n$ và $j \le k$.

Hãy thảo luận về cách tính phần tử tiếp theo $D[n][k]$ nếu chúng ta đã biết các giá trị trước đó.
Chúng ta sử dụng một cách tiếp cận phổ biến, chúng ta lấy đỉnh cuối cùng (chỉ số $n$).
Đỉnh này thuộc về một thành phần nào đó.
Nếu kích thước của thành phần này là $s$, thì có $\binom{n-1}{s-1}$ cách để chọn một tập hợp các đỉnh như vậy, và $C_s$ cách để kết nối chúng. Sau khi loại bỏ thành phần này khỏi đồ thị, chúng ta có $n-s$ đỉnh còn lại với $k-1$ thành phần liên thông.
Do đó chúng ta thu được quan hệ truy hồi sau:

$$D[n][k] = \sum_{s=1}^{n} \binom{n-1}{s-1} C_s D[n-s][k-1]$$

---

## Checklist

- Original lines: 58
- Translated lines: 58
- Code blocks changed? No
- Inline code changed? No
- Technical terms kept in English? Yes
- Headings anchors preserved/added correctly? Yes
- I confirm no character was omitted: YES
