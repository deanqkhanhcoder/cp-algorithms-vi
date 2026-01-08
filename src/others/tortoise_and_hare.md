---
tags:
  - Translated
e_maxx_link: tortoise_and_hare
---

# Thuật toán tìm chu trình trong danh sách liên kết của Floyd (Floyd's Linked List Cycle Finding Algorithm) {: #floyds-linked-list-cycle-finding-algorithm}

Cho một danh sách liên kết trong đó điểm bắt đầu của danh sách liên kết đó được ký hiệu là **head**, và có thể có hoặc không có chu trình. Ví dụ:

<div style="text-align: center;">
  <img src="tortoise_hare_algo.png" alt="Linked list with cycle">
</div>

Ở đây chúng ta cần tìm điểm **C**, tức là điểm bắt đầu của chu trình.

## Thuật toán đề xuất (Proposed algorithm) {: #proposed-algorithm}
Thuật toán này được gọi là **Thuật toán chu trình Floyd (Floyd’s Cycle Algorithm)** hoặc **Thuật toán Rùa và Thỏ (Tortoise And Hare algorithm)**.
Để tìm ra điểm bắt đầu của chu trình, chúng ta cần tìm xem chu trình có tồn tại hay không.
Điều này bao gồm hai bước:
1. Tìm ra sự hiện diện của chu trình.
2. Tìm ra điểm bắt đầu của chu trình.

### Bước 1: Sự hiện diện của chu trình (Step 1: Presence of the cycle) {: #step-1-presence-of-the-cycle}
1. Lấy hai con trỏ $slow$ (chậm) và $fast$ (nhanh).
2. Ban đầu cả hai sẽ trỏ đến head của danh sách liên kết.
3. $slow$ sẽ di chuyển từng bước một.
4. $fast$ sẽ di chuyển hai bước một lúc. (tốc độ gấp đôi con trỏ $slow$).
5. Kiểm tra xem liệu tại bất kỳ thời điểm nào chúng có trỏ đến cùng một nút trước khi bất kỳ ai (hoặc cả hai) chạm tới null hay không.
6. Nếu chúng trỏ đến cùng một nút tại bất kỳ điểm nào trong hành trình của chúng, điều đó cho thấy rằng một chu trình thực sự tồn tại trong danh sách liên kết.
7. Nếu chúng ta nhận được null, điều đó cho thấy danh sách liên kết không có chu trình.

<div style="text-align: center;">
  <img src="tortoise_hare_cycle_found.png" alt="Found cycle">
</div>

Bây giờ chúng ta đã tìm ra nếu có một chu trình hiện diện trong danh sách liên kết, bước tiếp theo chúng ta cần tìm ra điểm bắt đầu của chu trình, tức là **C**.

### Bước 2: Điểm bắt đầu của chu trình (Step 2: Starting point of the cycle) {: #step-2-starting-point-of-the-cycle}
1. Đặt lại con trỏ $slow$ về **head** của danh sách liên kết.
2. Di chuyển cả hai con trỏ từng bước một.
3. Điểm mà chúng gặp nhau sẽ là điểm bắt đầu của chu trình.

```java
// Presence of cycle
public boolean hasCycle(ListNode head) {
    ListNode slow = head;
    ListNode fast = head;

    while(fast != null && fast.next != null){
        slow = slow.next;
        fast = fast.next.next;
        if(slow==fast){
            return true;
        }
    }

    return false;
}
```

```java
// Assuming there is a cycle present and slow and fast are point to their meeting point
slow = head;
while(slow!=fast){
	slow = slow.next;
	fast = fast.next;
}

return slow; // the starting point of the cycle.
```

## Tại sao nó hoạt động (Why does it work) {: #why-does-it-work}

### Bước 1: Sự hiện diện của chu trình (Step 1: Presence of the cycle) {: #step-1-presence-of-the-cycle_1}
Vì con trỏ $fast$ di chuyển với tốc độ gấp đôi $slow$, chúng ta có thể nói rằng tại bất kỳ thời điểm nào, $fast$ sẽ đi được quãng đường gấp đôi $slow$.
Chúng ta cũng có thể suy ra rằng sự khác biệt giữa khoảng cách đi được của cả hai con trỏ này đang tăng lên $1$.
```
slow: 0 --> 1 --> 2 --> 3 --> 4 (distance covered)
fast: 0 --> 2 --> 4 --> 6 --> 8 (distance covered)
diff: 0 --> 1 --> 2 --> 3 --> 4 (difference between distance covered by both pointers)
```
Gọi $L$ biểu thị độ dài của chu trình và $a$ đại diện cho số bước cần thiết để con trỏ chậm đến được lối vào của chu trình. Tồn tại một số nguyên dương $k$ ($k > 0$) sao cho $k \cdot L \geq a$.
Khi con trỏ chậm đã di chuyển $k \cdot L$ bước, và con trỏ nhanh đã đi được $2 \cdot k \cdot L$ bước, cả hai con trỏ đều thấy mình nằm trong chu trình. Tại thời điểm này, có sự phân tách $k \cdot L$ giữa chúng. Cho rằng độ dài của chu trình vẫn là $L$, điều này có nghĩa là chúng gặp nhau tại cùng một điểm trong chu trình, dẫn đến cuộc gặp gỡ của chúng.

### Bước 2: Điểm bắt đầu của chu trình (Step 2: Starting point of the cycle) {: #step-2-starting-point-of-the-cycle_1}

Hãy thử tính khoảng cách đi được của cả hai con trỏ cho đến khi chúng gặp nhau trong chu trình.

<div style="text-align: center;">
  <img src="tortoise_hare_proof.png" alt="Proof">
</div>

$slowDist = a + xL + b$            , $x\ge0$

$fastDist = a + yL + b$            , $y\ge0$

- $slowDist$ là tổng khoảng cách đi được bởi con trỏ chậm.
- $fastDist$ là tổng khoảng cách đi được bởi con trỏ nhanh.
- $a$ là số bước mà cả hai con trỏ cần thực hiện để vào chu trình.
- $b$ là khoảng cách giữa **C** và **G**, tức là khoảng cách giữa điểm bắt đầu của chu trình và điểm gặp nhau của cả hai con trỏ.
- $x$ là số lần con trỏ chậm đã lặp bên trong chu trình, bắt đầu từ và kết thúc tại **C**.
- $y$ là số lần con trỏ nhanh đã lặp bên trong chu trình, bắt đầu từ và kết thúc tại **C**.

$fastDist = 2 \cdot (slowDist)$

$a + yL + b = 2(a + xL + b)$

Giải quyết công thức chúng ta nhận được:

$a=(y-2x)L-b$

trong đó $y-2x$ là một số nguyên

Về cơ bản, điều này có nghĩa là $a$ bước giống như thực hiện một số vòng lặp đầy đủ trong chu trình và đi ngược lại $b$ bước.
Vì con trỏ nhanh đã đi trước $b$ bước so với lối vào của chu trình, nếu con trỏ nhanh di chuyển thêm $a$ bước nữa, nó sẽ kết thúc tại lối vào của chu trình.
Và vì chúng ta để con trỏ chậm bắt đầu từ đầu danh sách liên kết, sau $a$ bước, nó cũng sẽ kết thúc tại lối vào chu trình. Vì vậy, nếu cả hai di chuyển $a$ bước, cả hai sẽ gặp lối vào của chu trình.

## Bài tập (Problems) {: #problems}
- [Linked List Cycle (EASY)](https://leetcode.com/problems/linked-list-cycle/)
- [Happy Number (Easy)](https://leetcode.com/problems/happy-number/)
- [Find the Duplicate Number (Medium)](https://leetcode.com/problems/find-the-duplicate-number/)

## Checklist

- [x] Dịch các khái niệm kỹ thuật sang tiếng Việt chính xác.
- [x] Đã cập nhật các liên kết nội bộ (đến 127.0.0.1:8000).
- [x] Định dạng lại các công thức toán học và code block.
- [x] Kiểm tra chính tả và ngữ pháp.
- [x] Đảm bảo tính nhất quán với các thuật ngữ đã dịch khác.
