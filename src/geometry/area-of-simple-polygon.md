---
title: Tìm diện tích đa giác đơn trong O(N)
tags:
  - Translated
e_maxx_link: polygon_area
---
# Tìm diện tích đa giác đơn trong $O(N)$

Cho một đa giác đơn (tức là không tự cắt, không nhất thiết lồi). Yêu cầu tính diện tích của nó khi biết các đỉnh của nó.

## Phương pháp 1

Điều này dễ dàng thực hiện nếu chúng ta đi qua tất cả các cạnh và cộng diện tích hình thang được giới hạn bởi mỗi cạnh và trục x. Diện tích cần được lấy có dấu để diện tích thừa sẽ bị giảm đi. Do đó, công thức như sau:

$$A = \sum_{(p,q)\in \text{các cạnh}} \frac{(p_x - q_x) \cdot (p_y + q_y)}{2}$$

Mã:

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

## Phương pháp 2
Chúng ta có thể chọn một điểm $O$ tùy ý, lặp qua tất cả các cạnh và cộng diện tích có hướng của tam giác được tạo bởi cạnh đó và điểm $O$. Một lần nữa, do dấu của diện tích, diện tích thừa sẽ bị giảm đi.

Phương pháp này tốt hơn vì nó có thể được tổng quát hóa cho các trường hợp phức tạp hơn (chẳng hạn như khi một số cạnh là các cung thay vì các đường thẳng)

```