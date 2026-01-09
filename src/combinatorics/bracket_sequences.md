---
tags:
  - Translated
e_maxx_link: bracket_sequences
---

# Dãy ngoặc cân bằng (Balanced bracket sequences) {: #balanced-bracket-sequences}

Một **dãy ngoặc cân bằng** là một chuỗi chỉ bao gồm các dấu ngoặc, sao cho chuỗi này, khi chèn một số số và phép toán toán học nhất định, tạo ra một biểu thức toán học hợp lệ.
Về mặt hình thức, bạn có thể định nghĩa dãy ngoặc cân bằng với:

- $e$ (chuỗi rỗng) là một dãy ngoặc cân bằng.
- nếu $s$ là một dãy ngoặc cân bằng, thì $(s)$ cũng vậy.
- nếu $s$ và $t$ là các dãy ngoặc cân bằng, thì $s t$ cũng vậy.

Ví dụ $(())()$ là một dãy ngoặc cân bằng, nhưng $())($ thì không.

Tất nhiên bạn cũng có thể định nghĩa các dãy ngoặc khác với nhiều loại dấu ngoặc theo cách tương tự.

Trong bài viết này, chúng ta thảo luận về một số bài toán cổ điển liên quan đến dãy ngoặc cân bằng (để đơn giản chúng ta sẽ chỉ gọi chúng là dãy): xác thực, số lượng dãy, tìm dãy tiếp theo theo thứ tự từ điển, tạo tất cả các dãy có kích thước nhất định, tìm chỉ số của dãy, và tạo dãy thứ $k$.
Chúng ta cũng sẽ thảo luận về hai biến thể cho các bài toán, phiên bản đơn giản hơn khi chỉ cho phép một loại dấu ngoặc, và trường hợp khó hơn khi có nhiều loại.

## Kiểm tra tính cân bằng (Balance validation) {: #balance-validation}

Chúng tôi muốn kiểm tra xem một chuỗi đã cho có cân bằng hay không.

Đầu tiên giả sử chỉ có một loại dấu ngoặc.
Đối với trường hợp này tồn tại một thuật toán rất đơn giản.
Gọi $\text{depth}$ là số lượng dấu ngoặc mở hiện tại.
Ban đầu $\text{depth} = 0$.
Chúng ta lặp qua tất cả các ký tự của chuỗi, nếu ký tự dấu ngoặc hiện tại là dấu ngoặc mở, thì chúng ta tăng $\text{depth}$, nếu không chúng ta giảm nó.
Nếu bất cứ lúc nào biến $\text{depth}$ trở nên âm, hoặc cuối cùng nó khác $0$, thì chuỗi không phải là một dãy cân bằng.
Ngược lại thì đúng.

Nếu có nhiều loại dấu ngoặc tham gia, thì thuật toán cần phải thay đổi.
Thay vì một bộ đếm $\text{depth}$ chúng ta tạo một ngăn xếp (stack), trong đó chúng ta sẽ lưu trữ tất cả các dấu ngoặc mở mà chúng ta gặp.
Nếu ký tự dấu ngoặc hiện tại là một dấu ngoặc mở, chúng ta đặt nó vào ngăn xếp.
Nếu nó là một dấu ngoặc đóng, thì chúng ta kiểm tra xem ngăn xếp có không rỗng hay không, và phần tử trên cùng của ngăn xếp có cùng loại với dấu ngoặc đóng hiện tại hay không.
Nếu cả hai điều kiện được đáp ứng, thì chúng ta loại bỏ dấu ngoặc mở khỏi ngăn xếp.
Nếu bất cứ lúc nào một trong các điều kiện không được đáp ứng, hoặc cuối cùng ngăn xếp không rỗng, thì chuỗi không cân bằng.
Ngược lại thì đúng.

## Số lượng dãy cân bằng (Number of balanced sequences) {: #number-of-balanced-sequences}

### Công thức (Formula) {: #formula}

Số lượng dãy ngoặc cân bằng với chỉ một loại dấu ngoặc có thể được tính bằng cách sử dụng [số Catalan](catalan-numbers.md).
Số lượng dãy ngoặc cân bằng có độ dài $2n$ ($n$ cặp dấu ngoặc) là:

$$\frac{1}{n+1} \binom{2n}{n}$$

Nếu chúng ta cho phép $k$ loại dấu ngoặc, thì mỗi cặp có thể thuộc bất kỳ loại nào trong số $k$ loại (độc lập với các loại khác), do đó số lượng dãy ngoặc cân bằng là:

$$\frac{1}{n+1} \binom{2n}{n} k^n$$

### Quy hoạch động (Dynamic programming) {: #dynamic-programming}

Mặt khác, những con số này có thể được tính toán bằng cách sử dụng **quy hoạch động**.
Gọi $d[n]$ là số lượng dãy ngoặc thông thường với $n$ cặp dấu ngoặc.
Lưu ý rằng ở vị trí đầu tiên luôn có một dấu ngoặc mở.
Và đâu đó sau đó là dấu ngoặc đóng tương ứng của cặp.
Rõ ràng là bên trong cặp này có một dãy ngoặc cân bằng, và tương tự sau cặp này có một dãy ngoặc cân bằng.
Vì vậy, để tính $d[n]$, chúng ta sẽ xem xét có bao nhiêu dãy cân bằng của $i$ cặp dấu ngoặc bên trong cặp dấu ngoặc đầu tiên này, và có bao nhiêu dãy cân bằng với $n-1-i$ cặp sau cặp này.
Do đó công thức có dạng:

$$d[n] = \sum_{i=0}^{n-1} d[i] \cdot d[n-1-i]$$

Giá trị ban đầu cho truy hồi này là $d[0] = 1$.

## Tìm dãy cân bằng tiếp theo theo thứ tự từ điển (Finding the lexicographical next balanced sequence) {: #finding-the-lexicographical-next-balanced-sequence}

Ở đây chúng ta chỉ xem xét trường hợp với một loại dấu ngoặc hợp lệ.

Cho một dãy cân bằng, chúng ta phải tìm dãy cân bằng tiếp theo (theo thứ tự từ điển).

Rõ ràng là, chúng ta phải tìm dấu ngoặc mở ngoài cùng bên phải, mà chúng ta có thể thay thế bằng một dấu ngoặc đóng mà không vi phạm điều kiện, rằng có nhiều dấu ngoặc đóng hơn dấu ngoặc mở cho đến vị trí này.
Sau khi thay thế vị trí này, chúng ta có thể điền phần còn lại của chuỗi bằng phần nhỏ nhất theo thứ tự từ điển: tức là đầu tiên với càng nhiều dấu ngoặc mở càng tốt, và sau đó điền vào các vị trí còn lại bằng các dấu ngoặc đóng.
Nói cách khác, chúng tôi cố gắng để lại một tiền tố dài nhất có thể không thay đổi, và hậu tố được thay thế bằng cái nhỏ nhất theo thứ tự từ điển.

Để tìm vị trí này, chúng ta có thể lặp qua ký tự từ phải sang trái, và duy trì độ cân bằng $\text{depth}$ của các dấu ngoặc mở và đóng.
Khi chúng ta gặp một dấu ngoặc mở, chúng ta sẽ giảm $\text{depth}$, và khi chúng ta gặp một dấu ngoặc đóng, chúng ta tăng nó.
Nếu tại một thời điểm nào đó chúng ta gặp một dấu ngoặc mở, và độ cân bằng sau khi xử lý ký hiệu này là dương, thì chúng ta đã tìm thấy vị trí ngoài cùng bên phải mà chúng ta có thể thay đổi.
Chúng ta thay đổi ký hiệu, tính số lượng dấu ngoặc mở và đóng mà chúng ta phải thêm vào phía bên phải, và sắp xếp chúng theo cách nhỏ nhất theo thứ tự từ điển.

Nếu chúng ta không tìm thấy một vị trí phù hợp, thì dãy này đã là dãy lớn nhất có thể, và không có câu trả lời.

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

Hàm này tính toán trong thời gian $O(n)$ dãy ngoặc cân bằng tiếp theo, và trả về false nếu không có dãy tiếp theo.

## Tìm tất cả các dãy cân bằng (Finding all balanced sequences) {: #finding-all-balanced-sequences}

Đôi khi được yêu cầu tìm và xuất tất cả các dãy ngoặc cân bằng có độ dài cụ thể $n$.

Để tạo sau đó, chúng ta có thể bắt đầu với dãy nhỏ nhất theo thứ tự từ điển $((\dots(())\dots))$, và sau đó tiếp tục tìm các dãy tiếp theo theo thứ tự từ điển với thuật toán được mô tả trong phần trước.

Tuy nhiên, nếu độ dài của chuỗi không quá dài (ví dụ $n$ nhỏ hơn $12$), thì chúng ta cũng có thể tạo tất cả các hoán vị một cách thuận tiện với hàm C++ STL `next_permutation`, và kiểm tra từng cái một cho tính cân bằng.

Ngoài ra chúng có thể được tạo bằng cách sử dụng các ý tưởng chúng ta đã sử dụng để đếm tất cả các dãy với quy hoạch động.
Chúng ta sẽ thảo luận về các ý tưởng trong hai phần tiếp theo.

## Chỉ số của dãy (Sequence index) {: #sequence-index}

Cho một dãy ngoặc cân bằng với $n$ cặp dấu ngoặc.
Chúng ta phải tìm chỉ số của nó trong danh sách được sắp xếp theo thứ tự từ điển của tất cả các dãy cân bằng với $n$ cặp dấu ngoặc.

Hãy xác định một mảng phụ trợ $d[i][j]$, trong đó $i$ là độ dài của dãy ngoặc (bán bân bằng, mỗi dấu ngoặc đóng có một dấu ngoặc mở tương ứng, nhưng không phải mọi dấu ngoặc mở nhất thiết phải có một dấu ngoặc đóng tương ứng), và $j$ là độ cân bằng hiện tại (hiệu giữa dấu ngoặc mở và đóng).
$d[i][j]$ là số lượng các dãy như vậy phù hợp với các tham số.
Chúng ta sẽ tính toán các số này chỉ với một loại dấu ngoặc.

Đối với giá trị bắt đầu $i = 0$ câu trả lời là rõ ràng: $d[0][0] = 1$, và $d[0][j] = 0$ cho $j > 0$.
Bây giờ gọi $i > 0$, và chúng ta nhìn vào ký tự cuối cùng trong dãy.
Nếu ký tự cuối cùng là một dấu ngoặc mở $($, thì trạng thái trước đó là $(i-1, j-1)$, nếu nó là một dấu ngoặc đóng $)$, thì trạng thái trước đó là $(i-1, j+1)$.
Do đó chúng ta thu được công thức đệ quy:

$$d[i][j] = d[i-1][j-1] + d[i-1][j+1]$$

$d[i][j] = 0$ giữ đúng rõ ràng cho $j$ âm.
Do đó chúng ta có thể tính mảng này trong $O(n^2)$.

Bây giờ chúng ta hãy tạo chỉ số cho một dãy đã cho.

Đầu tiên gọi chỉ có một loại dấu ngoặc.
Chúng ta sẽ sử dụng bộ đếm $\text{depth}$ cho biết mức độ lồng nhau hiện tại của chúng ta, và lặp qua các ký tự của dãy.
Nếu ký tự hiện tại $s[i]$ bằng $($, thì chúng ta tăng $\text{depth}$.
Nếu ký tự hiện tại $s[i]$ bằng $)$, thì chúng ta phải thêm $d[2n-i-1][\text{depth}+1]$ vào câu trả lời, tính đến tất cả các kết thúc có thể bắt đầu bằng một $($ (là các dãy nhỏ hơn theo thứ tự từ điển), và sau đó giảm $\text{depth}$.

Mới gọi có $k$ loại dấu ngoặc khác nhau.

Do đó, khi chúng ta nhìn vào ký tự hiện tại $s[i]$ trước khi tính toán lại $\text{depth}$, chúng ta phải đi qua tất cả các loại dấu ngoặc nhỏ hơn ký tự hiện tại, và cố gắng đặt dấu ngoặc này vào vị trí hiện tại (thu được độ cân bằng mới $\text{ndepth} = \text{depth} \pm 1$), và thêm số cách để hoàn thành dãy (độ dài $2n-i-1$, cân bằng $ndepth$) vào câu trả lời:

$$d[2n - i - 1][\text{ndepth}] \cdot k^{\frac{2n - i - 1 - ndepth}{2}}$$

Công thức này có thể được suy ra như sau:
Đầu tiên chúng ta "quên" rằng có nhiều loại dấu ngoặc, và chỉ lấy câu trả lời $d[2n - i - 1][\text{ndepth}]$.
Bây giờ chúng ta xem xét câu trả lời sẽ thay đổi như thế nào nếu chúng ta có $k$ loại dấu ngoặc.
Chúng ta có $2n - i - 1$ vị trí chưa xác định, trong đó $\text{ndepth}$ đã được xác định trước vì các dấu ngoặc mở.
Nhưng tất cả các dấu ngoặc khác ($(2n - i - 1 - \text{ndepth})/2$ cặp) có thể thuộc bất kỳ loại nào, do đó chúng ta nhân số đó với một lũy thừa như vậy của $k$.

## Tìm dãy thứ $k$ (Finding the $k$-th sequence) {: #finding-the-k-th-sequence data-toc-label="Finding the k-th sequence"}

Gọi $n$ là số lượng cặp dấu ngoặc trong dãy.
Chúng ta phải tìm dãy cân bằng thứ $k$ trong danh sách được sắp xếp theo thứ tự từ điển của tất cả các dãy cân bằng cho một $k$ đã cho.

Như trong phần trước, chúng ta tính mảng phụ $d[i][j]$, số lượng các dãy ngoặc bán cân bằng có độ dài $i$ với độ cân bằng $j$.

Đầu tiên, chúng ta bắt đầu với chỉ một loại dấu ngoặc.

Chúng ta sẽ lặp qua các ký tự trong chuỗi chúng ta muốn tạo.
Như trong bài toán trước, chúng ta lưu trữ một bộ đếm $\text{depth}$, độ sâu lồng nhau hiện tại.
Tại mỗi vị trí, chúng ta phải quyết định xem nên đặt một dấu ngoặc mở hay dấu ngoặc đóng. Để đặt một dấu ngoặc mở, $d[2n - i - 1][\text{depth}+1] \ge k$ phải đúng.
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

Bây giờ gọi có $k$ loại dấu ngoặc.
Giải pháp sẽ chỉ khác một chút ở chỗ chúng ta phải nhân giá trị $d[2n-i-1][\text{ndepth}]$ với $k^{(2n-i-1-\text{ndepth})/2}$ và tính đến việc có thể có các loại dấu ngoặc khác nhau cho ký tự tiếp theo.

Dưới đây là một cài đặt sử dụng hai loại dấu ngoặc: tròn và vuông:

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
