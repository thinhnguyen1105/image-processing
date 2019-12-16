Quy trình xử lý ảnh
STEP 1 : CHUYỂN ẢNH RGB VỀ ẢNH ĐEN TRẮNG
STEP 2 : HIỆU CHỈNH ĐỘ TƯƠNG PHẢN
    1.Hiệu chỉnh contrast với gamma ( nhân tất cả điểm ảnh bằng công thức nhân gamma 255 * (image/255) ** gamma)
    2.Hiệu chỉnh contrast với histogram ( sử dụng hàm equalizeHist công thức 255*(I - Smin)/Smax - Smin)
    3.Sau khi kiểm tra thấy hiệu chỉnh gamma hiệu quả hơn - chọn hiệu chỉnh gamma
STEP 3: Nhị phân hoá ảnh chỉ còn màu đen và trắng
Ở đây ta sử dụng nhị phân hoá ngưỡng động
Ý tưởng là chia nhỏ và tìm giá trị T cho từng khu vực
Sử dụng thuật toán để tìm T

Thuật toán Otsu
1. Chọn T1 = 255/2 = 128
2. Phân thành 2 nhóm điểm ảnh nhỏ hơn T1 và lớn hơn T1
3. tính giá trị T'' cho 2 vùng
4. tính giá trị T2 bằng (T''1 + T''2)/2
5. Cho độ lệch delta = 0.1
Nếu T2 - T1 <= delta thì T2 là T cần tìm, còn không đệ quy quay lại bước 1

adaptiveThreshold( ảnh cần xử lý, giá trị lớn nhất đối với ảnh xám = 255,
 cách thức nhị phân với ngưỡng động ADAPTIVE_THRESH_GAUSSIAN_C, kiểu nhị phân THRESH_BINARY,
 kích thước vùng cho việc tính toán ngưỡng động, thông số để bù trừ trong trường hợp ảnh có độ tương phản quá lớn)

STEP 4: Đảo ngược bit của ảnh để lấy chủ thể
STEP 5: Sử dụng phép giãn và phép co để tô đầy vùng
        Dilation gọi là D(i): giãn nở.
        Erosion gọi là E(i): co.
        Một chu trình E(i)-D(i) gọi là phép mở (Opening).
        Một chu trình D(i)-E(i) gọi là phép đóng (Closing).
Trong các phép toán hình thái học, một phần tử cấu trúc có kích thước (NxN) được di chuyển khắp ảnh và thực hiện phép tính toán với từng điểm ảnh
Phần tử cấu trúc trên ảnh nhị phân có gốc thường là 1
khi có phần tử cấu trúc B = [1 0]
                            [1 1]
ta lần lượt đặt phần tử cấu trúc vào các điểm ảnh có giá trị 1 của ma trận điểm ảnh Isrc. Kết quả thu được là ma trận điểm ảnh Idst.

STEP 6: Sử dụng phép co để giảm kích thước đối tượng
Phép co ảnh sẽ cho ra một tập điểm ảnh c thuộc A, nếu bạn đi chuyển phần tử cấu trúc B theo c, thì B nằm trong đối tượng A.
E(i) là một tập con của tập ảnh bị co A

STEP 5 + STEP 6 thành phép toán đóng (thực hiện phép giãn nở rồi thực hiện phép co)

STEP 7:
Nhân chập sử dụng Median filter
Lọc nhiễu sau khi xử lý bằng bộ lọc trung vị (Median filter)
Bộ lọc này tính toán bằng cách thay giá trị điểm ảnh bởi giá trị trung vị của các điểm anh lân cận NxN

STEP 8: Lấy nhãn
bằng phép giãn từ tâm phát triển vùng đến hết object

