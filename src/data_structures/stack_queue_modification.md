---
tags:
  - Translated
e_maxx_link: stacks_for_minima
---

# Ngăn xếp / Hàng đợi tìm giá trị nhỏ nhất (Minimum stack / Minimum queue) {: #minimum-stack-minimum-queue}

Trong bài viết này, chúng ta sẽ xem xét ba vấn đề:
đầu tiên chúng ta sẽ sửa đổi ngăn xếp (stack) theo cách cho phép chúng ta tìm phần tử nhỏ nhất của ngăn xếp trong $O(1)$, sau đó chúng ta sẽ làm điều tương tự với hàng đợi (queue), và cuối cùng chúng ta sẽ sử dụng các cấu trúc dữ liệu này để tìm giá trị nhỏ nhất trong tất cả các mảng con có độ dài cố định trong một mảng trong $O(n)$.

## Sửa đổi ngăn xếp (Stack modification) {: #stack-modification}

Chúng ta muốn sửa đổi cấu trúc dữ liệu ngăn xếp sao cho có thể tìm thấy phần tử nhỏ nhất trong ngăn xếp trong thời gian $O(1)$, trong khi vẫn duy trì hành vi tiệm cận tương tự cho việc thêm và xóa các phần tử khỏi ngăn xếp.
Nhắc lại nhanh, trên một ngăn xếp chúng ta chỉ thêm và xóa các phần tử ở một đầu.

Để làm điều này, chúng ta sẽ không chỉ lưu trữ các phần tử trong ngăn xếp, mà chúng ta sẽ lưu trữ chúng theo cặp: chính phần tử đó và giá trị nhỏ nhất trong ngăn xếp bắt đầu từ phần tử này trở xuống.

```cpp
stack<pair<int, int>> st;
```

Rõ ràng là việc tìm kiếm giá trị nhỏ nhất trong toàn bộ ngăn xếp chỉ bao gồm việc xem giá trị `stack.top().second`.

Cũng rõ ràng là việc thêm hoặc xóa một phần tử mới vào ngăn xếp có thể được thực hiện trong thời gian hằng số.

Cài đặt:

*   Thêm một phần tử:
```cpp
int new_min = st.empty() ? new_elem : min(new_elem, st.top().second);
st.push({new_elem, new_min});
```

*   Xóa một phần tử:
```cpp
int removed_element = st.top().first;
st.pop();
```

*   Tìm giá trị nhỏ nhất:
```cpp
int minimum = st.top().second;
```

## Sửa đổi hàng đợi (phương pháp 1) (Queue modification (method 1)) {: #queue-modification-method-1}

Bây giờ chúng ta muốn đạt được các thao tác tương tự với hàng đợi, tức là chúng ta muốn thêm các phần tử vào cuối và xóa chúng khỏi đầu.

Ở đây chúng ta xem xét một phương pháp đơn giản để sửa đổi hàng đợi.
Tuy nhiên, nó có một nhược điểm lớn, bởi vì hàng đợi được sửa đổi thực sự sẽ không lưu trữ tất cả các phần tử.

Ý tưởng chính là chỉ lưu trữ các mục trong hàng đợi cần thiết để xác định giá trị nhỏ nhất.
Cụ thể là chúng ta sẽ giữ hàng đợi theo thứ tự không giảm (tức là giá trị nhỏ nhất sẽ được lưu trữ ở đầu), và tất nhiên không phải theo bất kỳ cách tùy ý nào, giá trị nhỏ nhất thực tế phải luôn được chứa trong hàng đợi.
Theo cách này, phần tử nhỏ nhất sẽ luôn ở đầu hàng đợi.
Trước khi thêm một phần tử mới vào hàng đợi, chỉ cần thực hiện "cắt":
chúng ta sẽ loại bỏ tất cả các phần tử ở cuối hàng đợi lớn hơn phần tử mới, và sau đó thêm phần tử mới vào hàng đợi.
Theo cách này, chúng ta không phá vỡ thứ tự của hàng đợi, và chúng ta cũng sẽ không làm mất phần tử hiện tại nếu nó là giá trị nhỏ nhất ở bất kỳ bước tiếp theo nào.
Tất cả các phần tử mà chúng ta đã loại bỏ không bao giờ có thể là chính nó, vì vậy thao tác này được cho phép.
Khi chúng ta muốn trích xuất một phần tử từ đầu, nó thực sự có thể không ở đó (bởi vì chúng ta đã loại bỏ nó trước đó trong khi thêm một phần tử nhỏ hơn).
Do đó khi xóa một phần tử khỏi hàng đợi, chúng ta cần biết giá trị của phần tử đó.
Nếu đầu hàng đợi có cùng giá trị, chúng ta có thể xóa nó một cách an toàn, ngược lại chúng ta không làm gì cả.

Xem xét việc cài đặt các thao tác trên:

```cpp
deque<int> q;
```

*   Tìm giá trị nhỏ nhất:
```cpp
int minimum = q.front();
```

*   Thêm một phần tử:
```cpp
while (!q.empty() && q.back() > new_element)
    q.pop_back();
q.push_back(new_element);
```

*   Xóa một phần tử:
```cpp
if (!q.empty() && q.front() == remove_element)
    q.pop_front();
```

Rõ ràng là trung bình tất cả các thao tác này chỉ mất thời gian $O(1)$ (bởi vì mỗi phần tử chỉ có thể được đẩy và bật một lần).

## Sửa đổi hàng đợi (phương pháp 2) (Queue modification (method 2)) {: #queue-modification-method-2}

Đây là một sửa đổi của phương pháp 1.
Chúng ta muốn có thể xóa các phần tử mà không cần biết chúng ta phải xóa phần tử nào.
Chúng ta có thể thực hiện điều đó bằng cách lưu trữ chỉ số cho mỗi phần tử trong hàng đợi.
Và chúng ta cũng nhớ có bao nhiêu phần tử chúng ta đã thêm và xóa.

```cpp
deque<pair<int, int>> q;
int cnt_added = 0;
int cnt_removed = 0;
```

*   Tìm giá trị nhỏ nhất:
```cpp
int minimum = q.front().first;
```

*   Thêm một phần tử:
```cpp
while (!q.empty() && q.back().first > new_element)
    q.pop_back();
q.push_back({new_element, cnt_added});
cnt_added++;
```

*   Xóa một phần tử:
```cpp
if (!q.empty() && q.front().second == cnt_removed) 
    q.pop_front();
cnt_removed++;
```

## Sửa đổi hàng đợi (phương pháp 3) (Queue modification (method 3)) {: #queue-modification-method-3}

Ở đây chúng ta xem xét một cách khác để sửa đổi hàng đợi để tìm giá trị nhỏ nhất trong $O(1)$.
Cách này có phần phức tạp hơn để cài đặt, nhưng lần này chúng ta thực sự lưu trữ tất cả các phần tử.
Và chúng ta cũng có thể xóa một phần tử khỏi đầu mà không cần biết giá trị của nó.

Ý tưởng là giảm bài toán thành bài toán của ngăn xếp, vốn đã được giải quyết bởi chúng ta.
Vì vậy, chúng ta chỉ cần học cách mô phỏng một hàng đợi bằng cách sử dụng hai ngăn xếp.

Chúng ta tạo hai ngăn xếp, `s1` và `s2`.
Tất nhiên các ngăn xếp này sẽ ở dạng sửa đổi, để chúng ta có thể tìm thấy giá trị nhỏ nhất trong $O(1)$.
Chúng ta sẽ thêm các phần tử mới vào ngăn xếp `s1`, và xóa các phần tử khỏi ngăn xếp `s2`.
Nếu bất cứ lúc nào ngăn xếp `s2` trống, chúng ta di chuyển tất cả các phần tử từ `s1` sang `s2` (về cơ bản đảo ngược thứ tự của các phần tử đó).
Cuối cùng việc tìm kiếm giá trị nhỏ nhất trong một hàng đợi chỉ liên quan đến việc tìm giá trị nhỏ nhất của cả hai ngăn xếp.

Do đó, chúng ta thực hiện tất cả các thao tác trong $O(1)$ trung bình (mỗi phần tử sẽ được thêm vào ngăn xếp `s1` một lần, được chuyển sang `s2` một lần và được bật ra khỏi `s2` một lần)

Cài đặt:

```cpp
stack<pair<int, int>> s1, s2;
```

*   Tìm giá trị nhỏ nhất:
```cpp
if (s1.empty() || s2.empty()) 
    minimum = s1.empty() ? s2.top().second : s1.top().second;
else
    minimum = min(s1.top().second, s2.top().second);
```

*   Thêm phần tử:
```cpp
int minimum = s1.empty() ? new_element : min(new_element, s1.top().second);
s1.push({new_element, minimum});
```

*   Xóa một phần tử:
```cpp
if (s2.empty()) {
    while (!s1.empty()) {
        int element = s1.top().first;
        s1.pop();
        int minimum = s2.empty() ? element : min(element, s2.top().second);
        s2.push({element, minimum});
    }
}
int remove_element = s2.top().first;
s2.pop();
```

## Tìm giá trị nhỏ nhất cho mọi mảng con có độ dài cố định (Finding the minimum for all subarrays of fixed length) {: #finding-the-minimum-for-all-subarrays-of-fixed-length}

Giả sử chúng ta được cho một mảng $A$ có độ dài $N$ và một $M \le N$ đã cho.
Chúng ta phải tìm giá trị nhỏ nhất của mỗi mảng con có độ dài $M$ trong mảng này, tức là chúng ta phải tìm:

$$\min_{0 \le i \le M-1} A[i], \min_{1 \le i \le M} A[i], \min_{2 \le i \le M+1} A[i],~\dots~, \min_{N-M \le i \le N-1} A[i]$$

Chúng ta phải giải quyết bài toán này trong thời gian tuyến tính, tức là $O(n)$.

Chúng ta có thể sử dụng bất kỳ hàng đợi nào trong ba hàng đợi đã sửa đổi để giải quyết bài toán.
Các giải pháp nên rõ ràng:
chúng ta thêm $M$ phần tử đầu tiên của mảng, tìm và xuất giá trị nhỏ nhất của nó, sau đó thêm phần tử tiếp theo vào hàng đợi và xóa phần tử đầu tiên của mảng, tìm và xuất giá trị nhỏ nhất của nó, v.v.
Vì tất cả các thao tác với hàng đợi được thực hiện trong thời gian hằng số trung bình, độ phức tạp của toàn bộ thuật toán sẽ là $O(n)$.

## Bài tập (Practice Problems) {: #practice-problems}

*   [Queries with Fixed Length](https://www.hackerrank.com/challenges/queries-with-fixed-length/problem)
*   [Sliding Window Minimum](https://cses.fi/problemset/task/3221)
*   [Binary Land](https://www.codechef.com/MAY20A/problems/BINLAND)

---

## Checklist

- Original lines: 193
- Translated lines: 193
- Code blocks changed? No
- Inline code changed? No
- Technical terms kept in English? Yes
- Headings anchors preserved/added correctly? Yes
- I confirm no character was omitted: YES
