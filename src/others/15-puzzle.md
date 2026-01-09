---
tags:
  - Translated
e_maxx_link: 15_puzzle
---

# Trò chơi 15 Puzzle: Sự tồn tại của lời giải (15 Puzzle Game: Existence Of The Solution) {: #15-puzzle-game-existence-of-the-solution}

Trò chơi này được chơi trên một bảng $4 \times 4$. Trên bảng này có $15$ ô vuông được đánh số từ 1 đến 15. Một ô được để trống (ký hiệu là 0). Bạn cần đưa bảng về vị trí được trình bày bên dưới bằng cách di chuyển lặp đi lặp lại một trong các ô vuông vào không gian trống:

$$\begin{matrix} 1 & 2 & 3 & 4 \\ 5 & 6 & 7 & 8 \\ 9 & 10 & 11 & 12 \\ 13 & 14 & 15 & 0 \end{matrix}$$

Trò chơi "15 Puzzle" được tạo ra bởi Noyes Chapman vào năm 1880.

## Sự tồn tại của lời giải (Existence Of The Solution) {: #existence-of-the-solution}

Hãy xem xét bài toán này: cho một vị trí trên bảng, xác định xem có tồn tại một chuỗi các bước di chuyển dẫn đến lời giải hay không.

Giả sử chúng ta có một vị trí nào đó trên bảng:

$$\begin{matrix} a_1 & a_2 & a_3 & a_4 \\ a_5 & a_6 & a_7 & a_8 \\ a_9 & a_{10} & a_{11} & a_{12} \\ a_{13} & a_{14} & a_{15} & a_{16} \end{matrix}$$

trong đó một trong các phần tử bằng không và biểu thị một ô trống $a_z  = 0$

Hãy xem xét hoán vị:

$$a_1 a_2 ... a_{z-1} a_{z+1} ... a_{15} a_{16}$$

tức là hoán vị của các số tương ứng với vị trí trên bảng mà không có phần tử không.

Gọi $N$ là số lượng nghịch đảo trong hoán vị này (tức là số lượng các phần tử $a_i$ và $a_j$ sao cho $i < j$, nhưng $a_i  > a_j$).

Giả sử $K$ là chỉ số của hàng nơi phần tử trống toạ lạc (tức là sử dụng quy ước của chúng ta, $K = (z - 1) \div \ 4 + 1$).

Khi đó, **lời giải tồn tại khi và chỉ khi $N + K$ là số chẵn**.

## Cài đặt (Implementation) {: #implementation}

Thuật toán trên có thể được minh họa bằng mã chương trình sau:

```cpp
int a[16];
for (int i=0; i<16; ++i)
    cin >> a[i];

int inv = 0;
for (int i=0; i<16; ++i)
    if (a[i])
        for (int j=0; j<i; ++j)
            if (a[j] > a[i])
                ++inv;
for (int i=0; i<16; ++i)
    if (a[i] == 0)
        inv += 1 + i / 4;

puts ((inv & 1) ? "No Solution" : "Solution Exists");
```

## Chứng minh (Proof) {: #proof}

Năm 1879 Johnson đã chứng minh rằng nếu $N + K$ là lẻ, thì lời giải không tồn tại, và cùng năm đó Story đã chứng minh rằng tất cả các vị trí khi $N + K$ là chẵn đều có lời giải.

Tuy nhiên, tất cả các chứng minh này đều khá phức tạp.

Năm 1999 Archer đã đề xuất một chứng minh đơn giản hơn nhiều (bạn có thể tải xuống bài viết của ông [tại đây](http://www.cs.cmu.edu/afs/cs/academic/class/15859-f01/www/notes/15-puzzle.pdf)).

## Bài tập (Practice Problems) {: #practice-problems}

* [Hackerrank - N-puzzle](https://www.hackerrank.com/challenges/n-puzzle)
