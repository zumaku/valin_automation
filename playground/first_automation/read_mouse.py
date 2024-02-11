import pyautogui

def main():
    try:
        while True:
            # Membaca posisi x dan y mouse
            x, y = pyautogui.position()
            
            # Menampilkan posisi x dan y mouse
            print(f"Posisi X: {x}, Posisi Y: {y}")
    except KeyboardInterrupt:
        print("\nProgram berhenti.")

if __name__ == "__main__":
    main()
