---
tags:
  - Translated
e_maxx_link: preflow_push_faster
---

# Luồng cực đại - Phương pháp Push-relabel cải tiến (Maximum flow - Push-relabel method improved) {: #maximum-flow-push-relabel-method-improved}

Chúng ta sẽ sửa đổi [phương pháp push-relabel](push-relabel.md) để đạt được thời gian chạy tốt hơn.

## Mô tả (Description) {: #description}

Sửa đổi cực kỳ đơn giản:
Trong bài viết trước chúng ta đã chọn một đỉnh có dư thừa mà không có bất kỳ quy tắc cụ thể nào.
Nhưng hóa ra, nếu chúng ta luôn chọn các đỉnh có **độ cao lớn nhất**, và áp dụng các thao tác push và relabel trên chúng, thì độ phức tạp sẽ trở nên tốt hơn.
Hơn nữa, để chọn các đỉnh có độ cao lớn nhất, chúng ta thực sự không cần bất kỳ cấu trúc dữ liệu nào, chúng ta chỉ cần lưu trữ các đỉnh có độ cao lớn nhất trong một danh sách, và tính toán lại danh sách sau khi tất cả chúng đã được xử lý (sau đó các đỉnh có độ cao thấp hơn sẽ được thêm vào danh sách), hoặc bất cứ khi nào xuất hiện một đỉnh mới có dư thừa và độ cao lớn hơn (sau khi gán lại nhãn cho một đỉnh).

Bất chấp sự đơn giản, sửa đổi này làm giảm độ phức tạp đi rất nhiều.
Chính xác hơn, độ phức tạp của thuật toán thu được là $O(V E + V^2 \sqrt{E})$, trong trường hợp xấu nhất là $O(V^3)$.

Sửa đổi này được đề xuất bởi Cheriyan và Maheshwari vào năm 1989.

## Cài đặt (Implementation) {: #implementation}

```cpp
const int inf = 1000000000;

int n;
vector<vector<int>> capacity, flow;
vector<int> height, excess;

void push(int u, int v)
{
    int d = min(excess[u], capacity[u][v] - flow[u][v]);
    flow[u][v] += d;
    flow[v][u] -= d;
    excess[u] -= d;
    excess[v] += d;
}

void relabel(int u)
{
    int d = inf;
    for (int i = 0; i < n; i++) {
        if (capacity[u][i] - flow[u][i] > 0)
            d = min(d, height[i]);
    }
    if (d < inf)
        height[u] = d + 1;
}

vector<int> find_max_height_vertices(int s, int t) {
    vector<int> max_height;
    for (int i = 0; i < n; i++) {
        if (i != s && i != t && excess[i] > 0) {
            if (!max_height.empty() && height[i] > height[max_height[0]])
                max_height.clear();
            if (max_height.empty() || height[i] == height[max_height[0]])
                max_height.push_back(i);
        }
    }
    return max_height;
}

int max_flow(int s, int t)
{
    height.assign(n, 0);
    height[s] = n;
    flow.assign(n, vector<int>(n, 0));
    excess.assign(n, 0);
    excess[s] = inf;
    for (int i = 0; i < n; i++) {
        if (i != s)
            push(s, i);
    }

    vector<int> current;
    while (!(current = find_max_height_vertices(s, t)).empty()) {
        for (int i : current) {
            bool pushed = false;
            for (int j = 0; j < n && excess[i]; j++) {
                if (capacity[i][j] - flow[i][j] > 0 && height[i] == height[j] + 1) {
                    push(i, j);
                    pushed = true;
                }
            }
            if (!pushed) {
                relabel(i);
                break;
            }
        }
    }

    return excess[t];
}
```
