---
tags:
  - Original
---

# Tổng Minkowski của các đa giác lồi

## Định nghĩa
Xét hai tập hợp $A$ và $B$ gồm các điểm trên một mặt phẳng. Tổng Minkowski $A + B$ được định nghĩa là $\{a + b| a \in A, b \in B\}$.
Ở đây, chúng ta sẽ xem xét trường hợp khi $A$ và $B$ bao gồm các đa giác lồi $P$ và $Q$ cùng với phần bên trong của chúng.
Trong suốt bài viết này, chúng ta sẽ đồng nhất các đa giác với các dãy có thứ tự của các đỉnh của chúng, để ký hiệu như $|P|$ hoặc
$P_i$ có ý nghĩa.
Hóa ra tổng của các đa giác lồi $P$ và $Q$ là một đa giác lồi có nhiều nhất $|P| + |Q|$ đỉnh.

## Thuật toán

Ở đây chúng ta coi các đa giác được liệt kê theo chu kỳ, tức là $P_{|P|} = P_0,\ Q_{|Q|} = Q_0$ và cứ thế.

Vì kích thước của tổng là tuyến tính theo kích thước của các đa giác ban đầu, chúng ta nên nhắm đến việc tìm một thuật toán thời gian tuyến tính.
Giả sử rằng cả hai đa giác đều được sắp xếp ngược chiều kim đồng hồ. Xét các dãy cạnh $\{\overrightarrow{P_iP_{i+1}}\}$
và $\{\overrightarrow{Q_jQ_{j+1}}\}$ được sắp xếp theo góc cực. Chúng tôi khẳng định rằng dãy các cạnh của $P + Q$ có thể thu được bằng cách hợp nhất
hai dãy này bảo toàn thứ tự góc cực và thay thế các vector cùng hướng liên tiếp bằng tổng của chúng. Việc sử dụng trực tiếp ý tưởng này dẫn đến
một thuật toán thời gian tuyến tính, tuy nhiên, việc khôi phục các đỉnh của $P + Q$ từ dãy các cạnh đòi hỏi phải cộng lặp đi lặp lại các vector,
điều này có thể gây ra các vấn đề về độ chính xác không mong muốn nếu chúng ta làm việc với các tọa độ dấu phẩy động, vì vậy chúng tôi sẽ mô tả một sửa đổi nhỏ của ý tưởng này.


Đầu tiên, chúng ta nên sắp xếp lại các đỉnh theo cách sao cho đỉnh đầu tiên của mỗi đa giác có tọa độ y thấp nhất (trong trường hợp có nhiều đỉnh như vậy, hãy chọn đỉnh có tọa độ x nhỏ nhất). Sau đó, các cạnh của cả hai đa giác
sẽ được sắp xếp theo góc cực, vì vậy không cần phải sắp xếp chúng thủ công.
Bây giờ chúng ta tạo hai con trỏ $i$ (trỏ đến một đỉnh của $P$) và $j$ (trỏ đến một đỉnh của $Q$), cả hai ban đầu được đặt thành 0.
Chúng ta lặp lại các bước sau trong khi $i < |P|$ hoặc $j < |Q|$.

1. Nối $P_i + Q_j$ vào $P + Q$.

2. So sánh các góc cực của $\overrightarrow{P_iP_{i + 1}}$ và $\overrightarrow{Q_jQ_{j+1}}$.

3. Tăng con trỏ tương ứng với góc nhỏ nhất (nếu các góc bằng nhau, tăng cả hai).

## Trực quan hóa

Đây là một hình dung hay, có thể giúp bạn hiểu những gì đang diễn ra.

<div style="text-align: center;">
  <img src="minkowski.gif" alt="Trực quan">
</div>

## Khoảng cách giữa hai đa giác
Một trong những ứng dụng phổ biến nhất của tổng Minkowski là tính khoảng cách giữa hai đa giác lồi (hoặc đơn giản là kiểm tra xem chúng có giao nhau không).
Khoảng cách giữa hai đa giác lồi $P$ và $Q$ được định nghĩa là $\min\limits_{a \in P, b \in Q} ||a - b||$. Người ta có thể lưu ý rằng
khoảng cách luôn đạt được giữa hai đỉnh hoặc một đỉnh và một cạnh, vì vậy chúng ta có thể dễ dàng tìm thấy khoảng cách trong $O(|P||Q|)$. Tuy nhiên,
với việc sử dụng thông minh tổng Minkowski, chúng ta có thể giảm độ phức tạp xuống còn $O(|P| + |Q|)$.

Nếu chúng ta phản xạ $Q$ qua điểm $(0, 0)$ để thu được đa giác $-Q$, bài toán thu gọn về việc tìm khoảng cách nhỏ nhất giữa một điểm trong
$P + (-Q)$ và $(0, 0)$. Chúng ta có thể tìm khoảng cách đó trong thời gian tuyến tính bằng cách sử dụng ý tưởng sau.
Nếu $(0, 0)$ nằm bên trong hoặc trên biên của đa giác, khoảng cách là $0$, nếu không thì khoảng cách đạt được giữa $(0, 0)$ và một đỉnh hoặc cạnh nào đó của đa giác.
Vì tổng Minkowski có thể được tính toán
trong thời gian tuyến tính, chúng ta có được một thuật toán thời gian tuyến tính để tìm khoảng cách giữa hai đa giác lồi.

## Cài đặt
Dưới đây là việc triển khai tổng Minkowski cho các đa giác có các điểm nguyên. Lưu ý rằng trong trường hợp này, tất cả các tính toán có thể được thực hiện bằng số nguyên vì
thay vì tính toán các góc cực và so sánh chúng trực tiếp, chúng ta có thể xem xét dấu của tích có hướng của hai vector.

```{.cpp file=minkowski}
struct pt{
    long long x, y;
    pt operator + (const pt & p) const {
        return pt{x + p.x, y + p.y};
    }
    pt operator - (const pt & p) const {
        return pt{x - p.x, y - p.y};
    }
    long long cross(const pt & p) const {
        return x * p.y - y * p.x;
    }
};

void reorder_polygon(vector<pt> & P){
    size_t pos = 0;
    for(size_t i = 1; i < P.size(); i++){
        if(P[i].y < P[pos].y || (P[i].y == P[pos].y && P[i].x < P[pos].x))
            pos = i;
    }
    rotate(P.begin(), P.begin() + pos, P.end());
}

vector<pt> minkowski(vector<pt> P, vector<pt> Q){
    // đỉnh đầu tiên phải là đỉnh thấp nhất
    reorder_polygon(P);
    reorder_polygon(Q);
    // chúng ta phải đảm bảo chỉ số vòng
    P.push_back(P[0]);
    P.push_back(P[1]);
    Q.push_back(Q[0]);
    Q.push_back(Q[1]);
    // phần chính
    vector<pt> result;
    size_t i = 0, j = 0;
    while(i < P.size() - 2 || j < Q.size() - 2){
        result.push_back(P[i] + Q[j]);
        auto cross = (P[i + 1] - P[i]).cross(Q[j + 1] - Q[j]);
        if(cross >= 0 && i < P.size() - 2)
            ++i;
        if(cross <= 0 && j < Q.size() - 2)
            ++j;
    }
    return result;
}

```

## Các bài toán
 * [Codeforces 87E Mogohu-Rea Idol](https://codeforces.com/problemset/problem/87/E)
 * [Codeforces 1195F Geometers Anonymous Club](https://codeforces.com/contest/1195/problem/F)
 * [TIMUS 1894 Non-Flying Weather](https://acm.timus.ru/problem.aspx?space=1&num=1894)