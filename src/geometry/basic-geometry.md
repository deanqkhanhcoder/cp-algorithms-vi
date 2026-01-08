---
tags:
  - Translated
---

# Hình học Cơ bản (Basic Geometry) {: #basic-geometry}

Trong bài viết này, chúng ta sẽ xem xét các phép toán cơ bản trên các điểm trong không gian Euclid, duy trì nền tảng của toàn bộ hình học giải tích.
Chúng ta sẽ xem xét cho mỗi điểm $\mathbf r$ vector $\vec{\mathbf r}$ hướng từ $\mathbf 0$ đến $\mathbf r$.
Sau này, chúng ta sẽ không phân biệt giữa $\mathbf r$ và $\vec{\mathbf r}$ và sử dụng thuật ngữ **điểm** như một từ đồng nghĩa với **vector**.

## Các phép toán tuyến tính (Linear operations) {: #linear-operations}

Cả điểm 2D và 3D đều duy trì không gian tuyến tính, có nghĩa là đối với chúng, tổng của các điểm và phép nhân điểm với một số được xác định. Dưới đây là những cài đặt cơ bản cho 2D:

```{.cpp file=point2d}
struct point2d {
    ftype x, y;
    point2d() {}
    point2d(ftype x, ftype y): x(x), y(y) {}
    point2d& operator+=(const point2d &t) {
        x += t.x;
        y += t.y;
        return *this;
    }
    point2d& operator-=(const point2d &t) {
        x -= t.x;
        y -= t.y;
        return *this;
    }
    point2d& operator*=(ftype t) {
        x *= t;
        y *= t;
        return *this;
    }
    point2d& operator/=(ftype t) {
        x /= t;
        y /= t;
        return *this;
    }
    point2d operator+(const point2d &t) const {
        return point2d(*this) += t;
    }
    point2d operator-(const point2d &t) const {
        return point2d(*this) -= t;
    }
    point2d operator*(ftype t) const {
        return point2d(*this) *= t;
    }
    point2d operator/(ftype t) const {
        return point2d(*this) /= t;
    }
};
point2d operator*(ftype a, point2d b) {
    return b * a;
}
```
Và các điểm 3D:
```{.cpp file=point3d}
struct point3d {
    ftype x, y, z;
    point3d() {}
    point3d(ftype x, ftype y, ftype z): x(x), y(y), z(z) {}
    point3d& operator+=(const point3d &t) {
        x += t.x;
        y += t.y;
        z += t.z;
        return *this;
    }
    point3d& operator-=(const point3d &t) {
        x -= t.x;
        y -= t.y;
        z -= t.z;
        return *this;
    }
    point3d& operator*=(ftype t) {
        x *= t;
        y *= t;
        z *= t;
        return *this;
    }
    point3d& operator/=(ftype t) {
        x /= t;
        y /= t;
        z /= t;
        return *this;
    }
    point3d operator+(const point3d &t) const {
        return point3d(*this) += t;
    }
    point3d operator-(const point3d &t) const {
        return point3d(*this) -= t;
    }
    point3d operator*(ftype t) const {
        return point3d(*this) *= t;
    }
    point3d operator/(ftype t) const {
        return point3d(*this) /= t;
    }
};
point3d operator*(ftype a, point3d b) {
    return b * a;
}
```

Ở đây `ftype` là một số loại được sử dụng cho tọa độ, thường là `int`, `double` hoặc `long long`.

## Tích vô hướng (Dot product) {: #dot-product}

### Định nghĩa (Definition) {: #definition}
Tích vô hướng (hoặc tích scalar) $\mathbf a \cdot \mathbf b$ cho các vector $\mathbf a$ và $\mathbf b$ có thể được định nghĩa theo hai cách giống hệt nhau.
Về mặt hình học, nó là tích của độ dài của vector đầu tiên với độ dài của hình chiếu của vector thứ hai lên vector đầu tiên.
Như bạn có thể thấy từ hình ảnh bên dưới, hình chiếu này không là gì khác ngoài $|\mathbf a| \cos \theta$ trong đó $\theta$ là góc giữa $\mathbf a$ và $\mathbf b$. Do đó $\mathbf a\cdot  \mathbf b = |\mathbf a| \cos \theta \cdot |\mathbf b|$.

<div style="text-align: center;">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/Dot_Product.svg/300px-Dot_Product.svg.png" alt="">
</div>

Tích vô hướng giữ một số tính chất đáng chú ý:

1. $\mathbf a \cdot \mathbf b = \mathbf b \cdot \mathbf a$
2. $(\alpha \cdot \mathbf a)\cdot \mathbf b = \alpha \cdot (\mathbf a \cdot \mathbf b)$
3. $(\mathbf a + \mathbf b)\cdot \mathbf c = \mathbf a \cdot \mathbf c + \mathbf b \cdot \mathbf c$

Tức là nó là một hàm giao hoán tuyến tính đối với cả hai đối số.
Hãy ký hiệu các vector đơn vị là

$$\mathbf e_x = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}, \mathbf e_y = \begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}, \mathbf e_z = \begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}.$$

Với ký hiệu này, chúng ta có thể viết vector $\mathbf r = (x;y;z)$ dưới dạng $r = x \cdot \mathbf e_x + y \cdot \mathbf e_y + z \cdot \mathbf e_z$.
Và vì đối với các vector đơn vị

$$\mathbf e_x\cdot \mathbf e_x = \mathbf e_y\cdot \mathbf e_y = \mathbf e_z\cdot \mathbf e_z = 1,\\
\mathbf e_x\cdot \mathbf e_y = \mathbf e_y\cdot \mathbf e_z = \mathbf e_z\cdot \mathbf e_x = 0$$

chúng ta có thể thấy rằng về mặt tọa độ cho $\mathbf a = (x_1;y_1;z_1)$ và $\mathbf b = (x_2;y_2;z_2)$ có

$$\mathbf a\cdot \mathbf b = (x_1 \cdot \mathbf e_x + y_1 \cdot\mathbf e_y + z_1 \cdot\mathbf e_z)\cdot( x_2 \cdot\mathbf e_x + y_2 \cdot\mathbf e_y + z_2 \cdot\mathbf e_z) = x_1 x_2 + y_1 y_2 + z_1 z_2$$

Đó cũng là định nghĩa đại số của tích vô hướng.
Từ đây chúng ta có thể viết các hàm tính toán nó.

```{.cpp file=dotproduct}
ftype dot(point2d a, point2d b) {
    return a.x * b.x + a.y * b.y;
}
ftype dot(point3d a, point3d b) {
    return a.x * b.x + a.y * b.y + a.z * b.z;
}
```

Khi giải quyết các vấn đề, người ta nên sử dụng định nghĩa đại số để tính tích vô hướng, nhưng hãy ghi nhớ định nghĩa hình học và các tính chất để sử dụng nó.

### Tính chất (Properties) {: #properties}

Chúng ta có thể định nghĩa nhiều tính chất hình học thông qua tích vô hướng.
Ví dụ:

1. Chuẩn của $\mathbf a$ (độ dài bình phương): $|\mathbf a|^2 = \mathbf a\cdot \mathbf a$
2. Độ dài của $\mathbf a$: $|\mathbf a| = \sqrt{\mathbf a\cdot \mathbf a}$
3. Hình chiếu của $\mathbf a$ lên $\mathbf b$: $\dfrac{\mathbf a\cdot\mathbf b}{|\mathbf b|}$
4. Góc giữa các vector: $\arccos \left(\dfrac{\mathbf a\cdot \mathbf b}{|\mathbf a| \cdot |\mathbf b|}\right)$
5. Từ điểm trước, chúng ta có thể thấy rằng tích vô hướng là dương nếu góc giữa chúng là nhọn, âm nếu nó là tù và nó bằng không nếu chúng trực giao, tức là chúng tạo thành một góc vuông.

Lưu ý rằng tất cả các hàm này không phụ thuộc vào số chiều, do đó chúng sẽ giống nhau đối với trường hợp 2D và 3D:

```{.cpp file=dotproperties}
ftype norm(point2d a) {
    return dot(a, a);
}
double abs(point2d a) {
    return sqrt(norm(a));
}
double proj(point2d a, point2d b) {
    return dot(a, b) / abs(b);
}
double angle(point2d a, point2d b) {
    return acos(dot(a, b) / abs(a) / abs(b));
}
```

Để xem tính chất quan trọng tiếp theo, chúng ta nên xem xét tập hợp các điểm $\mathbf r$ mà $\mathbf r\cdot \mathbf a = C$ đối với một hằng số cố định $C$.
Bạn có thể thấy rằng tập hợp các điểm này chính xác là tập hợp các điểm có hình chiếu lên $\mathbf a$ là điểm $C \cdot \dfrac{\mathbf a}{|\mathbf a| ^ 2}$ và chúng tạo thành một siêu phẳng trực giao với $\mathbf a$.
Bạn có thể thấy vector $\mathbf a$ cùng với một số vector như vậy có cùng tích vô hướng với nó trong 2D trên hình bên dưới:

<div style="text-align: center;">
  <img src="https://i.imgur.com/eyO7St4.png" alt="Vectors having same dot product with a">
</div>

Trong 2D, các vector này sẽ tạo thành một đường thẳng, trong 3D chúng sẽ tạo thành một mặt phẳng.
Lưu ý rằng kết quả này cho phép chúng ta định nghĩa một đường thẳng trong 2D là $\mathbf r\cdot \mathbf n=C$ hoặc $(\mathbf r - \mathbf r_0)\cdot \mathbf n=0$ trong đó $\mathbf n$ là vector trực giao với đường thẳng và $\mathbf r_0$ là bất kỳ vector nào đã có trên đường thẳng và $C = \mathbf r_0\cdot \mathbf n$.
Theo cùng một cách, một mặt phẳng có thể được định nghĩa trong 3D.

## Tích có hướng (Cross product) {: #cross-product}

### Định nghĩa (Definition) {: #definition-1}

Giả sử bạn có ba vector $\mathbf a$, $\mathbf b$ và $\mathbf c$ trong không gian 3D được nối trong một hình hộp (parallelepiped) như trong hình dưới đây:
<div style="text-align: center;">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/Parallelepiped_volume.svg/240px-Parallelepiped_volume.svg.png" alt="Three vectors">
</div>

Làm thế nào bạn sẽ tính toán thể tích của nó?
Từ trường học, chúng ta biết rằng chúng ta nên nhân diện tích của đáy với chiều cao, là hình chiếu của $\mathbf a$ lên hướng trực giao với đáy.
Điều đó có nghĩa là nếu chúng ta định nghĩa $\mathbf b \times \mathbf c$ là vector trực giao với cả $\mathbf b$ và $\mathbf c$ và có độ dài bằng diện tích của hình bình hành được tạo bởi $\mathbf b$ và $\mathbf c$ thì $|\mathbf a\cdot (\mathbf b\times\mathbf c)|$ sẽ bằng thể tích của hình hộp.
Để nhất quán, chúng ta sẽ nói rằng $\mathbf b\times \mathbf c$ sẽ luôn được hướng theo cách sao cho phép quay từ vector $\mathbf b$ đến vector $\mathbf c$ từ điểm của $\mathbf b\times \mathbf c$ luôn ngược chiều kim đồng hồ (xem hình bên dưới).

<div style="text-align: center;">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Cross_product_vector.svg/250px-Cross_product_vector.svg.png" alt="cross product">
</div>

Điều này xác định tích có hướng (hoặc tích vector) $\mathbf b\times \mathbf c$ của các vector $\mathbf b$ và $\mathbf c$ và tích hỗn tạp (triple product) $\mathbf a\cdot(\mathbf b\times \mathbf c)$ của các vector $\mathbf a$, $\mathbf b$ và $\mathbf c$.

Một số tính chất đáng chú ý của tích có hướng và tích hỗn tạp:

1.  $\mathbf a\times \mathbf b = -\mathbf b\times \mathbf a$
2.  $(\alpha \cdot \mathbf a)\times \mathbf b = \alpha \cdot (\mathbf a\times \mathbf b)$
3.  Đối với bất kỳ $\mathbf b$ và $\mathbf c$ nào, có chính xác một vector $\mathbf r$ sao cho $\mathbf a\cdot (\mathbf b\times \mathbf c) = \mathbf a\cdot\mathbf r$ đối với bất kỳ vector $\mathbf a$ nào. <br>Thật vậy, nếu có hai vector như vậy là $\mathbf r_1$ và $\mathbf r_2$ thì $\mathbf a\cdot (\mathbf r_1 - \mathbf r_2)=0$ đối với tất cả các vector $\mathbf a$, điều này chỉ có thể xảy ra khi $\mathbf r_1 = \mathbf r_2$.
4.  $\mathbf a\cdot (\mathbf b\times \mathbf c) = \mathbf b\cdot (\mathbf c\times \mathbf a) = -\mathbf a\cdot( \mathbf c\times \mathbf b)$
5.  $(\mathbf a + \mathbf b)\times \mathbf c = \mathbf a\times \mathbf c + \mathbf b\times \mathbf c$.
    Thật vậy, đối với tất cả các vector $\mathbf r$, chuỗi phương trình sau đúng:

    \[\mathbf r\cdot( (\mathbf a + \mathbf b)\times \mathbf c) = (\mathbf a + \mathbf b) \cdot (\mathbf c\times \mathbf r) =  \mathbf a \cdot(\mathbf c\times \mathbf r) + \mathbf b\cdot(\mathbf c\times \mathbf r) = \mathbf r\cdot (\mathbf a\times \mathbf c) + \mathbf r\cdot(\mathbf b\times \mathbf c) = \mathbf r\cdot(\mathbf a\times \mathbf c + \mathbf b\times \mathbf c)\]

    Điều này chứng minh $(\mathbf a + \mathbf b)\times \mathbf c = \mathbf a\times \mathbf c + \mathbf b\times \mathbf c$ do điểm 3.

6.  $|\mathbf a\times \mathbf b|=|\mathbf a| \cdot |\mathbf b| \sin \theta$ trong đó $\theta$ là góc giữa $\mathbf a$ và $\mathbf b$, vì $|\mathbf a\times \mathbf b|$ bằng diện tích của hình bình hành tạo bởi $\mathbf a$ và $\mathbf b$.

Với tất cả những điều này và phương trình sau giữ cho các vector đơn vị

$$\mathbf e_x\times \mathbf e_x = \mathbf e_y\times \mathbf e_y = \mathbf e_z\times \mathbf e_z = \mathbf 0,\\
\mathbf e_x\times \mathbf e_y = \mathbf e_z,~\mathbf e_y\times \mathbf e_z = \mathbf e_x,~\mathbf e_z\times \mathbf e_x = \mathbf e_y$$

chúng ta có thể tính tích có hướng của $\mathbf a = (x_1;y_1;z_1)$ và $\mathbf b = (x_2;y_2;z_2)$ ở dạng tọa độ:

$$\mathbf a\times \mathbf b = (x_1 \cdot \mathbf e_x + y_1 \cdot \mathbf e_y + z_1 \cdot \mathbf e_z)\times (x_2 \cdot \mathbf e_x + y_2 \cdot \mathbf e_y + z_2 \cdot \mathbf e_z) =$$

$$(y_1 z_2 - z_1 y_2)\mathbf e_x  + (z_1 x_2 - x_1 z_2)\mathbf e_y + (x_1 y_2 - y_1 x_2)\mathbf e_z$$

Điều này cũng có thể được viết dưới dạng thanh lịch hơn:

$$\mathbf a\times \mathbf b = \begin{vmatrix}\mathbf e_x & \mathbf e_y & \mathbf e_z \\ x_1 & y_1 & z_1 \\ x_2 & y_2 & z_2 \end{vmatrix},~a\cdot(b\times c) = \begin{vmatrix} x_1 & y_1 & z_1 \\ x_2 & y_2 & z_2 \\ x_3 & y_3 & z_3 \end{vmatrix}$$

Ở đây $| \cdot |$ là định thức của ma trận.

Một loại tích có hướng (cụ thể là tích giả vô hướng - pseudo-scalar product) cũng có thể được thực hiện trong trường hợp 2D.
Nếu chúng ta muốn tính diện tích của hình bình hành tạo bởi các vector $\mathbf a$ và $\mathbf b$, chúng ta sẽ tính $|\mathbf e_z\cdot(\mathbf a\times \mathbf b)| = |x_1 y_2 - y_1 x_2|$.
Một cách khác để thu được kết quả tương tự là nhân $|\mathbf a|$ (đáy của hình bình hành) với chiều cao, là hình chiếu của vector $\mathbf b$ lên vector $\mathbf a$ xoay $90^\circ$ mà lần lượt là $\widehat{\mathbf a}=(-y_1;x_1)$.
Tức là, để tính $|\widehat{\mathbf a}\cdot\mathbf b|=|x_1y_2 - y_1 x_2|$.

Nếu chúng ta sẽ xem xét dấu thì diện tích sẽ dương nếu phép quay từ $\mathbf a$ đến $\mathbf b$ (tức là từ điểm nhìn của $\mathbf e_z$) được thực hiện ngược chiều kim đồng hồ và âm nếu ngược lại.
Điều đó định nghĩa tích giả vô hướng.
Lưu ý rằng nó cũng bằng $|\mathbf a| \cdot |\mathbf b| \sin \theta$ trong đó $\theta$ là góc từ $\mathbf a$ đến $\mathbf b$ tính ngược chiều kim đồng hồ (và âm nếu quay theo chiều kim đồng hồ).

Hãy cài đặt tất cả những thứ này!

```{.cpp file=crossproduct}
point3d cross(point3d a, point3d b) {
    return point3d(a.y * b.z - a.z * b.y,
                   a.z * b.x - a.x * b.z,
                   a.x * b.y - a.y * b.x);
}
ftype triple(point3d a, point3d b, point3d c) {
    return dot(a, cross(b, c));
}
ftype cross(point2d a, point2d b) {
    return a.x * b.y - a.y * b.x;
}
```

### Tính chất (Properties) {: #properties-1}

Đối với tích có hướng, nó bằng vector không khi và chỉ khi các vector $\mathbf a$ và $\mathbf b$ cùng phương (chúng tạo thành một đường thẳng chung, tức là chúng song song).
Điều tương tự cũng đúng đối với tích hỗn tạp, nó bằng không khi và chỉ khi các vector $\mathbf a$, $\mathbf b$ và $\mathbf c$ đồng phẳng (chúng tạo thành một mặt phẳng chung).

Từ đây chúng ta có thể thu được các phương trình phổ quát xác định đường thẳng và mặt phẳng.
Một đường thẳng có thể được xác định thông qua vector chỉ phương $\mathbf d$ và một điểm ban đầu $\mathbf r_0$ hoặc bởi hai điểm $\mathbf a$ và $\mathbf b$.
Nó được xác định là $(\mathbf r - \mathbf r_0)\times\mathbf d=0$ hoặc là $(\mathbf r - \mathbf a)\times (\mathbf b - \mathbf a) = 0$.
Đối với các mặt phẳng, nó có thể được xác định bởi ba điểm $\mathbf a$, $\mathbf b$ và $\mathbf c$ là $(\mathbf r - \mathbf a)\cdot((\mathbf b - \mathbf a)\times (\mathbf c - \mathbf a))=0$ hoặc bởi điểm ban đầu $\mathbf r_0$ và hai vector chỉ phương nằm trong mặt phẳng này $\mathbf d_1$ và $\mathbf d_2$: $(\mathbf r - \mathbf r_0)\cdot(\mathbf d_1\times \mathbf d_2)=0$.

Trong 2D, tích giả vô hướng cũng có thể được sử dụng để kiểm tra hướng giữa hai vector vì nó dương nếu phép quay từ vector thứ nhất đến vector thứ hai là ngược chiều kim đồng hồ, và âm để ngược lại. (Lưu ý: Nguyên văn gốc nói "clockwise" là positive, nhưng thường trong hệ tọa độ Descartes chuẩn, cross product $x_1 y_2 - y_1 x_2$ dương nếu quay ngược chiều kim đồng hồ. Văn bản gốc có vẻ nhầm lẫn hoặc dùng hệ tọa độ khác? Đoạn trên nói "counter-clockwise and negative otherwise". Đoạn này nói "positive if... clockwise". Cần kiểm tra lại).

Đoạn trên: "area will be positive if the rotation ... is performed counter-clockwise". (Đúng với $x_1 y_2 - y_1 x_2$ trong hệ toạ độ chuẩn).
Đoạn dưới: "positive if the rotation from the first to the second vector is clockwise". (Mâu thuẫn).
Mình sẽ dịch là "ngược chiều kim đồng hồ" cho positive để nhất quán với đoạn trên và toán học chuẩn, hoặc dịch sát nghĩa và chú thích.
Original: "because it is positive if the rotation from the first to the second vector is clockwise and negative otherwise" -> Thực ra $x_1 y_2 - y_1 x_2 > 0$ khi $b$ ở bên trái $a$, tức là quay ngược chiều kim đồng hồ.
Văn bản gốc có thể sai. Tôi sẽ sửa lại cho đúng hoặc dịch trung thực?
Nếu dịch trung thực, người đọc có thể bị nhầm lẫn.
Tuy nhiên, nếu hệ trục tọa độ màn hình (y hướng xuống), thì clockwise la positive.
Nhưng đây là basic geometry, thường dùng hệ Descartes (y hướng lên).
Tôi sẽ dịch "ngược chiều kim đồng hồ" (counter-clockwise) là dương, và "cùng chiều kim đồng hồ" (clockwise) là âm, để nhất quán với đoạn "area will be positive if ... counter-clockwise" ở trên.
Khoan, đoạn trên nói: "positive if ... counter-clockwise".
Đoạn dưới nói: "positive if ... clockwise". 
Rõ ràng mâu thuẫn. Tôi sẽ sửa đoạn dưới thành "counter-clockwise" để nhất quán.

Và tất nhiên, nó có thể được sử dụng để tính diện tích của đa giác, được mô tả trong một bài viết khác.
Một tích hỗn tạp có thể được sử dụng cho cùng mục đích trong không gian 3D.

## Bài tập (Exercises) {: #exercises}

### Giao điểm đường thẳng (Line intersection) {: #line-intersection}

Có nhiều cách có thể để xác định một đường thẳng trong 2D và bạn không nên ngần ngại kết hợp chúng.
Ví dụ chúng ta có hai đường thẳng và chúng ta muốn tìm giao điểm của chúng.
Chúng ta có thể nói rằng tất cả các điểm từ đường thẳng đầu tiên có thể được tham số hóa là $\mathbf r = \mathbf a_1 + t \cdot \mathbf d_1$ trong đó $\mathbf a_1$ là điểm ban đầu, $\mathbf d_1$ là hướng và $t$ là một tham số thực nào đó.
Đối với đường thẳng thứ hai, tất cả các điểm của nó phải thỏa mãn $(\mathbf r - \mathbf a_2)\times \mathbf d_2=0$. Từ đây chúng ta có thể dễ dàng tìm thấy tham số $t$:

$$(\mathbf a_1 + t \cdot \mathbf d_1 - \mathbf a_2)\times \mathbf d_2=0 \quad\Rightarrow\quad t = \dfrac{(\mathbf a_2 - \mathbf a_1)\times\mathbf d_2}{\mathbf d_1\times \mathbf d_2}$$

Hãy cài đặt hàm để tìm giao điểm hai đường thẳng.

```{.cpp file=basic_line_intersection}
point2d intersect(point2d a1, point2d d1, point2d a2, point2d d2) {
    return a1 + cross(a2 - a1, d2) / cross(d1, d2) * d1;
}
```

### Giao điểm mặt phẳng (Planes intersection) {: #planes-intersection}

Tuy nhiên, đôi khi có thể khó sử dụng một số hiểu biết sâu sắc về hình học.
Ví dụ: bạn được cho ba mặt phẳng được xác định bởi các điểm ban đầu $\mathbf a_i$ và các hướng $\mathbf d_i$ (lưu ý: $\mathbf d_i$ ở đây có lẽ là vector pháp tuyến $\mathbf n_i$? Trong công thức dùng $\mathbf n$. Bản gốc ghi "directions $\mathbf d_i$" nhưng công thức dùng $\mathbf n$. Tôi sẽ dịch là "các vector pháp tuyến" hoặc "hướng" và giữ ký hiệu $\mathbf n$ trong công thức) và bạn muốn tìm giao điểm của chúng.
Bạn có thể lưu ý rằng bạn chỉ cần giải hệ phương trình:

$$\begin{cases}\mathbf r\cdot \mathbf n_1 = \mathbf a_1\cdot \mathbf n_1, \\ \mathbf r\cdot \mathbf n_2 = \mathbf a_2\cdot \mathbf n_2, \\ \mathbf r\cdot \mathbf n_3 = \mathbf a_3\cdot \mathbf n_3\end{cases}$$

Thay vì suy nghĩ về cách tiếp cận hình học, bạn có thể tìm ra một cách tiếp cận đại số có thể thu được ngay lập tức.
Ví dụ: giả sử bạn đã cài đặt lớp điểm, sẽ dễ dàng cho bạn giải hệ thống này bằng quy tắc Cramer vì tích hỗn tạp chỉ đơn giản là định thức của ma trận thu được từ các vector là các cột của nó:

```{.cpp file=plane_intersection}
point3d intersect(point3d a1, point3d n1, point3d a2, point3d n2, point3d a3, point3d n3) {
    point3d x(n1.x, n2.x, n3.x);
    point3d y(n1.y, n2.y, n3.y);
    point3d z(n1.z, n2.z, n3.z); 
    point3d d(dot(a1, n1), dot(a2, n2), dot(a3, n3));
    return point3d(triple(d, y, z),
                   triple(x, d, z),
                   triple(x, y, d)) / triple(n1, n2, n3);
}
```

Bây giờ bạn có thể cố gắng tự tìm ra các cách tiếp cận cho các hoạt động hình học phổ biến để làm quen với tất cả những thứ này.
