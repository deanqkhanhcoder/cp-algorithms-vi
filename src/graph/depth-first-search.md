--- 
tags:
  - Translated
e_maxx_link: dfs
---

# Tìm kiếm theo chiều sâu (DFS)

Tìm kiếm theo chiều sâu là một trong những thuật toán đồ thị chính.

Tìm kiếm theo chiều sâu tìm đường đi đầu tiên theo thứ tự từ điển trong đồ thị từ một đỉnh nguồn $u$ đến mỗi đỉnh.
Tìm kiếm theo chiều sâu cũng sẽ tìm thấy các đường đi ngắn nhất trong một cây (vì chỉ tồn tại một đường đi đơn giản), nhưng trên các đồ thị tổng quát thì không phải như vậy.

Thuật toán hoạt động trong thời gian $O(m + n)$ trong đó $n$ là số đỉnh và $m$ là số cạnh.

## Mô tả thuật toán

Ý tưởng đằng sau DFS là đi sâu vào đồ thị nhất có thể, và quay lui một khi bạn ở một đỉnh không có đỉnh kề nào chưa được thăm.

Rất dễ để mô tả / triển khai thuật toán một cách đệ quy:
Chúng ta bắt đầu tìm kiếm tại một đỉnh.
Sau khi thăm một đỉnh, chúng ta tiếp tục thực hiện một DFS cho mỗi đỉnh kề mà chúng ta chưa thăm trước đó.
Bằng cách này, chúng ta thăm tất cả các đỉnh có thể đến được từ đỉnh bắt đầu.

Để biết thêm chi tiết, hãy xem phần triển khai.

## Ứng dụng của Tìm kiếm theo chiều sâu

  * Tìm bất kỳ đường đi nào trong đồ thị từ đỉnh nguồn $u$ đến tất cả các đỉnh.
  
  * Tìm đường đi đầu tiên theo thứ tự từ điển trong đồ thị từ nguồn $u$ đến tất cả các đỉnh.
  
  * Kiểm tra xem một đỉnh trong cây có phải là tổ tiên của một đỉnh khác hay không:
  
    Vào đầu và cuối mỗi lần gọi tìm kiếm, chúng ta ghi nhớ "thời gian" vào và ra của mỗi đỉnh.
    Bây giờ bạn có thể tìm câu trả lời cho bất kỳ cặp đỉnh nào $(i, j)$ trong $O(1)$:
    đỉnh $i$ là tổ tiên của đỉnh $j$ khi và chỉ khi $\text{entry}[i] < \text{entry}[j]$ và $\text{exit}[i] > \text{exit}[j]$.
  
  * Tìm tổ tiên chung thấp nhất (LCA) của hai đỉnh.
  
  * Sắp xếp tô pô:
  
    Chạy một loạt các tìm kiếm theo chiều sâu để thăm mỗi đỉnh đúng một lần trong thời gian $O(n + m)$.
    Thứ tự tô pô cần thiết sẽ là các đỉnh được sắp xếp theo thứ tự giảm dần của thời gian ra.
  
  
  * Kiểm tra xem một đồ thị đã cho có phải là không có chu trình hay không và tìm các chu trình trong một đồ thị. (Như đã đề cập dưới đây bằng cách đếm các cạnh ngược trong mọi thành phần liên thông).
  
  * Tìm các thành phần liên thông mạnh trong một đồ thị có hướng:
  
    Đầu tiên thực hiện sắp xếp tô pô của đồ thị.
    Sau đó chuyển vị đồ thị và chạy một loạt các tìm kiếm theo chiều sâu khác theo thứ tự được xác định bởi sắp xếp tô pô. Đối với mỗi lần gọi DFS, thành phần được tạo bởi nó là một thành phần liên thông mạnh.
  
  * Tìm các cầu trong một đồ thị vô hướng:
  
    Đầu tiên chuyển đổi đồ thị đã cho thành một đồ thị có hướng bằng cách chạy một loạt các tìm kiếm theo chiều sâu và làm cho mỗi cạnh có hướng khi chúng ta đi qua nó, theo hướng chúng ta đã đi. Thứ hai, tìm các thành phần liên thông mạnh trong đồ thị có hướng này. Cầu là các cạnh có các đầu thuộc các thành phần liên thông mạnh khác nhau.

## Phân loại các cạnh của đồ thị

Chúng ta có thể phân loại các cạnh của một đồ thị, $G$, bằng cách sử dụng thời gian vào và ra của các nút cuối $u$ và $v$ của các cạnh $(u,v)$.
Các phân loại này thường được sử dụng cho các bài toán như [tìm cầu](bridge-searching.md) và [tìm điểm khớp](cutpoints.md).

Chúng ta thực hiện một DFS và phân loại các cạnh gặp phải bằng các quy tắc sau:

Nếu $v$ chưa được thăm:

* Cạnh cây - Nếu $v$ được thăm sau $u$ thì cạnh $(u,v)$ được gọi là cạnh cây. Nói cách khác, nếu $v$ được thăm lần đầu tiên và $u$ hiện đang được thăm thì $(u,v)$ được gọi là cạnh cây.
Những cạnh này tạo thành một cây DFS và do đó có tên là cạnh cây.

Nếu $v$ được thăm trước $u$:

* Cạnh ngược - Nếu $v$ là tổ tiên của $u$, thì cạnh $(u,v)$ là một cạnh ngược. $v$ là một tổ tiên chính xác nếu chúng ta đã vào $v$, nhưng chưa ra khỏi nó. Các cạnh ngược hoàn thành một chu trình vì có một đường đi từ tổ tiên $v$ đến hậu duệ $u$ (trong đệ quy của DFS) và một cạnh từ hậu duệ $u$ đến tổ tiên $v$ (cạnh ngược), do đó một chu trình được hình thành. Các chu trình có thể được phát hiện bằng cách sử dụng các cạnh ngược.

* Cạnh xuôi - Nếu $v$ là hậu duệ của $u$, thì cạnh $(u, v)$ là một cạnh xuôi. Nói cách khác, nếu chúng ta đã thăm và ra khỏi $v$ và $\text{entry}[u] < \text{entry}[v]$ thì cạnh $(u,v)$ tạo thành một cạnh xuôi.
* Cạnh chéo: nếu $v$ không phải là tổ tiên cũng không phải là hậu duệ của $u$, thì cạnh $(u, v)$ là một cạnh chéo. Nói cách khác, nếu chúng ta đã thăm và ra khỏi $v$ và $\text{entry}[u] > \text{entry}[v]$ thì $(u,v)$ là một cạnh chéo.

**Định lý**. Cho $G$ là một đồ thị vô hướng. Khi đó, thực hiện một DFS trên $G$ sẽ phân loại mọi cạnh gặp phải là cạnh cây hoặc cạnh ngược, tức là, các cạnh xuôi và cạnh chéo chỉ tồn tại trong các đồ thị có hướng.

Giả sử $(u,v)$ là một cạnh tùy ý của $G$ và không mất tính tổng quát, $u$ được thăm trước $v$, tức là, $\text{entry}[u] < \text{entry}[v]$. Vì DFS chỉ xử lý các cạnh một lần, chỉ có hai cách để chúng ta có thể xử lý cạnh $(u,v)$ và do đó phân loại nó:

* Lần đầu tiên chúng ta khám phá cạnh $(u,v)$ là theo hướng từ $u$ đến $v$. Vì $\text{entry}[u] < \text{entry}[v]$, bản chất đệ quy của DFS có nghĩa là nút $v$ sẽ được khám phá hoàn toàn và do đó sẽ ra khỏi trước khi chúng ta có thể "quay trở lại ngăn xếp cuộc gọi" để ra khỏi nút $u$. Do đó, nút $v$ phải chưa được thăm khi DFS lần đầu tiên khám phá cạnh $(u,v)$ từ $u$ đến $v$ vì nếu không, việc tìm kiếm sẽ khám phá $(u,v)$ từ $v$ đến $u$ trước khi ra khỏi nút $v$, vì các nút $u$ và $v$ là hàng xóm. Do đó, cạnh $(u,v)$ là một cạnh cây.

* Lần đầu tiên chúng ta khám phá cạnh $(u,v)$ là theo hướng từ $v$ đến $u$. Vì chúng ta đã phát hiện ra nút $u$ trước khi phát hiện ra nút $v$, và chúng ta chỉ xử lý các cạnh một lần, cách duy nhất để chúng ta có thể khám phá cạnh $(u,v)$ theo hướng từ $v$ đến $u$ là nếu có một đường đi khác từ $u$ đến $v$ không liên quan đến cạnh $(u,v)$, do đó làm cho $u$ trở thành tổ tiên của $v$. Cạnh $(u,v)$ do đó hoàn thành một chu trình vì nó đi từ hậu duệ, $v$, đến tổ tiên, $u$, mà chúng ta chưa ra khỏi. Do đó, cạnh $(u,v)$ là một cạnh ngược.

Vì chỉ có hai cách để xử lý cạnh $(u,v)$, với hai trường hợp và các phân loại kết quả của chúng được nêu ở trên, việc thực hiện một DFS trên $G$ do đó sẽ phân loại mọi cạnh gặp phải là cạnh cây hoặc cạnh ngược, tức là, các cạnh xuôi và cạnh chéo chỉ tồn tại trong các đồ thị có hướng. Điều này hoàn thành chứng minh.

## Cài đặt

```cpp
vector<vector<int>> adj; // đồ thị được biểu diễn dưới dạng danh sách kề
int n; // số đỉnh

vector<bool> visited;

void dfs(int v) {
	visited[v] = true;
	for (int u : adj[v]) {
		if (!visited[u])
			dfs(u);
    }
}
```
Đây là cách triển khai đơn giản nhất của Tìm kiếm theo chiều sâu.
Như đã mô tả trong các ứng dụng, có thể hữu ích khi tính toán thêm thời gian vào và ra và màu của đỉnh.
Chúng ta sẽ tô màu tất cả các đỉnh bằng màu 0, nếu chúng ta chưa thăm chúng, bằng màu 1 nếu chúng ta đã thăm chúng, và bằng màu 2, nếu chúng ta đã ra khỏi đỉnh đó.

Đây là một triển khai chung tính toán thêm những điều đó:

```cpp
vector<vector<int>> adj; // đồ thị được biểu diễn dưới dạng danh sách kề
int n; // số đỉnh

vector<int> color;

vector<int> time_in, time_out;
int dfs_timer = 0;

void dfs(int v) {
	time_in[v] = dfs_timer++;
	color[v] = 1;
	for (int u : adj[v])
		if (color[u] == 0)
			dfs(u);
	color[v] = 2;
	time_out[v] = dfs_timer++;
}
```

## Bài tập thực hành

* [SPOJ: ABCPATH](http://www.spoj.com/problems/ABCPATH/)
* [SPOJ: EAGLE1](http://www.spoj.com/problems/EAGLE1/)
* [Codeforces: Kefa and Park](http://codeforces.com/problemset/problem/580/C)
* [Timus:Werewolf](http://acm.timus.ru/problem.aspx?space=1&num=1242)
* [Timus:Penguin Avia](http://acm.timus.ru/problem.aspx?space=1&num=1709)
* [Timus:Two Teams](http://acm.timus.ru/problem.aspx?space=1&num=1106)
* [SPOJ - Ada and Island](http://www.spoj.com/problems/ADASEA/)
* [UVA 657 - The die is cast](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=598)
* [SPOJ - Sheep](http://www.spoj.com/problems/KOZE/)
* [SPOJ - Path of the Rightenous Man](http://www.spoj.com/problems/RIOI_2_3/)
* [SPOJ - Validate the Maze](http://www.spoj.com/problems/MAKEMAZE/)
* [SPOJ - Ghosts having Fun](http://www.spoj.com/problems/GHOSTS/)
* [Codeforces - Underground Lab](http://codeforces.com/contest/781/problem/C)
* [DevSkill - Maze Tester (archived)](http://web.archive.org/web/20200319103915/https://www.devskill.com/CodingProblems/ViewProblem/3)
* [DevSkill - Tourist (archived)](http://web.archive.org/web/20190426175135/https://devskill.com/CodingProblems/ViewProblem/17)
* [Codeforces - Anton and Tree](http://codeforces.com/contest/734/problem/E)
* [Codeforces - Transformation: From A to B](http://codeforces.com/contest/727/problem/A)
* [Codeforces - One Way Reform](http://codeforces.com/contest/723/problem/E)
* [Codeforces - Centroids](http://codeforces.com/contest/709/problem/E)
* [Codeforces - Generate a String](http://codeforces.com/contest/710/problem/E)
* [Codeforces - Broken Tree](http://codeforces.com/contest/758/problem/E)
* [Codeforces - Dasha and Puzzle](http://codeforces.com/contest/761/problem/E)
* [Codeforces - Making genome In Berland](http://codeforces.com/contest/638/problem/B)
* [Codeforces - Road Improvement](http://codeforces.com/contest/638/problem/C)
* [Codeforces - Garland](http://codeforces.com/contest/767/problem/C)
* [Codeforces - Labeling Cities](http://codeforces.com/contest/794/problem/D)
* [Codeforces - Send the Fool Futher!](http://codeforces.com/contest/802/problem/K)
* [Codeforces - The tag Game](http://codeforces.com/contest/813/problem/C)
* [Codeforces - Leha and Another game about graphs](http://codeforces.com/contest/841/problem/D)
* [Codeforces - Shortest path problem](http://codeforces.com/contest/845/problem/G)
* [Codeforces - Upgrading Tree](http://codeforces.com/contest/844/problem/E)
* [Codeforces - From Y to Y](http://codeforces.com/contest/849/problem/C)
* [Codeforces - Chemistry in Berland](http://codeforces.com/contest/846/problem/E)
* [Codeforces - Wizards Tour](http://codeforces.com/contest/861/problem/F)
* [Codeforces - Ring Road](http://codeforces.com/contest/24/problem/A)
* [Codeforces - Mail Stamps](http://codeforces.com/contest/29/problem/C)
* [Codeforces - Ant on the Tree](http://codeforces.com/contest/29/problem/D)
* [SPOJ - Cactus](http://www.spoj.com/problems/CAC/)
* [SPOJ - Mixing Chemicals](http://www.spoj.com/problems/AMR10J/)