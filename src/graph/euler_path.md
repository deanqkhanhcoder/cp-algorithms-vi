---
title: Tìm đường đi Euler trong O(M)
tags:
  - Translated
e_maxx_link: euler_path
---
# Tìm đường đi Euler trong $O(M)$

Đường đi Euler là một đường đi trong đồ thị đi qua tất cả các cạnh của nó đúng một lần.
Chu trình Euler là một đường đi Euler mà là một chu trình.

Bài toán là tìm đường đi Euler trong một **đồ thị đa vô hướng có vòng lặp**.

## Thuật toán

Đầu tiên, chúng ta có thể kiểm tra xem có đường đi Euler hay không.
Chúng ta có thể sử dụng định lý sau. Một chu trình Euler tồn tại khi và chỉ khi bậc của tất cả các đỉnh là chẵn.
Và một đường đi Euler tồn tại khi và chỉ khi số lượng các đỉnh có bậc lẻ là hai (hoặc không, trong trường hợp tồn tại một chu trình Euler).
Ngoài ra, tất nhiên, đồ thị phải đủ liên thông (tức là, nếu bạn loại bỏ tất cả các đỉnh cô lập khỏi nó, bạn sẽ nhận được một đồ thị liên thông).

Để tìm đường đi Euler / chu trình Euler, chúng ta có thể sử dụng chiến lược sau:
Chúng ta tìm tất cả các chu trình đơn giản và kết hợp chúng thành một - đây sẽ là chu trình Euler.
Nếu đồ thị là sao cho đường đi Euler không phải là một chu trình, thì thêm cạnh còn thiếu, tìm chu trình Euler, sau đó loại bỏ cạnh thừa.

Tìm kiếm tất cả các chu trình và kết hợp chúng có thể được thực hiện bằng một thủ tục đệ quy đơn giản:

```nohighlight
procedure FindEulerPath(V)
  1. duyệt qua tất cả các cạnh đi ra từ đỉnh V;
       loại bỏ cạnh này khỏi đồ thị,
       và gọi FindEulerPath từ đầu kia của cạnh này;
  2. thêm đỉnh V vào câu trả lời.
```

Độ phức tạp của thuật toán này rõ ràng là tuyến tính so với số lượng cạnh.

Nhưng chúng ta có thể viết cùng một thuật toán ở phiên bản không đệ quy:

```nohighlight
ngăn xếp St;
đặt đỉnh bắt đầu vào St;
cho đến khi St rỗng
  gọi V là giá trị ở đỉnh St;
  nếu bậc(V) = 0, thì
    thêm V vào câu trả lời;
    xóa V khỏi đỉnh St;
  ngược lại
    tìm bất kỳ cạnh nào đi ra từ V;
    loại bỏ nó khỏi đồ thị;
    đặt đầu kia của cạnh này vào St;
```

Dễ dàng kiểm tra sự tương đương của hai dạng thuật toán này. Tuy nhiên, dạng thứ hai rõ ràng là nhanh hơn, và mã sẽ hiệu quả hơn nhiều.

## Bài toán Domino

Chúng tôi đưa ra ở đây một bài toán chu trình Euler cổ điển - bài toán Domino.

Có $N$ quân domino, như đã biết, ở cả hai đầu của Domino có một số được viết (thường từ 1 đến 6, nhưng trong trường hợp của chúng ta điều đó không quan trọng). Bạn muốn đặt tất cả các quân domino thành một hàng sao cho các số trên hai quân domino liền kề bất kỳ, được viết ở mặt chung của chúng, trùng khớp. Domino được phép xoay.

Phát biểu lại bài toán. Gọi các số được viết ở dưới đáy là các đỉnh của đồ thị, và các quân domino là các cạnh của đồ thị này (mỗi Domino với các số $(a,b)$ là các cạnh $(a,b)$ và $(b, a)$). Khi đó, bài toán của chúng ta được quy về bài toán tìm đường đi Euler trong đồ thị này.

## Cài đặt

Chương trình dưới đây tìm kiếm và xuất ra một vòng lặp hoặc đường đi Euler trong một đồ thị, hoặc xuất ra $-1$ nếu nó không tồn tại.

Đầu tiên, chương trình kiểm tra bậc của các đỉnh: nếu không có đỉnh nào có bậc lẻ, thì đồ thị có một chu trình Euler, nếu có $2$ đỉnh có bậc lẻ, thì trong đồ thị chỉ có một đường đi Euler (nhưng không có chu trình Euler), nếu có nhiều hơn $2$ đỉnh như vậy, thì trong đồ thị không có chu trình Euler hay đường đi Euler.
Để tìm đường đi Euler (không phải là một chu trình), chúng ta làm như sau: nếu $V1$ và $V2$ là hai đỉnh có bậc lẻ, thì chỉ cần thêm một cạnh $(V1, V2)$, trong đồ thị kết quả chúng ta tìm chu trình Euler (nó sẽ rõ ràng tồn tại), và sau đó loại bỏ cạnh "giả" $(V1, V2)$ khỏi câu trả lời.
Chúng ta sẽ tìm chu trình Euler chính xác như đã mô tả ở trên (phiên bản không đệ quy), và đồng thời ở cuối thuật toán này, chúng ta sẽ kiểm tra xem đồ thị có liên thông hay không (nếu đồ thị không liên thông, thì ở cuối thuật toán, một số cạnh sẽ vẫn còn trong đồ thị, và trong trường hợp này, chúng ta cần in ra $-1$).
Cuối cùng, chương trình tính đến việc có thể có các đỉnh cô lập trong đồ thị.

Lưu ý rằng chúng ta sử dụng ma trận kề trong bài toán này.
Việc triển khai này cũng xử lý việc tìm kiếm tiếp theo bằng vũ lực, yêu cầu lặp lại toàn bộ hàng trong ma trận.
Một cách tốt hơn sẽ là lưu trữ đồ thị dưới dạng danh sách kề, và loại bỏ các cạnh trong $O(1)$ và đánh dấu các cạnh ngược trong một danh sách riêng.
Bằng cách này, chúng ta có thể đạt được một thuật toán $O(N)$.

```cpp
int main() {
    int n;
    vector<vector<int>> g(n, vector<int>(n));
    // đọc đồ thị trong ma trận kề

    vector<int> deg(n);
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j)
            deg[i] += g[i][j];
    }

    int first = 0;
    while (first < n && !deg[first])
        ++first;
    if (first == n) {
        cout << -1;
        return 0;
    }

    int v1 = -1, v2 = -1;
    bool bad = false;
    for (int i = 0; i < n; ++i) {
        if (deg[i] & 1) {
            if (v1 == -1)
                v1 = i;
            else if (v2 == -1)
                v2 = i;
            else
                bad = true;
        }
    }

    if (v1 != -1)
        ++g[v1][v2], ++g[v2][v1];

    stack<int> st;
    st.push(first);
    vector<int> res;
    while (!st.empty()) {
        int v = st.top();
        int i;
        for (i = 0; i < n; ++i)
            if (g[v][i])
                break;
        if (i == n) {
            res.push_back(v);
            st.pop();
        } else {
            --g[v][i];
            --g[i][v];
            st.push(i);
        }
    }

    if (v1 != -1) {
        for (size_t i = 0; i + 1 < res.size(); ++i) {
            if ((res[i] == v1 && res[i + 1] == v2) ||
                (res[i] == v2 && res[i + 1] == v1)) {
                vector<int> res2;
                for (size_t j = i + 1; j < res.size(); ++j)
                    res2.push_back(res[j]);
                for (size_t j = 1; j <= i; ++j)
                    res2.push_back(res[j]);
                res = res2;
                break;
            }
        }
    }

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (g[i][j])
                bad = true;
        }
    }

    if (bad) {
        cout << -1;
    } else {
        for (int x : res)
            cout << x << " ";
    }
}
```
### Bài tập thực hành:

- [CSES : Mail Delivery](https://cses.fi/problemset/task/1691)
- [CSES : Teleporters Path](https://cses.fi/problemset/task/1693)
- [Codeforces - Melody](https://codeforces.com/contest/2110/problem/E)
- [Codeforces - Tanya and Password](https://codeforces.com/contest/508/problem/D)