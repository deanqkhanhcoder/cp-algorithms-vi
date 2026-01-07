---
tags:
  - Translated
e_maxx_link: sprague_grundy
---

# Định lý Sprague-Grundy. Trò chơi Nim

## Giới thiệu

Định lý này mô tả cái gọi là trò chơi hai người chơi **vô tư**,
tức là những trò chơi mà các nước đi có thể và thắng/thua chỉ phụ thuộc vào trạng thái của trò chơi.
Nói cách khác, sự khác biệt duy nhất giữa hai người chơi là một trong số họ đi trước.

Ngoài ra, chúng ta giả định rằng trò chơi có **thông tin hoàn hảo**, tức là không có thông tin nào bị che giấu khỏi người chơi (họ biết các quy tắc và các nước đi có thể).

Giả định rằng trò chơi là **hữu hạn**, tức là sau một số nước đi nhất định, một trong những người chơi sẽ kết thúc ở một vị thế thua — từ đó họ không thể di chuyển đến một vị thế khác.
Mặt khác, người chơi đã đặt đối thủ vào vị thế này sẽ thắng.
Dễ hiểu là không có hòa trong trò chơi này.

Những trò chơi như vậy có thể được mô tả hoàn toàn bằng một *đồ thị có hướng không có chu trình*: các đỉnh là các trạng thái của trò chơi và các cạnh là các chuyển tiếp (nước đi).
Một đỉnh không có cạnh đi ra là một đỉnh thua (một người chơi phải thực hiện một nước đi từ đỉnh này sẽ thua).

Vì không có hòa, chúng ta có thể phân loại tất cả các trạng thái của trò chơi thành **thắng** hoặc **thua**.
Trạng thái thắng là những trạng thái mà từ đó có một nước đi gây ra thất bại không thể tránh khỏi cho người chơi kia, ngay cả khi họ có phản ứng tốt nhất.
Trạng thái thua là những trạng thái mà từ đó tất cả các nước đi đều dẫn đến trạng thái thắng cho người chơi kia.
Tóm lại, một trạng thái là thắng nếu có ít nhất một chuyển tiếp đến một trạng thái thua và là thua nếu không có ít nhất một chuyển tiếp đến một trạng thái thua.

Nhiệm vụ của chúng ta là phân loại các trạng thái của một trò chơi đã cho.

Lý thuyết về các trò chơi như vậy đã được Roland Sprague phát triển độc lập vào năm 1935 và Patrick Michael Grundy vào năm 1939.

## Trò chơi Nim

Trò chơi này tuân thủ các hạn chế được mô tả ở trên.
Hơn nữa, *bất kỳ* trò chơi hai người chơi vô tư có thông tin hoàn hảo nào cũng có thể được quy về trò chơi Nim.
Việc nghiên cứu trò chơi này sẽ cho phép chúng ta giải quyết tất cả các trò chơi tương tự khác, nhưng sẽ nói thêm về điều đó sau.

Trong lịch sử, trò chơi này phổ biến từ thời cổ đại.
Nguồn gốc của nó có lẽ là ở Trung Quốc — hoặc ít nhất là trò chơi *Jianshizi* rất giống với nó.
Ở châu Âu, những tài liệu tham khảo sớm nhất về nó là từ thế kỷ 16.
Tên gọi này được đặt bởi Charles Bouton, người vào năm 1901 đã công bố một phân tích đầy đủ về trò chơi này.

### Mô tả trò chơi

Có một số đống, mỗi đống có một số viên đá.
Trong một nước đi, một người chơi có thể lấy bất kỳ số lượng viên đá dương nào từ bất kỳ một đống nào và vứt chúng đi.
Một người chơi thua nếu họ không thể thực hiện một nước đi, điều này xảy ra khi tất cả các đống đều trống.

Trạng thái của trò chơi được mô tả một cách rõ ràng bằng một đa tập hợp các số nguyên dương.
Một nước đi bao gồm việc giảm nghiêm ngặt một số nguyên được chọn (nếu nó trở thành không, nó sẽ bị xóa khỏi tập hợp).

### Giải pháp

Giải pháp của Charles L. Bouton trông như thế này:

**Định lý.**
Người chơi hiện tại có một chiến lược thắng khi và chỉ khi tổng xor của các kích thước đống là khác không.
Tổng xor của một dãy $a$ là $a_1 igoplus a_2 igoplus 	ext{…} igoplus  a_n$, trong đó $igoplus$ là *phép hoặc loại trừ từng bit*.

**Chứng minh.**
Chìa khóa của chứng minh là sự hiện diện của một **chiến lược đối xứng cho đối thủ**.
Chúng ta chỉ ra rằng một khi ở trong một vị trí có tổng xor bằng không, người chơi sẽ không thể làm cho nó khác không trong dài hạn —
nếu họ chuyển đến một vị trí có tổng xor khác không, đối thủ sẽ luôn có một nước đi đưa tổng xor trở lại bằng không.

Chúng ta sẽ chứng minh định lý bằng quy nạp toán học.

Đối với một Nim rỗng (nơi tất cả các đống đều trống, tức là đa tập hợp là rỗng) tổng xor là không và định lý là đúng.

Bây giờ giả sử chúng ta đang ở trong một trạng thái không rỗng.
Sử dụng giả thuyết quy nạp (và tính không có chu trình của trò chơi), chúng ta giả định rằng định lý đã được chứng minh cho tất cả các trạng thái có thể đạt được từ trạng thái hiện tại.

Khi đó, chứng minh được chia thành hai phần:
nếu đối với vị trí hiện tại tổng xor $s = 0$, chúng ta phải chứng minh rằng trạng thái này là thua, tức là tất cả các trạng thái có thể đạt được đều có tổng xor $t 
eq 0$.
Nếu $s 
eq 0$, chúng ta phải chứng minh rằng có một nước đi dẫn đến một trạng thái có $t = 0$.

*   Đặt $s = 0$ và hãy xem xét bất kỳ nước đi nào.
    Nước đi này giảm kích thước của một đống $x$ xuống kích thước $y$.
    Sử dụng các thuộc tính cơ bản của $igoplus$, chúng ta có
    
    $$ t = s igoplus x igoplus y = 0 igoplus x igoplus y = x igoplus y $$  
    
    Vì $y < x$, $y igoplus x$ không thể bằng không, vì vậy $t 
eq 0$.
    Điều đó có nghĩa là bất kỳ trạng thái nào có thể đạt được đều là một trạng thái thắng (theo giả thuyết quy nạp), vì vậy chúng ta đang ở trong một vị thế thua.

*   Đặt $s 
eq 0$.
    Hãy xem xét biểu diễn nhị phân của số $s$.
    Đặt $d$ là chỉ số của bit khác không hàng đầu (giá trị lớn nhất) của nó.
    Nước đi của chúng ta sẽ là trên một đống có kích thước mà bit số $d$ được đặt (nó phải tồn tại, nếu không bit sẽ không được đặt trong $s$).
    Chúng ta sẽ giảm kích thước $x$ của nó xuống $y = x igoplus s$.
    Tất cả các bit ở các vị trí lớn hơn $d$ trong $x$ và $y$ khớp nhau và bit $d$ được đặt trong $x$ nhưng không được đặt trong $y$.
    Do đó, $y < x$, đó là tất cả những gì chúng ta cần để một nước đi là hợp lệ.
    Bây giờ chúng ta có:
    
    $$ t = s igoplus x igoplus y = s igoplus x igoplus (s igoplus x) = 0 $$  
    
    Điều này có nghĩa là chúng ta đã tìm thấy một trạng thái thua có thể đạt được (theo giả thuyết quy nạp) và trạng thái hiện tại là thắng.

**Hệ quả.**
Bất kỳ trạng thái nào của Nim đều có thể được thay thế bằng một trạng thái tương đương miễn là tổng xor không thay đổi.
Hơn nữa, khi phân tích một Nim với nhiều đống, chúng ta có thể thay thế nó bằng một đống duy nhất có kích thước $s$.

### Trò chơi Misère

Trong một **trò chơi misère**, mục tiêu của trò chơi là ngược lại, vì vậy người chơi loại bỏ que diêm cuối cùng sẽ thua trò chơi.
Hóa ra trò chơi nim misère có thể được chơi một cách tối ưu gần giống như một trò chơi nim tiêu chuẩn.
 Ý tưởng là trước tiên hãy chơi trò chơi misère giống như trò chơi tiêu chuẩn, nhưng thay đổi chiến lược ở cuối trò chơi.
 Chiến lược mới sẽ được giới thiệu trong một tình huống mà mỗi đống sẽ chứa nhiều nhất một que diêm sau nước đi tiếp theo.
Trong trò chơi tiêu chuẩn, chúng ta nên chọn một nước đi sau đó có một số lượng chẵn các đống có một que diêm. Tuy nhiên, trong 
trò chơi misère, chúng ta chọn một nước đi sao cho có một số lượng lẻ các đống có một que diêm.
  Chiến lược này hoạt động vì một trạng thái mà chiến lược thay đổi luôn xuất hiện trong trò chơi, và trạng thái này là một 
  trạng thái thắng, bởi vì nó chứa chính xác một đống có nhiều hơn một que diêm nên tổng nim không phải là 0.

## Sự tương đương của các trò chơi vô tư và Nim (Định lý Sprague-Grundy)

Bây giờ chúng ta sẽ học cách tìm, đối với bất kỳ trạng thái trò chơi nào của bất kỳ trò chơi vô tư nào, một trạng thái tương ứng của Nim.

### Bổ đề về Nim với các lần tăng

Chúng ta xem xét sửa đổi sau đây đối với Nim: chúng ta cũng cho phép **thêm các viên đá vào một đống đã chọn**.
Các quy tắc chính xác về cách thức và thời điểm cho phép tăng **không làm chúng ta quan tâm**, tuy nhiên các quy tắc phải giữ cho trò chơi của chúng ta **không có chu trình**. Trong các phần sau, các trò chơi ví dụ được xem xét.

**Bổ đề.**
Việc thêm các lần tăng vào Nim không thay đổi cách xác định các trạng thái thắng và thua.
Nói cách khác, các lần tăng là vô ích, và chúng ta không phải sử dụng chúng trong một chiến lược thắng.

**Chứng minh.**
Giả sử một người chơi đã thêm các viên đá vào một đống. Khi đó đối thủ của họ có thể chỉ cần hoàn tác nước đi của họ — giảm số lượng trở lại giá trị trước đó.
Vì trò chơi không có chu trình, sớm hay muộn người chơi hiện tại sẽ không thể sử dụng một nước đi tăng và sẽ phải thực hiện nước đi Nim thông thường.

### Định lý Sprague-Grundy

Hãy xem xét một trạng thái $v$ của một trò chơi hai người chơi vô tư và đặt $v_i$ là các trạng thái có thể đạt được từ nó (trong đó $i 	ext{ ∈ } \{ 1, 2, \dots, k \} , k 	ext{ ≥ } 0$).
Đối với trạng thái này, chúng ta có thể gán một trò chơi Nim hoàn toàn tương đương với một đống có kích thước $x$.
Số $x$ được gọi là giá trị Grundy hoặc giá trị nim của trạng thái $v$.

Hơn nữa, số này có thể được tìm thấy theo cách đệ quy sau:

$$ x = \text{mex}
\{ x_1, \ldots, x_k \}, $$  

trong đó $x_i$ là giá trị Grundy cho trạng thái $v_i$ và hàm $\text{mex}$ (*số nguyên không âm nhỏ nhất không có trong tập hợp*) là số nguyên không âm nhỏ nhất không tìm thấy trong tập hợp đã cho.

Xem trò chơi như một đồ thị, chúng ta có thể tính toán dần dần các giá trị Grundy bắt đầu từ các đỉnh không có cạnh đi ra.
Giá trị Grundy bằng không có nghĩa là một trạng thái thua.

**Chứng minh.**
Chúng ta sẽ sử dụng chứng minh bằng quy nạp.

Đối với các đỉnh không có nước đi, giá trị $x$ là $\text{mex}$ của một tập hợp rỗng, là không.
Điều đó đúng, vì một Nim rỗng là thua.

Bây giờ hãy xem xét bất kỳ đỉnh nào khác $v$.
Theo quy nạp, chúng ta giả định các giá trị $x_i$ tương ứng với các đỉnh có thể đạt được của nó đã được tính toán.

Đặt $p = \text{mex}
\{ x_1, \ldots, x_k \}$.
Khi đó, chúng ta biết rằng đối với bất kỳ số nguyên $i \text{ ∈ } [0, p)$, tồn tại một đỉnh có thể đạt được với giá trị Grundy $i$.
Điều này có nghĩa là $v$ **tương đương với một trạng thái của trò chơi Nim với các lần tăng với một đống có kích thước $p$**.
Trong một trò chơi như vậy, chúng ta có các chuyển tiếp đến các đống có mọi kích thước nhỏ hơn $p$ và có thể có các chuyển tiếp đến các đống có kích thước lớn hơn $p$.
Do đó, $p$ thực sự là giá trị Grundy mong muốn cho trạng thái đang được xem xét.

## Ứng dụng của định lý

Cuối cùng, chúng tôi mô tả một thuật toán để xác định kết quả thắng/thua của một trò chơi, có thể áp dụng cho bất kỳ trò chơi hai người chơi vô tư nào.

Để tính toán giá trị Grundy của một trạng thái đã cho, bạn cần:

* Lấy tất cả các chuyển tiếp có thể có từ trạng thái này

* Mỗi chuyển tiếp có thể dẫn đến một **tổng của các trò chơi độc lập** (một trò chơi trong trường hợp thoái hóa).
Tính toán giá trị Grundy cho mỗi trò chơi độc lập và tổng xor chúng.
Tất nhiên, xor không làm gì nếu chỉ có một trò chơi.

* Sau khi chúng ta đã tính toán các giá trị Grundy cho mỗi chuyển tiếp, chúng ta tìm giá trị của trạng thái là $\text{mex}$ của các số này.

* Nếu giá trị là không, thì trạng thái hiện tại là thua, nếu không thì là thắng.

So với phần trước, chúng ta tính đến thực tế là có thể có các chuyển tiếp đến các trò chơi kết hợp.
Chúng ta coi chúng là một Nim với các kích thước đống bằng với các giá trị Grundy của các trò chơi độc lập.
Chúng ta có thể tổng xor chúng giống như Nim thông thường theo định lý của Bouton.

## Các mẫu hình trong các giá trị Grundy

Rất thường xuyên khi giải quyết các nhiệm vụ cụ thể bằng cách sử dụng các giá trị Grundy, có thể có lợi khi **nghiên cứu bảng các giá trị** để tìm kiếm các mẫu hình.

Trong nhiều trò chơi, có thể có vẻ khá khó để phân tích lý thuyết,
các giá trị Grundy hóa ra là tuần hoàn hoặc có một dạng dễ hiểu.
Trong đại đa số các trường hợp, mẫu hình được quan sát hóa ra là đúng và có thể được chứng minh bằng quy nạp nếu muốn.

Tuy nhiên, các giá trị Grundy không phải lúc nào cũng chứa các quy luật như vậy và ngay cả đối với một số trò chơi rất đơn giản, vấn đề hỏi liệu các quy luật đó có tồn tại hay không vẫn còn bỏ ngỏ (ví dụ: "trò chơi của Grundy").

## Các trò chơi ví dụ

### Chéo-chéo

**Luật chơi.**
Xét một dải kẻ ô có kích thước $1 \times n$. Trong một nước đi, người chơi phải đặt một dấu chéo, nhưng bị cấm đặt hai dấu chéo cạnh nhau (trong các ô liền kề). Như thường lệ, người chơi không có nước đi hợp lệ sẽ thua.

**Giải pháp.**
Khi một người chơi đặt một dấu chéo vào bất kỳ ô nào, chúng ta có thể nghĩ rằng dải bị chia thành hai phần độc lập:
bên trái của dấu chéo và bên phải của nó.
Trong trường hợp này, ô có dấu chéo, cũng như các ô láng giềng bên trái và bên phải của nó bị phá hủy — không thể đặt thêm gì vào chúng.
Do đó, nếu chúng ta đánh số các ô từ $1$ đến $n$ thì việc đặt dấu chéo vào vị trí $1 < i < n$ sẽ phá vỡ dải
thành hai dải có độ dài $i-2$ và $n-i-1$, tức là chúng ta đi đến tổng của các trò chơi $i-2$ và $n-i-1$.
Đối với trường hợp cạnh của dấu chéo được đánh dấu ở vị trí $1$ hoặc $n$, chúng ta đi đến trò chơi $n-2$.

Do đó, giá trị Grundy $g(n)$ có dạng:

$$g(n) = \text{mex} \Bigl( \{ g(n-2) \} \cup \{g(i-2) \oplus g(n-i-1) \mid 2 \leq i \leq n-1\} \Bigr) .$$  

Vì vậy, chúng ta đã có một giải pháp $O(n^2)$.

Trên thực tế, $g(n)$ có chu kỳ dài 34 bắt đầu từ $n=52$.


## Bài tập thực hành

- [KATTIS S-Nim](https://open.kattis.com/problems/snim)
- [CodeForces - Marbles (2018-2019 ACM-ICPC Brazil Subregional)](https://codeforces.com/gym/101908/problem/B)
- [KATTIS - Cuboid Slicing Game](https://open.kattis.com/problems/cuboidslicinggame)
- [HackerRank - Tower Breakers, Revisited!](https://www.hackerrank.com/contests/5-days-of-game-theory/challenges/tower-breakers-2)
- [HackerRank - Tower Breakers, Again!](https://www.hackerrank.com/contests/5-days-of-game-theory/challenges/tower-breakers-3/problem)
- [HackerRank - Chessboard Game, Again!](https://www.hackerrank.com/contests/5-days-of-game-theory/challenges/a-chessboard-game)
- [Atcoder - ABC368F - Dividing Game](https://atcoder.jp/contests/abc368/tasks/abc368_f)
