---
tags:
  - Translated
e_maxx_link: assignment_hungary
---

# Thuật toán Hungary giải bài toán phân công (Hungarian algorithm for solving the assignment problem) {: #hungarian-algorithm-for-solving-the-assignment-problem}

## Phát biểu bài toán phân công (Statement of the assignment problem) {: #statement-of-the-assignment-problem}

Có một số cách phát biểu tiêu chuẩn cho bài toán phân công (tất cả về cơ bản đều tương đương). Dưới đây là một số trong số đó:

- Có $n$ công việc và $n$ công nhân. Mỗi công nhân chỉ định số tiền họ mong đợi cho một công việc cụ thể. Mỗi công nhân chỉ có thể được giao một công việc. Mục tiêu là phân công công việc cho công nhân theo cách giảm thiểu tổng chi phí.

- Cho một ma trận $A$ kích thước $n \times n$, nhiệm vụ là chọn một số từ mỗi hàng sao cho mỗi cột có chính xác một số được chọn, và tổng của các số được chọn là nhỏ nhất.

- Cho một ma trận $A$ kích thước $n \times n$, nhiệm vụ là tìm một hoán vị $p$ có độ dài $n$ sao cho giá trị $\sum A[i]\left[p[i]\right]$ là nhỏ nhất.

- Xem xét một đồ thị hai phía đầy đủ với $n$ đỉnh mỗi phần, trong đó mỗi cạnh được gán một trọng số. Mục tiêu là tìm một cặp ghép hoàn hảo có tổng trọng số nhỏ nhất.

Điều quan trọng cần lưu ý là tất cả các tình huống trên đều là các bài toán "**vuông**", nghĩa là cả hai kích thước luôn bằng $n$. Trong thực tế, các công thức "**chữ nhật**" tương tự thường gặp, trong đó $n$ không bằng $m$, và nhiệm vụ là chọn $\min(n,m)$ phần tử. Tuy nhiên, có thể thấy rằng một bài toán "chữ nhật" luôn có thể được chuyển đổi thành bài toán "vuông" bằng cách thêm các hàng hoặc cột có giá trị 0 hoặc vô cùng tương ứng.

Chúng tôi cũng lưu ý rằng bằng cách tương tự với việc tìm kiếm giải pháp **nhỏ nhất**, người ta cũng có thể đặt ra bài toán tìm giải pháp **lớn nhất**. Tuy nhiên, hai bài toán này tương đương với nhau: chỉ cần nhân tất cả các trọng số với $-1$.

## Thuật toán Hungary (Hungarian algorithm) {: #hungarian-algorithm}

### Tham khảo lịch sử (Historical reference) {: #historical-reference}

Thuật toán được phát triển và xuất bản bởi Harold **Kuhn** vào năm 1955. Bản thân Kuhn đã đặt tên cho nó là "Hungary" vì nó dựa trên công trình trước đó của các nhà toán học người Hungary Dénes Kőnig và Jenő Egerváry.
Năm 1957, James **Munkres** đã chỉ ra rằng thuật toán này chạy trong thời gian đa thức (nghiêm ngặt), độc lập với chi phí.
Do đó, trong văn học, thuật toán này được biết đến không chỉ là "Hungary", mà còn là "thuật toán Kuhn-Mankres" hoặc "thuật toán Mankres".
Tuy nhiên, gần đây người ta phát hiện ra vào năm 2006 rằng cùng một thuật toán này đã được phát minh ra **một thế kỷ trước Kuhn** bởi nhà toán học người Đức Carl Gustav **Jacobi**. Công trình của ông, _Về nghiên cứu thứ tự của một hệ phương trình vi phân thường tùy ý_, được xuất bản sau khi ông qua đời vào năm 1890, có chứa, trong số các phát hiện khác, một thuật toán đa thức để giải quyết bài toán phân công. Thật không may, vì ấn phẩm bằng tiếng Latinh, nên nó đã không được các nhà toán học chú ý.

Cũng cần lưu ý rằng thuật toán ban đầu của Kuhn có độ phức tạp tiệm cận là $\mathcal{O}(n^4)$, và chỉ sau đó Jack **Edmonds** và Richard **Karp** (và một cách độc lập **Tomizawa**) đã chỉ ra cách cải thiện nó thành độ phức tạp tiệm cận là $\mathcal{O}(n^3)$.

### Thuật toán $\mathcal{O}(n^4)$ (The $\mathcal{O}(n^4)$ algorithm) {: #the-o-n-4-algorithm}

Để tránh sự mơ hồ, chúng tôi lưu ý ngay rằng chúng tôi chủ yếu quan tâm đến bài toán phân công trong một công thức ma trận (tức là, cho một ma trận $A$, bạn cần chọn $n$ ô từ nó nằm trong các hàng và cột khác nhau). Chúng tôi lập chỉ mục mảng bắt đầu bằng $1$, nghĩa là, ví dụ, ma trận $A$ có các chỉ số $A[1 \dots n][1 \dots n]$.

Chúng ta cũng sẽ giả sử rằng tất cả các số trong ma trận A đều **không âm** (nếu không phải vậy, bạn luôn có thể làm cho ma trận không âm bằng cách thêm một hằng số vào tất cả các số).

Hãy gọi một **thế năng** (potential) là hai mảng số tùy ý $u[1 \ldots n]$ và $v[1 \ldots n]$, sao cho điều kiện sau được thỏa mãn:

$$u[i]+v[j]\leq A[i][j],\quad i=1\dots n,\ j=1\dots n$$

(Như bạn có thể thấy, $u[i]$ tương ứng với hàng thứ $i$, và $v[j]$ tương ứng với cột thứ $j$ của ma trận).

Hãy gọi **giá trị $f$ của thế năng** là tổng các phần tử của nó:

$$f=\sum_{i=1}^{n} u[i] + \sum_{j=1}^{n} v[j].$$

Một mặt, dễ thấy rằng chi phí của giải pháp mong muốn $sol$ **không nhỏ hơn** giá trị của bất kỳ thế năng nào.

!!! info ""

    **Bổ đề.** $sol\geq f.$

??? info "Chứng minh"

    Giải pháp mong muốn của bài toán bao gồm $n$ ô của ma trận $A$, vì vậy $u[i]+v[j]\leq A[i][j]$ cho mỗi ô trong số đó. Vì tất cả các phần tử trong $sol$ nằm trong các hàng và cột khác nhau, cộng các bất đẳng thức này trên tất cả các $A[i][j]$ đã chọn, bạn nhận được $f$ ở phía bên trái của bất đẳng thức, và $sol$ ở phía bên phải.

Mặt khác, hóa ra luôn có một giải pháp và một thế năng biến bất đẳng thức này thành **đẳng thức**. Thuật toán Hungary được mô tả dưới đây sẽ là một bằng chứng xây dựng cho thực tế này. Bây giờ, hãy chỉ chú ý đến thực tế là nếu bất kỳ giải pháp nào có chi phí bằng với bất kỳ thế năng nào, thì giải pháp này là **tối ưu**.

Hãy cố định một thế năng nào đó. Hãy gọi một cạnh $(i,j)$ là **cứng** (rigid) nếu $u[i]+v[j]=A[i][j].$

Nhớ lại một công thức thay thế của bài toán phân công, sử dụng đồ thị hai phía. Ký hiệu $H$ là một đồ thị hai phía chỉ bao gồm các cạnh cứng. Thuật toán Hungary sẽ duy trì, cho thế năng hiện tại, **cặp ghép có số lượng cạnh tối đa** $M$ của đồ thị $H$. Ngay khi $M$ chứa $n$ cạnh, thì giải pháp cho bài toán sẽ chỉ là $M$ (rốt cuộc, nó sẽ là một giải pháp có chi phí trùng với giá trị của một thế năng).

Hãy tiến hành trực tiếp đến **mô tả thuật toán**.

**Bước 1.** Ban đầu, thế năng được giả định là bằng 0 ($u[i]=v[i]=0$ cho tất cả $i$), và cặp ghép $M$ được giả định là rỗng.

**Bước 2.** Hơn nữa, tại mỗi bước của thuật toán, chúng ta cố gắng, mà không thay đổi thế năng, để tăng lực lượng của cặp ghép hiện tại $M$ lên một (nhớ lại rằng cặp ghép được tìm kiếm trong đồ thị các cạnh cứng $H$). Để làm điều này, [Thuật toán Kuhn thông thường để tìm cặp ghép cực đại trong đồ thị hai phía](kuhn-maximum-bipartite-matching.md) được sử dụng. Hãy nhớ lại thuật toán ở đây.
Tất cả các cạnh của cặp ghép $M$ được định hướng theo hướng từ phần bên phải sang phần bên trái, và tất cả các cạnh khác của đồ thị $H$ được định hướng theo hướng ngược lại.

Nhớ lại (từ thuật ngữ tìm kiếm cặp ghép) rằng một đỉnh được gọi là bão hòa nếu một cạnh của cặp ghép hiện tại kề với nó. Một đỉnh không kề với bất kỳ cạnh nào của cặp ghép hiện tại được gọi là chưa bão hòa. Một đường đi có độ dài lẻ, trong đó cạnh đầu tiên không thuộc về cặp ghép, và đối với tất cả các cạnh tiếp theo có sự thay thế thuộc về cặp ghép (thuộc / không thuộc) - được gọi là đường tăng.
Từ tất cả các đỉnh chưa bão hòa trong phần bên trái, một duyệt [theo chiều sâu](depth-first-search.md) hoặc [theo chiều rộng](breadth-first-search.md) được bắt đầu. Nếu, kết quả của việc tìm kiếm, có thể đến được một đỉnh chưa bão hòa của phần bên phải, chúng ta đã tìm thấy một đường tăng từ phần bên trái sang phần bên phải. Nếu chúng ta bao gồm các cạnh lẻ của đường đi và loại bỏ các cạnh chẵn trong cặp ghép (tức là bao gồm cạnh đầu tiên trong cặp ghép, loại trừ cạnh thứ hai, bao gồm cạnh thứ ba, v.v.), thì chúng ta sẽ tăng lực lượng cặp ghép lên một.

Nếu không có đường tăng, thì cặp ghép hiện tại $M$ là cực đại trong đồ thị $H$.

**Bước 3.** Nếu ở bước hiện tại, không thể tăng lực lượng của cặp ghép hiện tại, thì việc tính toán lại thế năng được thực hiện theo cách sao cho, ở các bước tiếp theo, sẽ có nhiều cơ hội hơn để tăng cặp ghép.

Ký hiệu $Z_1$ là tập hợp các đỉnh của phần bên trái đã được thăm trong lần duyệt cuối cùng của thuật toán Kuhn, và qua $Z_2$ tập hợp các đỉnh đã được thăm của phần bên phải.

Hãy tính giá trị $\Delta$:

$$\Delta = \min_{i\in Z_1,\ j\notin Z_2} A[i][j]-u[i]-v[j].$$

!!! info ""

     **Bổ đề.** $\Delta > 0.$

??? info "Chứng minh"

    Giả sử $\Delta=0$. Khi đó tồn tại một cạnh cứng $(i,j)$ với $i\in Z_1$ và $j\notin Z_2$. Suy ra rằng cạnh $(i,j)$ phải được định hướng từ phần bên phải sang phần bên trái, tức là $(i,j)$ phải được bao gồm trong cặp ghép $M$. Tuy nhiên, điều này là không thể, bởi vì chúng ta không thể đến được đỉnh bão hòa $i$ ngoại trừ bằng cách đi dọc theo cạnh từ j đến i. Vì vậy $\Delta > 0$.

Bây giờ hãy **tính toán lại thế năng** theo cách này:

- cho tất cả các đỉnh $i\in Z_1$, thực hiện $u[i] \gets u[i]+\Delta$,

- cho tất cả các đỉnh $j\in Z_2$, thực hiện $v[j] \gets v[j]-\Delta$.

!!! info ""

    **Bổ đề.** Thế năng kết quả vẫn là một thế năng chính xác.

??? info "Chứng minh"

    Chúng ta sẽ chỉ ra rằng, sau khi tính toán lại, $u[i]+v[j]\leq A[i][j]$ cho tất cả $i,j$. Đối với tất cả các phần tử của $A$ với $i\in Z_1$ và $j\in Z_2$, tổng $u[i]+v[j]$ không thay đổi, vì vậy bất đẳng thức vẫn đúng. Đối với tất cả các phần tử với $i\notin Z_1$ và $j\in Z_2$, tổng $u[i]+v[j]$ giảm đi $\Delta$, vì vậy bất đẳng thức vẫn đúng. Đối với các phần tử khác có $i\in Z_1$ và $j\notin Z_2$, tổng tăng lên, nhưng bất đẳng thức vẫn được bảo tồn, vì giá trị $\Delta$, theo định nghĩa, là mức tăng tối đa không làm thay đổi bất đẳng thức.

!!! info ""

    **Bổ đề.** Cặp ghép cũ $M$ của các cạnh cứng là hợp lệ, tức là tất cả các cạnh của cặp ghép sẽ vẫn cứng.

??? info "Chứng minh"

    Để một số cạnh cứng $(i,j)$ ngừng cứng do thay đổi thế năng, cần phải có đẳng thức $u[i] + v[j] = A[i][j]$ chuyển thành bất đẳng thức $u[i] + v[j] < A[i][j]$. Tuy nhiên, điều này chỉ có thể xảy ra khi $i \notin Z_1$ và $j \in Z_2$. Nhưng $i \notin Z_1$ ngụ ý rằng cạnh $(i,j)$ không thể là một cạnh cặp ghép.

!!! info ""

    **Bổ đề.** Sau mỗi lần tính toán lại thế năng, số lượng đỉnh có thể đến được bằng cách duyệt, tức là $|Z_1|+|Z_2|$, tăng nghiêm ngặt.

??? info "Chứng minh"

    Trước tiên, lưu ý rằng bất kỳ đỉnh nào có thể đến được trước khi tính toán lại, vẫn có thể đến được. Thật vậy, nếu một số đỉnh có thể đến được, thì có một số đường đi từ các đỉnh có thể đến được đến nó, bắt đầu từ đỉnh chưa bão hòa của phần bên trái; vì đối với các cạnh có dạng $(i,j),\ i\in Z_1,\ j\in Z_2$ tổng $u[i]+v[j]$ không thay đổi, toàn bộ đường đi này sẽ được bảo tồn sau khi thay đổi thế năng.
    Thứ hai, chúng ta chỉ ra rằng sau một lần tính toán lại, ít nhất một đỉnh mới sẽ có thể đến được. Điều này tuân theo định nghĩa của $\Delta$: cạnh $(i,j)$ mà $\Delta$ đề cập đến sẽ trở nên cứng, vì vậy đỉnh $j$ sẽ có thể đến được từ đỉnh $i$.

Do bổ đề cuối cùng, **không quá $n$ lần tính toán lại thế năng có thể xảy ra** trước khi tìm thấy một đường tăng và lực lượng cặp ghép của $M$ được tăng lên.
Do đó, sớm hay muộn, một thế năng tương ứng với một cặp ghép hoàn hảo $M^*$ sẽ được tìm thấy, và $M^*$ sẽ là câu trả lời cho bài toán.
Nếu chúng ta nói về độ phức tạp của thuật toán, thì đó là $\mathcal{O}(n^4)$: tổng cộng sẽ có tối đa $n$ lần tăng cặp ghép, trước mỗi lần đó không quá $n$ lần tính toán lại thế năng, mỗi lần được thực hiện trong thời gian $\mathcal{O}(n^2)$.

Chúng tôi sẽ không đưa ra cài đặt cho thuật toán $\mathcal{O}(n^4)$ ở đây, vì nó sẽ không ngắn hơn cài đặt cho $\mathcal{O}(n^3)$, được mô tả bên dưới.

### Thuật toán $\mathcal{O}(n^3)$ (The $\mathcal{O}(n^3)$ algorithm) {: #the-o-n-3-algorithm}

Bây giờ hãy tìm hiểu cách cài đặt thuật toán tương tự trong $\mathcal{O}(n^3)$ (đối với các bài toán hình chữ nhật $n \times m$, $\mathcal{O}(n^2m)$).

Ý tưởng chính là **xem xét các hàng ma trận từng hàng một**, và không phải tất cả cùng một lúc. Do đó, thuật toán được mô tả ở trên sẽ có dạng sau:

1.  Xem xét hàng tiếp theo của ma trận $A$.

2.  Trong khi không có đường tăng bắt đầu trong hàng này, hãy tính toán lại thế năng.

3.  Ngay khi tìm thấy một đường tăng, hãy lan truyền cặp ghép dọc theo nó (do đó bao gồm cạnh cuối cùng trong cặp ghép), và khởi động lại từ bước 1 (để xem xét dòng tiếp theo).

Để đạt được độ phức tạp cần thiết, cần phải cài đặt các bước 2-3, được thực hiện cho mỗi hàng của ma trận, trong thời gian $\mathcal{O}(n^2)$ (đối với các bài toán hình chữ nhật trong $\mathcal{O}(nm)$).

Để làm điều này, hãy nhớ lại hai sự kiện đã được chứng minh ở trên:

- Với sự thay đổi về thế năng, các đỉnh có thể đến được bằng cách duyệt Kuhn sẽ vẫn có thể đến được.

- Tổng cộng, chỉ có $\mathcal{O}(n)$ lần tính toán lại thế năng có thể xảy ra trước khi tìm thấy một đường tăng.

Từ đây suy ra những **ý tưởng chính** này cho phép chúng ta đạt được độ phức tạp cần thiết:

- Để kiểm tra sự hiện diện của một đường tăng, không cần phải bắt đầu lại duyệt Kuhn sau mỗi lần tính toán lại thế năng. Thay vào đó, bạn có thể thực hiện duyệt Kuhn ở dạng **lặp**: sau mỗi lần tính toán lại thế năng, nhìn vào các cạnh cứng được thêm vào và, nếu đầu bên trái của chúng có thể đến được, hãy đánh dấu đầu bên phải của chúng cũng có thể đến được và tiếp tục duyệt từ chúng.

- Phát triển ý tưởng này hơn nữa, chúng ta có thể trình bày thuật toán như sau: ở mỗi bước của vòng lặp, thế năng được tính toán lại. Sau đó, một cột đã trở nên có thể đến được được xác định (cột này sẽ luôn tồn tại khi các đỉnh có thể đến được mới xuất hiện sau mỗi lần tính toán lại thế năng). Nếu cột chưa bão hòa, một chuỗi tăng được phát hiện. Ngược lại, nếu cột bão hòa, hàng ghép đôi cũng trở nên có thể đến được.

- Để tính toán lại nhanh thế năng (nhanh hơn phiên bản ngây thơ $\mathcal{O}(n^2)$), bạn cần duy trì các cực tiểu phụ trợ cho mỗi cột:

    <br><div style="text-align:center">$minv[j]=\min_{i\in Z_1} A[i][j]-u[i]-v[j].$</div><br>

    Dễ thấy rằng giá trị mong muốn $\Delta$ được biểu thị qua chúng như sau:

    <br><div style="text-align:center">$\Delta=\min_{j\notin Z_2} minv[j].$</div><br>

    Do đó, việc tìm $\Delta$ bây giờ có thể được thực hiện trong $\mathcal{O}(n)$.

    Cần cập nhật mảng $minv$ khi các hàng đã thăm mới xuất hiện. Điều này có thể được thực hiện trong $\mathcal{O}(n)$ cho hàng đã thêm (cộng dồn trên tất cả các hàng thành $\mathcal{O}(n^2)$). Cũng cần cập nhật mảng $minv$ khi tính toán lại thế năng, điều này cũng được thực hiện trong thời gian $\mathcal{O}(n)$ ($minv$ chỉ thay đổi đối với các cột chưa đến được: cụ thể, nó giảm đi $\Delta$).

Do đó, thuật toán có dạng sau: trong vòng lặp ngoài, chúng ta xem xét các hàng ma trận từng hàng một. Mỗi hàng được xử lý trong thời gian $\mathcal{O}(n^2)$, vì chỉ có $\mathcal{O}(n)$ lần tính toán lại thế năng có thể xảy ra (mỗi lần trong thời gian $\mathcal{O}(n)$), và mảng $minv$ được duy trì trong thời gian $\mathcal{O}(n^2)$; Thuật toán Kuhn sẽ hoạt động trong thời gian $\mathcal{O}(n^2)$ (vì nó được trình bày dưới dạng $\mathcal{O}(n)$ lần lặp, mỗi lần lặp thăm một cột mới).

Độ phức tạp kết quả là $\mathcal{O}(n^3)$ hoặc, nếu bài toán là hình chữ nhật, $\mathcal{O}(n^2m)$.

## Cài đặt thuật toán Hungary (Implementation of the Hungarian algorithm) {: #implementation-of-the-hungarian-algorithm}

Cài đặt dưới đây được phát triển bởi **Andrey Lopatin** vài năm trước. Nó được phân biệt bởi sự ngắn gọn đáng kinh ngạc: toàn bộ thuật toán bao gồm **30 dòng mã**.

Cài đặt tìm giải pháp cho ma trận chữ nhật $A[1\dots n][1\dots m]$, trong đó $n\leq m$. Ma trận dựa trên 1 thuận tiện và ngắn gọn mã: cài đặt này giới thiệu một hàng không giả và cột không giả, cho phép chúng ta viết nhiều chu trình ở dạng tổng quát, mà không cần kiểm tra thêm.

Các mảng $u[0 \ldots n]$ và $v[0 \ldots m]$ lưu trữ thế năng. Ban đầu, chúng được đặt bằng 0, điều này phù hợp với ma trận các hàng 0 (Lưu ý rằng đối với việc cài đặt này, việc ma trận $A$ có chứa số âm hay không là không quan trọng).

Mảng $p[0 \ldots m]$ chứa một cặp ghép: đối với mỗi cột $j = 1 \ldots m$, nó lưu trữ số $p[j]$ của hàng được chọn (hoặc $0$ nếu chưa có gì được chọn). Để thuận tiện cho việc cài đặt, $p[0]$ được giả định là bằng số của hàng hiện tại.

Mảng $minv[1 \ldots m]$ chứa, đối với mỗi cột $j$, các cực tiểu phụ trợ cần thiết để tính toán lại nhanh thế năng, như được mô tả ở trên.

Mảng $way[1 \ldots m]$ chứa thông tin về nơi các cực tiểu này đạt được để sau này chúng ta có thể khôi phục đường tăng. Lưu ý rằng, để khôi phục đường đi, chỉ cần lưu trữ các giá trị cột là đủ, vì số hàng có thể được lấy từ cặp ghép (tức là từ mảng $p$). Do đó, $way[j]$, đối với mỗi cột $j$, chứa số của cột trước đó trong đường đi (hoặc $0$ nếu không có).

Bản thân thuật toán là một **vòng lặp ngoài qua các hàng của ma trận**, bên trong đó hàng thứ $i$ của ma trận được xem xét. Vòng lặp _do-while_ đầu tiên chạy cho đến khi tìm thấy một cột tự do $j0$. Mỗi lần lặp của vòng lặp đánh dấu đã thăm một cột mới với số $j0$ (được tính toán ở lần lặp cuối cùng; và ban đầu bằng 0 - tức là chúng ta bắt đầu từ một cột giả), cũng như một hàng mới $i0$ - kề với nó trong cặp ghép (tức là $p[j0]$; và ban đầu khi $j0=0$ hàng thứ $i$ được lấy). Do sự xuất hiện của một hàng đã thăm mới $i0$, bạn cần tính toán lại mảng $minv$ và $\Delta$ tương ứng. Nếu $\Delta$ được cập nhật, thì cột $j1$ trở thành cực tiểu đã đạt được (lưu ý rằng với cài đặt như vậy $\Delta$ có thể bằng 0, điều đó có nghĩa là thế năng không thể thay đổi ở bước hiện tại: đã có một cột có thể đến được mới). Sau đó, thế năng và mảng $minv$ được tính toán lại. Ở cuối vòng lặp "do-while", chúng ta đã tìm thấy một đường tăng kết thúc bằng một cột $j0$ có thể được "mở ra" bằng cách sử dụng mảng tổ tiên $way$.

Hằng số <tt>INF</tt> là "vô cùng", tức là một số nào đó, rõ ràng lớn hơn tất cả các số có thể có trong ma trận đầu vào $A$.

```cpp
vector<int> u (n+1), v (m+1), p (m+1), way (m+1);
for (int i=1; i<=n; ++i) {
    p[0] = i;
    int j0 = 0;
    vector<int> minv (m+1, INF);
    vector<bool> used (m+1, false);
    do {
        used[j0] = true;
        int i0 = p[j0],  delta = INF,  j1;
        for (int j=1; j<=m; ++j)
            if (!used[j]) {
                int cur = A[i0][j]-u[i0]-v[j];
                if (cur < minv[j])
                    minv[j] = cur,  way[j] = j0;
                if (minv[j] < delta)
                    delta = minv[j],  j1 = j;
            }
        for (int j=0; j<=m; ++j)
            if (used[j])
                u[p[j]] += delta,  v[j] -= delta;
            else
                minv[j] -= delta;
        j0 = j1;
    } while (p[j0] != 0);
    do {
        int j1 = way[j0];
        p[j0] = p[j1];
        j0 = j1;
    } while (j0);
}
```

Để khôi phục câu trả lời ở dạng quen thuộc hơn, tức là tìm cho mỗi hàng $i = 1 \ldots n$ số $ans[i]$ của cột được chọn trong đó, có thể được thực hiện như sau:

```cpp
vector<int> ans (n+1);
for (int j=1; j<=m; ++j)
    ans[p[j]] = j;
```

Chi phí của cặp ghép có thể đơn giản được lấy làm thế năng của cột 0 (lấy với dấu ngược lại). Thật vậy, như bạn có thể thấy từ mã, $-v[0]$ chứa tổng của tất cả các giá trị của $\Delta$, tức là tổng thay đổi trong thế năng. Mặc dù một số giá trị của $u[i]$ và $v[j]$ có thể thay đổi cùng một lúc, tổng thay đổi trong thế năng chính xác bằng $\Delta$, vì cho đến khi có một đường tăng, số lượng hàng có thể đến được nhiều hơn chính xác một so với số lượng cột có thể đến được (chỉ có hàng hiện tại $i$ không có một "cặp" dưới dạng một cột đã thăm):

```cpp
int cost = -v[0];
```

## Kết nối với Thuật toán đường đi ngắn nhất liên tiếp (Connection to the Successive Shortest Path Algorithm) {: #connection-to-the-successive-shortest-path-algorithm}

Thuật toán Hungary có thể được coi là [Thuật toán đường đi ngắn nhất liên tiếp](min-cost-flow.md), được điều chỉnh cho bài toán phân công. Không đi sâu vào chi tiết, hãy cung cấp một trực giác về mối liên hệ giữa chúng.

Thuật toán đường đi liên tiếp sử dụng phiên bản sửa đổi của thuật toán Johnson làm kỹ thuật đánh trọng số lại. Điều này được chia thành bốn bước:

- Sử dụng thuật toán [Bellman-Ford](bellman-ford.md), bắt đầu từ đích $s$ và, đối với mỗi nút, tìm trọng số tối thiểu $h(v)$ của một đường đi từ $s$ đến $v$.

Cho mỗi bước của thuật toán chính:

- Đánh trọng số lại các cạnh của đồ thị ban đầu theo cách này: $w(u,v) \gets w(u,v)+h(u)-h(v)$.
- Sử dụng thuật toán [Dijkstra](dijkstra.md) để tìm đồ thị con đường đi ngắn nhất của mạng ban đầu.
- Cập nhật thế năng cho lần lặp tiếp theo.

Với mô tả này, chúng ta có thể quan sát thấy rằng có một sự tương tự mạnh mẽ giữa $h(v)$ và thế năng: có thể kiểm tra xem chúng có bằng nhau hay không cho đến một hằng số bù. Ngoài ra, có thể chỉ ra rằng, sau khi đánh trọng số lại, tập hợp tất cả các cạnh có trọng số bằng 0 đại diện cho đồ thị con đường đi ngắn nhất nơi thuật toán chính cố gắng tăng luồng. Điều này cũng xảy ra trong thuật toán Hungary: chúng ta tạo một đồ thị con được làm bằng các cạnh cứng (những cạnh mà lượng $A[i][j]-u[i]-v[j]$ bằng 0), và chúng ta cố gắng tăng kích thước của cặp ghép.

Trong bước 4, tất cả $h(v)$ được cập nhật: mỗi lần chúng ta sửa đổi mạng luồng, chúng ta nên đảm bảo rằng khoảng cách từ nguồn là chính xác (ngược lại, trong lần lặp tiếp theo, thuật toán Dijkstra có thể thất bại). Điều này nghe giống như bản cập nhật được thực hiện trên các thế năng, nhưng trong trường hợp này, chúng không được tăng đều.

Để hiểu sâu hơn về thế năng, hãy tham khảo [bài viết này](https://codeforces.com/blog/entry/105658).
