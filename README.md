# Title Project
NBA Point Per Game Prediction For The Next Season
## Repository Outline

Berikut deskripsi file:
```
1. README.md - Penjelasan gambaran umum project.
2. P1M2_raifky_leditho.ipynb - Notebook yang berisi pengolahan data seperti loading data, EDA, feature engineering, modeling dan kesimpulan.
3. P1M2_raifky_leditho_inf.ipynb - Notebook yang berisi model inference untuk predict data baru.
4. model_metadata.json - berisi kolom numerical, kategorical, target dan model.
5. ridge_pipeline.pkl - berisi pipeline yang berisis model ridge regression, preprocessing, encoder.
6. sportsref_nba.csv - berisi dataset dari project ini.
7. description.md - berisi definisi project, problem
```

## Problem Background
Dalam dunia olahraga basket, khususnya NBA, performa pemain dipengaruhi oleh berbagai faktor statistik seperti menit bermain, efisiensi tembakan, dan peran posisi pemain. Salah satu indikator utama performa tersebut adalah jumlah poin (PTS) yang dicetak dalam pertandingan. Namun, memprediksi jumlah poin berdasarkan data statistik bukanlah hal yang sederhana karena banyaknya variabel yang saling berkaitan.

Tanpa adanya pendekatan analisis yang terstruktur, evaluasi performa pemain cenderung bersifat subjektif dan kurang akurat. Oleh karena itu, diperlukan pendekatan berbasis machine learning dengan metode regresi untuk mempelajari pola dari data historis pemain sehingga dapat menghasilkan prediksi poin yang lebih objektif dan dapat diandalkan.

## Project Output
Output dari project machine learning ini adalah bisa memprediksi point (PTS) pemain NBA untuk musim depan, dan bisa memprediksi data baru.

## Data
Dataset ini saya dapatkan dari website https://www.basketball-reference.com/ website ini menyediakan statistik lampau pemain NBA dan juga statistik musim yang sedang berlangsung, Karakteristik dari dataset yang saya pakai adalah dataset tersebut adalah statistik akhir musim 2024-2025 dan mayoritas dari dataset tersebut bertipe numerical yang mempunyai 500 data dan terdapat 31 kolom, di kolom ini terdapat missing value pada kolom 3P% dengan jumlah 18, FT% 3 dan awards dengan 447 saya tidak handling missing value pada kolom tersebut karena kolom tersebut tidak di pakai sebagai fitur, terdapat outliers yang positive skewed di kolom FTA dengan persentase 1.25 dan kolom TRB dengan persentase 0.25 saya tidak handling outliers karena ingin keep data se-real mungkin dan juga skewed nya juga tidak terlalu ekstrem.

## Method
Project machine learning yang saya buat dengan berbasis supervised learning dengan menggunakan model ridge regression saya menggunakan ridge regression karena MAE nya paling kecil dari model yang lain dan MAPE nya hanya di angka 9.0 maka dari itu saya memilih ridge regression pada project machine learning ini.

## Stacks
Di project ini saya menggunakan bahasa pemrograman python dan deploy model ke hugging face dan menggunakan liblary seperti:

- pandas: untuk manipulasi data
- seaborn: untuk visualisasi data
- numpy: untuk manipulasi data
- matplotlib: untuk visualisasi data
- spearmann: untuk menghitung korelasi
- train_test_split: untuk train dan split data
- robustscaler: untuk scaling data
- onehotencoder: untuk encoding data
- columntransformer: untuk transform data
- pipeline: untuk membuat pipeline
- linear regression, ridge regression, lasso regression, randomforestregressor, gradientboostingregression: untuk model
- GridSearchCV: untuk melakukan hyperparameter tuning
- mean_absolute_error, mean_squared_error, r2_score: untuk evaluasi model
- json: untuk encode
- joblib: untuk saving
- warnings: untuk menghilangkan warning
- mean_absolute_percentage_error: untuk evaluasi model
- streamlit: untuk deploy model

## Reference
link Hugging Face: https://huggingface.co/spaces/Raifky/inference_nba
link dataset: https://www.basketball-reference.com
---

