---
tags:
  - Translated
e_maxx_link: diofant_1_equation
---

# Phương trình đồng dư tuyến tính (Linear Congruence Equation) {: #linear-congruence-equation}

Phương trình này có dạng:

$$a \cdot x \equiv b \pmod n,$$

trong đó $a$, $b$ và $n$ là các số nguyên đã cho và $x$ là một số nguyên chưa biết.

Yêu cầu là tìm giá trị $x$ từ khoảng $[0, n-1]$ (rõ ràng, trên toàn bộ trục số có thể có vô số nghiệm sẽ khác nhau $n \cdot k$, trong đó $k$ là bất kỳ số nguyên nào). Nếu nghiệm không duy nhất, thì chúng ta sẽ xem xét cách lấy tất cả các nghiệm.

## Giải pháp bằng cách tìm phần tử nghịch đảo (Solution by finding the inverse element) {: #solution-by-finding-the-inverse-element}

Trước tiên chúng ta hãy xem xét một trường hợp đơn giản hơn trong đó $a$ và $n$ **nguyên tố cùng nhau** ($\gcd(a, n) = 1$).
Khi đó ta có thể tìm [nghịch đảo](module-inverse.md) của $a$, và nhân cả hai vế của phương trình với nghịch đảo, và chúng ta có thể nhận được một nghiệm **duy nhất**.

$$x \equiv b \cdot a ^ {- 1} \pmod n$$

Bây giờ hãy xem xét trường hợp $a$ và $n$ **không nguyên tố cùng nhau** ($\gcd(a, n) \ne 1$).
Khi đó nghiệm sẽ không phải lúc nào cũng tồn tại (ví dụ $2 \cdot x \equiv 1 \pmod 4$ không có nghiệm).

Gọi $g = \gcd(a, n)$, tức là [ước chung lớn nhất](euclid-algorithm.md) của $a$ và $n$ (trong trường hợp này lớn hơn một).

Khi đó, nếu $b$ không chia hết cho $g$, thì không có nghiệm. Thực tế, với bất kỳ $x$ nào, vế trái của phương trình $a \cdot x \pmod n$, luôn chia hết cho $g$, trong khi vế phải không chia hết cho nó, do đó suy ra rằng không có nghiệm.

Nếu $g$ chia hết $b$, thì bằng cách chia cả hai vế của phương trình cho $g$ (tức là chia $a$, $b$ và $n$ cho $g$), chúng ta nhận được một phương trình mới:

$$a^\prime \cdot x \equiv b^\prime \pmod{n^\prime}$$

trong đó $a^\prime$ và $n^\prime$ đã nguyên tố cùng nhau, và chúng ta đã học cách xử lý một phương trình như vậy.
Chúng ta nhận được $x^\prime$ là nghiệm cho $x$.

Rõ ràng là $x^\prime$ này cũng sẽ là một nghiệm của phương trình ban đầu.
Tuy nhiên nó sẽ **không phải là nghiệm duy nhất**.
Có thể chỉ ra rằng phương trình ban đầu có chính xác $g$ nghiệm, và chúng sẽ trông như thế này:

$$x_i \equiv (x^\prime + i\cdot n^\prime) \pmod n \quad \text{với } i = 0 \ldots g-1$$

Tóm lại, chúng ta có thể nói rằng **số lượng nghiệm** của phương trình đồng dư tuyến tính bằng $g = \gcd(a, n)$ hoặc bằng không.

## Giải pháp với Thuật toán Euclid mở rộng (Solution with the Extended Euclidean Algorithm) {: #solution-with-the-extended-euclidean-algorithm}

Chúng ta có thể viết lại phương trình đồng dư tuyến tính thành phương trình Diophantine sau:

$$a \cdot x + n \cdot k = b,$$

trong đó $x$ và $k$ là các số nguyên chưa biết.

Phương pháp giải phương trình này được mô tả trong bài viết tương ứng [Phương trình Diophantine tuyến tính](linear-diophantine-equation.md) và nó bao gồm việc áp dụng [Thuật toán Euclid mở rộng](extended-euclid-algorithm.md).

Nó cũng mô tả phương pháp thu được tất cả các nghiệm của phương trình này từ một nghiệm tìm thấy, và tình cờ phương pháp này, khi được xem xét cẩn thận, hoàn toàn tương đương với phương pháp được mô tả trong phần trước.

---

## Checklist

- Original lines: 57
- Translated lines: 57
- Code blocks changed? No
- Inline code changed? No
- Technical terms kept in English? Yes
- Headings anchors preserved/added correctly? Yes
- I confirm no character was omitted: YES
