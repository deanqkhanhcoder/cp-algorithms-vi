---
tags:
  - Translated
e_maxx_link: maximum_zero_submatrix
---

# Tìm ma trận con toàn số 0 lớn nhất (Finding the largest zero submatrix) {: #finding-the-largest-zero-submatrix}

Bạn được cho một ma trận với `n` hàng và `m` cột. Tìm ma trận con lớn nhất chỉ bao gồm các số 0 (ma trận con là một vùng hình chữ nhật của ma trận).

## Thuật toán (Algorithm) {: #algorithm}

Các phần tử của ma trận sẽ là `a[i][j]`, trong đó `i = 0...n - 1`, `j = 0... m - 1`. Để đơn giản, chúng ta sẽ coi tất cả các phần tử khác 0 đều bằng 1.

### Bước 1: Quy hoạch động bổ trợ (Step 1: Auxiliary dynamic) {: #step-1-auxiliary-dynamic}

Đầu tiên, chúng ta tính toán ma trận phụ sau: `d[i][j]`, hàng gần nhất có số 1 phía trên `a[i][j]`. Nói một cách chính thức, `d[i][j]` là số hàng lớn nhất (từ `0` đến `i - 1`), trong đó có một phần tử bằng `1` ở cột thứ `j`.
Trong khi lặp từ trên cùng bên trái sang dưới cùng bên phải, khi chúng ta đứng ở hàng `i`, chúng ta biết các giá trị từ hàng trước đó, vì vậy, chỉ cần cập nhật các phần tử có giá trị `1` là đủ. Chúng ta có thể lưu các giá trị trong một mảng đơn giản `d[j]`, `j = 0...m - 1` (lưu ý: văn bản gốc ghi `i = 1...m - 1` nhưng theo ngữ cảnh là `j`), bởi vì trong thuật toán tiếp theo, chúng ta sẽ xử lý ma trận từng hàng một và chỉ cần các giá trị của hàng hiện tại.

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

### Bước 2: Giải quyết vấn đề (Step 2: Problem solving) {: #step-2-problem-solving}

Chúng ta có thể giải quyết bài toán trong $O(n m^2)$ bằng cách lặp qua các hàng, xem xét mọi cột trái và phải có thể có cho một ma trận con. Đáy của hình chữ nhật sẽ là hàng hiện tại, và sử dụng `d[i][j]`, chúng ta có thể tìm thấy hàng trên cùng. Tuy nhiên, có thể đi xa hơn và cải thiện đáng kể độ phức tạp của giải pháp.

Rõ ràng là ma trận con số 0 mong muốn được giới hạn ở cả bốn phía bởi một số số 1, ngăn không cho nó tăng kích thước và cải thiện câu trả lời. Vì vậy, chúng ta sẽ không bỏ lỡ câu trả lời nếu chúng ta hành động như sau: đối với mỗi ô `j` trong hàng `i` (hàng dưới cùng của ma trận con số 0 tiềm năng), chúng ta sẽ coi `d[i][j]` là hàng trên cùng của ma trận con số 0 hiện tại. Bây giờ vẫn còn phải xác định ranh giới bên trái và bên phải tối ưu của ma trận con số 0, tức là đẩy ma trận con này tối đa sang bên trái và bên phải của cột thứ `j`.

Đẩy tối đa sang bên trái nghĩa là gì? Có nghĩa là tìm một chỉ số `k1` mà `d[i][k1] > d[i][j]`, và đồng thời `k1` - chỉ số gần nhất bên trái chỉ số `j`. Rõ ràng là sau đó `k1 + 1` cho số của cột bên trái của ma trận con số 0 cần tìm (giả sử chỉ số cột bắt đầu từ 0). Nếu hoàn toàn không có chỉ số như vậy, thì đặt `k1` = `-1` (điều này có nghĩa là chúng ta có thể mở rộng ma trận con số 0 hiện tại sang bên trái cho đến tận biên của ma trận `a`).

Tương tự, bạn có thể định nghĩa chỉ số `k2` cho biên bên phải: đây là chỉ số gần nhất bên phải `j` sao cho `d[i][k2] > d[i][j]` (hoặc `m`, nếu không có chỉ số như vậy).

Vì vậy, các chỉ số `k1` và `k2`, nếu chúng ta học cách tìm kiếm chúng một cách hiệu quả, sẽ cung cấp cho chúng ta tất cả thông tin cần thiết về ma trận con số 0 hiện tại. Cụ thể, diện tích của nó sẽ bằng `(i - d[i][j]) * (k2 - k1 - 1)`.

Làm thế nào để tìm kiếm các chỉ số `k1` và `k2` này một cách hiệu quả với `i` và `j` cố định? Chúng ta có thể làm điều đó trung bình trong $O(1)$.

Để đạt được độ phức tạp như vậy, bạn có thể sử dụng ngăn xếp (stack) như sau. Trước tiên hãy tìm cách tìm kiếm chỉ số `k1`, và lưu giá trị của nó cho mỗi chỉ số `j` trong hàng hiện tại `i` vào mảng `d1[j]`. Để làm điều này, chúng ta sẽ xem qua tất cả các cột `j` từ trái sang phải, và chúng ta sẽ chỉ lưu trữ trong ngăn xếp các cột có `d` thực sự lớn hơn `d[j]`. Rõ ràng là khi di chuyển từ cột `j` sang cột tiếp theo, cần phải cập nhật nội dung của ngăn xếp. Khi có một phần tử không phù hợp ở đầu ngăn xếp (tức là `d` của đỉnh stack `<= d[j]`) hãy lấy nó ra (pop). Dễ hiểu là chỉ cần xóa khỏi ngăn xếp từ đỉnh của nó, và không phải từ bất kỳ nơi nào khác (vì ngăn xếp sẽ chứa một dãy các cột có `d` tăng dần).

Giá trị `d1[j]` cho mỗi `j` sẽ bằng giá trị nằm ở thời điểm đó trên đỉnh của ngăn xếp (nếu ngăn xếp rỗng thì là -1).

Động lực `d2[j]` để tìm các chỉ số `k2` được coi là tương tự, chỉ cần bạn xem các cột từ phải sang trái.

Rõ ràng là vì có chính xác `m` phần tử được thêm vào ngăn xếp trên mỗi dòng, nên cũng không thể có nhiều lần xóa hơn, tổng độ phức tạp sẽ là tuyến tính, vì vậy độ phức tạp cuối cùng của thuật toán là $O(nm)$.

Cũng cần lưu ý rằng thuật toán này tiêu thụ bộ nhớ $O(m)$ (không tính dữ liệu đầu vào - ma trận `a[][]`).

### Cài đặt (Implementation) {: #implementation}

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
