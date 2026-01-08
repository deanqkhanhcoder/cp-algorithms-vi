---
tags:
  - Translated
e_maxx_link: z_function
---

# Hàm Z và cách tính toán (Z-function and its calculation) {: #z-function-and-its-calculation}

Giả sử chúng ta được cho một chuỗi $s$ có độ dài $n$. **Hàm Z (Z-function)** cho chuỗi này là một mảng có độ dài $n$ trong đó phần tử thứ $i$ bằng số lượng ký tự lớn nhất bắt đầu từ vị trí $i$ trùng khớp với các ký tự đầu tiên của $s$.

Nói cách khác, $z[i]$ là độ dài của chuỗi dài nhất đồng thời là tiền tố của $s$ và là tiền tố của hậu tố của $s$ bắt đầu tại $i$.

**Lưu ý.** Trong bài viết này, để tránh mơ hồ, chúng tôi giả sử chỉ số bắt đầu từ $0$; tức là: ký tự đầu tiên của $s$ có chỉ số $0$ và ký tự cuối cùng có chỉ số $n-1$.

Phần tử đầu tiên của hàm Z, $z[0]$, thường không được định nghĩa rõ ràng. Trong bài viết này, chúng tôi sẽ giả sử nó bằng không (mặc dù nó không thay đổi bất cứ điều gì trong việc cài đặt thuật toán).

Bài viết này trình bày một thuật toán để tính toán hàm Z trong thời gian $O(n)$, cũng như các ứng dụng khác nhau của nó.

## Ví dụ (Examples) {: #examples}

Ví dụ, đây là các giá trị của hàm Z được tính toán cho các chuỗi khác nhau:

* "aaaaa" - $[0, 4, 3, 2, 1]$
* "aaabaab" - $[0, 2, 1, 0, 2, 1, 0]$
* "abacaba" - $[0, 0, 1, 0, 3, 0, 1]$

## Thuật toán tầm thường (Trivial algorithm) {: #trivial-algorithm}

Định nghĩa chính thức có thể được biểu diễn trong cài đặt sơ cấp $O(n^2)$ sau đây.

```cpp
vector<int> z_function_trivial(string s) {
	int n = s.size();
	vector<int> z(n);
	for (int i = 1; i < n; i++) {
		while (i + z[i] < n && s[z[i]] == s[i + z[i]]) {
			z[i]++;
		}
	}
	return z;
}
```

Chúng ta chỉ cần lặp qua mọi vị trí $i$ và cập nhật $z[i]$ cho mỗi vị trí đó, bắt đầu từ $z[i] = 0$ và tăng dần miễn là chúng ta không tìm thấy sự không khớp (và miễn là chúng ta không đến cuối dòng).

Tất nhiên, đây không phải là một cài đặt hiệu quả. Bây giờ chúng tôi sẽ hiển thị việc xây dựng một cài đặt hiệu quả.

## Thuật toán hiệu quả để tính hàm Z (Efficient algorithm to compute the Z-function) {: #efficient-algorithm-to-compute-the-z-function}

Để có được một thuật toán hiệu quả, chúng ta sẽ tính toán các giá trị của $z[i]$ lần lượt từ $i = 1$ đến $n - 1$ nhưng đồng thời, khi tính toán một giá trị mới, chúng ta sẽ cố gắng tận dụng tốt nhất có thể các giá trị đã được tính toán trước đó.

Để ngắn gọn, hãy gọi **đoạn khớp (segment matches)** là những chuỗi con trùng khớp với tiền tố của $s$. Ví dụ: giá trị của hàm Z mong muốn $z[i]$ là độ dài của đoạn khớp bắt đầu tại vị trí $i$ (và kết thúc tại vị trí $i + z[i] - 1$).

Để làm điều này, chúng ta sẽ giữ **các chỉ số $[l, r)$ của đoạn khớp ngoài cùng bên phải**. Tức là, trong số tất cả các đoạn được phát hiện, chúng ta sẽ giữ đoạn kết thúc xa nhất về bên phải. Theo một cách nào đó, chỉ số $r$ có thể được coi là "biên giới" mà chuỗi $s$ của chúng ta đã được quét bởi thuật toán; mọi thứ nằm ngoài điểm đó vẫn chưa được biết.

Sau đó, nếu chỉ số hiện tại (mà chúng ta phải tính toán giá trị tiếp theo của hàm Z) là $i$, chúng ta có một trong hai tùy chọn:

*   $i \geq r$ -- vị trí hiện tại nằm **bên ngoài** những gì chúng ta đã xử lý.

    Sau đó, chúng ta sẽ tính toán $z[i]$ với **thuật toán tầm thường** (tức là chỉ so sánh từng giá trị một). Lưu ý rằng cuối cùng, nếu $z[i] > 0$, chúng ta sẽ phải cập nhật các chỉ số của đoạn ngoài cùng bên phải, bởi vì đảm bảo rằng $r = i + z[i]$ mới tốt hơn $r$ trước đó.

*   $i < r$ -- vị trí hiện tại nằm bên trong đoạn khớp hiện tại $[l, r)$.

    Sau đó, chúng ta có thể sử dụng các giá trị Z đã tính toán để "khởi tạo" giá trị của $z[i]$ thành một cái gì đó (chắc chắn tốt hơn là "bắt đầu từ không"), thậm chí có thể là một số lớn.

    Để làm điều này, chúng ta quan sát thấy rằng các chuỗi con $s[l \dots r)$ và $s[0 \dots r-l)$ **khớp nhau**. Điều này có nghĩa là như một xấp xỉ ban đầu cho $z[i]$, chúng ta có thể lấy giá trị đã được tính toán cho đoạn tương ứng $s[0 \dots r-l)$, và đó là $z[i-l]$.

    Tuy nhiên, giá trị $z[i-l]$ có thể quá lớn: khi áp dụng cho vị trí $i$ nó có thể vượt quá chỉ số $r$. Điều này không được phép vì chúng ta không biết gì về các ký tự bên phải của $r$: chúng có thể khác với những ký tự được yêu cầu.

    Dưới đây là **một ví dụ** về một kịch bản tương tự:

    $$ s = "aaaabaa" $$

    Khi chúng ta đến vị trí cuối cùng ($i = 6$), đoạn khớp hiện tại sẽ là $[5, 7)$. Vị trí $6$ sau đó sẽ khớp với vị trí $6 - 5 = 1$, mà giá trị của hàm Z là $z[1] = 3$. Rõ ràng, chúng ta không thể khởi tạo $z[6]$ thành $3$, nó sẽ hoàn toàn không chính xác. Giá trị lớn nhất mà chúng ta có thể khởi tạo nó là $1$ -- bởi vì đó là giá trị lớn nhất không đưa chúng ta vượt quá chỉ số $r$ của đoạn khớp $[l, r)$.

    Do đó, như một **xấp xỉ ban đầu** cho $z[i]$, chúng ta có thể lấy một cách an toàn:

    $$ z_0[i] = \min(r - i,\; z[i-l]) $$

    Sau khi có $z[i]$ được khởi tạo thành $z_0[i]$, chúng ta cố gắng tăng $z[i]$ bằng cách chạy **thuật toán tầm thường** -- bởi vì nói chung, sau biên giới $r$, chúng ta không thể biết liệu đoạn đó có tiếp tục khớp hay không.

Do đó, toàn bộ thuật toán được chia thành hai trường hợp, chỉ khác nhau ở **giá trị ban đầu** của $z[i]$: trong trường hợp đầu tiên nó được giả định là không, trong trường hợp thứ hai nó được xác định bởi các giá trị đã được tính toán trước đó (sử dụng công thức trên). Sau đó, cả hai nhánh của thuật toán này có thể được rút gọn thành việc thực hiện **thuật toán tầm thường**, bắt đầu ngay sau khi chúng ta chỉ định giá trị ban đầu.

Thuật toán hóa ra rất đơn giản. Mặc dù thực tế là trên mỗi lần lặp, thuật toán tầm thường được chạy, chúng ta đã đạt được tiến bộ đáng kể, có một thuật toán chạy trong thời gian tuyến tính. Sau này chúng ta sẽ chứng minh rằng thời gian chạy là tuyến tính.

## Cài đặt (Implementation) {: #implementation}

Việc cài đặt hóa ra khá ngắn gọn:

```cpp
vector<int> z_function(string s) {
    int n = s.size();
    vector<int> z(n);
    int l = 0, r = 0;
    for(int i = 1; i < n; i++) {
        if(i < r) {
            z[i] = min(r - i, z[i - l]);
        }
        while(i + z[i] < n && s[z[i]] == s[i + z[i]]) {
            z[i]++;
        }
        if(i + z[i] > r) {
            l = i;
            r = i + z[i];
        }
    }
    return z;
}
```

### Nhận xét về việc cài đặt (Comments on this implementation) {: #comments-on-this-implementation}

Toàn bộ giải pháp được đưa ra dưới dạng một hàm trả về một mảng có độ dài $n$ -- hàm Z của $s$.

Mảng $z$ ban đầu được điền bằng các số không. Đoạn khớp ngoài cùng bên phải hiện tại được giả định là $[0; 0)$ (tức là một đoạn nhỏ một cách cố ý không chứa bất kỳ $i$ nào).

Bên trong vòng lặp cho $i = 1 \dots n - 1$, trước tiên chúng ta xác định giá trị ban đầu $z[i]$ -- nó sẽ vẫn bằng không hoặc được tính toán bằng công thức trên.

Sau đó, thuật toán tầm thường cố gắng tăng giá trị của $z[i]$ càng nhiều càng tốt.

Cuối cùng, nếu được yêu cầu (tức là nếu $i + z[i] > r$), chúng ta cập nhật đoạn khớp ngoài cùng bên phải $[l, r)$.

## Hành vi tiệm cận của thuật toán (Asymptotic behavior of the algorithm) {: #asymptotic-behavior-of-the-algorithm}

Chúng ta sẽ chứng minh rằng thuật toán trên có thời gian chạy tuyến tính theo độ dài của chuỗi -- do đó, nó là $O(n)$.

Bằng chứng rất đơn giản.

Chúng ta quan tâm đến vòng lặp `while` lồng nhau, vì mọi thứ khác chỉ là một loạt các hoạt động hằng số cộng lại thành $O(n)$.

Chúng taseẽ chỉ ra rằng **mỗi lần lặp** của vòng lặp `while` sẽ tăng biên giới bên phải $r$ của đoạn khớp.

Để làm điều đó, chúng ta sẽ xem xét cả hai nhánh của thuật toán:

*   $i \geq r$

    Trong trường hợp này, vòng lặp `while` sẽ không thực hiện bất kỳ lần lặp nào (nếu $s[0] \ne s[i]$), hoặc nó sẽ mất một vài lần lặp, bắt đầu tại vị trí $i$, mỗi lần di chuyển một ký tự sang phải. Sau đó, biên giới bên phải $r$ nhất thiết sẽ được cập nhật.

    Vì vậy, chúng ta đã thấy rằng, khi $i \geq r$, mỗi lần lặp của vòng lặp `while` làm tăng giá trị của chỉ số $r$ mới.

*   $i < r$

    Trong trường hợp này, chúng ta khởi tạo $z[i]$ thành một giá trị nhất định $z_0$ được đưa ra bởi công thức trên. Hãy so sánh giá trị ban đầu $z_0$ này với giá trị $r - i$. Chúng ta sẽ có ba trường hợp:

      *   $z_0 < r - i$

          Chúng ta chứng minh rằng trong trường hợp này không có lần lặp nào của vòng lặp `while` sẽ diễn ra.

          Rất dễ để chứng minh, ví dụ, bằng mâu thuẫn: nếu vòng lặp `while` thực hiện ít nhất một lần lặp, điều đó có nghĩa là xấp xỉ ban đầu $z[i] = z_0$ là không chính xác (nhỏ hơn độ dài thực tế của khớp). Nhưng vì $s[l \dots r)$ và $s[0 \dots r-l)$ giống nhau, điều này ngụ ý rằng $z[i-l]$ giữ giá trị sai (nhỏ hơn mức cần thiết).

          Do đó, vì $z[i-l]$ là chính xác và nó nhỏ hơn $r - i$, suy ra giá trị này trùng với giá trị bắt buộc $z[i]$.

      *   $z_0 = r - i$

          Trong trường hợp này, vòng lặp `while` có thể thực hiện một vài lần lặp, nhưng mỗi lần trong số đó sẽ dẫn đến sự gia tăng giá trị của chỉ số $r$ bởi vì chúng ta sẽ bắt đầu so sánh từ $s[r]$, sẽ leo ra ngoài khoảng $[l, r)$.

      *   $z_0 > r - i$

          Tùy chọn này là không thể, theo định nghĩa của $z_0$.

Vì vậy, chúng ta đã chứng minh rằng mỗi lần lặp của vòng lặp bên trong làm cho con trỏ $r$ tiến sang phải. Vì $r$ không thể lớn hơn $n-1$, điều này có nghĩa là vòng lặp bên trong sẽ không thực hiện quá $n-1$ lần lặp.

Vì phần còn lại của thuật toán hoạt động rõ ràng trong $O(n)$, chúng ta đã chứng minh rằng toàn bộ thuật toán để tính toán hàm Z chạy trong thời gian tuyến tính.

## Ứng dụng (Applications) {: #applications}

Bây giờ chúng ta sẽ xem xét một số cách sử dụng hàm Z cho các nhiệm vụ cụ thể.

Các ứng dụng này sẽ phần lớn tương tự như các ứng dụng của [hàm tiền tố](prefix-function.md).

### Tìm kiếm chuỗi con (Search the substring) {: #search-the-substring}

Để tránh nhầm lẫn, chúng ta gọi $t$ là **chuỗi văn bản**, và $p$ là **mẫu**. Bài toán là: tìm tất cả các lần xuất hiện của mẫu $p$ bên trong văn bản $t$.

Để giải quyết vấn đề này, chúng ta tạo ra một chuỗi mới $s = p + \diamond + t$, tức là, chúng ta áp dụng nối chuỗi cho $p$ và $t$ nhưng chúng ta cũng đặt một ký tự phân cách $\diamond$ ở giữa (chúng ta sẽ chọn $\diamond$ để nó chắc chắn sẽ không hiện diện ở bất cứ đâu trong các chuỗi $p$ hoặc $t$).

Tính hàm Z cho $s$. Sau đó, đối với bất kỳ $i$ nào trong khoảng $[0; \; \operatorname{length}(t) - 1]$, chúng ta sẽ xem xét giá trị tương ứng $k = z[i + \operatorname{length}(p) + 1]$. Nếu $k$ bằng $\operatorname{length}(p)$ thì chúng ta biết có một lần xuất hiện của $p$ ở vị trí thứ $i$ của $t$, ngược lại không có sự xuất hiện nào của $p$ ở vị trí thứ $i$ của $t$.

Thời gian chạy (và mức tiêu thụ bộ nhớ) là $O(\operatorname{length}(t) + \operatorname{length}(p))$.

### Số lượng chuỗi con riêng biệt trong một chuỗi (Number of distinct substrings in a string) {: #number-of-distinct-substrings-in-a-string}

Cho một chuỗi $s$ có độ dài $n$, hãy đếm số lượng chuỗi con riêng biệt của $s$.

Chúng ta sẽ giải quyết vấn đề này một cách lặp đi lặp lại. Tức là: biết số lượng chuỗi con khác nhau hiện tại, tính toán lại lượng này sau khi thêm vào cuối $s$ một ký tự.

Vì vậy, hãy để $k$ là số lượng chuỗi con riêng biệt hiện tại của $s$. Chúng ta thêm một ký tự mới $c$ vào $s$. Rõ ràng, có thể có một số chuỗi con mới kết thúc bằng ký tự mới $c$ này (cụ thể là tất cả các chuỗi kết thúc bằng ký hiệu này và chúng ta chưa gặp).

Lấy một chuỗi $t = s + c$ và đảo ngược nó (viết các ký tự của nó theo thứ tự ngược lại). Nhiệm vụ của chúng ta bây giờ là đếm có bao nhiêu tiền tố của $t$ không được tìm thấy ở bất kỳ nơi nào khác trong $t$. Hãy tính hàm Z của $t$ và tìm giá trị tối đa $z_{max}$ của nó. Rõ ràng, tiền tố của $t$ có độ dài $z_{max}$ cũng xuất hiện ở đâu đó ở giữa $t$. Rõ ràng, các tiền tố ngắn hơn cũng xuất hiện.

Vì vậy, chúng ta đã thấy rằng số lượng chuỗi con mới xuất hiện khi ký hiệu $c$ được thêm vào $s$ bằng $\operatorname{length}(t) - z_{max}$.

Do đó, thời gian chạy của giải pháp này là $O(n^2)$ cho một chuỗi có độ dài $n$.

Điều đáng chú ý là theo cách giống hệt nhau, chúng ta có thể tính toán lại, vẫn trong thời gian $O(n)$, số lượng chuỗi con riêng biệt khi thêm một ký tự vào đầu chuỗi, cũng như khi xóa nó (từ cuối hoặc đầu).

### Nén chuỗi (String compression) {: #string-compression}

Cho một chuỗi $s$ có độ dài $n$. Tìm biểu diễn "nén" ngắn nhất của nó, tức là: tìm một chuỗi $t$ có độ dài ngắn nhất sao cho $s$ có thể được biểu diễn dưới dạng nối của một hoặc nhiều bản sao của $t$.

Một giải pháp là: tính hàm Z của $s$, lặp qua tất cả $i$ sao cho $i$ chia hết cho $n$. Dừng lại ở $i$ đầu tiên sao cho $i + z[i] = n$. Sau đó, chuỗi $s$ có thể được nén thành độ dài $i$.

Bằng chứng cho thực tế này giống như giải pháp sử dụng [hàm tiền tố](prefix-function.md).

## Bài tập (Practice Problems) {: #practice-problems}

* [CSES - Finding Borders](https://cses.fi/problemset/task/1732)
* [eolymp - Blocks of string](https://www.eolymp.com/en/problems/1309)
* [Codeforces - Password [Difficulty: Easy]](http://codeforces.com/problemset/problem/126/B)
* [UVA # 455 "Periodic Strings" [Difficulty: Medium]](http://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=396)
* [UVA # 11022 "String Factoring" [Difficulty: Medium]](http://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1963)
* [UVa 11475 - Extend to Palindrome](http://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=2470)
* [LA 6439 - Pasti Pas!](https://icpcarchive.ecs.baylor.edu/index.php?option=com_onlinejudge&Itemid=8&category=588&page=show_problem&problem=4450)
* [Codechef - Chef and Strings](https://www.codechef.com/problems/CHSTR)
* [Codeforces - Prefixes and Suffixes](http://codeforces.com/problemset/problem/432/D)
