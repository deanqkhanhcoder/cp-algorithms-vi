---
tags:
  - Translated
e_maxx_link: segment_tree
---

# Cây phân đoạn

Cây phân đoạn là một cấu trúc dữ liệu lưu trữ thông tin về các khoảng của mảng dưới dạng một cây. Điều này cho phép trả lời các truy vấn trên đoạn của một mảng một cách hiệu quả, trong khi vẫn đủ linh hoạt để cho phép sửa đổi mảng nhanh chóng.
Điều này bao gồm việc tìm tổng của các phần tử mảng liên tiếp $a[l \dots r]$, hoặc tìm phần tử nhỏ nhất trong một đoạn như vậy trong thời gian $O(\log n)$. 
Giữa các lần trả lời các truy vấn như vậy, Cây phân đoạn cho phép sửa đổi mảng bằng cách thay thế một phần tử, hoặc thậm chí thay đổi các phần tử của cả một đoạn con (ví dụ: gán tất cả các phần tử $a[l \dots r]$ cho bất kỳ giá trị nào, hoặc cộng một giá trị vào tất cả các phần tử trong đoạn con). 

Nói chung, Cây phân đoạn là một cấu trúc dữ liệu rất linh hoạt, và một số lượng lớn các bài toán có thể được giải quyết bằng nó. 
Ngoài ra, cũng có thể áp dụng các hoạt động phức tạp hơn và trả lời các truy vấn phức tạp hơn (xem [Các phiên bản nâng cao của Cây phân đoạn](segment_tree.md#advanced-versions-of-segment-trees)).
Cụ thể, Cây phân đoạn có thể dễ dàng được tổng quát hóa cho các chiều lớn hơn. 
Ví dụ, với Cây phân đoạn hai chiều, bạn có thể trả lời các truy vấn tổng hoặc cực tiểu trên một hình chữ nhật con nào đó của một ma trận đã cho chỉ trong thời gian $O(\log^2 n)$. 

Một thuộc tính quan trọng của Cây phân đoạn là chúng chỉ yêu cầu một lượng bộ nhớ tuyến tính.
Cây phân đoạn tiêu chuẩn yêu cầu $4n$ đỉnh để làm việc trên một mảng có kích thước $n$. 

## Dạng đơn giản nhất của Cây phân đoạn

Để bắt đầu dễ dàng, chúng ta hãy xem xét dạng đơn giản nhất của Cây phân đoạn. 
Chúng ta muốn trả lời các truy vấn tổng một cách hiệu quả. 
Định nghĩa chính thức của nhiệm vụ của chúng ta là:
Cho một mảng $a[0 \dots n-1]$, Cây phân đoạn phải có khả năng tìm tổng các phần tử giữa các chỉ số $l$ và $r$ (tức là tính tổng $\sum_{i=l}^r a[i]$), và cũng xử lý việc thay đổi giá trị của các phần tử trong mảng (tức là thực hiện các phép gán có dạng $a[i] = x$).
Cây phân đoạn phải có khả năng xử lý **cả hai** truy vấn trong thời gian $O(\log n)$. 

Đây là một sự cải tiến so với các cách tiếp cận đơn giản hơn.
Một triển khai mảng ngây thơ - chỉ sử dụng một mảng đơn giản - có thể cập nhật các phần tử trong $O(1)$, nhưng yêu cầu $O(n)$ để tính mỗi truy vấn tổng. 
Và các tổng tiền tố được tính trước có thể tính các truy vấn tổng trong $O(1)$, nhưng việc cập nhật một phần tử mảng yêu cầu $O(n)$ thay đổi đối với các tổng tiền tố.

### Cấu trúc của Cây phân đoạn

Chúng ta có thể áp dụng cách tiếp cận chia để trị khi nói đến các đoạn mảng. 
Chúng ta tính toán và lưu trữ tổng của các phần tử của toàn bộ mảng, tức là tổng của đoạn $a[0 \dots n-1]$. 
Sau đó, chúng ta chia mảng thành hai nửa $a[0 \dots (n-1)/2]$ và $a[(n+1)/2 \dots n-1]$ và tính tổng của mỗi nửa và lưu trữ chúng. 
Mỗi nửa này lần lượt được chia thành hai nửa, và cứ thế cho đến khi tất cả các đoạn đạt đến kích thước $1$. 

Chúng ta có thể xem các đoạn này như là tạo thành một cây nhị phân: 
gốc của cây này là đoạn $a[0 \dots n-1]$, và mỗi đỉnh (ngoại trừ các đỉnh lá) có chính xác hai đỉnh con. 
Đây là lý do tại sao cấu trúc dữ liệu được gọi là "Cây phân đoạn", mặc dù trong hầu hết các triển khai, cây không được xây dựng một cách tường minh (xem [Triển khai](segment_tree.md#implementation)).

Đây là một biểu diễn trực quan của một Cây phân đoạn như vậy trên mảng $a = [1, 3, -2, 8, -7]$:

!["Cây phân đoạn tổng"](sum-segment-tree.png)

Từ mô tả ngắn gọn này về cấu trúc dữ liệu, chúng ta đã có thể kết luận rằng một Cây phân đoạn chỉ yêu cầu một số lượng đỉnh tuyến tính. 
Mức đầu tiên của cây chứa một nút duy nhất (gốc), mức thứ hai sẽ chứa hai đỉnh, ở mức thứ ba nó sẽ chứa bốn đỉnh, cho đến khi số đỉnh đạt đến $n$. 
Do đó, số đỉnh trong trường hợp xấu nhất có thể được ước tính bằng tổng $1 + 2 + 4 + \dots + 2^{\lceil\log_2 n\rceil} \lt 2^{\lceil\log_2 n\rceil + 1} \lt 4n$. 

Đáng chú ý là bất cứ khi nào $n$ không phải là lũy thừa của hai, không phải tất cả các cấp của Cây phân đoạn sẽ được lấp đầy hoàn toàn. 
Chúng ta có thể thấy hành vi đó trong hình ảnh. 
Bây giờ chúng ta có thể quên đi thực tế này, nhưng nó sẽ trở nên quan trọng sau này trong quá trình triển khai. 

Chiều cao của Cây phân đoạn là $O(\log n)$, bởi vì khi đi xuống từ gốc đến các lá, kích thước của các đoạn giảm khoảng một nửa. 

### Xây dựng

Trước khi xây dựng cây phân đoạn, chúng ta cần quyết định:

1. *giá trị* được lưu trữ tại mỗi nút của cây phân đoạn.
   Ví dụ, trong một cây phân đoạn tổng, một nút sẽ lưu trữ tổng của các phần tử trong đoạn của nó $[l, r]$.
2. phép toán *hợp nhất* hợp nhất hai nút anh em trong một cây phân đoạn.
   Ví dụ, trong một cây phân đoạn tổng, hai nút tương ứng với các đoạn $a[l_1 \dots r_1]$ và $a[l_2 \dots r_2]$ sẽ được hợp nhất thành một nút tương ứng với đoạn $a[l_1 \dots r_2]$ bằng cách cộng các giá trị của hai nút.

Lưu ý rằng một đỉnh là "đỉnh lá", nếu đoạn tương ứng của nó chỉ bao phủ một giá trị trong mảng ban đầu. Nó có mặt ở mức thấp nhất của một cây phân đoạn. Giá trị của nó sẽ bằng phần tử (tương ứng) $a[i]$. 

Bây giờ, để xây dựng cây phân đoạn, chúng ta bắt đầu ở mức dưới cùng (các đỉnh lá) và gán cho chúng các giá trị tương ứng của chúng. Trên cơ sở các giá trị này, chúng ta có thể tính toán các giá trị của mức trước đó, bằng cách sử dụng hàm `hợp nhất`. 
Và trên cơ sở những giá trị đó, chúng ta có thể tính toán các giá trị của mức trước đó, và lặp lại quy trình cho đến khi chúng ta đến đỉnh gốc. 

Thuận tiện để mô tả hoạt động này một cách đệ quy theo hướng khác, tức là từ đỉnh gốc đến các đỉnh lá. Quy trình xây dựng, nếu được gọi trên một đỉnh không phải là lá, thực hiện như sau:

1. đệ quy xây dựng các giá trị của hai đỉnh con
2. hợp nhất các giá trị đã tính của các con này.

Chúng ta bắt đầu xây dựng ở đỉnh gốc, và do đó, chúng ta có thể tính toán toàn bộ cây phân đoạn. 

Độ phức tạp thời gian của việc xây dựng này là $O(n)$, giả sử rằng hoạt động hợp nhất là thời gian không đổi (hoạt động hợp nhất được gọi $n$ lần, bằng với số lượng các nút bên trong trong cây phân đoạn).

### Truy vấn tổng

Bây giờ chúng ta sẽ trả lời các truy vấn tổng. Như một đầu vào, chúng ta nhận được hai số nguyên $l$ và $r$, và chúng ta phải tính tổng của đoạn $a[l \dots r]$ trong thời gian $O(\log n)$. 

Để làm điều này, chúng ta sẽ duyệt qua Cây phân đoạn và sử dụng các tổng đã được tính trước của các đoạn. 
Hãy giả sử rằng chúng ta hiện đang ở đỉnh bao phủ đoạn $a[tl \dots tr]$.
Có ba trường hợp có thể xảy ra. 

Trường hợp dễ nhất là khi đoạn $a[l \dots r]$ bằng với đoạn tương ứng của đỉnh hiện tại (tức là $a[l \dots r] = a[tl \dots tr]$), thì chúng ta đã xong và có thể trả về tổng đã được tính trước được lưu trữ trong đỉnh.

Ngoài ra, đoạn của truy vấn có thể hoàn toàn nằm trong miền của con trái hoặc con phải. 
Hãy nhớ lại rằng con trái bao phủ đoạn $a[tl \dots tm]$ và đỉnh phải bao phủ đoạn $a[tm + 1 \dots tr]$ với $tm = (tl + tr) / 2$. 
Trong trường hợp này, chúng ta có thể chỉ cần đi đến đỉnh con, mà đoạn tương ứng của nó bao phủ đoạn truy vấn, và thực hiện thuật toán được mô tả ở đây với đỉnh đó. 

Và sau đó là trường hợp cuối cùng, đoạn truy vấn giao với cả hai con. 
Trong trường hợp này, chúng ta không có lựa chọn nào khác ngoài việc thực hiện hai lệnh gọi đệ quy, một cho mỗi con. 
Đầu tiên, chúng ta đi đến con trái, tính toán một câu trả lời một phần cho đỉnh này (tức là tổng các giá trị của giao giữa đoạn của truy vấn và đoạn của con trái), sau đó đi đến con phải, tính toán câu trả lời một phần bằng cách sử dụng đỉnh đó, và sau đó kết hợp các câu trả lời bằng cách cộng chúng. 
Nói cách khác, vì con trái đại diện cho đoạn $a[tl \dots tm]$ và con phải đại diện cho đoạn $a[tm+1 \dots tr]$, chúng ta tính truy vấn tổng $a[l \dots tm]$ bằng cách sử dụng con trái, và truy vấn tổng $a[tm+1 \dots r]$ bằng cách sử dụng con phải. 

Vì vậy, việc xử lý một truy vấn tổng là một hàm gọi đệ quy chính nó một lần với con trái hoặc con phải (mà không thay đổi ranh giới truy vấn), hoặc hai lần, một lần cho con trái và một lần cho con phải (bằng cách chia truy vấn thành hai truy vấn con). 
Và đệ quy kết thúc, bất cứ khi nào ranh giới của đoạn truy vấn hiện tại trùng với ranh giới của đoạn của đỉnh hiện tại. 
Trong trường hợp đó, câu trả lời sẽ là giá trị đã được tính trước của tổng của đoạn này, được lưu trữ trong cây.

Nói cách khác, việc tính toán truy vấn là một cuộc duyệt cây, lan truyền qua tất cả các nhánh cần thiết của cây, và sử dụng các giá trị tổng đã được tính trước của các đoạn trong cây. 

Rõ ràng là chúng ta sẽ bắt đầu duyệt từ đỉnh gốc của Cây phân đoạn.

Quy trình được minh họa trong hình ảnh sau đây. 
Một lần nữa, mảng $a = [1, 3, -2, 8, -7]$ được sử dụng, và ở đây chúng ta muốn tính tổng $\sum_{i=2}^4 a[i]$. 
Các đỉnh được tô màu sẽ được truy cập, và chúng ta sẽ sử dụng các giá trị đã được tính trước của các đỉnh màu xanh lá cây. 
Điều này cho chúng ta kết quả $-2 + 1 = -1$. 

!["Truy vấn Cây phân đoạn tổng"](sum-segment-tree-query.png)

Tại sao độ phức tạp của thuật toán này là $O(\log n)$?
Để chứng minh độ phức tạp này, chúng ta hãy xem xét từng cấp độ của cây. 
Hóa ra, đối với mỗi cấp độ, chúng ta chỉ truy cập không quá bốn đỉnh. 
Và vì chiều cao của cây là $O(\log n)$, chúng ta nhận được thời gian chạy mong muốn. 

Chúng ta có thể chứng minh rằng mệnh đề này (tối đa bốn đỉnh mỗi cấp độ) là đúng bằng quy nạp. 
Ở cấp độ đầu tiên, chúng ta chỉ truy cập một đỉnh, đỉnh gốc, vì vậy ở đây chúng ta truy cập ít hơn bốn đỉnh. 
Bây giờ hãy xem xét một cấp độ tùy ý. 
Theo giả thuyết quy nạp, chúng ta truy cập nhiều nhất bốn đỉnh. 
Nếu chúng ta chỉ truy cập nhiều nhất hai đỉnh, cấp độ tiếp theo có nhiều nhất bốn đỉnh. Điều đó là tầm thường, vì mỗi đỉnh chỉ có thể gây ra nhiều nhất hai lệnh gọi đệ quy. 
Vì vậy, hãy giả sử rằng chúng ta truy cập ba hoặc bốn đỉnh ở cấp độ hiện tại. 
Từ những đỉnh đó, chúng ta sẽ phân tích kỹ hơn các đỉnh ở giữa. 
Vì truy vấn tổng yêu cầu tổng của một mảng con liên tục, chúng ta biết rằng các đoạn tương ứng với các đỉnh đã truy cập ở giữa sẽ được bao phủ hoàn toàn bởi đoạn của truy vấn tổng. 
Do đó, các đỉnh này sẽ không thực hiện bất kỳ lệnh gọi đệ quy nào. 
Vì vậy, chỉ có đỉnh ngoài cùng bên trái và ngoài cùng bên phải mới có khả năng thực hiện các lệnh gọi đệ quy. 
Và những lệnh gọi đó sẽ chỉ tạo ra nhiều nhất bốn lệnh gọi đệ quy, vì vậy cấp độ tiếp theo cũng sẽ thỏa mãn khẳng định. 
Chúng ta có thể nói rằng một nhánh tiếp cận ranh giới bên trái của truy vấn, và nhánh thứ hai tiếp cận ranh giới bên phải của nó. 

Do đó, chúng ta truy cập nhiều nhất là $4 \log n$ đỉnh tổng cộng, và điều đó tương đương với thời gian chạy $O(\log n)$. 

Kết luận, truy vấn hoạt động bằng cách chia đoạn đầu vào thành nhiều đoạn con mà tất cả các tổng đã được tính trước và được lưu trữ trong cây. 
Và nếu chúng ta ngừng phân vùng bất cứ khi nào đoạn truy vấn trùng với đoạn đỉnh, thì chúng ta chỉ cần $O(\log n)$ đoạn như vậy, điều này mang lại hiệu quả của Cây phân đoạn. 

### Truy vấn cập nhật

Bây giờ chúng ta muốn sửa đổi một phần tử cụ thể trong mảng, giả sử chúng ta muốn thực hiện phép gán $a[i] = x$. 
Và chúng ta phải xây dựng lại Cây phân đoạn, sao cho nó tương ứng với mảng mới, đã được sửa đổi.

Truy vấn này dễ hơn truy vấn tổng. 
Mỗi cấp độ của Cây phân đoạn tạo thành một phân hoạch của mảng. 
Do đó, một phần tử $a[i]$ chỉ đóng góp vào một đoạn từ mỗi cấp độ. 
Do đó, chỉ có $O(\log n)$ đỉnh cần được cập nhật. 

Dễ dàng thấy rằng, yêu cầu cập nhật có thể được triển khai bằng một hàm đệ quy. 
Hàm nhận vào đỉnh cây hiện tại, và nó đệ quy gọi chính nó với một trong hai đỉnh con (đỉnh chứa $a[i]$ trong đoạn của nó), và sau đó tính toán lại giá trị tổng của nó, tương tự như cách nó được thực hiện trong phương thức xây dựng (đó là tổng của hai con của nó).

Một lần nữa, đây là một hình dung sử dụng cùng một mảng. 
Ở đây chúng ta thực hiện cập nhật $a[2] = 3$. 
Các đỉnh màu xanh lá cây là các đỉnh mà chúng ta truy cập và cập nhật. 

!["Cập nhật Cây phân đoạn tổng"](sum-segment-tree-update.png)

### Cài đặt ### { #implementation}

Xem xét chính là cách lưu trữ Cây phân đoạn. 
Tất nhiên, chúng ta có thể định nghĩa một cấu trúc `Vertex` và tạo các đối tượng, lưu trữ ranh giới của đoạn, tổng của nó và ngoài ra còn có các con trỏ đến các đỉnh con của nó. 
Tuy nhiên, điều này đòi hỏi phải lưu trữ rất nhiều thông tin dư thừa dưới dạng con trỏ. 
Chúng ta sẽ sử dụng một mẹo đơn giản để làm cho điều này hiệu quả hơn nhiều bằng cách sử dụng một _cấu trúc dữ liệu ngầm_: Chỉ lưu trữ các tổng trong một mảng. 
(Một phương pháp tương tự được sử dụng cho các đống nhị phân). 
Tổng của đỉnh gốc ở chỉ số 1, tổng của hai đỉnh con của nó ở các chỉ số 2 và 3, tổng của các con của hai đỉnh đó ở các chỉ số 4 đến 7, v.v. 
Với chỉ số bắt đầu từ 1, thuận tiện là con trái của một đỉnh ở chỉ số $i$ được lưu trữ ở chỉ số $2i$, và con phải ở chỉ số $2i + 1$. 
Tương đương, cha của một đỉnh ở chỉ số $i$ được lưu trữ ở $i/2$ (phép chia số nguyên). 

Điều này đơn giản hóa việc triển khai rất nhiều. 
Chúng ta không cần phải lưu trữ cấu trúc của cây trong bộ nhớ. 
Nó được định nghĩa ngầm. 
Chúng ta chỉ cần một mảng chứa tổng của tất cả các đoạn. 

Như đã lưu ý trước đó, chúng ta cần lưu trữ nhiều nhất là $4n$ đỉnh. 
Nó có thể ít hơn, nhưng để thuận tiện, chúng ta luôn cấp phát một mảng có kích thước $4n$. 
Sẽ có một số phần tử trong mảng tổng không tương ứng với bất kỳ đỉnh nào trong cây thực tế, nhưng điều này không làm phức tạp việc triển khai. 

Vì vậy, chúng ta lưu trữ Cây phân đoạn đơn giản là một mảng $t[]$ với kích thước bốn lần kích thước đầu vào $n$: 

```{.cpp file=segment_tree_implementation_definition}
int n, t[4*MAXN];
```

Thủ tục xây dựng Cây phân đoạn từ một mảng $a[]$ đã cho trông như thế này: 
đó là một hàm đệ quy với các tham số $a[]$ (mảng đầu vào), $v$ (chỉ số của đỉnh hiện tại), và các ranh giới $tl$ và $tr$ của đoạn hiện tại. 
Trong chương trình chính, hàm này sẽ được gọi với các tham số của đỉnh gốc: $v = 1$, $tl = 0$, và $tr = n - 1$. 

```{.cpp file=segment_tree_implementation_build}
void build(int a[], int v, int tl, int tr) {
    if (tl == tr) {
        t[v] = a[tl];
    } else {
        int tm = (tl + tr) / 2;
        build(a, v*2, tl, tm);
        build(a, v*2+1, tm+1, tr);
        t[v] = t[v*2] + t[v*2+1];
    }
}
```

Tiếp theo, hàm trả lời các truy vấn tổng cũng là một hàm đệ quy, nhận vào các tham số về đỉnh/đoạn hiện tại (tức là chỉ số $v$ và các ranh giới $tl$ và $tr$) và cả thông tin về các ranh giới của truy vấn, $l$ và $r$. 
Để đơn giản hóa mã, hàm này luôn thực hiện hai lệnh gọi đệ quy, ngay cả khi chỉ có một lệnh gọi là cần thiết - trong trường hợp đó, lệnh gọi đệ quy thừa sẽ có $l > r$, và điều này có thể dễ dàng được bắt bằng một kiểm tra bổ sung ở đầu hàm. 

```{.cpp file=segment_tree_implementation_sum}
int sum(int v, int tl, int tr, int l, int r) {
    if (l > r) 
        return 0;
    if (l == tl && r == tr) {
        return t[v];
    }
    int tm = (tl + tr) / 2;
    return sum(v*2, tl, tm, l, min(r, tm))
           + sum(v*2+1, tm+1, tr, max(l, tm+1), r);
}
```

Cuối cùng là truy vấn cập nhật. Hàm cũng sẽ nhận thông tin về đỉnh/đoạn hiện tại, và ngoài ra còn có tham số của truy vấn cập nhật (tức là vị trí của phần tử và giá trị mới của nó). 

```{.cpp file=segment_tree_implementation_update}
void update(int v, int tl, int tr, int pos, int new_val) {
    if (tl == tr) {
        t[v] = new_val;
    } else {
        int tm = (tl + tr) / 2;
        if (pos <= tm)
            update(v*2, tl, tm, pos, new_val);
        else
            update(v*2+1, tm+1, tr, pos, new_val);
        t[v] = t[v*2] + t[v*2+1];
    }
}
```

### Cài đặt hiệu quả bộ nhớ

Hầu hết mọi người sử dụng triển khai từ phần trước. Nếu bạn nhìn vào mảng `t`, bạn có thể thấy rằng nó tuân theo việc đánh số các nút cây theo thứ tự duyệt BFS (duyệt theo cấp). 
Sử dụng duyệt này, các con của đỉnh $v$ lần lượt là $2v$ và $2v + 1$. 
Tuy nhiên, nếu $n$ không phải là lũy thừa của hai, phương pháp này sẽ bỏ qua một số chỉ số và để lại một số phần của mảng `t` không được sử dụng. 
Mức tiêu thụ bộ nhớ bị giới hạn bởi $4n$, mặc dù một Cây phân đoạn của một mảng gồm $n$ phần tử chỉ yêu cầu $2n - 1$ đỉnh. 

Tuy nhiên, nó có thể được giảm bớt. 
Chúng ta đánh số lại các đỉnh của cây theo thứ tự của một chuyến du lịch Euler (duyệt theo thứ tự trước), và chúng ta viết tất cả các đỉnh này cạnh nhau. 

Hãy xem một đỉnh ở chỉ số $v$, và để nó chịu trách nhiệm cho đoạn $[l, r]$, và đặt $mid = \dfrac{l + r}{2}$. 
Rõ ràng là con trái sẽ có chỉ số $v + 1$. 
Con trái chịu trách nhiệm cho đoạn $[l, mid]$, tức là tổng cộng sẽ có $2 * (mid - l + 1) - 1$ đỉnh trong cây con của con trái. 
Do đó, chúng ta có thể tính chỉ số của con phải của $v$. Chỉ số sẽ là $v + 2 * (mid - l + 1)$. 
Bằng cách đánh số này, chúng ta đạt được sự giảm bớt bộ nhớ cần thiết xuống còn $2n$. 

## Các phiên bản nâng cao của Cây phân đoạn


Cây phân đoạn là một cấu trúc dữ liệu rất linh hoạt, và cho phép các biến thể và mở rộng theo nhiều hướng khác nhau. 
Hãy thử phân loại chúng dưới đây. 

### Các truy vấn phức tạp hơn

Có thể khá dễ dàng để thay đổi Cây phân đoạn theo một hướng, để nó tính toán các truy vấn khác nhau (ví dụ: tính toán cực tiểu / cực đại thay vì tổng), nhưng nó cũng có thể rất không tầm thường. 

#### Tìm giá trị lớn nhất

Hãy thay đổi một chút điều kiện của bài toán được mô tả ở trên: thay vì truy vấn tổng, bây giờ chúng ta sẽ thực hiện các truy vấn tìm giá trị lớn nhất. 

Cây sẽ có cấu trúc hoàn toàn giống như cây được mô tả ở trên. 
Chúng ta chỉ cần thay đổi cách tính $t[v]$ trong các hàm `build` và `update`. 
$t[v]$ bây giờ sẽ lưu trữ giá trị lớn nhất của đoạn tương ứng. 
Và chúng ta cũng cần thay đổi việc tính toán giá trị trả về của hàm `sum` (thay thế phép cộng bằng phép lấy giá trị lớn nhất). 

Tất nhiên, bài toán này có thể dễ dàng được thay đổi thành tính toán giá trị nhỏ nhất thay vì giá trị lớn nhất. 

Thay vì hiển thị một triển khai cho bài toán này, việc triển khai sẽ được đưa ra cho một phiên bản phức tạp hơn của bài toán này trong phần tiếp theo. 

#### Tìm giá trị lớn nhất và số lần xuất hiện 

Nhiệm vụ này rất giống với nhiệm vụ trước đó. 
Ngoài việc tìm giá trị lớn nhất, chúng ta cũng phải tìm số lần xuất hiện của giá trị lớn nhất. 

Để giải quyết bài toán này, chúng ta lưu trữ một cặp số ở mỗi đỉnh trong cây: 
Ngoài giá trị lớn nhất, chúng ta còn lưu trữ số lần xuất hiện của nó trong đoạn tương ứng. 
Việc xác định cặp đúng để lưu trữ tại $t[v]$ vẫn có thể được thực hiện trong thời gian không đổi bằng cách sử dụng thông tin của các cặp được lưu trữ tại các đỉnh con. 
Việc kết hợp hai cặp như vậy nên được thực hiện trong một hàm riêng, vì đây sẽ là một hoạt động mà chúng ta sẽ thực hiện trong khi xây dựng cây, trong khi trả lời các truy vấn tìm giá trị lớn nhất và trong khi thực hiện các sửa đổi. 

```{.cpp file=segment_tree_maximum_and_count}
pair<int, int> t[4*MAXN];

pair<int, int> combine(pair<int, int> a, pair<int, int> b) {
    if (a.first > b.first) 
        return a;
    if (b.first > a.first)
        return b;
    return make_pair(a.first, a.second + b.second);
}

void build(int a[], int v, int tl, int tr) {
    if (tl == tr) {
        t[v] = make_pair(a[tl], 1);
    } else {
        int tm = (tl + tr) / 2;
        build(a, v*2, tl, tm);
        build(a, v*2+1, tm+1, tr);
        t[v] = combine(t[v*2], t[v*2+1]);
    }
}

pair<int, int> get_max(int v, int tl, int tr, int l, int r) {
    if (l > r)
        return make_pair(-INF, 0);
    if (l == tl && r == tr)
        return t[v];
    int tm = (tl + tr) / 2;
    return combine(get_max(v*2, tl, tm, l, min(r, tm)), 
                   get_max(v*2+1, tm+1, tr, max(l, tm+1), r));
}

void update(int v, int tl, int tr, int pos, int new_val) {
    if (tl == tr) {
        t[v] = make_pair(new_val, 1);
    } else {
        int tm = (tl + tr) / 2;
        if (pos <= tm)
            update(v*2, tl, tm, pos, new_val);
        else
            update(v*2+1, tm+1, tr, pos, new_val);
        t[v] = combine(t[v*2], t[v*2+1]);
    }
}
```
#### Tính ước chung lớn nhất / bội chung nhỏ nhất

Trong bài toán này, chúng ta muốn tính ƯCLN / BCNN của tất cả các số trong các đoạn đã cho của mảng. 

Biến thể thú vị này của Cây phân đoạn có thể được giải quyết theo cách hoàn toàn giống như các Cây phân đoạn mà chúng ta đã suy ra cho các truy vấn tổng / cực tiểu / cực đại:
chỉ cần lưu trữ ƯCLN / BCNN của đỉnh tương ứng trong mỗi đỉnh của cây. 
Việc kết hợp hai đỉnh có thể được thực hiện bằng cách tính ƯCLN / BCNN của cả hai đỉnh.

#### Đếm số lượng số không, tìm kiếm số không thứ $k$ { #counting-zero-search-kth data-toc-label="Counting the number of zeros, searching for the k-th zero"}

Trong bài toán này, chúng ta muốn tìm số lượng số không trong một đoạn đã cho, và ngoài ra tìm chỉ số của số không thứ $k$ bằng một hàm thứ hai. 

Một lần nữa, chúng ta phải thay đổi một chút các giá trị lưu trữ của cây:
lần này chúng ta sẽ lưu trữ số lượng số không trong mỗi đoạn trong $t[]$. 
Khá rõ ràng cách triển khai các hàm `build`, `update` và `count_zero`, chúng ta có thể chỉ cần sử dụng các ý tưởng từ bài toán truy vấn tổng. 
Do đó, chúng ta đã giải quyết được phần đầu tiên của bài toán. 

Bây giờ chúng ta học cách giải quyết bài toán tìm số không thứ $k$ trong mảng $a[]$. 
Để thực hiện nhiệm vụ này, chúng ta sẽ đi xuống Cây phân đoạn, bắt đầu từ đỉnh gốc, và di chuyển mỗi lần đến con trái hoặc con phải, tùy thuộc vào đoạn nào chứa số không thứ $k$. 
Để quyết định chúng ta cần đi đến con nào, chỉ cần xem xét số lượng số không xuất hiện trong đoạn tương ứng với đỉnh trái. 
Nếu số đếm đã được tính trước này lớn hơn hoặc bằng $k$, thì cần phải đi xuống con trái, và nếu không thì đi xuống con phải. 
Lưu ý, nếu chúng ta chọn con phải, chúng ta phải trừ số lượng số không của con trái khỏi $k$. 

Trong triển khai, chúng ta có thể xử lý trường hợp đặc biệt, $a[]$ chứa ít hơn $k$ số không, bằng cách trả về -1. 

```{.cpp file=segment_tree_kth_zero}
int find_kth(int v, int tl, int tr, int k) {
    if (k > t[v])
        return -1;
    if (tl == tr)
        return tl;
    int tm = (tl + tr) / 2;
    if (t[v*2] >= k)
        return find_kth(v*2, tl, tm, k);
    else 
        return find_kth(v*2+1, tm+1, tr, k - t[v*2]);
}
```

#### Tìm kiếm một tiền tố mảng với một tổng cho trước

Nhiệm vụ như sau: 
đối với một giá trị $x$ đã cho, chúng ta phải nhanh chóng tìm chỉ số nhỏ nhất $i$ sao cho tổng của $i$ phần tử đầu tiên của mảng $a[]$ lớn hơn hoặc bằng $x$ (giả sử rằng mảng $a[]$ chỉ chứa các giá trị không âm). 

Nhiệm vụ này có thể được giải quyết bằng tìm kiếm nhị phân, tính toán tổng của các tiền tố bằng Cây phân đoạn. 
Tuy nhiên, điều này sẽ dẫn đến một giải pháp $O(\log^2 n)$. 

Thay vào đó, chúng ta có thể sử dụng cùng một ý tưởng như trong phần trước, và tìm vị trí bằng cách đi xuống cây:
bằng cách di chuyển mỗi lần sang trái hoặc sang phải, tùy thuộc vào tổng của con trái. 
Do đó, tìm câu trả lời trong thời gian $O(\log n)$. 

#### Tìm kiếm phần tử đầu tiên lớn hơn một giá trị cho trước

Nhiệm vụ như sau: 
đối với một giá trị $x$ đã cho và một đoạn $a[l \dots r]$, tìm $i$ nhỏ nhất trong đoạn $a[l \dots r]$, sao cho $a[i]$ lớn hơn $x$. 

Nhiệm vụ này có thể được giải quyết bằng tìm kiếm nhị phân trên các truy vấn cực đại trên tiền tố với Cây phân đoạn. 
Tuy nhiên, điều này sẽ dẫn đến một giải pháp $O(\log^2 n)$. 

Thay vào đó, chúng ta có thể sử dụng cùng một ý tưởng như trong các phần trước, và tìm vị trí bằng cách đi xuống cây:
bằng cách di chuyển mỗi lần sang trái hoặc sang phải, tùy thuộc vào giá trị cực đại của con trái. 
Do đó, tìm câu trả lời trong thời gian $O(\log n)$. 

```{.cpp file=segment_tree_first_greater}
int get_first(int v, int tl, int tr, int l, int r, int x) {
    if(tl > r || tr < l) return -1;
    if(t[v] <= x) return -1;
    
    if (tl== tr) return tl; 
    
    int tm = tl + (tr-tl)/2;
    int left = get_first(2*v, tl, tm, l, r, x);
    if(left != -1) return left;
    return get_first(2*v+1, tm+1, tr, l ,r, x);
}
```

#### Tìm các đoạn con có tổng lớn nhất

Ở đây, chúng ta lại nhận được một đoạn $a[l \dots r]$ cho mỗi truy vấn, lần này chúng ta phải tìm một đoạn con $a[l^\prime \dots r^\]$ sao cho $l \le l^\prime$ và $r^\prime \le r$ và tổng các phần tử của đoạn này là lớn nhất. 
Như trước đây, chúng ta cũng muốn có thể sửa đổi các phần tử riêng lẻ của mảng. 
Các phần tử của mảng có thể là số âm, và đoạn con tối ưu có thể là rỗng (ví dụ: nếu tất cả các phần tử đều âm). 

Bài toán này là một cách sử dụng không tầm thường của Cây phân đoạn. 
Lần này, chúng ta sẽ lưu trữ bốn giá trị cho mỗi đỉnh: 
tổng của đoạn, tổng tiền tố lớn nhất, tổng hậu tố lớn nhất, và tổng của đoạn con lớn nhất trong đó. 
Nói cách khác, đối với mỗi đoạn của Cây phân đoạn, câu trả lời đã được tính trước cũng như các câu trả lời cho các đoạn chạm vào ranh giới trái và phải của đoạn. 

Làm thế nào để xây dựng một cây với dữ liệu như vậy? 
Một lần nữa, chúng ta tính toán nó theo cách đệ quy: 
trước tiên, chúng ta tính toán tất cả bốn giá trị cho con trái và con phải, và sau đó kết hợp chúng để đạt được bốn giá trị cho đỉnh hiện tại. 
Lưu ý rằng câu trả lời cho đỉnh hiện tại là một trong ba trường hợp sau:

 * câu trả lời của con trái, có nghĩa là đoạn con tối ưu hoàn toàn nằm trong đoạn của con trái
 * câu trả lời của con phải, có nghĩa là đoạn con tối ưu hoàn toàn nằm trong đoạn của con phải
 * tổng của tổng hậu tố lớn nhất của con trái và tổng tiền tố lớn nhất của con phải, có nghĩa là đoạn con tối ưu giao với cả hai con. 

Do đó, câu trả lời cho đỉnh hiện tại là giá trị lớn nhất của ba giá trị này. 
Việc tính toán tổng tiền tố / hậu tố lớn nhất thậm chí còn dễ hơn. 
Đây là triển khai của hàm `combine`, nhận dữ liệu chỉ từ con trái và con phải, và trả về dữ liệu của đỉnh hiện tại. 

```{.cpp file=segment_tree_maximal_sum_subsegments1}
struct data { int sum, pref, suff, ans; };

data combine(data l, data r) {
    data res;
    res.sum = l.sum + r.sum;
    res.pref = max(l.pref, l.sum + r.pref);
    res.suff = max(r.suff, r.sum + l.suff);
    res.ans = max(max(l.ans, r.ans), l.suff + r.pref);
    return res;
}
```

Sử dụng hàm `combine`, dễ dàng xây dựng Cây phân đoạn. 
Chúng ta có thể triển khai nó theo cách hoàn toàn giống như trong các triển khai trước đó. 
Để khởi tạo các đỉnh lá, chúng ta bổ sung thêm hàm phụ `make_data`, sẽ trả về một đối tượng `data` chứa thông tin của một giá trị duy nhất. 

```{.cpp file=segment_tree_maximal_sum_subsegments2}
data make_data(int val) {
    data res;
    res.sum = val;
    res.pref = res.suff = res.ans = max(0, val);
    return res;
}

void build(int a[], int v, int tl, int tr) {
    if (tl == tr) {
        t[v] = make_data(a[tl]);
    } else {
        int tm = (tl + tr) / 2;
        build(a, v*2, tl, tm);
        build(a, v*2+1, tm+1, tr);
        t[v] = combine(t[v*2], t[v*2+1]);
    }
}
 
void update(int v, int tl, int tr, int pos, int new_val) {
    if (tl == tr) {
        t[v] = make_data(new_val);
    } else {
        int tm = (tl + tr) / 2;
        if (pos <= tm)
            update(v*2, tl, tm, pos, new_val);
        else
            update(v*2+1, tm+1, tr, pos, new_val);
        t[v] = combine(t[v*2], t[v*2+1]);
    }
}
```

Chỉ còn lại việc làm thế nào để tính toán câu trả lời cho một truy vấn. 
Để trả lời nó, chúng ta đi xuống cây như trước, chia truy vấn thành nhiều đoạn con trùng với các đoạn của Cây phân đoạn, và kết hợp các câu trả lời trong chúng thành một câu trả lời duy nhất cho truy vấn. 
Khi đó, rõ ràng là công việc hoàn toàn giống như trong Cây phân đoạn đơn giản, nhưng thay vì cộng / lấy cực tiểu / cực đại các giá trị, chúng ta sử dụng hàm `combine`. 

```{.cpp file=segment_tree_maximal_sum_subsegments3}
data query(int v, int tl, int tr, int l, int r) {
    if (l > r) 
        return make_data(0);
    if (l == tl && r == tr) 
        return t[v];
    int tm = (tl + tr) / 2;
    return combine(query(v*2, tl, tm, l, min(r, tm)), 
                   query(v*2+1, tm+1, tr, max(l, tm+1), r));
}
```

### Lưu toàn bộ mảng con trong mỗi đỉnh

Đây là một tiểu mục riêng biệt đứng riêng so với các tiểu mục khác, bởi vì tại mỗi đỉnh của Cây phân đoạn, chúng ta không lưu trữ thông tin về đoạn tương ứng ở dạng nén (tổng, cực tiểu, cực đại, ...), mà lưu trữ tất cả các phần tử của đoạn. 
Do đó, gốc của Cây phân đoạn sẽ lưu trữ tất cả các phần tử của mảng, đỉnh con trái sẽ lưu trữ nửa đầu của mảng, đỉnh con phải nửa sau, v.v. 

Trong ứng dụng đơn giản nhất của kỹ thuật này, chúng ta lưu trữ các phần tử theo thứ tự được sắp xếp. 
Trong các phiên bản phức tạp hơn, các phần tử không được lưu trữ trong danh sách, mà là các cấu trúc dữ liệu nâng cao hơn (tập hợp, bản đồ, ...). 
Nhưng tất cả các phương pháp này đều có yếu tố chung, đó là mỗi đỉnh yêu cầu bộ nhớ tuyến tính (tức là tỷ lệ với độ dài của đoạn tương ứng). 

Câu hỏi tự nhiên đầu tiên, khi xem xét các Cây phân đoạn này, là về mức tiêu thụ bộ nhớ. 
Về mặt trực giác, điều này có vẻ giống như bộ nhớ $O(n^2)$, nhưng hóa ra cây hoàn chỉnh sẽ chỉ cần bộ nhớ $O(n \\\log n)$. 
Tại sao lại như vậy? 
Khá đơn giản, bởi vì mỗi phần tử của mảng chỉ rơi vào $O(\log n)$ đoạn (hãy nhớ chiều cao của cây là $O(\log n)$). 

Vì vậy, bất chấp sự xa hoa rõ ràng của một Cây phân đoạn như vậy, nó chỉ tiêu thụ nhiều hơn một chút bộ nhớ so với Cây phân đoạn thông thường. 

Một số ứng dụng điển hình của cấu trúc dữ liệu này được mô tả dưới đây. 
Điều đáng chú ý là sự tương đồng của các Cây phân đoạn này với các cấu trúc dữ liệu 2D (trên thực tế, đây là một cấu trúc dữ liệu 2D, nhưng với các khả năng khá hạn chế). 

#### Tìm số nhỏ nhất lớn hơn hoặc bằng một số đã cho. Không có truy vấn sửa đổi. 

Chúng ta muốn trả lời các truy vấn có dạng sau: 
đối với ba số đã cho $(l, r, x)$, chúng ta phải tìm số nhỏ nhất trong đoạn $a[l \dots r]$ lớn hơn hoặc bằng $x$. 

Chúng ta xây dựng một Cây phân đoạn. 
Trong mỗi đỉnh, chúng ta lưu trữ một danh sách đã được sắp xếp của tất cả các số xuất hiện trong đoạn tương ứng, như đã mô tả ở trên. 
Làm thế nào để xây dựng một Cây phân đoạn như vậy một cách hiệu quả nhất có thể? 
Như mọi khi, chúng ta tiếp cận vấn đề này một cách đệ quy: hãy để danh sách của các con trái và phải đã được xây dựng, và chúng ta muốn xây dựng danh sách cho đỉnh hiện tại. 
Từ quan điểm này, hoạt động bây giờ là tầm thường và có thể được hoàn thành trong thời gian tuyến tính: 
Chúng ta chỉ cần kết hợp hai danh sách đã được sắp xếp thành một, điều này có thể được thực hiện bằng cách lặp qua chúng bằng hai con trỏ. 
Thư viện chuẩn C++ đã có một triển khai của thuật toán này. 

Vì cấu trúc của Cây phân đoạn này và sự tương đồng với thuật toán sắp xếp trộn, cấu trúc dữ liệu này cũng thường được gọi là "Cây sắp xếp trộn". 

```{.cpp file=segment_tree_smallest_number_greater1}
vector<int> t[4*MAXN];

void build(int a[], int v, int tl, int tr) {
    if (tl == tr) {
        t[v] = vector<int>(1, a[tl]);
    } else { 
        int tm = (tl + tr) / 2;
        build(a, v*2, tl, tm);
        build(a, v*2+1, tm+1, tr);
        merge(t[v*2].begin(), t[v*2].end(), t[v*2+1].begin(), t[v*2+1].end(),
              back_inserter(t[v]));
    }
}
```

Chúng ta đã biết rằng Cây phân đoạn được xây dựng theo cách này sẽ yêu cầu bộ nhớ $O(n \\log n)$. 
Và nhờ vào việc triển khai này, việc xây dựng của nó cũng mất thời gian $O(n \\log n)$, sau tất cả mỗi danh sách được xây dựng trong thời gian tuyến tính đối với kích thước của nó. 

Bây giờ hãy xem xét câu trả lời cho truy vấn. 
Chúng ta sẽ đi xuống cây, giống như trong Cây phân đoạn thông thường, chia đoạn của chúng ta $a[l \dots r]$ thành nhiều đoạn con (thành nhiều nhất là $O(\log n)$ mảnh). 
Rõ ràng là câu trả lời của toàn bộ câu trả lời là giá trị nhỏ nhất của mỗi truy vấn con. 
Vì vậy, bây giờ chúng ta chỉ cần hiểu, làm thế nào để trả lời một truy vấn trên một đoạn con như vậy tương ứng với một đỉnh nào đó của cây. 

Chúng ta đang ở một đỉnh nào đó của Cây phân đoạn và chúng ta muốn tính toán câu trả lời cho truy vấn, tức là tìm số nhỏ nhất lớn hơn hoặc bằng một số $x$ đã cho. 
Vì đỉnh chứa danh sách các phần tử theo thứ tự đã sắp xếp, chúng ta có thể chỉ cần thực hiện tìm kiếm nhị phân trên danh sách này và trả về số đầu tiên, lớn hơn hoặc bằng $x$. 

Do đó, câu trả lời cho truy vấn trong một đoạn của cây mất thời gian $O(\log n)$, và toàn bộ truy vấn được xử lý trong $O(\log^2 n)$. 

```{.cpp file=segment_tree_smallest_number_greater2}
int query(int v, int tl, int tr, int l, int r, int x) {
    if (l > r)
        return INF;
    if (l == tl && r == tr) {
        vector<int>::iterator pos = lower_bound(t[v].begin(), t[v].end(), x);
        if (pos != t[v].end())
            return *pos;
        return INF;
    }
    int tm = (tl + tr) / 2;
    return min(query(v*2, tl, tm, l, min(r, tm), x), 
               query(v*2+1, tm+1, tr, max(l, tm+1), r, x));
}
```

Hằng số `INF` bằng một số lớn nào đó lớn hơn tất cả các số trong mảng. 
Việc sử dụng nó có nghĩa là không có số nào lớn hơn hoặc bằng $x$ trong đoạn. 
Nó có ý nghĩa là "không có câu trả lời trong khoảng đã cho". 

#### Tìm số nhỏ nhất lớn hơn hoặc bằng một số đã cho. Với các truy vấn sửa đổi. 

Nhiệm vụ này tương tự như nhiệm vụ trước đó. 
Cách tiếp cận cuối cùng có một nhược điểm, không thể sửa đổi mảng giữa các lần trả lời truy vấn. 
Bây giờ chúng ta muốn làm chính xác điều này: một truy vấn sửa đổi sẽ thực hiện phép gán $a[i] = y$. 

Giải pháp tương tự như giải pháp của bài toán trước, nhưng thay vì danh sách ở mỗi đỉnh của Cây phân đoạn, chúng ta sẽ lưu trữ một danh sách cân bằng cho phép bạn nhanh chóng tìm kiếm các số, xóa các số và chèn các số mới. 
Vì mảng có thể chứa một số được lặp lại, lựa chọn tối ưu là cấu trúc dữ liệu `multiset`. 

Việc xây dựng một Cây phân đoạn như vậy được thực hiện gần như theo cách tương tự như trong bài toán trước, chỉ bây giờ chúng ta cần kết hợp các `multiset` chứ không phải danh sách đã được sắp xếp. 
Điều này dẫn đến thời gian xây dựng là $O(n \\log^2 n)$ (nói chung, việc hợp nhất hai cây đỏ-đen có thể được thực hiện trong thời gian tuyến tính, nhưng C++ STL không đảm bảo độ phức tạp thời gian này). 

Hàm `query` cũng gần như tương đương, chỉ bây giờ hàm `lower_bound` của hàm `multiset` nên được gọi thay thế (`std::lower_bound` chỉ hoạt động trong thời gian $O(\log n)$ nếu được sử dụng với các trình vòng lặp truy cập ngẫu nhiên). 

Cuối cùng là yêu cầu sửa đổi. 
Để xử lý nó, chúng ta phải đi xuống cây, và sửa đổi tất cả các `multiset` từ các đoạn tương ứng có chứa phần tử bị ảnh hưởng. 
Chúng ta chỉ cần xóa giá trị cũ của phần tử này (nhưng chỉ một lần xuất hiện), và chèn giá trị mới. 

```cpp
void update(int v, int tl, int tr, int pos, int new_val) {
    t[v].erase(t[v].find(a[pos]));
    t[v].insert(new_val);
    if (tl != tr) {
        int tm = (tl + tr) / 2;
        if (pos <= tm)
            update(v*2, tl, tm, pos, new_val);
        else
            update(v*2+1, tm+1, tr, pos, new_val);
    } else {
        a[pos] = new_val;
    }
}
```

Việc xử lý truy vấn sửa đổi này cũng mất thời gian $O(\log^2 n)$. 

#### Tìm số nhỏ nhất lớn hơn hoặc bằng một số đã cho. Tăng tốc bằng "fractional cascading". 

Chúng ta có cùng một phát biểu bài toán, chúng ta muốn tìm số nhỏ nhất lớn hơn hoặc bằng $x$ trong một đoạn, nhưng lần này trong thời gian $O(\log n)$. 
Chúng ta sẽ cải thiện độ phức tạp thời gian bằng cách sử dụng kỹ thuật "fractional cascading". 

Fractional cascading là một kỹ thuật đơn giản cho phép bạn cải thiện thời gian chạy của nhiều tìm kiếm nhị phân, được thực hiện cùng một lúc. 
Cách tiếp cận trước đây của chúng ta đối với truy vấn tìm kiếm là, chúng ta chia nhiệm vụ thành nhiều nhiệm vụ con, mỗi nhiệm vụ được giải quyết bằng một tìm kiếm nhị phân. 
Fractional cascading cho phép bạn thay thế tất cả các tìm kiếm nhị phân này bằng một tìm kiếm duy nhất. 

Ví dụ đơn giản và rõ ràng nhất của fractional cascading là bài toán sau:
có $k$ danh sách số đã được sắp xếp, và chúng ta phải tìm trong mỗi danh sách số đầu tiên lớn hơn hoặc bằng số đã cho. 

Thay vì thực hiện một tìm kiếm nhị phân cho mỗi danh sách, chúng ta có thể hợp nhất tất cả các danh sách thành một danh sách lớn đã được sắp xếp. 
Ngoài ra, đối với mỗi phần tử $y$, chúng ta lưu trữ một danh sách các kết quả tìm kiếm $y$ trong mỗi trong số $k$ danh sách. 
Do đó, nếu chúng ta muốn tìm số nhỏ nhất lớn hơn hoặc bằng $x$, chúng ta chỉ cần thực hiện một tìm kiếm nhị phân duy nhất, và từ danh sách các chỉ số, chúng ta có thể xác định số nhỏ nhất trong mỗi danh sách. 
Tuy nhiên, cách tiếp cận này yêu cầu bộ nhớ $O(n \\cdot k)$ ($n$ là độ dài của các danh sách kết hợp), có thể khá không hiệu quả. 

Fractional cascading giảm độ phức tạp bộ nhớ này xuống còn bộ nhớ $O(n)$, bằng cách tạo ra từ $k$ danh sách đầu vào $k$ danh sách mới, trong đó mỗi danh sách chứa danh sách tương ứng và ngoài ra còn có mọi phần tử thứ hai của danh sách mới sau đây. 
Sử dụng cấu trúc này, chỉ cần lưu trữ hai chỉ số, chỉ số của phần tử trong danh sách ban đầu, và chỉ số của phần tử trong danh sách mới sau đây. 
Vì vậy, cách tiếp cận này chỉ sử dụng bộ nhớ $O(n)$, và vẫn có thể trả lời các truy vấn bằng một tìm kiếm nhị phân duy nhất. 

Nhưng đối với ứng dụng của chúng ta, chúng ta không cần toàn bộ sức mạnh của fractional cascading. 
Trong Cây phân đoạn của chúng ta, một đỉnh sẽ chứa danh sách đã được sắp xếp của tất cả các phần tử xuất hiện trong cả cây con trái hoặc cây con phải (giống như trong Cây sắp xếp trộn). 
Ngoài danh sách đã được sắp xếp này, chúng ta lưu trữ hai vị trí cho mỗi phần tử. 
Đối với một phần tử $y$, chúng ta lưu trữ chỉ số nhỏ nhất $i$, sao cho phần tử thứ $i$ trong danh sách đã được sắp xếp của con trái lớn hơn hoặc bằng $y$. 
Và chúng ta lưu trữ chỉ số nhỏ nhất $j$, sao cho phần tử thứ $j$ trong danh sách đã được sắp xếp của con phải lớn hơn hoặc bằng $y$. 
Các giá trị này có thể được tính toán song song với bước hợp nhất khi chúng ta xây dựng cây. 

Điều này tăng tốc các truy vấn như thế nào? 

Hãy nhớ, trong giải pháp thông thường, chúng ta đã thực hiện một tìm kiếm nhị phân trong mỗi nút. 
Nhưng với sửa đổi này, chúng ta có thể tránh tất cả ngoại trừ một. 

Để trả lời một truy vấn, chúng ta chỉ cần thực hiện một tìm kiếm nhị phân trong nút gốc. 
Điều này cho chúng ta phần tử nhỏ nhất $y \ge x$ trong mảng hoàn chỉnh, nhưng nó cũng cho chúng ta hai vị trí. 
Chỉ số của phần tử nhỏ nhất lớn hơn hoặc bằng $x$ trong cây con trái, và chỉ số của phần tử nhỏ nhất $y$ trong cây con phải. Lưu ý rằng $\\ge y$ cũng giống như $\\ge x$, vì mảng của chúng ta không chứa bất kỳ phần tử nào giữa $x$ và $y$. 
Trong giải pháp Cây sắp xếp trộn thông thường, chúng ta sẽ tính các chỉ số này thông qua tìm kiếm nhị phân, nhưng với sự trợ giúp của các giá trị đã được tính trước, chúng ta có thể chỉ cần tra cứu chúng trong $O(1)$. 
Và chúng ta có thể lặp lại điều đó cho đến khi chúng ta đã truy cập tất cả các nút bao phủ khoảng truy vấn của chúng ta. 

Tóm lại, như thường lệ, chúng ta chạm vào $O(\log n)$ nút trong một truy vấn. Trong nút gốc, chúng ta thực hiện một tìm kiếm nhị phân, và trong tất cả các nút khác, chúng ta chỉ thực hiện công việc không đổi. 
Điều này có nghĩa là độ phức tạp để trả lời một truy vấn là $O(\log n)$. 

Nhưng lưu ý, rằng điều này sử dụng bộ nhớ gấp ba lần so với một Cây sắp xếp trộn thông thường, vốn đã sử dụng rất nhiều bộ nhớ ($O(n \\log n)$). 

Rất đơn giản để áp dụng kỹ thuật này cho một bài toán không yêu cầu bất kỳ truy vấn sửa đổi nào. 
Hai vị trí chỉ là các số nguyên và có thể dễ dàng được tính toán bằng cách đếm khi hợp nhất hai chuỗi đã được sắp xếp. 

Vẫn có thể cho phép các truy vấn sửa đổi, nhưng điều đó làm phức tạp toàn bộ mã. 
Thay vì các số nguyên, bạn cần lưu trữ mảng đã được sắp xếp dưới dạng `multiset`, và thay vì các chỉ số, bạn cần lưu trữ các trình vòng lặp. 
Và bạn cần làm việc rất cẩn thận, để bạn tăng hoặc giảm các trình vòng lặp chính xác trong một truy vấn sửa đổi. 

#### Các biến thể khác có thể có

Kỹ thuật này ngụ ý một lớp ứng dụng mới có thể có. 
Thay vì lưu trữ một `vector` hoặc `multiset` trong mỗi đỉnh, các cấu trúc dữ liệu khác có thể được sử dụng: 
các Cây phân đoạn khác (được thảo luận phần nào trong [Tổng quát hóa cho các chiều cao hơn](segment_tree.md#generalization-to-higher-dimensions)), Cây Fenwick, cây Cartesian, v.v. 

### Cập nhật trên đoạn (Truyền lười)

Tất cả các bài toán trong các phần trên đã thảo luận về các truy vấn sửa đổi chỉ ảnh hưởng đến một phần tử duy nhất của mảng mỗi lần. 
Tuy nhiên, Cây phân đoạn cho phép áp dụng các truy vấn sửa đổi cho toàn bộ một đoạn các phần tử liên tục, và thực hiện truy vấn trong cùng thời gian $O(\log n)$. 

#### Cộng trên các đoạn

Chúng ta bắt đầu bằng cách xem xét các bài toán ở dạng đơn giản nhất: truy vấn sửa đổi sẽ cộng một số $x$ vào tất cả các số trong đoạn $a[l \dots r]$. 
Truy vấn thứ hai, mà chúng ta phải trả lời, chỉ đơn giản là hỏi giá trị của $a[i]$. 

Để thực hiện truy vấn cộng hiệu quả, chúng ta lưu trữ tại mỗi đỉnh trong Cây phân đoạn số lượng chúng ta nên cộng vào tất cả các số trong đoạn tương ứng. 
Ví dụ, nếu truy vấn "cộng 3 vào toàn bộ mảng $a[0 \dots n-1]$" đến, thì chúng ta đặt số 3 vào gốc của cây. 
Nói chung, chúng ta phải đặt số này vào nhiều đoạn, tạo thành một phân hoạch của đoạn truy vấn. 
Do đó, chúng ta không phải thay đổi tất cả các giá trị $O(n)$, mà chỉ cần thay đổi $O(\log n)$ giá trị. 

Nếu bây giờ có một truy vấn hỏi giá trị hiện tại của một mục mảng cụ thể, chỉ cần đi xuống cây và cộng tất cả các giá trị tìm thấy trên đường đi là đủ. 

```cpp
void build(int a[], int v, int tl, int tr) {
    if (tl == tr) {
        t[v] = a[tl];
    } else {
        int tm = (tl + tr) / 2;
        build(a, v*2, tl, tm);
        build(a, v*2+1, tm+1, tr);
        t[v] = 0;
    }
}

void update(int v, int tl, int tr, int l, int r, int add) {
    if (l > r)
        return;
    if (l == tl && r == tr) {
        t[v] += add;
    } else {
        int tm = (tl + tr) / 2;
        update(v*2, tl, tm, l, min(r, tm), add);
        update(v*2+1, tm+1, tr, max(l, tm+1), r, add);
    }
}

int get(int v, int tl, int tr, int pos) {
    if (tl == tr)
        return t[v];
    int tm = (tl + tr) / 2;
    if (pos <= tm)
        return t[v] + get(v*2, tl, tm, pos);
    else
        return t[v] + get(v*2+1, tm+1, tr, pos);
}
```

#### Gán giá trị trên các đoạn

Giả sử bây giờ truy vấn sửa đổi yêu cầu gán mỗi phần tử của một đoạn nhất định $a[l \dots r]$ cho một giá trị $p$ nào đó. 
Là một truy vấn thứ hai, chúng ta sẽ lại xem xét việc đọc giá trị của mảng $a[i]$. 

Để thực hiện truy vấn sửa đổi này trên toàn bộ một đoạn, bạn phải lưu trữ tại mỗi đỉnh của Cây phân đoạn xem đoạn tương ứng có được bao phủ hoàn toàn bởi cùng một giá trị hay không. 
Điều này cho phép chúng ta thực hiện một cập nhật "lười biếng": 
thay vì thay đổi tất cả các đoạn trong cây bao phủ đoạn truy vấn, chúng ta chỉ thay đổi một số, và để những đoạn khác không thay đổi. 
Một đỉnh được đánh dấu sẽ có nghĩa là mọi phần tử của đoạn tương ứng được gán cho giá trị đó, và thực tế là toàn bộ cây con cũng chỉ nên chứa giá trị này. 
Theo một nghĩa nào đó, chúng ta lười biếng và trì hoãn việc ghi giá trị mới cho tất cả các đỉnh đó. 
Chúng ta có thể thực hiện công việc tẻ nhạt này sau, nếu điều này là cần thiết. 

Vì vậy, sau khi truy vấn sửa đổi được thực hiện, một số phần của cây trở nên không liên quan - một số sửa đổi vẫn chưa được thực hiện trong đó. 

Ví dụ, nếu một truy vấn sửa đổi "gán một số cho toàn bộ mảng $a[0 \dots n-1]$" được thực hiện, trong Cây phân đoạn chỉ có một thay đổi được thực hiện - số được đặt vào gốc của cây và đỉnh này được đánh dấu. 
Các đoạn còn lại vẫn không thay đổi, mặc dù trên thực tế số đó nên được đặt trong toàn bộ cây. 

Giả sử bây giờ truy vấn sửa đổi thứ hai nói rằng, nửa đầu của mảng $a[0 \dots n/2]$ nên được gán với một số khác. 
Để xử lý truy vấn này, chúng ta phải gán mỗi phần tử trong toàn bộ con trái của đỉnh gốc với số đó. 
Nhưng trước khi chúng ta làm điều này, chúng ta phải sắp xếp đỉnh gốc trước. 
Sự tinh tế ở đây là nửa phải của mảng vẫn nên được gán cho giá trị của truy vấn đầu tiên, và tại thời điểm này không có thông tin nào cho nửa phải được lưu trữ. 

Cách giải quyết vấn đề này là đẩy thông tin từ gốc đến các con của nó, tức là nếu gốc của cây được gán với bất kỳ số nào, thì chúng ta gán các đỉnh con trái và phải với số này và xóa dấu của gốc. 
Sau đó, chúng ta có thể gán con trái với giá trị mới, mà không làm mất bất kỳ thông tin cần thiết nào. 

Tóm lại, chúng ta có được: 
đối với bất kỳ truy vấn nào (một truy vấn sửa đổi hoặc đọc), trong quá trình đi xuống cây, chúng ta nên luôn đẩy thông tin từ đỉnh hiện tại vào cả hai con của nó. 
Chúng ta có thể hiểu điều này theo cách, khi chúng ta đi xuống cây, chúng ta áp dụng các sửa đổi bị trì hoãn, nhưng chính xác là đủ (để không làm giảm độ phức tạp của $O(\log n)$). 

Để triển khai, chúng ta cần tạo một hàm `push`, nhận vào đỉnh hiện tại, và nó sẽ đẩy thông tin cho đỉnh của nó đến cả hai con của nó. 
Chúng ta sẽ gọi hàm này ở đầu các hàm truy vấn (nhưng chúng ta sẽ không gọi nó từ các lá, vì không cần đẩy thông tin từ chúng đi xa hơn nữa). 

```cpp
void push(int v) {
    if (marked[v]) {
        t[v*2] = t[v*2+1] = t[v];
        marked[v*2] = marked[v*2+1] = true;
        marked[v] = false;
    }
}

void update(int v, int tl, int tr, int l, int r, int new_val) {
    if (l > r) 
        return;
    if (l == tl && tr == r) {
        t[v] = new_val;
        marked[v] = true;
    } else {
        push(v);
        int tm = (tl + tr) / 2;
        update(v*2, tl, tm, l, min(r, tm), new_val);
        update(v*2+1, tm+1, tr, max(l, tm+1), r, new_val);
    }
}

int get(int v, int tl, int tr, int pos) {
    if (tl == tr) {
        return t[v];
    }
    push(v);
    int tm = (tl + tr) / 2;
    if (pos <= tm) 
        return get(v*2, tl, tm, pos);
    else
        return get(v*2+1, tm+1, tr, pos);
}
```

Lưu ý: hàm `get` cũng có thể được triển khai theo một cách khác: 
không thực hiện các cập nhật bị trì hoãn, mà trả về ngay lập tức giá trị `t[v]` nếu `marked[v]` là true. 

#### Cộng trên các đoạn, truy vấn tìm giá trị lớn nhất

Bây giờ truy vấn sửa đổi là cộng một số vào tất cả các phần tử trong một đoạn, và truy vấn đọc là tìm giá trị lớn nhất trong một đoạn. 

Vì vậy, đối với mỗi đỉnh của Cây phân đoạn, chúng ta phải lưu trữ giá trị lớn nhất của đoạn con tương ứng. 
Phần thú vị là làm thế nào để tính toán lại các giá trị này trong một yêu cầu sửa đổi. 

Vì mục đích này, chúng ta giữ một giá trị bổ sung cho mỗi đỉnh. 
Trong giá trị này, chúng ta lưu trữ các số hạng mà chúng ta chưa truyền cho các đỉnh con. 
Trước khi duyệt đến một đỉnh con, chúng ta gọi `push` và truyền giá trị cho cả hai con. 
Chúng ta phải làm điều này trong cả hàm `update` và hàm `query`. 

```cpp
void build(int a[], int v, int tl, int tr) {
    if (tl == tr) {
        t[v] = a[tl];
    } else {
        int tm = (tl + tr) / 2;
        build(a, v*2, tl, tm);
        build(a, v*2+1, tm+1, tr);
        t[v] = max(t[v*2], t[v*2 + 1]);
    }
}

void push(int v) {
    t[v*2] += lazy[v];
    lazy[v*2] += lazy[v];
    t[v*2+1] += lazy[v];
    lazy[v*2+1] += lazy[v];
    lazy[v] = 0;
}

void update(int v, int tl, int tr, int l, int r, int addend) {
    if (l > r) 
        return;
    if (l == tl && tr == r) {
        t[v] += addend;
        lazy[v] += addend;
    } else {
        push(v);
        int tm = (tl + tr) / 2;
        update(v*2, tl, tm, l, min(r, tm), addend);
        update(v*2+1, tm+1, tr, max(l, tm+1), r, addend);
        t[v] = max(t[v*2], t[v*2+1]);
    }
}

int query(int v, int tl, int tr, int l, int r) {
    if (l > r)
        return -INF;
    if (l == tl && tr == r)
        return t[v];
    push(v);
    int tm = (tl + tr) / 2;
    return max(query(v*2, tl, tm, l, min(r, tm)), 
               query(v*2+1, tm+1, tr, max(l, tm+1), r));
}
```

### Tổng quát hóa cho các chiều cao hơn

Một Cây phân đoạn có thể được tổng quát hóa khá tự nhiên cho các chiều cao hơn. 
Nếu trong trường hợp một chiều, chúng ta chia các chỉ số của mảng thành các đoạn, thì trong trường hợp hai chiều, chúng ta tạo một Cây phân đoạn thông thường đối với các chỉ số đầu tiên, và đối với mỗi đoạn, chúng ta xây dựng một Cây phân đoạn thông thường đối với các chỉ số thứ hai. 

#### Cây phân đoạn 2D đơn giản

Một ma trận $a[0 \dots n-1, 0 \dots m-1]$ được cho, và chúng ta phải tìm tổng (hoặc cực tiểu/cực đại) trên một ma trận con nào đó $a[x_1 \dots x_2, y_1 \dots y_2]$, cũng như thực hiện các sửa đổi của các phần tử ma trận riêng lẻ (tức là các truy vấn có dạng $a[x][y] = p$). 

Vì vậy, chúng ta xây dựng một Cây phân đoạn 2D: đầu tiên là Cây phân đoạn sử dụng tọa độ thứ nhất ($x$), sau đó là tọa độ thứ hai ($y$). 

Để làm cho quá trình xây dựng dễ hiểu hơn, bạn có thể quên một lúc rằng ma trận là hai chiều, và chỉ để lại tọa độ thứ nhất. 
Chúng ta sẽ xây dựng một Cây phân đoạn một chiều thông thường chỉ sử dụng tọa độ thứ nhất. 
Nhưng thay vì lưu trữ một số trong một đoạn, chúng ta lưu trữ toàn bộ một Cây phân đoạn: 
tức là tại thời điểm này, chúng ta nhớ rằng chúng ta cũng có một tọa độ thứ hai; nhưng vì tại thời điểm này tọa độ thứ nhất đã được cố định vào một khoảng nào đó $[l \dots r]$, chúng ta thực sự làm việc với một dải như vậy $a[l \dots r, 0 \dots m-1]$ và đối với nó, chúng ta xây dựng một Cây phân đoạn. 

Đây là việc triển khai xây dựng một Cây phân đoạn 2D. 
Nó thực sự đại diện cho hai khối riêng biệt: 
việc xây dựng một Cây phân đoạn dọc theo tọa độ $x$ (`build_x`), và tọa độ $y$ (`build_y`). 
Đối với các nút lá trong `build_y`, chúng ta phải tách hai trường hợp: 
khi đoạn hiện tại của tọa độ thứ nhất $[tlx \dots trx]$ có độ dài 1, và khi nó có độ dài lớn hơn một. Trong trường hợp đầu tiên, chúng ta chỉ lấy giá trị tương ứng từ ma trận, và trong trường hợp thứ hai, chúng ta có thể kết hợp các giá trị của hai Cây phân đoạn từ con trái và con phải ở tọa độ $x$. 

```cpp
void build_y(int vx, int lx, int rx, int vy, int ly, int ry) {
    if (ly == ry) {
        if (lx == rx)
            t[vx][vy] = a[lx][ly];
        else
            t[vx][vy] = t[vx*2][vy] + t[vx*2+1][vy];
    } else {
        int my = (ly + ry) / 2;
        build_y(vx, lx, rx, vy*2, ly, my);
        build_y(vx, lx, rx, vy*2+1, my+1, ry);
        t[vx][vy] = t[vx][vy*2] + t[vx][vy*2+1];
    }
}

void build_x(int vx, int lx, int rx) {
    if (lx != rx) {
        int mx = (lx + rx) / 2;
        build_x(vx*2, lx, mx);
        build_x(vx*2+1, mx+1, rx);
    }
    build_y(vx, lx, rx, 1, 0, m-1);
}
```

Một Cây phân đoạn như vậy vẫn sử dụng một lượng bộ nhớ tuyến tính, nhưng với một hằng số lớn hơn: $16 n m$. 
Rõ ràng là thủ tục `build_x` được mô tả cũng hoạt động trong thời gian tuyến tính. 

Bây giờ chúng ta chuyển sang xử lý các truy vấn. Chúng ta sẽ trả lời truy vấn hai chiều bằng cùng một nguyên tắc: 
trước tiên chia truy vấn trên tọa độ thứ nhất, và sau đó đối với mỗi đỉnh đã đến, chúng ta gọi Cây phân đoạn tương ứng của tọa độ thứ hai. 

```cpp
int sum_y(int vx, int vy, int tly, int try_, int ly, int ry) {
    if (ly > ry) 
        return 0;
    if (ly == tly && try_ == ry)
        return t[vx][vy];
    int tmy = (tly + try_) / 2;
    return sum_y(vx, vy*2, tly, tmy, ly, min(ry, tmy))
         + sum_y(vx, vy*2+1, tmy+1, try_, max(ly, tmy+1), ry);
}

int sum_x(int vx, int tlx, int trx, int lx, int rx, int ly, int ry) {
    if (lx > rx)
        return 0;
    if (lx == tlx && trx == rx)
        return sum_y(vx, 1, 0, m-1, ly, ry);
    int tmx = (tlx + trx) / 2;
    return sum_x(vx*2, tlx, tmx, lx, min(rx, tmx), ly, ry)
         + sum_x(vx*2+1, tmx+1, trx, max(lx, tmx+1), rx, ly, ry);
}
```

Hàm này hoạt động trong thời gian $O(\log n \\log m)$, vì nó trước tiên đi xuống cây ở tọa độ thứ nhất, và đối với mỗi đỉnh đã duyệt trong cây, nó thực hiện một truy vấn trong Cây phân đoạn tương ứng dọc theo tọa độ thứ hai. 

Cuối cùng, chúng ta xem xét truy vấn sửa đổi. 
Chúng ta muốn học cách sửa đổi Cây phân đoạn theo sự thay đổi giá trị của một phần tử nào đó $a[x][y] = p$. 
Rõ ràng là các thay đổi sẽ chỉ xảy ra ở những đỉnh của Cây phân đoạn thứ nhất bao phủ tọa độ $x$ (và sẽ có $O(\log n)$ đỉnh như vậy), và đối với các Cây phân đoạn tương ứng với chúng, các thay đổi sẽ chỉ xảy ra ở những đỉnh bao phủ tọa độ $y$ (và sẽ có $O(\log m)$ đỉnh như vậy). 
Do đó, việc triển khai sẽ không khác nhiều so với trường hợp một chiều, chỉ bây giờ chúng ta trước tiên đi xuống tọa độ thứ nhất, và sau đó là tọa độ thứ hai. 

```cpp
void update_y(int vx, int lx, int rx, int vy, int ly, int ry, int x, int y, int new_val) {
    if (ly == ry) {
        if (lx == rx)
            t[vx][vy] = new_val;
        else
            t[vx][vy] = t[vx*2][vy] + t[vx*2+1][vy];
    } else {
        int my = (ly + ry) / 2;
        if (y <= my)
            update_y(vx, lx, rx, vy*2, ly, my, x, y, new_val);
        else
            update_y(vx, lx, rx, vy*2+1, my+1, ry, x, y, new_val);
        t[vx][vy] = t[vx][vy*2] + t[vx][vy*2+1];
    }
}

void update_x(int vx, int lx, int rx, int x, int y, int new_val) {
    if (lx != rx) {
        int mx = (lx + rx) / 2;
        if (x <= mx)
            update_x(vx*2, lx, mx, x, y, new_val);
        else
            update_x(vx*2+1, mx+1, rx, x, y, new_val);
    }
    update_y(vx, lx, rx, 1, 0, m-1, x, y, new_val);
}
```

#### Nén Cây phân đoạn 2D

Đặt bài toán như sau: có $n$ điểm trên mặt phẳng được cho bởi tọa độ của chúng $(x_i, y_i)$ và các truy vấn có dạng "đếm số điểm nằm trong hình chữ nhật $((x_1, y_1), (x_2, y_2))$". 
Rõ ràng là trong trường hợp một bài toán như vậy, việc xây dựng một Cây phân đoạn hai chiều với $O(n^2)$ phần tử trở nên lãng phí một cách vô lý. 
Hầu hết bộ nhớ này sẽ bị lãng phí, vì mỗi điểm duy nhất chỉ có thể lọt vào $O(\log n)$ đoạn của cây dọc theo tọa độ thứ nhất, và do đó, kích thước "hữu ích" tổng thể của tất cả các đoạn cây trên tọa độ thứ hai là $O(n \\log n)$. 

Vì vậy, chúng ta tiến hành như sau: 
tại mỗi đỉnh của Cây phân đoạn đối với tọa độ thứ nhất, chúng ta lưu trữ một Cây phân đoạn chỉ được xây dựng bằng những tọa độ thứ hai xuất hiện trong đoạn hiện tại của tọa độ thứ nhất. 
Nói cách khác, khi xây dựng một Cây phân đoạn bên trong một đỉnh nào đó có chỉ số $vx$ và các ranh giới $tlx$ và $trx$, chúng ta chỉ xem xét những điểm rơi vào khoảng này $x \in [tlx, trx]$, và xây dựng một Cây phân đoạn chỉ bằng cách sử dụng chúng. 

Do đó, chúng ta sẽ đạt được rằng mỗi Cây phân đoạn trên tọa độ thứ hai sẽ chiếm đúng lượng bộ nhớ cần thiết. 
Kết quả là, tổng lượng bộ nhớ sẽ giảm xuống còn $O(n \\log n)$. 
Chúng ta vẫn có thể trả lời các truy vấn trong thời gian $O(\log^2 n)$, chúng ta chỉ cần thực hiện một tìm kiếm nhị phân trên tọa độ thứ hai, nhưng điều này sẽ không làm xấu đi độ phức tạp. 

Nhưng các truy vấn sửa đổi sẽ không thể thực hiện được với cấu trúc này: 
trên thực tế, nếu một điểm mới xuất hiện, chúng ta phải thêm một phần tử mới vào giữa một Cây phân đoạn nào đó dọc theo tọa độ thứ hai, điều này không thể được thực hiện một cách hiệu quả. 

Kết luận, chúng ta lưu ý rằng Cây phân đoạn hai chiều được thu gọn theo cách mô tả trở nên thực tế tương đương với việc sửa đổi Cây phân đoạn một chiều (xem [Lưu toàn bộ mảng con trong mỗi đỉnh](segment_tree.md#saving-the-entire-subarrays-in-each-vertex)). 
Cụ thể, Cây phân đoạn hai chiều chỉ là một trường hợp đặc biệt của việc lưu trữ một mảng con trong mỗi đỉnh của cây. 
Từ đó suy ra rằng, nếu bạn phải từ bỏ một Cây phân đoạn hai chiều do không thể thực hiện một truy vấn, có lý khi thử thay thế Cây phân đoạn lồng nhau bằng một cấu trúc dữ liệu mạnh mẽ hơn nào đó, ví dụ như một cây Cartesian. 

### Bảo toàn lịch sử các giá trị của nó (Cây phân đoạn bền bỉ)

Một cấu trúc dữ liệu bền bỉ là một cấu trúc dữ liệu ghi nhớ trạng thái trước đó của nó cho mỗi sửa đổi. 
Điều này cho phép truy cập bất kỳ phiên bản nào của cấu trúc dữ liệu này mà chúng ta quan tâm và thực hiện một truy vấn trên đó. 

Cây phân đoạn là một cấu trúc dữ liệu có thể được biến thành một cấu trúc dữ liệu bền bỉ một cách hiệu quả (cả về thời gian và mức tiêu thụ bộ nhớ). 
Chúng ta muốn tránh việc sao chép toàn bộ cây trước mỗi lần sửa đổi, và chúng ta không muốn mất hành vi thời gian $O(\log n)$ để trả lời các truy vấn trên đoạn. 

Trên thực tế, bất kỳ yêu cầu thay đổi nào trong Cây phân đoạn đều dẫn đến sự thay đổi dữ liệu của chỉ $O(\log n)$ đỉnh dọc theo đường đi bắt đầu từ gốc. 
Vì vậy, nếu chúng ta lưu trữ Cây phân đoạn bằng cách sử dụng con trỏ (tức là một đỉnh lưu trữ các con trỏ đến các đỉnh con trái và phải), thì khi thực hiện truy vấn sửa đổi, chúng ta chỉ cần tạo các đỉnh mới thay vì thay đổi các đỉnh có sẵn. 
Các đỉnh không bị ảnh hưởng bởi truy vấn sửa đổi vẫn có thể được sử dụng bằng cách trỏ các con trỏ đến các đỉnh cũ. 
Do đó, đối với một truy vấn sửa đổi, $O(\log n)$ đỉnh mới sẽ được tạo, bao gồm một đỉnh gốc mới của Cây phân đoạn, và toàn bộ phiên bản trước đó của cây có gốc tại đỉnh gốc cũ sẽ không thay đổi. 

Hãy đưa ra một ví dụ triển khai cho Cây phân đoạn đơn giản nhất: khi chỉ có một truy vấn hỏi tổng, và các truy vấn sửa đổi của các phần tử đơn lẻ. 

```cpp
struct Vertex {
    Vertex *l, *r;
    int sum;

    Vertex(int val) : l(nullptr), r(nullptr), sum(val) {}
    Vertex(Vertex *l, Vertex *r) : l(l), r(r), sum(0) {
        if (l) sum += l->sum;
        if (r) sum += r->sum;
    }
};

Vertex* build(int a[], int tl, int tr) {
    if (tl == tr)
        return new Vertex(a[tl]);
    int tm = (tl + tr) / 2;
    return new Vertex(build(a, tl, tm), build(a, tm+1, tr));
}

int get_sum(Vertex* v, int tl, int tr, int l, int r) {
    if (l > r)
        return 0;
    if (l == tl && tr == r)
        return v->sum;
    int tm = (tl + tr) / 2;
    return get_sum(v->l, tl, tm, l, min(r, tm))
         + get_sum(v->r, tm+1, tr, max(l, tm+1), r);
}

Vertex* update(Vertex* v, int tl, int tr, int pos, int new_val) {
    if (tl == tr)
        return new Vertex(new_val);
    int tm = (tl + tr) / 2;
    if (pos <= tm)
        return new Vertex(update(v->l, tl, tm, pos, new_val), v->r);
    else
        return new Vertex(v->l, update(v->r, tm+1, tr, pos, new_val));
}
```

Đối với mỗi sửa đổi của Cây phân đoạn, chúng ta sẽ nhận được một đỉnh gốc mới. 
Để chuyển đổi nhanh chóng giữa hai phiên bản khác nhau của Cây phân đoạn, chúng ta cần lưu trữ các gốc này trong một mảng. 
Để sử dụng một phiên bản cụ thể của Cây phân đoạn, chúng ta chỉ cần gọi truy vấn bằng cách sử dụng đỉnh gốc thích hợp. 

Với cách tiếp cận được mô tả ở trên, hầu hết mọi Cây phân đoạn đều có thể được biến thành một cấu trúc dữ liệu bền bỉ. 

#### Tìm số nhỏ thứ $k$ trong một đoạn {data-toc-label="Finding the k-th smallest number in a range"} 

Lần này chúng ta phải trả lời các truy vấn có dạng "Số nhỏ thứ $k$ trong đoạn $a[l \dots r]$ là gì. 
Truy vấn này có thể được trả lời bằng tìm kiếm nhị phân và một Cây sắp xếp trộn, nhưng độ phức tạp thời gian cho một truy vấn duy nhất sẽ là $O(\log^3 n)$. 
Chúng ta sẽ hoàn thành cùng một nhiệm vụ bằng cách sử dụng một Cây phân đoạn bền bỉ trong $O(\log n)$. 

Đầu tiên, chúng ta sẽ thảo luận về một giải pháp cho một bài toán đơn giản hơn: 
Chúng ta sẽ chỉ xem xét các mảng trong đó các phần tử bị giới hạn bởi $0 \le a[i] \lt n$. 
Và chúng ta chỉ muốn tìm số nhỏ thứ $k$ trong một tiền tố nào đó của mảng $a$. 
Sẽ rất dễ dàng để mở rộng các ý tưởng đã phát triển sau này cho các mảng không bị giới hạn và các truy vấn trên đoạn không bị giới hạn. 
Lưu ý rằng chúng ta sẽ sử dụng chỉ số bắt đầu từ 1 cho $a$. 

Chúng ta sẽ sử dụng một Cây phân đoạn đếm tất cả các số xuất hiện, tức là trong Cây phân đoạn, chúng ta sẽ lưu trữ biểu đồ tần suất của mảng. 
Vì vậy, các đỉnh lá sẽ lưu trữ số lần các giá trị $0$, $1$, $\dots$, $n-1$ sẽ xuất hiện trong mảng, và các đỉnh khác lưu trữ có bao nhiêu số trong một phạm vi nào đó trong mảng. 
Nói cách khác, chúng ta tạo một Cây phân đoạn thông thường với các truy vấn tổng trên biểu đồ tần suất của mảng. 
Nhưng thay vì tạo tất cả $n$ Cây phân đoạn cho mọi tiền tố có thể, chúng ta sẽ tạo một cây bền bỉ, sẽ chứa cùng một thông tin. 
Chúng ta sẽ bắt đầu với một Cây phân đoạn rỗng (tất cả các số đếm sẽ là $0$) được trỏ bởi $root_0$, và thêm các phần tử $a[1]$, $a[2]$, $\dots$, $a[n]$ lần lượt. 
Đối với mỗi sửa đổi, chúng ta sẽ nhận được một đỉnh gốc mới, hãy gọi $root_i$ là gốc của Cây phân đoạn sau khi chèn $i$ phần tử đầu tiên của mảng $a$. 
Cây phân đoạn có gốc tại $root_i$ sẽ chứa biểu đồ tần suất của tiền tố $a[1 \dots i]$. 
Sử dụng Cây phân đoạn này, chúng ta có thể tìm thấy vị trí của phần tử thứ $k$ trong thời gian $O(\log n)$ bằng cách sử dụng cùng một kỹ thuật đã được thảo luận trong [Đếm số lượng số không, tìm kiếm số không thứ $k$](segment_tree.md#counting-zero-search-kth). 

Bây giờ đến phiên bản không giới hạn của bài toán. 

Đầu tiên đối với giới hạn trên các truy vấn: 
Thay vì chỉ thực hiện các truy vấn này trên một tiền tố của $a$, chúng ta muốn sử dụng bất kỳ đoạn tùy ý nào $a[l \dots r]$. 
Ở đây, chúng ta cần một Cây phân đoạn đại diện cho biểu đồ tần suất của các phần tử trong đoạn $a[l \dots r]$. 
Dễ dàng thấy rằng một Cây phân đoạn như vậy chỉ là sự khác biệt giữa Cây phân đoạn có gốc tại $root_{r}$ và Cây phân đoạn có gốc tại $root_{l-1}$, tức là mọi đỉnh trong Cây phân đoạn $[l \dots r]$ có thể được tính bằng đỉnh của cây $root_{r}$ trừ đi đỉnh của cây $root_{l-1}$. 

Trong triển khai của hàm `find_kth`, điều này có thể được xử lý bằng cách truyền hai con trỏ đỉnh và tính toán số đếm/tổng của đoạn hiện tại dưới dạng hiệu của hai số đếm/tổng của các đỉnh. 

Đây là các hàm `build`, `update`  và `find_kth` đã được sửa đổi 

```{.cpp file=kth_smallest_persistent_segment_tree}
Vertex* build(int tl, int tr) {
    if (tl == tr)
        return new Vertex(0);
    int tm = (tl + tr) / 2;
    return new Vertex(build(tl, tm), build(tm+1, tr));
}

Vertex* update(Vertex* v, int tl, int tr, int pos) {
    if (tl == tr)
        return new Vertex(v->sum+1);
    int tm = (tl + tr) / 2;
    if (pos <= tm)
        return new Vertex(update(v->l, tl, tm, pos), v->r);
    else
        return new Vertex(v->l, update(v->r, tm+1, tr, pos));
}

int find_kth(Vertex* vl, Vertex *vr, int tl, int tr, int k) {
    if (tl == tr)
    	return tl;
    int tm = (tl + tr) / 2, left_count = vr->l->sum - vl->l->sum;
    if (left_count >= k)
    	return find_kth(vl->l, vr->l, tl, tm, k);
    return find_kth(vl->r, vr->r, tm+1, tr, k-left_count);
}
```

Như đã viết ở trên, chúng ta cần lưu trữ gốc của Cây phân đoạn ban đầu, và cả tất cả các gốc sau mỗi lần cập nhật. 
Đây là mã để xây dựng một Cây phân đoạn bền bỉ trên một vector `a` với các phần tử trong phạm vi `[0, MAX_VALUE]`. 

```{.cpp file=kth_smallest_persistent_segment_tree_build}
int tl = 0, tr = MAX_VALUE + 1;
std::vector<Vertex*> roots;
roots.push_back(build(tl, tr));
for (int i = 0; i < a.size(); i++) {
    roots.push_back(update(roots.back(), tl, tr, a[i]));
}

// tìm số nhỏ thứ 5 từ mảng con [a[2], a[3], ..., a[19]]
int result = find_kth(roots[2], roots[20], tl, tr, 5);
```

Bây giờ đến các giới hạn trên các phần tử mảng: 
Chúng ta thực sự có thể biến đổi bất kỳ mảng nào thành một mảng như vậy bằng cách nén chỉ số. 
Phần tử nhỏ nhất trong mảng sẽ được gán giá trị 0, phần tử nhỏ thứ hai giá trị 1, và cứ thế. 
Dễ dàng tạo ra các bảng tra cứu (ví dụ: sử dụng `map`), chuyển đổi một giá trị thành chỉ số của nó và ngược lại trong thời gian $O(\log n)$. 


### Cây phân đoạn động

(Được gọi như vậy vì hình dạng của nó là động và các nút thường được cấp phát động. 
Còn được gọi là _cây phân đoạn ngầm_ hoặc _cây phân đoạn thưa_.) 

Trước đây, chúng ta đã xem xét các trường hợp khi chúng ta có khả năng xây dựng cây phân đoạn ban đầu. Nhưng phải làm gì nếu kích thước ban đầu được lấp đầy bởi một phần tử mặc định nào đó, nhưng kích thước của nó không cho phép bạn xây dựng hoàn toàn trước? 

Chúng ta có thể giải quyết vấn đề này bằng cách tạo một cây phân đoạn một cách lười biếng (tăng dần). Ban đầu, chúng ta sẽ chỉ tạo gốc, và chúng ta sẽ tạo các đỉnh khác chỉ khi chúng ta cần chúng. 
Trong trường hợp này, chúng ta sẽ sử dụng việc triển khai trên các con trỏ (trước khi đi đến các con của đỉnh, hãy kiểm tra xem chúng có được tạo chưa, và nếu chưa, hãy tạo chúng). 
Mỗi truy vấn vẫn chỉ có độ phức tạp $O(\log n)$, đủ nhỏ cho hầu hết các trường hợp sử dụng (ví dụ: $\\log_2 10^9 \\approx 30$). 

Trong triển khai này, chúng ta có hai truy vấn, thêm một giá trị vào một vị trí (ban đầu tất cả các giá trị là $0$), và tính tổng của tất cả các giá trị trong một đoạn. 
`Vertex(0, n)` sẽ là đỉnh gốc của cây ngầm. 

```cpp
struct Vertex {
    int left, right;
    int sum = 0;
    Vertex *left_child = nullptr, *right_child = nullptr;

    Vertex(int lb, int rb) {
        left = lb;
        right = rb;
    }

    void extend() {
        if (!left_child && left + 1 < right) {
            int t = (left + right) / 2;
            left_child = new Vertex(left, t);
            right_child = new Vertex(t, right);
        }
    }

    void add(int k, int x) {
        extend();
        sum += x;
        if (left_child) {
            if (k < left_child->right)
                left_child->add(k, x);
            else
                right_child->add(k, x);
        }
    }

    int get_sum(int lq, int rq) {
        if (lq <= left && right <= rq)
            return sum;
        if (max(left, lq) >= min(right, rq))
            return 0;
        extend();
        return left_child->get_sum(lq, rq) + right_child->get_sum(lq, rq);
    }
};
```

Rõ ràng là ý tưởng này có thể được mở rộng theo nhiều cách khác nhau. Ví dụ: bằng cách thêm hỗ trợ cho các cập nhật trên đoạn thông qua truyền lười. 

## Các bài toán thực hành

* [SPOJ - KQUERY](http://www.spoj.com/problems/KQUERY/) [Cây phân đoạn bền bỉ / Cây sắp xếp trộn]
* [Codeforces - Xenia and Bit Operations](https://codeforces.com/problemset/problem/339/D)
* [UVA 11402 - Ahoy, Pirates!](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2397)
* [SPOJ - GSS3](http://www.spoj.com/problems/GSS3/)
* [Codeforces - Distinct Characters Queries](https://codeforces.com/problemset/problem/1234/D)
* [Codeforces - Knight Tournament](https://codeforces.com/contest/356/problem/A) [Dành cho người mới bắt đầu]
* [Codeforces - Ant colony](https://codeforces.com/contest/474/problem/F)
* [Codeforces - Drazil and Park](https://codeforces.com/contest/515/problem/E)
* [Codeforces - Circular RMQ](https://codeforces.com/problemset/problem/52/C)
* [Codeforces - Lucky Array](https://codeforces.com/contest/121/problem/E)
* [Codeforces - The Child and Sequence](https://codeforces.com/contest/438/problem/D)
* [Codeforces - DZY Loves Fibonacci Numbers](https://codeforces.com/contest/446/problem/C) [Truyền lười]
* [Codeforces - Alphabet Permutations](https://codeforces.com/problemset/problem/610/E)
* [Codeforces - Eyes Closed](https://codeforces.com/problemset/problem/895/E)
* [Codeforces - Kefa and Watch](https://codeforces.com/problemset/problem/580/E)
* [Codeforces - A Simple Task](https://codeforces.com/problemset/problem/558/E)
* [Codeforces - SUM and REPLACE](https://codeforces.com/problemset/problem/920/F)
* [Codeforces - XOR on Segment](https://codeforces.com/problemset/problem/242/E) [Truyền lười]
* [Codeforces - Please, another Queries on Array?](https://codeforces.com/problemset/problem/1114/F) [Truyền lười]
* [COCI - Deda](https://oj.uz/problem/view/COCI17_deda) [Phần tử cuối cùng nhỏ hơn hoặc bằng x / Tìm kiếm nhị phân]
* [Codeforces - The Untended Antiquity](https://codeforces.com/problemset/problem/869/E) [2D]
* [CSES - Hotel Queries](https://cses.fi/problemset/task/1143)
* [CSES - Polynomial Queries](https://cses.fi/problemset/task/1736)
* [CSES - Range Updates and Sums](https://cses.fi/problemset/task/1735)

## Các nguồn khác

* [Cây phân đoạn trên Wikipedia](http://en.wikipedia.org/wiki/Fenwick_tree)
* [Hướng dẫn về cây chỉ số nhị phân trên TopCoder](https://www.topcoder.com/community/data-science/data-science-tutorials/binary-indexed-trees/)
* [Cập nhật và truy vấn trên đoạn ](https://programmingcontests.quora.com/Tutorial-Range-Updates-in-Fenwick-Tree)