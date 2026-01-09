---
tags:
  - Translated
e_maxx_link: flow_with_limits
---

# Luồng với các nhu cầu (Flows with demands) {: #flows-with-demands}

Trong một mạng luồng bình thường, luồng của một cạnh chỉ bị giới hạn bởi dung lượng $c(e)$ từ phía trên và bởi 0 từ phía dưới.
Trong bài viết này, chúng ta sẽ thảo luận về các mạng luồng, trong đó chúng ta yêu cầu thêm luồng của mỗi cạnh phải có một lượng nhất định, tức là chúng ta chặn luồng từ phía dưới bởi một hàm **nhu cầu** (demand) $d(e)$:

$$ d(e) \le f(e) \le c(e)$$

Vì vậy, tiếp theo mỗi cạnh có một giá trị luồng tối thiểu, mà chúng ta phải chuyển dọc theo cạnh.

Đây là một sự tổng quát hóa của bài toán luồng bình thường, vì việc đặt $d(e) = 0$ cho tất cả các cạnh $e$ mang lại một mạng luồng bình thường.
Lưu ý rằng, trong mạng luồng bình thường, việc tìm một luồng hợp lệ là cực kỳ tầm thường, chỉ cần đặt $f(e) = 0$ đã là một luồng hợp lệ.
Tuy nhiên, nếu luồng của mỗi cạnh phải thỏa mãn một nhu cầu, thì việc tìm một luồng hợp lệ đột nhiên đã là khá phức tạp.

Chúng ta sẽ xem xét hai bài toán:

1.  tìm một luồng bất kỳ thỏa mãn tất cả các ràng buộc
2.  tìm một luồng cực tiểu thỏa mãn tất cả các ràng buộc

## Tìm một luồng bất kỳ (Finding an arbitrary flow) {: #finding-an-arbitrary-flow}

Chúng ta thực hiện các thay đổi sau trong mạng.
Chúng ta thêm một nguồn mới $s'$ và một đích mới $t'$, một cạnh mới từ nguồn $s'$ đến mọi đỉnh khác, một cạnh mới cho mọi đỉnh đến đích $t'$, và một cạnh từ $t$ đến $s$.
Ngoài ra chúng ta định nghĩa hàm dung lượng mới $c'$ như sau:

- $c'((s', v)) = \sum_{u \in V} d((u, v))$ cho mỗi cạnh $(s', v)$.
- $c'((v, t')) = \sum_{w \in V} d((v, w))$ cho mỗi cạnh $(v, t')$.
- $c'((u, v)) = c((u, v)) - d((u, v))$ cho mỗi cạnh $(u, v)$ trong mạng cũ.
- $c'((t, s)) = \infty$

Nếu mạng mới có một luồng bão hòa (một luồng trong đó mỗi cạnh đi ra từ $s'$ được lấp đầy hoàn toàn, tương đương với mọi cạnh đi vào $t'$ được lấp đầy hoàn toàn), thì mạng với nhu cầu có một luồng hợp lệ, và luồng thực tế có thể dễ dàng được xây dựng lại từ mạng mới.
Nếu không thì không tồn tại một luồng thỏa mãn tất cả các điều kiện.
Vì một luồng bão hòa phải là một luồng cực đại, nó có thể được tìm thấy bởi bất kỳ thuật toán luồng cực đại nào, như [thuật toán Edmonds-Karp](edmonds-karp.md) hoặc [thuật toán Push-relabel](push-relabel.md).

Tính đúng đắn của những biến đổi này khó hiểu hơn.
Chúng ta có thể nghĩ về nó theo cách sau:
Mỗi cạnh $e = (u, v)$ với $d(e) > 0$ ban đầu được thay thế bằng hai cạnh: một cạnh có dung lượng $d(i)$ , và cạnh kia có dung lượng $c(i) - d(i)$.
Chúng ta muốn tìm một luồng bão hòa cạnh đầu tiên (tức là luồng dọc theo cạnh này phải bằng dung lượng của nó).
Cạnh thứ hai ít quan trọng hơn - luồng dọc theo nó có thể là bất cứ thứ gì, giả sử rằng nó không vượt quá dung lượng của nó.
Xem xét mỗi cạnh phải được bão hòa, và chúng ta thực hiện thao tác sau:
chúng ta vẽ cạnh từ nguồn mới $s'$ đến điểm cuối $v$ của nó, vẽ cạnh từ điểm bắt đầu $u$ của nó đến đích mới $t'$, xóa cạnh đó, và từ đích cũ $t$ đến nguồn cũ $s$ chúng ta vẽ một cạnh có dung lượng vô hạn.
Bằng những hành động này, chúng ta mô phỏng thực tế rằng cạnh này được bão hòa - từ $v$ sẽ có thêm luồng $d(e)$ đi ra (chúng ta mô phỏng nó bằng một nguồn mới cung cấp lượng luồng phù hợp cho $v$), và $u$ cũng sẽ đẩy thêm luồng $d(e)$ (nhưng thay vì dọc theo cạnh cũ, luồng này sẽ đi trực tiếp đến đích mới $t'$).
Một luồng với giá trị $d(e)$, ban đầu chảy dọc theo đường đi $s - \dots - u - v - \dots t$ bây giờ có thể đi theo đường đi mới $s' - v - \dots - t - s - \dots - u - t'$.
Điều duy nhất được đơn giản hóa trong định nghĩa của mạng mới, là nếu thủ tục tạo ra nhiều cạnh giữa cùng một cặp đỉnh, thì chúng được kết hợp thành một cạnh duy nhất với dung lượng tổng.

## Luồng cực tiểu (Minimal flow) {: #minimal-flow}

Lưu ý rằng dọc theo cạnh $(t, s)$ (từ đích cũ đến nguồn cũ) với dung lượng $\infty$ chảy toàn bộ luồng của mạng cũ tương ứng.
Tức là dung lượng của cạnh này ảnh hưởng đến giá trị luồng của mạng cũ.
Bằng cách cho cạnh này một dung lượng đủ lớn (tức là $\infty$), luồng của mạng cũ là không giới hạn.
Bằng cách giới hạn cạnh này bởi các dung lượng nhỏ hơn, giá trị luồng sẽ giảm.
Tuy nhiên, nếu chúng ta giới hạn cạnh này bởi một giá trị quá nhỏ, thì mạng sẽ không có giải pháp bão hòa, ví dụ: giải pháp tương ứng cho mạng ban đầu sẽ không thỏa mãn nhu cầu của các cạnh.
Rõ ràng ở đây có thể sử dụng tìm kiếm nhị phân để tìm giá trị thấp nhất mà tất cả các ràng buộc vẫn được thỏa mãn.
Điều này mang lại luồng cực tiểu của mạng ban đầu.
