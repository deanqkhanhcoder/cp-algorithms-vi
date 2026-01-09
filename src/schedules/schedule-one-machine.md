---
tags:
  - Translated
e_maxx_link: johnson_problem_1
---

# Lập lịch các công việc trên một máy (Scheduling jobs on one machine) {: #scheduling-jobs-on-one-machine}

Chúng ta có một tập hợp các công việc và một máy có thể thực hiện tất cả các công việc đó.
Chúng ta được cho một hàm mục tiêu mà chúng ta muốn tối thiểu hóa.
Các tiêu chí phổ biến nhất là:

-   Tối thiểu hóa **tổng thời gian hoàn thành** $\sum C_i$ trong đó $C_i$ là thời gian hoàn thành của công việc $i$.
-   Tối thiểu hóa **tổng thời gian hoàn thành có trọng số** $\sum w_i C_i$ trong đó $w_i$ là độ ưu tiên của công việc $i$.
-   Tối thiểu hóa **thời gian hoàn thành tối đa** $\max C_i$ (makespan).
-   Tối thiểu hóa **độ trễ tối đa** $L_{max} = \max (C_i - d_i)$, trong đó $d_i$ là thời hạn (deadline) của công việc $i$.

Ở đây $C_i$ là thời gian mà tại đó việc xử lý công việc $i$ đã kết thúc.

## Tổng thời gian hoàn thành (Total completion time) {: #total-completion-time}

Chúng ta có $n$ công việc với thời gian xử lý $t_1, \dots, t_n$.
Chúng ta muốn tối thiểu hóa $\sum C_i$.

Để giải quyết vấn đề này, hãy xem xét trường hợp hai công việc.
Nếu chúng ta thực hiện công việc đầu tiên trước, thì $C_1 = t_1$ và $C_2 = t_1 + t_2$. Tổng thời gian hoàn thành là $2 t_1 + t_2$.
Nếu chúng ta thực hiện công việc thứ hai trước, thì $C_2 = t_2$ và $C_1 = t_1 + t_2$. Tổng thời gian hoàn thành là $2 t_2 + t_1$.

Rõ ràng là tốt hơn nên chọn công việc có thời gian xử lý nhỏ hơn trước.
Mở rộng cho $n$ công việc, chúng ta có thể thấy rằng thứ tự tối ưu đạt được bằng cách sắp xếp các công việc theo $t_i$ không giảm.

## Tổng thời gian hoàn thành có trọng số (Weighted total completion time) {: #weighted-total-completion-time}

Chúng ta có $n$ công việc với thời gian xử lý $t_1, \dots, t_n$ và trọng số $w_1, \dots, w_n$.
Chúng ta muốn tối thiểu hóa $\sum w_i C_i$.

Hãy xem xét lại trường hợp hai công việc.
Nếu chúng ta thực hiện công việc đầu tiên trước, thì chi phí là $w_1 t_1 + w_2 (t_1 + t_2) = (w_1 + w_2) t_1 + w_2 t_2$.
Nếu chúng ta thực hiện công việc thứ hai trước, thì chi phí là $w_2 t_2 + w_1 (t_1 + t_2) = (w_1 + w_2) t_2 + w_1 t_1$.

Lịch trình đầu tiên tốt hơn nếu
$$(w_1 + w_2) t_1 + w_2 t_2 < (w_1 + w_2) t_2 + w_1 t_1$$
$$\iff w_2 t_1 < w_1 t_2$$
$$\iff \frac{t_1}{w_1} < \frac{t_2}{w_2}$$

Do đó, đối với bất kỳ số lượng công việc nào, thứ tự tối ưu đạt được bằng cách sắp xếp các công việc theo tỷ lệ $\frac{t_i}{w_i}$ không giảm.

## Thời gian hoàn thành tối đa (Maximum completion time) {: #maximum-completion-time}

Bất kể thứ tự thực hiện các công việc như thế nào, thời gian hoàn thành tối đa sẽ luôn là $\sum t_i$.
Do đó, bất kỳ thứ tự nào cũng là tối ưu.

## Độ trễ tối đa (Maximum lateness) {: #maximum-lateness}

Chúng ta có $n$ công việc với thời gian xử lý $t_1, \dots, t_n$ và thời hạn $d_1, \dots, d_n$.
Chúng ta muốn tối thiểu hóa $L_{max} = \max (C_i - d_i)$.

Đối với bài toán này, thứ tự tối ưu đạt được bằng cách sắp xếp các công việc theo thời hạn $d_i$ không giảm.
Thuật toán này được gọi là **Quy tắc Earliest Due Date (EDD)**.

Hãy chứng minh điều này bằng cách sử dụng **phương pháp hoán đổi (exchange argument)** (đây là kỹ thuật chứng minh tiêu chuẩn cho các thuật toán tham lam).
Giả sử chúng ta có một lịch trình tối ưu không tuân theo quy tắc EDD.
Khi đó, phải tồn tại hai công việc liên tiếp $i$ và $j$ sao cho $d_i > d_j$, nhưng công việc $i$ được lên lịch trước công việc $j$.
Hãy hoán đổi hai công việc này và xem điều gì sẽ xảy ra với độ trễ tối đa.

Gọi $t$ là thời điểm bắt đầu xử lý công việc $i$ trong lịch trình ban đầu.
Trong lịch trình ban đầu:
$C_i = t + t_i$
$C_j = t + t_i + t_j$
$L_i = C_i - d_i$
$L_j = C_j - d_j$
Độ trễ tối đa cục bộ $L = \max(L_i, L_j)$.

Sau khi hoán đổi:
$C'_j = t + t_j$
$C'_i = t + t_j + t_i$
$L'_j = C'_j - d_j$
$L'_i = C'_i - d_i$
Độ trễ tối đa cục bộ $L' = \max(L'_j, L'_i)$.

Bây giờ chúng ta cần chứng minh $L' \le L$.
Rõ ràng là $C'_j < C_i < C_j = C'_i$.
Từ $C'_j < C_j$ suy ra $L'_j < L_j \le L$.
Bây giờ chúng ta cần so sánh $L'_i$ với $L$.
$L'_i = C'_i - d_i = C_j - d_i$.
Vì $d_i > d_j$, chúng ta có $C_j - d_i < C_j - d_j = L_j \le L$.
Vì vậy, cả $L'_j$ và $L'_i$ đều nhỏ hơn hoặc bằng $L$, điều đó có nghĩa là $L' \le L$.

Điều này ngụ ý rằng việc hoán đổi không làm tăng độ trễ tối đa.
Bằng cách lặp lại thực hiện các hoán đổi như vậy, chúng ta có thể chuyển bất kỳ lịch trình tối ưu nào thành lịch trình được sắp xếp theo EDD mà không làm giảm chất lượng giải pháp.

## Bài tập (Practice problems) {: #practice-problems}

-   [CSES : Tasks and Deadlines](https://cses.fi/problemset/task/1630)
