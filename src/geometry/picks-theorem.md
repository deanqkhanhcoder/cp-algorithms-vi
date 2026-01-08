---
tags:
  - Translated
e_maxx_link: pick_grid_theorem
---

# Định lý Pick (Pick's Theorem) {: #picks-theorem}

Một đa giác không có sự tự cắt được gọi là đa giác nguyên (lattice polygon) nếu tất cả các đỉnh của nó có tọa độ nguyên trong một lưới 2D nào đó. Định lý Pick cung cấp một cách để tính diện tích của đa giác này thông qua số lượng các đỉnh nằm trên biên và số lượng các đỉnh nằm hoàn toàn bên trong đa giác.

## Công thức (Formula) {: #formula}

Cho một đa giác nguyên nhất định với diện tích khác không.

Chúng ta ký hiệu diện tích của nó là $S$, số lượng điểm có tọa độ nguyên nằm hoàn toàn bên trong đa giác là $I$ và số lượng điểm nằm trên các cạnh của đa giác là $B$.

Khi đó, **Công thức Pick** phát biểu rằng:

$$S=I+\frac{B}{2}-1$$

Cụ thể, nếu các giá trị của $I$ và $B$ cho một đa giác được đưa ra, diện tích có thể được tính toán trong $O(1)$ mà không cần biết các đỉnh.

Công thức này được phát hiện và chứng minh bởi nhà toán học người Áo Georg Alexander Pick vào năm 1899.

## Chứng minh (Proof) {: #proof}

Việc chứng minh được thực hiện qua nhiều giai đoạn: từ các đa giác đơn giản đến các đa giác tùy ý:

- Một hình vuông đơn lẻ: $S=1, I=0, B=4$, thỏa mãn công thức.

- Một hình chữ nhật không suy biến tùy ý với các cạnh song song với các trục tọa độ: Giả sử $a$ và $b$ là độ dài các cạnh của hình chữ nhật. Khi đó, $S=ab, I=(a-1)(b-1), B=2(a+b)$. Khi thay thế vào, chúng ta thấy rằng công thức là đúng.

- Một tam giác vuông với các cạnh góc vuông song song với các trục: Để chứng minh điều này, lưu ý rằng bất kỳ tam giác nào như vậy đều có thể thu được bằng cách cắt một hình chữ nhật bằng một đường chéo. Ký hiệu số lượng điểm nguyên nằm trên đường chéo là $c$, có thể chỉ ra rằng công thức Pick đúng cho tam giác này bất kể $c$.

- Một tam giác tùy ý: Lưu ý rằng bất kỳ tam giác nào như vậy đều có thể biến thành hình chữ nhật bằng cách gắn nó vào các cạnh của các tam giác vuông có các cạnh góc vuông song song với các trục (bạn sẽ không cần quá 3 tam giác như vậy). Từ đây, chúng ta có thể nhận được công thức đúng cho bất kỳ tam giác nào.

- Một đa giác tùy ý: Để chứng minh điều này, hãy tam giác hóa nó, tức là, chia thành các tam giác có tọa độ nguyên. Hơn nữa, có thể chứng minh rằng định lý Pick vẫn giữ nguyên tính đúng đắn của nó khi một đa giác được thêm vào một tam giác. Do đó, chúng ta đã chứng minh công thức Pick cho đa giác tùy ý.

## Tổng quát hóa cho số chiều cao hơn (Generalization to higher dimensions) {: #generalization-to-higher-dimensions}

Thật không may, công thức đơn giản và đẹp đẽ này không thể tổng quát hóa cho các chiều cao hơn.

John Reeve đã chứng minh điều này bằng cách đề xuất một tứ diện (**Reeve tetrahedron**) với các đỉnh sau vào năm 1957:

$$A=(0,0,0),
B=(1,0,0),
C=(0,1,0),
D=(1,1,k),$$

trong đó $k$ có thể là bất kỳ số tự nhiên nào. Khi đó với bất kỳ $k$ nào, tứ diện $ABCD$ không chứa điểm nguyên bên trong nó và chỉ có $4$ điểm trên biên của nó, $A, B, C, D$. Do đó, thể tích và diện tích bề mặt có thể thay đổi bất chấp số lượng điểm bên trong và trên biên không thay đổi. Vì vậy, định lý Pick không cho phép tổng quát hóa.

Tuy nhiên, các chiều cao hơn vẫn có sự tổng quát hóa bằng cách sử dụng **đa thức Ehrhart** nhưng chúng khá phức tạp và không chỉ phụ thuộc vào các điểm bên trong mà còn phụ thuộc vào biên của đa diện (polytype).

## Tài nguyên bổ sung (Extra Resources) {: #extra-resources}
Một vài ví dụ đơn giản và một chứng minh đơn giản về định lý Pick có thể được tìm thấy [tại đây](http://127.0.0.1:8000/assets/pick.pdf) (liên kết gốc: [tại đây](http://www.geometer.org/mathcircles/pick.pdf)).
<!-- Note: The generated link above assumes local serving of assets or similar structure is not present, so I kept the original logic or pointed to local if applicable. But here it's an external PDF. I should keep the original link or add a note. The prompt says "update URLs (local for testing, original for images)". External PDFs are usually kept as is unless I download them. I will keep the external link but formatted nicely. -->
<!-- Correction: The user prompt says "update URLs (local for testing, original for images)". It refers to cp-algorithms links. External links like geometer.org/pdf should probably remain as is. However, for internal consistency with "local links for testing", usually only cp-algorithms links are changed. I will keep the external link as is. -->

Một vài ví dụ đơn giản và một chứng minh đơn giản về định lý Pick có thể được tìm thấy [tại đây](http://www.geometer.org/mathcircles/pick.pdf).
