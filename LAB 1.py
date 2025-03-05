#bài1:Viết chương trình nhập vào số giờ làm mỗi tuần
Số_giờ_làm_việc = float(input("Nhập số giờ làm việc trong tuần: ")) #Kiểu dữ liệu float: giúp lấy cả phần thập phân, vì số giờ làm việc và lương theo giờ có thể không phải số nguyên.
Giá_theo_giờ = float(input("Nhập thù lao mỗi giờ làm tiêu chuẩn: "))

Giờ_tiêu_chuẩn = 40
Số_giờ_vượt_chuẩn = 1.5

if Số_giờ_làm_việc > Giờ_tiêu_chuẩn:
    Giờ_làm_thêm = Số_giờ_làm_việc - Giờ_tiêu_chuẩn
    Lương_chuẩn = (Giờ_tiêu_chuẩn * Giá_theo_giờ) + (Giờ_làm_thêm * Giá_theo_giờ * Số_giờ_vượt_chuẩn)
else:
    Lương_chuẩn = Số_giờ_làm_việc * Giá_theo_giờ

print(f"Số tiền thực lĩnh của nhân viên: {Lương_chuẩn:.2f} VND") # dùng để định dạng số khi in ra màn hình. f: Định dạng số kiểu float (số thực, có dấu thập phân)..2: Giới hạn 2 chữ số sau dấu thập phân.

# Bài 2: Viết chương trình nhập vào ngày tháng năm sinh sau đó tínhtuổi của người đó.
Ngày_sinh = int(input("Nhập ngày sinh: "))
Tháng_sinh = int(input("Nhập tháng sinh: "))
Năm_sinh = int(input("Nhập năm sinh: "))

Ngày_hiện_tại = int(input("Nhập ngày hiện tại: "))
Tháng_hiện_tại = int(input("Nhập tháng hiện tại: "))
Năm_hiện_tại = int(input("Nhập năm hiện tại: "))

Tuổi = Năm_hiện_tại - Năm_sinh

if (Tháng_hiện_tại < Tháng_sinh) or (Tháng_hiện_tại == Tháng_sinh and Ngày_hiện_tại < Ngày_sinh):
    Tuổi -= 1 # Kiểm tra nếu chưa qua sinh nhật trong năm nay thì trừ 1 tuổi

print(f"Tuổi của bạn là: {Tuổi} tuổi")

#bài3
# Khởi tạo danh sách rỗng
square_numbers = []

# Lặp qua các số từ 1 đến 9
for i in range(1, 10):
    square_numbers.append(i ** 2)  # Tính bình phương và thêm vào danh sách
    print(square_numbers)  # In danh sách sau mỗi lần thêm phần tử

#bài4: viết chương trình in ra bảng cửu chương
   # Duyệt qua từng số trong bảng cửu chương (từ 1 đến 9)
for i in range(1, 10):
    print(f"\nBảng cửu chương {i}:")  # In tiêu đề
    for j in range(1, 10):  
        print(f"{i} x {j} = {i * j}",end='\t')# In phép nhân
    print()  # Xuống dòng sau khi in hết 1 bảng cửu chương
        
#Bài 5: Viết một chương trình nhập vào một số từ tách biệt bởi khoảng trắng
# Nhập vào một chuỗi từ cách nhau bởi khoảng trắng
chuoi_nhap = input("Nhập các từ (cách nhau bởi khoảng trắng): ")

# Chuyển chuỗi thành danh sách từ
danh_sach_tu = chuoi_nhap.split()

# Loại bỏ từ trùng lặp bằng cách chuyển thành tập hợp, sau đó chuyển lại thành danh sách
danh_sach_tu = list(set(danh_sach_tu))

# Sắp xếp danh sách theo thứ tự bảng chữ cái
danh_sach_tu.sort()

# Chuyển các từ bắt đầu bằng 'A' hoặc 'a' thành chữ in hoa
danh_sach_tu = [tu.upper() if tu.lower().startswith('a') else tu for tu in danh_sach_tu]

# In kết quả
print("Kết quả sau khi xử lý:", " ".join(danh_sach_tu))

#bài 6
# Nhập chuỗi số nhị phân từ bàn phím, tách thành danh sách
chuoi_nhi_phan = input("Nhập các số nhị phân (phân tách bởi dấu phẩy): ").split(',')

# Danh sách lưu kết quả
ket_qua = []

# Duyệt qua từng số nhị phân trong danh sách
for so in chuoi_nhi_phan:
    # Chuyển số nhị phân sang thập phân
    gia_tri_thap_phan = int(so, 2)
    
    # Kiểm tra nếu chia hết cho 5
    if gia_tri_thap_phan % 5 == 0:
        ket_qua.append(so)

# In kết quả với dấu phẩy phân cách
print(",".join(ket_qua))

#bài7
import math

# Danh sách lưu các số thỏa mãn điều kiện
ket_qua = []

# Duyệt qua các số từ 100 đến 2000
for so in range(100, 2001):
    # Kiểm tra số chính phương
    can_bac_hai = math.sqrt(so)
    if can_bac_hai.is_integer():  # Nếu căn bậc hai là số nguyên
        # Kiểm tra số chữ số chẵn
        so_str = str(so)  # Chuyển số thành chuỗi để duyệt từng chữ số
        so_chu_so_chan = sum(1 for chu_so in so_str if int(chu_so) % 2 == 0)  # Đếm chữ số chẵn
        
        if so_chu_so_chan >= 2:  # Nếu có ít nhất 2 chữ số chẵn thì thêm vào danh sách
            ket_qua.append(str(so))

# In kết quả, các số cách nhau bởi dấu phẩy
print(",".join(ket_qua))

#bài 8 Viết một chương trình nhập vào một câu sau đó đếm xem có bao nhiêu chữ hoa, bao nhiêu chữ thường.
# Nhập câu từ bàn phím
cau = input("Nhập một câu: ")

# Biến đếm số chữ hoa và chữ thường
dem_hoa = 0
dem_thuong = 0

# Duyệt từng ký tự trong câu
for ky_tu in cau:
    if ky_tu.isupper():  # Kiểm tra chữ hoa
        dem_hoa += 1
    elif ky_tu.islower():  # Kiểm tra chữ thường
        dem_thuong += 1

# In kết quả
print(f"Số chữ hoa: {dem_hoa}")
print(f"Số chữ thường: {dem_thuong}")

 #bài 9
 # Nhập chuỗi từ người dùng
chuoi = input("Nhập chuỗi: ")

# Loại bỏ khoảng trắng thừa và chuẩn hóa chuỗi
chuoi_chuan_hoa = ' '.join(chuoi.split())  # Tách các từ, loại bỏ khoảng trắng dư thừa
chuoi_ket_qua = chuoi_chuan_hoa.title()  # Viết hoa chữ cái đầu mỗi từ

# In kết quả
print(f"Chuỗi sau khi định dạng: {chuoi_ket_qua}")

#bài 10
# Đọc file danh sách bài hát
with open("danhsach_baihat.txt", "r", encoding="utf-8") as file:
    danh_sach = file.readlines()

# Loại bỏ khoảng trắng thừa và loại bỏ trùng lặp bằng set
danh_sach_khong_trung = sorted(set(bai.strip() for bai in danh_sach))

# Ghi danh sách không trùng vào file mới
with open("danhsach_khong_trung.txt", "w", encoding="utf-8") as file_moi:
    for bai_hat in danh_sach_khong_trung:
        file_moi.write(bai_hat + "\n")

print("Đã tạo file mới chứa danh sách bài hát không trùng lặp.")

