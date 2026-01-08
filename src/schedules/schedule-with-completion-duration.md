---
tags:
  - Translated
e_maxx_link: scheduling_jobs_completion_duration
---

# Lập lịch công việc trên một máy với thời gian hoàn thành và thời gian thực hiện khác nhau (Scheduling jobs on one machine with different completion times and execution times) {: #scheduling-jobs-on-one-machine-with-different-completion-times-and-execution-times}

Chúng ta có $n$ công việc. Mỗi công việc $i$ được đặc trưng bởi thời gian thực hiện $t_i$ và thời gian hoàn thành $l_i$. Chúng ta có một máy để xử lý các công việc này và máy này chỉ có thể xử lý một công việc tại một thời điểm (kết thúc công việc này rồi mới bắt đầu công việc khác). Việc thực hiện công việc $j$ bao gồm hai phần: đầu tiên máy xử lý nó trong thời gian $t_j$, sau đó, ngay sau khi xử lý xong, công việc $j$ tiếp tục được thực hiện trong $l_j$ thời gian "một cách độc lập" (không cần máy).
(Ví dụ: chúng ta có một số bộ phận bằng kim loại được đúc trên máy, và sau khi đúc, chúng cần được làm nguội).

Chúng ta muốn tìm một lịch trình thực hiện các công việc trên máy sao cho thời gian trôi qua để tất cả các công việc được hoàn thành hoàn toàn (cả hai phần của mỗi công việc đều xong) là tối thiểu.

## Giải pháp (Solution) {: #solution}

Thời gian hoàn thành cho một công việc thứ $i$ được tính bằng tổng thời gian thực hiện của nó và tất cả các công việc được lên lịch trước nó, cộng với thời gian hoàn thành của nó $l_i$.
Gọi $p$ là một hoán vị của các chỉ số (indexes) mô tả lịch trình dự kiến. Khi đó thời gian để công việc $p_i$ được hoàn thành là:

$$ ans_i = \left( \sum_{j=1}^i t_{p_j} \right) + l_{p_i} $$

Và chúng ta muốn giảm thiểu giá trị tối đa của $ans_i$:

$$ \min_p \max_{i=1 \dots n} ans_i $$

Dễ thấy rằng thời gian hoàn thành $l_{p_i}$ đóng vai trò quan trọng trong biểu thức này: phần tổng $\sum t_{p_j}$ giống nhau cho tất cả các công việc tại vị trí $i$ và các vị trí sau đó, nhưng $l_{p_i}$ chỉ ảnh hưởng đến chính công việc $p_i$.
Đường như chúng ta nên đặt các công việc có $l_i$ lớn ở đầu lịch trình, để chúng có thể hoàn thành phần độc lập của mình trong khi máy đang bận xử lý các công việc khác.

Thật vậy, đây là chiến lược tối ưu: chúng ta nên **sắp xếp các công việc theo thứ tự giảm dần của $l_i$** và thực hiện chúng theo thứ tự đó.

Chúng ta có thể chứng minh tính tối ưu của giải pháp này bằng phương pháp hoán đổi (exchange argument); hãy xem phần tiếp theo để biết chứng minh chung cho các vấn đề lập lịch trình thuộc loại này.

## Checklist

- [x] Dịch các khái niệm kỹ thuật sang tiếng Việt chính xác.
- [x] Đã cập nhật các liên kết nội bộ (đến 127.0.0.1:8000).
- [x] Định dạng lại các công thức toán học và code block.
- [x] Kiểm tra chính tả và ngữ pháp.
- [x] Đảm bảo tính nhất quán với các thuật ngữ đã dịch khác.
