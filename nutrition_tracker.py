# nutrition_tracker.py

class UserTracker:
    def __init__(self):
        self.__current_kalori = 0
        self.limit = 2000 
        self.goal = "Maintenance"

    def hitung_kebutuhan(self, bb, tb, goal_user):
        self.goal = goal_user
        # Rumus BMR (Mifflin-St Jeor)
        bmr = (10 * bb) + (6.25 * tb) - (5 * 20) + 5 
        tdee = bmr * 1.3 
        
        if self.goal == "Cutting":
            self.limit = int(tdee - 500)
        elif self.goal == "Bulking":
            self.limit = int(tdee + 500)
        else:
            self.limit = int(tdee)
            
        return self.limit

    # FILTER Makanan dari food dataaaa
    def cek_kecocokan_makanan(self, makanan):
        p = makanan.protein
        k = makanan.karbo
        cal = makanan.kalori

        if self.goal == "Cutting":
            # Syarat: Protein Tinggi (>20), Karbo Rendah (<30), Kalori Kecil
            if p >= 20 and k < 30 and cal < 400:
                return True
                
        elif self.goal == "Bulking":
            # Syarat: Kalori Besar (>500) ATAU (Protein & Karbo Tinggi)
            if cal > 500 or (p > 20 and k > 50):
                return True
                
        elif self.goal == "Maintenance":
            # Syarat: Kalori Normal (300-600)
            if 300 <= cal <= 600:
                return True
                
        return False


# Parameter progesi kalori hariann
    def makan(self, makanan_obj):
        self.__current_kalori += makanan_obj.kalori
    
    # === BAGIAN INI YANG SUDAH DIGABUNG (UPDATE LOGIKA OVERLIMIT) ===
    def get_status(self):
        sisa = self.limit - self.__current_kalori
        
        # LOGIKA OVERLIMIT (MODUL 2)
        if sisa < 0:
            # abs() itu absolute value, biar angkanya gak minus pas ditampilin
            kelebihan = abs(sisa) 
            return f"OVERLIMIT KALORI HARIAN!!!! (+{kelebihan} kkal)"
        else:
            return f"{self.__current_kalori} / {self.limit} kkal (Sisa: {sisa})"
    # ================================================================

    def get_limit(self):
        return self.limit

    # --- FUNGSI INFO STRATEGI ---
    def get_goal_info(self):
        if self.goal == "Cutting":
            return "Strategi: Protein Tinggi, Kurangi Karbo & Lemak"
        elif self.goal == "Bulking":
            return "Strategi: Surplus Kalori, Karbo & Protein Tinggi"
        else:
            return "Strategi: Gizi Seimbang & Kalori Normal"