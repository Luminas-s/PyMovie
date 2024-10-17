# from django.db import models

# # Bảng Rạp Chiếu (Cinema)
# class RapChieu(models.Model):
#     ten_rap = models.CharField(max_length=200)  # Tên rạp chiếu
#     dia_chi = models.CharField(max_length=255)  # Địa chỉ của rạp chiếu
#     so_dien_thoai = models.CharField(max_length=15)  # Số điện thoại liên hệ
#     email = models.EmailField()  # Email của rạp chiếu

#     def __str__(self):
#         return self.ten_rap

# # Bảng Định Dạng Phim (Film Format)
# class DinhDangPhim(models.Model):
#     ten_dinh_dang = models.CharField(max_length=50)

#     def __str__(self):
#         return self.ten_dinh_dang

# # Bảng Thể Loại (Genre)
# class TheLoai(models.Model):
#     ten_the_loai = models.CharField(max_length=100)

#     def __str__(self):
#         return self.ten_the_loai

# # Bảng Phim (Movie)
# class Phim(models.Model):
#     ten_phim = models.CharField(max_length=200)
#     the_loai = models.ManyToManyField(TheLoai)  # Một phim có thể thuộc nhiều thể loại
#     dao_dien = models.CharField(max_length=100)
#     dien_vien = models.TextField()
#     thoi_luong = models.PositiveIntegerField()  # Thời lượng tính bằng phút
#     tom_tat = models.TextField()
#     thumbnail = models.CharField(max_length=200)  # Link ảnh thumbnail của phim

#     def __str__(self):
#         return self.ten_phim

# # Bảng Xuất Chiếu (Showtimes)
# class XuatChieu(models.Model):
#     phim = models.ForeignKey(Phim, on_delete=models.CASCADE)
#     thoi_gian_chieu = models.DateTimeField()
#     rap_chieu = models.ForeignKey(RapChieu, on_delete=models.CASCADE)  # Liên kết đến bảng rạp chiếu
#     dinh_dang_phim = models.ForeignKey(DinhDangPhim, on_delete=models.CASCADE)  # Liên kết đến bảng định dạng phim

#     def __str__(self):
#         return f"{self.phim.ten_phim} - {self.thoi_gian_chieu}"

# # Bảng Người Dùng (User)
# class NguoiDung(models.Model):
#     username = models.CharField(max_length=150, unique=True)
#     email = models.EmailField(unique=True)
#     sdt = models.CharField(max_length=15)
#     password = models.CharField(max_length=128)
#     gioi_tinh = models.CharField(max_length=10, choices=[('Nam', 'Nam'), ('Nu', 'Nữ')])
#     ngay_sinh = models.DateField()

#     def __str__(self):
#         return self.username

# # Bảng Vé (Ticket)
# class Ve(models.Model):
#     phim = models.ForeignKey(Phim, on_delete=models.CASCADE)
#     thoi_gian_chieu = models.ForeignKey(XuatChieu, on_delete=models.CASCADE)
#     rap = models.ForeignKey(RapChieu, on_delete=models.CASCADE)
#     ghe_ngoi = models.CharField(max_length=10)
#     loai_ghe = models.CharField(max_length=50)
#     gia_ve = models.DecimalField(max_digits=10, decimal_places=2)
#     ma_qr_ve = models.CharField(max_length=100)
#     user_mua_ve = models.ForeignKey(NguoiDung, on_delete=models.CASCADE)
#     link_face = models.CharField(max_length=200)  # Link hình ảnh để nhận diện khuôn mặt

#     def __str__(self):
#         return f"Vé {self.phim.ten_phim} - {self.user_mua_ve.username}"














# from django.db import models

# # Bảng Rạp Chiếu (Cinema)
# class RapChieu(models.Model):
#     ten_rap = models.CharField(max_length=200)  # Tên rạp chiếu
#     dia_chi = models.CharField(max_length=255)  # Địa chỉ của rạp chiếu
#     so_dien_thoai = models.CharField(max_length=15)  # Số điện thoại liên hệ
#     email = models.EmailField()  # Email của rạp chiếu

#     def __str__(self):
#         return self.ten_rap

# # Bảng Định Dạng Phim (Film Format)
# class DinhDangPhim(models.Model):
#     ten_dinh_dang = models.CharField(max_length=50)

#     def __str__(self):
#         return self.ten_dinh_dang

# # Bảng Thể Loại (Genre)
# class TheLoai(models.Model):
#     ten_the_loai = models.CharField(max_length=100)

#     def __str__(self):
#         return self.ten_the_loai

# # Bảng Phim (Movie)
# class Phim(models.Model):
#     ten_phim = models.CharField(max_length=200)
#     the_loai = models.ManyToManyField(TheLoai)  # Một phim có thể thuộc nhiều thể loại
#     dao_dien = models.CharField(max_length=100)
#     dien_vien = models.TextField()
#     thoi_luong = models.PositiveIntegerField()  # Thời lượng tính bằng phút
#     tom_tat = models.TextField()
#     thumbnail = models.CharField(max_length=200)  # Link ảnh thumbnail của phim

#     def __str__(self):
#         return self.ten_phim

# # Bảng Xuất Chiếu (Showtimes)
# class XuatChieu(models.Model):
#     phim = models.ForeignKey(Phim, on_delete=models.CASCADE)
#     thoi_gian_chieu = models.DateTimeField()
#     rap_chieu = models.ForeignKey(RapChieu, on_delete=models.CASCADE)  # Liên kết đến bảng rạp chiếu
#     dinh_dang_phim = models.ForeignKey(DinhDangPhim, on_delete=models.CASCADE)  # Liên kết đến bảng định dạng phim

#     def __str__(self):
#         return f"{self.phim.ten_phim} - {self.thoi_gian_chieu}"

# # Bảng Ghế Ngồi (Seat)
# class GheNgoi(models.Model):
#     ten_ghe = models.CharField(max_length=10)  # Tên ghế
#     rap_chieu = models.ForeignKey(RapChieu, on_delete=models.CASCADE)  # Rạp chiếu liên kết
#     loai_ghe = models.CharField(max_length=50)  # Loại ghế
#     gia_ve = models.DecimalField(max_digits=10, decimal_places=2)  # Giá vé

#     def __str__(self):
#         return f"{self.ten_ghe} - {self.rap_chieu.ten_rap} ({self.loai_ghe})"

# # Bảng Người Dùng (User)
# class NguoiDung(models.Model):
#     username = models.CharField(max_length=150, unique=True)
#     email = models.EmailField(unique=True)
#     sdt = models.CharField(max_length=15)
#     password = models.CharField(max_length=128)
#     gioi_tinh = models.CharField(max_length=10, choices=[('Nam', 'Nam'), ('Nu', 'Nữ')])
#     ngay_sinh = models.DateField()

#     def __str__(self):
#         return self.username

# # Bảng Vé (Ticket)
# class Ve(models.Model):
#     phim = models.ForeignKey(Phim, on_delete=models.CASCADE)
#     thoi_gian_chieu = models.ForeignKey(XuatChieu, on_delete=models.CASCADE)
#     rap = models.ForeignKey(RapChieu, on_delete=models.CASCADE)
#     ghe_ngoi = models.ForeignKey(GheNgoi, on_delete=models.CASCADE)  # Liên kết đến bảng Ghế Ngồi
#     loai_ghe = models.CharField(max_length=50, blank=True, editable=False)  # Tự động điền loại ghế
#     gia_ve = models.DecimalField(max_digits=10, decimal_places=2, blank=True, editable=False)  # Tự động điền giá vé
#     ma_qr_ve = models.CharField(max_length=100)
#     user_mua_ve = models.ForeignKey(NguoiDung, on_delete=models.CASCADE)
#     link_face = models.CharField(max_length=200)  # Link hình ảnh để nhận diện khuôn mặt

#     def __str__(self):
#         return f"Vé {self.phim.ten_phim} - {self.user_mua_ve.username}"

#     # Ghi đè phương thức save để tự động điền loai_ghe và gia_ve từ bảng Ghế Ngồi
#     def save(self, *args, **kwargs):
#         if self.ghe_ngoi:
#             self.loai_ghe = self.ghe_ngoi.loai_ghe  # Lấy loại ghế từ Ghế Ngồi
#             self.gia_ve = self.ghe_ngoi.gia_ve  # Lấy giá vé từ Ghế Ngồi
#         super().save(*args, **kwargs)







# from django.db import models

# # Bảng Combo (Combo)
# class Combo(models.Model):
#     ten_combo = models.CharField(max_length=100)  # Tên combo
#     gia_combo = models.DecimalField(max_digits=10, decimal_places=2)  # Giá combo

#     def __str__(self):
#         return f"{self.ten_combo} - {self.gia_combo}"

# # Bảng Rạp Chiếu (Cinema)
# class RapChieu(models.Model):
#     ten_rap = models.CharField(max_length=200)  # Tên rạp chiếu
#     dia_chi = models.CharField(max_length=255)  # Địa chỉ của rạp chiếu
#     so_dien_thoai = models.CharField(max_length=15)  # Số điện thoại liên hệ
#     email = models.EmailField()  # Email của rạp chiếu

#     def __str__(self):
#         return self.ten_rap

# # Bảng Định Dạng Phim (Film Format)
# class DinhDangPhim(models.Model):
#     ten_dinh_dang = models.CharField(max_length=50)

#     def __str__(self):
#         return self.ten_dinh_dang

# # Bảng Thể Loại (Genre)
# class TheLoai(models.Model):
#     ten_the_loai = models.CharField(max_length=100)

#     def __str__(self):
#         return self.ten_the_loai

# # Bảng Phim (Movie)
# class Phim(models.Model):
#     ten_phim = models.CharField(max_length=200)
#     the_loai = models.ManyToManyField(TheLoai)  # Một phim có thể thuộc nhiều thể loại
#     dao_dien = models.CharField(max_length=100)
#     dien_vien = models.TextField()
#     thoi_luong = models.PositiveIntegerField()  # Thời lượng tính bằng phút
#     tom_tat = models.TextField()
#     thumbnail = models.CharField(max_length=200)  # Link ảnh thumbnail của phim

#     def __str__(self):
#         return self.ten_phim

# # Bảng Xuất Chiếu (Showtimes)
# class XuatChieu(models.Model):
#     phim = models.ForeignKey(Phim, on_delete=models.CASCADE)
#     thoi_gian_chieu = models.DateTimeField()
#     rap_chieu = models.ForeignKey(RapChieu, on_delete=models.CASCADE)  # Liên kết đến bảng rạp chiếu
#     dinh_dang_phim = models.ForeignKey(DinhDangPhim, on_delete=models.CASCADE)  # Liên kết đến bảng định dạng phim

#     def __str__(self):
#         return f"{self.phim.ten_phim} - {self.thoi_gian_chieu}"

# # Bảng Ghế Ngồi (Seat)
# class GheNgoi(models.Model):
#     ten_ghe = models.CharField(max_length=10)  # Tên ghế
#     rap_chieu = models.ForeignKey(RapChieu, on_delete=models.CASCADE)  # Rạp chiếu liên kết
#     loai_ghe = models.CharField(max_length=50)  # Loại ghế
#     gia_ve = models.DecimalField(max_digits=10, decimal_places=2)  # Giá vé

#     def __str__(self):
#         return f"{self.ten_ghe} - {self.rap_chieu.ten_rap} ({self.loai_ghe})"

# # Bảng Người Dùng (User)
# class NguoiDung(models.Model):
#     username = models.CharField(max_length=150, unique=True)
#     email = models.EmailField(unique=True)
#     sdt = models.CharField(max_length=15)
#     password = models.CharField(max_length=128)
#     gioi_tinh = models.CharField(max_length=10, choices=[('Nam', 'Nam'), ('Nu', 'Nữ')])
#     ngay_sinh = models.DateField()

#     def __str__(self):
#         return self.username

# # Bảng Vé (Ticket)
# class Ve(models.Model):
#     phim = models.ForeignKey(Phim, on_delete=models.CASCADE)
#     thoi_gian_chieu = models.ForeignKey(XuatChieu, on_delete=models.CASCADE)
#     rap = models.ForeignKey(RapChieu, on_delete=models.CASCADE)
#     ghe_ngoi = models.ForeignKey(GheNgoi, on_delete=models.CASCADE)  # Liên kết đến bảng Ghế Ngồi
#     loai_ghe = models.CharField(max_length=50, blank=True, editable=False)  # Tự động điền loại ghế
#     gia_ve = models.DecimalField(max_digits=10, decimal_places=2, blank=True, editable=False)  # Tự động điền giá vé
#     ma_qr_ve = models.CharField(max_length=100)
#     user_mua_ve = models.ForeignKey(NguoiDung, on_delete=models.CASCADE)
#     link_face = models.CharField(max_length=200)  # Link hình ảnh để nhận diện khuôn mặt
#     combo = models.ForeignKey(Combo, on_delete=models.CASCADE, null=True, blank=True)  # Liên kết đến bảng Combo

#     def __str__(self):
#         return f"Vé {self.phim.ten_phim} - {self.user_mua_ve.username}"

#     # Ghi đè phương thức save để tự động điền loai_ghe và gia_ve từ bảng Ghế Ngồi
#     def save(self, *args, **kwargs):
#         if self.ghe_ngoi:
#             self.loai_ghe = self.ghe_ngoi.loai_ghe  # Lấy loại ghế từ Ghế Ngồi
#             self.gia_ve = self.ghe_ngoi.gia_ve  # Lấy giá vé từ Ghế Ngồi
#         super().save(*args, **kwargs)


from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Bảng Combo (Combo)
class Combo(models.Model):
    ten_combo = models.CharField(max_length=100)  # Tên combo
    gia_combo = models.DecimalField(max_digits=10, decimal_places=2)  # Giá combo

    def __str__(self):
        return f"{self.ten_combo} - {self.gia_combo}"

# Bảng Rạp Chiếu (Cinema)
class RapChieu(models.Model):
    ten_rap = models.CharField(max_length=200)  # Tên rạp chiếu
    dia_chi = models.CharField(max_length=255)  # Địa chỉ của rạp chiếu
    so_dien_thoai = models.CharField(max_length=15)  # Số điện thoại liên hệ
    email = models.EmailField()  # Email của rạp chiếu

    def __str__(self):
        return self.ten_rap

# Bảng Định Dạng Phim (Film Format)
class DinhDangPhim(models.Model):
    ten_dinh_dang = models.CharField(max_length=50)

    def __str__(self):
        return self.ten_dinh_dang

# Bảng Thể Loại (Genre)
class TheLoai(models.Model):
    ten_the_loai = models.CharField(max_length=100)

    def __str__(self):
        return self.ten_the_loai

# Bảng Phim (Movie)
class Phim(models.Model):
    ten_phim = models.CharField(max_length=200)
    the_loai = models.ManyToManyField(TheLoai)  # Một phim có thể thuộc nhiều thể loại
    dao_dien = models.CharField(max_length=100)
    dien_vien = models.TextField()
    thoi_luong = models.PositiveIntegerField()  # Thời lượng tính bằng phút
    tom_tat = models.TextField()
    thumbnail = models.CharField(max_length=200)  # Link ảnh thumbnail của phim
    do_tuoi = models.PositiveIntegerField(validators=[MinValueValidator(0)], default=0)  # Độ tuổi được xem phim

    def __str__(self):
        return self.ten_phim

# Bảng Xuất Chiếu (Showtimes)
class XuatChieu(models.Model):
    phim = models.ForeignKey(Phim, on_delete=models.CASCADE)
    thoi_gian_chieu = models.DateTimeField()
    rap_chieu = models.ForeignKey(RapChieu, on_delete=models.CASCADE)  # Liên kết đến bảng rạp chiếu
    dinh_dang_phim = models.ForeignKey(DinhDangPhim, on_delete=models.CASCADE)  # Liên kết đến bảng định dạng phim

    def __str__(self):
        return f"{self.phim.ten_phim} - {self.thoi_gian_chieu}"

# Bảng Ghế Ngồi (Seat)
class GheNgoi(models.Model):
    ten_ghe = models.CharField(max_length=10)  # Tên ghế
    rap_chieu = models.ForeignKey(RapChieu, on_delete=models.CASCADE)  # Rạp chiếu liên kết
    loai_ghe = models.CharField(max_length=50)  # Loại ghế
    gia_ve = models.DecimalField(max_digits=10, decimal_places=2)  # Giá vé

    def __str__(self):
        return f"{self.ten_ghe} - {self.rap_chieu.ten_rap} ({self.loai_ghe})"

# Bảng Người Dùng (User)
class NguoiDung(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    sdt = models.CharField(max_length=15)
    password = models.CharField(max_length=128)
    gioi_tinh = models.CharField(max_length=10, choices=[('Nam', 'Nam'), ('Nu', 'Nữ')])
    ngay_sinh = models.DateField()

    def __str__(self):
        return self.username

# Bảng Vé (Ticket)
class Ve(models.Model):
    phim = models.ForeignKey(Phim, on_delete=models.CASCADE)
    thoi_gian_chieu = models.ForeignKey(XuatChieu, on_delete=models.CASCADE)
    rap = models.ForeignKey(RapChieu, on_delete=models.CASCADE)
    ghe_ngoi = models.ForeignKey(GheNgoi, on_delete=models.CASCADE)  # Liên kết đến bảng Ghế Ngồi
    loai_ghe = models.CharField(max_length=50, blank=True, editable=False)  # Tự động điền loại ghế
    gia_ve = models.DecimalField(max_digits=10, decimal_places=2, blank=True, editable=False)  # Tự động điền giá vé
    ma_qr_ve = models.CharField(max_length=100)
    user_mua_ve = models.ForeignKey(NguoiDung, on_delete=models.CASCADE)
    link_face = models.CharField(max_length=200)  # Link hình ảnh để nhận diện khuôn mặt
    combo = models.ForeignKey(Combo, on_delete=models.CASCADE, null=True, blank=True)  # Liên kết đến bảng Combo

    def __str__(self):
        return f"Vé {self.phim.ten_phim} - {self.user_mua_ve.username}"

    # Ghi đè phương thức save để tự động điền loai_ghe và gia_ve từ bảng Ghế Ngồi
    def save(self, *args, **kwargs):
        if self.ghe_ngoi:
            self.loai_ghe = self.ghe_ngoi.loai_ghe  # Lấy loại ghế từ Ghế Ngồi
            self.gia_ve = self.ghe_ngoi.gia_ve  # Lấy giá vé từ Ghế Ngồi
        super().save(*args, **kwargs)

# Bảng Bình Luận (Comment)
class BinhLuan(models.Model):
    phim = models.ForeignKey(Phim, on_delete=models.CASCADE)  # Tên phim liên kết
    user_binh_luan = models.ForeignKey(NguoiDung, on_delete=models.CASCADE)  # Người dùng bình luận
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])  # Rating 1-5
    noi_dung = models.TextField()  # Nội dung bình luận

    def __str__(self):
        return f"Bình luận của {self.user_binh_luan.username} - {self.phim.ten_phim}"
