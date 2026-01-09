---
tags:
  - Translated
e_maxx_link: string_tandems
---

# Tìm kiếm lặp lại (Finding repetitions) {: #finding-repetitions}

Cho một chuỗi $s$ có độ dài $n$.

Một **sự lặp lại** (**repetition**) là hai lần xuất hiện của một chuỗi liên tiếp nhau.
Nói cách khác, một sự lặp lại có thể được mô tả bởi một cặp chỉ số $i < j$ sao cho chuỗi con $s[i \dots j]$ bao gồm hai chuỗi giống hệt nhau được viết sau nhau.

Thách thức là **tìm tất cả các lần lặp lại** trong một chuỗi $s$ nhất định.
Hoặc một nhiệm vụ đơn giản hóa: tìm **bất kỳ** sự lặp lại nào hoặc tìm sự lặp lại **dài nhất**.

Thuật toán được mô tả ở đây được công bố vào năm 1982 bởi Main và Lorentz.

## Ví dụ (Example) {: #example}

Hãy xem xét các sự lặp lại trong chuỗi ví dụ sau:

$$acababaee$$

Chuỗi chứa ba lần lặp lại sau:

- $s[2 \dots 5] = abab$
- $s[3 \dots 6] = baba$
- $s[7 \dots 8] = ee$

Một ví dụ khác:

$$abaaba$$

Ở đây chỉ có hai lần lặp lại:

- $s[0 \dots 5] = abaaba$
- $s[2 \dots 3] = aa$

## Số lượng lặp lại (Number of repetitions) {: #number-of-repetitions}

Nói chung, có thể có tới $O(n^2)$ lần lặp lại trong một chuỗi có độ dài $n$.
Một ví dụ rõ ràng là một chuỗi bao gồm $n$ lần cùng một chữ cái, trong trường hợp này, bất kỳ chuỗi con nào có độ dài chẵn đều là một sự lặp lại.
Nói chung, bất kỳ chuỗi tuần hoàn nào có chu kỳ ngắn sẽ chứa rất nhiều sự lặp lại.

Mặt khác, thực tế này không ngăn cản việc tính toán số lần lặp lại trong thời gian $O(n \log n)$, bởi vì thuật toán có thể đưa ra các lần lặp lại ở dạng nén, theo nhóm của nhiều mảnh cùng một lúc.

Thậm chí còn có khái niệm mô tả các nhóm chuỗi con tuần hoàn với các bộ bốn kích thước.
Người ta đã chứng minh rằng số lượng các nhóm như vậy tối đa là tuyến tính đối với độ dài chuỗi.

Ngoài ra, đây là một số kết quả thú vị hơn liên quan đến số lần lặp lại:

  - Số lượng lặp lại nguyên thủy (những lần lặp lại có nửa không phải là lặp lại) tối đa là $O(n \log n)$.
  - Nếu chúng ta mã hóa các lần lặp lại bằng các bộ số (được gọi là bộ ba Crochemore) $(i,~ p,~ r)$ (trong đó $i$ là vị trí bắt đầu, $p$ độ dài của chuỗi con lặp lại và $r$ số lần lặp lại), thì tất cả các lần lặp lại có thể được mô tả bằng $O(n \log n)$ bộ ba như vậy.
  - Chuỗi Fibonacci, được định nghĩa là
    
    \[\begin{align}
    t_0 &= a, \\\\
    t_1 &= b, \\\\
    t_i &= t_{i-1} + t_{i-2},
    \end{align}\]
    
    là tuần hoàn "mạnh".
    Số lượng lặp lại trong chuỗi Fibonacci $f_i$, ngay cả khi được nén bằng bộ ba Crochemore, là $O(f_n \log f_n)$.
    Số lượng lặp lại nguyên thủy cũng là $O(f_n \log f_n)$.

## Thuật toán Main-Lorentz (Main-Lorentz algorithm) {: #main-lorentz-algorithm}

Ý tưởng đằng sau thuật toán Main-Lorentz là **chia để trị** (**divide-and-conquer**).

Nó chia chuỗi ban đầu thành một nửa và tính toán số lần lặp lại nằm hoàn toàn trong mỗi nửa bằng hai lệnh gọi đệ quy.
Sau đó đến phần khó khăn.
Thuật toán tìm tất cả các lần lặp lại bắt đầu ở nửa đầu và kết thúc ở nửa sau (chúng tôi sẽ gọi là **lặp lại chéo** - **crossing repetitions**).
Đây là phần thiết yếu của thuật toán Main-Lorentz và chúng ta sẽ thảo luận chi tiết về nó ở đây.

Độ phức tạp của các thuật toán chia để trị được nghiên cứu kỹ lưỡng.
[Định lý Master](https://vi.wikipedia.org/wiki/%C4%90%E1%BB%8Bnh_l%C3%BD_th%E1%BB%A3) nói rằng, chúng ta sẽ kết thúc với thuật toán $O(n \log n)$, nếu chúng ta có thể tính toán các lần lặp lại chéo trong thời gian $O(n)$.

### Tìm kiếm các lặp lại chéo (Search for crossing repetitions) {: #search-for-crossing-repetitions}

Vì vậy, chúng ta muốn tìm tất cả các lần lặp lại như vậy bắt đầu ở nửa đầu của chuỗi, hãy gọi nó là $u$, và kết thúc ở nửa sau, hãy gọi nó là $v$:

$$s = u + v$$

Độ dài của chúng xấp xỉ bằng độ dài của $s$ chia cho hai.

Xem xét một lần lặp lại tùy ý và nhìn vào ký tự ở giữa (chính xác hơn là ký tự đầu tiên của nửa sau của lần lặp lại).
Tức là nếu sự lặp lại là một chuỗi con $s[i \dots j]$, thì ký tự ở giữa là $(i + j + 1) / 2$.

Chúng tôi gọi một sự lặp lại là **trái** (**left**) hoặc **phải** (**right**) tùy thuộc vào chuỗi nào ký tự này nằm ở - trong chuỗi $u$ hay trong chuỗi $v$.
Nói cách khác, một chuỗi được gọi là trái, nếu phần lớn của nó nằm trong $u$, nếu không chúng tôi gọi nó là phải.

Bây giờ chúng ta sẽ thảo luận về cách tìm **tất cả các lặp lại trái**.
Việc tìm tất cả các lặp lại phải có thể được thực hiện theo cùng một cách.

Chúng ta hãy biểu thị độ dài của lần lặp lại bên trái bằng $2l$ (tức là mỗi nửa của lần lặp lại có độ dài $l$).
Xem xét ký tự đầu tiên của lần lặp lại rơi vào chuỗi $v$ (nó ở vị trí $|u|$ trong chuỗi $s$).
Nó trùng với ký tự $l$ vị trí trước nó, hãy biểu thị vị trí này là $cntr$.

Chúng tôi sẽ cố định vị trí này $cntr$, và **tìm kiếm tất cả các lần lặp lại tại vị trí này** $cntr$.

Ví dụ:

$$c ~ \underset{cntr}{a} ~ c ~ | ~ a ~ d ~ a$$

Các đường thẳng đứng chia hai nửa.
Ở đây chúng ta cố định vị trí $cntr = 1$, và tại vị trí này chúng ta tìm thấy sự lặp lại $caca$.

Rõ ràng là, nếu chúng ta cố định vị trí $cntr$, chúng ta đồng thời cố định độ dài của các lần lặp lại có thể: $l = |u| - cntr$.
Khi chúng ta biết cách tìm các lần lặp lại này, chúng ta sẽ lặp lại trên tất cả các giá trị có thể có cho $cntr$ từ $0$ đến $|u|-1$, và tìm tất cả các lần lặp lại chéo trái có độ dài $l = |u|,~ |u|-1,~ \dots, 1$.

### Tiêu chí cho các lặp lại chéo trái (Criterion for left crossing repetitions) {: #criterion-for-left-crossing-repetitions}

Bây giờ, làm thế nào chúng ta có thể tìm thấy tất cả các lần lặp lại như vậy cho một $cntr$ cố định?
Hãy nhớ rằng vẫn có thể có nhiều lần lặp lại như vậy.

Hãy nhìn lại một hình dung, lần này cho sự lặp lại $abcabc$:

$$\overbrace{a}^{l_1} ~ \overbrace{\underset{cntr}{b} ~ c}^{l_2} ~ \overbrace{a}^{l_1} ~ | ~ \overbrace{b ~ c}^{l_2}$$

Ở đây chúng tôi biểu thị độ dài của hai phần của sự lặp lại bằng $l_1$ và $l_2$:
$l_1$ là độ dài của lần lặp lại đến vị trí $cntr-1$, và $l_2$ là độ dài của lần lặp lại từ $cntr$ đến hết nửa của lần lặp lại.
Chúng ta có $2l = l_1 + l_2 + l_1 + l_2$ là tổng độ dài của sự lặp lại.

Chúng ta hãy tạo các điều kiện **cần và đủ** cho một sự lặp lại như vậy tại vị trí $cntr$ có độ dài $2l = 2(l_1 + l_2) = 2(|u| - cntr)$:

- Gọi $k_1$ là số lớn nhất sao cho $k_1$ ký tự đầu tiên trước vị trí $cntr$ trùng với $k_1$ ký tự cuối cùng trong chuỗi $u$:
  
$$
u[cntr - k_1 \dots cntr - 1] = u[|u| - k_1 \dots |u| - 1]
$$
  
- Gọi $k_2$ là số lớn nhất sao cho $k_2$ ký tự bắt đầu tại vị trí $cntr$ trùng với $k_2$ ký tự đầu tiên trong chuỗi $v$:

$$  
  u[cntr \dots cntr + k_2 - 1] = v[0 \dots k_2 - 1]
$$
  
- Sau đó, chúng ta có một sự lặp lại chính xác cho bất kỳ cặp $(l_1,~ l_2)$ nào với

$$
  \begin{align}
  l_1 &\le k_1, \\\\
  l_2 &\le k_2. \\\\
  \end{align}
$$

Tóm lại:

- Chúng tôi cố định một vị trí cụ thể $cntr$.
- Tất cả các lần lặp lại mà chúng tôi sẽ tìm thấy bây giờ có độ dài $2l = 2(|u| - cntr)$.
  Có thể có nhiều lần lặp lại như vậy, chúng phụ thuộc vào độ dài $l_1$ và $l_2 = l - l_1$.
- Chúng ta tìm thấy $k_1$ và $k_2$ như mô tả ở trên.
- Khi đó tất cả các lần lặp lại phù hợp là những lần mà độ dài của các mảnh $l_1$ và $l_2$ thỏa mãn các điều kiện:

$$
  \begin{align}
  l_1 + l_2 &= l = |u| - cntr \\\\
  l_1 &\le k_1, \\\\
  l_2 &\le k_2. \\\\
  \end{align}
$$

Do đó, phần còn lại duy nhất là cách chúng ta có thể tính toán các giá trị $k_1$ và $k_2$ một cách nhanh chóng cho mọi vị trí $cntr$.
May mắn thay, chúng ta có thể tính toán chúng trong $O(1)$ bằng cách sử dụng [Hàm Z (Z-function)](z-function.md):

- Để có thể tìm giá trị $k_1$ cho mỗi vị trí bằng cách tính toán hàm Z cho chuỗi $\overline{u}$ (tức là chuỗi đảo ngược $u$).
  Sau đó, giá trị $k_1$ cho một $cntr$ cụ thể sẽ bằng với giá trị tương ứng của mảng hàm Z.
- Để tính toán trước tất cả các giá trị $k_2$, chúng ta tính toán hàm Z cho chuỗi $v + \# + u$ (tức là chuỗi $u$ được nối với ký tự phân tách $\#$ và chuỗi $v$).
  Một lần nữa chúng ta chỉ cần tra cứu giá trị tương ứng trong hàm Z để có được giá trị $k_2$.

Vì vậy, điều này là đủ để tìm tất cả các lần lặp lại chéo trái.

### Lặp lại chéo phải (Right crossing repetitions) {: #right-crossing-repetitions}

Để tính toán các lần lặp lại chéo phải, chúng ta hành động tương tự:
chúng ta xác định tâm $cntr$ là ký tự tương ứng với ký tự cuối cùng trong chuỗi $u$.

Sau đó, độ dài $k_1$ sẽ được xác định là số lượng lớn nhất các ký tự trước vị trí $cntr$ (bao gồm cả nó) trùng với các ký tự cuối cùng của chuỗi $u$.
Và độ dài $k_2$ sẽ được xác định là số lượng lớn nhất các ký tự bắt đầu tại $cntr + 1$ trùng với các ký tự của chuỗi $v$.

Do đó, chúng ta có thể tìm thấy các giá trị $k_1$ và $k_2$ bằng cách tính toán hàm Z cho các chuỗi $\overline{u} + \# + \overline{v}$ và $v$.

Sau đó, chúng ta có thể tìm thấy các lần lặp lại bằng cách xem xét tất cả các vị trí $cntr$ và sử dụng tiêu chí tương tự như chúng ta đã có cho các lần lặp lại chéo trái.

### Cài đặt (Implementation) {: #implementation}

Việc cài đặt thuật toán Main-Lorentz tìm tất cả các lần lặp lại dưới dạng các bộ bốn đặc biệt: $(cntr,~ l,~ k_1,~ k_2)$ trong thời gian $O(n \log n)$.
Nếu bạn chỉ muốn tìm số lần lặp lại trong một chuỗi hoặc chỉ muốn tìm lần lặp lại dài nhất trong một chuỗi, thông tin này là đủ và thời gian chạy vẫn sẽ là $O(n \log n)$.

Lưu ý rằng nếu bạn muốn mở rộng các bộ này để có vị trí bắt đầu và kết thúc của mỗi lần lặp lại, thì thời gian chạy sẽ là $O(n^2)$ (hãy nhớ rằng có thể có $O(n^2)$ lần lặp lại).
Trong quá trình triển khai này, chúng tôi sẽ làm như vậy và lưu trữ tất cả các lần lặp lại được tìm thấy trong một vector gồm các cặp chỉ số bắt đầu và kết thúc.
```cpp title="main_lorentz"
vector<int> z_function(string const& s) {
    int n = s.size();
    vector<int> z(n);
    for (int i = 1, l = 0, r = 0; i < n; i++) {
        if (i <= r)
            z[i] = min(r-i+1, z[i-l]);
        while (i + z[i] < n && s[z[i]] == s[i+z[i]])
            z[i]++;
        if (i + z[i] - 1 > r) {
            l = i;
            r = i + z[i] - 1;
        }
    }
    return z;
}

int get_z(vector<int> const& z, int i) {
    if (0 <= i && i < (int)z.size())
        return z[i];
    else
        return 0;
}

vector<pair<int, int>> repetitions;

void convert_to_repetitions(int shift, bool left, int cntr, int l, int k1, int k2) {
    for (int l1 = max(1, l - k2); l1 <= min(l, k1); l1++) {
        if (left && l1 == l) break;
        int l2 = l - l1;
        int pos = shift + (left ? cntr - l1 : cntr - l - l1 + 1);
        repetitions.emplace_back(pos, pos + 2*l - 1);
    }
}

void find_repetitions(string s, int shift = 0) {
    int n = s.size();
    if (n == 1)
        return;

    int nu = n / 2;
    int nv = n - nu;
    string u = s.substr(0, nu);
    string v = s.substr(nu);
    string ru(u.rbegin(), u.rend());
    string rv(v.rbegin(), v.rend());

    find_repetitions(u, shift);
    find_repetitions(v, shift + nu);

    vector<int> z1 = z_function(ru);
    vector<int> z2 = z_function(v + '#' + u);
    vector<int> z3 = z_function(ru + '#' + rv);
    vector<int> z4 = z_function(v);

    for (int cntr = 0; cntr < n; cntr++) {
        int l, k1, k2;
        if (cntr < nu) {
            l = nu - cntr;
            k1 = get_z(z1, nu - cntr);
            k2 = get_z(z2, nv + 1 + cntr);
        } else {
            l = cntr - nu + 1;
            k1 = get_z(z3, nu + 1 + nv - 1 - (cntr - nu));
            k2 = get_z(z4, (cntr - nu) + 1);
        }
        if (k1 + k2 >= l)
            convert_to_repetitions(shift, cntr < nu, cntr, l, k1, k2);
    }
}
```
