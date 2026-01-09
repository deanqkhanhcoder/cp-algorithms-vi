---
tags:
  - Translated
title: MEX (minimal excluded) of a sequence
e_maxx_link: mex_of_sequence
---
# MEX (giá trị nhỏ nhất không xuất hiện) của một dãy (MEX (minimal excluded) of a sequence) {: #mex-minimal-excluded-of-a-sequence}

Cho một mảng $A$ có kích thước $N$. Bạn phải tìm phần tử không âm nhỏ nhất không có trong mảng. Số đó thường được gọi là **MEX** (minimal excluded).

$$
\begin{align}
\text{mex}(\{0, 1, 2, 4, 5\}) &= 3 \\
\text{mex}(\{0, 1, 2, 3, 4\}) &= 5 \\
\text{mex}(\{1, 2, 3, 4, 5\}) &= 0 \\
\end{align}
$$

Lưu ý rằng MEX của một mảng có kích thước $N$ không bao giờ có thể lớn hơn chính $N$.

Cách tiếp cận dễ nhất là tạo một tập hợp (set) của tất cả các phần tử trong mảng $A$, để chúng ta có thể nhanh chóng kiểm tra xem một số có phải là một phần của mảng hay không.
Sau đó, chúng ta có thể kiểm tra tất cả các số từ $0$ đến $N$, nếu số hiện tại không có trong tập hợp, hãy trả về nó.

## Cài đặt (Implementation) {: #implementation}

Thuật toán sau chạy trong thời gian $O(N \log N)$.

```{.cpp file=mex_simple}
int mex(vector<int> const& A) {
    set<int> b(A.begin(), A.end());

    int result = 0;
    while (b.count(result))
        ++result;
    return result;
}
```

Nếu một thuật toán yêu cầu tính toán MEX trong $O(N)$, có thể thực hiện được bằng cách sử dụng một vectơ boolean thay vì một tập hợp.
Lưu ý rằng mảng cần phải lớn bằng kích thước mảng lớn nhất có thể.


```{.cpp file=mex_linear}
int mex(vector<int> const& A) {
    static bool used[MAX_N+1] = { 0 };

    // đánh dấu các số đã cho
    for (int x : A) {
        if (x <= MAX_N)
            used[x] = true;
    }

    // tìm mex
    int result = 0;
    while (used[result])
        ++result;
 
    // xóa mảng một lần nữa
    for (int x : A) {
        if (x <= MAX_N)
            used[x] = false;
    }

    return result;
}
```

Cách tiếp cận này nhanh, nhưng chỉ hoạt động tốt nếu bạn phải tính toán MEX một lần.
Nếu bạn cần tính toán MEX lặp đi lặp lại, ví dụ: vì mảng của bạn liên tục thay đổi, thì nó không hiệu quả.
Đối với điều đó, chúng ta cần một cái gì đó tốt hơn.

## MEX với cập nhật mảng (MEX with array updates) {: #mex-with-array-updates}

Trong bài toán, bạn cần thay đổi từng số trong mảng và tính toán MEX mới của mảng sau mỗi lần cập nhật như vậy.

Cần có một cấu trúc dữ liệu tốt hơn để xử lý các truy vấn như vậy một cách hiệu quả.

Một cách tiếp cận sẽ là lấy tần suất của mỗi số từ $0$ đến $N$, và xây dựng một cấu trúc dữ liệu giống như cây trên đó.
Ví dụ: cây phân đoạn (segment tree) hoặc treap.
Mỗi nút đại diện cho một phạm vi số, và cùng với tổng tần suất trong phạm vi, bạn lưu trữ thêm lượng số riêng biệt trong phạm vi đó.
Có thể cập nhật cấu trúc dữ liệu này trong thời gian $O(\log N)$, và cũng tìm thấy MEX trong thời gian $O(\log N)$, bằng cách thực hiện tìm kiếm nhị phân cho MEX.
Nếu nút đại diện cho phạm vi $[0, \lfloor N/2 \rfloor)$ không chứa $\lfloor N/2 \rfloor$ nhiều số riêng biệt, thì một số bị thiếu và MEX nhỏ hơn $\lfloor N/2 \rfloor$, và bạn có thể đệ quy trong nhánh bên trái của cây. Nếu không, nó ít nhất là $\lfloor N/2 \rfloor$, và bạn có thể đệ quy trong nhánh bên phải của cây.

Cũng có thể sử dụng các cấu trúc dữ liệu thư viện chuẩn `map` và `set` (dựa trên một cách tiếp cận được giải thích [tại đây](https://codeforces.com/blog/entry/81287?#comment-677837)).
Với `map`, chúng ta sẽ nhớ tần suất của từng số và với `set`, chúng ta đại diện cho các số hiện đang thiếu trong mảng.
Vì `set` được sắp xếp, `*set.begin()` sẽ là MEX.
Tổng cộng chúng ta cần $O(N \log N)$ tính toán trước và sau đó có thể tính toán MEX trong $O(1)$ và cập nhật có thể được thực hiện trong $O(\log N)$.

```{.cpp file=mex_updates}
class Mex {
private:
    map<int, int> frequency;
    set<int> missing_numbers;
    vector<int> A;

public:
    Mex(vector<int> const& A) : A(A) {
        for (int i = 0; i <= A.size(); i++)
            missing_numbers.insert(i);

        for (int x : A) {
            ++frequency[x];
            missing_numbers.erase(x);
        }
    }

    int mex() {
        return *missing_numbers.begin();
    }

    void update(int idx, int new_value) {
        if (--frequency[A[idx]] == 0)
            missing_numbers.insert(A[idx]);
        A[idx] = new_value;
        ++frequency[new_value];
        missing_numbers.erase(new_value);
    }
};
```

## Bài tập (Practice Problems) {: #practice-problems}

- [AtCoder: Neq Min](https://atcoder.jp/contests/hhkb2020/tasks/hhkb2020_c)
- [Codeforces: Informatics in MAC](https://codeforces.com/contest/1935/problem/B)
- [Codeforces: Replace by MEX](https://codeforces.com/contest/1375/problem/D)
- [Codeforces: Vitya and Strange Lesson](https://codeforces.com/problemset/problem/842/D)
- [Codeforces: MEX Queries](https://codeforces.com/contest/817/problem/F)
