---
tags:
  - Translated
e_maxx_link: balanced_ternary
---

# Hệ tam phân cân bằng

!["Máy tính Setun sử dụng hệ tam phân cân bằng"](https://earltcampbell.files.wordpress.com/2014/12/setun.jpeg?w=300)

Đây là một **hệ đếm** không tiêu chuẩn nhưng vẫn là hệ đếm theo vị trí. Đặc điểm của nó là các chữ số có thể có một trong các giá trị `-1`, `0` và `1`.
Tuy nhiên, cơ số của nó vẫn là `3` (vì có ba giá trị khả dĩ). Vì không tiện để viết `-1` như một chữ số,
chúng ta sẽ sử dụng chữ cái `Z` cho mục đích này. Nếu bạn nghĩ rằng đây là một hệ thống khá lạ - hãy nhìn vào bức tranh - đây là một trong những máy tính sử dụng nó.

Dưới đây là một vài số đầu tiên được viết trong hệ tam phân cân bằng:

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

Lưu ý rằng một số âm bắt đầu bằng `Z` và số dương bắt đầu bằng `1`.

## Thuật toán chuyển đổi

Ta có thể dễ dàng biểu diễn một số đã cho trong **hệ tam phân cân bằng** bằng cách biểu diễn tạm thời nó trong hệ tam phân thông thường. Khi một giá trị ở dạng tam phân tiêu chuẩn, các chữ số của nó là `0`, `1` hoặc `2`. Lặp từ chữ số thấp nhất, ta có thể bỏ qua bất kỳ chữ số `0` và `1` nào,
tuy nhiên `2` phải được chuyển thành `Z` và cộng `1` vào chữ số tiếp theo. Chữ số `3` cũng được chuyển thành `0` theo cách tương tự -
những chữ số như vậy không có trong số ban đầu nhưng chúng có thể xuất hiện sau khi ta tăng một vài chữ số `2`.

**Ví dụ 1:** Hãy chuyển `64` sang hệ tam phân cân bằng. Trước tiên, ta sử dụng hệ tam phân thông thường để viết lại số:

$$ 64_{10} = 02101_{3} $$

Hãy xử lý nó từ chữ số có nghĩa nhỏ nhất (ngoài cùng bên phải):

- `1`,`0` và `1` được giữ nguyên. (Vì `0` và `1` được cho phép trong hệ tam phân cân bằng)
- `2` được chuyển thành `Z` và tăng chữ số bên trái nó lên, ta được `1Z101`.

Kết quả cuối cùng là `1Z101`.

Hãy chuyển nó trở lại hệ thập phân bằng cách cộng các giá trị vị trí có trọng số:

$$ 1Z101 = 81 \cdot 1 + 27 \cdot (-1) + 9 \cdot 1 + 3 \cdot 0 + 1 \cdot 1 = 64_{10} $$

**Ví dụ 2:** Hãy chuyển `237` sang hệ tam phân cân bằng. Trước tiên, ta sử dụng hệ tam phân thông thường để viết lại số:

$$ 237_{10} = 22210_{3} $$

Hãy xử lý nó từ chữ số có nghĩa nhỏ nhất (ngoài cùng bên phải):

- `0` và `1` được giữ nguyên. (Vì `0` và `1` được cho phép trong hệ tam phân cân bằng)
- `2` được chuyển thành `Z` và tăng chữ số bên trái nó lên, ta được `23Z10`.
- `3` được chuyển thành `0` và tăng chữ số bên trái nó lên, ta được `30Z10`.
- `3` được chuyển thành `0` và tăng chữ số bên trái nó lên (mặc định là `0`), và ta được `100Z10`.

Kết quả cuối cùng là `100Z10`.

Hãy chuyển nó trở lại hệ thập phân bằng cách cộng các giá trị vị trí có trọng số:

$$ 100Z10 = 243 \cdot 1 + 81 \cdot 0 + 27 \cdot 0 + 9 \cdot (-1) + 3 \cdot 1 + 1 \cdot 0 = 237_{10} $$

## Bài tập luyện tập

* [Topcoder SRM 604, Div1-250](http://community.topcoder.com/stat?c=problem_statement&pm=12917&rd=15837)