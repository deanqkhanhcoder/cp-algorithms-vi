---
title: Sinh tất cả các tổ hợp chập K
tags:
  - Translated
e_maxx_link: generating_combinations
---
# Sinh tất cả các tổ hợp chập $K$

Trong bài viết này, chúng ta sẽ thảo luận về bài toán sinh tất cả các tổ hợp chập $K$.
Cho các số tự nhiên $N$ và $K$, và xét một tập hợp các số từ $1$ đến $N$.
Nhiệm vụ là suy ra tất cả các **tập con có kích thước $K$**.

## Sinh tổ hợp chập K tiếp theo theo thứ tự từ điển {data-toc-label="Generate next lexicographical K-combination"}

Đầu tiên, chúng ta sẽ sinh chúng theo thứ tự từ điển.
Thuật toán cho việc này rất đơn giản. Tổ hợp đầu tiên sẽ là ${1, 2, ..., K}$. Bây giờ hãy xem làm thế nào
để tìm tổ hợp ngay sau tổ hợp này, theo thứ tự từ điển. Để làm điều đó, chúng ta xem xét tổ hợp hiện tại của mình,
và tìm phần tử ngoài cùng bên phải chưa đạt đến giá trị cao nhất có thể của nó. Sau khi tìm thấy
phần tử này, chúng ta tăng nó lên $1$, và gán giá trị hợp lệ thấp nhất cho tất cả các phần tử tiếp theo.

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

## Sinh tất cả các tổ hợp chập K sao cho các tổ hợp liền kề khác nhau một phần tử {data-toc-label="Generate all K-combinations such that adjacent combinations differ by one element"}

Lần này, chúng ta muốn sinh tất cả các tổ hợp chập $K$ theo một thứ tự
sao cho các tổ hợp liền kề khác nhau chính xác một phần tử.

Điều này có thể được giải quyết bằng cách sử dụng [Mã Gray](../algebra/gray-code.md):
Nếu chúng ta gán một bitmask cho mỗi tập con, thì bằng cách sinh và lặp qua các bitmask này bằng mã Gray, chúng ta có thể có được câu trả lời của mình.

Nhiệm vụ sinh các tổ hợp chập $K$ cũng có thể được giải quyết bằng cách sử dụng Mã Gray theo một cách khác:
Sinh Mã Gray cho các số từ $0$ đến $2^N - 1$ và chỉ giữ lại những mã chứa $K$ bit $1$.
Sự thật đáng ngạc nhiên là trong dãy kết quả của các bit được đặt $K$, bất kỳ hai mặt nạ lân cận nào (bao gồm cả
mặt nạ đầu tiên và cuối cùng - lân cận theo nghĩa vòng) - sẽ khác nhau chính xác hai bit, đó là mục tiêu của chúng ta (loại bỏ
một số, thêm một số).

Hãy chứng minh điều này:

Để chứng minh, chúng ta nhớ lại thực tế rằng dãy $G(N)$ (đại diện cho Mã Gray thứ $N$) có thể 
được thu được như sau:

$$G(N) = 0G(N-1) \cup 1G(N-1)^\text{R}$$ 

Tức là, xét dãy Mã Gray cho $N-1$, và đặt tiền tố $0$ trước mỗi số hạng. Và xét dãy 
Mã Gray đảo ngược cho $N-1$ và đặt tiền tố $1$ trước mỗi mặt nạ, và
nối hai dãy này lại.

Bây giờ chúng ta có thể đưa ra chứng minh của mình.

Đầu tiên, chúng ta chứng minh rằng mặt nạ đầu tiên và cuối cùng khác nhau chính xác hai bit. Để làm điều này, chỉ cần lưu ý
rằng mặt nạ đầu tiên của dãy $G(N)$ sẽ có dạng $N-K$ số $0$, theo sau là $K$ số $1$. Vì
bit đầu tiên được đặt là $0$, sau đó là $(N-K-1)$ số $0$, sau đó là $K$ bit được đặt và mặt nạ cuối cùng sẽ có dạng $1$, sau đó là $(N-K)$ số $0$, sau đó là $K-1$ số $1$.
Áp dụng nguyên lý quy nạp toán học, và sử dụng công thức cho $G(N)$, kết thúc chứng minh.

Bây giờ nhiệm vụ của chúng ta là chỉ ra rằng bất kỳ hai mã liền kề nào cũng khác nhau chính xác hai bit, chúng ta có thể làm điều này bằng cách xem xét phương trình đệ quy của chúng ta để sinh Mã Gray. Hãy giả sử nội dung của hai nửa được hình thành bởi $G(N-1)$ là đúng. Bây giờ chúng ta cần chứng minh rằng cặp liên tiếp mới được hình thành tại điểm nối (bằng cách nối hai nửa này) cũng hợp lệ, tức là chúng khác nhau chính xác hai bit.

Điều này có thể được thực hiện, vì chúng ta biết mặt nạ cuối cùng của nửa đầu tiên và mặt nạ đầu tiên của nửa thứ hai. Mặt nạ cuối cùng của nửa đầu tiên sẽ là $1$, sau đó là $(N-K-1)$ số $0$, sau đó là $K-1$ số $1$. Và mặt nạ đầu tiên của nửa thứ hai sẽ là $0$, sau đó là $(N-K-2)$ số $0$ sẽ theo sau, và sau đó là $K$ số $1$. Do đó, so sánh hai mặt nạ, chúng ta tìm thấy chính xác hai bit khác nhau.

Sau đây là một triển khai ngây thơ hoạt động bằng cách sinh tất cả $2^{n}$ tập con có thể, và tìm các tập con có kích thước
$K$.

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

Đáng nói là tồn tại một triển khai hiệu quả hơn chỉ dựa vào việc xây dựng các tổ hợp hợp lệ và do đó
hoạt động trong $O
\cdot \binom{N}{K}\right)$ tuy nhiên nó có bản chất đệ quy và đối với các giá trị nhỏ hơn của $N$, nó có thể có hằng số lớn hơn
so với giải pháp trước đó.

Việc triển khai được suy ra từ công thức:

$$G(N, K) = 0G(N-1, K) \cup 1G(N-1, K-1)^\text{R}$$ 

Công thức này thu được bằng cách sửa đổi phương trình chung để xác định mã Gray, và hoạt động bằng cách chọn
dãy con từ các phần tử thích hợp.

Việc triển khai của nó như sau:

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