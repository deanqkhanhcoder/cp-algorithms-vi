---
tags:
  - Translated
e_maxx_link: duval_algorithm
---

# Phân rã Lyndon (Lyndon factorization) {: #lyndon-factorization}

## Phân rã Lyndon (Lyndon factorization) {: #lyndon-factorization-1}

Trước tiên hãy định nghĩa khái niệm về phân rã Lyndon.

Một chuỗi được gọi là **đơn** (**simple**) (hoặc một từ Lyndon), nếu nó thực sự **nhỏ hơn** bất kỳ **hậu tố** không tầm thường nào của chính nó theo thứ tự từ điển.
Ví dụ về các chuỗi đơn là: $a$, $b$, $ab$, $aab$, $abb$, $ababb$, $abcd$.
Có thể chỉ ra rằng một chuỗi là đơn, khi và chỉ khi nó thực sự **nhỏ hơn** tất cả các **dịch chuyển vòng** không tầm thường của nó.

Tiếp theo, giả sử có một chuỗi $s$ nhất định.
**Phân rã Lyndon** của chuỗi $s$ là một phân rã $s = w_1 w_2 \dots w_k$, trong đó tất cả các chuỗi $w_i$ là chuỗi đơn, và chúng theo thứ tự không tăng về mặt từ điển $w_1 \ge w_2 \ge \dots \ge w_k$.

Người ta có thể chứng minh rằng với bất kỳ chuỗi nào, một phân rã như vậy luôn tồn tại và là duy nhất.

## Thuật toán Duval (Duval algorithm) {: #duval-algorithm}

Thuật toán Duval xây dựng phân rã Lyndon trong thời gian $O(n)$ sử dụng bộ nhớ bổ sung $O(1)$.

Trước tiên hãy giới thiệu một khái niệm khác:
một chuỗi $t$ được gọi là **tiền đơn** (**pre-simple**), nếu nó có dạng $t = w w \dots w \overline{w}$, trong đó $w$ là một chuỗi đơn và $\overline{w}$ là một tiền tố của $w$ (có thể rỗng).
Một chuỗi đơn cũng là tiền đơn.

Thuật toán Duval là thuật toán tham lam.
Tại bất kỳ thời điểm nào trong quá trình thực thi, chuỗi $s$ thực sự sẽ được chia thành ba chuỗi $s = s_1 s_2 s_3$, trong đó phân rã Lyndon cho $s_1$ đã được tìm thấy và hoàn thiện, chuỗi $s_2$ là tiền đơn (và chúng ta biết độ dài của chuỗi đơn trong đó), và $s_3$ hoàn toàn chưa được chạm tới.
Trong mỗi lần lặp, thuật toán Duval lấy ký tự đầu tiên của chuỗi $s_3$ và cố gắng thêm nó vào chuỗi $s_2$.
Nếu $s_2$ không còn là tiền đơn nữa, thì phân rã Lyndon cho một phần nào đó của $s_2$ được biết đến, và phần này đi vào $s_1$.

Hãy mô tả thuật toán chi tiết hơn.
Con trỏ $i$ sẽ luôn trỏ đến đầu chuỗi $s_2$.
Vòng lặp bên ngoài sẽ được thực thi miễn là $i < n$.
Bên trong vòng lặp, chúng ta sử dụng thêm hai con trỏ, $j$ trỏ đến đầu của $s_3$, và $k$ trỏ đến ký tự hiện tại mà chúng ta đang so sánh.
Chúng ta muốn thêm ký tự $s[j]$ vào chuỗi $s_2$, điều này đòi hỏi phải so sánh với ký tự $s[k]$.
Có thể có ba trường hợp khác nhau:

- $s[j] = s[k]$: nếu trường hợp này xảy ra, thì việc thêm ký hiệu $s[j]$ vào $s_2$ không vi phạm tính tiền đơn của nó.
  Vì vậy, chúng ta chỉ cần tăng các con trỏ $j$ và $k$.
- $s[j] > s[k]$: ở đây, chuỗi $s_2 + s[j]$ trở thành đơn.
  Chúng ta có thể tăng $j$ và đặt lại $k$ về đầu của $s_2$, để ký tự tiếp theo có thể được so sánh với đầu của từ đơn.
- $s[j] < s[k]$: chuỗi $s_2 + s[j]$ không còn là tiền đơn nữa.
  Do đó, chúng ta sẽ chia chuỗi tiền đơn $s_2$ thành các chuỗi đơn của nó và phần còn lại, có thể rỗng.
  Chuỗi đơn sẽ có độ dài $j - k$.
  Trong lần lặp tiếp theo, chúng ta bắt đầu lại với phần còn lại $s_2$.

### Cài đặt (Implementation) {: #implementation}

Dưới đây chúng tôi trình bày việc cài đặt thuật toán Duval, thuật toán này sẽ trả về phân rã Lyndon mong muốn của một chuỗi $s$ nhất định.
```cpp title="duval_algorithm"
vector<string> duval(string const& s) {
    int n = s.size();
    int i = 0;
    vector<string> factorization;
    while (i < n) {
        int j = i + 1, k = i;
        while (j < n && s[k] <= s[j]) {
            if (s[k] < s[j])
                k = i;
            else
                k++;
            j++;
        }
        while (i <= k) {
            factorization.push_back(s.substr(i, j - k));
            i += j - k;
        }
    }
    return factorization;
}
```

### Độ phức tạp (Complexity) {: #complexity}

Hãy ước tính thời gian chạy của thuật toán này.

**Vòng lặp while bên ngoài** không vượt quá $n$ lần lặp, vì ở cuối mỗi lần lặp $i$ đều tăng.
Vòng lặp while bên trong thứ hai cũng chạy trong $O(n)$, vì chỉ xuất ra kết quả phân rã cuối cùng.

Vì vậy, chúng ta chỉ quan tâm đến **vòng lặp while bên trong thứ nhất**.
Nó thực hiện bao nhiêu lần lặp trong trường hợp xấu nhất?
Dễ thấy rằng các từ đơn mà chúng ta xác định trong mỗi lần lặp của vòng lặp bên ngoài dài hơn phần còn lại mà chúng ta đã so sánh thêm.
Do đó, tổng của các phần còn lại cũng sẽ nhỏ hơn $n$, có nghĩa là chúng ta chỉ thực hiện tối đa $O(n)$ lần lặp của vòng lặp while bên trong thứ nhất.
Trên thực tế, tổng số phép so sánh ký tự sẽ không vượt quá $4n - 3$.

## Tìm dịch chuyển vòng nhỏ nhất (Finding the smallest cyclic shift) {: #finding-the-smallest-cyclic-shift}

Giả sử có một chuỗi $s$.
Chúng ta xây dựng phân rã Lyndon cho chuỗi $s + s$ (trong thời gian $O(n)$).
Chúng ta sẽ tìm kiếm một chuỗi đơn trong phân rã, bắt đầu tại vị trí nhỏ hơn $n$ (tức là nó bắt đầu trong bản sao đầu tiên của $s$), và kết thúc ở vị trí lớn hơn hoặc bằng $n$ (tức là trong bản sao thứ hai của $s$).
Người ta nói rằng, vị trí bắt đầu của chuỗi đơn này sẽ là đầu của dịch chuyển vòng nhỏ nhất mong muốn.
Điều này có thể được kiểm chứng dễ dàng bằng cách sử dụng định nghĩa của phân rã Lyndon.

Đầu của khối đơn có thể được tìm thấy dễ dàng - chỉ cần nhớ con trỏ $i$ ở đầu mỗi lần lặp của vòng lặp bên ngoài, con trỏ này chỉ ra đầu của chuỗi tiền đơn hiện tại.

Vì vậy, chúng ta có cách cài đặt sau:
```cpp title="smallest_cyclic_string"
string min_cyclic_string(string s) {
    s += s;
    int n = s.size();
    int i = 0, ans = 0;
    while (i < n / 2) {
        ans = i;
        int j = i + 1, k = i;
        while (j < n && s[k] <= s[j]) {
            if (s[k] < s[j])
                k = i;
            else
                k++;
            j++;
        }
        while (i <= k)
            i += j - k;
    }
    return s.substr(ans, n / 2);
}
```

## Bài tập (Problems) {: #problems}

- [UVA #719 - Glass Beads](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=660)
