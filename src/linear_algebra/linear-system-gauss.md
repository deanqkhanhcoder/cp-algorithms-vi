---
tags:
  - Translated
e_maxx_link: linear_systems_gauss
---

# Phương pháp Gauss để giải hệ phương trình tuyến tính (Gauss method for solving system of linear equations) {: #gauss-method-for-solving-system-of-linear-equations}

Cho một hệ gồm $n$ phương trình đại số tuyến tính (System of Linear Algebraic Equations - SLAE) với $m$ ẩn số. Bạn được yêu cầu giải hệ phương trình: xác định xem nó không có nghiệm, có đúng một nghiệm hay có vô số nghiệm. Và trong trường hợp nó có ít nhất một nghiệm, hãy tìm bất kỳ nghiệm nào trong số đó.

Một cách hình thức, bài toán được phát biểu như sau: giải hệ phương trình:

$$\begin{align}
a_{11} x_1 + a_{12} x_2 + &\dots + a_{1m} x_m = b_1 \\
a_{21} x_1 + a_{22} x_2 + &\dots + a_{2m} x_m = b_2\\
&\vdots \\
a_{n1} x_1 + a_{n2} x_2 + &\dots + a_{nm} x_m = b_n
\end{align}$$

trong đó các hệ số $a_{ij}$ (với $i$ từ 1 đến $n$, $j$ từ 1 đến $m$) và $b_i$ ($i$ từ 1 đến $n$) đã biết và các biến số $x_i$ ($i$ từ 1 đến $m$) là ẩn số.

Bài toán này cũng có biểu diễn ma trận đơn giản:

$$Ax = b,$$

trong đó $A$ là ma trận kích thước $n \times m$ của các hệ số $a_{ij}$ và $b$ là vectơ cột kích thước $n$.

Cần lưu ý rằng phương pháp được trình bày trong bài viết này cũng có thể được sử dụng để giải phương trình đồng dư modulo p bất kỳ, tức là:

$$\begin{align}
a_{11} x_1 + a_{12} x_2 + &\dots + a_{1m} x_m \equiv b_1 \pmod p \\
a_{21} x_1 + a_{22} x_2 + &\dots + a_{2m} x_m \equiv b_2 \pmod p \\
&\vdots \\
a_{n1} x_1 + a_{n2} x_2 + &\dots + a_{nm} x_m \equiv b_n \pmod p
\end{align}$$

## Gauss

Nói một cách chính xác, phương pháp được mô tả dưới đây nên được gọi là "Gauss-Jordan", hoặc khử Gauss-Jordan (Gauss-Jordan elimination), bởi vì nó là một biến thể của phương pháp Gauss, được mô tả bởi Jordan vào năm 1887.

## Tổng quan (Overview) {: #overview}

Thuật toán là một sự `khử tuần tự` (`sequential elimination`) các biến trong mỗi phương trình, cho đến khi mỗi phương trình chỉ còn lại một biến. Nếu $n = m$, bạn có thể nghĩ về nó như là biến đổi ma trận $A$ thành ma trận đơn vị, và giải phương trình trong trường hợp hiển nhiên này, trong đó nghiệm là duy nhất và bằng hệ số $b_i$.

Khử Gaussian dựa trên hai phép biến đổi đơn giản:

* Có thể hoán đổi hai phương trình
* Bất kỳ phương trình nào cũng có thể được thay thế bằng tổ hợp tuyến tính của hàng đó (với hệ số khác không), và một số hàng khác (với các hệ số tùy ý).

Trong bước đầu tiên, thuật toán Gauss-Jordan chia hàng đầu tiên cho $a_{11}$. Sau đó, thuật toán cộng hàng đầu tiên vào các hàng còn lại sao cho các hệ số trong cột đầu tiên trở thành tất cả các số không. Để đạt được điều này, trên hàng thứ $i$, chúng ta phải thêm hàng đầu tiên nhân với $- a_{i1}$. Lưu ý rằng, thao tác này cũng phải được thực hiện trên vectơ $b$. Theo một nghĩa nào đó, nó hoạt động như thể vectơ $b$ là cột thứ $m+1$ của ma trận $A$.

Kết quả là, sau bước đầu tiên, cột đầu tiên của ma trận $A$ sẽ bao gồm $1$ trên hàng đầu tiên và $0$ ở các hàng khác.

Tương tự, chúng ta thực hiện bước thứ hai của thuật toán, trong đó chúng ta xem xét cột thứ hai của hàng thứ hai. Đầu tiên, hàng được chia cho $a_{22}$, sau đó nó được trừ đi từ các hàng khác sao cho tất cả cột thứ hai trở thành $0$ (ngoại trừ hàng thứ hai).

Chúng ta tiếp tục quá trình này cho tất cả các cột của ma trận $A$. Nếu $n = m$, thì $A$ sẽ trở thành ma trận đơn vị.

## Tìm kiếm phần tử trụ (Search for the pivoting element) {: #search-for-the-pivoting-element}

Lược đồ được mô tả đã bỏ qua nhiều chi tiết. Tại bước thứ $i$, nếu $a_{ii}$ bằng không, chúng ta không thể áp dụng trực tiếp phương pháp được mô tả. Thay vào đó, trước tiên chúng ta phải `chọn một hàng trụ` (`select a pivoting row`): tìm một hàng của ma trận mà cột thứ $i$ khác không, sau đó tráo đổi hai hàng.

Lưu ý rằng, ở đây chúng ta tráo đổi các hàng nhưng không tráo đổi các cột. Điều này là do nếu bạn tráo đổi các cột, thì khi bạn tìm thấy một nghiệm, bạn phải nhớ tráo đổi lại đúng vị trí. Do đó, việc tráo đổi các hàng dễ thực hiện hơn nhiều.

Trong nhiều triển khai, khi $a_{ii} \neq 0$, bạn có thể thấy mọi người vẫn tráo đổi hàng thứ $i$ với một số hàng trụ, sử dụng một số phỏng đoán (heuristics) chẳng hạn như chọn hàng trụ có giá trị tuyệt đối lớn nhất của $a_{ji}$. Phỏng đoán này được sử dụng để giảm phạm vi giá trị của ma trận trong các bước sau. Nếu không có phỏng đoán này, ngay cả đối với các ma trận có kích thước khoảng $20$, sai số sẽ quá lớn và có thể gây tràn số đối với các loại dữ liệu dấu phẩy động của C++.

## Các trường hợp suy biến (Degenerate cases) {: #degenerate-cases}

Trong trường hợp $m = n$ và hệ thống không suy biến (tức là nó có định thức khác không và có nghiệm duy nhất), thuật toán được mô tả ở trên sẽ biến đổi $A$ thành ma trận đơn vị.

Bây giờ chúng ta xem xét `trường hợp tổng quát` (`general case`), trong đó $n$ và $m$ không nhất thiết phải bằng nhau và hệ thống có thể bị suy biến. Trong những trường hợp này, phần tử trụ trong bước thứ $i$ có thể không tìm thấy. Điều này có nghĩa là trên cột thứ $i$, bắt đầu từ dòng hiện tại, tất cả đều chứa số không. Trong trường hợp này, hoặc không có giá trị nào của biến $x_i$ (nghĩa là SLAE không có nghiệm), hoặc $x_i$ là một biến độc lập và có thể nhận giá trị tùy ý. Khi triển khai Gauss-Jordan, bạn nên tiếp tục công việc cho các biến tiếp theo và chỉ cần bỏ qua cột thứ $i$ (điều này tương đương với việc xóa cột thứ $i$ của ma trận).

Vì vậy, một số biến trong quá trình có thể được coi là độc lập. Khi số lượng biến, $m$ lớn hơn số lượng phương trình, $n$, thì ít nhất $m - n$ biến độc lập sẽ được tìm thấy.

Nhìn chung, nếu bạn tìm thấy ít nhất một biến độc lập, nó có thể nhận bất kỳ giá trị tùy ý nào, trong khi các biến khác (phụ thuộc) được biểu thị qua nó. Điều này có nghĩa là khi chúng ta làm việc trong trường số thực, hệ thống có khả năng có vô số nghiệm. Nhưng bạn nên nhớ rằng khi có các biến độc lập, SLAE hoàn toàn có thể không có nghiệm. Điều này xảy ra khi các phương trình chưa được xử lý còn lại có ít nhất một hằng số khác không. Bạn có thể kiểm tra điều này bằng cách gán số không cho tất cả các biến độc lập, tính toán các biến khác và sau đó thay vào SLAE ban đầu để kiểm tra xem chúng có thỏa mãn nó hay không.

## Cài đặt (Implementation) {: #implementation}

Sau đây là một triển khai của Gauss-Jordan. Việc chọn hàng trụ được thực hiện với phỏng đoán: chọn giá trị lớn nhất trong cột hiện tại.

Đầu vào cho hàm `gauss` là ma trận hệ thống $a$. Cột cuối cùng của ma trận này là vectơ $b$.

Hàm trả về số lượng nghiệm của hệ thống $(0, 1,\textrm{hoặc } \infty)$. Nếu tồn tại ít nhất một nghiệm, thì nó được trả về trong vectơ $ans$.
```cpp title="gauss"
const double EPS = 1e-9;
const int INF = 2; // nó thực sự không cần phải là vô cùng hoặc một số lớn

int gauss (vector < vector<double> > a, vector<double> & ans) {
	int n = (int) a.size();
	int m = (int) a[0].size() - 1;

	vector<int> where (m, -1);
	for (int col=0, row=0; col<m && row<n; ++col) {
		int sel = row;
		for (int i=row; i<n; ++i)
			if (abs (a[i][col]) > abs (a[sel][col]))
				sel = i;
		if (abs (a[sel][col]) < EPS)
			continue;
		for (int i=col; i<=m; ++i)
			swap (a[sel][i], a[row][i]);
		where[col] = row;

		for (int i=0; i<n; ++i)
			if (i != row) {
				double c = a[i][col] / a[row][col];
				for (int j=col; j<=m; ++j)
					a[i][j] -= a[row][j] * c;
			}
		++row;
	}

	ans.assign (m, 0);
	for (int i=0; i<m; ++i)
		if (where[i] != -1)
			ans[i] = a[where[i]][m] / a[where[i]][i];
	for (int i=0; i<n; ++i) {
		double sum = 0;
		for (int j=0; j<m; ++j)
			sum += ans[j] * a[i][j];
		if (abs (sum - a[i][m]) > EPS)
			return 0;
	}

	for (int i=0; i<m; ++i)
		if (where[i] == -1)
			return INF;
	return 1;
}
```

Ghi chú triển khai:

* Hàm sử dụng hai con trỏ - cột hiện tại $col$ và hàng hiện tại $row$.
* Đối với mỗi biến $x_i$, giá trị $where(i)$ là dòng mà cột này không bằng không. Vectơ này là cần thiết vì một số biến có thể độc lập.
* Trong triển khai này, dòng thứ $i$ hiện tại không chia cho $a_{ii}$ như mô tả ở trên, vì vậy cuối cùng ma trận không phải là ma trận đơn vị (mặc dù rõ ràng việc chia dòng thứ $i$ có thể giúp giảm sai số).
* Sau khi tìm thấy một nghiệm, nó được chèn lại vào ma trận - để kiểm tra xem hệ thống có ít nhất một nghiệm hay không. Nếu nghiệm thử nghiệm thành công, thì hàm trả về 1 hoặc $\inf$, tùy thuộc vào việc có ít nhất một biến độc lập hay không.

## Độ phức tạp (Complexity) {: #complexity}

Bây giờ chúng ta nên ước tính độ phức tạp của thuật toán này. Thuật toán bao gồm $m$ giai đoạn, trong mỗi giai đoạn:

* Tìm kiếm và tráo đổi hàng trụ. Việc này mất $O(n + m)$ khi sử dụng phỏng đoán được đề cập ở trên.
* Nếu phần tử trụ trong cột hiện tại được tìm thấy - thì chúng ta phải thêm phương trình này vào tất cả các phương trình khác, mất thời gian $O(nm)$.

Vì vậy, độ phức tạp cuối cùng của thuật toán là $O(\min (n, m) . nm)$.
Trong trường hợp $n = m$, độ phức tạp đơn giản là $O(n^3)$.

Lưu ý rằng khi SLAE không nằm trên số thực, mà ở modulo 2, thì hệ thống có thể được giải nhanh hơn nhiều, được mô tả bên dưới.

## Tăng tốc thuật toán (Acceleration of the algorithm) {: #acceleration-of-the-algorithm}

Việc triển khai trước đó có thể được tăng tốc gấp hai lần, bằng cách chia thuật toán thành hai giai đoạn: thuận (forward) và nghịch (reverse):

* Giai đoạn thuận: Tương tự như triển khai trước, nhưng hàng hiện tại chỉ được thêm vào các hàng sau nó. Kết quả là, chúng ta thu được một ma trận tam giác thay vì ma trận đường chéo.
* Giai đoạn nghịch: Khi ma trận là tam giác, đầu tiên chúng ta tính giá trị của biến cuối cùng. Sau đó thay giá trị này để tìm giá trị của biến tiếp theo. Sau đó thay hai giá trị này để tìm các biến tiếp theo...

Giai đoạn nghịch chỉ mất $O(nm)$, nhanh hơn nhiều so với giai đoạn thuận. Trong giai đoạn thuận, chúng ta giảm một nửa số lượng phép toán, do đó giảm thời gian chạy của triển khai.

## Giải SLAE mô-đun (Solving modular SLAE) {: #solving-modular-slae}

Để giải SLAE trong một mô-đun nào đó, chúng ta vẫn có thể sử dụng thuật toán được mô tả. Tuy nhiên, trong trường hợp mô-đun bằng 2, chúng ta có thể thực hiện khử Gauss-Jordan hiệu quả hơn nhiều bằng cách sử dụng các phép toán bit và kiểu dữ liệu bitset của C++:

```cpp
int gauss (vector < bitset<N> > a, int n, int m, bitset<N> & ans) {
	vector<int> where (m, -1);
	for (int col=0, row=0; col<m && row<n; ++col) {
		for (int i=row; i<n; ++i)
			if (a[i][col]) {
				swap (a[i], a[row]);
				break;
			}
		if (! a[row][col])
			continue;
		where[col] = row;

		for (int i=0; i<n; ++i)
			if (i != row && a[i][col])
				a[i] ^= a[row];
		++row;
	}
        // Phần còn lại của việc triển khai tương tự như trên
}
```

Vì chúng ta sử dụng nén bit, việc triển khai không chỉ ngắn hơn mà còn nhanh hơn 32 lần.

## Một chút lưu ý về các phỏng đoán khác nhau của việc chọn hàng trụ (A little note about different heuristics of choosing pivoting row) {: #heuristics}

Không có quy tắc chung cho những phỏng đoán nào để sử dụng.

Các phỏng đoán được sử dụng trong triển khai trước hoạt động khá tốt trong thực tế. Nó cũng cho ra kết quả gần như giống hệt như "trụ đầy đủ" ("full pivoting") - trong đó hàng trụ được tìm kiếm giữa tất cả các phần tử của ma trận con (từ hàng hiện tại và cột hiện tại).

Tuy nhiên, bạn nên lưu ý rằng cả hai phỏng đoán đều phụ thuộc vào mức độ các phương trình ban đầu được thu phóng. Ví dụ, nếu một trong các phương trình được nhân với $10^6$, thì phương trình này gần như chắc chắn được chọn làm trụ trong bước đầu tiên. Điều này có vẻ khá lạ, vì vậy có vẻ hợp lý khi chuyển sang một phỏng đoán phức tạp hơn, được gọi là `trụ ngầm định` (`implicit pivoting`).

Trụ ngầm định so sánh các phần tử như thể cả hai dòng đều được chuẩn hóa, sao cho phần tử lớn nhất sẽ là đơn vị. Để thực hiện kỹ thuật này, người ta cần duy trì giá trị lớn nhất trong mỗi hàng (hoặc duy trì từng dòng sao cho giá trị lớn nhất là đơn vị, nhưng điều này có thể dẫn đến sự gia tăng sai số tích lũy).

## Cải thiện nghiệm (Improve the solution) {: #improve-the-solution}

Bất chấp các phỏng đoán khác nhau, thuật toán Gauss-Jordan vẫn có thể dẫn đến sai số lớn trong các ma trận đặc biệt thậm chí có kích thước $50 - 100$.

Do đó, giải pháp Gauss-Jordan kết quả đôi khi phải được cải thiện bằng cách áp dụng một phương pháp số đơn giản - ví dụ, phương pháp lặp đơn.

Do đó, giải pháp biến thành hai bước: Đầu tiên, thuật toán Gauss-Jordan được áp dụng, và sau đó một phương pháp số lấy nghiệm ban đầu làm nghiệm trong bước đầu tiên.

## Bài tập (Practice Problems) {: #practice-problems}
* [Spoj - Xor Maximization](http://www.spoj.com/problems/XMAX/)
* [Codechef - Knight Moving](https://www.codechef.com/SEP12/problems/KNGHTMOV)
* [Lightoj - Graph Coloring](http://lightoj.com/volume_showproblem.php?problem=1279)
* [UVA 12910 - Snakes and Ladders](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=4775)
* [TIMUS1042 Central Heating](http://acm.timus.ru/problem.aspx?space=1&num=1042)
* [TIMUS1766 Humpty Dumpty](http://acm.timus.ru/problem.aspx?space=1&num=1766)
* [TIMUS1266 Kirchhoff's Law](http://acm.timus.ru/problem.aspx?space=1&num=1266)
* [Codeforces - No game no life](https://codeforces.com/problemset/problem/1411/G)
