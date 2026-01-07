---
tags:
  - Translated
e_maxx_link: flow_with_limits
---

# Luồng có yêu cầu

Trong một mạng luồng thông thường, luồng của một cạnh chỉ bị giới hạn bởi khả năng thông qua $c(e)$ từ phía trên và bởi 0 từ phía dưới.
Trong bài viết này, chúng ta sẽ thảo luận về các mạng luồng, trong đó chúng ta còn yêu cầu luồng của mỗi cạnh phải có một lượng nhất định, tức là chúng ta giới hạn luồng từ phía dưới bằng một hàm **yêu cầu** $d(e)$:

$$ d(e) \le f(e) \le c(e)$$

Vì vậy, tiếp theo mỗi cạnh có một giá trị luồng tối thiểu, mà chúng ta phải đi qua cạnh đó.

Đây là một sự tổng quát hóa của bài toán luồng thông thường, vì việc đặt $d(e) = 0$ cho tất cả các cạnh $e$ sẽ cho một mạng luồng thông thường.
Lưu ý, trong mạng luồng thông thường, việc tìm một luồng hợp lệ là cực kỳ tầm thường, chỉ cần đặt $f(e) = 0$ đã là một luồng hợp lệ.
Tuy nhiên, nếu luồng của mỗi cạnh phải thỏa mãn một yêu cầu, thì việc tìm một luồng hợp lệ đột nhiên trở nên khá phức tạp.

Chúng ta sẽ xem xét hai bài toán:

1. tìm một luồng bất kỳ thỏa mãn tất cả các ràng buộc
2. tìm một luồng tối thiểu thỏa mãn tất cả các ràng buộc

## Tìm một luồng bất kỳ

Chúng ta thực hiện các thay đổi sau trong mạng.
Chúng ta thêm một nguồn mới $s'$ và một đích mới $t'$, một cạnh mới từ nguồn $s'$ đến mọi đỉnh khác, một cạnh mới từ mọi đỉnh đến đích $t'$, và một cạnh từ $t$ đến $s$.
Ngoài ra, chúng ta định nghĩa hàm khả năng thông qua mới $c'$ như sau:

- $c'((s', v)) = \sum_{u \in V} d((u, v))$ cho mỗi cạnh $(s', v)$.
- $c'((v, t')) = \sum_{w \in V} d((v, w))$ cho mỗi cạnh $(v, t')$.
- $c'((u, v)) = c((u, v)) - d((u, v))$ cho mỗi cạnh $(u, v)$ trong mạng cũ.
- $c'((t, s)) = \infty$

Nếu mạng mới có một luồng bão hòa (một luồng trong đó mỗi cạnh đi ra từ $s'$ được lấp đầy hoàn toàn, tương đương với mỗi cạnh đi vào $t'$ được lấp đầy hoàn toàn), thì mạng có yêu cầu có một luồng hợp lệ, và luồng thực tế có thể được tái tạo dễ dàng từ mạng mới.
Ngược lại, không tồn tại một luồng thỏa mãn tất cả các điều kiện.
Vì một luồng bão hòa phải là một luồng cực đại, nó có thể được tìm thấy bằng bất kỳ thuật toán luồng cực đại nào, như thuật toán [Edmonds-Karp](edmonds_karp.md) hoặc thuật toán [Đẩy-nhãn lại](push-relabel.md).

Tính đúng đắn của những biến đổi này khó hiểu hơn.
Chúng ta có thể nghĩ về nó theo cách sau:
Mỗi cạnh $e = (u, v)$ với $d(e) > 0$ ban đầu được thay thế bằng hai cạnh: một với khả năng thông qua $d(i)$, và cạnh kia với $c(i) - d(i)$.
Chúng ta muốn tìm một luồng làm bão hòa cạnh đầu tiên (tức là luồng dọc theo cạnh này phải bằng khả năng thông qua của nó).
Cạnh thứ hai ít quan trọng hơn - luồng dọc theo nó có thể là bất cứ thứ gì, miễn là nó không vượt quá khả năng thông qua của nó.
Xem xét mỗi cạnh phải được bão hòa, và chúng ta thực hiện thao tác sau:
chúng ta vẽ cạnh từ nguồn mới $s'$ đến đầu cuối của nó là $v$, vẽ cạnh từ đầu bắt đầu của nó là $u$ đến đích mới $t'$, loại bỏ chính cạnh đó, và từ đích cũ $t$ đến nguồn cũ $s$, chúng ta vẽ một cạnh có khả năng thông qua vô hạn.
Bằng những hành động này, chúng ta mô phỏng thực tế rằng cạnh này được bão hòa - từ $v$ sẽ có một luồng $d(e)$ bổ sung đi ra (chúng ta mô phỏng nó bằng một nguồn mới cung cấp lượng luồng phù hợp cho $v$), và $u$ cũng sẽ đẩy một luồng bổ sung $d(e)$ (nhưng thay vì dọc theo cạnh cũ, luồng này sẽ đi trực tiếp đến đích mới $t'$).
Một luồng có giá trị $d(e)$, ban đầu chảy dọc theo đường đi $s - \dots - u - v - \dots t$ bây giờ có thể đi theo đường đi mới $s' - v - \dots - t - s - \dots - u - t'$.
Điều duy nhất được đơn giản hóa trong định nghĩa của mạng mới, là nếu thủ tục tạo ra nhiều cạnh giữa cùng một cặp đỉnh, thì chúng được kết hợp thành một cạnh duy nhất với khả năng thông qua được cộng lại.

## Luồng tối thiểu

Lưu ý rằng dọc theo cạnh $(t, s)$ (từ đích cũ đến nguồn cũ) với khả năng thông qua $\infty$, toàn bộ luồng của mạng cũ tương ứng sẽ chảy qua.
Tức là, khả năng thông qua của cạnh này ảnh hưởng đến giá trị luồng của mạng cũ.
Bằng cách cho cạnh này một khả năng thông qua đủ lớn (tức là $\infty$), luồng của mạng cũ không bị giới hạn.
Bằng cách giới hạn cạnh này bằng các khả năng thông qua nhỏ hơn, giá trị luồng sẽ giảm.
Tuy nhiên, nếu chúng ta giới hạn cạnh này bằng một giá trị quá nhỏ, thì mạng sẽ không có giải pháp bão hòa, ví dụ: giải pháp tương ứng cho mạng ban đầu sẽ không thỏa mãn yêu cầu của các cạnh.
Rõ ràng ở đây có thể sử dụng một tìm kiếm nhị phân để tìm giá trị thấp nhất mà tất cả các ràng buộc vẫn được thỏa mãn.
Điều này cho luồng tối thiểu của mạng ban đầu.