---
tags:
  - Translated
e_maxx_link: counting_connected_graphs
---

# Đếm đồ thị có nhãn

## Đồ thị có nhãn

Cho số đỉnh của một đồ thị là $n$.
Chúng ta phải tính số lượng $G_n$ của các đồ thị có nhãn với $n$ đỉnh (có nhãn có nghĩa là các đỉnh được đánh dấu bằng các số từ $1$ đến $n$).
Các cạnh của đồ thị được coi là vô hướng, và không cho phép khuyên và cạnh bội.

Chúng ta xét tập hợp tất cả các cạnh có thể có của đồ thị.
Đối với mỗi cạnh $(i, j)$ chúng ta có thể giả sử rằng $i < j$ (vì đồ thị là vô hướng và không có khuyên).
Do đó, tập hợp tất cả các cạnh có lực lượng là $\binom{n}{2}$, tức là $\frac{n(n-1)}{2}$.

Vì bất kỳ đồ thị có nhãn nào cũng được xác định duy nhất bởi các cạnh của nó, số lượng các đồ thị có nhãn với $n$ đỉnh bằng:

$$G_n = 2^{\frac{n(n-1)}{2}}$$

## Đồ thị có nhãn liên thông

Ở đây, chúng ta thêm vào ràng buộc rằng đồ thị phải liên thông.

Hãy ký hiệu số lượng các đồ thị liên thông cần tìm với $n$ đỉnh là $C_n$.

Trước tiên, chúng ta sẽ thảo luận có bao nhiêu đồ thị **không liên thông** tồn tại.
Sau đó, số lượng các đồ thị liên thông sẽ là $G_n$ trừ đi số lượng các đồ thị không liên thông.
Hơn nữa, chúng ta sẽ đếm số lượng các **đồ thị có gốc, không liên thông**. Một đồ thị có gốc là một đồ thị, trong đó chúng ta nhấn mạnh một đỉnh bằng cách gán nhãn cho nó là gốc.
Rõ ràng là chúng ta có $n$ khả năng để đặt gốc cho một đồ thị có $n$ đỉnh được gán nhãn, do đó chúng ta sẽ cần phải chia số lượng các đồ thị có gốc không liên thông cho $n$ ở cuối để có được số lượng các đồ thị không liên thông.

Đỉnh gốc sẽ xuất hiện trong một thành phần liên thông có kích thước $1, \dots n-1$.
Có $k \binom{n}{k} C_k G_{n-k}$ đồ thị sao cho đỉnh gốc nằm trong một thành phần liên thông với $k$ đỉnh (có $\binom{n}{k}$ cách để chọn $k$ đỉnh cho thành phần, chúng được kết nối theo một trong $C_k$ cách, đỉnh gốc có thể là bất kỳ trong số $k$ đỉnh, và $n-k$ đỉnh còn lại có thể được kết nối/không kết nối theo bất kỳ cách nào, điều này cho một hệ số $G_{n-k}$).
Do đó, số lượng các đồ thị không liên thông với $n$ đỉnh là:

$$\frac{1}{n} \sum_{k=1}^{n-1} k \binom{n}{k} C_k G_{n-k}$$

Và cuối cùng, số lượng các đồ thị liên thông là:

$$C_n = G_n - \frac{1}{n} \sum_{k=1}^{n-1} k \binom{n}{k} C_k G_{n-k}$$

## Đồ thị có nhãn với $k$ thành phần liên thông {data-toc-label="Labeled graphs with k connected components"}

Dựa trên công thức từ phần trước, chúng ta sẽ học cách đếm số lượng các đồ thị có nhãn với $n$ đỉnh và $k$ thành phần liên thông.

Số này có thể được tính bằng quy hoạch động.
Chúng ta sẽ tính $D[i][j]$ - số lượng các đồ thị có nhãn với $i$ đỉnh và $j$ thành phần - cho mỗi $i \le n$ và $j \le k$.

Hãy thảo luận cách tính phần tử tiếp theo $D[n][k]$ nếu chúng ta đã biết các giá trị trước đó.
Chúng ta sử dụng một cách tiếp cận phổ biến, chúng ta lấy đỉnh cuối cùng (chỉ số $n$).
Đỉnh này thuộc về một thành phần nào đó.
Nếu kích thước của thành phần này là $s$, thì có $\binom{n-1}{s-1}$ cách để chọn một tập hợp các đỉnh như vậy, và $C_s$ cách để kết nối chúng. Sau khi loại bỏ thành phần này khỏi đồ thị, chúng ta còn lại $n-s$ đỉnh với $k-1$ thành phần liên thông.
Do đó, chúng ta có được quan hệ truy hồi sau:

$$D[n][k] = \sum_{s=1}^{n} \binom{n-1}{s-1} C_s D[n-s][k-1]$$