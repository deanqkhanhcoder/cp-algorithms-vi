---
tags:
  - Translated
e_maxx_link: bracket_sequences
---

# Dãy ngoặc cân bằng

Một **dãy ngoặc cân bằng** là một chuỗi chỉ bao gồm các dấu ngoặc, sao cho chuỗi này, khi được chèn thêm các số và các phép toán nhất định, sẽ tạo ra một biểu thức toán học hợp lệ.
Về mặt hình thức, bạn có thể định nghĩa dãy ngoặc cân bằng với:

- $e$ (chuỗi rỗng) là một dãy ngoặc cân bằng.
- nếu $s$ là một dãy ngoặc cân bằng, thì $(s)$ cũng vậy.
- nếu $s$ và $t$ là các dãy ngoặc cân bằng, thì $s t$ cũng vậy.

Ví dụ, $(())()$ là một dãy ngoặc cân bằng, nhưng $())($ thì không.

Tất nhiên, bạn cũng có thể định nghĩa các dãy ngoặc khác với nhiều loại ngoặc theo cách tương tự.

Trong bài viết này, chúng ta thảo luận về một số bài toán cổ điển liên quan đến dãy ngoặc cân bằng (để đơn giản, chúng ta sẽ chỉ gọi chúng là dãy): kiểm tra tính hợp lệ, số lượng dãy, tìm dãy tiếp theo theo thứ tự từ điển, tạo tất cả các dãy có kích thước nhất định, tìm chỉ số của dãy, và tạo dãy thứ $k$.
Chúng ta cũng sẽ thảo luận hai biến thể cho các bài toán, phiên bản đơn giản hơn khi chỉ cho phép một loại ngoặc, và trường hợp khó hơn khi có nhiều loại.

## Kiểm tra tính cân bằng

Chúng ta muốn kiểm tra xem một chuỗi đã cho có cân bằng hay không.

Lúc đầu, giả sử chỉ có một loại ngoặc.
Đối với trường hợp này, có một thuật toán rất đơn giản.
Đặt $\text{depth}$ là số lượng ngoặc mở hiện tại.
Ban đầu $\text{depth} = 0$.
Chúng ta lặp qua tất cả các ký tự của chuỗi, nếu ký tự ngoặc hiện tại là ngoặc mở, thì chúng ta tăng $\text{depth}$, nếu không thì giảm nó.
Nếu tại bất kỳ thời điểm nào biến $\text{depth}$ trở nên âm, hoặc cuối cùng nó khác $0$, thì chuỗi đó không phải là một dãy cân bằng.
Nếu không thì nó là một dãy cân bằng.

Nếu có nhiều loại ngoặc, thì thuật toán cần phải được thay đổi.
Thay vì một bộ đếm $\text{depth}$, chúng ta tạo một ngăn xếp, trong đó chúng ta sẽ lưu trữ tất cả các dấu ngoặc mở mà chúng ta gặp.
Nếu ký tự ngoặc hiện tại là ngoặc mở, chúng ta đẩy nó vào ngăn xếp.
Nếu nó là ngoặc đóng, thì chúng ta kiểm tra xem ngăn xếp có rỗng không, và nếu phần tử trên cùng của ngăn xếp có cùng loại với dấu ngoặc đóng hiện tại.
Nếu cả hai điều kiện đều được thỏa mãn, thì chúng ta xóa dấu ngoặc mở khỏi ngăn xếp.
Nếu tại bất kỳ thời điểm nào một trong các điều kiện không được thỏa mãn, hoặc cuối cùng ngăn xếp không rỗng, thì chuỗi đó không cân bằng.
Nếu không thì nó cân bằng.

## Số lượng dãy ngoặc cân bằng

### Công thức

Số lượng dãy ngoặc cân bằng chỉ với một loại ngoặc có thể được tính bằng [số Catalan](catalan-numbers.md).
Số lượng dãy ngoặc cân bằng có độ dài $2n$ ($n$ cặp ngoặc) là:

$$\frac{1}{n+1} \binom{2n}{n}$$

Nếu chúng ta cho phép $k$ loại ngoặc, thì mỗi cặp có thể là bất kỳ loại nào trong $k$ loại (độc lập với các loại khác), do đó số lượng dãy ngoặc cân bằng là:

$$\frac{1}{n+1} \binom{2n}{n} k^n$$

### Quy hoạch động

Mặt khác, các số này có thể được tính bằng **quy hoạch động**.
Đặt $d[n]$ là số lượng dãy ngoặc đều với $n$ cặp ngoặc.
Lưu ý rằng ở vị trí đầu tiên luôn có một dấu ngoặc mở.
Và ở đâu đó sau đó là dấu ngoặc đóng tương ứng của cặp.
Rõ ràng là bên trong cặp này có một dãy ngoặc cân bằng, và tương tự sau cặp này là một dãy ngoặc cân bằng.
Vì vậy, để tính $d[n]$, chúng ta sẽ xem có bao nhiêu dãy ngoặc cân bằng của $i$ cặp ngoặc bên trong cặp ngoặc đầu tiên này, và có bao nhiêu dãy ngoặc cân bằng với $n-1-i$ cặp sau cặp này.
Do đó, công thức có dạng:

$$d[n] = \sum_{i=0}^{n-1} d[i] \cdot d[n-1-i]$$

Giá trị ban đầu cho công thức truy hồi này là $d[0] = 1$.

## Tìm dãy ngoặc cân bằng tiếp theo theo thứ tự từ điển

Ở đây chúng ta chỉ xem xét trường hợp với một loại ngoặc hợp lệ.

Cho một dãy cân bằng, chúng ta phải tìm dãy cân bằng tiếp theo (theo thứ tự từ điển).

Rõ ràng là chúng ta phải tìm dấu ngoặc mở ngoài cùng bên phải, mà chúng ta có thể thay thế bằng một dấu ngoặc đóng mà không vi phạm điều kiện, rằng có nhiều dấu ngoặc đóng hơn dấu ngoặc mở cho đến vị trí này.
Sau khi thay thế vị trí này, chúng ta có thể điền vào phần còn lại của chuỗi bằng chuỗi nhỏ nhất theo thứ tự từ điển: tức là trước tiên với càng nhiều dấu ngoặc mở càng tốt, và sau đó điền vào các vị trí còn lại bằng các dấu ngoặc đóng.
Nói cách khác, chúng ta cố gắng để lại một tiền tố dài nhất có thể không thay đổi, và hậu tố được thay thế bằng hậu tố nhỏ nhất theo thứ tự từ điển.

Để tìm vị trí này, chúng ta có thể lặp qua các ký tự từ phải sang trái, và duy trì sự cân bằng $\text{depth}$ của các dấu ngoặc mở và đóng.
Khi chúng ta gặp một dấu ngoặc mở, chúng ta sẽ giảm $\text{depth}$, và khi chúng ta gặp một dấu ngoặc đóng, chúng ta tăng nó.
Nếu tại một thời điểm nào đó chúng ta gặp một dấu ngoặc mở, và sự cân bằng sau khi xử lý ký hiệu này là dương, thì chúng ta đã tìm thấy vị trí ngoài cùng bên phải mà chúng ta có thể thay đổi.
Chúng ta thay đổi ký hiệu, tính số lượng dấu ngoặc mở và đóng mà chúng ta phải thêm vào phía bên phải, và sắp xếp chúng theo cách nhỏ nhất theo thứ tự từ điển.

Nếu chúng ta không tìm thấy một vị trí phù hợp, thì dãy này đã là dãy lớn nhất có thể, và không có câu trả lời nào.

```{.cpp file=next_balanced_brackets_sequence}
bool next_balanced_sequence(string & s) {
    int n = s.size();
    int depth = 0;
    for (int i = n - 1; i >= 0; i--) {
        if (s[i] == '(')
            depth--;
        else
            depth++;

        if (s[i] == '(' && depth > 0) {
            depth--;
            int open = (n - i - 1 - depth) / 2;
            int close = n - i - 1 - open;
            string next = s.substr(0, i) + ')' + string(open, '(') + string(close, ')');
            s.swap(next);
            return true;
        }
    }
    return false;
}
```

Hàm này tính toán dãy ngoặc cân bằng tiếp theo trong thời gian $O(n)$, và trả về false nếu không có dãy tiếp theo.

## Tìm tất cả các dãy ngoặc cân bằng

Đôi khi cần phải tìm và xuất tất cả các dãy ngoặc cân bằng có độ dài cụ thể $n$.

Để tạo chúng, chúng ta có thể bắt đầu với dãy nhỏ nhất theo thứ tự từ điển $((\dots(())\dots))$, và sau đó tiếp tục tìm các dãy tiếp theo theo thứ tự từ điển với thuật toán được mô tả trong phần trước.

Tuy nhiên, nếu độ dài của dãy không quá dài (ví dụ: $n$ nhỏ hơn $12$), thì chúng ta cũng có thể tạo tất cả các hoán vị một cách thuận tiện với hàm `next_permutation` của C++ STL, và kiểm tra tính cân bằng của mỗi hoán vị.

Chúng cũng có thể được tạo ra bằng cách sử dụng các ý tưởng mà chúng ta đã sử dụng để đếm tất cả các dãy bằng quy hoạch động.
Chúng ta sẽ thảo luận về các ý tưởng trong hai phần tiếp theo.

## Chỉ số của dãy

Cho một dãy ngoặc cân bằng với $n$ cặp ngoặc.
Chúng ta phải tìm chỉ số của nó trong danh sách được sắp xếp theo thứ tự từ điển của tất cả các dãy ngoặc cân bằng với $n$ cặp ngoặc.

Hãy định nghĩa một mảng phụ $d[i][j]$, trong đó $i$ là độ dài của dãy ngoặc (bán cân bằng, mỗi dấu ngoặc đóng có một dấu ngoặc mở tương ứng, nhưng không phải mọi dấu ngoặc mở đều nhất thiết phải có một dấu ngoặc đóng tương ứng), và $j$ là độ cân bằng hiện tại (hiệu số giữa dấu ngoặc mở và đóng).
$d[i][j]$ là số lượng các dãy như vậy phù hợp với các tham số.
Chúng ta sẽ tính các số này chỉ với một loại ngoặc.

Đối với giá trị bắt đầu $i = 0$, câu trả lời là rõ ràng: $d[0][0] = 1$, và $d[0][j] = 0$ đối với $j > 0$.
Bây giờ đặt $i > 0$, và chúng ta xem xét ký tự cuối cùng trong dãy.
Nếu ký tự cuối cùng là một dấu ngoặc mở $($, thì trạng thái trước đó là $(i-1, j-1)$, nếu nó là một dấu ngoặc đóng $)$, thì trạng thái trước đó là $(i-1, j+1)$.
Do đó, chúng ta có được công thức truy hồi:

$$d[i][j] = d[i-1][j-1] + d[i-1][j+1]$$

$d[i][j] = 0$ rõ ràng đúng đối với $j$ âm.
Do đó, chúng ta có thể tính mảng này trong $O(n^2)$.

Bây giờ hãy tạo chỉ số cho một dãy đã cho.

Trước tiên, giả sử chỉ có một loại ngoặc.
Chúng ta sẽ sử dụng bộ đếm $\text{depth}$ cho chúng ta biết độ lồng hiện tại của chúng ta, và lặp qua các ký tự của dãy.
Nếu ký tự hiện tại $s[i]$ bằng $($, thì chúng ta tăng $\text{depth}$.
Nếu ký tự hiện tại $s[i]$ bằng $)$, thì chúng ta phải cộng $d[2n-i-1][\text{depth}+1]$ vào câu trả lời, tính đến tất cả các kết thúc có thể bắt đầu bằng một $($ (là các dãy nhỏ hơn về mặt từ điển), và sau đó giảm $\text{depth}$.

Bây giờ giả sử có $k$ loại ngoặc khác nhau.

Do đó, khi chúng ta xem xét ký tự hiện tại $s[i]$ trước khi tính toán lại $\text{depth}$, chúng ta phải đi qua tất cả các loại ngoặc nhỏ hơn ký tự hiện tại, và cố gắng đặt dấu ngoặc này vào vị trí hiện tại (thu được một độ cân bằng mới $\text{ndepth} = \text{depth} \pm 1$), và cộng số cách để hoàn thành dãy (độ dài $2n-i-1$, độ cân bằng $ndepth$) vào câu trả lời:

$$d[2n - i - 1][\text{ndepth}] \cdot k^{\frac{2n - i - 1 - ndepth}{2}}$$

Công thức này có thể được suy ra như sau:
Đầu tiên chúng ta "quên" rằng có nhiều loại ngoặc, và chỉ lấy câu trả lời $d[2n - i - 1][\text{ndepth}]$.
Bây giờ chúng ta xem xét câu trả lời sẽ thay đổi như thế nào nếu chúng ta có $k$ loại ngoặc.
Chúng ta có $2n - i - 1$ vị trí chưa xác định, trong đó $\text{ndepth}$ đã được xác định trước vì các dấu ngoặc mở.
Nhưng tất cả các dấu ngoặc khác ($(2n - i - 1 - \text{ndepth})/2$ cặp) có thể là bất kỳ loại nào, do đó chúng ta nhân số đó với một lũy thừa của $k$.

## Tìm dãy thứ $k$ {data-toc-label="Finding the k-th sequence"}

Đặt $n$ là số cặp ngoặc trong dãy.
Chúng ta phải tìm dãy ngoặc cân bằng thứ $k$ trong danh sách được sắp xếp theo thứ tự từ điển của tất cả các dãy ngoặc cân bằng cho một $k$ đã cho.

Như trong phần trước, chúng ta tính mảng phụ $d[i][j]$, số lượng các dãy ngoặc bán cân bằng có độ dài $i$ với độ cân bằng $j$.

Đầu tiên, chúng ta bắt đầu chỉ với một loại ngoặc.

Chúng ta sẽ lặp qua các ký tự trong chuỗi chúng ta muốn tạo.
Như trong bài toán trước, chúng ta lưu trữ một bộ đếm $\text{depth}$, độ sâu lồng nhau hiện tại.
Ở mỗi vị trí, chúng ta phải quyết định đặt một dấu ngoặc mở hay một dấu ngoặc đóng. Để đặt một dấu ngoặc mở, $d[2n - i - 1][\text{depth}+1] \ge k$ phải đúng.
Nếu vậy, chúng ta tăng bộ đếm $\text{depth}$, và chuyển sang ký tự tiếp theo.
Nếu không, chúng ta giảm $k$ đi $d[2n - i - 1][\text{depth}+1]$, đặt một dấu ngoặc đóng, và tiếp tục.

```{.cpp file=kth_balances_bracket}
string kth_balanced(int n, int k) {
    vector<vector<int>> d(2*n+1, vector<int>(n+1, 0));
    d[0][0] = 1;
    for (int i = 1; i <= 2*n; i++) {
        d[i][0] = d[i-1][1];
        for (int j = 1; j < n; j++)
            d[i][j] = d[i-1][j-1] + d[i-1][j+1];
        d[i][n] = d[i-1][n-1];
    }

    string ans;
    int depth = 0;
    for (int i = 0; i < 2*n; i++) {
        if (depth + 1 <= n && d[2*n-i-1][depth+1] >= k) {
            ans += '(';
            depth++;
        } else {
            ans += ')';
            if (depth + 1 <= n)
                k -= d[2*n-i-1][depth+1];
            depth--;
        }
    }
    return ans;
}
```

Bây giờ giả sử có $k$ loại ngoặc.
Giải pháp sẽ chỉ khác một chút ở chỗ chúng ta phải nhân giá trị $d[2n-i-1][\text{ndepth}]$ với $k^{(2n-i-1-\text{ndepth})/2}$ và tính đến việc có thể có các loại ngoặc khác nhau cho ký tự tiếp theo.

Đây là một triển khai sử dụng hai loại ngoặc: ngoặc tròn và ngoặc vuông:

```{.cpp file=kth_balances_bracket_multiple}
string kth_balanced2(int n, int k) {
    vector<vector<int>> d(2*n+1, vector<int>(n+1, 0));
    d[0][0] = 1;
    for (int i = 1; i <= 2*n; i++) {
        d[i][0] = d[i-1][1];
        for (int j = 1; j < n; j++)
            d[i][j] = d[i-1][j-1] + d[i-1][j+1];
        d[i][n] = d[i-1][n-1];
    }

    string ans;
    int shift, depth = 0;

    stack<char> st;
    for (int i = 0; i < 2*n; i++) {

        // '('
        shift = ((2*n-i-1-depth-1) / 2);
        if (shift >= 0 && depth + 1 <= n) {
            int cnt = d[2*n-i-1][depth+1] << shift;
            if (cnt >= k) {
                ans += '(';
                st.push('(');
                depth++;
                continue;
            }
            k -= cnt;
        }

        // ')'
        shift = ((2*n-i-1-depth+1) / 2);
        if (shift >= 0 && depth && st.top() == '(') {
            int cnt = d[2*n-i-1][depth-1] << shift;
            if (cnt >= k) {
                ans += ')';
                st.pop();
                depth--;
                continue;
            }
            k -= cnt;
        }
            
        // '['
        shift = ((2*n-i-1-depth-1) / 2);
        if (shift >= 0 && depth + 1 <= n) {
            int cnt = d[2*n-i-1][depth+1] << shift;
            if (cnt >= k) {
                ans += '[';
                st.push('[');
                depth++;
                continue;
            }
            k -= cnt;
        }

        // ']'
        ans += ']';
        st.pop();
        depth--;
    }
    return ans;
}
```