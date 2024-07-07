def ask_question(question, options):
    print(question)
    for i, option in enumerate(options):
        print(f"{chr(97 + i)}. {option[0]} ({option[1]})")
    while True:
        answer = input("Pilih jawaban (a, b, c, d): ").lower()
        if answer in ['a', 'b', 'c', 'd']:
            return options[ord(answer) - 97][1]
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

def calculate_score(answers):
    a_score = sum(score for i, score in enumerate(answers) if i % 2 == 0)
    d_score = sum(score for i, score in enumerate(answers) if i % 2 != 0)
    return a_score, d_score

def interpret_score(a_score, d_score):
    print("\nJUMLAH TOTAL")
    print(f"A: {a_score}")
    print(f"D: {d_score}")
    
    def interpret_individual_score(score):
        if score <= 7:
            return "Normal"
        elif 8 <= score <= 10:
            return "Borderline Abnormal"
        else:
            return "Abnormal"

    print("\nPenilaian")
    print(f"A: {interpret_individual_score(a_score)}")
    print(f"D: {interpret_individual_score(d_score)}")

def main():
    questions = [
        ("Saya merasa tegang:", [("Hampir sepanjang waktu", 3), ("Sebagian besar waktu", 2), ("Kadang-kadang", 1), ("Tidak sama sekali", 0)]),
        ("Saya masih bisa menikmati sesuatu yang biasanya saya sukai:", [("Masih seperti biasanya", 0), ("Tidak terlalu banyak", 1), ("Hanya sedikit", 2), ("Tidak sama sekali", 3)]),
        ("Saya mempunyai perasaan takut seperti sesuatu yang buruk akan terjadi:", [("Benar dan membuat saya takut", 3), ("Ya, tapi tidak terlalu buruk", 2), ("Sedikit, tapi tidak membuat saya khawatir", 1), ("Tidak sama sekali", 0)]),
        ("Saya bisa tertawa dan bisa melihat sesuatu yang lucu:", [("Masih seperti biasanya", 0), ("Tidak seperti biasanya", 1), ("Hampir tidak bisa", 2), ("Tidak sama sekali", 3)]),
        ("Perasaan khawatir dalam pikiran:", [("Hampir sepanjang waktu", 3), ("Sebagian besar waktu", 2), ("Kadang-kadang, tidak terlalu sering", 1), ("Sangat jarang", 0)]),
        ("Saya merasa gembira:", [("Tidak sama sekali", 0), ("Jarang", 1), ("Kadang-kadang", 2), ("Sebagian besar waktu", 3)]),
        ("Saya bisa duduk tenang dan merasa santai:", [("Ya", 0), ("Selalu", 1), ("Jarang", 2), ("Tidak sama sekali", 3)]),
        ("Saya bisa tertawa dan bisa melihat sesuatu yang lucu:", [("Hampir sepanjang waktu", 3), ("Sering", 2), ("Kadang-kadang", 1), ("Tidak sama sekali", 0)]),
        ("Saya mempunyai perasaan menakutkan seperti ada yang tidak beres didalam perut:", [("Tidak sama sekali", 3), ("Kadang-kadang", 2), ("Sering", 1), ("Sangat sering", 0)]),
        ("Saya kehilangan minat untuk menjaga penampilan:", [("Ya", 0), ("Sangat tidak memperhatikan", 1), ("Saya hanya sedikit memperhatikan", 2), ("Saya memperhatikan sebisa saya", 3)]),
        ("Saya merasa lelah saat beraktivitas:", [("Sangat lelah", 3), ("Sering lelah", 2), ("Kadang-kadang lelah", 1), ("Tidak sama sekali", 0)]),
        ("Saya melakukan sesuatu dengan senang hati:", [("Ya, seperti biasanya", 0), ("Lebih jarang daripada biasanya", 1), ("Hampir tidak seperti biasanya", 2), ("Tidak sama sekali", 3)]),
        ("Saya merasa tiba-tiba ada perasaan panik:", [("Sangat sering", 3), ("Sering", 2), ("Jarang", 1), ("Tidak sama sekali", 0)]),
        ("Saya merasa gembira:", [("Sering", 0), ("Kadang-kadang", 1), ("Jarang", 2), ("Sangat jarang", 3)])
    ]
    
    answers = []
    for question, options in questions:
        score = ask_question(question, options)
        answers.append(score)
    
    a_score, d_score = calculate_score(answers)
    interpret_score(a_score, d_score)

if __name__ == "__main__":
    main()
