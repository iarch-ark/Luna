import google.generativeai as genai

genai.configure(api_key="AIzaSyBdgf-erUKvLnJGLmra82Ue7qPWN6M3n3I")
    

# Main
print("Halo! Aku Luna. Ketik 'keluar' untuk berhenti.")

while True:
    User = input("\nKamu: ")
    if User.lower() == "keluar":
        print("Luna: Sampai jumpa lagi!")
        break

    jawaban = respon_bot(User)
    print(f"Luna: {jawaban}")
