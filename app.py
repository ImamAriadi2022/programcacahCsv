import pandas as pd

# Baca file CSV
file_path = 'survey-lung-cancer.csv'


# Baca file CSV tanpa header, gunakan delimiter koma
data = pd.read_csv(file_path, header=None, delimiter=',')

# Pisahkan header (baris pertama)
headers = data.iloc[0].tolist()  # Ambil baris pertama sebagai header
data = data[1:]  # Sisakan baris berikutnya sebagai data

# Tetapkan header ke dataframe
data.columns = headers

# Simpan hasil ke file Excel
output_path = 'output_file.xlsx'
data.to_excel(output_path, index=False)

print("Data berhasil diproses dan disimpan ke:", output_path)