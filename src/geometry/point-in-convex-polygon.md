---
title: Kiểm tra điểm có thuộc đa giác lồi trong O(log N)
tags:
  - Translated
e_maxx_link: pt_in_polygon
---
# Kiểm tra điểm có thuộc đa giác lồi trong $O(\log N)$ (Check if point belongs to the convex polygon in $O(\log N)$) {: #check-if-point-belongs-to-the-convex-polygon-in-o-log-n}

Xem xét bài toán sau: bạn được cho một đa giác lồi với các đỉnh nguyên và rất nhiều truy vấn.
Mỗi truy vấn là một điểm, mà chúng ta cần xác định xem nó nằm bên trong hay trên biên của đa giác hay không.
Giả sử đa giác được sắp xếp ngược chiều kim đồng hồ. Chúng ta sẽ trả lời mỗi truy vấn trong $O(\log n)$ trực tuyến (online).

## Thuật toán (Algorithm) {: #algorithm}
Hãy chọn điểm có tọa độ x nhỏ nhất. Nếu có một vài điểm như vậy, chúng ta chọn điểm có tọa độ y nhỏ nhất. Hãy ký hiệu nó là $p_0$.
Bây giờ tất cả các điểm khác $p_1,\dots,p_n$ của đa giác được sắp xếp theo góc cực của chúng từ điểm đã chọn (vì đa giác được sắp xếp ngược chiều kim đồng hồ).

Nếu điểm thuộc về đa giác, nó thuộc về một tam giác nào đó $p_0, p_i, p_{i + 1}$ (có thể nhiều hơn một nếu nó nằm trên biên của các tam giác).
Xem xét tam giác $p_0, p_i, p_{i + 1}$ sao cho $p$ thuộc về tam giác này và $i$ là lớn nhất trong số tất cả các tam giác như vậy.

Có một trường hợp đặc biệt. $p$ nằm trên đoạn thẳng $(p_0, p_n)$. Trường hợp này chúng ta sẽ kiểm tra riêng.
Ngược lại tất cả các điểm $p_j$ với $j \le i$ nằm ngược chiều kim đồng hồ so với $p$ đối với $p_0$, và tất cả các điểm khác không ngược chiều kim đồng hồ so với $p$.
Điều này có nghĩa là chúng ta có thể áp dụng tìm kiếm nhị phân cho điểm $p_i$, sao cho $p_i$ không nằm ngược chiều kim đồng hồ so với $p$ đối với $p_0$, và $i$ là lớn nhất trong số tất cả các điểm như vậy.
Và sau đó chúng ta kiểm tra xem điểm có thực sự nằm trong tam giác đã xác định hay không.

Dấu của $(a - c) \times (b - c)$ sẽ cho chúng ta biết, nếu điểm $a$ nằm cùng chiều kim đồng hồ hay ngược chiều kim đồng hồ so với điểm $b$ đối với điểm $c$.
Nếu $(a - c) \times (b - c) > 0$, thì điểm $a$ nằm bên phải của vector đi từ $c$ đến $b$, điều này có nghĩa là cùng chiều kim đồng hồ so với $b$ đối với $c$.
Và nếu $(a - c) \times (b - c) < 0$, thì điểm nằm bên trái, hoặc ngược chiều kim đồng hồ.
Và nó nằm chính xác trên đường thẳng giữa các điểm $b$ và $c$ nếu tích bằng 0.

Quay lại thuật toán:
Xem xét một điểm truy vấn $p$.
Đầu tiên, chúng ta phải kiểm tra xem điểm có nằm giữa $p_1$ và $p_n$ hay không.
Ngược lại chúng ta đã biết rằng nó không thể là một phần của đa giác.
Điều này có thể được thực hiện bằng cách kiểm tra xem tích có hướng $(p_1 - p_0)\times(p - p_0)$ là bằng không hoặc có cùng dấu với $(p_1 - p_0)\times(p_n - p_0)$, và $(p_n - p_0)\times(p - p_0)$ là bằng không hoặc có cùng dấu với $(p_n - p_0)\times(p_1 - p_0)$.

Sau đó chúng ta xử lý trường hợp đặc biệt trong đó $p$ là một phần của đường thẳng $(p_0, p_1)$.
Và sau đó chúng ta có thể tìm kiếm nhị phân điểm cuối cùng từ $p_1,\dots p_n$ mà không nằm ngược chiều kim đồng hồ so với $p$ đối với $p_0$.
Đối với một điểm đơn lẻ $p_i$, điều kiện này có thể được kiểm tra bằng cách kiểm tra xem $(p_i - p_0)\times(p - p_0) \le 0$. Sau khi chúng ta tìm thấy một điểm như vậy $p_i$, chúng ta phải kiểm tra xem $p$ có nằm bên trong tam giác $p_0, p_i, p_{i + 1}$ hay không.
Để kiểm tra xem nó có thuộc về tam giác hay không, chúng ta chỉ cần kiểm tra xem $|(p_i - p_0)\times(p_{i + 1} - p_0)| = |(p_0 - p)\times(p_i - p)| + |(p_i - p)\times(p_{i + 1} - p)| + |(p_{i + 1} - p)\times(p_0 - p)|$.
Điều này kiểm tra xem diện tích của tam giác $p_0, p_i, p_{i+1}$ có cùng kích thước chính xác với tổng kích thước của tam giác $p_0, p_i, p$, tam giác $p_0, p, p_{i+1}$ và tam giác $p_i, p_{i+1}, p$.
Nếu $p$ ở bên ngoài, thì tổng của ba tam giác đó sẽ lớn hơn kích thước của tam giác.
Nếu nó ở bên trong, thì nó sẽ bằng nhau.

## Cài đặt (Implementation) {: #implementation}

Hàm `prepare` sẽ đảm bảo rằng điểm nhỏ nhất theo thứ tự từ điển (giá trị x nhỏ nhất, và trong trường hợp hòa thì giá trị y nhỏ nhất) sẽ là $p_0$, và tính toán các vector $p_i - p_0$.
Sau đó hàm `pointInConvexPolygon` tính toán kết quả của một truy vấn.
Chúng ta ghi nhớ thêm điểm $p_0$ và tịnh tiến tất cả các điểm được truy vấn với nó để tính toán khoảng cách chính xác, vì các vector không có điểm ban đầu.
Bằng cách tịnh tiến các điểm truy vấn, chúng ta có thể giả định rằng tất cả các vector bắt đầu tại gốc tọa độ $(0, 0)$, và đơn giản hóa các tính toán cho khoảng cách và độ dài.

```{.cpp file=points_in_convex_polygon}
struct pt {
    long long x, y;
    pt() {}
    pt(long long _x, long long _y) : x(_x), y(_y) {}
    pt operator+(const pt &p) const { return pt(x + p.x, y + p.y); }
    pt operator-(const pt &p) const { return pt(x - p.x, y - p.y); }
    long long cross(const pt &p) const { return x * p.y - y * p.x; }
    long long dot(const pt &p) const { return x * p.x + y * p.y; }
    long long cross(const pt &a, const pt &b) const { return (a - *this).cross(b - *this); }
    long long dot(const pt &a, const pt &b) const { return (a - *this).dot(b - *this); }
    long long sqrLen() const { return this->dot(*this); }
};

bool lexComp(const pt &l, const pt &r) {
    return l.x < r.x || (l.x == r.x && l.y < r.y);
}

int sgn(long long val) { return val > 0 ? 1 : (val == 0 ? 0 : -1); }

vector<pt> seq;
pt translation;
int n;

bool pointInTriangle(pt a, pt b, pt c, pt point) {
    long long s1 = abs(a.cross(b, c));
    long long s2 = abs(point.cross(a, b)) + abs(point.cross(b, c)) + abs(point.cross(c, a));
    return s1 == s2;
}

void prepare(vector<pt> &points) {
    n = points.size();
    int pos = 0;
    for (int i = 1; i < n; i++) {
        if (lexComp(points[i], points[pos]))
            pos = i;
    }
    rotate(points.begin(), points.begin() + pos, points.end());

    n--;
    seq.resize(n);
    for (int i = 0; i < n; i++)
        seq[i] = points[i + 1] - points[0];
    translation = points[0];
}

bool pointInConvexPolygon(pt point) {
    point = point - translation;
    if (seq[0].cross(point) != 0 &&
            sgn(seq[0].cross(point)) != sgn(seq[0].cross(seq[n - 1])))
        return false;
    if (seq[n - 1].cross(point) != 0 &&
            sgn(seq[n - 1].cross(point)) != sgn(seq[n - 1].cross(seq[0])))
        return false;

    if (seq[0].cross(point) == 0)
        return seq[0].sqrLen() >= point.sqrLen();

    int l = 0, r = n - 1;
    while (r - l > 1) {
        int mid = (l + r) / 2;
        int pos = mid;
        if (seq[pos].cross(point) >= 0)
            l = mid;
        else
            r = mid;
    }
    int pos = l;
    return pointInTriangle(seq[pos], seq[pos + 1], pt(0, 0), point);
}
```

## Bài tập (Problems) {: #problems}
* [SGU253 Theodore Roosevelt](https://codeforces.com/problemsets/acmsguru/problem/99999/253)
* [Codeforces 55E Very simple problem](https://codeforces.com/contest/55/problem/E)
* [Codeforces 166B Polygons](https://codeforces.com/problemset/problem/166/B)
