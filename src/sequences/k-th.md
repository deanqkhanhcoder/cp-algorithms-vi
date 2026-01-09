---
title: Thống kê thứ tự thứ K trong O(N)
tags:
  - Translated
e_maxx_link: kth_order_statistics
---
# Thống kê thứ tự thứ $K$ trong $O(N)$ ($K$th order statistic in $O(N)$) {: #kth-order-statistic-in-o-n}

Cho một mảng $A$ có kích thước $N$ và một số $K$. Bài toán là tìm số lớn thứ $K$ trong mảng, tức là thống kê thứ tự thứ $K$.

Ý tưởng cơ bản - sử dụng ý tưởng của thuật toán sắp xếp nhanh (quick sort). Trên thực tế, thuật toán rất đơn giản, nhưng khó chứng minh hơn là nó chạy trung bình trong $O(N)$, trái ngược với sắp xếp nhanh.

## Cài đặt (không đệ quy) (Implementation (not recursive)) {: #implementation-not-recursive}

```cpp
template <class T>
T order_statistics (std::vector<T> a, unsigned n, unsigned k)
{
    using std::swap;
    for (unsigned l=1, r=n; ; )
    {
        if (r <= l+1)
        {
            // kích thước phần hiện tại là 1 hoặc 2, vì vậy rất dễ tìm thấy câu trả lời
            if (r == l+1 && a[r] < a[l])
                swap (a[l], a[r]);
            return a[k];
        }

        // sắp xếp a[l], a[l+1], a[r]
        unsigned mid = (l + r) >> 1;
        swap (a[mid], a[l+1]);
        if (a[l] > a[r])
            swap (a[l], a[r]);
        if (a[l+1] > a[r])
            swap (a[l+1], a[r]);
        if (a[l] > a[l+1])
            swap (a[l], a[l+1]);

        // thực hiện phân chia
        // rào cản là a[l + 1], tức là trung vị giữa a[l], a[l + 1], a[r]
        unsigned
            i = l+1,
            j = r;
        const T
            cur = a[l+1];
        for (;;)
        {
            while (a[++i] < cur) ;
            while (a[--j] > cur) ;
            if (i > j)
                break;
            swap (a[i], a[j]);
        }

        // chèn rào cản
        a[l+1] = a[j];
        a[j] = cur;
        
        // chúng ta tiếp tục làm việc trong phần đó, phần phải chứa phần tử cần thiết
        if (j >= k)
            r = j-1;
        if (j <= k)
            l = i;
    }
}
```

## Ghi chú (Notes) {: #notes}
* Thuật toán ngẫu nhiên ở trên có tên là [quickselect](https://en.wikipedia.org/wiki/Quickselect). Bạn nên xáo trộn ngẫu nhiên $A$ trước khi gọi nó hoặc sử dụng một phần tử ngẫu nhiên làm rào cản để nó chạy đúng cách. Cũng có những thuật toán xác định giải quyết vấn đề đã chỉ định trong thời gian tuyến tính, chẳng hạn như [median of medians](https://en.wikipedia.org/wiki/Median_of_medians).
* [std::nth_element](https://en.cppreference.com/w/cpp/algorithm/nth_element) giải quyết vấn đề này trong C++ nhưng triển khai của gcc chạy trong trường hợp xấu nhất $O(n \log n )$.
* Việc tìm $K$ phần tử nhỏ nhất có thể được giảm xuống thành việc tìm phần tử thứ $K$ với chi phí chung tuyến tính, vì chúng chính xác là các phần tử nhỏ hơn phần tử thứ $K$.

## Bài tập (Practice Problems) {: #practice-problems}
- [Leetcode: Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/description/)
- [CODECHEF: Median](https://www.codechef.com/problems/CD1IT1)
