---
tags:
  - Translated
e_maxx_link: length_of_segments_union
---

# Độ dài hợp của các đoạn

Cho $n$ đoạn trên một đường thẳng, mỗi đoạn được mô tả bởi một cặp tọa độ $(a_{i1}, a_{i2})$.
Chúng ta phải tìm độ dài của hợp của chúng.

Thuật toán sau được Klee đề xuất vào năm 1977.
Nó hoạt động trong $O(n\log n)$ và đã được chứng minh là tối ưu về mặt tiệm cận.

## Giải pháp

Chúng ta lưu trữ trong một mảng $x$ các điểm cuối của tất cả các đoạn được sắp xếp theo giá trị của chúng.
Và ngoài ra, chúng ta lưu trữ xem đó là điểm cuối bên trái hay bên phải của một đoạn.
Bây giờ chúng ta lặp qua mảng, giữ một bộ đếm $c$ của các đoạn hiện đang mở.
Bất cứ khi nào phần tử hiện tại là một điểm cuối bên trái, chúng ta tăng bộ đếm này, và ngược lại thì giảm nó.
Để tính toán câu trả lời, chúng ta lấy độ dài giữa các giá trị $x$ cuối cùng $x_i - x_{i-1}$, bất cứ khi nào chúng ta đến một tọa độ mới, và hiện tại có ít nhất một đoạn đang mở.

## Cài đặt

```cpp
int length_union(const vector<pair<int, int>> &a) {
    int n = a.size();
    vector<pair<int, bool>> x(n*2);
    for (int i = 0; i < n; i++) {
        x[i*2] = {a[i].first, false};
        x[i*2+1] = {a[i].second, true};
    }

    sort(x.begin(), x.end());

    int result = 0;
    int c = 0;
    for (int i = 0; i < n * 2; i++) {
        if (i > 0 && x[i].first > x[i-1].first && c > 0)
            result += x[i].first - x[i-1].first;
        if (x[i].second)
            c--;
        else
            c++;
    }
    return result;
}
```