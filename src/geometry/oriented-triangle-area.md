---
tags:
  - Translated
e_maxx_link: oriented_area
---

# Diện tích có hướng của tam giác (Oriented area of a triangle) {: #oriented-area-of-a-triangle}

Cho ba điểm $p_1$, $p_2$ và $p_3$, tính diện tích có hướng (có dấu) của tam giác được tạo bởi chúng. Dấu của diện tích được xác định theo cách sau: hãy tưởng tượng bạn đang đứng trong mặt phẳng tại điểm $p_1$ và đang đối mặt với $p_2$. Bạn đi đến $p_2$ và nếu $p_3$ ở bên phải của bạn (khi đó chúng ta nói ba vector quay "cùng chiều kim đồng hồ"), dấu của diện tích là âm, ngược lại nó là dương. Nếu ba điểm thẳng hàng, diện tích bằng không.

Sử dụng diện tích có dấu này, chúng ta có thể vừa nhận được diện tích không dấu thông thường (như giá trị tuyệt đối của diện tích có dấu) vừa xác định xem các điểm nằm cùng chiều kim đồng hồ hay ngược chiều kim đồng hồ theo thứ tự đã chỉ định của chúng (điều này hữu ích, ví dụ, trong các thuật toán bao lồi).

## Tính toán (Calculation) {: #calculation}
Chúng ta có thể sử dụng thực tế là định thức của ma trận $2\times 2$ bằng với diện tích có dấu của hình bình hành được tạo bởi các vector cột (hoặc hàng) của ma trận.
Điều này tương tự với định nghĩa của tích có hướng trong 2D (xem [Hình học cơ bản](basic-geometry.md)).
Bằng cách chia diện tích này cho hai, chúng ta nhận được diện tích của tam giác mà chúng ta quan tâm.
Chúng ta sẽ sử dụng $\vec{p_1p_2}$ và $\vec{p_2p_3}$ làm các vector cột và tính toán định thức $2\times 2$:

$$2S=\left|\begin{matrix}x_2-x_1 & x_3-x_2\\y_2-y_1 & y_3-y_2\end{matrix}\right|=(x_2-x_1)(y_3-y_2)-(x_3-x_2)(y_2-y_1)$$

## Cài đặt (Implementation) {: #implementation}

```cpp
int signed_area_parallelogram(point2d p1, point2d p2, point2d p3) {
    return cross(p2 - p1, p3 - p2);
}

double triangle_area(point2d p1, point2d p2, point2d p3) {
    return abs(signed_area_parallelogram(p1, p2, p3)) / 2.0;
}

bool clockwise(point2d p1, point2d p2, point2d p3) {
    return signed_area_parallelogram(p1, p2, p3) < 0;
}

bool counter_clockwise(point2d p1, point2d p2, point2d p3) {
    return signed_area_parallelogram(p1, p2, p3) > 0;
}
```

## Bài tập (Practice Problems) {: #practice-problems}
* [Codechef - Chef and Polygons](https://www.codechef.com/problems/CHEFPOLY)
