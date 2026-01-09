---
tags:
  - Translated
e_maxx_link: treap
---

# Treap (Cây Descartes) {: #treap-cartesian-tree}

Một treap là một cấu trúc dữ liệu kết hợp giữa cây nhị phân (binary tree) và heap nhị phân (binary heap) (do đó có tên: tree + heap $\Rightarrow$ Treap).

Cụ thể hơn, treap là một cấu trúc dữ liệu lưu trữ các cặp $(X, Y)$ trong một cây nhị phân theo cách mà nó là một cây tìm kiếm nhị phân theo $X$ và một heap nhị phân theo $Y$.
Nếu một nút nào đó của cây chứa các giá trị $(X_0, Y_0)$, tất cả các nút trong cây con bên trái có $X \leq X_0$, tất cả các nút trong cây con bên phải có $X_0 \leq X$, và tất cả các nút trong cả hai cây con bên trái và bên phải đều có $Y \leq Y_0$.

Một treap cũng thường được gọi là "cây Descartes" (cartesian tree), vì rất dễ nhúng nó vào một mặt phẳng Descartes:

<center>
<img src="https://upload.wikimedia.org/wikipedia/commons/e/e4/Treap.svg" width="350px"/>
</center>

Treap đã được đề xuất bởi Raimund Siedel và Cecilia Aragon vào năm 1989.

## Ưu điểm của cách tổ chức dữ liệu như vậy (Advantages of such data organisation) {: #advantages-of-such-data-organisation}

Trong cách cài đặt như vậy, các giá trị $X$ là các khóa (và đồng thời là các giá trị được lưu trữ trong treap), và các giá trị $Y$ được gọi là **độ ưu tiên** (priorities). Nếu không có độ ưu tiên, treap sẽ là một cây tìm kiếm nhị phân thông thường theo $X$, và một tập hợp các giá trị $X$ có thể tương ứng với rất nhiều cây khác nhau, một số trong đó bị suy biến (ví dụ, dưới dạng danh sách liên kết), và do đó cực kỳ chậm (các thao tác chính sẽ có độ phức tạp $O(N)$).

Đồng thời, **độ ưu tiên** (khi chúng là duy nhất) cho phép xác định **duy nhất** cây sẽ được xây dựng (tất nhiên, nó không phụ thuộc vào thứ tự mà các giá trị được thêm vào), điều này có thể được chứng minh bằng định lý tương ứng. Rõ ràng, nếu bạn **chọn độ ưu tiên một cách ngẫu nhiên**, bạn sẽ nhận được các cây không suy biến về trung bình, điều này sẽ đảm bảo độ phức tạp $O(\log N)$ cho các thao tác chính. Do đó tên gọi khác của cấu trúc dữ liệu này - **cây tìm kiếm nhị phân ngẫu nhiên** (randomized binary search tree).

## Các thao tác (Operations) {: #operations}

Một treap cung cấp các thao tác sau:

-   **Insert (X,Y)** trong $O(\log N)$.
    Thêm một nút mới vào cây. Một biến thể có thể là chỉ truyền $X$ và tạo $Y$ ngẫu nhiên bên trong thao tác.
-   **Search (X)** trong $O(\log N)$.
    Tìm kiếm một nút với giá trị khóa $X$ được chỉ định. Việc cài đặt giống như đối với một cây tìm kiếm nhị phân thông thường.
-   **Erase (X)** trong $O(\log N)$.
    Tìm kiếm một nút với giá trị khóa $X$ được chỉ định và xóa nó khỏi cây.
-   **Build ($X_1$, ..., $X_N$)** trong $O(N)$.
    Xây dựng một cây từ một danh sách các giá trị. Điều này có thể được thực hiện trong thời gian tuyến tính (giả sử rằng $X_1, ..., X_N$ đã được sắp xếp).
-   **Union ($T_1$, $T_2$)** trong $O(M \log (N/M))$.
    Hợp nhất hai cây, giả sử rằng tất cả các phần tử đều khác nhau. Có thể đạt được cùng độ phức tạp nểu các phần tử trùng lặp cần được loại bỏ trong khi hợp nhất.
-   **Intersect ($T_1$, $T_2$)** trong $O(M \log (N/M))$.
    Tìm giao của hai cây (tức là các phần tử chung của chúng). Chúng ta sẽ không xem xét việc cài đặt thao tác này ở đây.

Ngoài ra, do thực tế là treap là một cây tìm kiếm nhị phân, nó có thể thực hiện các thao tác khác, chẳng hạn như tìm phần tử lớn thứ $K$ hoặc tìm chỉ số của một phần tử.

## Mô tả cài đặt (Implementation Description) {: #implementation-description}

Về mặt cài đặt, mỗi nút chứa $X$, $Y$ và các con trỏ đến các con bên trái ($L$) và bên phải ($R$).

Chúng ta sẽ cài đặt tất cả các thao tác cần thiết chỉ bằng hai thao tác phụ trợ: Split (Tách) và Merge (Hợp).

### Split (Tách) {: #split}

<center>
<img src="https://upload.wikimedia.org/wikipedia/commons/6/69/Treap_split.svg" width="450px"/>
</center>

**Split ($T$, $X$)** tách cây $T$ thành 2 cây con $L$ và $R$ (là các giá trị trả về của split) sao cho $L$ chứa tất cả các phần tử có khóa $X_L \le X$, và $R$ chứa tất cả các phần tử có khóa $X_R > X$. Thao tác này có độ phức tạp $O (\log N)$ và được cài đặt bằng cách sử dụng để quy sạch:

1.  Nếu giá trị của nút gốc (R) là $\le X$, thì `L` ít nhất sẽ bao gồm `R->L` và `R`. Sau đó chúng ta gọi split trên `R->R`, và ghi nhận kết quả split của nó là `L'` và `R'`. Cuối cùng, `L` cũng sẽ chứa `L'`, trong khi `R = R'`.
2.  Nếu giá trị của nút gốc (R) là $> X$, thì `R` ít nhất sẽ bao gồm `R` và `R->R`. Sau đó chúng ta gọi split trên `R->L`, và ghi nhận kết quả split của nó là `L'` và `R'`. Cuối cùng, `L=L'`, trong khi `R` cũng sẽ chứa `R'`.

Do đó, thuật toán split là:

1.  quyết định cây con nào nút gốc sẽ thuộc về (trái hoặc phải)
2.  gọi đệ quy split trên một trong các con của nó
3.  tạo kết quả cuối cùng bằng cách sử dụng lại lệnh gọi split đệ quy.

### Merge (Hợp) {: #merge}

<center>
<img src="https://upload.wikimedia.org/wikipedia/commons/a/a8/Treap_merge.svg" width="500px"/>
</center>

**Merge ($T_1$, $T_2$)** kết hợp hai cây con $T_1$ và $T_2$ và trả về cây mới. Thao tác này cũng có độ phức tạp $O (\log N)$. Nó hoạt động dưới giả định rằng $T_1$ và $T_2$ đã được sắp xếp (tất cả các khóa $X$ trong $T_1$ đều nhỏ hơn các khóa trong $T_2$). Vì vậy, chúng ta cần kết hợp các cây này mà không vi phạm thứ tự của độ ưu tiên $Y$. Để làm điều này, chúng ta chọn cây nào có độ ưu tiên $Y$ cao hơn trong nút gốc làm gốc, và gọi đệ quy Merge cho cây kia và cây con tương ứng của nút gốc đã chọn.

### Insert (Chèn) {: #insert}

<center>
<img src="https://upload.wikimedia.org/wikipedia/commons/3/35/Treap_insert.svg" width="500px"/>
</center>

Bây giờ việc cài đặt **Insert ($X$, $Y$)** trở nên rõ ràng. Đầu tiên chúng ta đi xuống trong cây (như trong một cây tìm kiếm nhị phân thông thường theo X), và dừng lại ở nút đầu tiên mà giá trị độ ưu tiên nhỏ hơn $Y$. Chúng ta đã tìm thấy nơi chúng ta sẽ chèn phần tử mới. Tiếp theo, chúng ta gọi **Split (T, X)** trên cây con bắt đầu tại nút tìm thấy, và sử dụng các cây con $L$ và $R$ được trả về làm con trái và phải của nút mới.

Ngoài ra, insert có thể được thực hiện bằng cách tách treap ban đầu theo $X$ và thực hiện $2$ lần merge với nút mới (xem hình).

### Erase (Xóa) {: #erase}

<center>
<img src="https://upload.wikimedia.org/wikipedia/commons/6/62/Treap_erase.svg" width="500px"/>
</center>

Việc cài đặt **Erase ($X$)** cũng rõ ràng. Đầu tiên chúng ta đi xuống trong cây (như trong một cây tìm kiếm nhị phân thường theo $X$), tìm kiếm phần tử chúng ta muốn xóa. Khi tìm thấy nút, chúng ta gọi **Merge** trên các con của nó và đặt giá trị trả về của thao tác vào vị trí của phần tử chúng ta đang xóa.

Ngoài ra, chúng ta có thể tách cây con giữ $X$ bằng $2$ thao tác split và hợp nhất các treap còn lại (xem hình).

### Build (Xây dựng) {: #build}

Chúng ta cài đặt thao tác **Build** với độ phức tạp $O (N \log N)$ bằng cách sử dụng $N$ lệnh gọi **Insert**.

### Union (Hợp nhất) {: #union}

**Union ($T_1$, $T_2$)** có độ phức tạp lý thuyết là $O (M \log (N / M))$, nhưng trong thực tế nó hoạt động rất tốt, có thể với một hằng số ẩn rất nhỏ. Hãy giả sử không mất tính tổng quát rằng $T_1 \rightarrow Y > T_2 \rightarrow Y$, tức là gốc của $T_1$ sẽ là gốc của kết quả. Để có được kết quả, chúng ta cần hợp nhất các cây $T_1 \rightarrow L$, $T_1 \rightarrow R$ và $T_2$ thành hai cây có thể là con của gốc $T_1$. Để làm điều này, chúng ta gọi Split ($T_2$, $T_1\rightarrow X$), do đó tách $T_2$ thành hai phần L và R, sau đó chúng ta kết hợp đệ quy với các con của $T_1$: Union ($T_1 \rightarrow L$, $L$) và Union ($T_1 \rightarrow R$, $R$), do đó nhận được các cây con bên trái và bên phải của kết quả.

## Cài đặt (Implementation) {: #implementation}

```cpp
struct item {
	int key, prior;
	item *l, *r;
	item () { }
	item (int key) : key(key), prior(rand()), l(NULL), r(NULL) { }
	item (int key, int prior) : key(key), prior(prior), l(NULL), r(NULL) { }
};
typedef item* pitem;
```

Đây là định nghĩa item của chúng ta. Lưu ý có hai con trỏ con, và một khóa số nguyên (cho BST) và một độ ưu tiên số nguyên (cho heap). Độ ưu tiên được gán bằng cách sử dụng một bộ tạo số ngẫu nhiên.

```cpp
void split (pitem t, int key, pitem & l, pitem & r) {
	if (!t)
		l = r = NULL;
	else if (t->key <= key)
        split (t->r, key, t->r, r),  l = t;
	else
        split (t->l, key, l, t->l),  r = t;
}
```

`t` là treap để tách, và `key` là giá trị BST để tách theo. Lưu ý rằng chúng ta không `return` giá trị kết quả ở bất cứ đâu, thay vào đó, chúng ta chỉ sử dụng chúng như sau:

```cpp
pitem l = nullptr, r = nullptr;
split(t, 5, l, r);
if (l) cout << "Left subtree size: " << (l->size) << endl;
if (r) cout << "Right subtree size: " << (r->size) << endl;
```

Hàm `split` này có thể khó hiểu, vì nó có cả con trỏ (`pitem`) cũng như tham chiếu đến các con trỏ đó (`pitem &l`). Hãy hiểu bằng lời những gì hàm gọi `split(t, k, l, r)` dự định: "tách treap `t` theo giá trị `k` thành hai treap, và lưu trữ treap bên trái trong `l` và treap bên phải trong `r`". Tuyệt vời! Bây giờ, hãy áp dụng định nghĩa này cho hai lệnh gọi đệ quy, sử dụng trường hợp chúng ta đã phân tích trong phần trước: (Điều kiện if đầu tiên là trường hợp cơ sở tầm thường cho một treap rỗng)

1.  Khi giá trị nút gốc là $\le$ key, chúng ta gọi `split (t->r, key, t->r, r)`, có nghĩa là: "tách treap `t->r` (cây con bên phải của `t`) theo giá trị `key` và lưu trữ cây con bên trái trong `t->r` và cây con bên phải trong `r`". Sau đó, chúng ta đặt `l = t`. Lưu ý bây giờ giá trị kết quả `l` chứa `t->l`, `t` cũng như `t->r` (là kết quả của lệnh gọi đệ quy chúng ta đã thực hiện) tất cả đã được hợp nhất theo đúng thứ tự! Bạn nên tạm dừng để đảm bảo rằng kết quả này của `l` và `r` tương ứng chính xác với những gì chúng ta đã thảo luận trước đó trong Mô tả Cài đặt.
2.  Khi giá trị nút gốc lớn hơn key, chúng ta gọi `split (t->l, key, l, t->l)`, có nghĩa là: "tách treap `t->l` (cây con bên trái của `t`) theo giá trị `key` và lưu trữ cây con bên trái trong `l` và cây con bên phải trong `t->l`". Sau đó, chúng ta đặt `r = t`. Lưu ý bây giờ giá trị kết quả `r` chứa `t->l` (là kết quả của lệnh gọi đệ quy chúng ta đã thực hiện), `t` cũng như `t->r`, tất cả đã được hợp nhất theo đúng thứ tự! Bạn nên tạm dừng để đảm bảo rằng kết quả này của `l` và `r` tương ứng chính xác với những gì chúng ta đã thảo luận trước đó trong Mô tả Cài đặt.

Nếu bạn vẫn gặp khó khăn trong việc hiểu cài đặt, bạn nên nhìn vào nó một cách _quy nạp_, tức là: *đừng* cố gắng phá vỡ các lệnh gọi đệ quy lặp đi lặp lại. Giả sử việc cài đặt split hoạt động chính xác trên treap rỗng, sau đó thử chạy nó cho treap một nút, sau đó là treap hai nút, và cứ thế, mỗi lần sử dụng lại kiến thức của bạn rằng split trên các treap nhỏ hơn hoạt động.

```cpp
void insert (pitem & t, pitem it) {
	if (!t)
		t = it;
	else if (it->prior > t->prior)
		split (t, it->key, it->l, it->r),  t = it;
	else
		insert (t->key <= it->key ? t->r : t->l, it);
}

void merge (pitem & t, pitem l, pitem r) {
	if (!l || !r)
		t = l ? l : r;
	else if (l->prior > r->prior)
		merge (l->r, l->r, r),  t = l;
	else
		merge (r->l, l, r->l),  t = r;
}

void erase (pitem & t, int key) {
	if (t->key == key) {
		pitem th = t;
		merge (t, t->l, t->r);
		delete th;
	}
	else
		erase (key < t->key ? t->l : t->r, key);
}

pitem unite (pitem l, pitem r) {
	if (!l || !r)  return l ? l : r;
	if (l->prior < r->prior)  swap (l, r);
	pitem lt, rt;
	split (r, l->key, lt, rt);
	l->l = unite (l->l, lt);
	l->r = unite (l->r, rt);
	return l;
}
```

## Duy trì kích thước của các cây con (Maintaining the sizes of subtrees) {: #maintaining-the-sizes-of-subtrees}

Để mở rộng chức năng của treap, thường cần lưu trữ số lượng nút trong cây con của mỗi nút - trường `int cnt` trong cấu trúc `item`. Ví dụ, nó có thể được sử dụng để tìm phần tử lớn thứ K của cây trong $O (\log N)$, hoặc để tìm chỉ số của phần tử trong danh sách được sắp xếp với cùng độ phức tạp. Việc cài đặt các thao tác này sẽ giống như đối với cây tìm kiếm nhị phân thông thường.

Khi một cây thay đổi (các nút được thêm hoặc xóa, v.v.), `cnt` của một số nút nên được cập nhật tương ứng. Chúng ta sẽ tạo hai hàm: `cnt()` sẽ trả về giá trị hiện tại của `cnt` hoặc 0 nếu nút không tồn tại, và `upd_cnt()` sẽ cập nhật giá trị của `cnt` cho nút này giả sử rằng đối với các con của nó L và R, các giá trị của `cnt` đã được cập nhật. Rõ ràng là đủ để thêm các lệnh gọi `upd_cnt()` vào cuối `insert`, `erase`, `split` và `merge` để giữ cho các giá trị `cnt` được cập nhật.

```cpp
int cnt (pitem t) {
	return t ? t->cnt : 0;
}

void upd_cnt (pitem t) {
	if (t)
		t->cnt = 1 + cnt(t->l) + cnt (t->r);
}
```

## Xây dựng một Treap trong $O (N)$ ở chế độ offline (Building a Treap in O(N) in offline mode) {: #building-a-treap-in-o-n-in-offline-mode data-toc-label="Building a Treap in O(N) in offline mode"}

Cho một danh sách các khóa đã phân loại, có thể xây dựng một treap nhanh hơn so với việc chèn các khóa từng cái một mất $O(N \log N)$. Vì các khóa đã được sắp xếp, một cây tìm kiếm nhị phân cân bằng có thể được xây dựng dễ dàng trong thời gian tuyến tính. Các giá trị heap $Y$ được khởi tạo ngẫu nhiên và sau đó có thể được heapify độc lập với các khóa $X$ để [xây dựng heap](https://en.wikipedia.org/wiki/Binary_heap#Building_a_heap) trong $O(N)$.

```cpp
void heapify (pitem t) {
	if (!t) return;
	pitem max = t;
	if (t->l != NULL && t->l->prior > max->prior)
		max = t->l;
	if (t->r != NULL && t->r->prior > max->prior)
		max = t->r;
	if (max != t) {
		swap (t->prior, max->prior);
		heapify (max);
	}
}

pitem build (int * a, int n) {
	// Construct a treap on values {a[0], a[1], ..., a[n - 1]}
	if (n == 0) return NULL;
	int mid = n / 2;
	pitem t = new item (a[mid], rand ());
	t->l = build (a, mid);
	t->r = build (a + mid + 1, n - mid - 1);
	heapify (t);
	upd_cnt(t)
	return t;
}
```

Lưu ý: gọi `upd_cnt(t)` chỉ cần thiết nếu bạn cần kích thước cây con.

Cách tiếp cận trên luôn cung cấp một cây cân bằng hoàn hảo, điều này thường tốt cho các mục đích thực tế, nhưng với cái giá là không bảo tồn các ưu tiên ban đầu được gán cho mỗi nút. Do đó, cách tiếp cận này không khả thi để giải quyết vấn đề sau:

!!! example "[acmsguru - Cartesian Tree](https://codeforces.com/problemsets/acmsguru/problem/99999/155)"
    Cho một dãy các cặp $(x_i, y_i)$, xây dựng một cây Descartes trên chúng. Tất cả $x_i$ và tất cả $y_i$ là duy nhất.

Lưu ý rằng trong bài toán này các ưu tiên không phải là ngẫu nhiên, do đó chỉ cần chèn các đỉnh từng cái một có thể cung cấp một giải pháp bậc hai.

Một trong những giải pháp khả thi ở đây là tìm cho mỗi phần tử các phần tử gần nhất bên trái và bên phải có độ ưu tiên nhỏ hơn phần tử này. Trong số hai phần tử này, phần tử có độ ưu tiên lớn hơn phải là cha của phần tử hiện tại.

Bài toán này có thể giải được với sửa đổi [ngăn xếp tìm min](./stack_queue_modification.md) trong thời gian tuyến tính:

```cpp
void connect(auto from, auto to) {
    vector<pitem> st;
    for(auto it: ranges::subrange(from, to)) {
        while(!st.empty() && st.back()->prior > it->prior) {
            st.pop_back();
        }
        if(!st.empty()) {
            if(!it->p || it->p->prior < st.back()->prior) {
                it->p = st.back();
            }
        }
        st.push_back(it);
    }
}

pitem build(int *x, int *y, int n) {
    vector<pitem> nodes(n);
    for(int i = 0; i < n; i++) {
        nodes[i] = new item(x[i], y[i]);
    }
    connect(nodes.begin(), nodes.end());
    connect(nodes.rbegin(), nodes.rend());
    for(int i = 0; i < n; i++) {
        if(nodes[i]->p) {
            if(nodes[i]->p->key < nodes[i]->key) {
                nodes[i]->p->r = nodes[i];
            } else {
                nodes[i]->p->l = nodes[i];
            }
        }
    }
    return nodes[min_element(y, y + n) - y];
}
```

## Implicit Treaps (Treap ngầm định) {: #implicit-treaps}

Treap ngầm định là một sửa đổi đơn giản của treap thông thường nhưng là một cấu trúc dữ liệu rất mạnh mẽ. Trên thực tế, treap ngầm định có thể được coi là một mảng với các thủ tục sau được cài đặt (tất cả trong $O (\log N)$ trong chế độ trực tuyến):

-   Chèn một phần tử vào mảng ở bất kỳ vị trí nào
-   Xóa một phần tử tùy ý
-   Tìm tổng, phần tử nhỏ nhất / lớn nhất, v.v. trên một khoảng tùy ý
-   Phép cộng, tô màu trên một khoảng tùy ý
-   Đảo ngược các phần tử trên một khoảng tùy ý

Ý tưởng là các khóa phải là các **chỉ số** dựa trên null của các phần tử trong mảng. Nhưng chúng ta sẽ không lưu trữ các giá trị này một cách rõ ràng (nếu không, ví dụ, chèn một phần tử sẽ gây ra thay đổi khóa trong $O (N)$ nút của cây).

Lưu ý rằng khóa của một nút là số lượng nút nhỏ hơn nó (các nút như vậy có thể hiện diện không chỉ trong cây con bên trái của nó mà còn trong các cây con bên trái của tổ tiên nó).
Cụ thể hơn, **khóa ngầm định** (implicit key) cho một số nút T là số lượng đỉnh $cnt (T \rightarrow L)$ trong cây con bên trái của nút này cộng với các giá trị tương tự $cnt (P \rightarrow L) + 1$ cho mỗi tổ tiên P của nút T, và nếu T nằm trong cây con bên phải của P.

Bây giờ đã rõ cách tính toán nhanh khóa ngầm định của nút hiện tại. Vì trong tất cả các thao tác, chúng ta đến bất kỳ nút nào bằng cách đi xuống trong cây, chúng ta chỉ có thể tích lũy tổng này và chuyển nó cho hàm. Nếu chúng ta đi đến cây con bên trái, tổng tích lũy không thay đổi, nếu chúng ta đi đến cây con bên phải, nó tăng thêm $cnt (T \rightarrow L) +1$.

Dưới đây là các cài đặt mới của **Split** và **Merge**:

```cpp
void merge (pitem & t, pitem l, pitem r) {
	if (!l || !r)
		t = l ? l : r;
	else if (l->prior > r->prior)
		merge (l->r, l->r, r),  t = l;
	else
		merge (r->l, l, r->l),  t = r;
	upd_cnt (t);
}

void split (pitem t, pitem & l, pitem & r, int key, int add = 0) {
	if (!t)
		return void( l = r = 0 );
	int cur_key = add + cnt(t->l); //implicit key
	if (key <= cur_key)
		split (t->l, l, t->l, key, add),  r = t;
	else
		split (t->r, t->r, r, key, add + 1 + cnt(t->l)),  l = t;
	upd_cnt (t);
}
```

Trong cài đặt trên, sau lệnh gọi $split(T, T_1, T_2, k)$, cây $T_1$ sẽ bao gồm $k$ phần tử đầu tiên của $T$ (tức là, các phần tử có khóa ngầm định nhỏ hơn $k$) và $T_2$ sẽ bao gồm tất cả các phần còn lại.

Bây giờ hãy xem xét việc cài đặt các thao tác khác nhau trên các treap ngầm định:

-   **Chèn phần tử**.
    Giả sử chúng ta cần chèn một phần tử tại vị trí $pos$. Chúng ta chia treap thành hai phần, tương ứng với các mảng $[0..pos-1]$ và $[pos..sz]$; để làm điều này chúng ta gọi $split(T, T_1, T_2, pos)$. Sau đó chúng ta có thể kết hợp cây $T_1$ với đỉnh mới bằng cách gọi $merge(T_1, T_1, \text{new item})$ (dễ thấy rằng tất cả các điều kiện tiên quyết đều được đáp ứng). Cuối cùng, chúng ta kết hợp các cây $T_1$ và $T_2$ trở lại thành $T$ bằng cách gọi $merge(T, T_1, T_2)$.
-   **Xóa phần tử**.
    Thao tác này thậm chí còn dễ dàng hơn: tìm phần tử cần xóa $T$, thực hiện merge các con của nó $L$ và $R$, và thay thế phần tử $T$ bằng kết quả của merge. Trên thực tế, xóa phần tử trong treap ngầm định hoàn toàn giống như trong treap thông thường.
-   Tìm **tổng / giá trị nhỏ nhất**, v.v. trên khoảng.
    Đầu tiên, tạo thêm một trường $F$ trong cấu trúc `item` để lưu trữ giá trị của hàm mục tiêu cho cây con của nút này. Trường này dễ bảo trì tương tự như duy trì kích thước của các cây con: tạo một hàm tính toán giá trị này cho một nút dựa trên các giá trị cho các con của nó và thêm các lệnh gọi hàm này vào cuối tất cả các hàm sửa đổi cây.
    Thứ hai, chúng ta cần biết cách xử lý truy vấn cho một khoảng tùy ý $[A; B]$.
    Để lấy một phần của cây tương ứng với khoảng $[A; B]$, chúng ta cần gọi $split(T, T_2, T_3, B+1)$, và sau đó $split(T_2, T_1, T_2, A)$: sau đó $T_2$ sẽ bao gồm tất cả các phần tử trong khoảng $[A; B]$, và chỉ chúng mà thôi. Do đó, phản hồi cho truy vấn sẽ được lưu trữ trong trường $F$ của gốc của $T_2$. Sau khi truy vấn được trả lời, cây phải được khôi phục bằng cách gọi $merge(T, T_1, T_2)$ và $merge(T, T, T_3)$.
-   **Phép cộng / tô màu** trên khoảng.
    Chúng ta hành động tương tự như đoạn trước, nhưng thay vì trường F chúng ta sẽ lưu trữ một trường `add` sẽ chứa giá trị đã thêm cho cây con (hoặc giá trị mà cây con được tô màu). Trước khi thực hiện bất kỳ thao tác nào, chúng ta phải "đẩy" (push) giá trị này một cách chính xác - tức là thay đổi $T \rightarrow L \rightarrow add$ và $T \rightarrow R \rightarrow add$, và làm sạch `add` trong nút cha. Theo cách này sau bất kỳ thay đổi nào đối với cây thông tin sẽ không bị mất.
-   **Đảo ngược** trên khoảng.
    Điều này một lần nữa tương tự như thao tác trước: chúng ta phải thêm cờ boolean `rev` và đặt nó thành true khi cây con của nút hiện tại phải được đảo ngược. Việc "đẩy" giá trị này hơi phức tạp - chúng ta hoán đổi các con của nút này và đặt cờ này thành true cho chúng.

Dưới đây là một ví dụ cài đặt của treap ngầm định với đảo ngược trên khoảng. Đối với mỗi nút, chúng ta lưu trữ trường được gọi là `value` là giá trị thực tế của phần tử mảng tại vị trí hiện tại. Chúng ta cũng cung cấp việc cài đặt hàm `output()`, xuất ra một mảng tương ứng với trạng thái hiện tại của treap ngầm định.

```cpp
typedef struct item * pitem;
struct item {
	int prior, value, cnt;
	bool rev;
	pitem l, r;
};

int cnt (pitem it) {
	return it ? it->cnt : 0;
}

void upd_cnt (pitem it) {
	if (it)
		it->cnt = cnt(it->l) + cnt(it->r) + 1;
}

void push (pitem it) {
	if (it && it->rev) {
		it->rev = false;
		swap (it->l, it->r);
		if (it->l)  it->l->rev ^= true;
		if (it->r)  it->r->rev ^= true;
	}
}

void merge (pitem & t, pitem l, pitem r) {
	push (l);
	push (r);
	if (!l || !r)
		t = l ? l : r;
	else if (l->prior > r->prior)
		merge (l->r, l->r, r),  t = l;
	else
		merge (r->l, l, r->l),  t = r;
	upd_cnt (t);
}

void split (pitem t, pitem & l, pitem & r, int key, int add = 0) {
	if (!t)
		return void( l = r = 0 );
	push (t);
	int cur_key = add + cnt(t->l);
	if (key <= cur_key)
		split (t->l, l, t->l, key, add),  r = t;
	else
		split (t->r, t->r, r, key, add + 1 + cnt(t->l)),  l = t;
	upd_cnt (t);
}

void reverse (pitem t, int l, int r) {
	pitem t1, t2, t3;
	split (t, t1, t2, l);
	split (t2, t2, t3, r-l+1);
	t2->rev ^= true;
	merge (t, t1, t2);
	merge (t, t, t3);
}

void output (pitem t) {
	if (!t)  return;
	push (t);
	output (t->l);
	printf ("%d ", t->value);
	output (t->r);
}
```

## Tài liệu tham khảo (Literature) {: #literature}

*   [Blelloch, Reid-Miller "Fast Set Operations Using Treaps"](https://www.cs.cmu.edu/~scandal/papers/treaps-spaa98.pdf)

## Bài tập (Practice Problems) {: #practice-problems}

*   [SPOJ - Ada and Aphids](http://www.spoj.com/problems/ADAAPHID/)
*   [SPOJ - Ada and Harvest](http://www.spoj.com/problems/ADACROP/)
*   [Codeforces - Radio Stations](http://codeforces.com/contest/762/problem/E)
*   [SPOJ - Ghost Town](http://www.spoj.com/problems/COUNT1IT/)
*   [SPOJ - Arrangement Validity](http://www.spoj.com/problems/IITWPC4D/)
*   [SPOJ - All in One](http://www.spoj.com/problems/ALLIN1/)
*   [Codeforces - Dog Show](http://codeforces.com/contest/847/problem/D)
*   [Codeforces - Yet Another Array Queries Problem](http://codeforces.com/contest/863/problem/D)
*   [SPOJ - Mean of Array](http://www.spoj.com/problems/MEANARR/)
*   [SPOJ - TWIST](http://www.spoj.com/problems/TWIST/)
*   [SPOJ - KOILINE](http://www.spoj.com/problems/KOILINE/)
*   [CodeChef - The Prestige](https://www.codechef.com/problems/PRESTIGE)
*   [Codeforces - T-Shirts](https://codeforces.com/contest/702/problem/F)
*   [Codeforces - Wizards and Roads](https://codeforces.com/problemset/problem/167/D)
*   [Codeforces - Yaroslav and Points](https://codeforces.com/contest/295/problem/E)

---
