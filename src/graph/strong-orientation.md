---
tags:
  - Translated
e_maxx_link: strong_orientation
---

# Định hướng mạnh (Strong Orientation) {: #strong-orientation}

Một **định hướng mạnh** của một đồ thị vô hướng là một phép gán hướng cho mỗi cạnh sao cho nó trở thành một [đồ thị liên thông mạnh](strongly-connected-components.md).
Nghĩa là, sau khi *định hướng* chúng ta có thể thăm bất kỳ đỉnh nào từ bất kỳ đỉnh nào bằng cách đi theo các cạnh có hướng.

## Giải pháp (Solution) {: #solution}

Tất nhiên, điều này không thể thực hiện được với *mọi* đồ thị.
Hãy xem xét một [cầu (bridge)](bridge-searching.md) trong một đồ thị.
Chúng ta phải gán một hướng cho nó và bằng cách làm như vậy, chúng ta làm cho cầu này chỉ có thể "đi qua" theo một hướng. Điều đó có nghĩa là chúng ta không thể đi từ một đầu của cầu đến đầu kia, vì vậy chúng ta không thể làm cho đồ thị liên thông mạnh.

Bây giờ hãy xem xét một [DFS](depth-first-search.md) qua một đồ thị liên thông không có cầu.
Rõ ràng, chúng ta sẽ thăm mỗi đỉnh.
Và vì không có cầu, chúng ta có thể loại bỏ bất kỳ cạnh cây DFS nào và vẫn có thể đi từ bên dưới cạnh đến bên trên cạnh bằng cách sử dụng một đường đi chứa ít nhất một cạnh ngược.
Từ đó suy ra rằng từ bất kỳ đỉnh nào chúng ta có thể đi đến gốc của cây DFS.
Ngoài ra, từ gốc của cây DFS chúng ta có thể thăm bất kỳ đỉnh nào chúng ta chọn.
Chúng ta đã tìm thấy một định hướng mạnh!

Nói cách khác, để định hướng mạnh một đồ thị liên thông không có cầu, hãy chạy một DFS trên nó và để các cạnh cây DFS hướng ra xa khỏi gốc DFS và tất cả các cạnh khác từ hậu duệ đến tổ tiên trong cây DFS.

Kết quả cho thấy rằng các đồ thị liên thông không có cầu chính xác là các đồ thị có định hướng mạnh được gọi là **định lý Robbins**.

## Mở rộng bài toán (Problem extension) {: #problem-extension}

Hãy xem xét bài toán tìm định hướng đồ thị sao cho số lượng SCC là tối thiểu.

Tất nhiên, mỗi thành phần đồ thị có thể được xem xét riêng biệt.
Bây giờ, vì chỉ các đồ thị không có cầu mới có thể định hướng mạnh, hãy tạm thời loại bỏ tất cả các cầu.
Chúng ta kết thúc với một số lượng các thành phần không có cầu
(chính xác là *có bao nhiêu thành phần lúc đầu* + *có bao nhiêu cầu*)
 và chúng ta biết rằng chúng ta có thể định hướng mạnh mỗi thành phần đó.

Chúng ta chỉ được phép định hướng các cạnh, không được loại bỏ chúng, nhưng hóa ra chúng ta có thể định hướng các cầu một cách tùy ý.
Tất nhiên, cách dễ nhất để định hướng chúng là chạy thuật toán được mô tả ở trên mà không sửa đổi trên mỗi thành phần liên thông ban đầu.

### Cài đặt (Implementation) {: #implementation}

Ở đây, đầu vào là *n* — số lượng đỉnh, *m* — số lượng cạnh, sau đó *m* dòng mô tả các cạnh.

Đầu ra là số lượng tối thiểu các SCC trên dòng đầu tiên và trên dòng thứ hai là một chuỗi gồm *m* ký tự,
hoặc `>` — cho chúng ta biết rằng cạnh tương ứng từ đầu vào được định hướng từ đỉnh bên trái sang đỉnh bên phải (như trong đầu vào),
hoặc `<` — ngược lại.

Đây là một thuật toán tìm kiếm cầu được sửa đổi để cũng định hướng các cạnh,
bạn cũng có thể định hướng các cạnh như một bước đầu tiên và đếm các SCC trên đồ thị có hướng như một bước thứ hai.

```cpp
vector<vector<pair<int, int>>> adj; // adjacency list - vertex and edge pairs
vector<pair<int, int>> edges;

vector<int> tin, low;
int bridge_cnt;
string orient;
vector<bool> edge_used;
void find_bridges(int v) {
	static int time = 0;
	low[v] = tin[v] = time++;
	for (auto p : adj[v]) {
		if (edge_used[p.second]) continue;
		edge_used[p.second] = true;
		orient[p.second] = v == edges[p.second].first ? '>' : '<';
		int nv = p.first;
		if (tin[nv] == -1) { // if nv is not visited yet
			find_bridges(nv);
			low[v] = min(low[v], low[nv]);
			if (low[nv] > tin[v]) {
				// a bridge between v and nv
				bridge_cnt++;
			}
		} else {
			low[v] = min(low[v], tin[nv]);
		}
	}
}

int main() {
	int n, m;
	scanf("%d %d", &n, &m);
	adj.resize(n);
	tin.resize(n, -1);
	low.resize(n, -1);
	orient.resize(m);
	edges.resize(m);
	edge_used.resize(m);
	for (int i = 0; i < m; i++) {
		int a, b;
		scanf("%d %d", &a, &b);
		a--; b--;
		adj[a].push_back({b, i});
		adj[b].push_back({a, i});
		edges[i] = {a, b};
	}
	int comp_cnt = 0;
	for (int v = 0; v < n; v++) {
		if (tin[v] == -1) {
			comp_cnt++;
			find_bridges(v);
		}
	}
	printf("%d\n%s\n", comp_cnt + bridge_cnt, orient.c_str());
}
```

## Bài tập (Practice Problems) {: #practice-problems}

* [26th Polish OI - Osiedla](https://szkopul.edu.pl/problemset/problem/nldsb4EW1YuZykBlf4lcZL1Y/site/)
