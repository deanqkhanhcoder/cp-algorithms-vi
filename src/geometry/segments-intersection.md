---
tags:
  - Translated
e_maxx_link: segments_intersection
---

# Tìm giao của hai đoạn thẳng (Finding intersection of two segments) {: #finding-intersection-of-two-segments}

Bạn được cho hai đoạn thẳng AB và CD, được mô tả dưới dạng các cặp điểm đầu mút của chúng. Mỗi đoạn thẳng có thể là một điểm duy nhất nếu các điểm đầu mút của nó giống nhau.
Bạn phải tìm giao của các đoạn thẳng này, có thể là rỗng (nếu các đoạn thẳng không cắt nhau), một điểm duy nhất hoặc một đoạn thẳng (nếu các đoạn thẳng đã cho chồng lấn lên nhau).

## Giải pháp (Solution) {: #solution}

Chúng ta có thể tìm điểm giao nhau của các đoạn thẳng theo cách tương tự như [giao điểm của các đường thẳng](lines-intersection.md):
xây dựng lại phương trình đường thẳng từ các điểm đầu mút của đoạn thẳng và kiểm tra xem chúng có song song hay không.

Nếu các đường thẳng không song song, chúng ta cần tìm điểm giao nhau của chúng và kiểm tra xem nó có thuộc về cả hai đoạn thẳng hay không
(để làm điều này, đủ để xác minh rằng điểm giao nhau thuộc về từng đoạn thẳng được chiếu trên các trục X và Y).
Trong trường hợp này, câu trả lời sẽ là "không giao nhau" hoặc điểm giao nhau duy nhất của các đường thẳng.

Trường hợp các đường thẳng song song phức tạp hơn một chút (trường hợp một hoặc nhiều đoạn thẳng là một điểm duy nhất cũng thuộc về đây).
Trong trường hợp này, chúng ta cần kiểm tra xem cả hai đoạn thẳng có thuộc cùng một đường thẳng hay không.
Nếu không, câu trả lời là "không giao nhau".
Nếu có, câu trả lời là giao của các đoạn thẳng thuộc cùng một đường thẳng, thu được bằng cách sắp xếp các điểm đầu mút của cả hai đoạn thẳng theo thứ tự tăng dần của một tọa độ nhất định và lấy điểm cực phải của các điểm đầu mút trái và điểm cực trái của các điểm đầu mút phải.

Nếu cả hai đoạn thẳng là các điểm đơn lẻ, các điểm này phải giống hệt nhau, và việc thực hiện kiểm tra này riêng biệt là hợp lý.

Ở đầu thuật toán, hãy thêm một kiểm tra hộp bao (bounding box) - điều này cần thiết cho trường hợp khi các đoạn thẳng thuộc cùng một đường thẳng, và (là một kiểm tra nhẹ) nó cho phép thuật toán hoạt động nhanh hơn trung bình trên các thử nghiệm ngẫu nhiên.

## Cài đặt (Implementation) {: #implementation}

Dưới đây là cài đặt, bao gồm tất cả các hàm trợ giúp cho việc xử lý đường thẳng và đoạn thẳng.

Hàm chính `intersect` trả về true nếu các đoạn thẳng có giao điểm khác rỗng,
và lưu trữ các điểm đầu mút của đoạn thẳng giao nhau trong các đối số `left` và `right`.
Nếu câu trả lời là một điểm duy nhất, các giá trị được ghi vào `left` và `right` sẽ giống nhau.
```cpp title="segment_intersection"
const double EPS = 1E-9;

struct pt {
    double x, y;

    bool operator<(const pt& p) const
    {
        return x < p.x - EPS || (abs(x - p.x) < EPS && y < p.y - EPS);
    }
};

struct line {
    double a, b, c;

    line() {}
    line(pt p, pt q)
    {
        a = p.y - q.y;
        b = q.x - p.x;
        c = -a * p.x - b * p.y;
        norm();
    }

    void norm()
    {
        double z = sqrt(a * a + b * b);
        if (abs(z) > EPS)
            a /= z, b /= z, c /= z;
    }

    double dist(pt p) const { return a * p.x + b * p.y + c; }
};

double det(double a, double b, double c, double d)
{
    return a * d - b * c;
}

inline bool betw(double l, double r, double x)
{
    return min(l, r) <= x + EPS && x <= max(l, r) + EPS;
}

inline bool intersect_1d(double a, double b, double c, double d)
{
    if (a > b)
        swap(a, b);
    if (c > d)
        swap(c, d);
    return max(a, c) <= min(b, d) + EPS;
}

bool intersect(pt a, pt b, pt c, pt d, pt& left, pt& right)
{
    if (!intersect_1d(a.x, b.x, c.x, d.x) || !intersect_1d(a.y, b.y, c.y, d.y))
        return false;
    line m(a, b);
    line n(c, d);
    double zn = det(m.a, m.b, n.a, n.b);
    if (abs(zn) < EPS) {
        if (abs(m.dist(c)) > EPS || abs(n.dist(a)) > EPS)
            return false;
        if (b < a)
            swap(a, b);
        if (d < c)
            swap(c, d);
        left = max(a, c);
        right = min(b, d);
        return true;
    } else {
        left.x = right.x = -det(m.c, m.b, n.c, n.b) / zn;
        left.y = right.y = -det(m.a, m.c, n.a, n.c) / zn;
        return betw(a.x, b.x, left.x) && betw(a.y, b.y, left.y) &&
               betw(c.x, d.x, left.x) && betw(c.y, d.y, left.y);
    }
}
```
