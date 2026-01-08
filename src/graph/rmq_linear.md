---
tags:
  - Translated
e_maxx_link: rmq_linear
---

# Giải RMQ (Truy vấn giá trị nhỏ nhất trong phạm vi) bằng cách tìm LCA (Tổ tiên chung thấp nhất) (Solve RMQ (Range Minimum Query) by finding LCA (Lowest Common Ancestor)) {: #solve-rmq-range-minimum-query-by-finding-lca-lowest-common-ancestor}

Cho một mảng `A[0..N-1]`.
Đối với mỗi truy vấn có dạng `[L, R]`, chúng ta muốn tìm giá trị nhỏ nhất trong mảng `A` bắt đầu từ vị trí `L` và kết thúc bằng vị trí `R`.
Chúng ta sẽ giả định rằng mảng `A` không thay đổi trong quá trình, tức là bài viết này mô tả một giải pháp cho bài toán RMQ tĩnh.

Dưới đây là mô tả về một giải pháp tối ưu tiệm cận.
Nó đứng tách biệt với các giải pháp khác cho bài toán RMQ, vì nó rất khác biệt với chúng:
nó quy giảm bài toán RMQ thành bài toán LCA, và sau đó sử dụng [thuật toán Farach-Colton và Bender](lca_farachcoltonbender.md), vốn quy giảm bài toán LCA trở lại thành một bài toán RMQ chuyên biệt và giải quyết nó.

## Thuật toán (Algorithm) {: #algorithm}

Chúng ta xây dựng một **cây Cartesian** từ mảng `A`.
Cây Cartesian của một mảng `A` là một cây nhị phân có thuộc tính min-heap (giá trị của nút cha phải nhỏ hơn hoặc bằng giá trị của các con của nó) sao cho việc duyệt cây theo thứ tự giữa (in-order traversal) sẽ thăm các nút theo cùng thứ tự như chúng nằm trong mảng `A`.

Nói cách khác, cây Cartesian là một cấu trúc dữ liệu đệ quy.
Mảng `A` sẽ được phân chia thành 3 phần: tiền tố của mảng cho đến giá trị nhỏ nhất, giá trị nhỏ nhất, và hậu tố còn lại.
Gốc của cây sẽ là một nút tương ứng với phần tử nhỏ nhất của mảng `A`, cây con bên trái sẽ là cây Cartesian của tiền tố, và cây con bên phải sẽ là cây Cartesian của hậu tố.

Trong hình ảnh sau đây, bạn có thể thấy một mảng có độ dài 10 và cây Cartesian tương ứng.
<div style="text-align: center;">
  <img src="CartesianTree.png" alt="Image of Cartesian Tree">
</div>

Truy vấn giá trị nhỏ nhất trong phạm vi `[l, r]` tương đương với truy vấn tổ tiên chung thấp nhất `[l', r']`, trong đó `l'` là nút tương ứng với phần tử `A[l]` và `r'` là nút tương ứng với phần tử `A[r]`.
Thật vậy, nút tương ứng với phần tử nhỏ nhất trong phạm vi phải là tổ tiên của tất cả các nút trong phạm vi, do đó cũng từ `l'` và `r'`.
Điều này tự động theo sau từ thuộc tính min-heap.
Và nó cũng phải là tổ tiên thấp nhất, bởi vì nếu không `l'` và `r'` sẽ đều ở trong cây con bên trái hoặc bên phải, điều này tạo ra một mâu thuẫn vì trong trường hợp như vậy giá trị nhỏ nhất thậm chí sẽ không nằm trong phạm vi.

Trong hình ảnh sau đây, bạn có thể thấy các truy vấn LCA cho các truy vấn RMQ `[1, 3]` và `[5, 9]`.
Trong truy vấn đầu tiên, LCA của các nút `A[1]` và `A[3]` là nút tương ứng với `A[2]` có giá trị 2, và trong truy vấn thứ hai, LCA của `A[5]` và `A[9]` là nút tương ứng với `A[8]` có giá trị 3.
<div style="text-align: center;">
  <img src="CartesianTreeLCA.png" alt="LCA queries in the Cartesian Tree">
</div>

Một cây như vậy có thể được xây dựng trong thời gian $O(N)$ và thuật toán Farach-Colton và Bender có thể tiền xử lý cây trong $O(N)$ và tìm LCA trong $O(1)$.

## Xây dựng cây Cartesian (Construction of a Cartesian tree) {: #construction-of-a-cartesian-tree}

Chúng ta sẽ xây dựng cây Cartesian bằng cách thêm các phần tử lần lượt từng cái một.
Trong mỗi bước, chúng ta duy trì một cây Cartesian hợp lệ của tất cả các phần tử đã xử lý.
Dễ dàng thấy rằng, việc thêm một phần tử `s[i]` chỉ có thể thay đổi các nút trong đường đi ngoài cùng bên phải - bắt đầu từ gốc và lặp đi lặp lại việc lấy con bên phải - của cây.
Cây con của nút có giá trị nhỏ nhất, nhưng lớn hơn hoặc bằng `s[i]`, trở thành cây con bên trái của `s[i]`, và cây có gốc `s[i]` sẽ trở thành cây con bên phải mới của nút có giá trị lớn nhất, nhưng nhỏ hơn `s[i]`.

Điều này có thể được cài đặt bằng cách sử dụng một ngăn xếp để lưu trữ các chỉ số của các nút ngoài cùng bên phải.

```cpp
vector<int> parent(n, -1);
stack<int> s;
for (int i = 0; i < n; i++) {
    int last = -1;
    while (!s.empty() && A[s.top()] >= A[i]) {
        last = s.top();
        s.pop();
    }
    if (!s.empty())
        parent[i] = s.top();
    if (last >= 0)
        parent[last] = i;
    s.push(i);
}
```
