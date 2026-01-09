---
tags:
  - Translated
e_maxx_link: sqrt_tree
---

# Sqrt Tree {: #sqrt-tree}

Cho một mảng $a$ chứa $n$ phần tử và phép toán $\circ$ thỏa mãn tính chất kết hợp: $(x \circ y) \circ z = x \circ (y \circ z)$ là đúng với mọi $x$, $y$, $z$.

Vì vậy, các phép toán như $\gcd$, $\min$, $\max$, $+$, $\text{and}$, $\text{or}$, $\text{xor}$, v.v. thỏa mãn các điều kiện này.

Ngoài ra chúng ta có một số truy vấn $q(l, r)$. Đối với mỗi truy vấn, chúng ta cần tính $a_l \circ a_{l+1} \circ \dots \circ a_r$.

Sqrt Tree có thể xử lý các truy vấn như vậy trong thời gian $O(1)$ với thời gian tiền xử lý $O(n \cdot \log \log n)$ và bộ nhớ $O(n \cdot \log \log n)$.

## Mô tả (Description) {: #description}

### Xây dựng phân rã căn bậc hai (Building sqrt decomposition) {: #building-sqrt-decomposition}

Hãy thực hiện một [phân rã căn bậc hai (sqrt decomposition)](sqrt-decomposition.md). Chúng ta chia mảng của mình thành $\sqrt{n}$ khối, mỗi khối có kích thước $\sqrt{n}$. Đối với mỗi khối, chúng ta tính toán:

1.  Câu trả lời cho các truy vấn nằm trong khối và bắt đầu ở đầu khối ($\text{prefixOp}$)
2.  Câu trả lời cho các truy vấn nằm trong khối và kết thúc ở cuối khối ($\text{suffixOp}$)

Và chúng ta sẽ tính toán thêm một mảng:

3.  $\text{between}_{i, j}$ (với $i \le j$) - câu trả lời cho truy vấn bắt đầu ở đầu khối $i$ và kết thúc ở cuối khối $j$. Lưu ý rằng chúng ta có $\sqrt{n}$ khối, vì vậy kích thước của mảng này sẽ là $O(\sqrt{n}^2) = O(n)$.

Hãy xem ví dụ.

Giả sử $\circ$ là $+$ (chúng ta tính tổng trên một đoạn) và chúng ta có mảng $a$ sau:

`{1, 2, 3, 4, 5, 6, 7, 8, 9}`

Nó sẽ được chia thành ba khối: `{1, 2, 3}`, `{4, 5, 6}` và `{7, 8, 9}`.

Đối với khối đầu tiên $\text{prefixOp}$ là `{1, 3, 6}` và $\text{suffixOp}$ là `{6, 5, 3}`.

Đối với khối thứ hai $\text{prefixOp}$ là `{4, 9, 15}` và $\text{suffixOp}$ là `{15, 11, 6}`.

Đối với khối thứ ba $\text{prefixOp}$ là `{7, 15, 24}` và $\text{suffixOp}$ là `{24, 17, 9}`.

Mảng $\text{between}$ là:

~~~~~
{
    {6, 21, 45},
    {0, 15, 39},
    {0, 0,  24}
}
~~~~~

(chúng ta giả sử rằng các phần tử không hợp lệ nơi $i > j$ được điền bằng số không)

Rõ ràng để thấy rằng các mảng này có thể được tính toán dễ dàng trong thời gian và bộ nhớ $O(n)$.

Chúng ta đã có thể trả lời một số truy vấn bằng các mảng này. Nếu truy vấn không nằm gọn trong một khối, chúng ta có thể chia nó thành ba phần: hậu tố của một khối, sau đó là một đoạn của các khối liền kề và sau đó là tiền tố của một khối nào đó. Chúng ta có thể trả lời một truy vấn bằng cách chia nó thành ba phần và thực hiện phép toán của chúng ta với một giá trị từ $\text{suffixOp}$, sau đó một giá trị từ $\text{between}$, sau đó một giá trị từ $\text{prefixOp}$.

Nhưng nếu chúng ta có các truy vấn nằm hoàn toàn trong một khối, chúng ta không thể xử lý chúng bằng ba mảng này. Vì vậy, chúng ta cần phải làm gì đó.

### Tạo một cái cây (Making a tree) {: #making-a-tree}

Chúng ta không thể trả lời các truy vấn nằm hoàn toàn trong một khối. Nhưng điều gì sẽ xảy ra **nếu chúng ta xây dựng cùng một cấu trúc như mô tả ở trên cho mỗi khối?** Đúng vậy, chúng ta có thể làm điều đó. Và chúng ta làm điều đó một cách đệ quy, cho đến khi chúng ta đạt đến kích thước khối là $1$ hoặc $2$. Câu trả lời cho các khối như vậy có thể được tính toán dễ dàng trong $O(1)$.

Vì vậy, chúng ta nhận được một cái cây. Mỗi nút của cây đại diện cho một đoạn của mảng. Nút đại diện cho đoạn mảng có kích thước $k$ có $\sqrt{k}$ con -- cho mỗi khối. Ngoài ra mỗi nút chứa ba mảng được mô tả ở trên cho đoạn mà nó chứa. Gốc của cây đại diện cho toàn bộ mảng. Các nút có độ dài đoạn $1$ hoặc $2$ là các lá.

Cũng rõ ràng là chiều cao của cây này là $O(\log \log n)$, bởi vì nếu một đỉnh nào đó của cây đại diện cho một mảng có độ dài $k$, thì các con của nó có độ dài $\sqrt{k}$. $\log(\sqrt{k}) = \frac{\log{k}}{2}$, vì vậy $\log k$ giảm hai lần mỗi lớp của cây và do đó chiều cao của nó là $O(\log \log n)$. Thời gian xây dựng và sử dụng bộ nhớ sẽ là $O(n \cdot \log \log n)$, bởi vì mỗi phần tử của mảng xuất hiện chính xác một lần trên mỗi lớp của cây.

Bây giờ chúng ta có thể trả lời các truy vấn trong $O(\log \log n)$. Chúng ta có thể đi xuống cây cho đến khi gặp một đoạn có độ dài $1$ hoặc $2$ (câu trả lời cho nó có thể được tính trong thời gian $O(1)$) hoặc gặp đoạn đầu tiên mà truy vấn của chúng ta không nằm gọn hoàn toàn trong một khối. Xem phần đầu tiên về cách trả lời truy vấn trong trường hợp này.

OK, bây giờ chúng ta có thể thực hiện $O(\log \log n)$ mỗi truy vấn. Có thể làm nhanh hơn không?

### Tối ưu hóa độ phức tạp truy vấn (Optimizing the query complexity) {: #optimizing-the-query-complexity}

Một trong những tối ưu hóa rõ ràng nhất là tìm kiếm nhị phân nút cây chúng ta cần. Sử dụng tìm kiếm nhị phân, chúng ta có thể đạt được độ phức tạp $O(\log \log \log n)$ mỗi truy vấn. Chúng ta có thể làm nhanh hơn nữa không?

Câu trả lời là có. Hãy giả sử hai điều sau:

1.  Kích thước mỗi khối là một lũy thừa của hai.
2.  Tất cả các khối đều bằng nhau trên mỗi lớp.

Để đạt được điều này, chúng ta có thể thêm một số phần tử zero vào mảng của mình để kích thước của nó trở thành lũy thừa của hai.

Khi chúng ta sử dụng điều này, kích thước một số khối có thể trở nên lớn gấp đôi để trở thành lũy thừa của hai, nhưng nó vẫn có kích thước $O(\sqrt{k})$ và chúng ta giữ độ phức tạp tuyến tính để xây dựng các mảng trong một đoạn.

Bây giờ, chúng ta có thể dễ dàng kiểm tra xem truy vấn có nằm hoàn toàn trong một khối có kích thước $2^k$ hay không. Hãy viết các phạm vi của truy vấn, $l$ và $r$ (chúng ta sử dụng chỉ số 0) dưới dạng nhị phân. Ví dụ: giả sử $k=4, l=39, r=46$. Biểu diễn nhị phân của $l$ và $r$ là:

$l = 39_{10} = 100111_2$

$r = 46_{10} = 101110_2$

Hãy nhớ rằng một lớp chứa các đoạn có kích thước bằng nhau, và khối trên một lớp cũng có kích thước bằng nhau (trong trường hợp của chúng ta, kích thước của chúng là $2^k = 2^4 = 16$. Các khối bao phủ mảng hoàn toàn, vì vậy khối đầu tiên bao phủ các phần tử $(0 - 15)$ ($(000000_2 - 001111_2)$ trong hệ nhị phân), khối thứ hai bao phủ các phần tử $(16 - 31)$ ($(010000_2 - 011111_2)$ trong hệ nhị phân) và cứ thế. Chúng ta thấy rằng các chỉ số của các vị trí được bao phủ bởi một khối có thể chỉ khác nhau ở $k$ bit cuối cùng (trong trường hợp của chúng ta là $4$). Trong trường hợp của chúng ta $l$ và $r$ có các bit bằng nhau ngoại trừ bốn bit thấp nhất, vì vậy chúng nằm trong một khối.

Vì vậy, chúng ta cần kiểm tra xem không có gì nhiều hơn $k$ bit nhỏ nhất khác nhau (hoặc $l\ \text{xor}\ r$ không vượt quá $2^k-1$).

Sử dụng quan sát này, chúng ta có thể tìm thấy một lớp phù hợp để trả lời truy vấn một cách nhanh chóng. Cách làm điều này:

1.  Đối với mỗi $i$ không vượt quá kích thước mảng, chúng ta tìm bit cao nhất bằng $1$. Để làm điều này nhanh chóng, chúng ta sử dụng DP và một mảng được tính toán trước.

2.  Bây giờ, đối với mỗi $q(l, r)$ chúng ta tìm bit cao nhất của $l\ \text{xor}\ r$ và, sử dụng thông tin này, thật dễ dàng để chọn lớp mà chúng ta có thể xử lý truy vấn một cách dễ dàng. Chúng ta cũng có thể sử dụng một mảng được tính toán trước ở đây.

Để biết thêm chi tiết, hãy xem mã bên dưới.

Vì vậy, sử dụng điều này, chúng ta có thể trả lời các truy vấn trong $O(1)$ mỗi truy vấn. Hoan hô! :)

## Cập nhật các phần tử (Updating elements) {: #updating-elements}

Chúng ta cũng có thể cập nhật các phần tử trong Sqrt Tree. Cả cập nhật phần tử đơn lẻ và cập nhật trên một đoạn đều được hỗ trợ.

### Cập nhật một phần tử đơn lẻ (Updating a single element) {: #updating-a-single-element}

Xem xét một truy vấn $\text{update}(x, val)$ thực hiện phép gán $a_x = val$. Chúng ta cần thực hiện truy vấn này đủ nhanh.

#### Cách tiếp cận ngây thơ (Naive approach) {: #naive-approach}

Đầu tiên, hãy xem những gì thay đổi trong cây khi một phần tử đơn lẻ thay đổi. Xem xét một nút cây có độ dài $l$ và các mảng của nó: $\text{prefixOp}$, $\text{suffixOp}$ và $\text{between}$. Dễ thấy rằng chỉ có $O(\sqrt{l})$ phần tử từ $\text{prefixOp}$ và $\text{suffixOp}$ thay đổi (chỉ bên trong khối với phần tử đã thay đổi). $O(l)$ phần tử được thay đổi trong $\text{between}$. Do đó, $O(l)$ phần tử trong nút cây được cập nhật.

Chúng ta nhớ rằng bất kỳ phần tử $x$ nào cũng hiện diện trong chính xác một nút cây ở mỗi lớp. Nút gốc (lớp $0$) có độ dài $O(n)$, các nút trên lớp $1$ có độ dài $O(\sqrt{n})$, các nút trên lớp $2$ có độ dài $O(\sqrt{\sqrt{n}})$, v.v. Vì vậy, độ phức tạp thời gian cho mỗi lần cập nhật là $O(n + \sqrt{n} + \sqrt{\sqrt{n}} + \dots) = O(n)$.

Nhưng nó quá chậm. Có thể làm nhanh hơn không?

#### Một sqrt-tree bên trong sqrt-tree (An sqrt-tree inside the sqrt-tree) {: #an-sqrt-tree-inside-the-sqrt-tree}

Lưu ý rằng nút thắt cổ chai của việc cập nhật là xây dựng lại $\text{between}$ của nút gốc. Để tối ưu hóa cây, hãy loại bỏ mảng này! Thay vì mảng $\text{between}$, chúng ta lưu trữ một sqrt-tree khác cho nút gốc. Hãy gọi nó là $\text{index}$. Nó đóng vai trò tương tự như $\text{between}$&mdash; trả lời các truy vấn trên các đoạn của các khối. Lưu ý rằng các nút cây còn lại không có $\text{index}$, chúng giữ các mảng $\text{between}$ của mình.

Một sqrt-tree được gọi là _được lập chỉ mục_ (_indexed_), nếu nút gốc của nó có $\text{index}$. Một sqrt-tree với mảng $\text{between}$ trong nút gốc của nó là _không được lập chỉ mục_ (_unindexed_). Lưu ý rằng $\text{index}$ **bản thân nó là _không được lập chỉ mục_**.

Vì vậy, chúng ta có thuật toán sau để cập nhật một cây _được lập chỉ mục_:

*   Cập nhật $\text{prefixOp}$ và $\text{suffixOp}$ trong $O(\sqrt{n})$.

*   Cập nhật $\text{index}$. Nó có độ dài $O(\sqrt{n})$ và chúng ta chỉ cần cập nhật một mục trong đó (mục đại diện cho khối đã thay đổi). Vì vậy, độ phức tạp thời gian cho bước này là $O(\sqrt{n})$. Chúng ta có thể sử dụng thuật toán được mô tả ở đầu phần này (thuật toán "chậm") để làm điều đó.

*   Đi vào nút con đại diện cho khối đã thay đổi và cập nhật nó trong $O(\sqrt{n})$ bằng thuật toán "chậm".

Lưu ý rằng độ phức tạp truy vấn vẫn là $O(1)$: chúng ta cần sử dụng $\text{index}$ trong truy vấn không quá một lần, và điều này sẽ mất thời gian $O(1)$.

Vì vậy, tổng độ phức tạp thời gian để cập nhật một phần tử đơn lẻ là $O(\sqrt{n})$. Hoan hô! :)

### Cập nhật một đoạn (Updating a segment) {: #updating-a-segment}

Sqrt-tree cũng có thể thực hiện những việc như gán một phần tử trên một đoạn. $\text{massUpdate}(x, l, r)$ có nghĩa là $a_i = x$ cho tất cả $l \le i \le r$.

Có hai cách tiếp cận để làm điều này: một trong số chúng thực hiện $\text{massUpdate}$ trong $O(\sqrt{n}\cdot \log \log n)$, giữ $O(1)$ cho mỗi truy vấn. Cách thứ hai thực hiện $\text{massUpdate}$ trong $O(\sqrt{n})$, nhưng độ phức tạp truy vấn trở thành $O(\log \log n)$.

Chúng ta sẽ thực hiện lazy propagation theo cùng một cách như được thực hiện trong segment trees: chúng ta đánh dấu một số nút là _lazy_, nghĩa là chúng ta sẽ đẩy chúng khi cần thiết. Nhưng có một điều khác với segment trees: đẩy một nút rất tốn kém, vì vậy nó không thể được thực hiện trong các truy vấn. Trên lớp $0$, đẩy một nút mất thời gian $O(\sqrt{n})$. Vì vậy, chúng ta không đẩy các nút bên trong các truy vấn, chúng ta chỉ xem liệu nút hiện tại hoặc cha của nó có _lazy_ hay không, và chỉ tính đến nó trong khi thực hiện các truy vấn.

#### Cách tiếp cận đầu tiên (First approach) {: #first-approach}

Trong cách tiếp cận đầu tiên, chúng ta nói rằng chỉ các nút trên lớp $1$ (với độ dài $O(\sqrt{n}$) có thể là _lazy_. Khi đẩy một nút như vậy, nó cập nhật tất cả cây con của nó bao gồm chính nó trong $O(\sqrt{n}\cdot \log \log n)$. Quá trình $\text{massUpdate}$ được thực hiện như sau:

*   Xem xét các nút trên lớp $1$ và các khối tương ứng với chúng.

*   Một số khối được bao phủ hoàn toàn bởi $\text{massUpdate}$. Đánh dấu chúng là _lazy_ trong $O(\sqrt{n})$.

*   Một số khối được bao phủ một phần. Lưu ý rằng không có quá hai khối loại này. Xây dựng lại chúng trong $O(\sqrt{n}\cdot \log \log n)$. Nếu chúng là _lazy_, hãy tính đến nó.

*   Cập nhật $\text{prefixOp}$ và $\text{suffixOp}$ cho các khối được bao phủ một phần trong $O(\sqrt{n})$ (bởi vì chỉ có hai khối như vậy).

*   Xây dựng lại $\text{index}$ trong $O(\sqrt{n}\cdot \log \log n)$.

Vì vậy, chúng ta có thể thực hiện $\text{massUpdate}$ nhanh chóng. Nhưng lazy propagation ảnh hưởng đến các truy vấn như thế nào? Chúng sẽ có các sửa đổi sau:

*   Nếu truy vấn của chúng ta nằm hoàn toàn trong một khối _lazy_, hãy tính toán nó và tính đến _lazy_. $O(1)$.

*   Nếu truy vấn của chúng ta bao gồm nhiều khối, một số trong đó là _lazy_, chúng ta chỉ cần quan tâm đến _lazy_ trên khối ngoài cùng bên trái và ngoài cùng bên phải. Các khối còn lại được tính toán bằng cách sử dụng $\text{index}$, vốn đã biết câu trả lời trên khối _lazy_ (vì nó được xây dựng lại sau mỗi lần sửa đổi). $O(1)$.

Độ phức tạp truy vấn vẫn là $O(1)$.

#### Cách tiếp cận thứ hai (Second approach) {: #second-approach}

Trong cách tiếp cận này, mỗi nút có thể là _lazy_ (trừ gốc). Ngay cả các nút trong $\text{index}$ cũng có thể là _lazy_. Vì vậy, trong khi xử lý một truy vấn, chúng ta phải tìm các thẻ _lazy_ trong tất cả các nút cha, tức là độ phức tạp truy vấn sẽ là $O(\log \log n)$.

Nhưng $\text{massUpdate}$ trở nên nhanh hơn. Nó trông như sau:

*   Một số khối được bao phủ hoàn toàn với $\text{massUpdate}$. Vì vậy, các thẻ _lazy_ được thêm vào chúng. Đó là $O(\sqrt{n})$.

*   Cập nhật $\text{prefixOp}$ và $\text{suffixOp}$ cho các khối được bao phủ một phần trong $O(\sqrt{n})$ (bởi vì chỉ có hai khối như vậy).

*   Đừng quên cập nhật index. Đó là $O(\sqrt{n})$ (chúng ta sử dụng cùng một thuật toán $\text{massUpdate}$).

*   Cập nhật mảng $\text{between}$ cho các cây con _unindexed_.

*   Đi vào các nút đại diện cho các khối được bao phủ một phần và gọi $\text{massUpdate}$ một cách đệ quy.

Lưu ý rằng khi chúng ta thực hiện cuộc gọi đệ quy, chúng ta thực hiện $\text{massUpdate}$ tiền tố hoặc hậu tố. Nhưng đối với các cập nhật tiền tố và hậu tố, chúng ta không thể có quá một con được bao phủ một phần. Vì vậy, chúng ta truy cập một nút trên lớp $1$, hai nút trên lớp $2$ và hai nút trên bất kỳ cấp độ sâu hơn nào. Vì vậy, độ phức tạp thời gian là $O(\sqrt{n} + \sqrt{\sqrt{n}} + \dots) = O(\sqrt{n})$. Cách tiếp cận ở đây tương tự như cập nhật hàng loạt segment tree.

## Cài đặt (Implementation) {: #implementation}

Việc cài đặt sau đây của Sqrt Tree có thể thực hiện các thao tác sau: xây dựng trong $O(n \cdot \log \log n)$, trả lời các truy vấn trong $O(1)$ và cập nhật một phần tử trong $O(\sqrt{n})$.

```cpp
SqrtTreeItem op(const SqrtTreeItem &a, const SqrtTreeItem &b);

inline int log2Up(int n) {
	int res = 0;
	while ((1 << res) < n) {
		res++;
	}
	return res;
}

class SqrtTree {
private:
	int n, lg, indexSz;
	vector<SqrtTreeItem> v;
	vector<int> clz, layers, onLayer;
	vector< vector<SqrtTreeItem> > pref, suf, between;
	
	inline void buildBlock(int layer, int l, int r) {
		pref[layer][l] = v[l];
		for (int i = l+1; i < r; i++) {
			pref[layer][i] = op(pref[layer][i-1], v[i]);
		}
		suf[layer][r-1] = v[r-1];
		for (int i = r-2; i >= l; i--) {
			suf[layer][i] = op(v[i], suf[layer][i+1]);
		}
	}
	
	inline void buildBetween(int layer, int lBound, int rBound, int betweenOffs) {
		int bSzLog = (layers[layer]+1) >> 1;
		int bCntLog = layers[layer] >> 1;
		int bSz = 1 << bSzLog;
		int bCnt = (rBound - lBound + bSz - 1) >> bSzLog;
		for (int i = 0; i < bCnt; i++) {
			SqrtTreeItem ans;
			for (int j = i; j < bCnt; j++) {
				SqrtTreeItem add = suf[layer][lBound + (j << bSzLog)];
				ans = (i == j) ? add : op(ans, add);
				between[layer-1][betweenOffs + lBound + (i << bCntLog) + j] = ans;
			}
		}
	}
	
	inline void buildBetweenZero() {
		int bSzLog = (lg+1) >> 1;
		for (int i = 0; i < indexSz; i++) {
			v[n+i] = suf[0][i << bSzLog];
		}
		build(1, n, n + indexSz, (1 << lg) - n);
	}
	
	inline void updateBetweenZero(int bid) {
		int bSzLog = (lg+1) >> 1;
		v[n+bid] = suf[0][bid << bSzLog];
		update(1, n, n + indexSz, (1 << lg) - n, n+bid);
	}
	
	void build(int layer, int lBound, int rBound, int betweenOffs) {
		if (layer >= (int)layers.size()) {
			return;
		}
		int bSz = 1 << ((layers[layer]+1) >> 1);
		for (int l = lBound; l < rBound; l += bSz) {
			int r = min(l + bSz, rBound);
			buildBlock(layer, l, r);
			build(layer+1, l, r, betweenOffs);
		}
		if (layer == 0) {
			buildBetweenZero();
		} else {
			buildBetween(layer, lBound, rBound, betweenOffs);
		}
	}
	
	void update(int layer, int lBound, int rBound, int betweenOffs, int x) {
		if (layer >= (int)layers.size()) {
			return;
		}
		int bSzLog = (layers[layer]+1) >> 1;
		int bSz = 1 << bSzLog;
		int blockIdx = (x - lBound) >> bSzLog;
		int l = lBound + (blockIdx << bSzLog);
		int r = min(l + bSz, rBound);
		buildBlock(layer, l, r);
		if (layer == 0) {
			updateBetweenZero(blockIdx);
		} else {
			buildBetween(layer, lBound, rBound, betweenOffs);
		}
		update(layer+1, l, r, betweenOffs, x);
	}
	
	inline SqrtTreeItem query(int l, int r, int betweenOffs, int base) {
		if (l == r) {
			return v[l];
		}
		if (l + 1 == r) {
			return op(v[l], v[r]);
		}
		int layer = onLayer[clz[(l - base) ^ (r - base)]];
		int bSzLog = (layers[layer]+1) >> 1;
		int bCntLog = layers[layer] >> 1;
		int lBound = (((l - base) >> layers[layer]) << layers[layer]) + base;
		int lBlock = ((l - lBound) >> bSzLog) + 1;
		int rBlock = ((r - lBound) >> bSzLog) - 1;
		SqrtTreeItem ans = suf[layer][l];
		if (lBlock <= rBlock) {
			SqrtTreeItem add = (layer == 0) ? (
				query(n + lBlock, n + rBlock, (1 << lg) - n, n)
			) : (
				between[layer-1][betweenOffs + lBound + (lBlock << bCntLog) + rBlock]
			);
			ans = op(ans, add);
		}
		ans = op(ans, pref[layer][r]);
		return ans;
	}
public:
	inline SqrtTreeItem query(int l, int r) {
		return query(l, r, 0, 0);
	}
	
	inline void update(int x, const SqrtTreeItem &item) {
		v[x] = item;
		update(0, 0, n, 0, x);
	}
	
	SqrtTree(const vector<SqrtTreeItem>& a)
		: n((int)a.size()), lg(log2Up(n)), v(a), clz(1 << lg), onLayer(lg+1) {
		clz[0] = 0;
		for (int i = 1; i < (int)clz.size(); i++) {
			clz[i] = clz[i >> 1] + 1;
		}
		int tlg = lg;
		while (tlg > 1) {
			onLayer[tlg] = (int)layers.size();
			layers.push_back(tlg);
			tlg = (tlg+1) >> 1;
		}
		for (int i = lg-1; i >= 0; i--) {
			onLayer[i] = max(onLayer[i], onLayer[i+1]);
		}
		int betweenLayers = max(0, (int)layers.size() - 1);
		int bSzLog = (lg+1) >> 1;
		int bSz = 1 << bSzLog;
		indexSz = (n + bSz - 1) >> bSzLog;
		v.resize(n + indexSz);
		pref.assign(layers.size(), vector<SqrtTreeItem>(n + indexSz));
		suf.assign(layers.size(), vector<SqrtTreeItem>(n + indexSz));
		between.assign(betweenLayers, vector<SqrtTreeItem>((1 << lg) + bSz));
		build(0, 0, n, 0);
	}
};

```

## Bài tập (Problems) {: #problems}

[CodeChef - SEGPROD](https://www.codechef.com/NOV17/problems/SEGPROD)
