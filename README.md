**TÓM TẮT LÝ THUYẾT XỬ LÝ ẢNH**
* CHƯƠNG 2
- Độ tương phản của ảnh được 
- Lược đồ ảnh
- Một số kĩ thuật cân bằng ảnh
- Các phép toán trên ảnh
- Nội suy ảnh

* CHƯƠNG 3
- Hạt nhân chập là một ma trận ( thường là số lẻ )
[https://www.pyimagesearch.com/2016/07/25/convolutions-with-opencv-and-python/][Lý thuyết nhân chập]

* CHƯƠNG 4
- Link tutorial
[https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_transforms/py_fourier_transform/py_fourier_transform.html][Fast Fourier Transform]
- Fast Fourier Transform
- Biến đổi số phức
- Một số ví dụ hàm FT cơ bản: Sinus, Gaussian, Square, Pulses
- Lọc thông thấp, thông cao và lọc nhiễu sin

* CHƯƠNG 5 Edges
- Biên là sự thay đổi đột ngột về cường độ sáng
- Có 3 loại biên: step(bậc thang), ramp(dốc), và roof (mái nhà)
- Phân biệt biên nhiễu ít và biên nhiễu nhiều
- Đạo hàm bậc 1 để tìm ra threshould (ngưỡng biên)

- Sử dụng mặt nạ nhân chập cho 2 hướng đạo hàm để phát hiện biên
Bộ lọc Roberts, prewitt, sobel phát hiện biên
- Image gradient: sử dụng magnitude

- Dùng đạo hàm bậc 2 phát hiện biên:
Laplacian

- Bộ lọc tối ưu - Canny
1. Áp dụng bộ lọc Gauss
2. Tính độ lớn gradient
3. Tính hướng gradient
4. Tính toán độ lớn gradient
5. Lấy ngưỡng cho biên

* CHƯƠNG 6 Phân vùng (Region Segmentation)
- Mục đích: để lấy ra vật thể một cách rõ ràng để cho các hoạt động sau
- Phân vùng dựa trên tính không liên tục và tính đồng nhất
- Các phương pháp tiếp cận :
 + Theo vùng
 + Theo biên
 + Tiếp cận lai (vùng và biên)
 
 - Lấy ngưỡng (Thresholding)
 + ngưỡng toàn cục: 1 ngưỡng cho toàn bộ bức ảnh
 + ngưỡng cục bộ: 1 ngưỡng cho 1 phần nào đó của bức ảnh
 + ngưỡng thích nghi: 1 ngưỡng được tinh chỉnh tuỳ theo mỗi ảnh hoặc mỗi phần trong ảnh
 + Ý tưởng: chia thành 2 lớp, lớn và nhỏ hơn ngưỡng
 + Cách chọn ngưỡng: 
 1. toàn cục: lấy giá trị trung bình
 2. Dựa trên histogram : số đỉnh là số lớp, phân chia thành nhiều phần và n ngưỡng sẽ chia ảnh thành n+1 lớp
 
 
Otsu Algorithm - ngưỡng toàn cục
Đối với ảnh gradient không sử dụng ngưỡng toàn cục được, vậy sử dụng ngưỡng thích nghi
Chia ảnh thành nhiều phần nhỏ và xử lý trên từng ảnh nhỏ vs ngưỡng riêng
- Chia ảnh
- Lựa chọn kích thước ảnh nhỏ
- Kiểm tra phương sai

K-means Algorithm
- Chia các điểm và K nhóm, định nghĩa tâm của mỗi nhóm = trung bình tất cả các pixels

Chia và hợp
- Chia các vùng không đồng nhất thành những vùng nhỏ 
- Hơp các vùng đồng nhất lân cận 

Ảnh có thể biểu diễn bằng 1 cây, chia nhánh đến khi không còn vùng không đồng nhất

Phát triển vùng
- Bắt đầu từ nhân và lan ra nếu đủ tiêu chí đồng nhất (phương sai nhỏ, độ xám dưới ngưỡng nào đó)

Watershed segmentation
Gestalt Approach


Chương 8 : Các bước xử lý ảnh 
Thay đổi độ phân giải của ảnh
Tiền xử lý : thay đổi độ sáng , không gian màu , lọc nhiễu, phóng to thu nhỏ để giảm điểm ảnh . . 
Phân vùng ảnh  

Sau khi phân vùng nếu chất lượng chưa tốt thì hậu xử lý ảnh 

Hậu xử lý: 
Bỏ bớt vùng thừa
C giãn đóng mở, đánh nhãn thành phần liên thông, đánh số thành phần liên thông suy ra số nhãn tiếp theo 
Tách từng vùng bằng mặt nạ nhị phân, 

Chương 9: Ảnh nhị phân (Bit 0-1)
Liên kết các pixel (nhóm 4 và nhóm 8)
Khoảng cách giữa 2 điểm
- Khoảng cách manhattan (Các điểm có cùng khoảng cách tạo thành hình kim cương với tâm ở giữa)
- Khoảng cách chesboard (tạo thành hình vuông tâm x,y)
- Mã hoá Freeman
Định nghĩa: mã hoá các đường biên (contours, edges, bắt đầu từ 1 điểm và theo chiều kim đồng hồ)

Cách gán nhãn các thành phần

*** BÀI TẬP: ĐẾM MỘT ẢNH ĐẦU VÀO CÓ BAO NHIÊU OBJECT 

*** BÀI TẬP: XỬ LÝ ẢNH NÂNG CAO - NHIỀU ẢNH KHÁC NHAU , THUẬT TOÁN KHÁC NHAU  ***