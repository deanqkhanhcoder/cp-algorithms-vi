# CP-Algorithms Vietnam - Style Guide

Tài liệu này quy định các chuẩn mực về định dạng, cấu trúc và văn phong cho dự án dịch thuật **cp-algorithms-vi**. Tất cả các đóng góp (PR) cần tuân thủ hướng dẫn này để đảm bảo tính nhất quán.

## 1. Quy ước Đặt tên & Cấu trúc File

### Tên File và Thư mục
- Sử dụng **kebab-case** (chữ thường, nối bằng dấu gạch ngang) cho toàn bộ file và thư mục.
- **Tốt**: `segment-tree.md`, `breadth-first-search.md`, `graph/`
- **Xấu**: `SegmentTree.md`, `01_bfs.md`, `Graph_Theory/`

### Cấu trúc File Markdown
Mỗi file `.md` phải bắt đầu bằng khối Front-matter và tuân theo cấu trúc sau:

```markdown
---
tags:
  - Translated
e_maxx_link: original_link_slug
---

# Tên Bài Viết Tiếng Việt (English Name) {: #slug-bai-viet}

[Đoạn mở đầu - Lead Paragraph]: Tóm tắt ngắn gọn bài toán hoặc thuật toán trong 1-2 câu. Súc tích, đi thẳng vào vấn đề.

## 1. Định nghĩa / Ý tưởng

Nội dung chi tiết...

## 2. Thuật toán

### Cài đặt (Implementation)
```

## 2. Quy ước Markdown & Code

### Code Blocks
- Luôn chỉ định ngôn ngữ lập trình.
- Sử dụng `title` để đặt tên file cho đoạn code (tạo cảm giác chuyên nghiệp hơn `file=...`).

**Chuẩn mới (Khuyên dùng):**
\```cpp title="segment-tree-implementation.cpp"
void build(int a[], int v, int tl, int tr) {
    // ...
}
\```

### Toán học (MathJax)
- Sử dụng `$` cho công thức nội dòng (inline) và `$$` cho công thức khối (block).
- Các toán tử: Nên dùng `\dots` thay vì `...` trong ngữ cảnh toán học ($1, 2, \dots, n$).
- Interval: Dùng `$[l, r]$` thay vì `[l, r]` thường để render đẹp hơn.

### Links & Images
- **Link nội bộ**: Dùng đường dẫn tương đối. VD: `[Dijkstra](../graph/dijkstra.md)`.
- **Anhc**: Đặt tất cả ảnh vào thư mục `src/assets/images/` (cần refactor).
  - Cú pháp: `![Alt text](../../assets/images/image-name.png)`

## 3. Văn phong & Dịch thuật

### Tone & Voice
- **Chuyên nghiệp, Kỹ thuật, Khách quan**.
- Tránh dùng ngôi thứ nhất "tôi", "chúng tôi" (we/I) trừ khi thực sự cần thiết.
- Ưu tiên câu bị động hoặc chủ ngữ giả để tập trung vào đối tượng kỹ thuật.
  - *Gốc*: "We use a segment tree to solve this."
  - *Dịch*: "Bài toán này có thể được giải quyết bằng Segment Tree." hoặc "Sử dụng Segment Tree để giải quyết..."

### Dịch thuật
- **Không dịch word-by-word**. Hãy hiểu ý và viết lại bằng tiếng Việt tự nhiên.
- **Giữ nguyên thuật toán/cấu trúc dữ liệu** nếu tên tiếng Việt không phổ biến hoặc dễ gây nhầm lẫn.
  - VD: Giữ "Suffix Automaton" thay vì "Máy tự động hậu tố" (trừ khi có chú thích rõ).
  - VD: "Segment Tree" có thể dịch là "Cây phân đoạn" (phổ biến) hoặc giữ nguyên.
- Tuyệt đối tránh lạm dụng Google Translate. Câu văn phải gãy gọn, không thừa từ đệm (thì, là, mà...).

---
*Vui lòng tham khảo thêm [GLOSSARY.md](GLOSSARY.md) để sử dụng thuật ngữ chuẩn.*
