---
title: Thuật toán Manacher - Tìm tất cả các chuỗi con đối xứng trong O(N)
tags:
  - Translated
e_maxx_link: palindromes_count
---
# Thuật toán Manacher - Tìm tất cả các chuỗi con đối xứng trong $O(N)$ (Manacher's Algorithm - Finding all sub-palindromes in $O(N)$) {: #manachers-algorithm-finding-all-sub-palindromes-in-o-n}

## Phát biểu (Statement) {: #statement}

Cho chuỗi $s$ với độ dài $n$. Tìm tất cả các cặp $(i, j)$ sao cho chuỗi con $s[i\dots j]$ là một palindrome (chuỗi đối xứng). Chuỗi $t$ là một palindrome khi $t = t_{rev}$ ($t_{rev}$ là chuỗi đảo ngược của $t$).

## Phát biểu chính xác hơn (More precise statement) {: #more-precise-statement}

Trong trường hợp xấu nhất, chuỗi có thể có tới $O(n^2)$ chuỗi con đối xứng, và thoạt nhìn có vẻ như không có thuật toán tuyến tính nào cho vấn đề này.

Nhưng thông tin về các palindrome có thể được lưu giữ **một cách nhỏ gọn**: đối với mỗi vị trí $i$, chúng ta sẽ tìm số lượng các palindrome không rỗng có tâm tại vị trí này.

Các palindrome có chung tâm tạo thành một chuỗi liên tiếp, nghĩa là nếu chúng ta có một palindrome có độ dài $l$ ở tâm $i$, chúng ta cũng có các palindrome có độ dài $l-2$, $l-4$ và cứ thế tiếp tục cũng ở tâm $i$. Do đó, chúng ta sẽ thu thập thông tin về tất cả các chuỗi con đối xứng theo cách này.

Các palindrome có độ dài lẻ và chẵn được tính riêng biệt là $d_{odd}[i]$ và $d_{even}[i]$. Đối với các palindrome có độ dài chẵn, chúng tôi giả sử rằng chúng có tâm ở vị trí $i$ nếu hai ký tự trung tâm của chúng là $s[i]$ và $s[i-1]$.

Ví dụ, chuỗi $s = abababc$ có ba palindrome có độ dài lẻ với tâm ở vị trí $s[3] = b$, tức là $d_{odd}[3] = 3$:

$$a\ \overbrace{b\ a\ \underbrace{b}_{s_3}\ a\ b}^{d_{odd}[3]=3} c$$

Và chuỗi $s = cbaabd$ có hai palindrome có độ dài chẵn với tâm ở vị trí $s[3] = a$, tức là $d_{even}[3] = 2$:

$$c\ \overbrace{b\ a\ \underbrace{a}_{s_3}\ b}^{d_{even}[3]=2} d$$

Thật đáng ngạc nhiên là có một thuật toán, đủ đơn giản, tính toán các "mảng palindrome" này $d_{odd}[]$ và $d_{even}[]$ trong thời gian tuyến tính. Thuật toán được mô tả trong bài viết này.

## Giải pháp (Solution) {: #solution}

Nói chung, vấn đề này có nhiều giải pháp: với [Băm chuỗi](string-hashing.md) nó có thể được giải quyết trong $O(n\cdot \log n)$, và với [Cây hậu tố](suffix-tree-ukkonen.md) và LCA nhanh vấn đề này có thể được giải quyết trong $O(n)$.

Nhưng phương pháp được mô tả ở đây **đủ** đơn giản hơn và có hằng số ẩn ít hơn trong độ phức tạp thời gian và bộ nhớ. Thuật toán này được phát hiện bởi **Glenn K. Manacher** vào năm 1975.

Một cách hiện đại khác để giải quyết vấn đề này và đối phó với các palindrome nói chung là thông qua cái gọi là cây palindrome, hoặc eertree.

## Thuật toán tầm thường (Trivial algorithm) {: #trivial-algorithm}

Để tránh sự mơ hồ trong mô tả thêm, chúng tôi biểu thị "thuật toán tầm thường" là gì.

Đó là thuật toán thực hiện những điều sau đây. Đối với mỗi vị trí tâm $i$, nó cố gắng tăng câu trả lời lên một miễn là có thể, so sánh một cặp ký tự tương ứng mỗi lần.

Một thuật toán như vậy là chậm, nó chỉ có thể tính toán câu trả lời trong $O(n^2)$.

Việc cài đặt thuật toán tầm thường là:

```cpp
vector<int> manacher_odd_trivial(string s) {
    int n = s.size();
    s = "$" + s + "^";
    vector<int> p(n + 2);
    for(int i = 1; i <= n; i++) {
        while(s[i - p[i]] == s[i + p[i]]) {
            p[i]++;
        }
    }
    return vector<int>(begin(p) + 1, end(p) - 1);
}
```

Các ký tự kết thúc `$` và `^` đã được sử dụng để tránh xử lý các đầu của chuỗi một cách riêng biệt.

## Thuật toán Manacher (Manacher's algorithm) {: #manachers-algorithm}

Chúng tôi mô tả thuật toán để tìm tất cả các chuỗi con đối xứng có độ dài lẻ, tức là để tính $d_{odd}[]$.

Để tính toán nhanh, chúng tôi sẽ duy trì **các biên giới độc quyền $(l, r)$** của (chuỗi con) palindrome (con) ngoài cùng bên phải được tìm thấy (tức là (chuỗi con) palindrome ngoài cùng bên phải hiện tại là $s[l+1] s[l+2] \dots s[r-1]$). Ban đầu chúng tôi đặt $l = 0, r = 1$, tương ứng với chuỗi rỗng.

Vì vậy, chúng tôi muốn tính $d_{odd}[i]$ cho $i$ tiếp theo, và tất cả các giá trị trước đó trong $d_{odd}[]$ đã được tính toán. Chúng tôi thực hiện như sau:

* Nếu $i$ nằm ngoài chuỗi con đối xứng hiện tại, tức là $i \geq r$, chúng tôi sẽ chỉ khởi chạy thuật toán tầm thường.
    
    Vì vậy, chúng tôi sẽ tăng $d_{odd}[i]$ liên tiếp và kiểm tra mỗi lần xem chuỗi con ngoài cùng bên phải hiện tại $[i - d_{odd}[i]\dots i + d_{odd}[i]]$ có phải là palindrome hay không. Khi chúng tôi tìm thấy sự không khớp đầu tiên hoặc gặp ranh giới của $s$, chúng tôi sẽ dừng lại. Trong trường hợp này, cuối cùng chúng tôi đã tính toán $d_{odd}[i]$. Sau đó, chúng ta không được quên cập nhật $(l, r)$. $r$ nên được cập nhật theo cách mà nó đại diện cho chỉ số cuối cùng của chuỗi con đối xứng ngoài cùng bên phải hiện tại.

* Bây giờ hãy xem xét trường hợp khi $i \le r$. Chúng tôi sẽ cố gắng trích xuất một số thông tin từ các giá trị đã được tính toán trong $d_{odd}[]$. Vì vậy, hãy tìm vị trí "gương" của $i$ trong chuỗi con đối xứng $(l, r)$, tức là chúng tôi sẽ nhận được vị trí $j = l + (r - i)$, và chúng tôi kiểm tra giá trị của $d_{odd}[j]$. Bởi vì $j$ là vị trí đối xứng với $i$ so với $(l+r)/2$, chúng tôi **hầu như luôn luôn** có thể gán $d_{odd}[i] = d_{odd}[j]$. Minh họa về điều này (palindrome xung quanh $j$ thực sự được "sao chép" vào palindrome xung quanh $i$):
    
    $$
    \ldots\ 
    \overbrace{
        s_{l+1}\ \ldots\ 
        \underbrace{
            s_{j-d_{odd}[j]+1}\ \ldots\ s_j\ \ldots\ s_{j+d_{odd}[j]-1}\ 
        }_\text{palindrome}\ 
        \ldots\ 
        \underbrace{
            s_{i-d_{odd}[j]+1}\ \ldots\ s_i\ \ldots\ s_{i+d_{odd}[j]-1}\ 
        }_\text{palindrome}\ 
        \ldots\ s_{r-1}\ 
    }^\text{palindrome}\ 
    \ldots
    $$
    
    Nhưng có một **trường hợp khó khăn** cần được xử lý chính xác: khi palindrome "bên trong" chạm đến biên giới của cái "bên ngoài", tức là $j - d_{odd}[j] \le l$ (hoặc, giống nhau là $i + d_{odd}[j] \ge r$). Bởi vì tính đối xứng bên ngoài palindrome "bên ngoài" không được đảm bảo, chỉ cần gán $d_{odd}[i] = d_{odd}[j]$ sẽ không chính xác: chúng tôi không có đủ dữ liệu để nói rằng palindrome ở vị trí $i$ có cùng độ dài.
    
    Thực ra, chúng ta nên hạn chế độ dài của palindrome của mình ngay bây giờ, tức là gán $d_{odd}[i] = r - i$, để xử lý các tình huống như vậy một cách chính xác. Sau đó, chúng tôi sẽ chạy thuật toán tầm thường sẽ cố gắng tăng $d_{odd}[i]$ trong khi có thể.
    
    Minh họa trường hợp này (palindrome với tâm $j$ bị hạn chế để phù hợp với palindrome "bên ngoài"):
    
    $$
    \ldots\ 
    \overbrace{
        \underbrace{
            s_{l+1}\ \ldots\ s_j\ \ldots\ s_{j+(j-l)-1}\ 
        }_\text{palindrome}\ 
        \ldots\ 
        \underbrace{
            s_{i-(r-i)+1}\ \ldots\ s_i\ \ldots\ s_{r-1}
        }_\text{palindrome}\ 
    }^\text{palindrome}\ 
    \underbrace{
        \ldots \ldots \ldots \ldots \ldots
    }_\text{thử di chuyển đến đây}
    $$
    
    Trong hình minh họa cho thấy mặc dù palindrome có tâm $j$ có thể lớn hơn và đi ra ngoài palindrome "bên ngoài", nhưng với $i$ là trung tâm, chúng tôi chỉ có thể sử dụng phần hoàn toàn phù hợp với palindrome "bên ngoài". Nhưng câu trả lời cho vị trí $i$ ($d_{odd}[i]$) có thể lớn hơn nhiều so với phần này, vì vậy tiếp theo chúng tôi sẽ chạy thuật toán tầm thường của mình sẽ cố gắng phát triển nó ra ngoài palindrome "bên ngoài" của chúng tôi, tức là đến vùng "thử di chuyển đến đây".

Một lần nữa, chúng ta không được quên cập nhật các giá trị $(l, r)$ sau khi tính mỗi $d_{odd}[i]$.

## Độ phức tạp của thuật toán Manacher (Complexity of Manacher's algorithm) {: #complexity-of-manachers-algorithm}

Thoạt nhìn, không rõ ràng rằng thuật toán này có độ phức tạp thời gian tuyến tính, bởi vì chúng ta thường chạy thuật toán ngây thơ trong khi tìm kiếm câu trả lời cho một vị trí cụ thể.

Tuy nhiên, một phân tích cẩn thận hơn cho thấy thuật toán là tuyến tính. Trong thực tế, [thuật toán xây dựng hàm Z](z-function.md), trông tương tự như thuật toán này, cũng hoạt động trong thời gian tuyến tính.

Chúng ta có thể nhận thấy rằng mọi lần lặp của thuật toán tầm thường đều tăng $r$ thêm một. Ngoài ra $r$ không thể giảm trong thuật toán. Vì vậy, thuật toán tầm thường sẽ thực hiện tổng cộng $O(n)$ lần lặp.

Các phần khác của thuật toán Manacher hoạt động rõ ràng trong thời gian tuyến tính. Do đó, chúng ta nhận được độ phức tạp thời gian $O(n)$.

## Cài đặt thuật toán Manacher (Implementation of Manacher's algorithm) {: #implementation-of-manachers-algorithm}

Để tính $d_{odd}[]$, chúng ta nhận được mã sau. Những điều cần lưu ý:

 - $i$ là chỉ số của chữ cái tâm của palindrome hiện tại.
 - Nếu $i$ vượt quá $r$, $d_{odd}[i]$ được khởi tạo thành 0.
 - Nếu $i$ không vượt quá $r$, $d_{odd}[i]$ được khởi tạo thành $d_{odd}[j]$, trong đó $j$ là vị trí gương của $i$ trong $(l,r)$, hoặc $d_{odd}[i]$ bị giới hạn ở kích thước của palindrome "bên ngoài".
 - Vòng lặp while biểu thị thuật toán tầm thường. Chúng tôi khởi chạy nó bất kể giá trị của $k$.
 - Nếu kích thước của palindrome có tâm tại $i$ là $x$, thì $d_{odd}[i]$ lưu trữ $\frac{x+1}{2}$.

```{.cpp file=manacher_odd}
vector<int> manacher_odd(string s) {
    int n = s.size();
    s = "$" + s + "^";
    vector<int> p(n + 2);
    int l = 0, r = 1;
    for(int i = 1; i <= n; i++) {
        p[i] = min(r - i, p[l + (r - i)]);
        while(s[i - p[i]] == s[i + p[i]]) {
            p[i]++;
        }
        if(i + p[i] > r) {
            l = i - p[i], r = i + p[i];
        }
    }
    return vector<int>(begin(p) + 1, end(p) - 1);
}
```

## Làm việc với tính chẵn lẻ (Working with parities) {: #working-with-parities}

Mặc dù có thể triển khai thuật toán Manacher cho độ dài lẻ và chẵn một cách riêng biệt, nhưng việc triển khai phiên bản cho độ dài chẵn thường được coi là khó khăn hơn, vì nó kém tự nhiên hơn và dễ dẫn đến lỗi lệch một đơn vị (off-by-one errors).

Để giảm thiểu điều này, có thể giảm toàn bộ vấn đề xuống trường hợp khi chúng ta chỉ xử lý các palindrome có độ dài lẻ. Để làm điều này, chúng ta có thể đặt thêm ký tự `#` giữa mỗi chữ cái trong chuỗi và cả ở đầu và cuối chuỗi:

$$abcbcba \to \#a\#b\#c\#b\#c\#b\#a\#,$$

$$d = [1,2,1,2,1,4,1,8,1,4,1,2,1,2,1].$$

Như bạn có thể thấy, $d[2i]=2 d_{even}[i]+1$ và $d[2i+1]=2 d_{odd}[i]$ trong đó $d$ biểu thị mảng Manacher cho các palindrome có độ dài lẻ trong chuỗi được nối `#`, trong khi $d_{odd}$ và $d_{even}$ tương ứng với các mảng được xác định ở trên trong chuỗi ban đầu.

Thật vậy, các ký tự `#` không ảnh hưởng đến các palindrome có độ dài lẻ, vẫn tập trung vào các ký tự của chuỗi ban đầu, nhưng bây giờ các palindrome có độ dài chẵn của chuỗi ban đầu là các palindrome có độ dài lẻ của chuỗi mới tập trung vào các ký tự `#`.

Lưu ý rằng $d[2i]$ và $d[2i+1]$ về cơ bản là độ dài tăng thêm $1$ của các palindrome có độ dài lẻ và chẵn lớn nhất có tâm tại $i$ tương ứng.

Việc giảm được thực hiện theo cách sau:

```cpp
vector<int> manacher(string s) {
    string t;
    for(auto c: s) {
        t += string("#") + c;
    }
    auto res = manacher_odd(t + "#");
    return vector<int>(begin(res) + 1, end(res) - 1);
}
```

Để đơn giản, việc chia mảng thành $d_{odd}$ và $d_{even}$ cũng như tính toán rõ ràng của chúng bị bỏ qua.

## Bài tập (Problems) {: #problems}

- [Library Checker - Enumerate Palindromes](https://judge.yosupo.jp/problem/enumerate_palindromes)
- [Longest Palindrome](https://cses.fi/problemset/task/1111)
- [UVA 11475 - Extend to Palindrome](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=26&page=show_problem&problem=2470)
- [GYM - (Q) QueryreuQ](https://codeforces.com/gym/101806/problem/Q)
- [CF - Prefix-Suffix Palindrome](https://codeforces.com/contest/1326/problem/D2)
- [SPOJ - Number of Palindromes](https://www.spoj.com/problems/NUMOFPAL/)
- [Kattis - Palindromes](https://open.kattis.com/problems/palindromes)
