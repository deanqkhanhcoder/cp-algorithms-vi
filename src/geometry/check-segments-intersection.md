---
tags:
  - Translated
e_maxx_link: segments_intersection_checking
---

# Kiểm tra hai đoạn thẳng giao nhau

Bạn được cho hai đoạn thẳng $(a, b)$ và $(c, d)$.
Bạn phải kiểm tra xem chúng có giao nhau không.
Tất nhiên, bạn có thể tìm giao điểm của chúng và kiểm tra xem nó có rỗng không, nhưng điều này không thể thực hiện được bằng số nguyên đối với các đoạn thẳng có tọa độ nguyên.
Cách tiếp cận được mô tả ở đây có thể hoạt động với số nguyên.

## Thuật toán

Đầu tiên, hãy xem xét trường hợp các đoạn thẳng là một phần của cùng một đường thẳng.
Trong trường hợp này, chỉ cần kiểm tra xem hình chiếu của chúng trên $Ox$ và $Oy$ có giao nhau hay không.
Trong trường hợp khác, $a$ và $b$ không được nằm trên cùng một phía của đường thẳng $(c, d)$, và $c$ và $d$ không được nằm trên cùng một phía của đường thẳng $(a, b)$.
Điều này có thể được kiểm tra bằng một vài tích có hướng.

## Cài đặt

Thuật toán đã cho được triển khai cho các điểm có tọa độ nguyên. Tất nhiên, nó có thể dễ dàng được sửa đổi để hoạt động với số thực.

```{.cpp file=check-segments-inter}
struct pt {
    long long x, y;
    pt() {}
    pt(long long _x, long long _y) : x(_x), y(_y) {}
    pt operator-(const pt& p) const { return pt(x - p.x, y - p.y); }
    long long cross(const pt& p) const { return x * p.y - y * p.x; }
    long long cross(const pt& a, const pt& b) const { return (a - *this).cross(b - *this); }
};

int sgn(const long long& x) { return x >= 0 ? x ? 1 : 0 : -1; }

bool inter1(long long a, long long b, long long c, long long d) {
    if (a > b)
        swap(a, b);
    if (c > d)
        swap(c, d);
    return max(a, c) <= min(b, d);
}

bool check_inter(const pt& a, const pt& b, const pt& c, const pt& d) {
    if (c.cross(a, d) == 0 && c.cross(b, d) == 0)
        return inter1(a.x, b.x, c.x, d.x) && inter1(a.y, b.y, c.y, d.y);
    return sgn(a.cross(b, c)) != sgn(a.cross(b, d)) &&
           sgn(c.cross(d, a)) != sgn(c.cross(d, b));
}
```