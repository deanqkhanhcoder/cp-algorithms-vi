---
title: Sinh tất cả các tổ hợp chập K (Generating all K-combinations)
tags:
  - Translated
e_maxx_link: generating_combinations
---
# Sinh tất cả các tổ hợp chập $K$ (Generating all $K$-combinations) {: #generating-all-k-combinations}

Trong bài viết này, chúng ta sẽ thảo luận về bài toán sinh tất cả các tổ hợp chập $K$.
Cho các số tự nhiên $N$ và $K$, và xem xét một tập hợp các số từ $1$ đến $N$.
Nhiệm vụ là tìm ra tất cả các **tập con có kích thước $K$**.

## Sinh tổ hợp chập $K$ tiếp theo theo thứ tự từ điển (Generate next lexicographical $K$-combination) {: #generate-next-lexicographical-k-combination data-toc-label="Generate next lexicographical K-combination"}

Đầu tiên chúng ta sẽ sinh chúng theo thứ tự từ điển.
Thuật toán cho việc này rất đơn giản. Tổ hợp đầu tiên sẽ là ${1, 2, ..., K}$. Bây giờ hãy xem làm thế nào để tìm tổ hợp theo ngay sau tổ hợp này, theo thứ tự từ điển. Để làm như vậy, chúng ta xem xét tổ hợp hiện tại của mình, và tìm phần tử ngoài cùng bên phải chưa đạt đến giá trị cao nhất có thể của nó. Khi tìm thấy phần tử này, chúng ta tăng nó thêm $1$, và gán giá trị hợp lệ thấp nhất cho tất cả các phần tử tiếp theo.

```{.cpp file=next_combination}
bool next_combination(vector<int>& a, int n) {
    int k = (int)a.size();
    for (int i = k - 1; i >= 0; i--) {
        if (a[i] < n - k + i + 1) {
            a[i]++;
            for (int j = i + 1; j < k; j++)
                a[j] = a[j - 1] + 1;
            return true;
        }
    }
    return false;
}
```

## Sinh tất cả các tổ hợp chập $K$ sao cho các tổ hợp kề nhau khác nhau một phần tử (Generate all $K$-combinations such that adjacent combinations differ by one element) {: #generate-all-k-combinations-such-that-adjacent-combinations-differ-by-one-element data-toc-label="Generate all K-combinations such that adjacent combinations differ by one element"}

Lần này chúng ta muốn sinh tất cả các tổ hợp chập $K$ theo một thứ tự sao cho các tổ hợp kề nhau khác nhau chính xác một phần tử.

Điều này có thể được giải quyết bằng cách sử dụng [Mã Gray](../algebra/gray-code.md):
Nếu chúng ta gán một bitmask cho mỗi tập con, thì bằng cách sinh và lặp qua các bitmask này với mã Gray, chúng ta có thể thu được câu trả lời của mình.

Nhiệm vụ sinh các tổ hợp chập $K$ cũng có thể được giải quyết bằng cách sử dụng Mã Gray theo một cách khác:
Sinh Mã Gray cho các số từ $0$ đến $2^N - 1$ và chỉ giữ lại những mã chứa $K$ số $1$.
Sự thật đáng ngạc nhiên là trong chuỗi $K$ bit được set kết quả, bất kỳ hai mặt nạ lân cận nào (bao gồm cả mặt nạ đầu tiên và cuối cùng - lân cận theo nghĩa vòng tròn) - sẽ khác nhau chính xác hai bit, đó là mục tiêu của chúng ta (xóa một số, thêm một số).

Hãy chứng minh điều này:

Để chứng minh, chúng ta nhắc lại thực tế là chuỗi $G(N)$ (đại diện cho Mã Gray thứ $N$) có thể thu được như sau:

$$G(N) = 0G(N-1) \cup 1G(N-1)^\text{R}$$

Nghĩa là, xem xét chuỗi Mã Gray cho $N-1$, và thêm tiền tố $0$ trước mỗi số hạng. Và xem xét chuỗi Mã Gray đảo ngược cho $N-1$ và thêm tiền tố $1$ trước mỗi mặt nạ, và nối hai chuỗi này lại.

Bây giờ chúng ta có thể đưa ra chứng minh của mình.

Đầu tiên, chúng ta chứng minh rằng mặt nạ đầu tiên và cuối cùng khác nhau chính xác ở hai bit. Để làm điều này, là đủ để lưu ý rằng mặt nạ đầu tiên của chuỗi $G(N)$, sẽ có dạng $N-K$ số $0$, theo sau là $K$ số $1$. Vì bit đầu tiên được đặt là $0$, sau đó là $(N-K-1)$ số $0$, sau đó là $K$ bit được set theo sau và mặt nạ cuối cùng sẽ có dạng $1$, sau đó là $(N-K)$ số $0$, sau đó là $K-1$ số $1$.
Áp dụng nguyên lý quy nạp toán học, và sử dụng công thức cho $G(N)$, kết luận chứng minh.

Bây giờ nhiệm vụ của chúng ta là chỉ ra rằng bất kỳ hai mã liền kề nào cũng khác nhau chính xác ở hai bit, chúng ta có thể làm điều này bằng cách xem xét phương trình đệ quy của chúng ta cho việc sinh Mã Gray. Hãy giả sử nội dung của hai nửa được hình thành bởi $G(N-1)$ là đúng. Bây giờ chúng ta cần chứng minh rằng cặp liên tiếp mới được hình thành tại điểm nối (bằng cách nối hai nửa này) cũng hợp lệ, tức là chúng khác nhau chính xác hai bit.

Điều này có thể được thực hiện, vì chúng ta biết mặt nạ cuối cùng của nửa đầu tiên và mặt nạ đầu tiên của nửa thứ hai. Mặt nạ cuối cùng của nửa đầu tiên sẽ là $1$, sau đó là $(N-K-1)$ số $0$, sau đó là $K-1$ số $1$. Và mặt nạ đầu tiên của nửa thứ hai sẽ là $0$, sau đó $(N-K-2)$ số $0$ sẽ theo sau, và sau đó là $K$ số $1$. Do đó, so sánh hai mặt nạ, chúng ta tìm thấy chính xác hai bit khác nhau.

Dưới đây là một cài đặt ngây thơ hoạt động bằng cách sinh tất cả $2^{n}$ tập con có thể, và tìm các tập con có kích thước $K$.

```{.cpp file=generate_all_combinations_naive}
int gray_code (int n) {
    return n ^ (n >> 1);
}

int count_bits (int n) {
    int res = 0;
    for (; n; n >>= 1)
        res += n & 1;
    return res;
}

void all_combinations (int n, int k) {
    for (int i = 0; i < (1 << n); i++) {
        int cur = gray_code (i);
        if (count_bits(cur) == k) {
            for (int j = 0; j < n; j++) {
                if (cur & (1 << j))
                    cout << j + 1;
            }
            cout << "\n";
        }
    }
}
```

Đáng chú ý là tồn tại một cài đặt hiệu quả hơn chỉ dùng đến việc xây dựng các tổ hợp hợp lệ và do đó hoạt động trong $O\left(N \cdot \binom{N}{K}\right)$ tuy nhiên nó có bản chất đệ quy và đối với các giá trị nhỏ của $N$ nó có thể có hằng số lớn hơn so với giải pháp trước đó.

Việc cài đặt được bắt nguồn từ công thức:

$$G(N, K) = 0G(N-1, K) \cup 1G(N-1, K-1)^\text{R}$$

Công thức này thu được bằng cách sửa đổi phương trình chung để xác định mã Gray, và hoạt động bằng cách chọn chuỗi con từ các phần tử thích hợp.

Cài đặt của nó như sau:

```{.cpp file=generate_all_combinations_fast}
vector<int> ans;

void gen(int n, int k, int idx, bool rev) {
    if (k > n || k < 0)
        return;

    if (!n) {
        for (int i = 0; i < idx; ++i) {
            if (ans[i])
                cout << i + 1;
        }
        cout << "\n";
        return;
    }

    ans[idx] = rev;
    gen(n - 1, k - rev, idx + 1, false);
    ans[idx] = !rev;
    gen(n - 1, k - !rev, idx + 1, true);
}

void all_combinations(int n, int k) {
    ans.resize(n);
    gen(n, k, 0, false);
}
```

---

## Checklist

- Original lines: 142
- Translated lines: 142
- Code blocks changed? No
- Inline code changed? No
- Technical terms kept in English? Yes
- Headings anchors preserved/added correctly? Yes
- I confirm no character was omitted: YES
