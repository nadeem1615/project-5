import pandas as pd

def main():
    # Specify the encoding parameter explicitly
    df = pd.read_csv(r"C:\Users\Admin\Desktop\Edda mvone.txt", encoding="utf-8")
    print(df)

if __name__ == "__main__":
    main()
