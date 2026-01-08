---
title: Tìm diện tích đa giác đơn trong O(N) (Finding area of simple polygon in O(N))
tags:
  - Translated
e_maxx_link: polygon_area
---
# Tìm diện tích đa giác đơn trong $O(N)$ (Finding area of simple polygon in $O(N)$) {: #finding-area-of-simple-polygon-in-on}

Cho một đa giác đơn (tức là không tự cắt, không nhất thiết phải lồi). Yêu cầu tính diện tích của nó khi biết các đỉnh.

## Phương pháp 1 (Method 1) {: #method-1}

Điều này rất dễ thực hiện nếu chúng ta đi qua tất cả các cạnh và thêm diện tích hình thang được giới hạn bởi mỗi cạnh và trục hoành (trục x). Diện tích cần được lấy có dấu để phần diện tích thừa sẽ bị giảm bớt. Do đó, công thức như sau:

$$A = \sum_{(p,q)\in \text{edges}} \frac{(p_x - q_x) \cdot (p_y + q_y)}{2}$$

Mã nguồn:

```cpp
double area(const vector<point>& fig) {
    double res = 0;
    for (unsigned i = 0; i < fig.size(); i++) {
        point p = i ? fig[i - 1] : fig.back();
        point q = fig[i];
        res += (p.x - q.x) * (p.y + q.y);
    }
    return fabs(res) / 2;
}
```

## Phương pháp 2 (Method 2) {: #method-2}
Chúng ta có thể chọn một điểm $O$ bất kỳ, lặp qua tất cả các cạnh và cộng diện tích định hướng của tam giác được tạo bởi cạnh đó và điểm $O$. Một lần nữa, do dấu của diện tích, phần diện tích thừa sẽ bị giảm bớt.

Phương pháp này tốt hơn vì nó có thể được tổng quát hóa cho các trường hợp phức tạp hơn (chẳng hạn như khi một số cạnh là cung tròn thay vì đường thẳng).
