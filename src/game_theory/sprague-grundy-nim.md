---
tags:
  - Translated
e_maxx_link: sprague_grundy
---

# Định lý Sprague-Grundy. Nim (Sprague-Grundy theorem. Nim) {: #sprague-grundy-theorem-nim}

## Giới thiệu (Introduction) {: #introduction}

Định lý này mô tả cái gọi là trò chơi hai người chơi **công bằng** (impartial game),
tức là những trò chơi mà các nước đi có sẵn và việc thắng/thua chỉ phụ thuộc vào trạng thái của trò chơi.
Nói cách khác, sự khác biệt duy nhất giữa hai người chơi là một trong hai người đi trước.

Ngoài ra, chúng ta giả sử rằng trò chơi có **thông tin hoàn hảo** (perfect information), tức là không có thông tin nào bị ẩn khỏi người chơi (họ biết luật chơi và các nước đi có thể).

Người ta giả định rằng trò chơi là **hữu hạn** (finite), tức là sau một số lượng nước đi nhất định, một trong hai người chơi sẽ rơi vào vị trí thua — từ đó họ không thể di chuyển đến vị trí khác.
Mặt khác, người chơi đã thiết lập vị trí này cho đối thủ sẽ thắng.
Dễ hiểu là không có kết quả hòa trong trò chơi này.

Trò chơi như vậy có thể được mô tả hoàn toàn bằng một *đồ thị có hướng không chu trình* (DAG): các đỉnh là trạng thái trò chơi và các cạnh là các chuyển đổi (nước đi).
Một đỉnh không có cạnh ra là một đỉnh thua (người chơi phải thực hiện nước đi từ đỉnh này sẽ thua).

Vì không có kết quả hòa, chúng ta có thể phân loại tất cả các trạng thái trò chơi là **thắng** hoặc **thua**.
Trạng thái thắng là những trạng thái mà từ đó có một nước đi gây ra thất bại không thể tránh khỏi cho đối thủ, ngay cả khi họ phản ứng tốt nhất.
Trạng thái thua là những trạng thái mà từ đó mọi nước đi đều dẫn đến trạng thái thắng cho đối thủ.
Tóm lại, một trạng thái là thắng nếu có ít nhất một chuyển đổi đến trạng thái thua và là thua nếu không có ít nhất một chuyển đổi đến trạng thái thua.

Nhiệm vụ của chúng ta là phân loại các trạng thái của một trò chơi nhất định.

Lý thuyết về các trò chơi như vậy được phát triển độc lập bởi Roland Sprague vào năm 1935 và Patrick Michael Grundy vào năm 1939.

## Nim {: #nim}

Trò chơi này tuân theo các hạn chế được mô tả ở trên.
Hơn nữa, *bất kỳ* trò chơi hai người chơi công bằng có thông tin hoàn hảo nào cũng có thể được quy về trò chơi Nim.
Nghiên cứu trò chơi này sẽ cho phép chúng ta giải quyết tất cả các trò chơi tương tự khác, nhưng sẽ nói thêm về điều đó sau.

Về mặt lịch sử, trò chơi này phổ biến từ thời cổ đại.
Nguồn gốc của nó có lẽ là ở Trung Quốc — hoặc ít nhất là trò chơi *Jianshizi* rất giống với nó.
Ở châu Âu, các tài liệu tham khảo sớm nhất về nó là từ thế kỷ 16.
Cái tên này được đặt bởi Charles Bouton, người vào năm 1901 đã công bố một phân tích đầy đủ về trò chơi này.

### Mô tả trò chơi (Game description) {: #game-description}

Có một vài đống sỏi, mỗi đống có một vài viên sỏi.
Trong một nước đi, người chơi có thể lấy bất kỳ số lượng sỏi dương nào từ bất kỳ đống nào và ném chúng đi.
Người chơi thua nếu họ không thể thực hiện nước đi, điều này xảy ra khi tất cả các đống đều trống.

Trạng thái trò chơi được mô tả rõ ràng bởi một đa tập (multiset) các số nguyên dương.
Một nước đi bao gồm việc giảm nghiêm ngặt một số nguyên đã chọn (nếu nó trở thành 0, nó sẽ bị xóa khỏi tập hợp).

### Giải pháp (The solution) {: #the-solution}

Giải pháp của Charles L. Bouton trông như thế này:

**Định lý.**
Người chơi hiện tại có chiến lược thắng khi và chỉ khi tổng xor (xor-sum) của kích thước các đống là khác không.
Tổng xor của một dãy $a$ là $a_1 \oplus a_2 \oplus \ldots \oplus  a_n$, trong đó $\oplus$ là *bitwise exclusive or* (phép XOR bit).

**Chứng minh.**
Chìa khóa của chứng minh là sự hiện diện của một **chiến lược đối xứng cho đối thủ**.
Chúng ta chỉ ra rằng một khi ở vị trí có tổng xor bằng không, người chơi sẽ không thể làm cho nó khác không trong dài hạn —
nếu họ chuyển sang một vị trí có tổng xor khác không, đối thủ sẽ luôn có một nước đi đưa tổng xor trở lại bằng không.

Chúng ta sẽ chứng minh định lý bằng quy nạp toán học.

Đối với Nim rỗng (trong đó tất cả các đống đều trống, tức là đa tập rỗng), tổng xor bằng 0 và định lý là đúng.

Bây giờ giả sử chúng ta đang ở trạng thái không rỗng.
Sử dụng giả thuyết quy nạp (và tính không chu trình của trò chơi), chúng ta giả sử rằng định lý đã được chứng minh cho tất cả các trạng thái có thể truy cập được từ trạng thái hiện tại.

Sau đó, chứng minh chia thành hai phần:
nếu đối với vị trí hiện tại, tổng xor $s = 0$, chúng ta phải chứng minh rằng trạng thái này là thua, tức là tất cả các trạng thái có thể truy cập đều có tổng xor $t \neq 0$.
Nếu $s \neq 0$, chúng ta phải chứng minh rằng có một nước đi dẫn đến trạng thái có $t = 0$.

*   Hãy để $s = 0$ và xem xét bất kỳ nước đi nào.
    Nước đi này làm giảm kích thước của một đống $x$ xuống kích thước $y$.
    Sử dụng các tính chất cơ bản của $\oplus$, chúng ta có
    
    \[ t = s \oplus x \oplus y = 0 \oplus x \oplus y = x \oplus y \]
    
    Vì $y < x$, $y \oplus x$ không thể bằng 0, vì vậy $t \neq 0$.
    Điều đó có nghĩa là bất kỳ trạng thái nào có thể truy cập được đều là thắng (theo giả thuyết quy nạp), vì vậy chúng ta đang ở vị trí thua.

*   Hãy để $s \neq 0$.
    Xem xét biểu diễn nhị phân của số $s$.
    Gọi $d$ là chỉ số của bit khác 0 quan trọng nhất (giá trị lớn nhất) của nó.
    Nước đi của chúng ta sẽ ở trên một đống có bit số $d$ của kích thước được bật (nó phải tồn tại, nếu không bit sẽ không được bật trong $s$).
    Chúng ta sẽ giảm kích thước $x$ của nó xuống $y = x \oplus s$.
    Tất cả các bit ở các vị trí lớn hơn $d$ trong $x$ và $y$ đều khớp và bit $d$ được bật trong $x$ nhưng không được bật trong $y$.
    Do đó, $y < x$, đó là tất cả những gì chúng ta cần để một nước đi là hợp lệ.
    Bây giờ chúng ta có:
    
    \[ t = s \oplus x \oplus y = s \oplus x \oplus (s \oplus x) = 0 \]
    
    Điều này có nghĩa là chúng ta đã tìm thấy một trạng thái thua có thể truy cập được (theo giả thuyết quy nạp) và trạng thái hiện tại là thắng.

**Hệ quả.**
Bất kỳ trạng thái nào của Nim cũng có thể được thay thế bằng một trạng thái tương đương miễn là tổng xor không thay đổi.
Hơn nữa, khi phân tích Nim với nhiều đống, chúng ta có thể thay thế nó bằng một đống duy nhất có kích thước $s$.

### Trò chơi Misère (Misère Game) {: #misere-game}

Trong một **trò chơi misère**, mục tiêu của trò chơi là ngược lại, vì vậy người chơi loại bỏ que cuối cùng sẽ thua trò chơi.
Hóa ra trò chơi misère nim có thể được chơi tối ưu gần giống như trò chơi nim tiêu chuẩn.
Ý tưởng là trước tiên hãy chơi trò chơi misère giống như trò chơi tiêu chuẩn, nhưng thay đổi chiến lược khi kết thúc trò chơi.
Chiến lược mới sẽ được đưa ra trong tình huống mà mỗi đống sẽ chứa tối đa một que sau nước đi tiếp theo.
Trong trò chơi tiêu chuẩn, chúng ta nên chọn một nước đi sao cho có một số chẵn các đống có một que. Tuy nhiên, trong trò chơi misère, chúng ta chọn một nước đi sao cho có một số lẻ các đống có một que.
Chiến lược này hoạt động vì trạng thái thay đổi chiến lược luôn xuất hiện trong trò chơi và trạng thái này là trạng thái thắng, vì nó chứa chính xác một đống có nhiều hơn một que nên tổng nim không phải là 0.

## Sự tương đương của các trò chơi công bằng và Nim (định lý Sprague-Grundy) (The equivalence of impartial games and Nim (Sprague-Grundy theorem)) {: #equivalence-impartial-games-nim}

Bây giờ chúng ta sẽ tìm hiểu cách tìm, cho bất kỳ trạng thái trò chơi nào của bất kỳ trò chơi công bằng nào, một trạng thái tương ứng của Nim.

### Bổ đề về Nim với sự gia tăng (Lemma about Nim with increases) {: #lemma-nim-increases}

Chúng ta xem xét sửa đổi sau đối với Nim: chúng ta cũng cho phép **thêm sỏi vào một đống đã chọn**.
Các quy tắc chính xác về cách thức và thời điểm cho phép tăng **không làm chúng ta quan tâm**, tuy nhiên các quy tắc phải giữ cho trò chơi của chúng ta **không có chu trình**. Trong các phần sau, các trò chơi ví dụ sẽ được xem xét.

**Bổ đề.**
Việc bổ sung sự gia tăng cho Nim không làm thay đổi cách xác định trạng thái thắng và thua.
Nói cách khác, sự gia tăng là vô ích và chúng ta không phải sử dụng chúng trong chiến lược thắng.

**Chứng minh.**
Giả sử một người chơi đã thêm sỏi vào một đống. Sau đó, đối thủ của anh ta có thể đơn giản hoàn tác nước đi của anh ta — giảm số lượng trở lại giá trị trước đó.
Vì trò chơi không có chu trình, sớm hay muộn người chơi hiện tại sẽ không thể sử dụng nước đi tăng và sẽ phải thực hiện nước đi Nim thông thường.

### Định lý Sprague-Grundy (Sprague-Grundy theorem) {: #sprague-grundy-theorem}

Hãy xem xét một trạng thái $v$ của một trò chơi công bằng hai người chơi và gọi $v_i$ là các trạng thái có thể truy cập được từ nó (trong đó $i \in \{ 1, 2, \dots, k \} , k \ge 0$).
Đối với trạng thái này, chúng ta có thể gán một trò chơi Nim hoàn toàn tương đương với một đống kích thước $x$.
Số $x$ được gọi là giá trị Grundy hoặc giá trị nim (nim-value) của trạng thái $v$.

Hơn nữa, số này có thể được tìm thấy theo cách đệ quy sau:

$$ x = \text{mex}\ \{ x_1, \ldots, x_k \}, $$

trong đó $x_i$ là giá trị Grundy cho trạng thái $v_i$ và hàm $\text{mex}$ (*minimum excludant*) là số nguyên không âm nhỏ nhất không tìm thấy trong tập hợp đã cho.

Xem trò chơi như một đồ thị, chúng ta có thể tính toán dần dần các giá trị Grundy bắt đầu từ các đỉnh không có cạnh ra.
Giá trị Grundy bằng không có nghĩa là trạng thái đang thua.

**Chứng minh.**
Chúng ta sẽ sử dụng chứng minh bằng quy nạp.

Đối với các đỉnh không có nước đi, giá trị $x$ là $\text{mex}$ của một tập hợp rỗng, là không.
Điều đó đúng, vì Nim rỗng là thua.

Bây giờ hãy xem xét bất kỳ đỉnh nào khác $v$.
Bằng quy nạp, chúng ta giả sử các giá trị $x_i$ tương ứng với các đỉnh có thể truy cập của nó đã được tính toán.

Gọi $p = \text{mex}\ \{ x_1, \ldots, x_k \}$.
Sau đó, chúng ta biết rằng đối với bất kỳ số nguyên $i \in [0, p)$ nào cũng tồn tại một đỉnh có thể truy cập được với giá trị Grundy $i$.
Điều này có nghĩa là $v$ **tương đương với một trạng thái của trò chơi Nim có sự gia tăng với một đống kích thước $p$**.
Trong trò chơi như vậy, chúng ta có các chuyển đổi sang các đống có mọi kích thước nhỏ hơn $p$ và có thể chuyển đổi sang các đống có kích thước lớn hơn $p$.
Do đó, $p$ thực sự là giá trị Grundy mong muốn cho trạng thái đang được xem xét.

## Ứng dụng của định lý (Application of the theorem) {: #application-of-the-theorem}

Cuối cùng, chúng ta mô tả một thuật toán để xác định kết quả thắng/thua của một trò chơi, áp dụng cho bất kỳ trò chơi công bằng hai người chơi nào.

Để tính giá trị Grundy của một trạng thái nhất định, bạn cần:

*   Nhận tất cả các chuyển đổi có thể có từ trạng thái này

*   Mỗi chuyển đổi có thể dẫn đến một **tổng của các trò chơi độc lập** (một trò chơi trong trường hợp suy biến).
    Tính giá trị Grundy cho mỗi trò chơi độc lập và tính tổng xor của chúng.
    Tất nhiên xor không làm gì nếu chỉ có một trò chơi.

*   Sau khi chúng ta tính toán các giá trị Grundy cho mỗi chuyển đổi, chúng ta tìm giá trị của trạng thái bằng $\text{mex}$ của các số này.

*   Nếu giá trị bằng 0, thì trạng thái hiện tại là thua, ngược lại là thắng.

So với phần trước, chúng ta tính đến thực tế là có thể có các chuyển đổi sang các trò chơi kết hợp.
Chúng ta coi chúng là một Nim với kích thước đống bằng giá trị Grundy của các trò chơi độc lập.
Chúng ta có thể tính tổng xor của chúng giống như Nim thông thường theo định lý Bouton.

## Các mẫu trong giá trị Grundy (Patterns in Grundy values) {: #patterns-in-grundy-values}

Rất thường xuyên khi giải quyết các nhiệm vụ cụ thể bằng cách sử dụng các giá trị Grundy, có thể có lợi khi **nghiên cứu bảng giá trị** để tìm kiếm các mẫu.

Trong nhiều trò chơi, có vẻ khá khó khăn để phân tích lý thuyết,
các giá trị Grundy hóa ra là tuần hoàn hoặc có dạng dễ hiểu.
Trong đại đa số các trường hợp, mẫu quan sát được hóa ra là đúng và có thể được chứng minh bằng quy nạp nếu muốn.

Tuy nhiên, các giá trị Grundy không phải *lúc nào* cũng chứa các quy luật như vậy và ngay cả đối với một số trò chơi rất đơn giản, vấn đề hỏi liệu các quy luật đó có tồn tại hay không vẫn còn mở (ví dụ: "trò chơi của Grundy").

## Các trò chơi ví dụ (Example games) {: #example-games}

### Crosses-crosses {: #crosses-crosses}

**Luật chơi.**
Hãy xem xét một dải ô vuông có kích thước $1 \times n$. Trong một nước đi, người chơi phải đặt một dấu chéo, nhưng không được phép đặt hai dấu chéo cạnh nhau (trong các ô liền kề). Như thường lệ, người chơi không có nước đi hợp lệ sẽ thua.

**Giải pháp.**
Khi một người chơi đặt dấu chéo vào bất kỳ ô nào, chúng ta có thể nghĩ đến việc dải bị chia thành hai phần độc lập:
sang trái của dấu chéo và sang phải của nó.
Trong trường hợp này, ô có dấu chéo, cũng như các hàng xóm bên trái và bên phải của nó bị phá hủy — không thể đặt thêm gì vào chúng.
Do đó, nếu chúng ta đánh số các ô từ $1$ đến $n$ thì việc đặt dấu chéo ở vị trí $1 < i < n$ sẽ phá vỡ dải
thành hai dải có chiều dài $i-2$ và $n-i-1$, tức là chúng ta đi đến tổng của các trò chơi $i-2$ và $n-i-1$.
Đối với trường hợp biên của dấu chéo được đánh dấu ở vị trí $1$ hoặc $n$, chúng ta đi đến trò chơi $n-2$.

Do đó, giá trị Grundy $g(n)$ có dạng:

$$g(n) = \text{mex} \Bigl( \{ g(n-2) \} \cup \{g(i-2) \oplus g(n-i-1) \mid 2 \leq i \leq n-1\} \Bigr) .$$

Vì vậy, chúng ta đã có một giải pháp $O(n^2)$.

Trên thực tế, $g(n)$ có chu kỳ độ dài 34 bắt đầu với $n=52$.

## Bài tập (Practice Problems) {: #practice-problems}

- [KATTIS S-Nim](https://open.kattis.com/problems/snim)
- [CodeForces - Marbles (2018-2019 ACM-ICPC Brazil Subregional)](https://codeforces.com/gym/101908/problem/B)
- [KATTIS - Cuboid Slicing Game](https://open.kattis.com/problems/cuboidslicinggame)
- [HackerRank - Tower Breakers, Revisited!](https://www.hackerrank.com/contests/5-days-of-game-theory/challenges/tower-breakers-2)
- [HackerRank - Tower Breakers, Again!](https://www.hackerrank.com/contests/5-days-of-game-theory/challenges/tower-breakers-3/problem)
- [HackerRank - Chessboard Game, Again!](https://www.hackerrank.com/contests/5-days-of-game-theory/challenges/a-chessboard-game)
- [Atcoder - ABC368F - Dividing Game](https://atcoder.jp/contests/abc368/tasks/abc368_f)