---
tags:
  - Translated
e_maxx_link: randomized_heap
---

# Heap ngẫu nhiên (Randomized Heap) {: #randomized-heap}

Một heap ngẫu nhiên (randomized heap) là một heap, thông qua việc sử dụng ngẫu nhiên hóa, cho phép thực hiện tất cả các thao tác trong thời gian logarit kỳ vọng.

Một **min heap** là một cây nhị phân trong đó giá trị của mỗi đỉnh nhỏ hơn hoặc bằng giá trị của các con của nó.
Do đó, giá trị nhỏ nhất của cây luôn ở đỉnh gốc.

Một max heap có thể được định nghĩa theo cách tương tự: bằng cách thay thế nhỏ hơn bằng lớn hơn.

Các thao tác mặc định của một heap là:

- Thêm một giá trị
- Trích xuất giá trị nhỏ nhất
- Xóa giá trị nhỏ nhất
- Hợp nhất hai heap (không xóa các bản sao)
- Xóa một phần tử bất kỳ (nếu biết vị trí của nó trong cây)

Một heap ngẫu nhiên có thể thực hiện tất cả các thao tác này trong thời gian kỳ vọng $O(\log n)$ với một cài đặt rất đơn giản.

## Cấu trúc dữ liệu (Data structure) {: #data-structure}

Chúng ta có thể mô tả ngay cấu trúc của binary heap:

```{.cpp file=randomized_heap_structure}
struct Tree {
    int value;
    Tree * l = nullptr;
    Tree * r = nullptr;
    Tree(int val) : value(val) {}
};
```

Trong đỉnh, chúng ta lưu trữ một giá trị.
Ngoài ra, chúng ta có các con trỏ đến con trái và con phải, trỏ đến null nếu con tương ứng không tồn tại.

## Các thao tác (Operations) {: #operations}

Không khó để thấy rằng tất cả các thao tác có thể được giảm xuống thành một thao tác duy nhất: **hợp nhất** hai heap thành một.
Thật vậy, thêm một giá trị mới vào heap tương đương với việc hợp nhất heap với một heap bao gồm một đỉnh duy nhất có giá trị đó.
Tìm giá trị nhỏ nhất hoàn toàn không yêu cầu bất kỳ thao tác nào - giá trị nhỏ nhất đơn giản là giá trị tại gốc.
Xóa giá trị nhỏ nhất tương đương với kết quả của việc hợp nhất con trái và con phải của đỉnh gốc.
Và xóa một phần tử bất kỳ cũng tương tự.
Chúng ta hợp nhất các con của đỉnh và thay thế đỉnh bằng kết quả của việc hợp nhất.

Vì vậy, chúng ta thực sự chỉ cần cài đặt thao tác hợp nhất hai heap.
Tất cả các thao tác khác đều được giảm một cách tầm thường xuống thao tác này.

Giả sử có hai heap $T_1$ và $T_2$.
Rõ ràng là gốc của mỗi heap này chứa giá trị nhỏ nhất của nó.
Vì vậy, gốc của heap kết quả sẽ là giá trị nhỏ nhất của hai giá trị này.
Vì vậy, chúng ta so sánh cả hai giá trị, và sử dụng giá trị nhỏ hơn làm gốc mới.
Bây giờ chúng ta phải kết hợp các con của đỉnh đã chọn với heap còn lại.
Để làm điều này, chúng ta chọn một trong các con, và hợp nhất nó với heap còn lại.
Do đó, chúng ta lại có thao tác hợp nhất hai heap.
Sớm hay muộn quá trình này sẽ kết thúc (số bước như vậy bị giới hạn bởi tổng chiều cao của hai heap).

Để đạt được độ phức tạp logarit trung bình, chúng ta cần chỉ định một phương pháp để chọn một trong hai con sao cho độ dài đường đi trung bình là logarit.
Không khó để đoán rằng, chúng ta sẽ đưa ra quyết định này **một cách ngẫu nhiên**.
Do đó, việc cài đặt thao tác hợp nhất như sau:

```{.cpp file=randomized_heap_merge}
Tree* merge(Tree* t1, Tree* t2) {
    if (!t1 || !t2)
        return t1 ? t1 : t2;
    if (t2->value < t1->value)
        swap(t1, t2);
    if (rand() & 1)
        swap(t1->l, t1->r);
    t1->l = merge(t1->l, t2);
    return t1;
}
```

Ở đây đầu tiên chúng ta kiểm tra xem một trong các heap có rỗng hay không, nếu có thì chúng ta hoàn toàn không cần thực hiện bất kỳ hành động hợp nhất nào.
Ngược lại, chúng ta biến heap `t1` thành heap có giá trị nhỏ hơn (bằng cách hoán đổi `t1` và `t2` nếu cần thiết).
Chúng ta muốn hợp nhất con trái của `t1` với `t2`, do đó chúng ta hoán đổi ngẫu nhiên các con của `t1`, và sau đó thực hiện hợp nhất.

## Độ phức tạp (Complexity) {: #complexity}

Chúng ta giới thiệu biến ngẫu nhiên $h(T)$ biểu thị **độ dài của đường đi ngẫu nhiên** từ gốc đến lá (độ dài theo số lượng cạnh).
Rõ ràng là thuật toán `merge` thực hiện các bước $O(h(T_1) + h(T_2))$.
Do đó, để hiểu độ phức tạp của các thao tác, chúng ta phải xem xét biến ngẫu nhiên $h(T)$.

### Giá trị kỳ vọng (Expected value) {: #expected-value}

Chúng ta giả định rằng kỳ vọng $h(T)$ có thể được ước tính từ phía trên bằng logarit của số lượng đỉnh trong heap:

$$\mathbf{E} h(T) \le \log(n+1)$$

Điều này có thể dễ dàng được chứng minh bằng quy nạp.
Gọi $L$ và $R$ là các cây con bên trái và bên phải của gốc $T$, và $n_L$ và $n_R$ là số lượng đỉnh trong chúng ($n = n_L + n_R + 1$).

Điều sau đây cho thấy bước quy nạp:

$$\begin{align}
\mathbf{E} h(T) &= 1 + \frac{\mathbf{E} h(L) + \mathbf{E} h(R)}{2} 
\le 1 + \frac{\log(n_L + 1) \log(n_R + 1)}{2} \\\\
&= 1 + \log\sqrt{(n_L + 1)(n_R + 1)} = \log 2\sqrt{(n_L + 1)(n_R + 1)} \\\\
&\le \log \frac{2\left((n_L + 1) + (n_R + 1)\right)}{2} = \log(n_L + n_R + 2) = \log(n+1)
\end{align}$$

### Vượt quá giá trị kỳ vọng (Exceeding the expected value) {: #exceeding-the-expected-value}

Tất nhiên chúng ta vẫn chưa hài lòng.
Giá trị kỳ vọng của $h(T)$ không nói lên điều gì về trường hợp xấu nhất.
Vẫn có thể xảy ra trường hợp các đường đi từ gốc đến các đỉnh trung bình lớn hơn nhiều so với $\log(n + 1)$ đối với một cây cụ thể.

Hãy chứng minh rằng việc vượt quá giá trị kỳ vọng thực sự là rất nhỏ:

$$P\{h(T) > (c+1) \log n\} < \frac{1}{n^c}$$

đối với bất kỳ hằng số dương $c$ nào.

Ở đây chúng ta ký hiệu $P$ là tập hợp các đường đi từ gốc của heap đến các lá có độ dài vượt quá $(c+1) \log n$.
Lưu ý rằng đối với bất kỳ đường đi $p$ nào có độ dài $|p|$, xác suất để nó được chọn làm đường đi ngẫu nhiên là $2^{-|p|}$.
Do đó chúng ta nhận được:

$$P\{h(T) > (c+1) \log n\} = \sum_{p \in P} 2^{-|p|} < \sum_{p \in P} 2^{-(c+1) \log n} = |P| n^{-(c+1)} \le n^{-c}$$

### Độ phức tạp của thuật toán (Complexity of the algorithm) {: #complexity-of-the-algorithm}

Do đó, thuật toán `merge`, và do đó tất cả các thao tác khác được thể hiện bằng nó, có thể được thực hiện trong $O(\log n)$ trung bình.

Hơn nữa, đối với bất kỳ hằng số dương $\epsilon$ nào, có một hằng số dương $c$, sao cho xác suất mà thao tác sẽ yêu cầu nhiều hơn $c \log n$ bước nhỏ hơn $n^{-\epsilon}$ (theo một nghĩa nào đó, điều này mô tả hành vi trường hợp xấu nhất của thuật toán).

---

## Checklist

- Original lines: 130
- Translated lines: 130
- Code blocks changed? No
- Inline code changed? No
- Technical terms kept in English? Yes
- Headings anchors preserved/added correctly? Yes
- I confirm no character was omitted: YES
