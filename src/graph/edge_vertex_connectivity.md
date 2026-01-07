--- 
tags:
  - Translated
e_maxx_link:
  - rib_connectivity
  - vertex_connectivity
---

# Liên thông cạnh / Liên thông đỉnh

## Định nghĩa

Cho một đồ thị vô hướng $G$ với $n$ đỉnh và $m$ cạnh.
Cả liên thông cạnh và liên thông đỉnh đều là các đặc tính mô tả đồ thị.

### Liên thông cạnh

**Liên thông cạnh** $\lambda$ của đồ thị $G$ là số cạnh tối thiểu cần phải xóa để đồ thị $G$ bị ngắt kết nối.

Ví dụ, một đồ thị đã bị ngắt kết nối có liên thông cạnh là $0$, một đồ thị liên thông có ít nhất một cầu có liên thông cạnh là $1$, và một đồ thị liên thông không có cầu có liên thông cạnh ít nhất là $2$.

Chúng ta nói rằng một tập hợp các cạnh $S$ **chia tách** các đỉnh $s$ và $t$, nếu sau khi xóa tất cả các cạnh trong $S$ khỏi đồ thị $G$, các đỉnh $s$ và $t$ nằm trong các thành phần liên thông khác nhau.

Rõ ràng, liên thông cạnh của một đồ thị bằng kích thước tối thiểu của một tập hợp như vậy chia tách hai đỉnh $s$ và $t$, được lấy trên tất cả các cặp có thể có $(s, t)$.

### Liên thông đỉnh

**Liên thông đỉnh** $\kappa$ của đồ thị $G$ là số đỉnh tối thiểu cần phải xóa để đồ thị $G$ bị ngắt kết nối.

Ví dụ, một đồ thị đã bị ngắt kết nối có liên thông đỉnh là $0$, và một đồ thị liên thông có một điểm khớp có liên thông đỉnh là $1$.
Chúng ta định nghĩa rằng một đồ thị đầy đủ có liên thông đỉnh là $n-1$.
Đối với tất cả các đồ thị khác, liên thông đỉnh không vượt quá $n-2$, vì bạn có thể tìm thấy một cặp đỉnh không được nối bằng một cạnh, và xóa tất cả $n-2$ đỉnh khác.

Chúng ta nói rằng một tập hợp các đỉnh $T$ **chia tách** các đỉnh $s$ và $t$, nếu sau khi xóa tất cả các đỉnh trong $T$ khỏi đồ thị $G$, các đỉnh nằm trong các thành phần liên thông khác nhau.

Rõ ràng, liên thông đỉnh của một đồ thị bằng kích thước tối thiểu của một tập hợp như vậy chia tách hai đỉnh $s$ và $t$, được lấy trên tất cả các cặp có thể có $(s, t)$.

## Các tính chất

### Bất đẳng thức Whitney

**Bất đẳng thức Whitney** (1932) đưa ra một mối quan hệ giữa liên thông cạnh $\lambda$, liên thông đỉnh $\kappa$, và bậc tối thiểu của bất kỳ đỉnh nào trong đồ thị $\delta$:

$$\kappa \le \lambda \le \delta$$

Một cách trực quan, nếu chúng ta có một tập hợp các cạnh có kích thước $\lambda$, làm cho đồ thị bị ngắt kết nối, chúng ta có thể chọn một trong mỗi điểm cuối, và tạo ra một tập hợp các đỉnh, cũng làm cho đồ thị bị ngắt kết nối.
Và tập hợp này có kích thước $\le \lambda$.

Và nếu chúng ta chọn đỉnh có bậc tối thiểu $\delta$, và xóa tất cả các cạnh nối với nó, thì chúng ta cũng sẽ có một đồ thị bị ngắt kết nối.
Do đó, bất đẳng thức thứ hai là $\lambda \le \delta$.

Điều thú vị cần lưu ý là, bất đẳng thức Whitney không thể được cải thiện:
tức là, với bất kỳ bộ ba số nào thỏa mãn bất đẳng thức này đều tồn tại ít nhất một đồ thị tương ứng.
Một đồ thị như vậy có thể được xây dựng theo cách sau:
Đồ thị sẽ bao gồm $2(\delta + 1)$ đỉnh, $\delta + 1$ đỉnh đầu tiên tạo thành một clique (tất cả các cặp đỉnh được nối với nhau bằng một cạnh), và $\delta + 1$ đỉnh thứ hai tạo thành một clique thứ hai.
Ngoài ra, chúng ta nối hai clique bằng $\lambda$ cạnh, sao cho nó sử dụng $\lambda$ đỉnh khác nhau trong clique thứ nhất, và chỉ $\kappa$ đỉnh trong clique thứ hai.
Đồ thị kết quả sẽ có ba đặc tính này.

### Định lý Ford-Fulkerson

**Định lý Ford-Fulkerson** ngụ ý rằng, số lượng lớn nhất các đường đi không giao nhau về cạnh nối hai đỉnh, bằng với số lượng nhỏ nhất các cạnh chia tách hai đỉnh này.

## Tính toán các giá trị

### Liên thông cạnh sử dụng luồng cực đại

Phương pháp này dựa trên định lý Ford-Fulkerson.

Chúng ta lặp qua tất cả các cặp đỉnh $(s, t)$ và giữa mỗi cặp, chúng ta tìm số lượng lớn nhất các đường đi không giao nhau giữa chúng.
Giá trị này có thể được tìm thấy bằng thuật toán luồng cực đại:
chúng ta sử dụng $s$ làm nguồn, $t$ làm đích, và gán cho mỗi cạnh một khả năng thông qua là $1$.
Khi đó luồng cực đại là số lượng các đường đi không giao nhau.

Độ phức tạp của thuật toán sử dụng [Edmonds-Karp](../graph/edmonds_karp.md) là $O(V^2 V E^2) = O(V^3 E^2)$. 
Nhưng chúng ta nên lưu ý rằng, điều này bao gồm một yếu tố ẩn, vì thực tế không thể tạo ra một đồ thị sao cho thuật toán luồng cực đại sẽ chậm cho tất cả các nguồn và đích.
Đặc biệt, thuật toán sẽ chạy khá nhanh trên các đồ thị ngẫu nhiên.

### Thuật toán đặc biệt cho liên thông cạnh 

Nhiệm vụ tìm liên thông cạnh tương đương với nhiệm vụ tìm **lát cắt tối thiểu toàn cục**.

Các thuật toán đặc biệt đã được phát triển cho nhiệm vụ này.
Một trong số đó là thuật toán Stoer-Wagner, hoạt động trong thời gian $O(V^3)$ hoặc $O(V E)$.

### Liên thông đỉnh

Một lần nữa, chúng ta lặp qua tất cả các cặp đỉnh $s$ và $t$, và với mỗi cặp, chúng ta tìm số lượng đỉnh tối thiểu chia tách $s$ và $t$.

Bằng cách làm này, chúng ta có thể áp dụng cùng một phương pháp luồng cực đại như đã mô tả trong các phần trước.

Chúng ta chia mỗi đỉnh $x$ với $x \neq s$ và $x \neq t$ thành hai đỉnh $x_1$ và $x_2$.
Chúng ta nối hai đỉnh này bằng một cạnh có hướng $(x_1, x_2)$ với khả năng thông qua là $1$, và thay thế tất cả các cạnh $(u, v)$ bằng hai cạnh có hướng $(u_2, v_1)$ và $(v_2, u_1)$, cả hai đều có khả năng thông qua là 1.
Theo cấu trúc, giá trị của luồng cực đại sẽ bằng số lượng đỉnh tối thiểu cần thiết để chia tách $s$ và $t$.

Phương pháp này có cùng độ phức tạp với phương pháp luồng để tìm liên thông cạnh.