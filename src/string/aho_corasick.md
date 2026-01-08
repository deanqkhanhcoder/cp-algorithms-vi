---
tags:
  - Translated
e_maxx_link: aho_corasick
---

# Thuật toán Aho-Corasick (Aho-Corasick algorithm) {: #aho-corasick-algorithm}

Thuật toán Aho-Corasick cho phép chúng ta nhanh chóng tìm kiếm nhiều mẫu trong một văn bản.
Tập hợp các chuỗi mẫu còn được gọi là _từ điển_ (_dictionary_).
Chúng ta sẽ ký hiệu tổng độ dài của các chuỗi cấu thành nó là $m$ và kích thước của bảng chữ cái là $k$.
Thuật toán xây dựng một automaton trạng thái hữu hạn (finite state automaton) dựa trên một trie trong thời gian $O(m k)$ và sau đó sử dụng nó để xử lý văn bản.

Thuật toán được đề xuất bởi Alfred Aho và Margaret Corasick vào năm 1975.

## Xây dựng trie (Construction of the trie) {: #construction-of-the-trie}

<center>
<img src="https://upload.wikimedia.org/wikipedia/commons/e/e2/Trie.svg" width="400px">
<br>
<i>Một trie dựa trên các từ "Java", "Rad", "Rand", "Rau", "Raum" và "Rose".</i>
<br>
<i><a href="https://commons.wikimedia.org/wiki/File:Trie.svg">Hình ảnh</a> bởi [nd](https://de.wikipedia.org/wiki/Benutzer:Nd) được phân phối theo giấy phép <a href="https://creativecommons.org/licenses/by-sa/3.0/deed.en">CC BY-SA 3.0</a>.</i>
</center>

Về mặt hình thức, trie là một cây có gốc, trong đó mỗi cạnh của cây được gắn nhãn với một chữ cái nào đó
và các cạnh đi ra từ một đỉnh có các nhãn khác nhau.

Chúng ta sẽ xác định mỗi đỉnh trong trie với chuỗi được tạo bởi các nhãn trên đường dẫn từ gốc đến đỉnh đó.

Mỗi đỉnh cũng sẽ có một cờ $\text{output}$ sẽ được đặt
nếu đỉnh tương ứng với một mẫu trong từ điển.

Theo đó, một trie cho một tập hợp các chuỗi là một trie sao cho mỗi đỉnh $\text{output}$ tương ứng với một chuỗi từ tập hợp, và ngược lại, mỗi chuỗi của tập hợp tương ứng với một đỉnh $\text{output}$.

Bây giờ chúng tôi mô tả cách xây dựng một trie cho một tập hợp các chuỗi nhất định trong thời gian tuyến tính đối với tổng độ dài của chúng.

Chúng tôi giới thiệu một cấu trúc cho các đỉnh của cây:
```{.cpp file=aho_corasick_trie_definition}
const int K = 26;

struct Vertex {
    int next[K];
    bool output = false;

    Vertex() {
        fill(begin(next), end(next), -1);
    }
};

vector<Vertex> trie(1);
```

Ở đây, chúng tôi lưu trữ trie dưới dạng một mảng các $\text{Vertex}$.
Mỗi $\text{Vertex}$ chứa cờ $\text{output}$ và các cạnh dưới dạng một mảng $\text{next}[]$, trong đó $\text{next}[i]$ là chỉ số của đỉnh mà chúng ta đạt được bằng cách theo ký tự $i$, hoặc $-1$ nếu không có cạnh như vậy.
Ban đầu, trie chỉ bao gồm một đỉnh - gốc - với chỉ số $0$.

Bây giờ chúng ta thực hiện một hàm sẽ thêm một chuỗi $s$ vào trie.
Việc thực hiện rất đơn giản:
chúng ta bắt đầu tại nút gốc, và miễn là có các cạnh tương ứng với các ký tự của $s$, chúng ta đi theo chúng.
Nếu không có cạnh cho một ký tự, chúng ta tạo một đỉnh mới và kết nối nó với một cạnh.
Vào cuối quá trình, chúng ta đánh dấu đỉnh cuối cùng bằng cờ $\text{output}$.

```{.cpp file=aho_corasick_trie_add}
void add_string(string const& s) {
    int v = 0;
    for (char ch : s) {
        int c = ch - 'a';
        if (trie[v].next[c] == -1) {
            trie[v].next[c] = trie.size();
            trie.emplace_back();
        }
        v = trie[v].next[c];
    }
    trie[v].output = true;
}
```

Việc cài đặt này rõ ràng chạy trong thời gian tuyến tính,
và vì mỗi đỉnh lưu trữ $k$ liên kết, nó sẽ sử dụng bộ nhớ $O(m k)$.

Có thể giảm mức tiêu thụ bộ nhớ xuống $O(m)$ bằng cách sử dụng map thay vì mảng trong mỗi đỉnh.
Tuy nhiên, điều này sẽ làm tăng độ phức tạp thời gian lên $O(m \log k)$.

## Xây dựng một automaton (Construction of an automaton) {: #construction-of-an-automaton}

Giả sử chúng ta đã xây dựng một trie cho tập hợp các chuỗi đã cho.
Bây giờ hãy nhìn nó từ một phía khác.
Nếu chúng ta nhìn vào bất kỳ đỉnh nào,
chuỗi tương ứng với nó là tiền tố của một hoặc nhiều chuỗi trong tập hợp, do đó mỗi đỉnh của trie có thể được hiểu là một vị trí trong một hoặc nhiều chuỗi từ tập hợp.

Trong thực tế, các đỉnh trie có thể được hiểu là các trạng thái trong một **automaton đơn định hữu hạn** (**finite deterministic automaton**).
Từ bất kỳ trạng thái nào, chúng ta có thể chuyển đổi - sử dụng một số chữ cái đầu vào - sang các trạng thái khác, tức là sang một vị trí khác trong tập hợp các chuỗi.
Ví dụ: nếu chỉ có một chuỗi $abc$ trong từ điển, và chúng ta đang đứng ở đỉnh $ab$, thì sử dụng chữ cái $c$ chúng ta có thể đi đến đỉnh $abc$.

Do đó, chúng ta có thể hiểu các cạnh của trie là các chuyển đổi trong một automaton theo chữ cái tương ứng.
Tuy nhiên, trong một automaton, chúng ta cần có các danh sách chuyển đổi cho mỗi sự kết hợp của một trạng thái và một chữ cái.
Nếu chúng ta cố gắng thực hiện một chuyển đổi bằng một chữ cái, và không có cạnh tương ứng trong trie, thì chúng ta vẫn phải đi vào một trạng thái nào đó.

Chính xác hơn, giả sử chúng ta đang ở trạng thái tương ứng với chuỗi $t$, và chúng ta muốn chuyển sang một trạng thái khác bằng ký tự $c$.
Nếu có một cạnh được gắn nhãn bằng chữ cái $c$ này, thì chúng ta có thể chỉ cần đi qua cạnh này và lấy đỉnh tương ứng với $t + c$.
Nếu không có cạnh như vậy, vì chúng ta muốn duy trì bất biến (invariant) rằng trạng thái hiện tại là phần khớp một phần dài nhất trong chuỗi được xử lý, chúng ta phải tìm chuỗi dài nhất trong trie là hậu tố thực sự của chuỗi $t$ và cố gắng thực hiện chuyển đổi từ đó.

Ví dụ: hãy để trie được xây dựng bởi các chuỗi $ab$ và $bc$, và chúng ta hiện đang ở đỉnh tương ứng với $ab$, đây cũng là một đỉnh $\text{output}$.
Để chuyển đổi với chữ cái $c$, chúng ta buộc phải đi đến trạng thái tương ứng với chuỗi $b$, và từ đó đi theo cạnh với chữ cái $c$.

<center>
<img src="https://upload.wikimedia.org/wikipedia/commons/9/90/A_diagram_of_the_Aho-Corasick_string_search_algorithm.svg" width="300px">
<br>
<i>Một automaton Aho-Corasick dựa trên các từ "a", "ab", "bc", "bca", "c" và "caa".</i>
<br>
<i>Mũi tên màu xanh là liên kết hậu tố (suffix match), mũi tên màu xanh lá cây là liên kết kết thúc (terminal link).</i>
</center>

Một **liên kết hậu tố** (**suffix link**) cho một đỉnh $p$ là một cạnh trỏ đến hậu tố thực sự dài nhất của chuỗi tương ứng với đỉnh $p$.
Trường hợp đặc biệt duy nhất là gốc của trie, có liên kết hậu tố sẽ trỏ đến chính nó.
Bây giờ chúng ta có thể cải tổ lại tuyên bố về các chuyển đổi trong automaton như thế này:
trong khi không có chuyển đổi từ đỉnh hiện tại của trie sử dụng chữ cái hiện tại (hoặc cho đến khi chúng ta đến gốc), chúng ta đi theo liên kết hậu tố.

Do đó, chúng ta đã giảm vấn đề xây dựng automaton thành vấn đề tìm liên kết hậu tố cho tất cả các đỉnh của trie.
Tuy nhiên, chúng ta sẽ xây dựng các liên kết hậu tố này, thật kỳ lạ, bằng cách sử dụng các chuyển đổi được xây dựng trong automaton.

Các liên kết hậu tố của đỉnh gốc và tất cả các con trực tiếp của nó trỏ đến đỉnh gốc.
Đối với bất kỳ đỉnh $v$ nào sâu hơn trong cây, chúng ta có thể tính toán liên kết hậu tố như sau:
nếu $p$ là tổ tiên của $v$ với $c$ là chữ cái gắn nhãn cạnh từ $p$ đến $v$,
đi đến $p$,
sau đó đi theo liên kết hậu tố của nó, và thực hiện chuyển đổi với chữ cái $c$ từ đó.

Do đó, vấn đề tìm các chuyển đổi đã được giảm thành vấn đề tìm các liên kết hậu tố, và vấn đề tìm các liên kết hậu tố đã được giảm thành vấn đề tìm một liên kết hậu tố và một chuyển đổi, ngoại trừ các đỉnh gần gốc hơn.
Vì vậy, chúng ta có một sự phụ thuộc đệ quy mà chúng ta có thể giải quyết trong thời gian tuyến tính.

Hãy chuyển sang phần cài đặt.
Lưu ý rằng bây giờ chúng ta sẽ lưu trữ tổ tiên $p$ và ký tự $pch$ của cạnh từ $p$ đến $v$ cho mỗi đỉnh $v$.
Ngoài ra, tại mỗi đỉnh, chúng ta sẽ lưu trữ liên kết hậu tố $\text{link}$ (hoặc $-1$ nếu nó chưa được tính toán), và trong mảng $\text{go}[k]$ lưu trữ các chuyển đổi trong máy cho mỗi ký hiệu (một lần nữa là $-1$ nếu nó chưa được tính toán).

```{.cpp file=aho_corasick_automaton}
const int K = 26;

struct Vertex {
    int next[K];
    bool output = false;
    int p = -1;
    char pch;
    int link = -1;
    int go[K];

    Vertex(int p=-1, char ch='$') : p(p), pch(ch) {
        fill(begin(next), end(next), -1);
        fill(begin(go), end(go), -1);
    }
};

vector<Vertex> t(1);

void add_string(string const& s) {
    int v = 0;
    for (char ch : s) {
        int c = ch - 'a';
        if (t[v].next[c] == -1) {
            t[v].next[c] = t.size();
            t.emplace_back(v, ch);
        }
        v = t[v].next[c];
    }
    t[v].output = true;
}

int go(int v, char ch);

int get_link(int v) {
    if (t[v].link == -1) {
        if (v == 0 || t[v].p == 0)
            t[v].link = 0;
        else
            t[v].link = go(get_link(t[v].p), t[v].pch);
    }
    return t[v].link;
}

int go(int v, char ch) {
    int c = ch - 'a';
    if (t[v].go[c] == -1) {
        if (t[v].next[c] != -1)
            t[v].go[c] = t[v].next[c];
        else
            t[v].go[c] = v == 0 ? 0 : go(get_link(v), ch);
    }
    return t[v].go[c];
} 
```

Dễ thấy rằng nhờ việc ghi nhớ (memoization) các liên kết hậu tố và chuyển đổi,
tổng thời gian để tìm tất cả các liên kết hậu tố và chuyển đổi sẽ là tuyến tính.

Để minh họa cho khái niệm này, hãy tham khảo slide số 103 của [Stanford slides](http://web.stanford.edu/class/archive/cs/cs166/cs166.1166/lectures/02/Slides02.pdf).

### Xây dựng dựa trên BFS (BFS-based construction) {: #bfs-based-construction}

Thay vì tính toán các chuyển đổi và liên kết hậu tố bằng các lệnh gọi đệ quy đến `go` và `get_link`, có thể tính toán chúng từ dưới lên bắt đầu từ gốc.
(Trong thực tế, khi từ điển chỉ bao gồm một chuỗi, chúng ta thu được thuật toán Knuth-Morris-Pratt quen thuộc.)

Cách tiếp cận này sẽ có một số lợi thế so với cách được mô tả ở trên vì, thay vì tổng độ dài $m$, thời gian chạy của nó chỉ phụ thuộc vào số lượng đỉnh $n$ trong trie. Hơn nữa, có thể điều chỉnh nó cho các bảng chữ cái lớn bằng cách sử dụng cấu trúc dữ liệu mảng bền vững (persistent array data structure), do đó làm cho thời gian xây dựng $O(n \log k)$ thay vì $O(mk)$, đây là một cải tiến đáng kể với điều kiện $m$ có thể lên tới $n^2$.

Chúng ta có thể suy luận theo quy nạp bằng cách sử dụng thực tế là BFS từ gốc đi qua các đỉnh theo thứ tự độ dài tăng dần.
Chúng ta có thể giả định rằng khi chúng ta ở một đỉnh $v$, liên kết hậu tố của nó $u = link[v]$ đã được tính toán thành công và đối với tất cả các đỉnh có độ dài ngắn hơn, các chuyển đổi từ chúng cũng được tính toán đầy đủ.

Giả sử rằng tại thời điểm này chúng ta đang đứng ở một đỉnh $v$ và xem xét một ký tự $c$. Về cơ bản chúng ta có hai trường hợp:

1. $go[v][c] = -1$. Trong trường hợp này, chúng ta có thể gán $go[v][c] = go[u][c]$, điều này đã được biết đến theo giả thuyết quy nạp;
2. $go[v][c] = w \neq -1$. Trong trường hợp này, chúng ta có thể gán $link[w] = go[u][c]$.

Theo cách này, chúng ta dành thời gian $O(1)$ cho mỗi cặp đỉnh và ký tự, làm cho thời gian chạy là $O(nk)$. Chi phí chính ở đây là chúng ta sao chép rất nhiều chuyển đổi từ $u$ trong trường hợp đầu tiên, trong khi các chuyển đổi của trường hợp thứ hai tạo thành trie và tổng cộng lên tới $n$ trên tất cả các đỉnh. Để tránh sao chép $go[u][c]$, chúng ta có thể sử dụng cấu trúc dữ liệu mảng bền vững, sử dụng nó ban đầu chúng ta sao chép $go[u]$ vào $go[v]$ và sau đó chỉ cập nhật các giá trị cho các ký tự trong đó quá trình chuyển đổi sẽ khác nhau. Điều này dẫn đến thuật toán $O(n \log k)$.

## Ứng dụng (Applications) {: #applications}

### Tìm tất cả các chuỗi từ một tập hợp nhất định trong một văn bản (Find all strings from a given set in a text) {: #find-all-strings-from-a-given-set-in-a-text}

Chúng ta được cho một tập hợp các chuỗi và một văn bản.
Chúng ta phải in tất cả các lần xuất hiện của tất cả các chuỗi từ tập hợp trong văn bản đã cho trong $O(\text{len} + \text{ans})$, trong đó $\text{len}$ là độ dài của văn bản và $\text{ans}$ là kích thước của câu trả lời.

Chúng ta xây dựng một automaton cho tập hợp các chuỗi này.
Bây giờ chúng ta sẽ xử lý văn bản từng chữ cái một bằng cách sử dụng automaton,
bắt đầu từ gốc của trie.
Nếu chúng ta ở bất kỳ lúc nào tại trạng thái $v$, và ký tự tiếp theo là $c$, thì chúng ta chuyển sang trạng thái tiếp theo với $\text{go}(v, c)$, do đó hoặc tăng độ dài của chuỗi con khớp hiện tại thêm $1$, hoặc giảm nó bằng cách đi theo một liên kết hậu tố.

Làm thế nào chúng ta có thể tìm ra cho một trạng thái $v$, nếu có bất kỳ kết quả khớp nào với các chuỗi cho tập hợp?
Đầu tiên, rõ ràng là nếu chúng ta đứng trên một đỉnh $\text{output}$, thì chuỗi tương ứng với đỉnh đó kết thúc tại vị trí này trong văn bản.
Tuy nhiên, đây hoàn toàn không phải là trường hợp duy nhất có thể đạt được một kết quả khớp:
nếu chúng ta có thể đạt được một hoặc nhiều đỉnh $\text{output}$ bằng cách di chuyển dọc theo các liên kết hậu tố, thì cũng sẽ có một kết quả khớp tương ứng với mỗi đỉnh $\text{output}$ được tìm thấy.
Một ví dụ đơn giản chứng minh tình huống này có thể được tạo bằng cách sử dụng tập hợp các chuỗi $\{dabce, abc, bc\}$ và văn bản $dabc$.

Do đó, nếu chúng ta lưu trữ trong mỗi đỉnh $\text{output}$ chỉ số của chuỗi tương ứng với nó (hoặc danh sách các chỉ số nếu các chuỗi trùng lặp xuất hiện trong tập hợp), thì chúng ta có thể tìm thấy trong thời gian $O(n)$ các chỉ số của tất cả các chuỗi khớp với trạng thái hiện tại, bằng cách đơn giản là đi theo các liên kết hậu tố từ đỉnh hiện tại đến gốc.
Đây không phải là giải pháp hiệu quả nhất, vì điều này dẫn đến độ phức tạp tổng thể là $O(n ~ \text{len})$.
Tuy nhiên, điều này có thể được tối ưu hóa bằng cách tính toán và lưu trữ đỉnh $\text{output}$ gần nhất có thể truy cập được bằng cách sử dụng các liên kết hậu tố (đôi khi được gọi là **liên kết thoát** (**exit link**)).
Giá trị này chúng ta có thể tính toán một cách lười biếng trong thời gian tuyến tính.
Do đó, đối với mỗi đỉnh, chúng ta có thể tiến trong thời gian $O(1)$ đến đỉnh được đánh dấu tiếp theo trong đường dẫn liên kết hậu tố, tức là đến kết quả khớp tiếp theo.
Do đó, đối với mỗi trận đấu, chúng tôi dành thời gian $O(1)$, và do đó chúng tôi đạt đến độ phức tạp $O(\text{len} + \text{ans})$.

Nếu bạn chỉ muốn đếm số lần xuất hiện và không tìm thấy chính các chỉ số, bạn có thể tính toán số lượng các đỉnh được đánh dấu trong đường dẫn liên kết hậu tố cho mỗi đỉnh $v$.
Điều này có thể được tính toán trong tổng thời gian $O(n)$.
Do đó chúng ta có thể tổng hợp tất cả các kết quả khớp trong $O(\text{len})$.

### Tìm chuỗi nhỏ nhất theo từ điển có độ dài nhất định không khớp với bất kỳ chuỗi nào đã cho (Finding the lexicographically smallest string of a given length that doesn't match any given strings) {: #finding-the-lexicographically-smallest-string-of-a-given-length-that-doesnt-match-any-given-strings}

Một tập hợp các chuỗi và một độ dài $L$ được đưa ra.
Chúng ta phải tìm một chuỗi có độ dài $L$, không chứa bất kỳ chuỗi nào, và lấy chuỗi nhỏ nhất theo từ điển trong số các chuỗi đó.

Chúng ta có thể xây dựng automaton cho tập hợp các chuỗi.
Nhớ lại rằng các đỉnh $\text{output}$ là các trạng thái mà chúng ta có một kết quả khớp với một chuỗi từ tập hợp.
Vì trong nhiệm vụ này chúng ta phải tránh các kết quả khớp, chúng ta không được phép vào các trạng thái như vậy.
Mặt khác, chúng ta có thể nhập tất cả các đỉnh khác.
Do đó, chúng ta xóa tất cả các đỉnh "xấu" khỏi máy, và trong biểu đồ còn lại của automaton, chúng ta tìm đường dẫn nhỏ nhất theo từ điển có độ dài $L$.
Nhiệm vụ này có thể được giải quyết trong $O(L)$ ví dụ bằng cách [tìm kiếm theo chiều sâu](../graph/depth-first-search.md).

### Tìm chuỗi ngắn nhất chứa tất cả các chuỗi đã cho (Finding the shortest string containing all given strings) {: #finding-the-shortest-string-containing-all-given-strings}

Ở đây chúng ta sử dụng những ý tưởng tương tự.
Đối với mỗi đỉnh, chúng ta lưu trữ một mặt nạ (mask) biểu thị các chuỗi khớp ở trạng thái này.
Sau đó, bài toán có thể được cải tổ lại như sau:
ban đầu ở trạng thái $(v = \text{root},~ \text{mask} = 0)$, chúng ta muốn đạt đến trạng thái $(v,~ \text{mask} = 2^n - 1)$, trong đó $n$ là số lượng chuỗi trong tập hợp.
Khi chúng ta chuyển từ trạng thái này sang trạng thái khác bằng một chữ cái, chúng ta cập nhật mặt nạ cho phù hợp.
Bằng cách chạy một [tìm kiếm theo chiều rộng](../graph/breadth-first-search.md), chúng ta có thể tìm thấy một đường dẫn đến trạng thái $(v,~ \text{mask} = 2^n - 1)$ với độ dài nhỏ nhất.

### Tìm chuỗi nhỏ nhất theo từ điển có độ dài $L$ chứa $k$ chuỗi (Finding the lexicographically smallest string of length $L$ containing $k$ strings) {: #finding-the-lexicographically-smallest-string-of-length-l-containing-k-strings}

Như trong bài toán trước, chúng ta tính toán cho mỗi đỉnh số lượng kết quả khớp tương ứng với nó (đó là số lượng các đỉnh được đánh dấu có thể truy cập bằng cách sử dụng các liên kết hậu tố).
Chúng ta cải tổ bài toán: trạng thái hiện tại được xác định bởi một bộ ba số $(v,~ \text{len},~ \text{cnt})$, và chúng ta muốn đạt được từ trạng thái $(\text{root},~ 0,~ 0)$ đến trạng thái $(v,~ L,~ k)$, trong đó $v$ có thể là bất kỳ đỉnh nào.
Do đó, chúng ta có thể tìm thấy một đường dẫn như vậy bằng cách sử dụng tìm kiếm theo chiều sâu (và nếu tìm kiếm nhìn vào các cạnh theo thứ tự tự nhiên của chúng, thì đường dẫn được tìm thấy sẽ tự động là nhỏ nhất theo từ điển).

## Bài tập (Problems) {: #problems}

- [UVA #11590 - Prefix Lookup](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2637)
- [UVA #11171 - SMS](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2112)
- [UVA #10679 - I Love Strings!!](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1620)
- [Codeforces - x-prime Substrings](https://codeforces.com/problemset/problem/1400/F)
- [Codeforces - Frequency of String](http://codeforces.com/problemset/problem/963/D)
- [CodeChef - TWOSTRS](https://www.codechef.com/MAY20A/problems/TWOSTRS)

## Tài liệu tham khảo (References) {: #references}
- [Stanford's CS166 - Aho-Corasick Automata](http://web.stanford.edu/class/archive/cs/cs166/cs166.1166/lectures/02/Slides02.pdf) ([Condensed](http://web.stanford.edu/class/archive/cs/cs166/cs166.1166/lectures/02/Small02.pdf))
