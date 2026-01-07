---
tags:
  - Original
---

# Giao nửa mặt phẳng

Trong bài viết này, chúng ta sẽ thảo luận về bài toán tính giao của một tập hợp các nửa mặt phẳng. Một giao như vậy có thể được biểu diễn một cách thuận tiện dưới dạng một vùng/đa giác lồi, trong đó mọi điểm bên trong nó cũng nằm bên trong tất cả các nửa mặt phẳng, và chính đa giác này là thứ chúng ta đang cố gắng tìm hoặc xây dựng. Chúng tôi đưa ra một số trực giác ban đầu cho bài toán, mô tả một cách tiếp cận $O(N \log N)$ được gọi là thuật toán Sắp xếp và Tăng dần và đưa ra một số ứng dụng mẫu của kỹ thuật này.

Người đọc được khuyến khích mạnh mẽ nên quen thuộc với các nguyên thủy và phép toán hình học cơ bản (điểm, vector, giao của các đường thẳng). Ngoài ra, kiến thức về [Bao lồi](../geometry/convex-hull.md) hoặc [Mẹo bao lồi](../geometry/convex_hull_trick.md) có thể giúp hiểu rõ hơn các khái niệm trong bài viết này, nhưng chúng không phải là điều kiện tiên quyết.

## Các làm rõ và định nghĩa ban đầu

Trong toàn bộ bài viết, chúng ta sẽ đưa ra một số giả định (trừ khi có quy định khác):

1. Chúng ta định nghĩa $N$ là số lượng nửa mặt phẳng trong tập hợp đã cho.
2. Chúng ta sẽ biểu diễn các đường thẳng và nửa mặt phẳng bằng một điểm và một vector (bất kỳ điểm nào nằm trên đường thẳng đã cho và vector chỉ phương của đường thẳng). Trong trường hợp nửa mặt phẳng, chúng ta giả định rằng mỗi nửa mặt phẳng cho phép vùng ở phía bên trái của vector chỉ phương của nó. Ngoài ra, chúng ta định nghĩa góc của một nửa mặt phẳng là góc cực của vector chỉ phương của nó. Xem hình ảnh dưới đây để biết ví dụ.
3. Chúng ta sẽ giả định rằng giao kết quả luôn là một vùng bị chặn hoặc rỗng. Nếu chúng ta cần xử lý trường hợp không bị chặn, chúng ta có thể chỉ cần thêm 4 nửa mặt phẳng xác định một hộp giới hạn đủ lớn. 
4. Chúng ta sẽ giả định, để đơn giản, rằng không có nửa mặt phẳng song song trong tập hợp đã cho. Về cuối bài viết, chúng ta sẽ thảo luận cách đối phó với các trường hợp như vậy.

![](halfplanes_rep.png) 

Nửa mặt phẳng $y \geq 2x - 2$ có thể được biểu diễn bằng điểm $P = (1, 0)$ với vector chỉ phương $PQ = Q - P = (1, 2)$

## Cách tiếp cận vét cạn - $O(N^3)$ {data-toc-label="Brute force approach - O(N^3)"}

Một trong những giải pháp đơn giản và rõ ràng nhất là tính toán điểm giao của các đường thẳng của tất cả các cặp nửa mặt phẳng và, đối với mỗi điểm, kiểm tra xem nó có nằm bên trong tất cả các nửa mặt phẳng khác không. Vì có $O(N^2)$ điểm giao, và đối với mỗi điểm trong số đó, chúng ta phải kiểm tra $O(N)$ nửa mặt phẳng, tổng độ phức tạp thời gian là $O(N^3)$. Vùng giao thực tế sau đó có thể được tái tạo bằng cách sử dụng, ví dụ, một thuật toán Bao lồi trên tập hợp các điểm giao nằm trong tất cả các nửa mặt phẳng. 

Khá dễ hiểu tại sao điều này hoạt động: các đỉnh của đa giác lồi kết quả đều là các điểm giao của các đường thẳng của nửa mặt phẳng, và mỗi đỉnh đó rõ ràng là một phần của tất cả các nửa mặt phẳng. Ưu điểm chính của phương pháp này là nó dễ hiểu, dễ nhớ và dễ viết mã nhanh nếu bạn chỉ cần kiểm tra xem giao có rỗng hay không. Tuy nhiên, nó rất chậm và không phù hợp với hầu hết các bài toán, vì vậy chúng ta cần một cái gì đó nhanh hơn.

## Cách tiếp cận tăng dần - $O(N^2)$ {data-toc-label="Incremental approach - O(N^2)"}

Một cách tiếp cận khá đơn giản khác là xây dựng giao của các nửa mặt phẳng một cách tăng dần, mỗi lần một nửa mặt phẳng. Phương pháp này về cơ bản tương đương với việc cắt một đa giác lồi bằng một đường thẳng $N$ lần, và loại bỏ các nửa mặt phẳng dư thừa ở mỗi bước. Để làm điều này, chúng ta có thể biểu diễn đa giác lồi dưới dạng một danh sách các đoạn thẳng, và để cắt nó bằng một nửa mặt phẳng, chúng ta chỉ cần tìm các điểm giao của các đoạn thẳng với đường thẳng của nửa mặt phẳng (sẽ chỉ có hai điểm giao nếu đường thẳng cắt đúng đa giác), và thay thế tất cả các đoạn thẳng ở giữa bằng đoạn thẳng mới tương ứng với nửa mặt phẳng. Vì một thủ tục như vậy có thể được thực hiện trong thời gian tuyến tính, chúng ta có thể chỉ cần bắt đầu với một hộp giới hạn lớn và cắt nó xuống bằng mỗi nửa mặt phẳng, thu được tổng độ phức tạp thời gian là $O(N^2)$.

Phương pháp này là một bước tiến lớn đúng hướng, nhưng cảm thấy lãng phí khi phải lặp qua $O(N)$ nửa mặt phẳng ở mỗi bước. Tiếp theo, chúng ta sẽ thấy rằng, bằng cách đưa ra một số quan sát thông minh, các ý tưởng đằng sau cách tiếp cận tăng dần này có thể được tái sử dụng để tạo ra một thuật toán $O(N \log N)$.

## Thuật toán Sắp xếp và Tăng dần - $O(N \log N)$ {data-toc-label="Sort-and-Incremental algorithm - O(N log N)"}

Nguồn tài liệu đầu tiên được ghi chép đúng cách về thuật toán này mà chúng tôi có thể tìm thấy là luận án của Zeyuan Zhu cho Cuộc thi Chọn đội tuyển Trung Quốc có tựa đề [Thuật toán mới cho Giao nửa mặt phẳng và Giá trị thực tiễn của nó](http://people.csail.mit.edu/zeyuan/publications.htm), từ năm 2006. Cách tiếp cận mà chúng tôi sẽ mô tả tiếp theo dựa trên cùng một thuật toán này, nhưng thay vì tính toán hai giao riêng biệt cho nửa trên và nửa dưới của các giao, chúng tôi sẽ xây dựng tất cả cùng một lúc trong một lần duyệt bằng một deque (hàng đợi hai đầu).

Bản thân thuật toán, như tên gọi có thể tiết lộ, tận dụng thực tế là vùng kết quả từ giao của các nửa mặt phẳng là lồi, và do đó nó sẽ bao gồm một số đoạn của các nửa mặt phẳng theo thứ tự được sắp xếp theo góc của chúng. Điều này dẫn đến một quan sát quan trọng: nếu chúng ta giao dần các nửa mặt phẳng theo thứ tự được sắp xếp theo góc của chúng (như chúng sẽ xuất hiện trong hình dạng cuối cùng, kết quả của giao) và lưu trữ chúng trong một hàng đợi hai đầu, thì chúng ta sẽ chỉ cần loại bỏ các nửa mặt phẳng từ phía trước và phía sau của deque.

Để hình dung rõ hơn thực tế này, giả sử chúng ta đang thực hiện cách tiếp cận tăng dần được mô tả trước đó trên một tập hợp các nửa mặt phẳng được sắp xếp theo góc (trong trường hợp này, chúng ta sẽ giả định chúng được sắp xếp từ $-\pi$ đến $\pi$), và giả sử rằng chúng ta sắp bắt đầu một bước thứ $k$ tùy ý nào đó. Điều này có nghĩa là chúng ta đã xây dựng giao của $k-1$ nửa mặt phẳng đầu tiên. Bây giờ, bởi vì các nửa mặt phẳng được sắp xếp theo góc, bất kể nửa mặt phẳng thứ $k$ là gì, chúng ta có thể chắc chắn rằng nó sẽ tạo thành một khúc cua lồi với nửa mặt phẳng thứ $(K-1)$. Vì lý do đó, một vài điều có thể xảy ra:

1. Một số (có thể không có) nửa mặt phẳng ở phía sau của giao có thể trở nên *dư thừa*. Trong trường hợp này, chúng ta cần phải lấy ra các nửa mặt phẳng vô dụng này từ phía sau của deque. 
2. Một số (có thể không có) nửa mặt phẳng ở phía trước có thể trở nên *dư thừa*. Tương tự như trường hợp 1, chúng ta chỉ cần lấy chúng ra từ phía trước của deque.
3. Giao có thể trở nên rỗng (sau khi xử lý các trường hợp 1 và/hoặc 2). Trong trường hợp này, chúng ta chỉ cần báo cáo giao là rỗng và kết thúc thuật toán.

*Chúng ta nói một nửa mặt phẳng là "dư thừa" nếu nó không đóng góp gì cho giao. Một nửa mặt phẳng như vậy có thể được loại bỏ và giao kết quả sẽ không thay đổi chút nào.*

Đây là một ví dụ nhỏ với một hình minh họa:

Đặt $H = \{ A, B, C, D, E \}$ là tập hợp các nửa mặt phẳng hiện có trong giao. Ngoài ra, đặt $P = \{ p, q, r, s \}$ là tập hợp các điểm giao của các nửa mặt phẳng liền kề trong H. Bây giờ, giả sử chúng ta muốn giao nó với nửa mặt phẳng $F$, như được thấy trong hình minh họa dưới đây:

![](halfplanes_hp1.png)

Lưu ý nửa mặt phẳng $F$ làm cho $A$ và $E$ trở nên dư thừa trong giao. Vì vậy, chúng ta loại bỏ cả $A$ và $E$ lần lượt từ phía trước và phía sau của giao, và thêm $F$ vào cuối. Và cuối cùng chúng ta có được giao mới $H = \{ B, C, D, F\}$ với $P = \{ q, r, t, u \}$.

![](halfplanes_hp2.png)

Với tất cả những điều này, chúng ta có gần như mọi thứ chúng ta cần để thực sự triển khai thuật toán, nhưng chúng ta vẫn cần nói về một số trường hợp đặc biệt. Ở đầu bài viết, chúng tôi đã nói rằng chúng tôi sẽ thêm một hộp giới hạn để xử lý các trường hợp giao có thể không bị chặn, vì vậy trường hợp khó duy nhất mà chúng ta thực sự cần xử lý là các nửa mặt phẳng song song. Chúng ta có thể có hai trường hợp con: hai nửa mặt phẳng có thể song song với cùng một hướng hoặc với hướng ngược lại. Lý do trường hợp này cần được xử lý riêng là vì chúng ta sẽ cần tính các điểm giao của các đường thẳng của nửa mặt phẳng để có thể kiểm tra xem một nửa mặt phẳng có dư thừa hay không, và hai đường thẳng song song không có điểm giao, vì vậy chúng ta cần một cách đặc biệt để đối phó với chúng.

Đối với trường hợp các nửa mặt phẳng song song có hướng ngược lại: Lưu ý rằng, bởi vì chúng ta đang thêm hộp giới hạn để đối phó với trường hợp không bị chặn, điều này cũng giải quyết trường hợp chúng ta có hai nửa mặt phẳng song song liền kề có hướng ngược lại sau khi sắp xếp, vì sẽ phải có ít nhất một trong các nửa mặt phẳng của hộp giới hạn ở giữa hai nửa mặt phẳng này (hãy nhớ chúng được sắp xếp theo góc). 

 * Tuy nhiên, có thể xảy ra trường hợp, sau khi loại bỏ một số nửa mặt phẳng từ phía sau của deque, hai nửa mặt phẳng song song có hướng ngược lại lại đứng cạnh nhau. Trường hợp này chỉ xảy ra, cụ thể là khi hai nửa mặt phẳng này tạo thành một giao rỗng, vì nửa mặt phẳng cuối cùng này sẽ khiến mọi thứ bị loại bỏ khỏi deque. Để tránh vấn đề này, chúng ta phải kiểm tra thủ công các nửa mặt phẳng song song, và nếu chúng có hướng ngược lại, chúng ta chỉ cần dừng thuật toán ngay lập tức và trả về một giao rỗng.


Do đó, trường hợp duy nhất mà chúng ta thực sự cần xử lý là có nhiều nửa mặt phẳng có cùng một góc, và hóa ra trường hợp này khá dễ xử lý: chúng ta chỉ cần giữ lại nửa mặt phẳng ngoài cùng bên trái và xóa phần còn lại, vì chúng sẽ hoàn toàn dư thừa.
Tóm lại, thuật toán đầy đủ sẽ gần như trông như sau:

1. Chúng ta bắt đầu bằng cách sắp xếp tập hợp các nửa mặt phẳng theo góc, mất thời gian $O(N \log N)$.
2. Chúng ta sẽ lặp qua tập hợp các nửa mặt phẳng, và đối với mỗi nửa mặt phẳng, chúng ta sẽ thực hiện thủ tục tăng dần, lấy ra từ phía trước và phía sau của hàng đợi hai đầu khi cần thiết. Điều này sẽ mất tổng cộng thời gian tuyến tính, vì mỗi nửa mặt phẳng chỉ có thể được thêm hoặc xóa một lần.
3. Cuối cùng, đa giác lồi kết quả từ giao có thể được thu được đơn giản bằng cách tính các điểm giao của các nửa mặt phẳng liền kề trong deque ở cuối thủ tục. Điều này cũng sẽ mất thời gian tuyến tính. Cũng có thể lưu trữ các điểm như vậy trong bước 2 và bỏ qua hoàn toàn bước này, nhưng chúng tôi tin rằng việc tính toán chúng một cách nhanh chóng sẽ dễ hơn một chút (về mặt triển khai).

Tổng cộng, chúng ta đã đạt được độ phức tạp thời gian là $O(N \log N)$. Vì việc sắp xếp rõ ràng là nút thắt cổ chai, thuật toán có thể được thực hiện để chạy trong thời gian tuyến tính trong trường hợp đặc biệt khi chúng ta được cho các nửa mặt phẳng được sắp xếp trước theo góc của chúng (một ví dụ về một trường hợp như vậy là thu được các nửa mặt phẳng xác định một đa giác lồi). 

### Triển khai trực tiếp

Đây là một mẫu, triển khai trực tiếp của thuật toán, với các bình luận giải thích hầu hết các phần: 

Các cấu trúc điểm/vector và nửa mặt phẳng đơn giản:

```cpp
// Định nghĩa lại epsilon và vô cực nếu cần. Cẩn thận với lỗi chính xác.
const long double eps = 1e-9, inf = 1e9; 

// Cấu trúc điểm/vector cơ bản.
struct Point { 

    long double x, y;
    explicit Point(long double x = 0, long double y = 0) : x(x), y(y) {}

    // Phép cộng, trừ, nhân với hằng số, tích vô hướng, tích có hướng.

    friend Point operator + (const Point& p, const Point& q) {
        return Point(p.x + q.x, p.y + q.y); 
    }

    friend Point operator - (const Point& p, const Point& q) { 
        return Point(p.x - q.x, p.y - q.y); 
    }

    friend Point operator * (const Point& p, const long double& k) { 
        return Point(p.x * k, p.y * k); 
    } 
    
    friend long double dot(const Point& p, const Point& q) {
    	return p.x * q.x + p.y * q.y;
    }

    friend long double cross(const Point& p, const Point& q) { 
        return p.x * q.y - p.y * q.x; 
    }
};

// Cấu trúc nửa mặt phẳng cơ bản.
struct Halfplane { 

    // 'p' là một điểm đi qua của đường thẳng và 'pq' là vector chỉ phương của đường thẳng.
    Point p, pq; 
    long double angle;

    Halfplane() {}
    Halfplane(const Point& a, const Point& b) : p(a), pq(b - a) {
        angle = atan2l(pq.y, pq.x);    
    }

    // Kiểm tra xem điểm 'r' có nằm ngoài nửa mặt phẳng này không. 
    // Mỗi nửa mặt phẳng cho phép vùng ở bên TRÁI của đường thẳng của nó.
    bool out(const Point& r) { 
        return cross(pq, r - p) < -eps; 
    }

    // Hàm so sánh để sắp xếp. 
    bool operator < (const Halfplane& e) const { 
        return angle < e.angle;
    } 

    // Điểm giao của các đường thẳng của hai nửa mặt phẳng. Giả định rằng chúng không bao giờ song song.
    friend Point inter(const Halfplane& s, const Halfplane& t) {
        long double alpha = cross((t.p - s.p), t.pq) / cross(s.pq, t.pq);
        return s.p + (s.pq * alpha);
    }
};
```

Thuật toán: 

```cpp
// Thuật toán thực tế
vector<Point> hp_intersect(vector<Halfplane>& H) { 

    Point box[4] = {  // Hộp giới hạn theo thứ tự ngược chiều kim đồng hồ
        Point(inf, inf), 
        Point(-inf, inf), 
        Point(-inf, -inf), 
        Point(inf, -inf) 
    };

    for(int i = 0; i<4; i++) { // Thêm các nửa mặt phẳng của hộp giới hạn.
        Halfplane aux(box[i], box[(i+1) % 4]);
        H.push_back(aux);
    }

    // Sắp xếp theo góc và bắt đầu thuật toán
    sort(H.begin(), H.end());
    deque<Halfplane> dq;
    int len = 0;
    for(int i = 0; i < int(H.size()); i++) {

        // Xóa khỏi phía sau của deque khi nửa mặt phẳng cuối cùng là dư thừa
        while (len > 1 && H[i].out(inter(dq[len-1], dq[len-2]))) {
            dq.pop_back();
            --len;
        }

        // Xóa khỏi phía trước của deque khi nửa mặt phẳng đầu tiên là dư thừa
        while (len > 1 && H[i].out(inter(dq[0], dq[1]))) {
            dq.pop_front();
            --len;
        }
        
        // Kiểm tra trường hợp đặc biệt: Các nửa mặt phẳng song song
        if (len > 0 && fabsl(cross(H[i].pq, dq[len-1].pq)) < eps) {
        	// Các nửa mặt phẳng song song ngược hướng được kiểm tra với nhau.
        	if (dot(H[i].pq, dq[len-1].pq) < 0.0)
        		return vector<Point>();
        	
        	// Nửa mặt phẳng cùng hướng: chỉ giữ lại nửa mặt phẳng ngoài cùng bên trái.
        	if (H[i].out(dq[len-1].p)) {
        		dq.pop_back();
        		--len;
        	}
        	else continue;
        }
        
        // Thêm nửa mặt phẳng mới
        dq.push_back(H[i]);
        ++len;
    }

    // Dọn dẹp cuối cùng: Kiểm tra các nửa mặt phẳng ở phía trước so với phía sau và ngược lại
    while (len > 2 && dq[0].out(inter(dq[len-1], dq[len-2]))) {
        dq.pop_back();
        --len;
    }

    while (len > 2 && dq[len-1].out(inter(dq[0], dq[1]))) {
        dq.pop_front();
        --len;
    }

    // Báo cáo giao rỗng nếu cần
    if (len < 3) return vector<Point>();

    // Tái tạo đa giác lồi từ các nửa mặt phẳng còn lại.
    vector<Point> ret(len);
    for(int i = 0; i+1 < len; i++) {
        ret[i] = inter(dq[i], dq[i+1]);
    }
    ret.back() = inter(dq[len-1], dq[0]);
    return ret;
}
```


### Thảo luận về triển khai

Một điều đặc biệt cần lưu ý là, trong trường hợp có nhiều nửa mặt phẳng giao nhau tại cùng một điểm, thì thuật toán này có thể trả về các điểm liền kề lặp lại trong đa giác cuối cùng. Tuy nhiên, điều này không ảnh hưởng đến việc đánh giá đúng xem giao có rỗng hay không, và nó cũng không ảnh hưởng đến diện tích đa giác. Bạn có thể muốn loại bỏ các bản sao này tùy thuộc vào các nhiệm vụ bạn cần làm sau đó. Bạn có thể làm điều này rất dễ dàng với std::unique. Chúng tôi muốn giữ các điểm lặp lại trong quá trình thực hiện thuật toán để các giao có diện tích bằng không có thể được tính toán chính xác (ví dụ, các giao bao gồm một điểm, đường thẳng hoặc đoạn thẳng duy nhất). Tôi khuyến khích người đọc thử một số trường hợp nhỏ tự tạo trong đó giao kết quả là một điểm hoặc đường thẳng duy nhất.

Một điều nữa cần nói đến là phải làm gì nếu chúng ta được cho các nửa mặt phẳng dưới dạng một ràng buộc tuyến tính (ví dụ, $ax + by + c \leq 0$). Trong trường hợp đó, có hai lựa chọn. Bạn có thể triển khai thuật toán với các sửa đổi tương ứng để hoạt động với biểu diễn như vậy (về cơ bản là tạo cấu trúc nửa mặt phẳng của riêng bạn, sẽ khá đơn giản nếu bạn quen thuộc với mẹo bao lồi), hoặc bạn có thể chuyển đổi các đường thẳng thành biểu diễn mà chúng ta đã sử dụng trong bài viết này bằng cách lấy 2 điểm bất kỳ của mỗi đường thẳng. Nói chung, nên làm việc với biểu diễn mà bạn được cho trong bài toán để tránh các vấn đề về độ chính xác bổ sung.

## Các bài toán, nhiệm vụ và ứng dụng

Nhiều bài toán có thể được giải quyết bằng giao nửa mặt phẳng cũng có thể được giải quyết mà không cần nó, nhưng với các cách tiếp cận (thường) phức tạp hoặc không phổ biến hơn. Nói chung, giao nửa mặt phẳng có thể xuất hiện khi xử lý các bài toán liên quan đến đa giác (chủ yếu là lồi), tầm nhìn trên mặt phẳng và quy hoạch tuyến tính hai chiều. Dưới đây là một số nhiệm vụ mẫu có thể được giải quyết bằng kỹ thuật này: 

### Giao đa giác lồi 

Một trong những ứng dụng cổ điển của giao nửa mặt phẳng: Cho $N$ đa giác, tính toán vùng nằm bên trong tất cả các đa giác. 

Vì giao của một tập hợp các nửa mặt phẳng là một đa giác lồi, chúng ta cũng có thể biểu diễn một đa giác lồi dưới dạng một tập hợp các nửa mặt phẳng (mỗi cạnh của đa giác là một đoạn của một nửa mặt phẳng). Tạo các nửa mặt phẳng này cho mọi đa giác và tính toán giao của toàn bộ tập hợp. Tổng độ phức tạp thời gian là $O(S \log S)$, trong đó S là tổng số cạnh của tất cả các đa giác. Bài toán cũng có thể được giải quyết về mặt lý thuyết trong $O(S \log N)$ bằng cách hợp nhất $N$ tập hợp các nửa mặt phẳng bằng cách sử dụng một đống và sau đó chạy thuật toán mà không có bước sắp xếp, nhưng một giải pháp như vậy có hệ số hằng số tệ hơn nhiều so với sắp xếp thẳng và chỉ cung cấp lợi ích tốc độ nhỏ đối với $N$ rất nhỏ.

### Tầm nhìn trong mặt phẳng

Các bài toán yêu cầu một cái gì đó trong số các dòng "xác định xem một số đoạn thẳng có thể nhìn thấy từ một số điểm trên mặt phẳng hay không" thường có thể được xây dựng thành các bài toán giao nửa mặt phẳng. Lấy ví dụ, nhiệm vụ sau: Cho một đa giác đơn (không nhất thiết phải lồi), xác định xem có bất kỳ điểm nào bên trong đa giác sao cho toàn bộ biên của đa giác có thể được quan sát từ điểm đó hay không. Điều này còn được gọi là tìm [nhân của một đa giác](https://en.wikipedia.org/wiki/Star-shaped_polygon) và có thể được giải quyết bằng giao nửa mặt phẳng đơn giản, lấy mỗi cạnh của đa giác làm một nửa mặt phẳng và sau đó tính toán giao của nó.

Đây là một bài toán liên quan, thú vị hơn được Artem Vasilyev trình bày trong một trong những [bài giảng tại Trường hè ICPC Brazil](https://youtu.be/WKyZSitpm6M?t=6463): 
Cho một tập hợp $p$ gồm các điểm $p_1, p_2\ \dots \ p_n$ trên mặt phẳng, xác định xem có bất kỳ điểm $q$ nào bạn có thể đứng tại đó sao cho bạn có thể nhìn thấy tất cả các điểm của $p$ từ trái sang phải theo thứ tự tăng dần của chỉ số của chúng.

Một bài toán như vậy có thể được giải quyết bằng cách nhận thấy rằng việc có thể nhìn thấy một điểm $p_i$ nào đó ở bên trái của $p_j$ cũng giống như việc có thể nhìn thấy phía bên phải của đoạn thẳng từ $p_i$ đến $p_j$ (hoặc tương đương, có thể nhìn thấy phía bên trái của đoạn thẳng từ $p_j$ đến $p_i$). Với ý nghĩ đó, chúng ta có thể chỉ cần tạo một nửa mặt phẳng cho mỗi đoạn thẳng $p_i p_{i+1}$ (hoặc $p_{i+1} p_i$ tùy thuộc vào hướng bạn chọn) và kiểm tra xem giao của toàn bộ tập hợp có rỗng hay không.

### Giao nửa mặt phẳng với tìm kiếm nhị phân

Một ứng dụng phổ biến khác là sử dụng giao nửa mặt phẳng như một công cụ để xác thực vị từ của một thủ tục tìm kiếm nhị phân. Dưới đây là một ví dụ về một bài toán như vậy, cũng được Artem Vasilyev trình bày trong cùng một bài giảng đã được đề cập trước đó: Cho một đa giác **lồi** $P$, tìm chu vi lớn nhất có thể được nội tiếp bên trong nó.

Thay vì tìm kiếm một loại giải pháp dạng đóng nào đó, các công thức khó chịu hoặc các giải pháp thuật toán tối nghĩa, hãy thử tìm kiếm nhị phân trên câu trả lời. Lưu ý rằng, đối với một $r$ cố định, một đường tròn có bán kính $r$ có thể được nội tiếp bên trong $P$ chỉ khi tồn tại một điểm nào đó bên trong $P$ có khoảng cách lớn hơn hoặc bằng $r$ đến tất cả các điểm của biên của $P$. Điều kiện này có thể được xác thực bằng cách "thu hẹp" đa giác vào trong một khoảng cách là $r$ và kiểm tra xem đa giác có còn không suy biến hay không (hoặc là một điểm/đoạn thẳng). Một thủ tục như vậy có thể được mô phỏng bằng cách lấy các nửa mặt phẳng của các cạnh của đa giác theo thứ tự ngược chiều kim đồng hồ, tịnh tiến mỗi nửa mặt phẳng một khoảng cách là $r$ theo hướng của vùng mà chúng cho phép (tức là, vuông góc với vector chỉ phương của nửa mặt phẳng), và kiểm tra xem giao có rỗng hay không.

Rõ ràng, nếu chúng ta có thể nội tiếp một đường tròn bán kính $r$, chúng ta cũng có thể nội tiếp bất kỳ đường tròn nào khác có bán kính nhỏ hơn $r$. Vì vậy, chúng ta có thể thực hiện một tìm kiếm nhị phân trên bán kính $r$ và xác thực mỗi bước bằng cách sử dụng giao nửa mặt phẳng. Ngoài ra, lưu ý rằng các nửa mặt phẳng của một đa giác lồi đã được sắp xếp theo góc, vì vậy bước sắp xếp có thể được bỏ qua trong thuật toán. Do đó, chúng ta có được tổng độ phức tạp thời gian là $O(NK)$, trong đó $N$ là số đỉnh của đa giác và $K$ là số lần lặp của tìm kiếm nhị phân (giá trị thực tế sẽ phụ thuộc vào phạm vi các câu trả lời có thể có và độ chính xác mong muốn).

### Quy hoạch tuyến tính hai chiều

Một ứng dụng nữa của giao nửa mặt phẳng là quy hoạch tuyến tính trong hai biến. Tất cả các ràng buộc tuyến tính cho hai biến có thể được biểu diễn dưới dạng $Ax + By + C \leq 0$ (toán tử so sánh bất đẳng thức có thể thay đổi). Rõ ràng, đây chỉ là các nửa mặt phẳng, vì vậy việc kiểm tra xem một giải pháp khả thi có tồn tại cho một tập hợp các ràng buộc tuyến tính hay không có thể được thực hiện bằng giao nửa mặt phẳng. Ngoài ra, đối với một tập hợp các ràng buộc tuyến tính đã cho, có thể tính toán vùng các giải pháp khả thi (tức là giao của các nửa mặt phẳng) và sau đó trả lời nhiều truy vấn tối đa hóa/tối thiểu hóa một số hàm tuyến tính $f(x, y)$ tuân theo các ràng buộc trong $O(\log N)$ cho mỗi truy vấn bằng cách sử dụng tìm kiếm nhị phân (rất giống với mẹo bao lồi).

Điều đáng nói là cũng tồn tại một thuật toán ngẫu nhiên khá đơn giản có thể kiểm tra xem một tập hợp các ràng buộc tuyến tính có một giải pháp khả thi hay không, và tối đa hóa/tối thiểu hóa một số hàm tuyến tính tuân theo các ràng buộc đã cho. Thuật toán ngẫu nhiên này cũng đã được Artem Vasilyev giải thích một cách hay trong bài giảng đã đề cập trước đó. Dưới đây là một số tài liệu bổ sung về nó, nếu người đọc quan tâm: [CG - Bài giảng 4, phần 4 và 5](https://youtu.be/5dfc355t2y4) và [Blog của Petr Mitrichev (bao gồm giải pháp cho bài toán khó nhất trong danh sách các bài toán thực hành dưới đây)](https://petr-mitrichev.blogspot.com/2016/07/a-half-plane-week.html).

## Các bài toán thực hành

### Các bài toán cổ điển, ứng dụng trực tiếp

* [Codechef - Animesh decides to settle down](https://www.codechef.com/problems/CHN02)
* [POJ - How I mathematician Wonder What You Are!](http://poj.org/problem?id=3130)
* [POJ - Rotating Scoreboard](http://poj.org/problem?id=3335)
* [POJ - Video Surveillance](http://poj.org/problem?id=1474)
* [POJ - Art Gallery](http://poj.org/problem?id=1279)
* [POJ - Uyuw's Concert](http://poj.org/problem?id=2451)

### Các bài toán khó hơn

* [POJ - Most Distant Point from the Sea - Trung bình](http://poj.org/problem?id=3525)
* [Baekjoon - Jeju's Island - Tương tự như trên nhưng có vẻ như các trường hợp kiểm thử mạnh hơn](https://www.acmicpc.net/problem/3903)
* [POJ - Feng Shui - Trung bình](http://poj.org/problem?id=3384)
* [POJ - Triathlon - Trung bình/khó](http://poj.org/problem?id=1755)
* [DMOJ - Arrow - Trung bình/khó](https://dmoj.ca/problem/ccoprep3p3)
* [POJ - Jungle Outpost - Khó](http://poj.org/problem?id=3968)
* [Codeforces - Jungle Outpost (liên kết thay thế, bài toán J) - Khó](https://codeforces.com/gym/101309/attachments?mobile=false) 
* [Yandex - Asymmetry Value (cần có cuộc thi ảo để xem, bài toán F) - Rất khó](https://contest.yandex.com/contest/2540/enter/)

### Các bài toán bổ sung

* Trại lập trình Petrozavodsk lần thứ 40, mùa đông năm 2021 - Ngày 1: Cuộc thi Jagiellonian U, Grand Prix of Krakow - Bài toán B: (Almost) Fair Cake-Cutting. Tại thời điểm viết bài, bài toán này là riêng tư và chỉ có thể truy cập bởi những người tham gia Trại lập trình.

## Tài liệu tham khảo, thư mục và các nguồn khác

### Các nguồn chính

* [Thuật toán mới cho Giao nửa mặt phẳng và Giá trị thực tiễn của nó.](http://people.csail.mit.edu/zeyuan/publications.htm) Bài báo gốc của thuật toán.
* [Bài giảng tại Trường hè ICPC Brazil 2020 của Artem Vasilyev.](https://youtu.be/WKyZSitpm6M?t=6463) Bài giảng tuyệt vời về giao nửa mặt phẳng. Cũng bao gồm các chủ đề hình học khác.

### Các blog hay (tiếng Trung)

* [Cơ sở của Hình học tính toán - Giao của các nửa mặt phẳng.](https://zhuanlan.zhihu.com/p/83499723)
* [Giới thiệu chi tiết về thuật toán giao nửa mặt phẳng.](https://blog.csdn.net/qq_40861916/article/details/83541403)
* [Tóm tắt các bài toán giao nửa mặt phẳng.](https://blog.csdn.net/qq_40482358/article/details/87921815)
* [Phương pháp tăng dần sắp xếp của giao nửa mặt phẳng.](https://blog.csdn.net/u012061345/article/details/23872929)

### Thuật toán ngẫu nhiên

* [Quy hoạch tuyến tính và Giao nửa mặt phẳng - Phần 4 và 5.](https://youtu.be/5dfc355t2y4)
* [Blog của Petr Mitrichev: Một tuần nửa mặt phẳng.](https://petr-mitrichev.blogspot.com/2016/07/a-half-plane-week.html)