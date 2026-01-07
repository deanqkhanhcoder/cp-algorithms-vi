---
tags:
  - Translated
e_maxx_link: fixed_length_paths
---

# Số lượng đường đi có độ dài cố định / Đường đi ngắn nhất có độ dài cố định

Bài viết sau đây mô tả các giải pháp cho hai bài toán này được xây dựng trên cùng một ý tưởng:
quy bài toán về việc xây dựng ma trận và tính toán giải pháp bằng phép nhân ma trận thông thường hoặc bằng một phép nhân được sửa đổi.

## Số lượng đường đi có độ dài cố định

Chúng ta được cho một đồ thị có hướng, không trọng số $G$ với $n$ đỉnh và một số nguyên $k$.
Nhiệm vụ như sau:
với mỗi cặp đỉnh $(i, j)$, chúng ta phải tìm số lượng đường đi có độ dài $k$ giữa các đỉnh này.
Các đường đi không cần phải đơn giản, tức là các đỉnh và các cạnh có thể được thăm bất kỳ số lần nào trong một đường đi duy nhất.

Chúng ta giả định rằng đồ thị được chỉ định bằng một ma trận kề, tức là ma trận $G[][]$ kích thước $n \times n$, trong đó mỗi phần tử $G[i][j]$ bằng $1$ nếu đỉnh $i$ được nối với $j$ bằng một cạnh, và $0$ nếu chúng không được nối bằng một cạnh.
Thuật toán sau đây cũng hoạt động trong trường hợp có nhiều cạnh:
nếu một cặp đỉnh $(i, j)$ nào đó được nối với $m$ cạnh, thì chúng ta có thể ghi lại điều này trong ma trận kề bằng cách đặt $G[i][j] = m$.
Thuật toán cũng hoạt động nếu đồ thị chứa các vòng lặp (vòng lặp là một cạnh nối một đỉnh với chính nó).

Rõ ràng là ma trận kề được xây dựng là câu trả lời cho bài toán cho trường hợp $k = 1$.
Nó chứa số lượng đường đi có độ dài $1$ giữa mỗi cặp đỉnh.

Chúng ta sẽ xây dựng giải pháp một cách lặp đi lặp lại:
Giả sử chúng ta biết câu trả lời cho một $k$ nào đó.
Ở đây chúng ta mô tả một phương pháp làm thế nào chúng ta có thể xây dựng câu trả lời cho $k + 1$.
Ký hiệu $C_k$ là ma trận cho trường hợp $k$, và $C_{k+1}$ là ma trận chúng ta muốn xây dựng.
Với công thức sau, chúng ta có thể tính toán mọi mục của $C_{k+1}$:

$$C_{k+1}[i][j] = \sum_{p = 1}^{n} C_k[i][p] \cdot G[p][j]$$

Dễ thấy rằng công thức này không tính toán gì khác ngoài tích của các ma trận $C_k$ và $G$:

$$C_{k+1} = C_k \cdot G$$ 

Do đó, giải pháp của bài toán có thể được biểu diễn như sau:

$$C_k = \underbrace{G \cdot G \cdots G}_{k \text{ lần}} = G^k$$ 

Chỉ cần lưu ý rằng tích ma trận có thể được nâng lên một lũy thừa cao một cách hiệu quả bằng cách sử dụng [Lũy thừa nhị phân](../algebra/binary-exp.md).
Điều này cho một giải pháp với độ phức tạp $O(n^3 \log k)$.

## Đường đi ngắn nhất có độ dài cố định

Chúng ta được cho một đồ thị có hướng có trọng số $G$ với $n$ đỉnh và một số nguyên $k$.
Với mỗi cặp đỉnh $(i, j)$, chúng ta phải tìm độ dài của đường đi ngắn nhất giữa $i$ và $j$ bao gồm chính xác $k$ cạnh.

Chúng ta giả định rằng đồ thị được chỉ định bằng một ma trận kề, tức là thông qua ma trận $G[][]$ kích thước $n \times n$, trong đó mỗi phần tử $G[i][j]$ chứa độ dài của các cạnh từ đỉnh $i$ đến đỉnh $j$.
Nếu không có cạnh nào giữa hai đỉnh, thì phần tử tương ứng của ma trận sẽ được gán là vô cùng $\infty$.

Rõ ràng là ở dạng này, ma trận kề là câu trả lời cho bài toán cho $k = 1$.
Nó chứa độ dài của các đường đi ngắn nhất giữa mỗi cặp đỉnh, hoặc $\infty$ nếu không tồn tại đường đi bao gồm một cạnh.

Một lần nữa, chúng ta có thể xây dựng giải pháp cho bài toán một cách lặp đi lặp lại:
Giả sử chúng ta biết câu trả lời cho một $k$ nào đó.
Chúng ta chỉ ra cách chúng ta có thể tính toán câu trả lời cho $k+1$.
Hãy ký hiệu $L_k$ là ma trận cho $k$ và $L_{k+1}$ là ma trận chúng ta muốn xây dựng.
Khi đó, công thức sau tính toán mỗi mục của $L_{k+1}$:

$$L_{k+1}[i][j] = \min_{p = 1 \ldots n} \left(L_k[i][p] + G[p][j]\right)$$

Khi xem xét kỹ hơn công thức này, chúng ta có thể rút ra một sự tương tự với phép nhân ma trận:
thực tế ma trận $L_k$ được nhân với ma trận $G$, sự khác biệt duy nhất là thay vì trong phép nhân, chúng ta lấy giá trị nhỏ nhất thay vì tổng, và tổng thay vì phép nhân làm phép toán bên trong.

$$L_{k+1} = L_k \odot G,$$

trong đó phép toán $\odot$ được định nghĩa như sau:

$$A \odot B = C~~\Longleftrightarrow~~C_{i j} = \min_{p = 1 \ldots n}\left(A_{i p} + B_{p j}\right)$$

Do đó, giải pháp của nhiệm vụ có thể được biểu diễn bằng cách sử dụng phép nhân đã sửa đổi:

$$L_k = \underbrace{G \odot \ldots \odot G}_{k~\text{lần}} = G^{\odot k}$$

Chỉ cần lưu ý rằng chúng ta cũng có thể tính toán lũy thừa này một cách hiệu quả với [Lũy thừa nhị phân](../algebra/binary-exp.md), vì phép nhân đã sửa đổi rõ ràng là có tính kết hợp.
Vì vậy, giải pháp này cũng có độ phức tạp $O(n^3 \log k)$.

## Tổng quát hóa các bài toán cho các đường đi có độ dài lên tới $k$ {data-toc-label="Tổng quát hóa các bài toán cho các đường đi có độ dài lên tới k"}

Các giải pháp trên giải quyết các bài toán cho một $k$ cố định.
Tuy nhiên, các giải pháp có thể được điều chỉnh để giải quyết các bài toán cho phép các đường đi chứa không quá $k$ cạnh.

Điều này có thể được thực hiện bằng cách sửa đổi một chút đồ thị đầu vào.

Chúng ta nhân đôi mỗi đỉnh:
với mỗi đỉnh $v$, chúng ta tạo thêm một đỉnh $v'$ và thêm cạnh $(v, v')$ và vòng lặp $(v', v')$.
Số lượng đường đi giữa $i$ và $j$ có nhiều nhất $k$ cạnh bằng với số lượng đường đi giữa $i$ và $j'$ có chính xác $k + 1$ cạnh, vì có một song ánh ánh xạ mọi đường đi $[p_0 = i,~p_1,~\...~p_{m-1},~p_m = j]$ có độ dài $m \le k$ thành đường đi $[p_0 = i,~p_1,~\...~p_{m-1},~p_m = j, j', \ldots, j']$ có độ dài $k + 1$.

Thủ thuật tương tự có thể được áp dụng để tính toán các đường đi ngắn nhất có nhiều nhất $k$ cạnh.
Chúng ta lại nhân đôi mỗi đỉnh và thêm hai cạnh đã đề cập với trọng số $0$.