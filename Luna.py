def respon_bot(message):
    message = message.lower()
    
    if "halo" in message:
        return "Halo juga! Ada yang bisa aku bantu?"
    elif "nama kamu siapa" in message:
        return "Aku adalah AI sederhana buatanmu."
    elif "cuaca" in message:
        return "Wah, aku kurang tahu cuaca hari ini. Coba lihat ke luar jendela ya!"
    else:
        return "Maaf, aku belum paham maksudmu. Bisa tanyakan dengan kata lain?"

# Main
print("Halo! Aku Luna. Ketik 'keluar' untuk berhenti.")

while True:
    User = input("\nKamu: ")
    if User.lower() == "keluar":
        print("Luna: Sampai jumpa lagi!")
        break
      
    jawaban = respon_bot(User)
    print(f"Luna: {jawaban}")
