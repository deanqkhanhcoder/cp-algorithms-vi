---
tags:
  - Translated
e_maxx_link:
  - rib_connectivity
  - vertex_connectivity
---

# Độ liên thông cạnh / Độ liên thông đỉnh (Edge connectivity / Vertex connectivity) {: #edge-connectivity-vertex-connectivity}

## Định nghĩa (Definition) {: #definition}

Cho một đồ thị vô hướng $G$ với $n$ đỉnh và $m$ cạnh.
Cả độ liên thông cạnh và độ liên thông đỉnh đều là các đặc điểm mô tả đồ thị.

### Độ liên thông cạnh (Edge connectivity) {: #edge-connectivity}

**Độ liên thông cạnh** $\lambda$ của đồ thị $G$ là số lượng cạnh tối thiểu cần phải xóa, sao cho đồ thị $G$ bị mất liên thông.

Ví dụ, một đồ thị đã mất liên thông có độ liên thông cạnh là $0$, một đồ thị liên thông có ít nhất một cầu có độ liên thông cạnh là $1$, và một đồ thị liên thông không có cầu có độ liên thông cạnh ít nhất là $2$.

Chúng ta nói rằng một tập hợp $S$ các cạnh **phân tách** các đỉnh $s$ và $t$, nếu, sau khi loại bỏ tất cả các cạnh trong $S$ khỏi đồ thị $G$, các đỉnh $s$ và $t$ nằm trong các thành phần liên thông khác nhau.

Rõ ràng là, độ liên thông cạnh của một đồ thị bằng kích thước tối thiểu của một tập hợp như vậy phân tách hai đỉnh $s$ và $t$, được lấy trong số tất cả các cặp $(s, t)$ có thể.

### Độ liên thông đỉnh (Vertex connectivity) {: #vertex-connectivity}

**Độ liên thông đỉnh** $\kappa$ của đồ thị $G$ là số lượng đỉnh tối thiểu cần phải xóa, sao cho đồ thị $G$ bị mất liên thông.

Ví dụ, một đồ thị đã mất liên thông có độ liên thông đỉnh là $0$, và một đồ thị liên thông có một khớp có độ liên thông đỉnh là $1$.
Chúng ta định nghĩa rằng một đồ thị đầy đủ có độ liên thông đỉnh là $n-1$.
Đối với tất cả các đồ thị khác, độ liên thông đỉnh không vượt quá $n-2$, vì bạn có thể tìm thấy một cặp đỉnh không được nối với nhau bằng một cạnh và loại bỏ tất cả $n-2$ đỉnh khác.

Chúng ta nói rằng một tập hợp $T$ các đỉnh **phân tách** các đỉnh $s$ và $t$, nếu, sau khi loại bỏ tất cả các đỉnh trong $T$ khỏi đồ thị $G$, các đỉnh nằm trong các thành phần liên thông khác nhau.

Rõ ràng là, độ liên thông đỉnh của một đồ thị bằng kích thước tối thiểu của một tập hợp như vậy phân tách hai đỉnh $s$ và $t$, được lấy trong số tất cả các cặp $(s, t)$ có thể.

## Tính chất (Properties) {: #properties}

### Bất đẳng thức Whitney (The Whitney inequalities) {: #the-whitney-inequalities}

**Bất đẳng thức Whitney** (1932) đưa ra mối quan hệ giữa độ liên thông cạnh $\lambda$, độ liên thông đỉnh $\kappa$ và bậc nhỏ nhất của bất kỳ đỉnh nào trong đồ thị $\delta$:

$$\kappa \le \lambda \le \delta$$

Về mặt trực giác, nếu chúng ta có một tập hợp các cạnh có kích thước $\lambda$, làm cho đồ thị mất liên thông, chúng ta có thể chọn một trong mỗi điểm cuối, và tạo ra một tập hợp các đỉnh, cũng làm mất liên thông đồ thị.
Và tập hợp này có kích thước $\le \lambda$.

Và nếu chúng ta chọn đỉnh và bậc tối thiểu $\delta$, và loại bỏ tất cả các cạnh được nối với nó, thì chúng ta cũng sẽ có một đồ thị mất liên thông.
Do đó bất đẳng thức thứ hai $\lambda \le \delta$.

Thật thú vị khi lưu ý rằng các bất đẳng thức Whitney không thể được cải thiện:
tức là đối với bất kỳ bộ ba số nào thỏa mãn bất đẳng thức này, tồn tại ít nhất một đồ thị tương ứng.
Một đồ thị như vậy có thể được xây dựng theo cách sau:
Đồ thị sẽ bao gồm $2(\delta + 1)$ đỉnh, $\delta + 1$ đỉnh đầu tiên tạo thành một clique (tất cả các cặp đỉnh được nối với nhau qua một cạnh), và $\delta + 1$ đỉnh thứ hai tạo thành một clique thứ hai.
Ngoài ra, chúng ta kết nối hai clique bằng $\lambda$ cạnh, sao cho nó sử dụng $\lambda$ đỉnh khác nhau trong clique đầu tiên, và chỉ $\kappa$ đỉnh trong clique thứ hai.
Đồ thị kết quả sẽ có ba đặc điểm.

### Định lý Ford-Fulkerson (The Ford-Fulkerson theorem) {: #the-ford-fulkerson-theorem}

**Định lý Ford-Fulkerson** ngụ ý rằng, số lượng lớn nhất các đường đi không giao nhau về cạnh kết nối hai đỉnh, bằng số lượng nhỏ nhất các cạnh phân tách các đỉnh này.

## Tính toán các giá trị (Computing the values) {: #computing-the-values}

### Độ liên thông cạnh sử dụng luồng cực đại (Edge connectivity using maximum flow) {: #edge-connectivity-using-maximum-flow}

Phương pháp này dựa trên định lý Ford-Fulkerson.

Chúng ta lặp qua tất cả các cặp đỉnh $(s, t)$ và giữa mỗi cặp, chúng ta tìm số lượng lớn nhất các đường đi không giao nhau giữa chúng.
Giá trị này có thể được tìm thấy bằng cách sử dụng thuật toán luồng cực đại:
chúng ta sử dụng $s$ làm nguồn, $t$ làm đích, và gán cho mỗi cạnh một dung lượng là $1$.
Sau đó, luồng cực đại là số lượng đường đi không giao nhau.

Độ phức tạp cho thuật toán sử dụng [Edmonds-Karp](../graph/edmonds_karp.md) là $O(V^2 V E^2) = O(V^3 E^2)$.
Nhưng chúng ta nên lưu ý rằng, điều này bao gồm một yếu tố ẩn, vì thực tế không thể tạo ra một đồ thị sao cho thuật toán luồng cực đại sẽ chậm cho tất cả các nguồn và đích.
Đặc biệt thuật toán sẽ chạy khá nhanh đối với các đồ thị ngẫu nhiên.

### Thuật toán đặc biệt cho độ liên thông cạnh (Special algorithm for edge connectivity) {: #special-algorithm-for-edge-connectivity}

Nhiệm vụ tìm độ liên thông cạnh tương đương với nhiệm vụ tìm **lát cắt cực tiểu toàn cục** (global minimum cut).

Các thuật toán đặc biệt đã được phát triển cho nhiệm vụ này.
Một trong số đó là thuật toán Stoer-Wagner, hoạt động trong thời gian $O(V^3)$ hoặc $O(V E)$.

### Độ liên thông đỉnh (Vertex connectivity) {: #vertex-connectivity-1}

Một lần nữa chúng ta lặp qua tất cả các cặp đỉnh $s$ và $t$, và đối với mỗi cặp, chúng ta tìm số lượng đỉnh tối thiểu phân tách $s$ và $t$.

Bằng cách làm điều này, chúng ta có thể áp dụng cùng một cách tiếp cận luồng cực đại như được mô tả trong các phần trước.

Chúng ta chia mỗi đỉnh $x$ với $x \neq s$ và $x \neq t$ thành hai đỉnh $x_1$ và $x_2$.
Chúng ta kết nối hai đỉnh này bằng một cạnh có hướng $(x_1, x_2)$ với dung lượng $1$, và thay thế tất cả các cạnh $(u, v)$ bằng hai cạnh có hướng $(u_2, v_1)$ và $(v_2, u_1)$, cả hai đều có dung lượng là 1.
Bằng cách xây dựng, giá trị của luồng cực đại sẽ bằng số lượng đỉnh tối thiểu cần thiết để phân tách $s$ và $t$.

Cách tiếp cận này có cùng độ phức tạp như cách tiếp cận luồng để tìm độ liên thông cạnh.
