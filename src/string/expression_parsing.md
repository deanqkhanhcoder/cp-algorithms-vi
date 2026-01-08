---
tags:
  - Translated
e_maxx_link: expressions_parsing
---

# Phân tích biểu thức (Expression parsing) {: #expression-parsing}

Một chuỗi chứa biểu thức toán học bao gồm các số và các toán tử khác nhau được đưa ra.
Chúng ta phải tính giá trị của nó trong $O(n)$, trong đó $n$ là độ dài của chuỗi.

Thuật toán được thảo luận ở đây chuyển một biểu thức sang cái gọi là **ký pháp Ba Lan ngược** (**reverse Polish notation**) (một cách tường minh hoặc ngầm định), và tính toán giá trị biểu thức này.

## Ký pháp Ba Lan ngược (Reverse Polish notation) {: #reverse-polish-notation}

Ký pháp Ba Lan ngược là một dạng viết các biểu thức toán học, trong đó các toán tử nằm sau các toán hạng của chúng.
Ví dụ biểu thức sau

$$a + b * c * d + (e - f) * (g * h + i)$$

có thể được viết bằng ký pháp Ba Lan ngược theo cách sau:

$$a b c * d * + e f - g h * i + * +$$

Ký pháp Ba Lan ngược được phát triển bởi nhà triết học và chuyên gia khoa học máy tính người Úc Charles Hamblin vào giữa những năm 1950 trên cơ sở ký pháp Ba Lan, được đề xuất vào năm 1920 bởi nhà toán học người Ba Lan Jan Łukasiewicz.

Sự tiện lợi của ký pháp Ba Lan ngược là các biểu thức ở dạng này rất **dễ tính toán** trong thời gian tuyến tính.
Chúng ta sử dụng một ngăn xếp, ban đầu rỗng.
Chúng ta sẽ duyệt qua các toán hạng và toán tử của biểu thức trong ký pháp Ba Lan ngược.
Nếu phần tử hiện tại là một số, thì chúng ta đặt giá trị lên đỉnh ngăn xếp, nếu phần tử hiện tại là một toán tử, thì chúng ta lấy hai phần tử trên cùng từ ngăn xếp, thực hiện phép toán và đặt kết quả trở lại đỉnh ngăn xếp.
Cuối cùng sẽ có chính xác một phần tử còn lại trong ngăn xếp, đó sẽ là giá trị của biểu thức.

Rõ ràng việc tính toán đơn giản này chạy trong thời gian $O(n)$.

## Phân tích các biểu thức đơn giản (Parsing of simple expressions) {: #parsing-of-simple-expressions}

Hiện tại chúng tôi chỉ xem xét một vấn đề đơn giản hóa:
chúng tôi giả định rằng tất cả các toán tử là **hai ngôi** (**binary**) (tức là chúng lấy hai đối số), và tất cả đều **kết hợp trái** (**left-associative**) (nếu độ ưu tiên bằng nhau, chúng được thực hiện từ trái sang phải).
Dấu ngoặc đơn được cho phép.

Chúng ta sẽ thiết lập hai ngăn xếp: một cho số, và một cho toán tử và dấu ngoặc đơn.
Ban đầu cả hai ngăn xếp đều rỗng.
Đối với ngăn xếp thứ hai, chúng tôi sẽ duy trì điều kiện là tất cả các hoạt động được sắp xếp theo thứ tự ưu tiên giảm dần nghiêm ngặt.
Nếu có dấu ngoặc đơn trên ngăn xếp, thì mỗi khối toán tử (tương ứng với một cặp dấu ngoặc đơn) được sắp xếp, và toàn bộ ngăn xếp không nhất thiết phải được sắp xếp.

Chúng ta sẽ duyệt qua các ký tự của biểu thức từ trái sang phải.
Nếu ký tự hiện tại là một chữ số, thì chúng ta đặt giá trị của số này lên ngăn xếp.
Nếu ký tự hiện tại là dấu ngoặc đơn mở, thì chúng ta đặt nó lên ngăn xếp.
Nếu ký tự hiện tại là dấu ngoặc đơn đóng, chúng ta thực hiện tất cả các toán tử trên ngăn xếp cho đến khi chúng ta đến dấu ngoặc mở (nói cách khác là chúng ta thực hiện tất cả các phép toán bên trong dấu ngoặc đơn).
Cuối cùng, nếu ký tự hiện tại là một toán tử, thì trong khi đỉnh ngăn xếp có một toán tử có độ ưu tiên tương đương hoặc cao hơn, chúng ta sẽ thực hiện phép toán này và đặt phép toán mới lên ngăn xếp.

Sau khi chúng ta xử lý toàn bộ chuỗi, một số toán tử vẫn có thể nằm trong ngăn xếp, vì vậy chúng ta thực hiện chúng.

Đây là việc triển khai phương pháp này cho bốn toán tử $+$ $-$ $*$ $/$:

```{.cpp file=expression_parsing_simple}
bool delim(char c) {
    return c == ' ';
}

bool is_op(char c) {
    return c == '+' || c == '-' || c == '*' || c == '/';
}

int priority (char op) {
    if (op == '+' || op == '-')
        return 1;
    if (op == '*' || op == '/')
        return 2;
    return -1;
}

void process_op(stack<int>& st, char op) {
    int r = st.top(); st.pop();
    int l = st.top(); st.pop();
    switch (op) {
        case '+': st.push(l + r); break;
        case '-': st.push(l - r); break;
        case '*': st.push(l * r); break;
        case '/': st.push(l / r); break;
    }
}

int evaluate(string& s) {
    stack<int> st;
    stack<char> op;
    for (int i = 0; i < (int)s.size(); i++) {
        if (delim(s[i]))
            continue;
        
        if (s[i] == '(') {
            op.push('(');
        } else if (s[i] == ')') {
            while (op.top() != '(') {
                process_op(st, op.top());
                op.pop();
            }
            op.pop();
        } else if (is_op(s[i])) {
            char cur_op = s[i];
            while (!op.empty() && priority(op.top()) >= priority(cur_op)) {
                process_op(st, op.top());
                op.pop();
            }
            op.push(cur_op);
        } else {
            int number = 0;
            while (i < (int)s.size() && isalnum(s[i]))
                number = number * 10 + s[i++] - '0';
            --i;
            st.push(number);
        }
    }

    while (!op.empty()) {
        process_op(st, op.top());
        op.pop();
    }
    return st.top();
}
```

Như vậy chúng ta đã học cách tính giá trị của một biểu thức trong $O(n)$, đồng thời chúng ta đã sử dụng ngầm định ký pháp Ba Lan ngược.
Bằng cách sửa đổi một chút cách thực hiện ở trên, cũng có thể thu được biểu thức trong ký pháp Ba Lan ngược ở dạng tường minh.

## Toán tử một ngôi (Unary operators) {: #unary-operators}

Bây giờ giả sử rằng biểu thức cũng chứa các toán tử **một ngôi** (**unary**) (các toán tử lấy một đối số).
Cộng một ngôi và trừ một ngôi là những ví dụ phổ biến về các toán tử như vậy.

Một trong những khác biệt trong trường hợp này, là chúng ta cần xác định xem toán tử hiện tại là một ngôi hay hai ngôi.

Bạn có thể nhận thấy rằng trước một toán tử một ngôi, luôn có một toán tử khác hoặc dấu ngoặc đơn mở, hoặc không có gì cả (nếu nó nằm ở ngay đầu biểu thức).
Ngược lại, trước một toán tử hai ngôi sẽ luôn có một toán hạng (số) hoặc dấu ngoặc đơn đóng.
Do đó, thật dễ dàng để gắn cờ xem toán tử tiếp theo có thể là một ngôi hay không.

Ngoài ra chúng ta cần thực hiện một toán tử một ngôi và một toán tử hai ngôi khác nhau.
Và chúng ta cần chọn độ ưu tiên của toán tử một ngôi cao hơn tất cả các toán tử hai ngôi.

Ngoài ra cần lưu ý rằng, một số toán tử một ngôi (ví dụ: cộng một ngôi và trừ một ngôi) thực sự là **kết hợp phải** (**right-associative**).

## Kết hợp phải (Right-associativity) {: #right-associativity}

Kết hợp phải có nghĩa là, bất cứ khi nào các độ ưu tiên bằng nhau, các toán tử phải được đánh giá từ phải sang trái.

Như đã lưu ý ở trên, các toán tử một ngôi thường kết hợp phải.
Một ví dụ khác cho toán tử kết hợp phải là toán tử lũy thừa ($a \wedge b \wedge c$ thường được hiểu là $a^{b^c}$ và không phải là $(a^b)^c$).

Chúng ta cần tạo ra sự khác biệt nào để xử lý chính xác các toán tử kết hợp phải?
Hóa ra những thay đổi là rất nhỏ.
Sự khác biệt duy nhất sẽ là, nếu các độ ưu tiên bằng nhau, chúng ta sẽ hoãn việc thực hiện phép toán kết hợp phải.

Dòng duy nhất cần được thay thế là
```cpp
while (!op.empty() && priority(op.top()) >= priority(cur_op))
```
bằng
```cpp
while (!op.empty() && (
        (left_assoc(cur_op) && priority(op.top()) >= priority(cur_op)) ||
        (!left_assoc(cur_op) && priority(op.top()) > priority(cur_op))
    ))
```
trong đó `left_assoc` là một hàm quyết định xem một toán tử có phải là kết hợp trái hay không.

Dưới đây là một triển khai cho các toán tử hai ngôi $+$ $-$ $*$ $/$ và các toán tử một ngôi $+$ và $-$.

```{.cpp file=expression_parsing_unary}
bool delim(char c) {
    return c == ' ';
}

bool is_op(char c) {
    return c == '+' || c == '-' || c == '*' || c == '/';
}

bool is_unary(char c) {
    return c == '+' || c=='-';
}

int priority (char op) {
    if (op < 0) // unary operator
        return 3;
    if (op == '+' || op == '-')
        return 1;
    if (op == '*' || op == '/')
        return 2;
    return -1;
}

void process_op(stack<int>& st, char op) {
    if (op < 0) {
        int l = st.top(); st.pop();
        switch (-op) {
            case '+': st.push(l); break;
            case '-': st.push(-l); break;
        }
    } else {
        int r = st.top(); st.pop();
        int l = st.top(); st.pop();
        switch (op) {
            case '+': st.push(l + r); break;
            case '-': st.push(l - r); break;
            case '*': st.push(l * r); break;
            case '/': st.push(l / r); break;
        }
    }
}

int evaluate(string& s) {
    stack<int> st;
    stack<char> op;
    bool may_be_unary = true;
    for (int i = 0; i < (int)s.size(); i++) {
        if (delim(s[i]))
            continue;
        
        if (s[i] == '(') {
            op.push('(');
            may_be_unary = true;
        } else if (s[i] == ')') {
            while (op.top() != '(') {
                process_op(st, op.top());
                op.pop();
            }
            op.pop();
            may_be_unary = false;
        } else if (is_op(s[i])) {
            char cur_op = s[i];
            if (may_be_unary && is_unary(cur_op))
                cur_op = -cur_op;
            while (!op.empty() && (
                    (cur_op >= 0 && priority(op.top()) >= priority(cur_op)) ||
                    (cur_op < 0 && priority(op.top()) > priority(cur_op))
                )) {
                process_op(st, op.top());
                op.pop();
            }
            op.push(cur_op);
            may_be_unary = true;
        } else {
            int number = 0;
            while (i < (int)s.size() && isalnum(s[i]))
                number = number * 10 + s[i++] - '0';
            --i;
            st.push(number);
            may_be_unary = false;
        }
    }

    while (!op.empty()) {
        process_op(st, op.top());
        op.pop();
    }
    return st.top();
}
```
