---
tags:
  - Translated
e_maxx_link: kuhn_matching
---

# Thuật toán Kuhn cho Cặp ghép cực đại trên đồ thị hai phía (Kuhn's Algorithm for Maximum Bipartite Matching) {: #kuhns-algorithm-for-maximum-bipartite-matching}

## Bài toán (Problem) {: #problem}
Bạn được cho một đồ thị hai phía $G$ chứa $n$ đỉnh và $m$ cạnh. Tìm cặp ghép cực đại, tức là chọn càng nhiều cạnh càng tốt sao cho không có cạnh nào được chọn chia sẻ một đỉnh với bất kỳ cạnh nào được chọn khác.

## Mô tả thuật toán (Algorithm Description) {: #algorithm-description}

### Các định nghĩa cần thiết (Required Definitions) {: #required-definitions}

* Một **cặp ghép** (matching) $M$ là một tập hợp các cạnh không kề nhau từng đôi một của một đồ thị (nói cách khác, không quá một cạnh từ tập hợp này kề với bất kỳ đỉnh nào của đồ thị $M$).
* **Lực lượng** (cardinality) của một cặp ghép là số lượng cạnh trong đó.
* Tất cả những đỉnh có một cạnh kề từ cặp ghép (tức là có bậc chính xác là một trong đồ thị con được tạo bởi $M$) được gọi là **bão hòa** (saturated) bởi cặp ghép này.

* Một **cặp ghép tối đại** (maximal matching) là một cặp ghép $M$ của đồ thị $G$ mà không phải là tập con của bất kỳ cặp ghép nào khác.

* Một **cặp ghép cực đại** (maximum matching) (hay còn gọi là cặp ghép có lực lượng cực đại) là một cặp ghép chứa số lượng cạnh lớn nhất có thể. Mọi cặp ghép cực đại đều là cặp ghép tối đại.

* Một **đường đi** (path) có độ dài $k$ ở đây có nghĩa là một đường đi *đơn* (tức là không chứa các đỉnh hoặc cạnh lặp lại) chứa $k$ cạnh, trừ khi có quy định khác.

* Một **đường mở** (alternating path) (trong đồ thị hai phía, đối với một cặp ghép nào đó) là một đường đi trong đó các cạnh luân phiên thuộc về / không thuộc về cặp ghép.

* Một **đường tăng** (augmenting path) (trong đồ thị hai phía, đối với một cặp ghép nào đó) là một đường mở có các đỉnh đầu và cuối không bão hòa, tức là chúng không thuộc về cặp ghép.

* **Hiệu đối xứng** (symmetric difference) (còn được gọi là **hợp rời**) của các tập hợp $A$ và $B$, được biểu thị bằng $A \oplus B$, là tập hợp của tất cả các phần tử thuộc về chính xác một trong $A$ hoặc $B$, nhưng không thuộc về cả hai.
Tức là, $A \oplus B = (A - B) \cup (B - A) = (A \cup B) - (A \cap B)$.

### Bổ đề Berge (Berge's lemma) {: #berges-lemma}

Bổ đề này đã được chứng minh bởi nhà toán học người Pháp **Claude Berge** vào năm 1957, mặc dù nó đã được quan sát bởi nhà toán học người Đan Mạch **Julius Petersen** vào năm 1891 và nhà toán học người Hungary **Denés Kőnig** vào năm 1931.

#### Phát biểu (Formulation) {: #formulation}
Một cặp ghép $M$ là cực đại $\Leftrightarrow$ không có đường tăng nào liên quan đến cặp ghép $M$.

#### Chứng minh (Proof) {: #proof}

Cả hai vế của phép tương đương sẽ được chứng minh bằng phản chứng.

1.  Một cặp ghép $M$ là cực đại $\Rightarrow$ không có đường tăng nào liên quan đến cặp ghép $M$.

    Giả sử có một đường tăng $P$ liên quan đến cặp ghép cực đại đã cho $M$. Đường tăng $P$ này nhất thiết phải có độ dài lẻ, có nhiều hơn một cạnh không nằm trong $M$ so với số cạnh của nó cũng nằm trong $M$.
    Chúng ta tạo một cặp ghép mới $M'$ bằng cách bao gồm tất cả các cạnh trong cặp ghép ban đầu $M$ ngoại trừ những cạnh cũng nằm trong $P$, và các cạnh trong $P$ không nằm trong $M$.
    Đây là một cặp ghép hợp lệ vì các đỉnh đầu và cuối của $P$ không được bão hòa bởi $M$, và các đỉnh còn lại chỉ được bão hòa bởi cặp ghép $P \cap M$.
    Cặp ghép mới $M'$ này sẽ có nhiều hơn một cạnh so với $M$, và do đó $M$ không thể là cực đại.

    Một cách chính thức, với một đường tăng $P$ so với một cặp ghép cực đại $M$ nào đó, cặp ghép $M' = P \oplus M$ là sao cho $|M'| = |M| + 1$, một mâu thuẫn.

2.  Một cặp ghép $M$ là cực đại $\Leftarrow$ không có đường tăng nào liên quan đến cặp ghép $M$.

    Giả sử có một cặp ghép $M'$ có lực lượng lớn hơn $M$. Chúng ta xem xét hiệu đối xứng $Q = M \oplus M'$. Đồ thị con $Q$ không còn nhất thiết phải là một cặp ghép.
    Bất kỳ đỉnh nào trong $Q$ đều có bậc tối đa là $2$, có nghĩa là tất cả các thành phần liên thông trong nó là một trong ba loại -

      * một đỉnh cô lập
      * một đường đi (đơn) có các cạnh luân phiên từ $M$ và $M'$
      * một chu trình có độ dài chẵn có các cạnh luân phiên từ $M$ và $M'$

    Vì $M'$ có lực lượng lớn hơn $M$, $Q$ có nhiều cạnh từ $M'$ hơn $M$. Theo nguyên lý Pigeonhole, ít nhất một thành phần liên thông sẽ là một đường đi có nhiều cạnh từ $M'$ hơn $M$. Vì bất kỳ đường đi nào như vậy đều là đường mở, nên nó sẽ có các đỉnh đầu và cuối không được bão hòa bởi $M$, làm cho nó trở thành một đường tăng cho $M$, điều này mâu thuẫn với tiền đề. &ensp; $\blacksquare$

### Thuật toán Kuhn (Kuhn's algorithm) {: #kuhns-algorithm}

Thuật toán Kuhn là một ứng dụng trực tiếp của bổ đề Berge. Về cơ bản nó được mô tả như sau:

Đầu tiên, chúng ta lấy một cặp ghép rỗng. Sau đó, trong khi thuật toán có thể tìm thấy một đường tăng, chúng ta cập nhật cặp ghép bằng cách luân phiên nó dọc theo đường đi này và lặp lại quá trình tìm đường tăng. Ngay khi không thể tìm thấy một đường đi như vậy, chúng ta dừng quá trình - cặp ghép hiện tại là cực đại.

Vẫn còn phải trình bày chi tiết cách tìm các đường tăng. Thuật toán Kuhn chỉ đơn giản là tìm kiếm bất kỳ đường đi nào trong số này bằng cách sử dụng duyệt [theo chiều sâu](depth-first-search.md) hoặc [theo chiều rộng](breadth-first-search.md). Thuật toán lần lượt xem xét tất cả các đỉnh của đồ thị, bắt đầu mỗi lần duyệt từ nó, cố gắng tìm một đường tăng bắt đầu tại đỉnh này.

Thuật toán thuận tiện hơn để mô tả nếu chúng ta giả sử rằng đồ thị đầu vào đã được chia thành hai phần (mặc dù, trên thực tế, thuật toán có thể được cài đặt theo cách mà đồ thị đầu vào không được chia rõ ràng thành hai phần).

Thuật toán xem xét tất cả các đỉnh $v$ của phần đầu tiên của đồ thị: $v = 1 \ldots n_1$. Nếu đỉnh hiện tại $v$ đã được bão hòa với cặp ghép hiện tại (tức là, một số cạnh kề với nó đã được chọn), thì bỏ qua đỉnh này. Ngược lại, thuật toán cố gắng bão hòa đỉnh này, bằng cách bắt đầu tìm kiếm một đường tăng bắt đầu từ đỉnh này.

Việc tìm kiếm một đường tăng được thực hiện bằng cách sử dụng duyệt theo chiều sâu hoặc chiều rộng đặc biệt (thường duyệt theo chiều sâu được sử dụng để dễ cài đặt).
Ban đầu, duyệt theo chiều sâu ở tại đỉnh chưa bão hòa hiện tại $v$ của phần đầu tiên. Hãy xem qua tất cả các cạnh từ đỉnh này. Giả sử cạnh hiện tại là một cạnh $(v, to)$. Nếu đỉnh $to$ chưa được bão hòa với cặp ghép, thì chúng ta đã thành công trong việc tìm một đường tăng: nó bao gồm một cạnh duy nhất $(v, to)$; trong trường hợp này, chúng ta chỉ cần bao gồm cạnh này trong cặp ghép và ngừng tìm kiếm đường tăng từ đỉnh $v$. Ngược lại, nếu $to$ đã được bão hòa với một số cạnh $(to, p)$, thì sẽ đi dọc theo cạnh này: do đó chúng ta sẽ cố gắng tìm một đường tăng đi qua các cạnh $(v, to),(to, p), \ldots$.
Để làm điều này, chỉ cần đi đến đỉnh $p$ trong quá trình duyệt của chúng ta - bây giờ chúng ta cố gắng tìm một đường tăng từ đỉnh này.

Vì vậy, quá trình duyệt này, được khởi chạy từ đỉnh $v$, sẽ hoặc tìm thấy một đường tăng, và do đó bão hòa đỉnh $v$, hoặc nó sẽ không tìm thấy một đường tăng như vậy (và do đó, đỉnh $v$ này không thể được bão hòa).

Sau khi tất cả các đỉnh $v = 1 \ldots n_1$ đã được quét, cặp ghép hiện tại sẽ là cực đại.

### Thời gian chạy (Running time) {: #running-time}

Thuật toán Kuhn có thể được coi là một loạt $n$ lần chạy duyệt theo chiều sâu/chiều rộng trên toàn bộ đồ thị. Do đó, toàn bộ thuật toán được thực thi trong thời gian $O(nm)$, trong trường hợp xấu nhất là $O(n^3)$.

Tuy nhiên, ước tính này có thể được cải thiện một chút. Hóa ra đối với thuật toán Kuhn, điều quan trọng là phần nào của đồ thị được chọn làm phần thứ nhất và phần nào là phần thứ hai.
Thật vậy, trong cách cài đặt được mô tả ở trên, duyệt theo chiều sâu/chiều rộng chỉ bắt đầu từ các đỉnh của phần đầu tiên, vì vậy toàn bộ thuật toán được thực thi trong thời gian $O(n_1m)$, trong đó $n_1$ là số lượng đỉnh của phần đầu tiên. Trong trường hợp xấu nhất, đây là $O(n_1 ^ 2 n_2)$ (trong đó $n_2$ là số lượng đỉnh của phần thứ hai).
Điều này cho thấy rằng sẽ có lợi hơn khi phần đầu tiên chứa ít đỉnh hơn phần thứ hai. Trên các đồ thị rất mất cân bằng (khi $n_1$ và $n_2$ rất khác nhau), điều này chuyển thành sự khác biệt đáng kể về thời gian chạy.

## Cài đặt (Implementation) {: #implementation}

### Cài đặt tiêu chuẩn (Standard implementation) {: #standard-implementation}

Chúng ta hãy trình bày ở đây một cách cài đặt thuật toán trên dựa trên duyệt theo chiều sâu và chấp nhận một đồ thị hai phía dưới dạng một đồ thị được chia rõ ràng thành hai phần.
Cách cài đặt này rất ngắn gọn, và có lẽ nó nên được ghi nhớ ở dạng này.

Ở đây $n$ là số lượng đỉnh trong phần đầu tiên, $k$ - trong phần thứ hai, $g[v]$ là danh sách các cạnh từ đỉnh của phần đầu tiên (tức là danh sách các số của các đỉnh mà các cạnh này dẫn đến từ $v$). Các đỉnh trong cả hai phần được đánh số độc lập, tức là các đỉnh trong phần đầu tiên được đánh số $1 \ldots n$, và những đỉnh trong phần thứ hai được đánh số $1 \ldots k$.

Sau đó, có hai mảng phụ trợ: $\rm mt$ và $\rm used$. Mảng đầu tiên - $\rm mt$ - chứa thông tin về cặp ghép hiện tại. Để thuận tiện cho việc lập trình, thông tin này chỉ được chứa cho các đỉnh của phần thứ hai: $\textrm{mt[} i \rm]$ - đây là số của đỉnh của phần đầu tiên được nối bởi một cạnh với đỉnh $i$ của phần thứ hai (hoặc $-1$, nếu không có cạnh cặp ghép nào đi ra từ nó). Mảng thứ hai là $\rm used$: mảng "thăm" thông thường đến các đỉnh trong duyệt theo chiều sâu (nó chỉ cần thiết để duyệt theo chiều sâu không đi vào cùng một đỉnh hai lần).

Một hàm $\textrm{try\_kuhn}$ là một duyệt theo chiều sâu. Nó trả về $\rm true$ nếu nó có thể tìm thấy một đường tăng từ đỉnh $v$, và coi như hàm này đã thực hiện việc luân phiên cặp ghép dọc theo chuỗi tìm được.

Bên trong hàm, tất cả các cạnh đi ra từ đỉnh $v$ của phần đầu tiên được quét, và sau đó kiểm tra như sau: nếu cạnh này dẫn đến một đỉnh chưa bão hòa $to$, hoặc nếu đỉnh này $to$ được bão hòa, nhưng có thể tìm thấy một chuỗi tăng bằng cách bắt đầu đệ quy từ $\textrm{mt[}to \rm ]$, thì chúng ta nói rằng chúng ta đã tìm thấy một đường tăng, và trước khi trả về từ hàm với kết quả $\rm true$, chúng ta luân phiên cạnh hiện tại: chúng ta chuyển hướng cạnh kề với $to$ sang đỉnh $v$.

Chương trình chính trước tiên chỉ ra rằng cặp ghép hiện tại là rỗng (danh sách $\rm mt$ được điền bằng các số $-1$). Sau đó, đỉnh $v$ của phần đầu tiên được tìm kiếm bởi $\textrm{try\_kuhn}$, và một duyệt theo chiều sâu được bắt đầu từ nó, sau khi đã làm sạch mảng $\rm used$ trước đó.

Điều đáng chú ý là kích thước của cặp ghép rất dễ nhận được bằng số lượng lệnh gọi $\textrm{try\_kuhn}$ trong chương trình chính trả về kết quả $\rm true$. Bản thân cặp ghép cực đại mong muốn được chứa trong mảng $\rm mt$.

```cpp
int n, k;
vector<vector<int>> g;
vector<int> mt;
vector<bool> used;

bool try_kuhn(int v) {
    if (used[v])
        return false;
    used[v] = true;
    for (int to : g[v]) {
        if (mt[to] == -1 || try_kuhn(mt[to])) {
            mt[to] = v;
            return true;
        }
    }
    return false;
}

int main() {
    //... reading the graph ...

    mt.assign(k, -1);
    for (int v = 0; v < n; ++v) {
        used.assign(n, false);
        try_kuhn(v);
    }

    for (int i = 0; i < k; ++i)
        if (mt[i] != -1)
            printf("%d %d\n", mt[i] + 1, i + 1);
}
```

Chúng tôi lặp lại một lần nữa rằng thuật toán Kuhn rất dễ thực hiện theo cách mà nó hoạt động trên các đồ thị được biết là hai phía, nhưng sự phân chia rõ ràng của chúng thành hai phần chưa được đưa ra. Trong trường hợp này, sẽ cần phải từ bỏ việc chia thành hai phần thuận tiện, và lưu trữ tất cả thông tin cho tất cả các đỉnh của đồ thị. Đối với điều này, một mảng danh sách $g$ bây giờ được chỉ định không chỉ cho các đỉnh của phần đầu tiên, mà cho tất cả các đỉnh của đồ thị (tất nhiên, bây giờ các đỉnh của cả hai phần được đánh số theo một đánh số chung - từ $1$ đến $n$). Các mảng $\rm mt$ và $\rm used$ bây giờ cũng được định nghĩa cho các đỉnh của cả hai phần, và theo đó, chúng cần được giữ ở trạng thái này.

### Cài đặt cải tiến (Improved implementation) {: #improved-implementation}

Hãy sửa đổi thuật toán như sau. Trước vòng lặp chính của thuật toán, chúng ta sẽ tìm một **cặp ghép bất kỳ** bằng một thuật toán đơn giản nào đó (một **thuật toán heuristic** đơn giản), và chỉ sau đó chúng ta mới thực hiện một vòng lặp với các lệnh gọi đến hàm $\textrm{try\_kuhn}()$, hàm này sẽ cải thiện cặp ghép này. Kết quả là, thuật toán sẽ hoạt động nhanh hơn đáng kể trên các đồ thị ngẫu nhiên - bởi vì trong hầu hết các đồ thị, bạn có thể dễ dàng tìm thấy một cặp ghép có kích thước đủ lớn bằng cách sử dụng heuristic, và sau đó cải thiện cặp ghép đã tìm thấy đến mức tối đa bằng cách sử dụng thuật toán Kuhn thông thường. Do đó, chúng ta sẽ tiết kiệm được việc khởi chạy một duyệt theo chiều sâu từ những đỉnh mà chúng ta đã đưa vào cặp ghép hiện tại bằng heuristic.

Ví dụ, bạn có thể chỉ cần lặp qua tất cả các đỉnh của phần đầu tiên, và đối với mỗi đỉnh trong số chúng, tìm một cạnh bất kỳ có thể được thêm vào cặp ghép, và thêm nó.
Ngay cả một heuristic đơn giản như vậy cũng có thể tăng tốc thuật toán Kuhn lên nhiều lần.

Xin lưu ý rằng vòng lặp chính sẽ phải được sửa đổi một chút. Vì khi gọi hàm $\textrm{try\_kuhn}$ trong vòng lặp chính, người ta cho rằng đỉnh hiện tại chưa được đưa vào cặp ghép, nên bạn cần thêm một kiểm tra thích hợp.

Trong cài đặt, chỉ mã trong hàm $\textrm{main}()$ sẽ thay đổi:

```cpp
int main() {
    // ... reading the graph ...

    mt.assign(k, -1);
    vector<bool> used1(n, false);
    for (int v = 0; v < n; ++v) {
        for (int to : g[v]) {
            if (mt[to] == -1) {
                mt[to] = v;
                used1[v] = true;
                break;
            }
        }
    }
    for (int v = 0; v < n; ++v) {
        if (used1[v])
            continue;
        used.assign(n, false);
        try_kuhn(v);
    }

    for (int i = 0; i < k; ++i)
        if (mt[i] != -1)
            printf("%d %d\n", mt[i] + 1, i + 1);
}
```

**Một heuristic tốt khác** như sau. Ở mỗi bước, nó sẽ tìm kiếm đỉnh có bậc nhỏ nhất (nhưng không cô lập), chọn bất kỳ cạnh nào từ nó và thêm nó vào cặp ghép, sau đó loại bỏ cả hai đỉnh này với tất cả các cạnh kề khỏi đồ thị. Sự tham lam như vậy hoạt động rất tốt trên các đồ thị ngẫu nhiên; trong nhiều trường hợp nó thậm chí còn xây dựng được cặp ghép cực đại (mặc dù có một trường hợp kiểm tra chống lại nó, trong đó nó sẽ tìm thấy một cặp ghép nhỏ hơn nhiều so với cực đại).

## Ghi chú (Notes) {: #notes}

* Thuật toán Kuhn là một chương trình con trong **thuật toán Hungary**, còn được gọi là **thuật toán Kuhn-Munkres**.
* Thuật toán Kuhn chạy trong thời gian $O(nm)$. Nó thường đơn giản để thực hiện, tuy nhiên, các thuật toán hiệu quả hơn tồn tại cho bài toán cặp ghép hai phía cực đại - chẳng hạn như **thuật toán Hopcroft-Karp-Karzanov**, chạy trong thời gian $O(\sqrt{n}m)$.
* [Bài toán phủ đỉnh nhỏ nhất](https://en.wikipedia.org/wiki/Vertex_cover) là NP-khó cho các đồ thị tổng quát. Tuy nhiên, [định lý Kőnig](https://en.wikipedia.org/wiki/K%C5%91nig%27s_theorem_(graph_theory)) cho rằng, đối với các đồ thị hai phía, lực lượng của cặp ghép cực đại bằng lực lượng của phủ đỉnh nhỏ nhất. Do đó, chúng ta có thể sử dụng các thuật toán cặp ghép hai phía cực đại để giải quyết bài toán phủ đỉnh nhỏ nhất trong thời gian đa thức cho các đồ thị hai phía.

## Bài tập (Practice Problems) {: #practice-problems}

* [Kattis - Gopher II](https://open.kattis.com/problems/gopher2)
* [Kattis - Borders](https://open.kattis.com/problems/borders)
