---
tags:
  - Translated
e_maxx_link: fft_multiply
---

# Biến đổi Fourier nhanh (Fast Fourier transform) {: #fast-fourier-transform}

Trong bài viết này, chúng tôi sẽ thảo luận về một thuật toán cho phép chúng ta nhân hai đa thức có độ dài $n$ trong thời gian $O(n \log n)$, tốt hơn phép nhân tầm thường thông thường mất thời gian $O(n^2)$.
Rõ ràng việc nhân hai số lớn cũng có thể được đưa về việc nhân các đa thức, vì vậy hai số lớn cũng có thể được nhân trong thời gian $O(n \log n)$ (trong đó $n$ là số chữ số trong các số).

Việc khám phá ra **biến đổi Fourier nhanh (Fast Fourier transformation - FFT)** được cho là của Cooley và Tukey, những người đã công bố một thuật toán vào năm 1965.
Nhưng thực tế FFT đã được phát hiện lặp đi lặp lại trước đó, nhưng tầm quan trọng của nó đã không được hiểu trước khi có các phát minh của máy tính hiện đại.
Một số nhà nghiên cứu cho rằng việc khám phá ra FFT là của Runge và König vào năm 1924.
Nhưng thực sự Gauss đã phát triển một phương pháp như vậy vào năm 1805, nhưng chưa bao giờ công bố nó.

Lưu ý rằng thuật toán FFT được trình bày ở đây chạy trong thời gian $O(n \log n)$, nhưng nó không hoạt động để nhân các đa thức lớn tùy ý với các hệ số lớn tùy ý hoặc để nhân các số nguyên lớn tùy ý.
Nó có thể dễ dàng xử lý các đa thức có kích thước $10^5$ với các hệ số nhỏ, hoặc nhân hai số có kích thước $10^6$, thường là đủ để giải quyết các bài toán lập trình thi đấu. Ngoài quy mô nhân các số có $10^6$ bit, phạm vi và độ chính xác của các số dấu phẩy động được sử dụng trong quá trình tính toán sẽ không đủ để đưa ra kết quả cuối cùng chính xác, mặc dù có những biến thể phức tạp hơn có thể thực hiện phép nhân đa thức/số nguyên lớn tùy ý.
Ví dụ: vào năm 1971 Schönhage và Strasser đã phát triển một biến thể để nhân các số lớn tùy ý áp dụng FFT đệ quy trong các cấu trúc vành chạy trong $O(n \log n \log \log n)$.
Và gần đây (vào năm 2019) Harvey và van der Hoeven đã công bố một thuật toán chạy trong đúng $O(n \log n)$.

## Biến đổi Fourier rời rạc (Discrete Fourier transform) {: #discrete-fourier-transform}

Giả sử có một đa thức bậc $n - 1$:

$$A(x) = a_0 x^0 + a_1 x^1 + \dots + a_{n-1} x^{n-1}$$

Không mất tính tổng quát, chúng ta giả sử rằng $n$ - số lượng hệ số - là lũy thừa của $2$.
Nếu $n$ không phải là lũy thừa của $2$, thì chúng ta chỉ cần thêm các số hạng còn thiếu $a_i x^i$ và đặt các hệ số $a_i$ thành $0$.

Lý thuyết số phức cho chúng ta biết rằng phương trình $x^n = 1$ có $n$ nghiệm phức (được gọi là căn bậc $n$ của đơn vị), và các nghiệm có dạng $w_{n, k} = e^{\frac{2 k \pi i}{n}}$ với $k = 0 \dots n-1$.
Ngoài ra, các số phức này có một số tính chất rất thú vị:
ví dụ: căn bậc $n$ chính $w_n = w_{n, 1} = e^{\frac{2 \pi i}{n}}$ có thể được sử dụng để mô tả tất cả các căn bậc $n$ khác: $w_{n, k} = (w_n)^k$.

**Biến đổi Fourier rời rạc (DFT)** của đa thức $A(x)$ (hoặc tương đương là vectơ các hệ số $(a_0, a_1, \dots, a_{n-1})$) được định nghĩa là các giá trị của đa thức tại các điểm $x = w_{n, k}$, tức là nó là vectơ:

$$\begin{align}
\text{DFT}(a_0, a_1, \dots, a_{n-1}) &= (y_0, y_1, \dots, y_{n-1}) \\
&= (A(w_{n, 0}), A(w_{n, 1}), \dots, A(w_{n, n-1})) \\
&= (A(w_n^0), A(w_n^1), \dots, A(w_n^{n-1}))
\end{align}$$

Tương tự, **biến đổi Fourier rời rạc ngược (inverse discrete Fourier transform)** được định nghĩa:
Biến đổi DFT ngược của các giá trị của đa thức $(y_0, y_1, \dots, y_{n-1})$ là các hệ số của đa thức $(a_0, a_1, \dots, a_{n-1})$.

$$\text{InverseDFT}(y_0, y_1, \dots, y_{n-1}) = (a_0, a_1, \dots, a_{n-1})$$

Do đó, nếu một DFT trực tiếp tính toán các giá trị của đa thức tại các điểm ở căn bậc $n$, thì DFT ngược có thể khôi phục các hệ số của đa thức sử dụng các giá trị đó.

### Ứng dụng của DFT: nhân nhanh đa thức (Application of the DFT: fast multiplication of polynomials) {: #application-of-the-dft-fast-multiplication-of-polynomials}

Giả sử có hai đa thức $A$ và $B$.
Chúng ta tính DFT cho mỗi đa thức: $\text{DFT}(A)$ và $\text{DFT}(B)$.

Điều gì xảy ra nếu chúng ta nhân các đa thức này?
Rõ ràng tại mỗi điểm, các giá trị chỉ đơn giản là nhân với nhau, tức là

$$(A \cdot B)(x) = A(x) \cdot B(x).$$

Điều này có nghĩa là nếu chúng ta nhân các vectơ $\text{DFT}(A)$ và $\text{DFT}(B)$ - bằng cách nhân từng phần tử của một vectơ với phần tử tương ứng của vectơ kia - thì chúng ta không nhận được gì khác ngoài DFT của đa thức $\text{DFT}(A \cdot B)$:

$$\text{DFT}(A \cdot B) = \text{DFT}(A) \cdot \text{DFT}(B)$$

Cuối cùng, áp dụng DFT ngược, chúng ta thu được:

$$A \cdot B = \text{InverseDFT}(\text{DFT}(A) \cdot \text{DFT}(B))$$

Ở bên phải tích của hai DFT, chúng tôi có nghĩa là tích từng đôi một của các phần tử vectơ.
Điều này có thể được tính toán trong thời gian $O(n)$.
Nếu chúng ta có thể tính DFT và DFT ngược trong $O(n \log n)$, thì chúng ta có thể tính tích của hai đa thức (và do đó cũng là hai số lớn) với cùng độ phức tạp thời gian.

Cần lưu ý rằng hai đa thức phải có cùng bậc.
Nếu không, hai vectơ kết quả của DFT có độ dài khác nhau.
Chúng ta có thể thực hiện điều này bằng cách thêm các hệ số có giá trị $0$.

Và cũng vậy, vì kết quả của tích của hai đa thức là một đa thức bậc $2 (n - 1)$, chúng ta phải nhân đôi bậc của mỗi đa thức (một lần nữa bằng cách đệm các số $0$).
Từ một vectơ có $n$ giá trị, chúng ta không thể tái tạo đa thức mong muốn với $2n - 1$ hệ số.

### Biến đổi Fourier Nhanh (Fast Fourier Transform) {: #fast-fourier-transform-1}

**Biến đổi Fourier nhanh** là một phương pháp cho phép tính DFT trong thời gian $O(n \log n)$.
Ý tưởng cơ bản của FFT là áp dụng chia để trị.
Chúng ta chia vectơ hệ số của đa thức thành hai vectơ, tính toán đệ quy DFT cho mỗi vectơ đó và kết hợp các kết quả để tính DFT của đa thức hoàn chỉnh.

Vì vậy giả sử có một đa thức $A(x)$ với bậc $n - 1$, trong đó $n$ là lũy thừa của $2$, và $n > 1$:

$$A(x) = a_0 x^0 + a_1 x^1 + \dots + a_{n-1} x^{n-1}$$

Chúng ta chia nó thành hai đa thức nhỏ hơn, một chứa các hệ số của các vị trí chẵn, và một chứa các hệ số của các vị trí lẻ:

$$\begin{align}
A_0(x) &= a_0 x^0 + a_2 x^1 + \dots + a_{n-2} x^{\frac{n}{2}-1} \\
A_1(x) &= a_1 x^0 + a_3 x^1 + \dots + a_{n-1} x^{\frac{n}{2}-1}
\end{align}$$

Dễ dàng nhận thấy rằng

$$A(x) = A_0(x^2) + x A_1(x^2).$$

Các đa thức $A_0$ và $A_1$ chỉ có một nửa số lượng hệ số so với đa thức $A$.
Nếu chúng ta có thể tính $\text{DFT}(A)$ trong thời gian tuyến tính bằng cách sử dụng $\text{DFT}(A_0)$ và $\text{DFT}(A_1)$, thì chúng ta nhận được công thức truy hồi $T_{\text{DFT}}(n) = 2 T_{\text{DFT}}\left(\frac{n}{2}\right) + O(n)$ cho độ phức tạp thời gian, dẫn đến $T_{\text{DFT}}(n) = O(n \log n)$ theo **định lý thợ (master theorem)**.

Hãy tìm hiểu cách chúng ta có thể thực hiện điều đó.

Giả sử chúng ta đã tính toán các vectơ $\left(y_k^0\right)_{k=0}^{n/2-1} = \text{DFT}(A_0)$ và $\left(y_k^1\right)_{k=0}^{n/2-1} = \text{DFT}(A_1)$.
Hãy tìm một biểu thức cho $\left(y_k\right)_{k=0}^{n-1} = \text{DFT}(A)$.

Đối với $\frac{n}{2}$ giá trị đầu tiên, chúng ta chỉ cần sử dụng phương trình đã lưu ý trước đó $A(x) = A_0(x^2) + x A_1(x^2)$:

$$y_k = y_k^0 + w_n^k y_k^1, \quad k = 0 \dots \frac{n}{2} - 1.$$

Tuy nhiên đối với $\frac{n}{2}$ giá trị thứ hai, chúng ta cần tìm một biểu thức hơi khác:

$$\begin{align}
y_{k+n/2} &= A\left(w_n^{k+n/2}\right) \\
&= A_0\left(w_n^{2k+n}\right) + w_n^{k + n/2} A_1\left(w_n^{2k+n}\right) \\
&= A_0\left(w_n^{2k} w_n^n\right) + w_n^k w_n^{n/2} A_1\left(w_n^{2k} w_n^n\right) \\
&= A_0\left(w_n^{2k}\right) - w_n^k A_1\left(w_n^{2k}\right) \\
&= y_k^0 - w_n^k y_k^1
\end{align}$$

Ở đây chúng ta đã sử dụng lại $A(x) = A_0(x^2) + x A_1(x^2)$ và hai đẳng thức $w_n^n = 1$ và $w_n^{n/2} = -1$.

Do đó, chúng ta nhận được các công thức mong muốn để tính toán toàn bộ vectơ $(y_k)$:

$$\begin{align}
y_k &= y_k^0 + w_n^k y_k^1, &\quad k = 0 \dots \frac{n}{2} - 1, \\
y_{k+n/2} &= y_k^0 - w_n^k y_k^1, &\quad k = 0 \dots \frac{n}{2} - 1.
\end{align}$$

(Mẫu này $a + b$ và $a - b$ đôi khi được gọi là **bướm (butterfly)**.)

Như vậy chúng ta đã học được cách tính DFT trong thời gian $O(n \log n)$.

### FFT ngược (Inverse FFT) {: #inverse-fft}

Giả sử vectơ $(y_0, y_1, \dots y_{n-1})$ - các giá trị của đa thức $A$ bậc $n - 1$ tại các điểm $x = w_n^k$ - được cho.
Chúng ta muốn khôi phục các hệ số $(a_0, a_1, \dots, a_{n-1})$ của đa thức.
Bài toán đã biết này được gọi là **nội suy**, và có các thuật toán tổng quát để giải quyết nó.
Nhưng trong trường hợp đặc biệt này (vì chúng ta biết giá trị của các điểm tại các căn đơn vị), chúng ta có thể thu được một thuật toán đơn giản hơn nhiều (thực tế giống với FFT trực tiếp).

Chúng ta có thể viết DFT, theo định nghĩa của nó, dưới dạng ma trận:

$$
\begin{pmatrix}
w_n^0 & w_n^0 & w_n^0 & w_n^0 & \cdots & w_n^0 \\
w_n^0 & w_n^1 & w_n^2 & w_n^3 & \cdots & w_n^{n-1} \\
w_n^0 & w_n^2 & w_n^4 & w_n^6 & \cdots & w_n^{2(n-1)} \\
w_n^0 & w_n^3 & w_n^6 & w_n^9 & \cdots & w_n^{3(n-1)} \\
\vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\
w_n^0 & w_n^{n-1} & w_n^{2(n-1)} & w_n^{3(n-1)} & \cdots & w_n^{(n-1)(n-1)}
\end{pmatrix} \begin{pmatrix}
a_0 \\ a_1 \\ a_2 \\ a_3 \\ \vdots \\ a_{n-1}
\end{pmatrix} = \begin{pmatrix}
y_0 \\ y_1 \\ y_2 \\ y_3 \\ \vdots \\ y_{n-1}
\end{pmatrix}
$$

Ma trận này được gọi là **ma trận Vandermonde**.

Do đó chúng ta có thể tính toán vectơ $(a_0, a_1, \dots, a_{n-1})$ bằng cách nhân vectơ $(y_0, y_1, \dots y_{n-1})$ từ bên trái với nghịch đảo của ma trận:

$$
\begin{pmatrix}
a_0 \\ a_1 \\ a_2 \\ a_3 \\ \vdots \\ a_{n-1}
\end{pmatrix} = \begin{pmatrix}
w_n^0 & w_n^0 & w_n^0 & w_n^0 & \cdots & w_n^0 \\
w_n^0 & w_n^1 & w_n^2 & w_n^3 & \cdots & w_n^{n-1} \\
w_n^0 & w_n^2 & w_n^4 & w_n^6 & \cdots & w_n^{2(n-1)} \\
w_n^0 & w_n^3 & w_n^6 & w_n^9 & \cdots & w_n^{3(n-1)} \\
\vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\
w_n^0 & w_n^{n-1} & w_n^{2(n-1)} & w_n^{3(n-1)} & \cdots & w_n^{(n-1)(n-1)}
\end{pmatrix}^{-1} \begin{pmatrix}
y_0 \\ y_1 \\ y_2 \\ y_3 \\ \vdots \\ y_{n-1}
\end{pmatrix}
$$

Một kiểm tra nhanh có thể xác minh rằng nghịch đảo của ma trận có dạng sau:

$$
\frac{1}{n}
\begin{pmatrix}
w_n^0 & w_n^0 & w_n^0 & w_n^0 & \cdots & w_n^0 \\
w_n^0 & w_n^{-1} & w_n^{-2} & w_n^{-3} & \cdots & w_n^{-(n-1)} \\
w_n^0 & w_n^{-2} & w_n^{-4} & w_n^{-6} & \cdots & w_n^{-2(n-1)} \\
w_n^0 & w_n^{-3} & w_n^{-6} & w_n^{-9} & \cdots & w_n^{-3(n-1)} \\
\vdots & \vdots & \vdots & \vdots & \ddots & \vdots \\
w_n^0 & w_n^{-(n-1)} & w_n^{-2(n-1)} & w_n^{-3(n-1)} & \cdots & w_n^{-(n-1)(n-1)}
\end{pmatrix}
$$

Do đó chúng ta thu được công thức:

$$a_k = \frac{1}{n} \sum_{j=0}^{n-1} y_j w_n^{-k j}$$

So sánh điều này với công thức cho $y_k$

$$y_k = \sum_{j=0}^{n-1} a_j w_n^{k j},$$

chúng tôi nhận thấy rằng các bài toán này gần như giống nhau, vì vậy các hệ số $a_k$ có thể được tìm thấy bằng cùng một thuật toán chia để trị, cũng như FFT trực tiếp, chỉ thay vì $w_n^k$ chúng tôi phải sử dụng $w_n^{-k}$, và cuối cùng chúng tôi cần chia các hệ số kết quả cho $n$.

Do đó, việc tính toán DFT ngược gần giống như việc tính toán DFT trực tiếp, và nó cũng có thể được thực hiện trong thời gian $O(n \log n)$.

### Cài đặt {: #implementation}

Ở đây chúng tôi trình bày một **cài đặt đệ quy đơn giản của FFT** và FFT ngược, cả hai trong một hàm, vì sự khác biệt giữa FFT thuận và FFT ngược là rất nhỏ.
Để lưu trữ các số phức, chúng tôi sử dụng kiểu complex trong thư viện STL của C++.

```{.cpp file=fft_recursive}
using cd = complex<double>;
const double PI = acos(-1);

void fft(vector<cd> & a, bool invert) {
    int n = a.size();
    if (n == 1)
        return;

    vector<cd> a0(n / 2), a1(n / 2);
    for (int i = 0; 2 * i < n; i++) {
        a0[i] = a[2*i];
        a1[i] = a[2*i+1];
    }
    fft(a0, invert);
    fft(a1, invert);

    double ang = 2 * PI / n * (invert ? -1 : 1);
    cd w(1), wn(cos(ang), sin(ang));
    for (int i = 0; 2 * i < n; i++) {
        a[i] = a0[i] + w * a1[i];
        a[i + n/2] = a0[i] - w * a1[i];
        if (invert) {
            a[i] /= 2;
            a[i + n/2] /= 2;
        }
        w *= wn;
    }
}
```

Hàm được truyền một vectơ các hệ số, và hàm sẽ tính toán DFT hoặc DFT ngược và lưu trữ lại kết quả vào vectơ này.
Tham số $\text{invert}$ cho biết liệu DFT trực tiếp hay DFT ngược sẽ được tính toán.
Bên trong hàm, trước tiên chúng tôi kiểm tra xem độ dài của vectơ có bằng một hay không, nếu có thì chúng tôi không phải làm gì cả.
Nếu không, chúng tôi chia vectơ $a$ thành hai vectơ $a0$ và $a1$ và tính toán DFT cho cả hai đệ quy.
Sau đó, chúng tôi khởi tạo giá trị $wn$ và một biến $w$, biến này sẽ chứa lũy thừa hiện tại của $wn$.
Sau đó, các giá trị của DFT kết quả được tính bằng các công thức trên.

Nếu cờ $\text{invert}$ được đặt, thì chúng tôi thay thế $wn$ bằng $wn^{-1}$, và mỗi giá trị của kết quả được chia cho $2$ (vì điều này sẽ được thực hiện ở mỗi cấp độ của đệ quy, cuối cùng sẽ chia các giá trị cuối cùng cho $n$).

Sử dụng hàm này, chúng ta có thể tạo một hàm để **nhân hai đa thức**:

```{.cpp file=fft_multiply}
vector<int> multiply(vector<int> const& a, vector<int> const& b) {
    vector<cd> fa(a.begin(), a.end()), fb(b.begin(), b.end());
    int n = 1;
    while (n < a.size() + b.size()) 
        n <<= 1;
    fa.resize(n);
    fb.resize(n);

    fft(fa, false);
    fft(fb, false);
    for (int i = 0; i < n; i++)
        fa[i] *= fb[i];
    fft(fa, true);

    vector<int> result(n);
    for (int i = 0; i < n; i++)
        result[i] = round(fa[i].real());
    return result;
}
```

Hàm này hoạt động với các đa thức có hệ số nguyên, tuy nhiên bạn cũng có thể điều chỉnh nó để làm việc với các hệ số khác.
Vì có một số sai số khi làm việc với số phức, chúng ta cần làm tròn các hệ số kết quả ở cuối.

Cuối cùng, hàm để **nhân** hai số lớn thực tế không khác biệt so với hàm nhân đa thức.
Điều duy nhất chúng ta phải làm sau đó, là chuẩn hóa số:

```cpp
    int carry = 0;
    for (int i = 0; i < n; i++)
        result[i] += carry;
        carry = result[i] / 10;
        result[i] %= 10;
    }
```

Vì chiều dài của tích của hai số không bao giờ vượt quá tổng chiều dài của cả hai số, kích thước của vectơ là đủ để thực hiện tất cả các phép toán nhớ (carry).

### Cài đặt cải tiến: tính toán tại chỗ (Improved implementation: in-place computation) {: #improved-implementation-in-place-computation}

Để tăng hiệu quả, chúng tôi sẽ chuyển từ cài đặt đệ quy sang cài đặt lặp.
Trong cài đặt đệ quy ở trên, chúng tôi đã tách vectơ $a$ một cách rõ ràng thành hai vectơ - phần tử ở các vị trí chẵn được gán cho một vectơ tạm thời và các phần tử ở các vị trí lẻ cho một vectơ khác.
Tuy nhiên, nếu chúng ta sắp xếp lại các phần tử theo một cách nhất định, chúng ta không cần tạo các vectơ tạm thời này (tức là tất cả các phép tính có thể được thực hiện "tại chỗ", ngay trong vectơ $A$ chính nó).

Lưu ý rằng ở mức đệ quy đầu tiên, các phần tử có bit thấp nhất của vị trí là 0 được gán cho vectơ $a_0$, và các phần tử có số 1 là bit thấp nhất của vị trí được gán cho $a_1$.
Ở mức đệ quy thứ hai, điều tương tự cũng xảy ra, nhưng thay vào đó là bit thấp thứ hai, v.v.
Do đó, nếu chúng ta đảo ngược các bit của vị trí của mỗi hệ số và sắp xếp chúng theo các giá trị bị đảo ngược này, chúng ta sẽ nhận được thứ tự mong muốn (nó được gọi là hoán vị đảo ngược bit - bit-reversal permutation).

Ví dụ thứ tự mong muốn cho $n = 8$ có dạng:

$$a = \bigg\{ \Big[ (a_0, a_4), (a_2, a_6) \Big], \Big[ (a_1, a_5), (a_3, a_7) \Big] \bigg\}$$

Thật vậy, trong mức đệ quy đầu tiên (được bao quanh bởi dấu ngoặc nhọn), vectơ được chia thành hai phần $[a_0, a_2, a_4, a_6]$ và $[a_1, a_3, a_5, a_7]$.
Như chúng ta thấy, trong hoán vị đảo ngược bit, điều này tương ứng với việc đơn giản chia vectơ thành hai nửa: $\frac{n}{2}$ phần tử đầu tiên và $\frac{n}{2}$ phần tử cuối cùng.
Sau đó, có một lời gọi đệ quy cho mỗi nửa.
Giả sử DFT kết quả cho mỗi nửa đó được trả về tại vị trí của chính các phần tử đó (tức là nửa đầu và nửa sau của vectơ $a$ tương ứng).

$$a = \bigg\{ \Big[y_0^0, y_1^0, y_2^0, y_3^0\Big], \Big[y_0^1, y_1^1, y_2^1, y_3^1 \Big] \bigg\}$$

Bây giờ chúng ta muốn kết hợp hai DFT thành một cho vectơ hoàn chỉnh.
Thứ tự của các phần tử là lý tưởng, và chúng ta cũng có thể thực hiện phép hợp trực tiếp trong vectơ này.
Chúng ta có thể lấy các phần tử $y_0^0$ và $y_0^1$ và thực hiện biến đổi bướm.
Vị trí của hai giá trị kết quả giống với vị trí của hai giá trị ban đầu, vì vậy chúng ta nhận được:

$$a = \bigg\{ \Big[y_0^0 + w_n^0 y_0^1, y_1^0, y_2^0, y_3^0\Big], \Big[y_0^0 - w_n^0 y_0^1, y_1^1, y_2^1, y_3^1\Big] \bigg\}$$

Tương tự chúng ta có thể tính toán biến đổi bướm của $y_1^0$ và $y_1^1$ và đặt kết quả vào vị trí của chúng, v.v.
Kết quả chúng ta nhận được:

$$a = \bigg\{ \Big[y_0^0 + w_n^0 y_0^1, y_1^0 + w_n^1 y_1^1, y_2^0 + w_n^2 y_2^1, y_3^0 + w_n^3 y_3^1\Big], \Big[y_0^0 - w_n^0 y_0^1, y_1^0 - w_n^1 y_1^1, y_2^0 - w_n^2 y_2^1, y_3^0 - w_n^3 y_3^1\Big] \bigg\}$$

Như vậy chúng ta đã tính toán DFT cần thiết từ vectơ $a$.

Ở đây chúng tôi đã mô tả quá trình tính toán DFT chỉ ở mức đệ quy đầu tiên, nhưng điều tương tự rõ ràng cũng hoạt động cho tất cả các mức khác.
Do đó, sau khi áp dụng hoán vị đảo ngược bit, chúng ta có thể tính toán DFT tại chỗ, mà không cần thêm bộ nhớ.

Điều này bổ sung cho phép chúng ta loại bỏ đệ quy.
Chúng ta chỉ cần bắt đầu ở mức thấp nhất, tức là chúng ta chia vectơ thành các cặp và áp dụng biến đổi bướm cho chúng.
Kết quả là vectơ $a$ với công việc của mức cuối cùng đã được áp dụng.
Trong bước tiếp theo, chúng ta chia vectơ thành các vectơ có kích thước $4$, và lại áp dụng biến đổi bướm, cho chúng ta DFT cho mỗi khối có kích thước $4$.
Và cứ thế tiếp tục.
Cuối cùng ở bước cuối cùng, chúng ta thu được kết quả của các DFT của cả hai nửa của $a$, và bằng cách áp dụng biến đổi bướm, chúng ta thu được DFT cho vectơ $a$ hoàn chỉnh.

```{.cpp file=fft_implementation_iterative}
using cd = complex<double>;
const double PI = acos(-1);

int reverse(int num, int lg_n) {
    int res = 0;
    for (int i = 0; i < lg_n; i++) {
        if (num & (1 << i))
            res |= 1 << (lg_n - 1 - i);
    }
    return res;
}

void fft(vector<cd> & a, bool invert) {
    int n = a.size();
    int lg_n = 0;
    while ((1 << lg_n) < n)
        lg_n++;

    for (int i = 0; i < n; i++) {
        if (i < reverse(i, lg_n))
            swap(a[i], a[reverse(i, lg_n)]);
    }

    for (int len = 2; len <= n; len <<= 1) {
        double ang = 2 * PI / len * (invert ? -1 : 1);
        cd wlen(cos(ang), sin(ang));
        for (int i = 0; i < n; i += len) {
            cd w(1);
            for (int j = 0; j < len / 2; j++) {
                cd u = a[i+j], v = a[i+j+len/2] * w;
                a[i+j] = u + v;
                a[i+j+len/2] = u - v;
                w *= wlen;
            }
        }
    }

    if (invert) {
        for (cd & x : a)
            x /= n;
    }
}
```

Đầu tiên chúng tôi áp dụng hoán vị đảo ngược bit bằng cách tráo đổi từng phần tử với phần tử của vị trí bị đảo ngược.
Sau đó, $\log n - 1$ trạng thái của thuật toán chúng tôi tính toán DFT cho mỗi khối có kích thước tương ứng $\text{len}$.
Đối với tất cả các khối đó, chúng ta có cùng một căn của đơn vị $\text{wlen}$.
Chúng tôi lặp lại tất cả các khối và thực hiện biến đổi bướm trên mỗi khối đó.

Chúng ta có thể tối ưu hóa hơn nữa việc đảo ngược các bit.
Trong cài đặt trước, chúng tôi lặp lại tất cả các bit của chỉ số và tạo chỉ số bị đảo ngược bit.
Tuy nhiên, chúng ta có thể đảo ngược các bit theo một cách khác.

Giả sử rằng $j$ đã chứa đảo ngược của $i$.
Sau đó để đi đến $i + 1$, chúng ta phải tăng $i$, và chúng ta cũng phải tăng $j$, nhưng trong một hệ thống số "đảo ngược".
Cộng một trong hệ nhị phân thông thường tương đương với việc lật tất cả các số một ở đuôi thành số không và lật số không ngay trước chúng thành số một.
Tương đương trong hệ thống số "đảo ngược", chúng ta lật tất cả các số một dẫn đầu, và cũng là số không tiếp theo.

Do đó chúng ta nhận được cài đặt sau:

```{.cpp file=fft_implementation_iterative_opt}
using cd = complex<double>;
const double PI = acos(-1);

void fft(vector<cd> & a, bool invert) {
    int n = a.size();

    for (int i = 1, j = 0; i < n; i++) {
        int bit = n >> 1;
        for (; j & bit; bit >>= 1)
            j ^= bit;
        j ^= bit;

        if (i < j)
            swap(a[i], a[j]);
    }

    for (int len = 2; len <= n; len <<= 1) {
        double ang = 2 * PI / len * (invert ? -1 : 1);
        cd wlen(cos(ang), sin(ang));
        for (int i = 0; i < n; i += len) {
            cd w(1);
            for (int j = 0; j < len / 2; j++) {
                cd u = a[i+j], v = a[i+j+len/2] * w;
                a[i+j] = u + v;
                a[i+j+len/2] = u - v;
                w *= wlen;
            }
        }
    }

    if (invert) {
        for (cd & x : a)
            x /= n;
    }
}
```

Ngoài ra chúng ta có thể tính trước hoán vị đảo ngược bit từ trước.
Điều này đặc biệt hữu ích khi kích thước $n$ giống nhau cho tất cả các cuộc gọi.
Nhưng ngay cả khi chúng ta chỉ có ba cuộc gọi (cần thiết để nhân hai đa thức), hiệu quả là đáng chú ý.
Ngoài ra, chúng ta có thể tính trước tất cả các căn của đơn vị và lũy thừa của chúng.

## Biến đổi lý thuyết số (Number theoretic transform) {: #number-theoretic-transform}

Bây giờ chúng ta chuyển mục tiêu một chút.
Chúng ta vẫn muốn nhân hai đa thức trong thời gian $O(n \log n)$, nhưng lần này chúng ta muốn tính toán các hệ số modulo một số nguyên tố $p$.
Tất nhiên đối với nhiệm vụ này, chúng ta có thể sử dụng DFT thông thường và áp dụng toán tử modulo cho kết quả.
Tuy nhiên, làm như vậy có thể dẫn đến sai số làm tròn, đặc biệt khi xử lý các số lớn.
**Biến đổi lý thuyết số (number theoretic transform - NTT)** có lợi thế là nó chỉ hoạt động với số nguyên, và do đó kết quả được đảm bảo là chính xác.
 
Biến đổi Fourier rời rạc dựa trên các số phức, và các căn bậc $n$ của đơn vị.
Để tính toán hiệu quả nó, chúng ta sử dụng rộng rãi các tính chất của các căn (ví dụ: có một căn tạo ra tất cả các căn khác bằng phép lũy thừa).

Nhưng các tính chất tương tự cũng giữ cho các căn bậc $n$ của đơn vị trong số học modulo.
Một căn bậc $n$ của đơn vị dưới một trường nguyên thủy là một số $w_n$ thỏa mãn:

$$\begin{align}
(w_n)^n &= 1 \pmod{p}, \\
(w_n)^k &\ne 1 \pmod{p}, \quad 1 \le k < n.
\end{align}$$

$n-1$ căn khác có thể thu được dưới dạng lũy thừa của căn $w_n$.

Để áp dụng nó trong thuật toán biến đổi Fourier nhanh, chúng ta cần một căn tồn tại cho một số $n$, là lũy thừa của $2$, và cũng cho tất cả các lũy thừa nhỏ hơn.
Chúng ta có thể nhận thấy tính chất thú vị sau:

$$\begin{align}
(w_n^2)^m = w_n^n &= 1 \pmod{p}, \quad \text{với } m = \frac{n}{2}\\
(w_n^2)^k = w_n^{2k} &\ne 1 \pmod{p}, \quad 1 \le k < m.
\end{align}$$

Do đó nếu $w_n$ là căn bậc $n$ của đơn vị, thì $w_n^2$ là căn bậc $\frac{n}{2}$ của đơn vị.
Và kết quả là đối với tất cả các lũy thừa nhỏ hơn của hai đều tồn tại các căn có bậc yêu cầu, và chúng có thể được tính toán bằng cách sử dụng $w_n$.

Để tính toán DFT ngược, chúng ta cần nghịch đảo $w_n^{-1}$ của $w_n$.
Nhưng đối với modulo số nguyên tố, nghịch đảo luôn tồn tại.

Do đó, tất cả các tính chất mà chúng ta cần từ các căn phức cũng có sẵn trong số học modulo, miễn là chúng ta có một modulo $p$ đủ lớn mà căn bậc $n$ của đơn vị tồn tại.

Ví dụ, chúng ta có thể lấy các giá trị sau: modulo $p = 7340033$, $w_{2^{20}} = 5$.
Nếu modulo này không đủ, chúng ta cần tìm một cặp khác.
Chúng ta có thể sử dụng thực tế rằng đối với các modulo có dạng $p = c 2^k + 1$ (và $p$ là số nguyên tố), luôn tồn tại căn bậc $2^k$ của đơn vị.
Có thể chứng minh rằng $g^c$ là một căn bậc $2^k$ của đơn vị như vậy, trong đó $g$ là một [căn nguyên thủy](primitive-root.md) của $p$.

```{.cpp file=fft_implementation_modular_arithmetic}
const int mod = 7340033;
const int root = 5;
const int root_1 = 4404020;
const int root_pw = 1 << 20;

void fft(vector<int> & a, bool invert) {
    int n = a.size();

    for (int i = 1, j = 0; i < n; i++) {
        int bit = n >> 1;
        for (; j & bit; bit >>= 1)
            j ^= bit;
        j ^= bit;

        if (i < j)
            swap(a[i], a[j]);
    }

    for (int len = 2; len <= n; len <<= 1) {
        int wlen = invert ? root_1 : root;
        for (int i = len; i < root_pw; i <<= 1)
            wlen = (int)(1LL * wlen * wlen % mod);

        for (int i = 0; i < n; i += len) {
            int w = 1;
            for (int j = 0; j < len / 2; j++) {
                int u = a[i+j], v = (int)(1LL * a[i+j+len/2] * w % mod);
                a[i+j] = u + v < mod ? u + v : u + v - mod;
                a[i+j+len/2] = u - v >= 0 ? u - v : u - v + mod;
                w = (int)(1LL * w * wlen % mod);
            }
        }
    }

    if (invert) {
        int n_1 = inverse(n, mod);
        for (int & x : a)
            x = (int)(1LL * x * n_1 % mod);
    }
}
```

Ở đây hàm `inverse` tính toán nghịch đảo modulo (xem [Nghịch đảo nhân Modulo](module-inverse.md)).
Các hằng số `mod`, `root`, `root_pw` xác định modulo và căn, và `root_1` là nghịch đảo của `root` modulo `mod`.

Trong thực tế, cài đặt này chậm hơn so với cài đặt sử dụng số phức (do số lượng lớn các phép toán modulo), nhưng nó có một số ưu điểm như sử dụng ít bộ nhớ hơn và không có lỗi làm tròn.

## Phép nhân với modulo tùy ý (Multiplication with arbitrary modulus) {: #multiplication-with-arbitrary-modulus}

Ở đây chúng ta muốn đạt được cùng một mục tiêu như trong phần trước.
Nhân hai đa thức $A(x)$ và $B(x)$, và tính toán các hệ số modulo một số $M$.
Biến đổi lý thuyết số chỉ hoạt động cho một số số nguyên tố nhất định.
Còn trường hợp modulo không có dạng mong muốn thì sao?

Một tùy chọn sẽ là thực hiện nhiều biến đổi lý thuyết số với các số nguyên tố khác nhau có dạng $c 2^k + 1$, sau đó áp dụng [Định lý Thặng dư Trung Hoa](chinese-remainder-theorem.md) để tính toán các hệ số cuối cùng.

Tùy chọn khác là phân phối các đa thức $A(x)$ và $B(x)$ thành hai đa thức nhỏ hơn mỗi đa thức

$$\begin{align}
A(x) &= A_1(x) + A_2(x) \cdot C \\
B(x) &= B_1(x) + B_2(x) \cdot C
\end{align}$$

với $C \approx \sqrt{M}$.

Khi đó tích của $A(x)$ và $B(x)$ có thể được biểu diễn dưới dạng:

$$A(x) \cdot B(x) = A_1(x) \cdot B_1(x) + \left(A_1(x) \cdot B_2(x) + A_2(x) \cdot B_1(x)\right)\cdot C + \left(A_2(x) \cdot B_2(x)\right)\cdot C^2$$

Các đa thức $A_1(x)$, $A_2(x)$, $B_1(x)$ và $B_2(x)$ chỉ chứa các hệ số nhỏ hơn $\sqrt{M}$, do đó các hệ số của tất cả các tích xuất hiện đều nhỏ hơn $M \cdot n$, thường đủ nhỏ để xử lý với các kiểu dấu phẩy động điển hình.

Do đó, cách tiếp cận này yêu cầu tính toán tích của các đa thức với các hệ số nhỏ hơn (bằng cách sử dụng FFT thông thường và FFT ngược), và sau đó tích ban đầu có thể được khôi phục bằng cách sử dụng phép cộng và phép nhân modulo trong thời gian $O(n)$.

## Các ứng dụng (Applications) {: #applications}

DFT có thể được sử dụng trong rất nhiều bài toán khác, thoạt nhìn không liên quan gì đến nhân đa thức.

### Tất cả các tổng có thể (All possible sums) {: #all-possible-sums}

Chúng ta được cho hai mảng $a[]$ và $b[]$.
Chúng ta phải tìm tất cả các tổng có thể $a[i] + b[j]$, và đối với mỗi tổng đếm xem nó xuất hiện bao nhiêu lần.

Ví dụ đối với $a = [1,~ 2,~ 3]$ và $b = [2,~ 4]$ chúng ta nhận được:
khi đó tổng $3$ có thể thu được theo $1$ cách, tổng $4$ cũng theo $1$ cách, $5$ theo $2$ cách, $6$ theo $1$ cách, $7$ theo $1$ cách.

Chúng ta xây dựng cho các mảng $a$ và $b$ hai đa thức $A$ và $B$.
Các số của mảng sẽ đóng vai trò là số mũ trong đa thức ($a[i] \Rightarrow x^{a[i]}$); và các hệ số của số hạng này sẽ là tần xuất xuất hiện của số đó trong mảng.

Sau đó, bằng cách nhân hai đa thức này trong thời gian $O(n \log n)$, chúng ta nhận được một đa thức $C$, trong đó các số mũ sẽ cho biết tổng nào có thể thu được, và các hệ số cho biết tần suất.
Để minh họa điều này trên ví dụ:

$$(1 x^1 + 1 x^2 + 1 x^3) (1 x^2 + 1 x^4) = 1 x^3 + 1 x^4 + 2 x^5 + 1 x^6 + 1 x^7$$

### Tất cả các tích vô hướng có thể (All possible scalar products) {: #all-possible-scalar-products}

Chúng ta được cho hai mảng $a[]$ và $b[]$ có độ dài $n$.
Chúng ta phải tính toán tích của $a$ với mọi dịch chuyển vòng của $b$.

Chúng ta tạo ra hai mảng mới có kích thước $2n$:
Chúng ta đảo ngược $a$ và thêm $n$ số không vào nó.
Và chúng ta chỉ cần thêm $b$ vào chính nó.
Khi chúng ta nhân hai mảng này như đa thức, và nhìn vào các hệ số $c[n-1],~ c[n],~ \dots,~ c[2n-2]$ của tích $c$, chúng ta nhận được:

$$c[k] = \sum_{i+j=k} a[i] b[j]$$

Và vì tất cả các phần tử $a[i] = 0$ với $i \ge n$:

$$c[k] = \sum_{i=0}^{n-1} a[i] b[k-i]$$

Dễ dàng thấy rằng tổng này chỉ là tích vô hướng của vectơ $a$ với dịch chuyển vòng trái thứ $(k - (n - 1))$ của $b$.
Do đó, các hệ số này là câu trả lời cho bài toán, và chúng ta vẫn có thể thu được nó trong thời gian $O(n \log n)$.
Lưu ý ở đây rằng $c[2n-1]$ cũng cung cấp cho chúng ta dịch chuyển vòng thứ $n$ nhưng đó cũng giống như dịch chuyển vòng thứ $0$ nên chúng ta không cần xem xét riêng biệt vào câu trả lời của mình.

### Hai dải (Two stripes) {: #two-stripes}

Chúng ta được cho hai dải Boolean (mảng vòng các giá trị $0$ và $1$) $a$ và $b$.
Chúng ta muốn tìm tất cả các cách để gắn dải thứ nhất vào dải thứ hai, sao cho tại không vị trí nào chúng ta có số $1$ của dải thứ nhất bên cạnh số $1$ của dải thứ hai.

Bài toán thực sự không khác nhiều so với bài toán trước.
Gắn hai dải chỉ có nghĩa là chúng ta thực hiện dịch chuyển vòng trên mảng thứ hai, và chúng ta có thể gắn hai dải, nếu tích vô hướng của hai mảng là $0$.

### Khớp chuỗi (String matching) {: #string-matching}

Chúng ta được cho hai chuỗi, một văn bản $T$ và một mẫu $P$, bao gồm các chữ cái thường.
Chúng ta phải tính toán tất cả các lần xuất hiện của mẫu trong văn bản.

Chúng ta tạo một đa thức cho mỗi chuỗi ($T[i]$ và $P[I]$ là các số từ $0$ đến $25$ tương ứng với $26$ chữ cái của bảng chữ cái):

$$A(x) = a_0 x^0 + a_1 x^1 + \dots + a_{n-1} x^{n-1}, \quad n = |T|$$

với

$$a_i = \cos(\alpha_i) + i \sin(\alpha_i), \quad \alpha_i = \frac{2 \pi T[i]}{26}.$$

Và

$$B(x) = b_0 x^0 + b_1 x^1 + \dots + b_{m-1} x^{m-1}, \quad m = |P|$$

với

$$b_i = \cos(\beta_i) - i \sin(\beta_i), \quad \beta_i = \frac{2 \pi P[m-i-1]}{26}.$$

Lưu ý rằng với biểu thức $P[m-i-1]$ đảo ngược mẫu một cách rõ ràng.

Hệ số thứ $(m-1+i)$ của tích của hai đa thức $C(x) = A(x) \cdot B(x)$ sẽ cho chúng ta biết, nếu mẫu xuất hiện trong văn bản tại vị trí $i$.

$$c_{m-1+i} = \sum_{j = 0}^{m-1} a_{i+j} \cdot b_{m-1-j} = \sum_{j=0}^{m-1} \left(\cos(\alpha_{i+j}) + i \sin(\alpha_{i+j})\right) \cdot \left(\cos(\beta_j) - i \sin(\beta_j)\right)$$

với $\alpha_{i+j} = \frac{2 \pi T[i+j]}{26}$ và $\beta_j = \frac{2 \pi P[j]}{26}$

Nếu có một sự trùng khớp, thì $T[i+j] = P[j]$, và do đó $\alpha_{i+j} = \beta_j$.
Điều này đưa ra (sử dụng đẳng thức lượng giác Pythagore):

$$\begin{align}
c_{m-1+i} &= \sum_{j = 0}^{m-1}  \left(\cos(\alpha_{i+j}) + i \sin(\alpha_{i+j})\right) \cdot \left(\cos(\alpha_{i+j}) - i \sin(\alpha_{i+j})\right) \\
&= \sum_{j = 0}^{m-1} \cos(\alpha_{i+j})^2 + \sin(\alpha_{i+j})^2 = \sum_{j = 0}^{m-1} 1 = m
\end{align}$$

Nếu không có sự trùng khớp, thì ít nhất một ký tự là khác nhau, dẫn đến một trong các tích $a_{i+1} \cdot b_{m-1-j}$ không bằng $1$, dẫn đến hệ số $c_{m-1+i} \ne m$.

### Khớp chuỗi với ký tự đại diện (String matching with wildcards) {: #string-matching-with-wildcards}

Đây là một phần mở rộng của bài toán trước.
Lần này chúng ta cho phép mẫu chứa ký tự đại diện $\*$, có thể khớp với mọi chữ cái có thể.
Ví dụ: mẫu $a*c$ xuất hiện trong văn bản $abccaacc$ tại chính xác ba vị trí, tại chỉ số $0$, chỉ số $4$ và chỉ số $5$.

Chúng ta tạo ra các đa thức hoàn toàn giống nhau, ngoại trừ việc chúng ta đặt $b_i = 0$ nếu $P[m-i-1] = *$.
Nếu $x$ là số lượng ký tự đại diện trong $P$, thì chúng ta sẽ có một sự trùng khớp của $P$ trong $T$ tại chỉ số $i$ nếu $c_{m-1+i} = m - x$.

## Bài tập luyện tập {: #practice-problems}

- [SPOJ - POLYMUL](http://www.spoj.com/problems/POLYMUL/)
- [SPOJ - MAXMATCH](http://www.spoj.com/problems/MAXMATCH/)
- [SPOJ - ADAMATCH](http://www.spoj.com/problems/ADAMATCH/)
- [Codeforces - Yet Another String Matching Problem](http://codeforces.com/problemset/problem/954/I)
- [Codeforces - Lightsabers (hard)](http://codeforces.com/problemset/problem/958/F3)
- [Codeforces - Running Competition](https://codeforces.com/contest/1398/problem/G)
- [Kattis - A+B Problem](https://open.kattis.com/problems/aplusb)
- [Kattis - K-Inversions](https://open.kattis.com/problems/kinversions)
- [Codeforces - Dasha and cyclic table](http://codeforces.com/contest/754/problem/E)
- [CodeChef - Expected Number of Customers](https://www.codechef.com/COOK112A/problems/MMNN01)
- [CodeChef - Power Sum](https://www.codechef.com/SEPT19A/problems/PSUM)
- [Codeforces - Centroid Probabilities](https://codeforces.com/problemset/problem/1667/E)
