---
title: Factorial modulo p
tags:
  - Translated
e_maxx_link: modular_factorial
---

# Giai thừa modulo $p$ (Factorial modulo $p$) {: #factorial-modulo-p}

Trong một số trường hợp, cần phải xem xét các công thức phức tạp modulo một số nguyên tố $p$, chứa giai thừa ở cả tử số và mẫu số, giống như công thức bạn gặp trong công thức cho Hệ số nhị thức.
Chúng ta xem xét trường hợp khi $p$ tương đối nhỏ.
Bài toán này chỉ có ý nghĩa khi các giai thừa xuất hiện ở cả tử số và mẫu số của phân số.
Ngược lại $p!$ và các số hạng tiếp theo sẽ giảm xuống 0.
Nhưng trong phân số, các thừa số của $p$ có thể triệt tiêu, và biểu thức kết quả sẽ khác không modulo $p$.

Do đó, một cách hình thức nhiệm vụ là: Bạn muốn tính $n! \bmod p$, mà không tính đến tất cả các thừa số bội của $p$ xuất hiện trong giai thừa.
Hãy tưởng tượng bạn viết ra phân tích thừa số nguyên tố của $n!$, loại bỏ tất cả các thừa số $p$, và tính tích modulo $p$.
Chúng ta sẽ ký hiệu giai thừa *đã sửa đổi* này là $n!_{\%p}$.
Ví dụ $7!_{\%p} \equiv 1 \cdot 2 \cdot \underbrace{1}_{3} \cdot 4 \cdot 5 \underbrace{2}_{6} \cdot 7 \equiv 2 \bmod 3$.

Học cách tính toán hiệu quả giai thừa đã sửa đổi này cho phép chúng ta tính toán nhanh chóng giá trị của các công thức tổ hợp khác nhau (ví dụ, [Hệ số nhị thức](../combinatorics/binomial-coefficients.md)).

## Thuật toán (Algorithm) {: #algorithm}
Hãy viết giai thừa đã sửa đổi này một cách tường minh.

$$\begin{eqnarray}
n!_{\%p} &=& 1 \cdot 2 \cdot 3 \cdot \ldots \cdot (p-2) \cdot (p-1) \cdot \underbrace{1}_{p} \cdot (p+1) \cdot (p+2) \cdot \ldots \cdot (2p-1) \cdot \underbrace{2}_{2p} \\\
 & &\quad \cdot (2p+1) \cdot \ldots \cdot (p^2-1) \cdot \underbrace{1}_{p^2} \cdot (p^2 +1) \cdot \ldots \cdot n \pmod{p} \\\\
&=& 1 \cdot 2 \cdot 3 \cdot \ldots \cdot (p-2) \cdot (p-1) \cdot \underbrace{1}_{p} \cdot 1 \cdot 2 \cdot \ldots \cdot (p-1) \cdot \underbrace{2}_{2p} \cdot 1 \cdot 2 \\\
& &\quad \cdot \ldots \cdot (p-1) \cdot \underbrace{1}_{p^2} \cdot 1 \cdot 2 \cdot \ldots \cdot (n \bmod p) \pmod{p}
\end{eqnarray}$$

Có thể thấy rõ ràng rằng giai thừa được chia thành nhiều khối có cùng độ dài ngoại trừ khối cuối cùng.

$$\begin{eqnarray}
n!_{\%p}&=& \underbrace{1 \cdot 2 \cdot 3 \cdot \ldots \cdot (p-2) \cdot (p-1) \cdot 1}_{1\text{st}} \cdot \underbrace{1 \cdot 2 \cdot 3 \cdot \ldots \cdot (p-2) \cdot (p-1) \cdot 2}_{2\text{nd}} \cdot \ldots \\\\
& & \cdot \underbrace{1 \cdot 2 \cdot 3 \cdot \ldots \cdot (p-2) \cdot (p-1) \cdot 1}_{p\text{th}} \cdot \ldots \cdot \quad \underbrace{1 \cdot 2 \cdot \cdot \ldots \cdot (n \bmod p)}_{\text{đuôi}} \pmod{p}.
\end{eqnarray}$$

Phần chính của các khối rất dễ đếm — nó chỉ là $(p-1)!\ \mathrm{mod}\ p$.
Chúng ta có thể tính toán điều đó bằng lập trình hoặc chỉ cần áp dụng định lý Wilson phát biểu rằng $(p-1)! \bmod p = -1$ với bất kỳ số nguyên tố $p$ nào.

Chúng ta có chính xác $\lfloor \frac{n}{p} \rfloor$ khối như vậy, do đó chúng ta cần nâng $-1$ lên lũy thừa $\lfloor \frac{n}{p} \rfloor$.
Điều này có thể được thực hiện trong thời gian logarit bằng cách sử dụng [Lũy thừa nhị phân](binary-exp.md); tuy nhiên bạn cũng có thể nhận thấy rằng kết quả sẽ chuyển đổi giữa $-1$ và $1$, vì vậy chúng ta chỉ cần xem tính chẵn lẻ của số mũ và nhân với $-1$ nếu tính chẵn lẻ là lẻ.
Và thay vì nhân, chúng ta cũng có thể chỉ cần trừ kết quả hiện tại khỏi $p$.

Giá trị của khối một phần cuối cùng có thể được tính riêng trong $O(p)$.


Điều này chỉ để lại phần tử cuối cùng của mỗi khối.
Nếu chúng ta ẩn các phần tử đã xử lý, chúng ta có thể thấy mẫu sau:

$$n!_{\%p} = \underbrace{ \ldots \cdot 1 } \cdot \underbrace{ \ldots \cdot 2} \cdot \ldots \cdot \underbrace{ \ldots \cdot (p-1)} \cdot \underbrace{ \ldots \cdot 1 } \cdot \underbrace{ \ldots \cdot 1} \cdot \underbrace{ \ldots \cdot 2} \cdots$$

Đây lại là một giai thừa *đã sửa đổi*, chỉ với kích thước nhỏ hơn nhiều.
Đó là $\lfloor n / p \rfloor !_{\%p}$.

Do đó, trong quá trình tính toán giai thừa *đã sửa đổi* $n\!_{\%p}$ chúng ta đã thực hiện $O(p)$ phép toán và còn lại với việc tính toán $\lfloor n / p \rfloor !_{\%p}$.
Chúng ta có một công thức đệ quy.
Độ sâu đệ quy là $O(\log_p n)$, và do đó hành vi tiệm cận hoàn chỉnh của thuật toán là $O(p \log_p n)$.

Lưu ý, nếu bạn tính trước các giai thừa $0!,~ 1!,~ 2!,~ \dots,~ (p-1)!$ modulo $p$, thì độ phức tạp sẽ chỉ là $O(\log_p n)$.


## Cài đặt (Implementation) {: #implementation}

Chúng ta không cần đệ quy vì đây là trường hợp của đệ quy đuôi và do đó có thể dễ dàng được cài đặt bằng cách lặp.
Trong cài đặt sau, chúng tôi tính trước các giai thừa $0!,~ 1!,~ \dots,~ (p-1)!$, và do đó có thời gian chạy $O(p + \log_p n)$.
Nếu bạn cần gọi hàm nhiều lần, thì bạn có thể thực hiện việc tính trước bên ngoài hàm và thực hiện tính toán $n!_{\%p}$ trong thời gian $O(\log_p n)$.

```cpp
int factmod(int n, int p) {
    vector<int> f(p);
    f[0] = 1;
    for (int i = 1; i < p; i++)
        f[i] = f[i-1] * i % p;

    int res = 1;
    while (n > 1) {
        if ((n/p) % 2)
            res = p - res;
        res = res * f[n%p] % p;
        n /= p;
    }
    return res;
}
```

Thay thế, nếu bạn chỉ có bộ nhớ giới hạn và không thể lưu trữ tất cả các giai thừa, bạn cũng có thể chỉ cần nhớ các giai thừa mà bạn cần, sắp xếp chúng, và sau đó tính toán chúng trong một lần quét bằng cách tính các giai thừa $0!,~ 1!,~ 2!,~ \dots,~ (p-1)!$ trong một vòng lặp mà không lưu trữ chúng một cách rõ ràng.

## Số mũ của $p$ (Multiplicity of $p$) {: #multiplicity-of-p}

Nếu chúng ta muốn tính Hệ số nhị thức modulo $p$, thì chúng ta cần thêm số mũ của $p$ trong $n$, tức là số lần $p$ xuất hiện trong phân tích thừa số nguyên tố của $n$, hoặc số lần chúng ta đã xóa $p$ trong quá trình tính toán giai thừa *đã sửa đổi*.

[Công thức Legendre](https://en.wikipedia.org/wiki/Legendre%27s_formula) cho chúng ta một cách để tính điều này trong thời gian $O(\log_p n)$.
Công thức cho số mũ $\nu_p$ như sau:

$$\nu_p(n!) = \sum_{i=1}^{\infty} \left\lfloor \frac{n}{p^i} \right\rfloor$$

Do đó chúng ta có cài đặt:

```cpp
int multiplicity_factorial(int n, int p) {
    int count = 0;
    do {
        n /= p;
        count += n;
    } while (n);
    return count;
}
```

Công thức này có thể được chứng minh rất dễ dàng bằng cách sử dụng các ý tưởng tương tự mà chúng ta đã làm trong các phần trước.
Loại bỏ tất cả các phần tử không chứa thừa số $p$.
Điều này để lại $\lfloor n/p \rfloor$ phần tử còn lại.
Nếu chúng ta loại bỏ thừa số $p$ khỏi mỗi chúng, chúng ta nhận được tích $1 \cdot 2 \cdots \lfloor n/p \rfloor = \lfloor n/p \rfloor !$, và một lần nữa chúng ta có một đệ quy.

---
