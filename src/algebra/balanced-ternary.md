---
tags:
  - Translated
e_maxx_link: balanced_ternary
---

# Hệ tam phân cân bằng (Balanced Ternary) {: #balanced-ternary}

!["Setun computer using Balanced Ternary system"](https://earltcampbell.files.wordpress.com/2014/12/setun.jpeg?w=300)

Đây là một **hệ đếm** vị trí không chuẩn nhưng vẫn là hệ đếm vị trí. Đặc điểm của nó là các chữ số có thể nhận một trong các giá trị `-1`, `0` và `1`.
Tuy nhiên, cơ số của nó vẫn là `3` (vì có ba giá trị có thể). Vì việc viết `-1` như một chữ số không thuận tiện,
chúng tôi sẽ sử dụng ký tự `Z` sau đây cho mục đích này. Nếu bạn nghĩ đây là một hệ thống khá lạ - hãy nhìn vào bức ảnh - đây là một trong những
chiếc máy tính sử dụng nó.

Dưới đây là vài số đầu tiên được viết trong hệ tam phân cân bằng:

```nohighlight
    0    0
    1    1
    2    1Z
    3    10
    4    11
    5    1ZZ
    6    1Z0
    7    1Z1
    8    10Z
    9    100
```

Hệ thống này cho phép bạn viết các giá trị âm mà không cần dấu trừ ở đầu: bạn chỉ cần đảo ngược các chữ số trong bất kỳ số dương nào.

```nohighlight
    -1   Z
    -2   Z1
    -3   Z0
    -4   ZZ
    -5   Z11
```

Lưu ý rằng số âm bắt đầu bằng `Z` và số dương bắt đầu bằng `1`.

## Thuật toán chuyển đổi {: #conversion-algorithm}

Rất dễ dàng để biểu diễn một số đã cho trong **hệ tam phân cân bằng** thông qua việc biểu diễn tạm thời nó trong hệ tam phân thường. Khi giá trị
ở hệ tam phân chuẩn, các chữ số của nó là `0` hoặc `1` hoặc `2`. Duyệt từ chữ số thấp nhất, chúng ta có thể bỏ qua các số `0` và `1` một cách an toàn,
tuy nhiên `2` nên được chuyển thành `Z` cùng với việc cộng `1` vào chữ số tiếp theo. Chữ số `3` nên được chuyển thành `0` với cùng điều kiện -
những chữ số như vậy không có trong số ban đầu nhưng chúng có thể xuất hiện sau khi tăng một số `2`.

**Ví dụ 1:** Hãy chuyển `64` sang hệ tam phân cân bằng. Đầu tiên chúng ta dùng hệ tam phân thường để viết lại số:

$$ 64_{10} = 02101_{3} $$

Hãy xử lý nó từ chữ số ít quan trọng nhất (ngoài cùng bên phải):

- `1`,`0` và `1` được bỏ qua giữ nguyên. (Vì `0` và `1` được phép trong hệ tam phân cân bằng)
- `2` được chuyển thành `Z` tăng chữ số bên trái nó, vì vậy chúng ta nhận được `1Z101`.

Kết quả cuối cùng là `1Z101`.

Hãy chuyển đổi ngược lại sang hệ thập phân bằng cách cộng các giá trị vị trí có trọng số:

$$ 1Z101 = 81 \cdot 1 + 27 \cdot (-1) + 9 \cdot 1 + 3 \cdot 0 + 1 \cdot 1 = 64_{10} $$

**Ví dụ 2:** Hãy chuyển `237` sang hệ tam phân cân bằng. Đầu tiên chúng ta dùng hệ tam phân thường để viết lại số:

$$ 237_{10} = 22210_{3} $$

Hãy xử lý nó từ chữ số ít quan trọng nhất (ngoài cùng bên phải):

- `0` và `1` được bỏ qua giữ nguyên. (Vì `0` và `1` được phép trong hệ tam phân cân bằng)
- `2` được chuyển thành `Z` tăng chữ số bên trái nó, vì vậy chúng ta nhận được `23Z10`.
- `3` được chuyển thành `0` tăng chữ số bên trái nó, vì vậy chúng ta nhận được `30Z10`.
- `3` được chuyển thành `0` tăng chữ số bên trái nó (mặc định là `0`), và vì vậy chúng ta nhận được `100Z10`.

Kết quả cuối cùng là `100Z10`.

Hãy chuyển đổi ngược lại sang hệ thập phân bằng cách cộng các giá trị vị trí có trọng số:

$$ 100Z10 = 243 \cdot 1 + 81 \cdot 0 + 27 \cdot 0 + 9 \cdot (-1) + 3 \cdot 1 + 1 \cdot 0 = 237_{10} $$

## Bài tập luyện tập {: #practice-problems}

* [Topcoder SRM 604, Div1-250](http://community.topcoder.com/stat?c=problem_statement&pm=12917&rd=15837)
