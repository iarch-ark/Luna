def respon_bot(pesan):
    pesan = pesan.lower()
    
    if "halo" in pesan:
        return "Halo juga! Ada yang bisa aku bantu?"
    elif "nama kamu siapa" in pesan:
        return "Aku adalah AI sederhana buatanmu."
    elif "cuaca" in pesan:
        return "Wah, aku kurang tahu cuaca hari ini. Coba lihat ke luar jendela ya!"
    else:
        return "Maaf, aku belum paham maksudmu. Bisa tanyakan dengan kata lain?"

# Program utama
print("Halo! Aku AI sederhana. Ketik 'keluar' untuk berhenti.")

while True:
    pengguna = input("\nKamu: ")
    
    if pengguna.lower() == "keluar":
        print("AI: Sampai jumpa lagi!")
        break
        
    jawaban = respon_bot(pengguna)
    print(f"AI: {jawaban}")
