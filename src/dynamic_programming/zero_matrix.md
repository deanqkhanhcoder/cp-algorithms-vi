---
tags:
  - Translated
e_maxx_link: maximum_zero_submatrix
---

# Tìm ma trận con lớn nhất toàn phần tử 0

Cho một ma trận có `n` hàng và `m` cột. Hãy tìm ma trận con lớn nhất chỉ gồm các phần tử 0 (ma trận con là một vùng chữ nhật của ma trận).

## Thuật toán

Các phần tử của ma trận là `a[i][j]`, với `i = 0...n - 1`, `j = 0... m - 1`. Để đơn giản, ta coi mọi phần tử khác 0 đều bằng 1.

### Bước 1: Mảng phụ

Trước hết ta tính mảng phụ sau: `d[j]` là hàng gần nhất phía trên ô `a[i][j]` có chứa giá trị 1. Nói chính xác hơn, `d[j]` là chỉ số hàng lớn nhất (từ `0` đến `i - 1`) mà ở đó cột `j` có một phần tử bằng 1.
Khi duyệt từ trên xuống dưới và từ trái sang phải, khi đứng ở hàng `i` ta đã biết các giá trị từ hàng trước nên chỉ cần cập nhật những cột có giá trị 1. Ta có thể lưu các giá trị này trong một mảng một chiều `d` có kích thước `m`, vì trong phần còn lại của thuật toán chỉ cần xử lý từng hàng một.

```cpp
vector<int> d(m, -1);
for (int i = 0; i < n; ++i) {
    for (int j = 0; j < m; ++j) {
        if (a[i][j] == 1) {
            d[j] = i;
        }
    }
}
```

### Bước 2: Giải bài toán

Ta có thể giải bài toán bằng $O(n m^2)$ bằng cách duyệt các hàng và xét mọi cặp cột trái/phải là biên của ma trận con. Đáy của hình chữ nhật sẽ là hàng hiện tại, và dùng `d[j]` ta có thể tìm hàng trên cùng. Tuy nhiên ta có thể làm tốt hơn và cải thiện đáng kể độ phức tạp.

Rõ ràng ma trận con toàn số 0 tối ưu sẽ bị giới hạn bởi các phần tử 1 ở cả bốn phía, những phần tử này ngăn không cho ma trận con mở rộng thêm. Vì vậy đối với mỗi ô `j` ở hàng `i` (hàng đáy của một ma trận con khả dĩ), ta lấy `d[j]` làm hàng trên của ma trận con hiện thời. Việc còn lại là xác định biên trái và biên phải tối ưu, tức là mở rộng tối đa sang trái và phải của cột `j`.

Mở rộng tối đa sang trái có nghĩa là tìm chỉ số `k1` là vị trí gần nhất phía trái của `j` sao cho `d[k1] > d[j]`. Khi đó `k1 + 1` là chỉ số cột trái của ma trận con cần tìm. Nếu không tồn tại, đặt `k1 = -1` (nghĩa là ta có thể mở rộng tới biên trái của ma trận).

Tương tự, chỉ số `k2` cho biên phải là vị trí gần nhất phía phải của `j` sao cho `d[k2] > d[j]` (hoặc `m` nếu không tồn tại).

Khi biết `k1` và `k2`, diện tích của ma trận con tương ứng là `(i - d[j]) * (k2 - k1 - 1)`.

Làm sao để tìm `k1` và `k2` hiệu quả cho mọi `i, j`? Ta có thể làm trung bình O(1) cho mỗi ô bằng cách sử dụng ngăn xếp.

Cụ thể, để tìm `k1` cho mỗi cột `j` trên hàng `i`, duyệt các cột từ trái sang phải và duy trì một ngăn xếp chỉ chứa các cột có `d[]` lớn hơn `d[j]`. Khi chuyển sang cột tiếp theo, loại bỏ các phần tử không phù hợp ở đỉnh ngăn xếp (tức `d[top] <= d[j]`) bằng cách pop. Giá trị `d1[j]` là chỉ số hiện đang đứng ở đỉnh ngăn xếp (hoặc `-1` nếu rỗng).

Tương tự, để tìm `k2` ta lặp các cột từ phải sang trái và dùng cùng ý tưởng để tính `d2[j]`.

Mỗi cột được đẩy vào ngăn xếp đúng một lần và cũng bị pop tối đa một lần trên mỗi hàng, nên tổng chi phí cho mỗi hàng là O(m), và toàn bộ thuật toán chạy O(n m).

Thuật toán dùng thêm O(m) bộ nhớ (không tính dữ liệu vào `a[][]`).

### Cài đặt

```cpp
int zero_matrix(vector<vector<int>> a) {
    int n = a.size();
    int m = a[0].size();

    int ans = 0;
    vector<int> d(m, -1), d1(m), d2(m);
    stack<int> st;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (a[i][j] == 1)
                d[j] = i;
        }

        for (int j = 0; j < m; ++j) {
            while (!st.empty() && d[st.top()] <= d[j])
                st.pop();
            d1[j] = st.empty() ? -1 : st.top();
            st.push(j);
        }
        while (!st.empty())
            st.pop();

        for (int j = m - 1; j >= 0; --j) {
            while (!st.empty() && d[st.top()] <= d[j])
                st.pop();
            d2[j] = st.empty() ? m : st.top();
            st.push(j);
        }
        while (!st.empty())
            st.pop();

        for (int j = 0; j < m; ++j)
            ans = max(ans, (i - d[j]) * (d2[j] - d1[j] - 1));
    }
    return ans;
}
```