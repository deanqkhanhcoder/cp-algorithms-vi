---
search:
  exclude: true
---

# Cách Đóng góp

Cảm ơn bạn đã quan tâm đến việc đóng góp cho dự án cp-algorithms! Dù bạn muốn sửa một lỗi chính tả, cải thiện một bài viết, hay thêm nội dung mới, sự giúp đỡ của bạn luôn được chào đón. Tất cả những gì bạn cần là một [tài khoản GitHub](https://github.com). Các đóng góp được quản lý thông qua [kho lưu trữ GitHub của chúng tôi](https://github.com/cp-algorithms/cp-algorithms), nơi bạn có thể trực tiếp gửi thay đổi hoặc đề xuất cải tiến.

Các trang được biên dịch và xuất bản tại [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Các bước để Đóng góp

Hãy làm theo các bước sau để bắt đầu đóng góp:

1. **Tìm bài viết bạn muốn cải thiện**. Nhấp vào biểu tượng bút chì (:material-pencil:) bên cạnh tiêu đề bài viết.
2. **Fork kho lưu trữ** nếu được yêu cầu. Thao tác này tạo một bản sao của kho lưu trữ trong tài khoản GitHub của bạn.
3. **Thực hiện các thay đổi của bạn** trực tiếp trong trình chỉnh sửa của GitHub hoặc clone kho lưu trữ về để làm việc trên máy cục bộ.
4. **Xem trước các thay đổi của bạn** bằng cách sử dụng [trang xem trước](preview.md) để đảm bảo chúng hiển thị chính xác.
5. **Commit các thay đổi của bạn** bằng cách nhấp vào nút _Propose changes_.
6. **Tạo một Pull Request (PR)** bằng cách nhấp vào _Compare & pull request_.
7. **Quy trình đánh giá**: Một thành viên trong đội ngũ cốt lõi sẽ xem xét các thay đổi của bạn. Quá trình này có thể mất từ vài ngày đến vài tuần.

### Thực hiện các thay đổi lớn hơn

Nếu bạn dự định thực hiện các thay đổi quan trọng hơn, chẳng hạn như thêm bài viết mới hoặc sửa đổi nhiều tệp:

- **Fork dự án** bằng cách sử dụng quy trình làm việc Git truyền thống (tạo một nhánh cho các thay đổi của bạn).
- **Chỉnh sửa các tệp trên máy cục bộ hoặc trong giao diện người dùng GitHub**.
- **Gửi một pull request** với các cập nhật của bạn.

Để được trợ giúp về quy trình làm việc này, hãy xem hướng dẫn hữu ích sau: [Hướng dẫn từng bước để đóng góp trên GitHub](https://opensource.guide/how-to-contribute/).

### Cập nhật các chỉ mục

Khi bạn thêm bài viết mới hoặc sắp xếp lại các bài viết hiện có, hãy chắc chắn cập nhật các tệp sau:

- **[navigation.md](https://github.com/cp-algorithms/cp-algorithms/blob/main/src/navigation.md)**: Cập nhật danh sách tất cả các bài viết.
- **[README.md](https://github.com/cp-algorithms/cp-algorithms/blob/main/README.md)**: Cập nhật danh sách các bài viết mới trên trang chính.

## Cú pháp bài viết

Chúng tôi sử dụng [Markdown](https://daringfireball.net/projects/markdown) để định dạng bài viết. Các bài viết được kết xuất bằng [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/), cung cấp rất nhiều sự linh hoạt. Dưới đây là một số tính năng chính:

- **Công thức toán học**: Sử dụng [MathJax](https://squidfunk.github.io/mkdocs-material/reference/mathjax/#usage) cho các phương trình. Hãy chắc chắn để lại một dòng trống trước và sau bất kỳ khối toán học `$$` nào.
- **Khối mã**: [Các khối mã](https://squidfunk.github.io/mkdocs-material/reference/code-blocks/#usage) rất tuyệt vời để thêm các đoạn mã vào bài viết.
- **Lưu ý (Admonitions)**: Sử dụng [admonitions](https://squidfunk.github.io/mkdocs-material/reference/admonitions/#usage) cho nội dung đặc biệt, chẳng hạn như định lý hoặc ví dụ.
- **Tab**: Sắp xếp nội dung với [các tab nội dung](https://squidfunk.github.io/mkdocs-material/reference/content-tabs/#usage).
- **Bảng**: Sử dụng [bảng dữ liệu](https://squidfunk.github.io/mkdocs-material/reference/data-tables/#usage) để sắp xếp thông tin.

Một số tính năng nâng cao có thể không được bật hoặc yêu cầu đăng ký trả phí. Hãy ghi nhớ điều này khi thử nghiệm với định dạng.

### Đặt tiêu đề HTML

Theo mặc định, tiêu đề đầu tiên (`# header`) của bài viết sẽ được sử dụng làm tiêu đề HTML. Nếu tiêu đề của bạn chứa công thức hoặc văn bản phức tạp, bạn có thể đặt tiêu đề theo cách thủ công:

```markdown
---
title: Alternative HTML Title
---
# Proof of $a^2 + b^2 = c^2$
```

### Xử lý chuyển hướng

Nếu bạn di chuyển hoặc đổi tên một bài viết, hãy chắc chắn thiết lập một chuyển hướng. Một tệp chuyển hướng sẽ trông như thế này:

```md
<meta http-equiv="refresh" content="0; url=../new-section/new-article.html">
# Article Name
This article has been moved to a [new location](new-section/new-article.md).
```

### Duy trì liên kết neo (Anchor Links)

Nếu bạn đổi tên một mục, liên kết đến mục đó (`/article.html#old-section-title`) có thể bị hỏng. Để tránh điều này, hãy thêm một neo theo cách thủ công:

```html
<div id="old-section-title"></div>
```

Điều này sẽ cho phép các liên kết hiện có tiếp tục hoạt động ngay cả sau khi tiêu đề mục được thay đổi.

### Thẻ (Tags) bài viết

Chúng tôi sử dụng các thẻ để phân biệt giữa nội dung gốc và các bài viết đã dịch. Thêm thẻ thích hợp ở đầu bài viết của bạn:

- **Đối với các bài viết gốc**:

    ```md
    ---
    tags:
        - Original
    ---
    ```

- **Đối với các bài viết đã dịch**:

    ```md
    ---
    tags:
        - Translated
    e_maxx_link: <original-link>
    ---
    ```

    Thay thế `<original-link>` bằng phần cuối của URL (ví dụ: đối với `http://e-maxx.ru/algo/euler_function`, sử dụng `euler_function`).

## Quy ước

Chúng tôi tuân theo các quy ước nhất định trong toàn bộ dự án. Ví dụ, chúng tôi đã đồng ý sử dụng ký hiệu `\binom{n}{k}` cho tổ hợp chập k của n thay vì `C_n^k` như đã nêu trong [vấn đề #83](https://github.com/cp-algorithms/cp-algorithms/issues/83). Ký hiệu đầu tiên hiển thị là $\binom{n}{k}$ và là một quy ước phổ biến hơn. Ký hiệu thứ hai sẽ hiển thị là $C_n^k$.

## Thêm bài toán

Khi thêm các bài toán, hãy cố gắng sắp xếp chúng theo độ khó. Nếu bạn không thể, đừng lo lắng—chỉ cần thêm bài toán, và người khác có thể điều chỉnh thứ tự sau.

## Thiết lập môi trường phát triển cục bộ

Bạn có thể xem trước các thay đổi trên máy cục bộ trước khi đẩy chúng lên GitHub. Để làm điều này:

1. Clone kho lưu trữ:

    ```console
    git clone --recursive https://github.com/cp-algorithms/cp-algorithms.git && cd cp-algorithms
    ```

2. Cài đặt các phụ thuộc và phục vụ trang web:

    ```console
    scripts/install-mkdocs.sh # yêu cầu pip
    mkdocs serve
    ```

   Lệnh này sẽ chạy trang web trên máy cục bộ để bạn có thể xem trước các thay đổi của mình. Lưu ý rằng một số tính năng bị vô hiệu hóa trong các bản dựng cục bộ.

### Các plugin tùy chọn

- **Git Revision Date Plugin**: Bị vô hiệu hóa theo mặc định, vì nó tạo ra lỗi khi bạn có các thay đổi chưa được commit trong cây làm việc. Có thể được bật với:

    ```console
    export MKDOCS_ENABLE_GIT_REVISION_DATE=True
    ```

- **Git Committers Plugin**: Bị vô hiệu hóa theo mặc định, vì nó yêu cầu một token truy cập cá nhân của GitHub. Bật nó như sau:

    ```console
    export MKDOCS_ENABLE_GIT_COMMITTERS=True
    export MKDOCS_GIT_COMMITTERS_APIKEY=your_token_here
    ```

   Bạn có thể tạo token của mình [tại đây](https://github.com/settings/tokens). Chỉ cần quyền truy cập công khai.

## Kiểm thử các đoạn mã

Nếu bài viết của bạn bao gồm các đoạn mã, sẽ rất hữu ích nếu bao gồm các bài kiểm thử để đảm bảo rằng chúng chạy đúng.

1. Đặt tên cho đoạn mã:
````
```{.cpp file=snippet-name}
// code here
```
````
3. Chạy `extract_snippets.py` từ thư mục `test` để trích xuất các đoạn mã vào các tệp tiêu đề. Tạo một tệp kiểm thử bao gồm các tiêu đề này và kiểm tra hành vi của chúng.
4. Bạn có thể chạy tất cả các bài kiểm thử bằng kịch bản `test.sh`:
    ```console
    cd test
    ./test.sh
    ```
    **Ví dụ đầu ra:**
    ```
    Running test_aho_corasick.cpp - Passed in 635 ms
    Running test_balanced_brackets.cpp - Passed in 1390 ms
    Running test_burnside_tori.cpp - Passed in 378 ms
    ...
    51 PASSED in 49.00 seconds
    ```
   Kịch bản này sẽ chạy các bài kiểm thử và hiển thị kết quả.

Ngoài ra, tất cả các pull request sẽ được kiểm thử tự động thông qua [GitHub Actions](https://github.com/cp-algorithms/cp-algorithms/actions).

---
*   Original lines: 184
*   Translated lines: 184
*   Code blocks changed? No
*   Inline code changed? No
*   I confirm no character was omitted: YES
