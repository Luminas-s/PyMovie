from django import forms
from .models import Phim, NguoiDung, TheLoai, DinhDangPhim, XuatChieu, RapChieu, Ve, GheNgoi, Combo
from django.contrib.auth.hashers import make_password

class PhimForm(forms.ModelForm):
    class Meta:
        model = Phim
        fields = ['ten_phim', 'the_loai', 'dao_dien', 'dien_vien', 'thoi_luong', 'tom_tat', 'thumbnail']

class NguoiDungForm(forms.ModelForm):
    class Meta:
        model = NguoiDung
        fields = ['username', 'email', 'sdt', 'password', 'gioi_tinh', 'ngay_sinh']
        widgets = {
            'password': forms.PasswordInput(),  # Hiển thị trường mật khẩu
            'ngay_sinh': forms.DateInput(attrs={'type': 'date', 'placeholder': 'dd/mm/yyyy'})  # Định dạng ngày sinh
        }
        
class TheLoaiForm(forms.ModelForm):
    class Meta:
        model = TheLoai
        fields = ['ten_the_loai']
        
class DinhDangPhimForm(forms.ModelForm):
    class Meta:
        model = DinhDangPhim
        fields = ['ten_dinh_dang']
        
        
class RapChieuForm(forms.ModelForm):
    class Meta:
        model = RapChieu
        fields = ['ten_rap', 'dia_chi', 'so_dien_thoai', 'email']
        
        
        
class XuatChieuForm(forms.ModelForm):
    class Meta:
        model = XuatChieu
        fields = ['phim', 'thoi_gian_chieu', 'rap_chieu', 'dinh_dang_phim']
        widgets = {
            'thoi_gian_chieu': forms.DateTimeInput(attrs={'type': 'datetime-local'}),  # Định dạng cho thời gian chiếu
        }

# class VeForm(forms.ModelForm):
#     class Meta:
#         model = Ve
#         fields = ['phim', 'thoi_gian_chieu', 'rap', 'ghe_ngoi', 'loai_ghe', 'gia_ve', 'ma_qr_ve', 'user_mua_ve', 'link_face']



from django import forms
from .models import Ve

class VeForm(forms.ModelForm):
    class Meta:
        model = Ve
        fields = ['phim', 'thoi_gian_chieu', 'rap', 'ghe_ngoi', 'ma_qr_ve', 'user_mua_ve', 'combo','link_face']
        widgets = {
            'phim': forms.Select(),
            'thoi_gian_chieu': forms.Select(),
            'rap': forms.Select(),
            'ghe_ngoi': forms.Select(),
            'combo' : forms.Select(),
            'ma_qr_ve': forms.TextInput(),
            'user_mua_ve': forms.Select(),
        }

class ComboForm(forms.ModelForm):
    class Meta:
        model = Combo
        fields = ['ten_combo', 'gia_combo']
        widgets = {
            'gia_combo': forms.NumberInput(attrs={'step': '0.01'}),
        }
        
class GheNgoiForm(forms.ModelForm):
    class Meta:
        model = GheNgoi
        fields = ['ten_ghe', 'rap_chieu', 'loai_ghe', 'gia_ve']

####
class RegistrationForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput, label='Mật khẩu')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Nhập lại mật khẩu')

    class Meta:
        model = NguoiDung
        fields = ['username', 'email', 'sdt', 'gioi_tinh', 'ngay_sinh']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError("Mật khẩu không khớp!")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = make_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

