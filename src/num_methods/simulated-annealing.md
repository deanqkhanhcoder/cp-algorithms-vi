---
tags:
    - Original
---

# Luyện kim mô phỏng (Simulated Annealing) {: #simulated-annealing}

**Luyện kim mô phỏng (Simulated Annealing - SA)** là một thuật toán ngẫu nhiên, xấp xỉ tối ưu toàn cục của một hàm. Nó được gọi là thuật toán ngẫu nhiên, bởi vì nó sử dụng một lượng ngẫu nhiên nhất định trong tìm kiếm của mình và do đó đầu ra của nó có thể thay đổi đối với cùng một đầu vào.

## Vấn đề (The problem) {: #the-problem}

Chúng ta được cho một hàm $E(s)$, tính toán năng lượng của trạng thái $s$. Chúng tôi có nhiệm vụ tìm trạng thái $s_{best}$ tại đó $E(s)$ được giảm thiểu. **SA** phù hợp với các bài toán trong đó các trạng thái là rời rạc và $E(s)$ có nhiều cực tiểu địa phương. Chúng tôi sẽ lấy ví dụ về [Vấn đề người bán hàng (Travelling Salesman Problem - TSP)](https://en.wikipedia.org/wiki/Travelling_salesman_problem). 

### Vấn đề người bán hàng (Travelling Salesman Problem - TSP) {: #travelling-salesman-problem-tsp}

Bạn được cung cấp một tập hợp các nút trong không gian 2 chiều. Mỗi nút được đặc trưng bởi tọa độ $x$ và $y$ của nó. Nhiệm vụ của bạn là tìm thứ tự của các nút, thứ tự này sẽ giảm thiểu khoảng cách di chuyển khi truy cập các nút này theo thứ tự đó.

## Động lực (Motivation) {: #motivation}

Luyện kim (Annealing) là một quá trình luyện kim, trong đó vật liệu được nung nóng và để nguội, để cho phép các nguyên tử bên trong tự sắp xếp lại theo một sự sắp xếp với năng lượng bên trong tối thiểu, điều này làm cho vật liệu có các tính chất khác nhau. Trạng thái là sự sắp xếp của các nguyên tử và năng lượng bên trong là hàm được cực tiểu hóa. Chúng ta có thể nghĩ về trạng thái ban đầu của các nguyên tử, như một cực tiểu địa phương cho năng lượng bên trong của nó. Để làm cho vật liệu sắp xếp lại các nguyên tử của nó, chúng ta cần thúc đẩy nó đi qua một vùng mà năng lượng bên trong của nó không được giảm thiểu để đạt được cực tiểu toàn cục. Động lực này được đưa ra bằng cách nung nóng vật liệu đến nhiệt độ cao hơn.

Luyện kim mô phỏng, theo nghĩa đen, mô phỏng quá trình này. Chúng ta bắt đầu với một số trạng thái ngẫu nhiên (vật liệu) và thiết lập nhiệt độ cao (làm nóng nó). Bây giờ, thuật toán đã sẵn sàng chấp nhận các trạng thái có năng lượng cao hơn trạng thái hiện tại, vì nó được thúc đẩy bởi nhiệt độ cao. Điều này ngăn thuật toán bị kẹt bên trong cực tiểu cục bộ và di chuyển về phía cực tiểu toàn cục. Khi thời gian trôi qua, thuật toán nguội đi và từ chối các trạng thái có năng lượng cao hơn và di chuyển vào cực tiểu gần nhất mà nó tìm thấy.

### Hàm năng lượng E(s) {: #energy-function-e-s}

$E(s)$ là hàm cần được cực tiểu hóa (hoặc cực đại hóa). Nó ánh xạ mọi trạng thái đến một số thực. Trong trường hợp của TSP, $E(s)$ trả về khoảng cách đi một vòng tròn đầy đủ theo thứ tự các nút ở trạng thái đó.

### Trạng thái (State) {: #state}

Không gian trạng thái là miền của hàm năng lượng, $E(s)$, và trạng thái là bất kỳ phần tử nào thuộc về không gian trạng thái. Trong trường hợp của TSP, tất cả các đường đi có thể mà chúng ta có thể thực hiện để truy cập tất cả các nút là không gian trạng thái và bất kỳ đường đi nào trong số này cũng có thể được coi là một trạng thái.

### Trạng thái lân cận (Neighbouring state) {: #neighbouring-state}

Nó là một trạng thái trong không gian trạng thái gần với trạng thái trước đó. Điều này thường có nghĩa là chúng ta có thể thu được trạng thái lân cận từ trạng thái ban đầu bằng cách sử dụng một phép biến đổi đơn giản. Trong trường hợp của bài toán người bán hàng, trạng thái lân cận thu được bằng cách chọn ngẫu nhiên 2 nút và hoán đổi vị trí của chúng ở trạng thái hiện tại.

## Thuật toán (Algorithm) {: #algorithm}

Chúng ta bắt đầu với một trạng thái ngẫu nhiên $s$. Trong mỗi bước, chúng tôi chọn một trạng thái lân cận $s_{next}$ của trạng thái hiện tại $s$. Nếu $E(s_{next}) < E(s)$, thì chúng ta cập nhật $s = s_{next}$. Nếu không, chúng ta sử dụng hàm chấp nhận xác suất (**Probability Acceptance Function**) $P(E(s),E(s_{next}),T)$ để quyết định xem chúng ta nên chuyển sang $s_{next}$ hay ở lại $s$. T ở đây là nhiệt độ, ban đầu được đặt thành giá trị cao và phân rã chậm theo từng bước. Nhiệt độ càng cao, càng có nhiều khả năng di chuyển đến $s_{next}$.
Đồng thời, chúng tôi cũng theo dõi trạng thái tốt nhất $s_{best}$ qua tất cả các lần lặp. Tiếp tục cho đến khi hội tụ hoặc hết thời gian.


<center>
<img src="https://upload.wikimedia.org/wikipedia/commons/d/d5/Hill_Climbing_with_Simulated_Annealing.gif" width="800px">
<br>
<i>Biểu diễn trực quan về Luyện kim mô phỏng, tìm kiếm cực đại của hàm này với nhiều cực đại cục bộ.</i>
<br>
</center>

### Nhiệt độ (T) và phân rã (u) {: #temperature-t-and-decay-u}

Nhiệt độ của hệ thống định lượng sự sẵn sàng của thuật toán để chấp nhận một trạng thái có năng lượng cao hơn. Sự phân rã là một hằng số định lượng "tốc độ làm mát" của thuật toán. Tốc độ làm mát chậm ($u$ lớn hơn) được biết là cho kết quả tốt hơn.

## Hàm chấp nhận xác suất (Probability Acceptance Function - PAF) {: #probability-acceptance-function-paf}

$P(E,E_{next},T) = 
    \begin{cases}
       \text{True} &\quad\text{nếu }  \mathcal{U}_{[0,1]} \le \exp(-\frac{E_{next}-E}{T}) \\
       \text{False} &\quad\text{ngược lại}\\
     \end{cases}$

Ở đây, $\mathcal{U}_{[0,1]}$ là một giá trị ngẫu nhiên thống nhất liên tục trên $[0,1]$. Hàm này nhận trạng thái hiện tại, trạng thái tiếp theo và nhiệt độ, trả về giá trị boolean, cho biết tìm kiếm của chúng tôi liệu nó có nên chuyển đến $s_{next}$ hay ở lại $s$. Lưu ý rằng đối với $E_{next} < E$ , hàm này sẽ luôn trả về True, nếu không, nó vẫn có thể thực hiện di chuyển với xác suất $\exp(-\frac{E_{next}-E}{T})$, tương ứng với [thước đo Gibbs](https://en.wikipedia.org/wiki/Gibbs_measure).

```cpp
bool P(double E,double E_next,double T,mt19937 rng){
    double prob =  exp(-(E_next-E)/T);
    if(prob > 1) return true;
    else{
        bernoulli_distribution d(prob); 
        return d(rng);
    }
}
```
## Mẫu Code (Code Template) {: #code-template}

```cpp
class state {
    public:
    state() {
        // Tạo trạng thái ban đầu
    }
    state next() {
        state s_next;
        // Sửa đổi s_next thành trạng thái lân cận ngẫu nhiên
        return s_next;
    }
    double E() {
        // Cài đặt hàm năng lượng ở đây
    };
};


pair<double, state> simAnneal() {
    state s = state();
    state best = s;
    double T = 10000; // Nhiệt độ ban đầu
    double u = 0.995; // Tỷ lệ phân rã
    double E = s.E();
    double E_next;
    double E_best = E;
    mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());
    while (T > 1) {
        state next = s.next();
        E_next = next.E();
        if (P(E, E_next, T, rng)) {
            s = next;
            if (E_next < E_best) {
                best = s;
                E_best = E_next;
            }
            E = E_next;
        }
        T *= u;
    }
    return {E_best, best};
}

```
## Cách sử dụng (How to use) {: #how-to-use}
Điền vào các hàm lớp trạng thái khi thích hợp. Nếu bạn đang cố gắng tìm cực đại toàn cục chứ không phải cực tiểu, hãy đảm bảo rằng hàm $E()$ trả về số âm của hàm bạn đang tối đa hóa và in ra $-E_{best}$ cuối cùng. Đặt các tham số dưới đây theo nhu cầu của bạn.

### Tham số (Parameters) {: #parameters}
- $T$ : Nhiệt độ ban đầu. Đặt nó thành giá trị cao hơn nếu bạn muốn tìm kiếm chạy trong thời gian dài hơn.
- $u$ : Phân rã. Quyết định tốc độ làm mát. Tốc độ làm mát chậm hơn (giá trị u lớn hơn) thường cho kết quả tốt hơn với chi phí chạy trong thời gian dài hơn. Đảm bảo $u < 1$. 

Số lần lặp mà vòng lặp sẽ chạy được cho bởi biểu thức

$N =   \lceil -\log_{u}{T} \rceil$ 

Mẹo chọn $T$ và $u$ : Nếu có nhiều cực tiểu cục bộ và không gian trạng thái rộng, hãy đặt $u = 0.999$, đối với tốc độ làm mát chậm, điều này sẽ cho phép thuật toán khám phá nhiều khả năng hơn. Mặt khác, nếu không gian trạng thái hẹp hơn, $u = 0.99$ là đủ. Nếu bạn không chắc chắn, hãy chơi an toàn bằng cách đặt $u = 0.998$ hoặc cao hơn. Tính toán độ phức tạp thời gian của một lần lặp duy nhất của thuật toán và sử dụng giá trị này để ước tính giá trị của $N$ để ngăn TLE, sau đó sử dụng công thức dưới đây để thu được $T$.

$T = u^{-N}$

### Ví dụ cài đặt cho TSP (Example implementation for TSP) {: #example-implementation-for-tsp}

```cpp

class state {
    public:
    vector<pair<int, int>> points;
	std::mt19937 mt{ static_cast<std::mt19937::result_type>(
		std::chrono::steady_clock::now().time_since_epoch().count()
		) };
    state() {
        points = {% raw %}{{0,0},{2,2},{0,2},{2,0},{0,1},{1,2},{2,1},{1,0}}{% endraw %};
    }
    state next() {
        state s_next;
        s_next.points = points;
        uniform_int_distribution<> choose(0, points.size()-1);
        int a = choose(mt);
        int b = choose(mt);
        s_next.points[a].swap(s_next.points[b]);
        return s_next;
    }

    double euclidean(pair<int, int> a, pair<int, int> b) {
        return hypot(a.first - b.first, a.second - b.second);
    }
    
    double E() {
        double dist = 0;
        int n = points.size();
        for (int i = 0;i < n; i++)
            dist += euclidean(points[i], points[(i+1)%n]);
        return dist;
    };
};

int main() {
    pair<double, state> res;
    res = simAnneal();
    double E_best = res.first;
    state best = res.second;
    cout << "Lenght of shortest path found : " << E_best << "\n";
    cout << "Order of points in shortest path : \n";
    for(auto x: best.points) {
        cout << x.first << " " << x.second << "\n";
    }
}
```

## Các sửa đổi khác đối với thuật toán (Further modifications to the algorithm) {: #further-modifications-to-the-algorithm}

- Thêm điều kiện thoát dựa trên thời gian vào vòng lặp while để ngăn TLE
- Sự phân rã được thực hiện ở trên là phân rã theo cấp số nhân. Bạn luôn có thể thay thế điều này bằng một hàm phân rã theo nhu cầu của bạn.
- Hàm chấp nhận xác suất được đưa ra ở trên, thích chấp nhận các trạng thái có năng lượng thấp hơn vì thừa số $E_{next} - E$ trong tử số của số mũ. Bạn có thể chỉ cần loại bỏ yếu tố này để làm cho PAF độc lập với sự khác biệt về năng lượng.
- Ảnh hưởng của sự khác biệt về năng lượng, $E_{next} - E$, trên PAF có thể tăng/giảm bằng cách tăng/giảm cơ số của số mũ như hình dưới đây: 
```cpp
bool P(double E, double E_next, double T, mt19937 rng) {
    double e = 2; // đặt e thành bất kỳ số thực nào lớn hơn 1
    double prob =  pow(e,-(E_next-E)/T);
    if (prob > 1)
        return true;
    else {
        bernoulli_distribution d(prob); 
        return d(rng);
    }
}
```

## Bài tập (Problems) {: #problems}

- [USACO Jan 2017 - Subsequence Reversal](https://usaco.org/index.php?page=viewproblem2&cpid=698)
- [Deltix Summer 2021 - DIY Tree](https://codeforces.com/contest/1556/problem/H)
- [AtCoder Contest Scheduling](https://atcoder.jp/contests/intro-heuristics/tasks/intro_heuristics_a)
