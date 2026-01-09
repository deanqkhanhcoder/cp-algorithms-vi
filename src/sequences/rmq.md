---
tags:
  - Translated
e_maxx_link: rmq
---

# Truy vấn giá trị nhỏ nhất trong đoạn (Range Minimum Query) {: #range-minimum-query}

Bạn được cho một mảng $A[1..N]$.
Bạn phải trả lời các truy vấn đến có dạng $(L, R)$, yêu cầu tìm phần tử nhỏ nhất trong mảng $A$ giữa các vị trí $L$ và $R$.

RMQ có thể xuất hiện trực tiếp trong các bài toán hoặc có thể được áp dụng trong một số nhiệm vụ khác, ví dụ: bài toán [Tổ tiên chung thấp nhất (Lowest Common Ancestor)](../graph/lca.md).

## Giải pháp (Solution) {: #solution}

Có rất nhiều cách tiếp cận và cấu trúc dữ liệu có thể mà bạn có thể sử dụng để giải quyết tác vụ RMQ.

Những cái được giải thích trên trang web này được liệt kê dưới đây.

Đầu tiên là các cách tiếp cận cho phép sửa đổi mảng giữa các lần trả lời truy vấn.

- [Sqrt-decomposition](../data_structures/sqrt_decomposition.md) - trả lời mỗi truy vấn trong $O(\sqrt{N})$, tiền xử lý được thực hiện trong $O(N)$.
  Ưu điểm: một cấu trúc dữ liệu rất đơn giản. Nhược điểm: độ phức tạp tồi tệ hơn.
- [Segment tree](../data_structures/segment_tree.md) - trả lời mỗi truy vấn trong $O(\log N)$, tiền xử lý được thực hiện trong $O(N)$.
  Ưu điểm: độ phức tạp thời gian tốt. Nhược điểm: lượng mã lớn hơn so với các cấu trúc dữ liệu khác.
- [Fenwick tree](../data_structures/fenwick.md) - trả lời mỗi truy vấn trong $O(\log N)$, tiền xử lý được thực hiện trong $O(N \log N)$.
  Ưu điểm: mã ngắn nhất, độ phức tạp thời gian tốt. Nhược điểm: Cây Fenwick chỉ có thể được sử dụng cho các truy vấn có $L = 1$, vì vậy nó không áp dụng cho nhiều bài toán.

Và đây là những cách tiếp cận chỉ hoạt động trên các mảng tĩnh, tức là không thể thay đổi giá trị trong mảng mà không tính toán lại cấu trúc dữ liệu hoàn chỉnh.

- [Sparse Table](../data_structures/sparse-table.md) - trả lời mỗi truy vấn trong $O(1)$, tiền xử lý được thực hiện trong $O(N \log N)$.
  Ưu điểm: cấu trúc dữ liệu đơn giản, độ phức tạp thời gian tuyệt vời.
- [Sqrt Tree](../data_structures/sqrt-tree.md) - trả lời truy vấn trong $O(1)$, tiền xử lý được thực hiện trong $O(N \log \log N)$. Ưu điểm: nhanh. Nhược điểm: Phức tạp để cài đặt.
- [Disjoint Set Union / Arpa's Trick](../data_structures/disjoint_set_union.md#arpa) - trả lời truy vấn trong $O(1)$, tiền xử lý trong $O(n)$. Ưu điểm: ngắn, nhanh. Nhược điểm: chỉ hoạt động nếu tất cả các truy vấn được biết trước, tức là chỉ hỗ trợ xử lý off-line các truy vấn.
- [Cartesian Tree](../graph/rmq_linear.md) và [Thuật toán Farach-Colton và Bender](../graph/lca_farachcoltonbender.md) - trả lời truy vấn trong $O(1)$, tiền xử lý trong $O(n)$. Ưu điểm: độ phức tạp tối ưu. Nhược điểm: lượng mã lớn.

Lưu ý: Tiền xử lý là quá trình xử lý sơ bộ mảng đã cho bằng cách xây dựng cấu trúc dữ liệu tương ứng cho nó.

## Bài tập (Practice Problems) {: #practice-problems}
- [SPOJ: Range Minimum Query](http://www.spoj.com/problems/RMQSQ/)
- [CODECHEF: Chef And Array](https://www.codechef.com/problems/FRMQ)
- [Codeforces:  Array Partition](https://codeforces.com/contest/1454/problem/F)
