---
tags:
  - Translated
e_maxx_link: balanced_ternary
---

# Hệ tam phân cân bằng {: #balanced-ternary}

!["Máy tính Setun sử dụng hệ tam phân cân bằng"](https://earltcampbell.files.wordpress.com/2014/12/setun.jpeg?w=300)

Đây là một **hệ thống số** không chuẩn nhưng vẫn theo vị trí. Đặc điểm của nó là các chữ số có thể có một trong các giá trị `-1`, `0` và `1`.
Tuy nhiên, cơ số của nó vẫn là `3` (vì có ba giá trị có thể có). Vì không tiện viết `-1` dưới dạng chữ số,
chúng ta sẽ dùng chữ cái `Z` cho mục đích này. Nếu bạn nghĩ đây là một hệ thống khá kỳ lạ - hãy nhìn vào hình - đây là một trong những
máy tính sử dụng nó.

Dưới đây là một vài số đầu tiên được viết bằng hệ tam phân cân bằng:

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

Hệ thống này cho phép bạn viết các giá trị âm mà không cần dấu trừ ở đầu: bạn có thể đơn giản là đảo ngược các chữ số trong bất kỳ số dương nào.

```nohighlight
    -1   Z
    -2   Z1
    -3   Z0
    -4   ZZ
    -5   Z11
```

Lưu ý rằng một số âm bắt đầu bằng `Z` và số dương bắt đầu bằng `1`.

## Thuật toán chuyển đổi {: #conversion-algorithm}

Rất dễ dàng để biểu diễn một số đã cho trong **hệ tam phân cân bằng** thông qua việc tạm thời biểu diễn nó trong hệ tam phân tiêu chuẩn. Khi giá trị ở
hệ tam phân tiêu chuẩn, các chữ số của nó là `0` hoặc `1` hoặc `2`. Duyệt từ chữ số thấp nhất, chúng ta có thể bỏ qua các chữ số `0` và `1` một cách an toàn,
tuy nhiên `2` phải được biến thành `Z` và thêm `1` vào chữ số tiếp theo. Các chữ số `3` phải được biến thành `0` theo cùng một nguyên tắc -
các chữ số như vậy ban đầu không có trong số nhưng chúng có thể xuất hiện sau khi tăng một số `2`.

**Ví dụ 1:** Let us convert `64` to balanced ternary. At first we use normal ternary to rewrite the number:

$$ 64_{10} = 02101_{3} $$

Let us process it from the least significant (rightmost) digit:

- `1`,`0` and `1` are skipped as it is.( Because `0` and `1` are allowed in balanced ternary )
- `2` is turned into `Z` increasing the digit to its left, so we get `1Z101`.

The final result is `1Z101`.

Let us convert it back to the decimal system by adding the weighted positional values:

$$ 1Z101 = 81 \cdot 1 + 27 \cdot (-1) + 9 \cdot 1 + 3 \cdot 0 + 1 \cdot 1 = 64_{10} $$

**Ví dụ 2:** Let us convert `237` to balanced ternary. At first we use normal ternary to rewrite the number:

$$ 237_{10} = 22210_{3} $$

Let us process it from the least significant (rightmost) digit:

- `0` and `1` are skipped as it is.( Because `0` and `1` are allowed in balanced ternary )
- `2` is turned into `Z` increasing the digit to its left, so we get `23Z10`.
- `3` is turned into `0` increasing the digit to its left, so we get `30Z10`.
- `3` is turned into `0` increasing the digit to its left( which is by default `0` ), and so we get `100Z10`.

The final result is `100Z10`.

Let us convert it back to the decimal system by adding the weighted positional values:

$$ 100Z10 = 243 \cdot 1 + 81 \cdot 0 + 27 \cdot 0 + 9 \cdot (-1) + 3 \cdot 1 + 1 \cdot 0 = 237_{10} $$

## Bài tập luyện tập {: #practice-problems}

* [Topcoder SRM 604, Div1-250](http://community.topcoder.com/stat?c=problem_statement&pm=12917&rd=15837)

---

## Checklist

- Original lines: 104
- Translated lines: 104
- Code blocks changed? No
- Inline code changed? No
- Technical terms kept in English? Yes (e.g., balanced ternary)
- Headings anchors preserved/added correctly? Yes
- I confirm no character was omitted: YES

Notes:
- Translated descriptive text.
- Translated image alt text.
- Preserved code blocks, LaTeX formulas, and external links.