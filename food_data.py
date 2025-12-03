class Makanan:
    def __init__(self, nama, harga, mood, kalori, protein, karbo, lemak):
        self.nama = nama
        self.harga = int(harga)
        self.mood = mood
        self.kalori = int(kalori)
        self.protein = int(protein)
        self.karbo = int(karbo)
        self.lemak = int(lemak)

menu_list = [
# Bagian Cutting
    # Sedih
    Makanan("Sup Ayam Bening ", 15000, "Sedih", 220, 20, 18, 6),
    Makanan("Tahu Kukus Saus Kecap", 7000, "Sedih", 180, 14, 10, 5),
    Makanan("Nasi 1/2 + Ayam Rebus", 12000, "Sedih", 260, 24, 28, 4),

    # Marah
    Makanan("Capcay Tanpa Minyak", 18000, "Marah", 200, 10, 22, 4),
    Makanan("Ayam Lemon Kukus", 20000, "Marah", 240, 26, 12, 5),
    Makanan("Onigiri Tuna ", 11000, "Marah", 230, 14, 35, 3),

    # Sehat
    Makanan("Salad Tahu Telur", 18000, "Sehat", 250, 20, 14, 8),
    Makanan("Sup Sayur Ayam 1 porsi", 20000, "Sehat", 260, 22, 20, 6),
    Makanan("Nasi Merah 1/2 + Sayur", 18000, "Sehat", 230, 7, 42, 3),

    # Senang
    Makanan("Yogurt + Buah 1/2", 20000, "Senang", 240, 10, 35, 4),
    Makanan("Ayam Panggang Madu ", 25000, "Senang", 300, 27, 28, 6),
    Makanan("Sushi Telur Timun", 15000, "Senang", 230, 9, 40, 3),

    # Biasa
    Makanan("Tumis Sayur + Telur", 15000, "Biasa", 260, 14, 28, 8),
    Makanan("Tahu Putih Kukus", 6000, "Biasa", 200, 12, 8, 5),
    Makanan("Nasi 1/2 + Ikan Pindang", 18000, "Biasa", 300, 25, 30, 6),


# Ini tuh bagian maintance(stabil)
    # Sedih
    Makanan("Bakso Kuah 1 porsi", 15000, "Sedih", 350, 18, 32, 10),
    Makanan("Ayam Kecap 1 porsi", 20000, "Sedih", 480, 24, 50, 12),
    Makanan("Nasi Uduk Mini", 15000, "Sedih", 430, 14, 60, 15),

    # Marah
    Makanan("Ayam Sambal Bawang", 20000, "Marah", 500, 28, 55, 15),
    Makanan("Tempe Penyet", 12000, "Marah", 400, 18, 35, 20),
    Makanan("Bakmi Jawa 1 porsi", 20000, "Marah", 520, 22, 65, 14),

    # Sehat
    Makanan("Ikan Kembung Bakar", 27000, "Sehat", 520, 30, 55, 10),
    Makanan("Pecel Sayur + Telur", 18000, "Sehat", 480, 20, 55, 14),
    Makanan("Ayam Kukus + Sayur", 22000, "Sehat", 450, 32, 40, 8),

    # Senang
    Makanan("Chicken Mentai Rice porsi", 22000, "Senang", 600, 28, 70, 22),
    Makanan("Ayam Lada Hitam", 23000, "Senang", 560, 30, 65, 14),
    Makanan("Soto Ayam + Nasi", 20000, "Senang", 500, 22, 60, 10),

    # Biasa
    Makanan("Ayam Kuning + Nasi", 21000, "Biasa", 520, 28, 55, 12),
    Makanan("Capcay Ayam + Nasi", 23000, "Biasa", 540, 25, 60, 12),
    Makanan("Bakso + Mie Kuning", 20000, "Biasa", 580, 22, 70, 18),


# Bagian bulking
    # Sedih
    Makanan("Nasi 1.5 + Ayam Suwir", 25000, "Sedih", 650, 32, 85, 15),
    Makanan("Roti + Selai Kacang", 18000, "Sedih", 600, 18, 75, 20),
    Makanan("Mie Telur + Telur", 15000, "Sedih", 700, 22, 90, 20),

    # Marah
    Makanan("Ayam Crispy Jumbo", 20000, "Marah", 800, 32, 70, 38),
    Makanan("Nasi Ayam Korea Pedas", 23000, "Marah", 780, 32, 90, 28),
    Makanan("Katsu Don", 25000, "Marah", 750, 30, 95, 30),

    # Sehat
    Makanan("Nasi Merah + Ayam Grill", 28000, "Sehat", 680, 35, 75, 18),
    Makanan("Smoothie Oat Pisang", 17000, "Sehat", 550, 15, 80, 12),
    Makanan("Tumis Tahu Tempe + Nasi", 20000, "Sehat", 620, 30, 70, 20),

    # Senang
    Makanan("Chicken Mentai Rice", 22000, "Senang", 650, 28, 80, 28),
    Makanan("Beef Bowl", 25000, "Senang", 700, 35, 85, 25),
    Makanan("Roti Coklat + Susu", 18000, "Senang", 650, 14, 95, 15),

    # Biasa
    Makanan("Mie Ayam Bakso", 18000, "Biasa", 650, 25, 85, 20),
    Makanan("Nasi + Telur Dadar + Tempe", 17000, "Biasa", 680, 26, 80, 18),
    Makanan("Ayam Geprek Jumbo", 20000, "Biasa", 780, 32, 85, 28),
]