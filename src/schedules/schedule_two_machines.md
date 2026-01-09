---
tags:
  - Translated
e_maxx_link: johnson_problem_2
---

# Lập lịch các công việc trên hai máy (Johnson's Rule) (Scheduling jobs on two machines (Johnson's Rule)) {: #scheduling-jobs-on-two-machines-johnsons-rule}

Chúng ta có $n$ công việc. Mỗi công việc gồm hai phần: phần đầu tiên được xử lý trên máy thứ nhất và phần thứ hai được xử lý trên máy thứ hai. Mỗi phần phải được xử lý liên tục (không bị gián đoạn). Đối với mỗi công việc $i$, chúng ta biết thời gian xử lý trên máy thứ nhất $a_i$ và trên máy thứ hai $b_i$. Một máy chỉ có thể xử lý một bộ phận công việc tại một thời điểm. Ngoài ra, máy thứ hai không thể bắt đầu xử lý phần thứ hai của công việc $i$ cho đến khi máy thứ nhất hoàn thành phần đầu tiên của nó.
Chúng ta muốn tìm một lịch trình xử lý các công việc trên hai máy sao cho thời gian hoàn thành tất cả các công việc (makespan) là tối thiểu.

## Thuật toán (Algorithm) {: #algorithm}

Thuật toán cấu tạo này được đề xuất bởi S.M.Johnson vào năm 1954.

Lưu ý rằng chúng ta có thể giả định rằng thứ tự các công việc trên máy thứ nhất và máy thứ hai là giống nhau (việc chứng minh điều này không khó, bằng cách sử dụng phương pháp hoán đổi).
Do đó, chúng ta chỉ cần tìm dãy công việc.

Thuật toán Johnson như sau:

1.  Chia các công việc thành hai nhóm. Nhóm 1 chứa tất cả các công việc sao cho $a_i \le b_i$, và Nhóm 2 chứa tất cả các công việc có $a_i > b_i$.
2.  Sắp xếp các công việc trong Nhóm 1 theo thứ tự tăng dần của $a_i$.
3.  Sắp xếp các công việc trong Nhóm 2 theo thứ tự giảm dần của $b_i$.
4.  Lịch trình tối ưu là sự kết hợp của Nhóm 1 (đã sắp xếp) theo sau là Nhóm 2 (đã sắp xếp).

## Cài đặt (Implementation) {: #implementation}

```cpp
struct Job {
    int a, b, id;

    bool operator<(const Job& o) const {
        return min(a, b) < min(o.a, o.b);
    }
};

vector<Job> johnson_rule(vector<Job> jobs) {
    sort(jobs.begin(), jobs.end());
    vector<Job> a, b;
    for (Job j : jobs) {
        if (j.a < j.b)
            a.push_back(j);
        else
            b.push_back(j);
    }
    a.insert(a.end(), b.rbegin(), b.rend());
    return a;
}
```

## Chứng minh (Proof) {: #proof}

Chúng ta sẽ sử dụng phương pháp hoán đổi.
Gọi $t_i$ và $t'_i$ là thời điểm bắt đầu xử lý công việc thứ $i$ trong lịch trình trên máy 1 và máy 2.
Khi đó thời gian hoàn thành công việc thứ $i$ trên máy 2 là $C_i = t'_i + b_i$.
Tổng thời gian hoàn thành (makespan) là $C_n$.

Chúng ta có các mối quan hệ:
$t_1 = 0$
$t_{i+1} = t_i + a_i$
$t'_1 = a_1$
$t'_{i+1} = \max(t_{i+1} + a_{i+1}, t'_i + b_i) = \max(t_i + a_i + a_{i+1}, t'_i + b_i)$

Hãy xem xét hai công việc liền kề $i$ và $j$ trong lịch trình hiện tại.
Để sự hoán đổi này có lợi, chúng ta cần so sánh thời điểm hoàn thành của công việc thứ hai sau hai công việc này.
Trong thứ tự $(i, j)$:
$C_{ij} = \max(t + a_i + a_j + b_j, t + a_i + b_i + b_j, T + b_i + b_j)$
trong đó $t$ là thời điểm bắt đầu trên máy 1 trước khi xử lý $i$, và $T$ là thời điểm công việc trước đó hoàn thành trên máy 2.
Số hạng $t + a_i + a_j + b_j$ đại diện cho việc chờ máy 1.
Số hạng $t + a_i + b_i + b_j$ và $T + b_i + b_j$ đại diện cho sự chậm trễ tích lũy trên máy 2.

Thực ra, chúng ta có thể đơn giản hóa điều kiện. Johnson đã chứng minh rằng điều kiện tối ưu để xếp $i$ trước $j$ là:
$$\min(a_i, b_j) \le \min(a_j, b_i)$$

Dựa trên bất đẳng thức này:
- Nếu $a_i \le b_i$ (Nhóm 1) và $a_j \le b_j$ (Nhóm 1), thì $a_i \le a_j$. (Sắp xếp tăng dần theo $a$)
- Nếu $a_i > b_i$ (Nhóm 2) và $a_j > b_j$ (Nhóm 2), thì $b_j \le b_i \Rightarrow b_i \ge b_j$. (Sắp xếp giảm dần theo $b$)
- Nếu $i \in$ Nhóm 1 và $j \in$ Nhóm 2, thì $a_i \le b_i$ và $a_j > b_j$. Bất đẳng thức trở thành $\min(a_i, b_j) \le \min(a_j, b_i)$. Điều này luôn đúng vì $\min$ bên trái $\le a_i$ và $\min$ bên phải có thể là $b_i$ (lớn hơn $a_i$) hoặc $a_j$ (thường là lớn).
Chính xác hơn, quy tắc của Johnson tự động thỏa mãn điều kiện này.

## Bài tập (Practice problems) {: #practice-problems}

-   [Codeforces - 3T](http://codeforces.com/problemset/problem/730/G) (Một biến thể khó hơn một chút)
-   [SPOJ - BOOKGFT](http://www.spoj.com/problems/BOOKGFT/)
-   [UVA 11829 - Morning Manager](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=2929)
