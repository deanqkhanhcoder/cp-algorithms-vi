---
tags:
  - Translated
e_maxx_link: maximum_average_segment
---

# Tìm dãy con có tổng lớn nhất/nhỏ nhất (Search the subarray with the maximum/minimum sum) {: #search-the-subarray-with-the-maximum-minimum-sum}

Ở đây, chúng tôi xem xét bài toán tìm một dãy con (mảng con) có tổng lớn nhất, cũng như một số biến thể của nó (bao gồm thuật toán giải bài toán này trực tuyến - online).

## Đề bài (Problem statement) {: #problem-statement}

Cho một mảng các số $a[1 \ldots n]$. Yêu cầu tìm một dãy con $a[l \ldots r]$ có tổng cực đại:

$$ \max_{ 1 \le l \le r \le n } \sum_{i=l}^{r} a[i].$$

Ví dụ, nếu tất cả các số nguyên trong mảng $a[]$ không âm, thì câu trả lời sẽ là chính mảng đó.
Tuy nhiên, lời giải không tầm thường khi mảng có thể chứa cả số dương và số âm.

Rõ ràng là bài toán tìm dãy con **nhỏ nhất** về cơ bản là giống nhau, bạn chỉ cần đổi dấu của tất cả các số.

## Thuật toán 1 (Algorithm 1) {: #algorithm-1}

Ở đây chúng tôi xem xét một thuật toán gần như hiển nhiên. (Tiếp theo, chúng ta sẽ xem xét một thuật toán khác, khó nghĩ ra hơn một chút, nhưng cách cài đặt của nó thậm chí còn ngắn hơn.)

### Mô tả thuật toán (Algorithm description) {: #algorithm-description}

Thuật toán rất đơn giản.

Chúng tôi giới thiệu cho thuận tiện **ký hiệu**: $s[i] = \sum_{j=1}^{i} a[j]$. Tức là, mảng $s[i]$ là một mảng các tổng một phần của mảng $a[]$. Ngoài ra, đặt $s[0] = 0$.

Bây giờ chúng ta hãy lặp lại chỉ số $r = 1 \ldots n$, và tìm hiểu cách nhanh chóng tìm $l$ tối ưu cho mỗi giá trị $r$ hiện tại, tại đó tổng cực đại đạt được trên dãy con $[l, r]$.

Về mặt hình thức, điều này có nghĩa là đối với $r$ hiện tại, chúng ta cần tìm một $l$ (không vượt quá $r$), sao cho giá trị của $s[r] - s[l-1]$ là cực đại. Sau một phép biến đổi tầm thường, chúng ta có thể thấy rằng chúng ta cần tìm trong mảng $s[]$ một giá trị nhỏ nhất trên đoạn $[0, r-1]$.

Từ đây, chúng ta ngay lập tức có được một giải pháp: chúng ta chỉ cần lưu trữ vị trí tối thiểu hiện tại trong mảng $s[]$. Sử dụng giá trị tối thiểu này, chúng ta tìm thấy chỉ số tối ưu hiện tại $l$ trong $O(1)$, và khi chuyển từ chỉ số hiện tại $r$ sang chỉ số tiếp theo, chúng ta chỉ cần cập nhật giá trị tối thiểu này.

Rõ ràng, thuật toán này hoạt động trong $O(n)$ và là tối ưu tiệm cận.

### Cài đặt (Implementation) {: #implementation}

Để cài đặt nó, chúng ta thậm chí không cần lưu trữ rõ ràng một mảng các tổng một phần $s[]$ — chúng ta sẽ chỉ cần phần tử hiện tại từ nó.

Việc cài đặt được đưa ra trong các mảng đánh chỉ số từ 0, không phải trong đánh số từ 1 như được mô tả ở trên.

Đầu tiên chúng tôi đưa ra một giải pháp tìm câu trả lời số đơn giản mà không tìm thấy các chỉ số của đoạn mong muốn:

```cpp
int ans = a[0], sum = 0, min_sum = 0;

for (int r = 0; r < n; ++r) {
    sum += a[r];
    ans = max(ans, sum - min_sum);
    min_sum = min(min_sum, sum);
}
```

Bây giờ chúng tôi đưa ra một phiên bản đầy đủ của giải pháp, trong đó cũng tìm thấy ranh giới của đoạn mong muốn:

```cpp
int ans = a[0], ans_l = 0, ans_r = 0;
int sum = 0, min_sum = 0, min_pos = -1;

for (int r = 0; r < n; ++r) {
    sum += a[r];
    int cur = sum - min_sum;
    if (cur > ans) {
        ans = cur;
        ans_l = min_pos + 1;
        ans_r = r;
    }
    if (sum < min_sum) {
        min_sum = sum;
        min_pos = r;
    }
}
```

## Thuật toán 2 (Algorithm 2) {: #algorithm-2}

Ở đây chúng tôi xem xét một thuật toán khác. Nó khó hiểu hơn một chút, nhưng nó thanh lịch hơn ở trên, và việc cài đặt của nó ngắn hơn một chút. Thuật toán này được đề xuất bởi Jay Kadane vào năm 1984.

### Mô tả thuật toán (Algorithm description) {: #algorithm-description-1}

Bản thân thuật toán như sau. Hãy đi qua mảng và tích lũy tổng một phần hiện tại trong một số biến $s$. Nếu tại một thời điểm nào đó $s$ âm, chúng ta chỉ cần gán $s=0$. Người ta lập luận rằng giá trị lớn nhất trong tất cả các giá trị mà biến $s$ được gán trong thuật toán sẽ là câu trả lời cho bài toán.

**Chứng minh:**

Xem xét chỉ số đầu tiên khi tổng của $s$ trở thành âm. Điều này có nghĩa là bắt đầu với tổng một phần bằng không, cuối cùng chúng ta thu được tổng một phần âm — vì vậy toàn bộ tiền tố này của mảng, cũng như bất kỳ hậu tố nào, đều có tổng âm. Do đó, dãy con này không bao giờ đóng góp vào tổng một phần của bất kỳ dãy con nào mà nó là tiền tố, và có thể đơn giản bị loại bỏ.

Tuy nhiên, điều này không đủ để chứng minh thuật toán. Trong thuật toán, chúng ta thực sự bị giới hạn trong việc tìm câu trả lời chỉ cho các phân đoạn bắt đầu ngay sau những nơi khi $s<0$ xảy ra.

Nhưng, trên thực tế, xem xét một phân đoạn tùy ý $[l, r]$, và $l$ không ở vị trí "quan trọng" như vậy (tức là $l > p+1$, trong đó $p$ là vị trí cuối cùng như vậy, trong đó $s<0$). Vì vị trí quan trọng cuối cùng hoàn toàn sớm hơn $l-1$, hóa ra tổng của $a[p+1 \ldots l-1]$ là không âm. Điều này có nghĩa là bằng cách di chuyển $l$ đến vị trí $p+1$, chúng ta sẽ tăng câu trả lời hoặc, trong trường hợp cực đoan, chúng ta sẽ không thay đổi nó.

Bằng cách này hay cách khác, hóa ra khi tìm kiếm câu trả lời, bạn có thể tự giới hạn mình chỉ trong các phân đoạn bắt đầu ngay sau các vị trí mà $s<0$ xuất hiện. Điều này chứng minh rằng thuật toán là chính xác.

### Cài đặt (Implementation) {: #implementation-1}

Giống như trong thuật toán 1, ban đầu chúng tôi đưa ra một triển khai đơn giản chỉ tìm kiếm câu trả lời số mà không tìm thấy ranh giới của phân đoạn mong muốn:

```cpp
int ans = a[0], sum = 0;

for (int r = 0; r < n; ++r) {
    sum += a[r];
    ans = max(ans, sum);
    sum = max(sum, 0);
}
```

Một giải pháp hoàn chỉnh, duy trì các chỉ số của ranh giới của phân đoạn tương ứng:

```cpp
int ans = a[0], ans_l = 0, ans_r = 0;
int sum = 0, minus_pos = -1;

for (int r = 0; r < n; ++r) {
    sum += a[r];
    if (sum > ans) {
        ans = sum;
        ans_l = minus_pos + 1;
        ans_r = r;
    }
    if (sum < 0) {
        sum = 0;
        minus_pos = r;
    }
}
```

## Các bài toán liên quan (Related tasks) {: #related-tasks}

### Tìm dãy con lớn nhất/nhỏ nhất có ràng buộc (Finding the maximum/minimum subarray with constraints) {: #finding-the-maximum-minimum-subarray-with-constraints}

Nếu điều kiện bài toán áp đặt các hạn chế bổ sung cho phân đoạn $[l, r]$ được yêu cầu (ví dụ, độ dài $r-l+1$ của phân đoạn phải nằm trong giới hạn đã chỉ định), thì thuật toán được mô tả có khả năng dễ dàng khái quát hóa cho các trường hợp này — dù sao, bài toán vẫn sẽ là tìm giá trị nhỏ nhất trong mảng $s[]$ với các hạn chế bổ sung được chỉ định.

### Trường hợp hai chiều của bài toán: tìm kiếm ma trận con lớn nhất/nhỏ nhất (Two-dimensional case of the problem: search for maximum/minimum submatrix) {: #two-dimensional-case-of-the-problem}

Bài toán được mô tả trong bài viết này được khái quát hóa một cách tự nhiên cho các kích thước lớn. Ví dụ, trong trường hợp hai chiều, nó biến thành tìm kiếm ma trận con $[l_1 \ldots r_1, l_2 \ldots r_2]$ của một ma trận đã cho, có tổng các số trong đó là lớn nhất.

Sử dụng giải pháp cho trường hợp một chiều, rất dễ dàng để có được giải pháp trong $O(n^3)$ cho trường hợp hai chiều:
chúng ta lặp qua tất cả các giá trị có thể có của $l_1$ và $r_1$, và tính tổng từ $l_1$ đến $r_1$ trong mỗi hàng của ma trận. Bây giờ chúng ta có bài toán một chiều tìm các chỉ số $l_2$ và $r_2$ trong mảng này, vốn đã có thể được giải quyết trong thời gian tuyến tính.

Các thuật toán **nhanh hơn** để giải quyết vấn đề này đã được biết đến, nhưng chúng không nhanh hơn nhiều so với $O(n^3)$, và rất phức tạp (phức tạp đến mức nhiều trong số chúng kém hơn thuật toán tầm thường đối với tất cả các ràng buộc hợp lý bởi hằng số ẩn). Hiện tại, thuật toán tốt nhất được biết đến hoạt động trong thời gian $O\left(n^3 \frac{ \log^3 \log n }{ \log^2 n} \right)$ (T. Chan 2007 "More algorithms for all-pairs shortest paths in weighted graphs")

Thuật toán này của Chan, cũng như nhiều kết quả khác trong lĩnh vực này, thực sự mô tả **nhân ma trận nhanh** (trong đó nhân ma trận có nghĩa là phép nhân được sửa đổi: minimum được sử dụng thay vì phép cộng, và phép cộng được sử dụng thay vì phép nhân). Bài toán tìm ma trận con có tổng lớn nhất có thể được giảm xuống bài toán tìm đường đi ngắn nhất giữa tất cả các cặp đỉnh, và bài toán này, đến lượt nó, có thể được giảm xuống phép nhân ma trận như vậy.

### Tìm kiếm dãy con có trung bình lớn nhất/nhỏ nhất (Search for a subarray with a maximum/minimum average) {: #search-for-a-subarray-with-a-maximum-minimum-average}

Bài toán này nằm ở việc tìm phân đoạn $a[l, r]$ như vậy, sao cho giá trị trung bình là cực đại:

$$ \max_{l \le r} \frac{ 1 }{ r-l+1 } \sum_{i=l}^{r} a[i].$$

Tất nhiên, nếu không có điều kiện nào khác được áp đặt cho phân đoạn $[l, r]$ được yêu cầu, thì giải pháp sẽ luôn là phân đoạn có độ dài $1$ tại phần tử cực đại của mảng.
Bài toán chỉ có ý nghĩa, nếu có các hạn chế bổ sung (ví dụ, độ dài của phân đoạn mong muốn bị chặn dưới).

Trong trường hợp này, chúng tôi áp dụng **kỹ thuật tiêu chuẩn** khi làm việc với các bài toán về giá trị trung bình: chúng tôi sẽ chọn giá trị trung bình cực đại mong muốn bằng **tìm kiếm nhị phân**.

Để làm điều này, chúng ta cần học cách giải quyết bài toán con sau: cho số $x$, và chúng ta cần kiểm tra xem có dãy con nào của mảng $a[]$ (tất nhiên, thỏa mãn tất cả các ràng buộc bổ sung của bài toán), trong đó giá trị trung bình lớn hơn $x$ hay không.

Để giải quyết bài toán con này, hãy trừ $x$ khỏi mỗi phần tử của mảng $a[]$. Sau đó, bài toán con của chúng ta thực sự biến thành bài toán này: có hay không có các dãy con tổng dương trong mảng này. Và chúng ta đã biết cách giải quyết bài toán này.

Do đó, chúng tôi đã thu được giải pháp cho tiệm cận $O(T(n) \log W)$, trong đó $W$ là độ chính xác cần thiết, $T(n)$ là thời gian giải quyết bài toán con cho một mảng có độ dài $n$ (có thể thay đổi tùy thuộc vào các hạn chế bổ sung cụ thể được áp đặt).

### Giải bài toán trực tuyến (Solving the online problem) {: #solving-the-online-problem}

Điều kiện của bài toán như sau: cho một mảng gồm $n$ số và một số $L$. Có các truy vấn có dạng $(l,r)$, và để trả lời cho mỗi truy vấn, cần tìm một dãy con của đoạn $[l, r]$ có độ dài không nhỏ hơn $L$ với trung bình cộng lớn nhất có thể.

Thuật toán giải bài toán này khá phức tạp. KADR (Yaroslav Tverdokhleb) đã mô tả thuật toán của mình trên [diễn đàn Nga](http://e-maxx.ru/forum/viewtopic.php?id=410).

## Checklist

- [x] Dịch các khái niệm kỹ thuật sang tiếng Việt chính xác.
- [x] Đã cập nhật các liên kết nội bộ (đến 127.0.0.1:8000).
- [x] Định dạng lại các công thức toán học và code block.
- [x] Kiểm tra chính tả và ngữ pháp.
- [x] Đảm bảo tính nhất quán với các thuật ngữ đã dịch khác.
