class HocSinh:
    def __init__(self, ho_ten, dia_chi, chieu_cao, can_nang, hoc_luc):
        self.ho_ten = ho_ten
        self.dia_chi = dia_chi
        self.chieu_cao = chieu_cao
        self.can_nang = can_nang
        self.hoc_luc = hoc_luc

    def cap_nhat_dia_chi(self, dia_chi_moi):
        self.dia_chi = dia_chi_moi
        print(f"Địa chỉ của {self.ho_ten} đã được cập nhật thành: {self.dia_chi}")

    def cap_nhat_suc_khoe(self, chieu_cao_moi, can_nang_moi):
        self.chieu_cao = chieu_cao_moi
        self.can_nang = can_nang_moi
        print(f"Chiều cao và cân nặng của {self.ho_ten} đã được cập nhật. "
              f"Chiều cao: {self.chieu_cao} cm, Cân nặng: {self.can_nang} kg")

    def xuat_thong_tin(self):
        print("Thông tin học sinh:")
        print(f"Họ và tên: {self.ho_ten}")
        print(f"Địa chỉ: {self.dia_chi}")
        print(f"Chiều cao: {self.chieu_cao} cm")
        print(f"Cân nặng: {self.can_nang} kg")
        print(f"Học lực: {self.hoc_luc}")
