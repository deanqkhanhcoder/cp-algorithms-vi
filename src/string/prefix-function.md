---
tags:
  - Translated
e_maxx_link: prefix_function
---

# Hàm tiền tố. Thuật toán Knuth–Morris–Pratt (Prefix function. Knuth–Morris–Pratt algorithm) {: #prefix-function-knuth-morris-pratt-algorithm}

## Định nghĩa hàm tiền tố (Prefix function definition) {: #prefix-function-definition}

Bạn được cho một chuỗi $s$ có độ dài $n$.
**Hàm tiền tố** cho chuỗi này được định nghĩa là một mảng $\pi$ có độ dài $n$, trong đó $\pi[i]$ là độ dài của tiền tố thực sự dài nhất của chuỗi con $s[0 \dots i]$ mà cũng là một hậu tố của chuỗi con này.
Tiền tố thực sự của một chuỗi là tiền tố không bằng chính chuỗi đó.
Theo định nghĩa, $\pi[0] = 0$.

Về mặt toán học, định nghĩa của hàm tiền tố có thể được viết như sau:

$$\pi[i] = \max_ {k = 0 \dots i} \{k : s[0 \dots k-1] = s[i-(k-1) \dots i] \}$$

Ví dụ: hàm tiền tố của chuỗi "abcabcd" là $[0, 0, 0, 1, 2, 3, 0]$, và hàm tiền tố của chuỗi "aabaaab" là $[0, 1, 0, 1, 2, 2, 3]$.

## Thuật toán Tầm thường (Trivial Algorithm) {: #trivial-algorithm}

Một thuật toán tuân theo định nghĩa của hàm tiền tố một cách chính xác là như sau:

```{.cpp file=prefix_slow}
vector<int> prefix_function(string s) {
    int n = (int)s.length();
    vector<int> pi(n);
    for (int i = 0; i < n; i++)
        for (int k = 0; k <= i; k++)
            if (s.substr(0, k) == s.substr(i-k+1, k))
                pi[i] = k;
    return pi;
}
```

Dễ thấy rằng độ phức tạp của nó là $O(n^3)$, điều này có chỗ để cải thiện.

## Thuật toán Hiệu quả (Efficient Algorithm) {: #efficient-algorithm}

Thuật toán này được đề xuất bởi Knuth và Pratt và độc lập với họ bởi Morris vào năm 1977.
Nó được sử dụng làm hàm chính của một thuật toán tìm kiếm chuỗi con.

### Tối ưu hóa đầu tiên (First optimization) {: #first-optimization}

Quan sát quan trọng đầu tiên là, các giá trị của hàm tiền tố chỉ có thể tăng tối đa một.

Thật vậy, nếu không, nếu $\pi[i + 1] \gt \pi[i] + 1$, thì chúng ta có thể lấy hậu tố này kết thúc ở vị trí $i + 1$ với độ dài $\pi[i + 1]$ và loại bỏ ký tự cuối cùng khỏi nó.
Chúng ta kết thúc với một hậu tố kết thúc ở vị trí $i$ với độ dài $\pi[i + 1] - 1$, tốt hơn $\pi[i]$, tức là chúng ta gặp mâu thuẫn.

Hình minh họa sau đây cho thấy mâu thuẫn này.
Hậu tố thực sự dài nhất tại vị trí $i$ cũng là một tiền tố có độ dài $2$, và tại vị trí $i+1$ nó có độ dài $4$.
Do đó chuỗi $s_0 ~ s_1 ~ s_2 ~ s_3$ bằng với chuỗi $s_{i-2} ~ s_{i-1} ~ s_i ~ s_{i+1}$, điều đó có nghĩa là các chuỗi $s_0 ~ s_1 ~ s_2$ và $s_{i-2} ~ s_{i-1} ~ s_i$ cũng bằng nhau, do đó $\pi[i]$ phải là $3$.

$$\underbrace{\overbrace{s_0 ~ s_1}^{\pi[i] = 2} ~ s_2 ~ s_3}_{\pi[i+1] = 4} ~ \dots ~ \underbrace{s_{i-2} ~ \overbrace{s_{i-1} ~ s_{i}}^{\pi[i] = 2} ~ s_{i+1}}_{\pi[i+1] = 4}$$

Do đó khi di chuyển đến vị trí tiếp theo, giá trị của hàm tiền tố có thể tăng thêm một, giữ nguyên hoặc giảm đi một lượng nào đó.
Thực tế này đã cho phép chúng ta giảm độ phức tạp của thuật toán xuống $O(n^2)$, bởi vì trong một bước, hàm tiền tố có thể tăng tối đa một.
Tổng cộng hàm có thể tăng tối đa $n$ bước, và do đó cũng chỉ có thể giảm tổng cộng $n$ bước.
Điều này có nghĩa là chúng ta chỉ phải thực hiện $O(n)$ phép so sánh chuỗi, và đạt được độ phức tạp $O(n^2)$.

### Tối ưu hóa thứ hai (Second optimization) {: #second-optimization}

Hãy đi xa hơn, chúng ta muốn loại bỏ các so sánh chuỗi.
Để thực hiện điều này, chúng ta phải sử dụng tất cả thông tin đã được tính toán trong các bước trước đó.

Vì vậy, hãy tính giá trị của hàm tiền tố $\pi$ cho $i + 1$.
Nếu $s[i+1] = s[\pi[i]]$, thì chúng ta có thể nói chắc chắn rằng $\pi[i+1] = \pi[i] + 1$, vì chúng ta đã biết rằng hậu tố ở vị trí $i$ có độ dài $\pi[i]$ bằng với tiền tố có độ dài $\pi[i]$.
Điều này được minh họa lại bằng một ví dụ.

$$\underbrace{\overbrace{s_0 ~ s_1 ~ s_2}^{\pi[i]} ~ \overbrace{s_3}^{s_3 = s_{i+1}}}_{\pi[i+1] = \pi[i] + 1} ~ \dots ~ \underbrace{\overbrace{s_{i-2} ~ s_{i-1} ~ s_{i}}^{\pi[i]} ~ \overbrace{s_{i+1}}^{s_3 = s_{i + 1}}}_{\pi[i+1] = \pi[i] + 1}$$

Nếu không phải trường hợp này, $s[i+1] \neq s[\pi[i]]$, thì chúng ta cần thử một chuỗi ngắn hơn.
Để tăng tốc mọi thứ, chúng ta muốn di chuyển ngay lập tức đến độ dài dài nhất $j \lt \pi[i]$, sao cho tính chất tiền tố ở vị trí $i$ được giữ, tức là $s[0 \dots j-1] = s[i-j+1 \dots i]$:

$$\overbrace{\underbrace{s_0 ~ s_1}_j ~ s_2 ~ s_3}^{\pi[i]} ~ \dots ~ \overbrace{s_{i-3} ~ s_{i-2} ~ \underbrace{s_{i-1} ~ s_{i}}_j}^{\pi[i]} ~ s_{i+1}$$

Thật vậy, nếu chúng ta tìm thấy một độ dài $j$ như vậy, thì chúng ta lại chỉ cần so sánh các ký tự $s[i+1]$ và $s[j]$.
Nếu chúng bằng nhau, thì chúng ta có thể gán $\pi[i+1] = j + 1$.
Ngược lại, chúng ta sẽ cần tìm giá trị lớn nhất nhỏ hơn $j$, mà tính chất tiền tố được giữ, và cứ thế tiếp tục.
Điều này có thể xảy ra cho đến khi $j = 0$.
Nếu sau đó $s[i+1] = s[0]$, chúng ta gán $\pi[i+1] = 1$, và ngược lại $\pi[i+1] = 0$.

Vì vậy, chúng ta đã có một sơ đồ chung của thuật toán.
Câu hỏi duy nhất còn lại là làm thế nào để tìm hiệu quả các độ dài cho $j$.
Hãy tóm tắt lại:
đối với độ dài hiện tại $j$ tại vị trí $i$ mà tính chất tiền tố được giữ, tức là $s[0 \dots j-1] = s[i-j+1 \dots i]$, chúng ta muốn tìm $k \lt j$ lớn nhất, mà tính chất tiền tố được giữ.

$$\overbrace{\underbrace{s_0 ~ s_1}_k ~ s_2 ~ s_3}^j ~ \dots ~ \overbrace{s_{i-3} ~ s_{i-2} ~ \underbrace{s_{i-1} ~ s_{i}}_k}^j ~s_{i+1}$$

Hình minh họa cho thấy, đây phải là giá trị của $\pi[j-1]$, mà chúng ta đã tính toán trước đó.

### Thuật toán cuối cùng (Final algorithm) {: #final-algorithm}

Vì vậy, cuối cùng chúng ta có thể xây dựng một thuật toán không thực hiện bất kỳ so sánh chuỗi nào và chỉ thực hiện $O(n)$ hành động.

Dưới đây là thủ tục cuối cùng:

- Chúng ta tính toán các giá trị tiền tố $\pi[i]$ trong một vòng lặp bằng cách lặp từ $i = 1$ đến $i = n-1$ ($\pi[0]$ chỉ được gán bằng $0$).
- Để tính toán giá trị hiện tại $\pi[i]$, chúng ta đặt biến $j$ biểu thị độ dài của hậu tố tốt nhất cho $i-1$. Ban đầu $j = \pi[i-1]$.
- Kiểm tra xem hậu tố có độ dài $j+1$ có phải cũng là tiền tố hay không bằng cách so sánh $s[j]$ và $s[i]$.
Nếu chúng bằng nhau thì chúng ta gán $\pi[i] = j + 1$, ngược lại chúng ta giảm $j$ xuống $\pi[j-1]$ và lặp lại bước này.
- Nếu chúng ta đã đạt đến độ dài $j = 0$ và vẫn không có khớp, thì chúng ta gán $\pi[i] = 0$ và đi đến chỉ số tiếp theo $i + 1$.

### Cài đặt (Implementation) {: #implementation}

Việc cài đặt kết thúc ngắn gọn và biểu cảm một cách đáng ngạc nhiên.

```{.cpp file=prefix_fast}
vector<int> prefix_function(string s) {
    int n = (int)s.length();
    vector<int> pi(n);
    for (int i = 1; i < n; i++) {
        int j = pi[i-1];
        while (j > 0 && s[i] != s[j])
            j = pi[j-1];
        if (s[i] == s[j])
            j++;
        pi[i] = j;
    }
    return pi;
}
```

Đây là một thuật toán **trực tuyến** (**online**), tức là nó xử lý dữ liệu khi nó đến - ví dụ, bạn có thể đọc các ký tự chuỗi từng cái một và xử lý chúng ngay lập tức, tìm giá trị của hàm tiền tố cho mỗi ký tự tiếp theo.
Thuật toán vẫn yêu cầu lưu trữ chính chuỗi và các giá trị đã tính toán trước đó của hàm tiền tố, nhưng nếu chúng ta biết trước giá trị tối đa $M$ mà hàm tiền tố có thể nhận trên chuỗi, chúng ta chỉ có thể lưu trữ $M+1$ ký tự đầu tiên của chuỗi và cùng một số lượng giá trị của hàm tiền tố.

## Ứng dụng (Applications) {: #applications}

### Tìm kiếm một chuỗi con trong một chuỗi. Thuật toán Knuth-Morris-Pratt (Search for a substring in a string. The Knuth-Morris-Pratt algorithm) {: #search-for-a-substring-in-a-string-the-knuth-morris-pratt-algorithm}

Nhiệm vụ là ứng dụng cổ điển của hàm tiền tố.

Cho một văn bản $t$ và một chuỗi $s$, chúng ta muốn tìm và hiển thị các vị trí của tất cả các lần xuất hiện của chuỗi $s$ trong văn bản $t$.

Để thuận tiện, chúng ta ký hiệu $n$ là độ dài của chuỗi s và $m$ là độ dài của văn bản $t$.

Chúng ta tạo chuỗi $s + \# + t$, trong đó $\#$ là dấu phân cách không xuất hiện trong $s$ cũng như trong $t$.
Hãy tính hàm tiền tố cho chuỗi này.
Bây giờ hãy nghĩ về ý nghĩa của các giá trị của hàm tiền tố, ngoại trừ $n + 1$ mục đầu tiên (thuộc về chuỗi $s$ và dấu phân cách).
Theo định nghĩa, giá trị $\pi[i]$ hiển thị độ dài dài nhất của một chuỗi con kết thúc ở vị trí $i$ trùng khớp với tiền tố.
Nhưng trong trường hợp của chúng ta, điều này không hơn gì khối lớn nhất trùng khớp với $s$ và kết thúc tại vị trí $i$.
Độ dài này không thể lớn hơn $n$ do dấu phân cách.
Nhưng nếu đẳng thức $\pi[i] = n$ đạt được, thì điều đó có nghĩa là chuỗi $s$ xuất hiện hoàn toàn tại vị trí này, tức là nó kết thúc tại vị trí $i$.
Chỉ cần đừng quên rằng các vị trí được lập chỉ mục trong chuỗi $s + \# + t$.

Do đó, nếu tại một vị trí $i$ nào đó chúng ta có $\pi[i] = n$, thì tại vị trí $i - (n + 1) - n + 1 = i - 2n$ trong chuỗi $t$, chuỗi $s$ xuất hiện.

Như đã đề cập trong mô tả tính toán hàm tiền tố, nếu chúng ta biết rằng các giá trị tiền tố không bao giờ vượt quá một giá trị nhất định, thì chúng ta không cần lưu trữ toàn bộ chuỗi và toàn bộ hàm, mà chỉ cần phần đầu của nó.
Trong trường hợp của chúng ta, điều này có nghĩa là chúng ta chỉ cần lưu trữ chuỗi $s + \#$ và các giá trị của hàm tiền tố cho nó.
Chúng ta có thể đọc từng ký tự một của chuỗi $t$ và tính toán giá trị hiện tại của hàm tiền tố.

Do đó, thuật toán Knuth-Morris-Pratt giải quyết vấn đề trong thời gian $O(n + m)$ và bộ nhớ $O(n)$.

### Đếm số lần xuất hiện của mỗi tiền tố (Counting the number of occurrences of each prefix) {: #counting-the-number-of-occurrences-of-each-prefix}

Ở đây chúng ta thảo luận về hai vấn đề cùng một lúc.
Cho một chuỗi $s$ có độ dài $n$.
Trong biến thể đầu tiên của bài toán, chúng ta muốn đếm số lần xuất hiện của mỗi tiền tố $s[0 \dots i]$ trong cùng một chuỗi.
Trong biến thể thứ hai của bài toán, một chuỗi $t$ khác được đưa ra và chúng ta muốn đếm số lần xuất hiện của mỗi tiền tố $s[0 \dots i]$ trong $t$.

Đầu tiên chúng ta giải quyết vấn đề đầu tiên.
Xem xét giá trị của hàm tiền tố $\pi[i]$ tại một vị trí $i$.
Theo định nghĩa, điều đó có nghĩa là tiền tố có độ dài $\pi[i]$ của chuỗi $s$ xuất hiện và kết thúc tại vị trí $i$, và không có tiền tố dài hơn nào tuân theo định nghĩa này.
Đồng thời các tiền tố ngắn hơn có thể kết thúc tại vị trí này.
Không khó để thấy rằng, chúng ta có cùng một câu hỏi mà chúng ta đã trả lời khi chúng ta tính toán chính hàm tiền tố:
Cho một tiền tố có độ dài $j$ là một hậu tố kết thúc tại vị trí $i$, tiền tố nhỏ hơn tiếp theo $\lt j$ cũng là một hậu tố kết thúc tại vị trí $i$ là gì.
Do đó tại vị trí $i$ kết thúc tiền tố có độ dài $\pi[i]$, tiền tố có độ dài $\pi[\pi[i] - 1]$, tiền tố $\pi[\pi[\pi[i] - 1] - 1]$, và cứ thế tiếp tục, cho đến khi chỉ số trở thành không.
Do đó chúng ta có thể tính toán câu trả lời theo cách sau.

```{.cpp file=prefix_count_each_prefix}
vector<int> ans(n + 1);
for (int i = 0; i < n; i++)
    ans[pi[i]]++;
for (int i = n-1; i > 0; i--)
    ans[pi[i-1]] += ans[i];
for (int i = 0; i <= n; i++)
    ans[i]++;
```

Ở đây đối với mỗi giá trị của hàm tiền tố, trước tiên chúng ta đếm xem nó xuất hiện bao nhiêu lần trong mảng $\pi$, và sau đó tính toán các câu trả lời cuối cùng:
nếu chúng ta biết rằng tiền tố độ dài $i$ xuất hiện chính xác $\text{ans}[i]$ lần, thì số này phải được cộng vào số lần xuất hiện của hậu tố dài nhất của nó cũng là một tiền tố.
Cuối cùng chúng ta cần cộng $1$ vào mỗi kết quả, vì chúng ta cũng cần đếm các tiền tố ban đầu.

Bây giờ hãy xem xét vấn đề thứ hai.
Chúng ta áp dụng thủ thuật từ Knuth-Morris-Pratt:
chúng ta tạo chuỗi $s + \# + t$ và tính toán hàm tiền tố của nó.
Sự khác biệt duy nhất so với nhiệm vụ đầu tiên là, chúng ta chỉ quan tâm đến các giá trị tiền tố liên quan đến chuỗi $t$, tức là $\pi[i]$ cho $i \ge n + 1$.
Với các giá trị đó, chúng ta có thể thực hiện các tính toán chính xác như trong nhiệm vụ đầu tiên.

### Số lượng chuỗi con khác nhau trong một chuỗi (The number of different substring in a string) {: #the-number-of-different-substring-in-a-string}

Cho một chuỗi $s$ có độ dài $n$.
Chúng ta muốn tính toán số lượng chuỗi con khác nhau xuất hiện trong nó.

Chúng ta sẽ giải quyết vấn đề này một cách lặp đi lặp lại.
Cụ thể là chúng ta sẽ tìm hiểu, khi biết số lượng chuỗi con khác nhau hiện tại, làm thế nào để tính toán lại số lượng này bằng cách thêm một ký tự vào cuối.

Vì vậy, hãy để $k$ là số lượng chuỗi con khác nhau hiện tại trong $s$, và chúng ta thêm ký tự $c$ vào cuối $s$.
Rõ ràng một số chuỗi con mới kết thúc bằng $c$ sẽ xuất hiện.
Chúng ta muốn đếm các chuỗi con mới này chưa xuất hiện trước đó.

Chúng ta lấy chuỗi $t = s + c$ và đảo ngược nó.
Bây giờ nhiệm vụ được chuyển đổi thành việc tính toán có bao nhiêu tiền tố không xuất hiện ở bất kỳ nơi nào khác.
Nếu chúng ta tính toán giá trị cực đại của hàm tiền tố $\pi_{\text{max}}$ của chuỗi đảo ngược $t$, thì tiền tố dài nhất xuất hiện trong $s$ dài $\pi_{\text{max}}$.
Rõ ràng tất cả các tiền tố có độ dài nhỏ hơn cũng xuất hiện trong đó.

Do đó số lượng chuỗi con mới xuất hiện khi chúng ta thêm một ký tự mới $c$ là $|s| + 1 - \pi_{\text{max}}$.

Vì vậy, đối với mỗi ký tự được thêm vào, chúng ta có thể tính toán số lượng chuỗi con mới trong thời gian $O(n)$, điều này cho độ phức tạp thời gian tổng cộng là $O(n^2)$.

Điều đáng chú ý là, chúng ta cũng có thể tính toán số lượng chuỗi con khác nhau bằng cách thêm các ký tự vào đầu, hoặc bằng cách xóa các ký tự từ đầu hoặc cuối.

### Nén một chuỗi (Compressing a string) {: #compressing-a-string}

Cho một chuỗi $s$ có độ dài $n$.
Chúng ta muốn tìm biểu diễn "nén" ngắn nhất của chuỗi, tức là chúng ta muốn tìm một chuỗi $t$ có độ dài nhỏ nhất sao cho $s$ có thể được biểu diễn dưới dạng nối của một hoặc nhiều bản sao của $t$.

Rõ ràng là chúng ta chỉ cần tìm độ dài của $t$. Biết độ dài, câu trả lời cho vấn đề sẽ là tiền tố của $s$ với độ dài này.

Hãy tính toán hàm tiền tố cho $s$.
Sử dụng giá trị cuối cùng của nó, chúng ta xác định giá trị $k = n - \pi[n - 1]$.
Chúng ta sẽ chỉ ra rằng, nếu $k$ chia hết cho $n$, thì $k$ sẽ là câu trả lời, ngược lại không có nén hiệu quả nào và câu trả lời là $n$.

Giả sử $n$ chia hết cho $k$.
Khi đó chuỗi có thể được phân chia thành các khối có độ dài $k$.
Theo định nghĩa của hàm tiền tố, tiền tố có độ dài $n - k$ sẽ bằng với hậu tố của nó.
Nhưng điều này có nghĩa là khối cuối cùng bằng với khối trước đó.
Và khối trước đó phải bằng khối trước nó.
Và cứ thế tiếp tục.
Kết quả là, hóa ra tất cả các khối đều bằng nhau, do đó chúng ta có thể nén chuỗi $s$ thành độ dài $k$.

Tất nhiên chúng ta vẫn cần chỉ ra rằng đây thực sự là mức tối ưu.
Thật vậy, nếu có một nén nhỏ hơn $k$, thì hàm tiền tố ở cuối sẽ lớn hơn $n - k$.
Do đó $k$ thực sự là câu trả lời.

Bây giờ chúng ta hãy giả sử rằng $n$ không chia hết cho $k$.
Chúng ta chỉ ra rằng điều này ngụ ý rằng độ dài của câu trả lời là $n$.
Chúng ta chứng minh nó bằng mâu thuẫn.
Giả sử tồn tại một câu trả lời, và nén có độ dài $p$ ($p$ chia hết cho $n$).
Thì giá trị cuối cùng của hàm tiền tố phải lớn hơn $n - p$, tức là hậu tố sẽ bao phủ một phần khối đầu tiên.
Bây giờ hãy xem xét khối thứ hai của chuỗi.
Vì tiền tố bằng với hậu tố, và cả tiền tố và hậu tố đều bao phủ khối này và sự dịch chuyển của chúng so với nhau $k$ không chia hết cho độ dài khối $p$ (ngược lại $k$ chia hết cho $n$), nên tất cả các ký tự của khối phải giống hệt nhau.
Nhưng sau đó chuỗi chỉ bao gồm một ký tự lặp đi lặp lại, do đó chúng ta có thể nén nó thành một chuỗi có kích thước $1$, điều này cho $k = 1$, và $k$ chia hết cho $n$.
Mâu thuẫn.

$$\overbrace{s_0 ~ s_1 ~ s_2 ~ s_3}^p ~ \overbrace{s_4 ~ s_5 ~ s_6 ~ s_7}^p$$

$$s_0 ~ s_1 ~ s_2 ~ \underbrace{\overbrace{s_3 ~ s_4 ~ s_5 ~ s_6}^p ~ s_7}_{\pi[7] = 5}$$

$$s_4 = s_3, ~ s_5 = s_4, ~ s_6 = s_5, ~ s_7 = s_6 ~ \Rightarrow ~ s_0 = s_1 = s_2 = s_3$$

### Xây dựng một automaton theo hàm tiền tố (Building an automaton according to the prefix function) {: #building-an-automaton-according-to-the-prefix-function}

Hãy quay lại việc nối hai chuỗi thông qua một dấu phân cách, tức là đối với các chuỗi $s$ và $t$, chúng ta tính toán hàm tiền tố cho chuỗi $s + \# + t$.
Rõ ràng, vì $\#$ là dấu phân cách, giá trị của hàm tiền tố sẽ không bao giờ vượt quá $|s|$.
Suy ra rằng, chỉ cần lưu trữ chuỗi $s + \#$ và các giá trị của hàm tiền tố cho nó là đủ, và chúng ta có thể tính toán hàm tiền tố cho tất cả các ký tự tiếp theo một cách nhanh chóng:

$$\underbrace{s_0 ~ s_1 ~ \dots ~ s_{n-1} ~ \#}_{\text{cần lưu trữ}} ~ \underbrace{t_0 ~ t_1 ~ \dots ~ t_{m-1}}_{\text{không cần lưu trữ}}$$

Thật vậy, trong tình huống như vậy, biết ký tự tiếp theo $c \in t$ và giá trị của hàm tiền tố ở vị trí trước đó là đủ thông tin để tính toán giá trị tiếp theo của hàm tiền tố, mà không cần sử dụng bất kỳ ký tự nào trước đó của chuỗi $t$ và giá trị của hàm tiền tố trong chúng.

Nói cách khác, chúng ta có thể xây dựng một **automaton** (một máy trạng thái hữu hạn): trạng thái trong đó là giá trị hiện tại của hàm tiền tố, và quá trình chuyển đổi từ trạng thái này sang trạng thái khác sẽ được thực hiện thông qua ký tự tiếp theo.

Do đó, ngay cả khi không có chuỗi $t$, chúng ta có thể xây dựng một bảng chuyển đổi như vậy $(\text{old}_\pi, c) \rightarrow \text{new}_\pi$ bằng cách sử dụng cùng thuật toán như để tính toán bảng chuyển đổi:

```{.cpp file=prefix_automaton_slow}
void compute_automaton(string s, vector<vector<int>>& aut) {
    s += '#';
    int n = s.size();
    vector<int> pi = prefix_function(s);
    aut.assign(n, vector<int>(26));
    for (int i = 0; i < n; i++) {
        for (int c = 0; c < 26; c++) {
            int j = i;
            while (j > 0 && 'a' + c != s[j])
                j = pi[j-1];
            if ('a' + c == s[j])
                j++;
            aut[i][c] = j;
        }
    }
}
```

Tuy nhiên, ở dạng này, thuật toán chạy trong thời gian $O(n^2 26)$ cho các chữ cái viết thường của bảng chữ cái.
Lưu ý rằng chúng ta có thể áp dụng quy hoạch động và sử dụng các phần đã được tính toán của bảng.
Bất cứ khi nào chúng ta đi từ giá trị $j$ đến giá trị $\pi[j-1]$, chúng ta thực sự có nghĩa là quá trình chuyển đổi $(j, c)$ dẫn đến cùng một trạng thái với quá trình chuyển đổi như $(\pi[j-1], c)$, và câu trả lời này đã được tính toán chính xác.

```{.cpp file=prefix_automaton_fast}
void compute_automaton(string s, vector<vector<int>>& aut) {
    s += '#';
    int n = s.size();
    vector<int> pi = prefix_function(s);
    aut.assign(n, vector<int>(26));
    for (int i = 0; i < n; i++) {
        for (int c = 0; c < 26; c++) {
            if (i > 0 && 'a' + c != s[i])
                aut[i][c] = aut[pi[i-1]][c];
            else
                aut[i][c] = i + ('a' + c == s[i]);
        }
    }
}
```

Kết quả là chúng ta xây dựng automaton trong thời gian $O(26 n)$.

Khi nào thì một automaton như vậy hữu ích?
Để bắt đầu, hãy nhớ rằng chúng ta sử dụng hàm tiền tố cho chuỗi $s + \# + t$ và các giá trị của nó chủ yếu cho một mục đích duy nhất: tìm tất cả các lần xuất hiện của chuỗi $s$ trong chuỗi $t$.

Do đó lợi ích rõ ràng nhất của automaton này là **tăng tốc tính toán hàm tiền tố** cho chuỗi $s + \# + t$.
Bằng cách xây dựng automaton cho $s + \#$, chúng ta không còn cần lưu trữ chuỗi $s$ hoặc các giá trị của hàm tiền tố trong đó.
Tất cả các chuyển đổi đã được tính toán trong bảng.

Nhưng có một ứng dụng thứ hai, ít rõ ràng hơn.
Chúng ta có thể sử dụng automaton khi chuỗi $t$ là một **chuỗi khổng lồ được xây dựng bằng một số quy tắc**.
Ví dụ, đây có thể là các chuỗi Gray, hoặc một chuỗi được hình thành bởi sự kết hợp đệ quy của một số chuỗi ngắn từ đầu vào.

Để hoàn thiện, chúng ta sẽ giải quyết một vấn đề như vậy:
cho một số $k \le 10^5$ và một chuỗi $s$ có độ dài $\le 10^5$.
Chúng ta phải tính toán số lần xuất hiện của $s$ trong chuỗi Gray thứ $k$.
Nhớ lại rằng các chuỗi Gray được định nghĩa theo cách sau:

$$\begin{align}
g_1 &= \text{"a"}\\
g_2 &= \text{"aba"}\\
g_3 &= \text{"abacaba"}\\
g_4 &= \text{"abacabadabacaba"}
\end{align}$$

Trong những trường hợp như vậy, ngay cả việc xây dựng chuỗi $t$ cũng sẽ là không thể, vì độ dài thiên văn của nó.
Chuỗi Gray thứ $k$ dài $2^k-1$ ký tự.
Tuy nhiên, chúng ta có thể tính toán giá trị của hàm tiền tố ở cuối chuỗi một cách hiệu quả, bằng cách chỉ biết giá trị của hàm tiền tố ở đầu.

Ngoài bản thân automaton, chúng ta cũng tính toán các giá trị $G[i][j]$ - giá trị của automaton sau khi xử lý chuỗi $g_i$ bắt đầu với trạng thái $j$.
Và thêm vào đó chúng ta tính toán các giá trị $K[i][j]$ - số lần xuất hiện của $s$ trong $g_i$, trước khi trong quá trình xử lý $g_i$ bắt đầu với trạng thái $j$.
Thực ra $K[i][j]$ là số lần hàm tiền tố nhận giá trị $|s|$ trong khi thực hiện các thao tác.
Câu trả lời cho vấn đề sau đó sẽ là $K[k][0]$.

Làm thế nào chúng ta có thể tính toán các giá trị này?
Đầu tiên các giá trị cơ bản là $G[0][j] = j$ và $K[0][j] = 0$.
Và tất cả các giá trị tiếp theo có thể được tính toán từ các giá trị trước đó và sử dụng automaton.
Để tính toán giá trị cho một số $i$, chúng ta nhớ rằng chuỗi $g_i$ bao gồm $g_{i-1}$, ký tự thứ $i$ của bảng chữ cái, và $g_{i-1}$.
Do đó automaton sẽ đi vào trạng thái:

$$\text{mid} = \text{aut}[G[i-1][j]][i]$$

$$G[i][j] = G[i-1][\text{mid}]$$

Các giá trị cho $K[i][j]$ cũng có thể được đếm một cách dễ dàng.

$$K[i][j] = K[i-1][j] + (\text{mid} == |s|) + K[i-1][\text{mid}]$$

Vì vậy, chúng ta có thể giải quyết vấn đề cho các chuỗi Gray, và tương tự như vậy cũng có một số lượng lớn các vấn đề tương tự khác.
Ví dụ, cùng một phương pháp chính xác cũng giải quyết vấn đề sau:
chúng ta được cho một chuỗi $s$ và một số mẫu $t_i$, mỗi mẫu được chỉ định như sau:
nó là một chuỗi các ký tự thông thường, và có thể có một số lần chèn đệ quy của các chuỗi trước đó có dạng $t_k^{\text{cnt}}$, điều đó có nghĩa là tại nơi này chúng ta phải chèn chuỗi $t_k$ $\text{cnt}$ lần.
Một ví dụ về các mẫu như vậy:

$$\begin{align}
t_1 &= \text{"abdeca"}\\
t_2 &= \text{"abc"} + t_1^{30} + \text{"abd"}\\
t_3 &= t_2^{50} + t_1^{100}\\
t_4 &= t_2^{10} + t_3^{100}
\end{align}$$

Các phép thay thế đệ quy thổi phồng chuỗi lên, sao cho độ dài của chúng có thể đạt tới bậc $100^{100}$.

Chúng ta phải tìm số lần chuỗi $s$ xuất hiện trong mỗi chuỗi.

Vấn đề có thể được giải quyết theo cùng một cách bằng cách xây dựng automaton của hàm tiền tố, và sau đó chúng ta tính toán các chuyển đổi trong cho mỗi mẫu bằng cách sử dụng các kết quả trước đó.

## Bài tập (Practice Problems) {: #practice-problems}

* [UVA # 455 "Periodic Strings"](http://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=396)
* [UVA # 11022 "String Factoring"](http://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1963)
* [UVA # 11452 "Dancing the Cheeky-Cheeky"](http://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=2447)
* [UVA 12604 - Caesar Cipher](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=4282)
* [UVA 12467 - Secret Word](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=3911)
* [UVA 11019 - Matrix Matcher](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1960)
* [SPOJ - Pattern Find](http://www.spoj.com/problems/NAJPF/)
* [SPOJ - A Needle in the Haystack](https://www.spoj.com/problems/NHAY/)
* [Codeforces - Anthem of Berland](http://codeforces.com/contest/808/problem/G)
* [Codeforces - MUH and Cube Walls](http://codeforces.com/problemset/problem/471/D)
* [Codeforces - Prefixes and Suffixes](https://codeforces.com/contest/432/problem/D)
