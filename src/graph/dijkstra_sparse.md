---
tags:
  - Translated
e_maxx_link: dijkstra_sparse
---

# Dijkstra trên đồ thị thưa

Để biết phát biểu của bài toán, thuật toán với việc triển khai và chứng minh có thể được tìm thấy trong bài viết [Thuật toán của Dijkstra](dijkstra.md).

## Thuật toán

Chúng ta nhớ lại trong việc suy ra độ phức tạp của thuật toán Dijkstra, chúng ta đã sử dụng hai yếu tố:
thời gian tìm đỉnh chưa được đánh dấu có khoảng cách $d[v]$ nhỏ nhất, và thời gian của việc nới lỏng (relaxation), tức là thời gian thay đổi các giá trị $d[\text{to}]$. 

Trong việc triển khai đơn giản nhất, các thao tác này yêu cầu thời gian $O(n)$ và $O(1)$.
Do đó, vì chúng ta thực hiện thao tác đầu tiên $O(n)$ lần và thao tác thứ hai $O(m)$ lần, chúng ta có được độ phức tạp $O(n^2 + m)$. 

Rõ ràng, độ phức tạp này là tối ưu cho một đồ thị dày đặc, tức là khi $m \approx n^2$.
Tuy nhiên, trong các đồ thị thưa, khi $m$ nhỏ hơn nhiều so với số cạnh tối đa $n^2$, độ phức tạp trở nên kém tối ưu hơn vì số hạng đầu tiên.
Do đó, cần phải cải thiện thời gian thực hiện của thao tác đầu tiên (và tất nhiên là không ảnh hưởng nhiều đến thao tác thứ hai).

Để thực hiện điều đó, chúng ta có thể sử dụng một biến thể của nhiều cấu trúc dữ liệu phụ trợ.
Hiệu quả nhất là **đống Fibonacci**, cho phép thao tác đầu tiên chạy trong $O(\log n)$, và thao tác thứ hai trong $O(1)$.
Do đó, chúng ta sẽ có được độ phức tạp $O(n \log n + m)$ cho thuật toán của Dijkstra, đây cũng là mức tối thiểu lý thuyết cho bài toán tìm đường đi ngắn nhất.
Do đó, thuật toán này hoạt động tối ưu, và đống Fibonacci là cấu trúc dữ liệu tối ưu.
Không tồn tại bất kỳ cấu trúc dữ liệu nào có thể thực hiện cả hai thao tác trong $O(1)$, vì điều này cũng sẽ cho phép sắp xếp một danh sách các số ngẫu nhiên trong thời gian tuyến tính, điều này là không thể.
Thật thú vị, có một thuật toán của Thorup tìm đường đi ngắn nhất trong thời gian $O(m)$, tuy nhiên chỉ hoạt động với trọng số nguyên, và sử dụng một ý tưởng hoàn toàn khác.
Vì vậy, điều này không dẫn đến bất kỳ mâu thuẫn nào.
Đống Fibonacci cung cấp độ phức tạp tối ưu cho nhiệm vụ này.
Tuy nhiên, chúng khá phức tạp để triển khai, và cũng có một hằng số ẩn khá lớn.

Như một sự thỏa hiệp, bạn có thể sử dụng các cấu trúc dữ liệu thực hiện cả hai loại thao tác (trích xuất một phần tử tối thiểu và cập nhật một mục) trong $O(\log n)$.
Khi đó, độ phức tạp của thuật toán Dijkstra là $O(n \log n + m \log n) = O(m \log n)$.

C++ cung cấp hai cấu trúc dữ liệu như vậy: `set` và `priority_queue`.
Cái đầu tiên dựa trên cây đỏ-đen, và cái thứ hai dựa trên đống.
Do đó, `priority_queue` có hằng số ẩn nhỏ hơn, nhưng cũng có một nhược điểm:
nó không hỗ trợ thao tác xóa một phần tử.
Vì lý do này, chúng ta cần thực hiện một "giải pháp thay thế", thực tế dẫn đến một yếu tố hơi tệ hơn là $\log m$ thay vì $\log n$ (mặc dù về mặt độ phức tạp, chúng giống hệt nhau).

## Cài đặt

### set

Hãy bắt đầu với container `set`.
Vì chúng ta cần lưu trữ các đỉnh được sắp xếp theo các giá trị $d[]$ của chúng, nên sẽ thuận tiện khi lưu trữ các cặp thực tế: khoảng cách và chỉ số của đỉnh.
Kết quả là trong một `set`, các cặp được tự động sắp xếp theo khoảng cách của chúng.

```cpp
const int INF = 1000000000;
vector<vector<pair<int, int>>> adj;

void dijkstra(int s, vector<int> & d, vector<int> & p) {
    int n = adj.size();
    d.assign(n, INF);
    p.assign(n, -1);

    d[s] = 0;
    set<pair<int, int>> q;
    q.insert({0, s});
    while (!q.empty()) {
        int v = q.begin()->second;
        q.erase(q.begin());

        for (auto edge : adj[v]) {
            int to = edge.first;
            int len = edge.second;
            
            if (d[v] + len < d[to]) {
                q.erase({d[to], to});
                d[to] = d[v] + len;
                p[to] = v;
                q.insert({d[to], to});
            }
        }
    }
}
```

Chúng ta không cần mảng $u[]$ từ việc triển khai thuật toán Dijkstra thông thường nữa.
Chúng ta sẽ sử dụng `set` để lưu trữ thông tin đó, và cũng tìm đỉnh có khoảng cách ngắn nhất với nó.
Nó hoạt động giống như một hàng đợi.
Các vòng lặp chính thực hiện cho đến khi không còn đỉnh nào trong tập/hàng đợi.
Một đỉnh có khoảng cách nhỏ nhất được trích xuất, và đối với mỗi lần nới lỏng thành công, trước tiên chúng ta xóa cặp cũ, và sau đó sau khi nới lỏng, thêm cặp mới vào hàng đợi.

### priority_queue

Sự khác biệt chính so với việc triển khai với `set` là trong nhiều ngôn ngữ, bao gồm cả C++, chúng ta không thể xóa các phần tử khỏi `priority_queue` (mặc dù các đống có thể hỗ trợ thao tác đó về mặt lý thuyết).
Do đó, chúng ta phải sử dụng một giải pháp thay thế:
Chúng ta chỉ đơn giản là không xóa cặp cũ khỏi hàng đợi.
Kết quả là một đỉnh có thể xuất hiện nhiều lần với khoảng cách khác nhau trong hàng đợi cùng một lúc.
Trong số các cặp này, chúng ta chỉ quan tâm đến các cặp mà phần tử đầu tiên bằng với giá trị tương ứng trong $d[]$, tất cả các cặp khác đều là cặp cũ.
Do đó, chúng ta cần thực hiện một sửa đổi nhỏ:
vào đầu mỗi lần lặp, sau khi trích xuất cặp tiếp theo, chúng ta kiểm tra xem nó có phải là một cặp quan trọng hay nó đã là một cặp cũ và đã được xử lý.
Việc kiểm tra này rất quan trọng, nếu không độ phức tạp có thể tăng lên đến $O(n m)$.

Theo mặc định, `priority_queue` sắp xếp các phần tử theo thứ tự giảm dần.
Để làm cho nó sắp xếp các phần tử theo thứ tự tăng dần, chúng ta có thể lưu trữ các khoảng cách bị phủ định trong đó, hoặc truyền cho nó một hàm sắp xếp khác.
Chúng ta sẽ thực hiện tùy chọn thứ hai.

```cpp
const int INF = 1000000000;
vector<vector<pair<int, int>>> adj;

void dijkstra(int s, vector<int> & d, vector<int> & p) {
    int n = adj.size();
    d.assign(n, INF);
    p.assign(n, -1);

    d[s] = 0;
    using pii = pair<int, int>;
    priority_queue<pii, vector<pii>, greater<pii>> q;
    q.push({0, s});
    while (!q.empty()) {
        int v = q.top().second;
        int d_v = q.top().first;
        q.pop();
        if (d_v != d[v])
            continue;

        for (auto edge : adj[v]) {
            int to = edge.first;
            int len = edge.second;
            
            if (d[v] + len < d[to]) {
                d[to] = d[v] + len;
                p[to] = v;
                q.push({d[to], to});
            }
        }
    }
}
```

Trong thực tế, phiên bản `priority_queue` nhanh hơn một chút so với phiên bản với `set`.

Thật thú vị, một [báo cáo kỹ thuật năm 2007](https://www3.cs.stonybrook.edu/~rezaul/papers/TR-07-54.pdf) đã kết luận rằng biến thể của thuật toán không sử dụng các thao tác giảm khóa chạy nhanh hơn biến thể có giảm khóa, với khoảng cách hiệu suất lớn hơn cho các đồ thị thưa.

### Loại bỏ các cặp

Bạn có thể cải thiện hiệu suất thêm một chút nếu bạn không lưu trữ các cặp trong các container, mà chỉ lưu trữ các chỉ số của đỉnh.
Trong trường hợp này, chúng ta phải nạp chồng toán tử so sánh:
nó phải so sánh hai đỉnh bằng cách sử dụng các khoảng cách được lưu trữ trong $d[]$.

Kết quả của việc nới lỏng, khoảng cách của một số đỉnh sẽ thay đổi.
Tuy nhiên, cấu trúc dữ liệu sẽ không tự động sắp xếp lại.
Thực tế, việc thay đổi khoảng cách của các đỉnh trong hàng đợi có thể phá hủy cấu trúc dữ liệu.
Như trước đây, chúng ta cần xóa đỉnh trước khi chúng ta nới lỏng nó, và sau đó chèn lại nó sau đó.

Vì chúng ta chỉ có thể xóa khỏi `set`, tối ưu hóa này chỉ áp dụng cho phương pháp `set`, và không hoạt động với việc triển khai `priority_queue`.
Trong thực tế, điều này làm tăng đáng kể hiệu suất, đặc biệt là khi các kiểu dữ liệu lớn hơn được sử dụng để lưu trữ khoảng cách, như `long long` hoặc `double`.

```