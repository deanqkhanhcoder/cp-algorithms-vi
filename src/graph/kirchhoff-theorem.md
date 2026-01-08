---
tags:
  - Translated
e_maxx_link: kirchhoff_theorem
---

# Định lý Kirchhoff. Tìm số lượng cây khung (Kirchhoff's theorem. Finding the number of spanning trees) {: #kirchhoffs-theorem-finding-the-number-of-spanning-trees}

Bài toán: Bạn được cho một đồ thị vô hướng liên thông (có thể có nhiều cạnh) được biểu diễn bằng ma trận kề. Tìm số lượng cây khung khác nhau của đồ thị này.

Công thức sau đây đã được chứng minh bởi Kirchhoff vào năm 1847.

## Định lý ma trận cây Kirchhoff (Kirchhoff's matrix tree theorem) {: #kirchhoffs-matrix-tree-theorem}

Gọi $A$ là ma trận kề của đồ thị: $A_{u,v}$ là số lượng cạnh giữa $u$ và $v$.
Gọi $D$ là ma trận bậc của đồ thị: một ma trận đường chéo với $D_{u,u}$ là bậc của đỉnh $u$ (bao gồm cả nhiều cạnh và vòng lặp - các cạnh nối đỉnh $u$ với chính nó).

Ma trận Laplacian của đồ thị được định nghĩa là $L = D - A$.
Theo định lý Kirchhoff, tất cả các phần bù đại số (cofactors) của ma trận này đều bằng nhau, và chúng bằng số lượng cây khung của đồ thị.
Phần bù đại số $(i,j)$ của một ma trận là tích của $(-1)^{i + j}$ với định thức của ma trận mà bạn nhận được sau khi loại bỏ hàng thứ $i$ và cột thứ $j$.
Vì vậy, bạn có thể, ví dụ, xóa hàng cuối cùng và cột cuối cùng của ma trận $L$, và giá trị tuyệt đối của định thức của ma trận kết quả sẽ cho bạn số lượng cây khung.

Định thức của ma trận có thể được tìm thấy trong $O(N^3)$ bằng cách sử dụng [phương pháp Gaussian](../linear_algebra/determinant-gauss.md).

Chứng minh định lý này khá khó và không được trình bày ở đây; để biết phác thảo chứng minh và các biến thể của định lý cho đồ thị không có nhiều cạnh và cho đồ thị có hướng, hãy tham khảo [Wikipedia](https://en.wikipedia.org/wiki/Kirchhoff%27s_theorem).

## Quan hệ với các định luật mạch Kirchhoff (Relation to Kirchhoff's circuit laws) {: #relation-to-kirchhoffs-circuit-laws}

Định lý ma trận cây Kirchhoff và các định luật Kirchhoff cho mạch điện có quan hệ theo một cách đẹp đẽ. Có thể chỉ ra (sử dụng định luật Ohm và định luật Kirchhoff thứ nhất) rằng điện trở $R_{ij}$ giữa hai điểm của mạch $i$ và $j$ là

$$R_{ij} = \frac{ \left| L^{(i,j)} \right| }{ | L^j | }.$$

Ở đây ma trận $L$ thu được từ ma trận điện trở nghịch đảo $A$ ($A_{i,j}$ là nghịch đảo của điện trở của dây dẫn giữa các điểm $i$ và $j$) bằng cách sử dụng quy trình được mô tả trong định lý ma trận cây Kirchhoff.
$T^j$ là ma trận với hàng và cột $j$ bị loại bỏ, $T^{(i,j)}$ là ma trận với hai hàng và hai cột $i$ và $j$ bị loại bỏ.

Định lý Kirchhoff mang lại cho công thức này ý nghĩa hình học.

## Bài tập (Practice Problems) {: #practice-problems}

 - [CODECHEF: Roads in Stars](https://www.codechef.com/problems/STARROAD)
 - [SPOJ: Maze](http://www.spoj.com/problems/KPMAZE/)
 - [CODECHEF: Complement Spanning Trees](https://www.codechef.com/problems/CSTREE)
