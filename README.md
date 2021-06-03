# Bike Sharing in Washington DC using Machine Learning

ScikitLearnGroup_JC_DS_12_FinalProject

Member :
- Ibnu Yusuf Prakoso (iyp36@hotmail.com)
- Kevin Octavio Untoro (kevinoctavio.u@gmail.com)
- Kelvin Lois (kelvinnlois@gmail.com)

Dataset taken from : [Bike Sharing in Washington D.C. Dataset](https://www.kaggle.com/marklvl/bike-sharing-dataset)

### Background
Bike sharing systems are a new generation of traditional bike rentals where the whole process from membership, rental and return back has become automatic. Through these systems, user is able to easily rent a bike from a particular position and return back to another position. Currently, there are about over 500 bike-sharing programs around the world which are composed of over 500 thousands bicycles. Today, there exists great interest in these systems due to their important role in traffic, environmental and health issues.

Apart from interesting real-world applications of bike sharing systems, the characteristics of data being generated by these systems make them attractive for the research. Opposed to other transport services such as bus or subway, the duration of travel, departure and arrival position is explicitly recorded in these systems. This feature turns bike sharing system into a virtual sensor network that can be used for sensing mobility in the city. Hence, it is expected that most of important events in the city could be detected via monitoring these data.

This dataset contains the hourly and daily count of rental bikes between years 2011 and 2012 in Capital bikeshare system in Washington, DC with the corresponding weather and seasonal information.

Dataset Characteristic

- instant: Record index
- dteday: Date
- season: Season (1:spring, 2:summer, 3:fall, 4:winter)
- yr: Year (0: 2011, 1:2012)
- mnth: Month (1 to 12)
- hr: Hour (0 to 23)
- holiday: whether day is holiday or not (extracted from Holiday Schedule)
- weekday: Day of the week
- workingday: If day is neither weekend nor holiday is 1, otherwise is 0.
- weathersit: (extracted from Freemeteo)
    - 1: Clear, Few clouds, Partly cloudy, Partly cloudy
    - 2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist
    - 3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds
    - 4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog
- temp: Normalized temperature in Celsius. The values are derived via (t-tmin)/(tmax-tmin), tmin=-8, t_max=+39 (only in hourly scale)
- atemp: Normalized feeling temperature in Celsius. The values are derived via (t-tmin)/(tmax-tmin), tmin=-16, t_max=+50 (only in hourly scale)
- hum: Normalized humidity. The values are divided to 100 (max)
- windspeed: Normalized wind speed. The values are divided to 67 (max)
- casual: count of casual users
- registered: count of registered users
- cnt: count of total rental bikes including both casual and registered



### Introduction

Sepeda membutuhkan pemeliharaan rutin untuk dapat dipakai (sebagai sepeda rental) dalam jangka waktu yang lama. Karena volume penggunaan sepeda bervariasi dari waktu ke waktu (e.g. bervariasi terhadap jam, bulan, tahun), maka jadwal maintenance sepeda harus terstruktur dan dinamis. Penjadwalan maintenance yang disesuaikan trend volume penggunaan sepeda diharapkan dapat memaksimumkan umur penggunaan sepeda, meminimalisir _customer loss_ akibat kekurangan stok sepeda yang ada di lapangan ketika permitaan sepeda tinggi dan memaksimumkan _income_ apabila permintaan penggunaan sepeda selalu dapat dipenuhi.

### Problems

- Penjadwalan maintenance yang buruk dapat mengurangi umur sepeda dan dapat menyebabkan kehilangan pelanggan (pemeliharaan sepeda mempengaruhi masualah stok di lapangan, karena sepeda yg sedang diperbaiki akan ditarik dari peredaran untuk sesaat. Disaat banyak nya sepeda yg harus diperbaiki secara bersamaan, secara tidak langsung mengurangi stok sepeda di lapangan dan menjadi potensi kehilangan customer).
- Volume penggunaan sepeda pada musim tertentu (_winter_) relatif lebih kecil dari musim-musim lain. 
- Pada hari-hari tertentu, jumlah permintaan sepeda naik/turun secara drastis.


### Goals

- __Prediksi penggunaan sepeda__ (minimum dan maksimum) untuk meminimalisir _customer loss_ dan memperkirakan stok sepeda.
- Membuat __penjadwalan *maintenance*__ yang baik untuk meminimalisir _customer loss_.


### Data Cleaning & Pre - Processing

- Checking Missing Value
    - ![Missing Value](https://github.com/PurwadhikaDev/ScikitLearnGroup_JC_DS_12_FinalProject/blob/main/SS/missing%20value.jpeg)
    
- Checking Outliers
    - ![Outliers Box Plot](https://github.com/PurwadhikaDev/ScikitLearnGroup_JC_DS_12_FinalProject/blob/main/SS/outliers%20boxplot.jpeg)
    - ![Outliers Tabular](https://github.com/PurwadhikaDev/ScikitLearnGroup_JC_DS_12_FinalProject/blob/main/SS/outliers%20tabular.jpeg)

- Pre-processing 
    - Membuat kolom baru untuk memisahkan Outliers dengan data asli. Untuk melakukan pengecheckan apakah Outliers ini berpengaruh terhadap data asli
    
    - Melakukan re-scaling ulang terhadap Variable tertentu seperti: 
        - temp (Temperature)
        - atemp (Feels like - Temperature)
        - Humidity (Kelembaban)
        - Windspeed (Kecepatan Angin)
            - Yang di gunakan untuk mempermudah mencari **INSIGHT** dari **Exploratory Data Analysis**
      
     - Melakukan perubahan Nama untuk Variable:
         - Season
         - Month
         - Year
         - Holiday
         - Workingday
         - Weathersit
             - Dilakukannya perubahan agar memudahkan untuk mencerna Dataset.
         
### Quick Data Analysis
-  Dari Analisa yang kita dapatkan, masyrakat di Washington D.C lebih cenderung bersepeda saat kondisi temperature yang hangat dengan range temperature 20-30s derajat Celcius, bisa di artikan bahwa itu adalah temperature yang ideal. Dikarenakan rata-rata temperature di Washington DC adalah 17 derajat Celcius.

- Penyewaan Sepeda cenderung lebih ramai di hari kerja (Senin - Jumat) pada pukul 8 dan 17 karena di gunakan untuk berangkat dan pulang kerja.

- Saat Weekend (Sabtu dan Minggu) penyewaan sepeda Ramai di jam 13.00 karena di gunakan untuk rekreasi

- Weathersit Clear adalah kondisi dimana masyarakat Washington D.C paling banyak menyewa Sepeda. Dengan rata-rata 205 sepeda per jam.

- Di bulan Juni, Juli , Agustus merupakan bulan yang mempunyai musim Summer (Panas) yang memiliki temperature paling tinggi di antara semua bulan di Tahun tersebut. Dengan demikian jumlah masyarakat yang menyewa sepeda di musim Summer adalah yang terbanyak di bandingkan musim yang lain. Dengan Rata- Rata 236 orang sepeda per jam nya.

- Diantara tahun 2011 dan 2012, penyewaan sepeda terbanyak terjadi di tahun 2012. Yang mempunyai peningkatan sebesar **39.3%**) dari tahun 2011

- [Full Data Analysis](https://github.com/PurwadhikaDev/ScikitLearnGroup_JC_DS_12_FinalProject/blob/main/Exploratory%20Data%20Analysis%20-%20Bike%20Sharing.ipynb)

### Machine Learning Regression

Machine Learning Regression di lakukan untuk memprediksi jumlah Stock sepeda yang di sediakan setiap harinya. Target Scoring adalah R-Squared, Mean Absolute Error dan Residual Negative. Semakin tinggi nilai R-Squared, maka semakin kecil Mean Absolute Error yang di dapat.

Feature Selection di lakukan terhadap Variable:
    - temp
        - Sudah terwakilkan dengan variable atemp
    - dteday
        - Sudah di extract menjadi Year, Month, Day, Hour
    - casual
    - registered
        - Dilakukannya pengedrop-an casual dan registered karena target model yang di gunakan adalah variable **cnt** yang merupakan penjumlahan data **casual** dan data **registered**.

- Base Model Terbaik:
    - Decision Tree
        - ![Decision Tree](https://github.com/PurwadhikaDev/ScikitLearnGroup_JC_DS_12_FinalProject/blob/main/SS/DT%20Based.png)    
   
    
    - Random Forest Regressor
        - ![Random Forest](https://github.com/PurwadhikaDev/ScikitLearnGroup_JC_DS_12_FinalProject/blob/main/SS/RF%20Base.png)
    
    - XGBoost
        - ![XGBoost](https://github.com/PurwadhikaDev/ScikitLearnGroup_JC_DS_12_FinalProject/blob/main/SS/XGB%20Base.png)
    
- Hyperparameter Tuning:
     - Decision Tree
         - best.params: 'max_depth' : [15], 'max_features' : None, 'min_samples_leaf' : [2], 'min_samples_split' : [12]
        
            - ![Decision Tree](https://github.com/PurwadhikaDev/ScikitLearnGroup_JC_DS_12_FinalProject/blob/main/SS/DT%20Grid%201.png)
    
    - Random Forest Regressor
        - best.params: 'n_estimators' : [2280], 'max_depth' : [81], 'max_features' : ['None'], 'min_samples_leaf' : [1], 'min_samples_split' : [4]
        
            - ![Random Forest](https://github.com/PurwadhikaDev/ScikitLearnGroup_JC_DS_12_FinalProject/blob/main/SS/RF-Bayes.png)
    
    - XGBoost
        - best.params: 'learning_rate' : [0.3], 'max_depth' : [46], 'n_estimators' : [5700]
        
            - ![XGBoost](https://github.com/PurwadhikaDev/ScikitLearnGroup_JC_DS_12_FinalProject/blob/main/SS/XGB%20Random.png)


Tabel Evaluation Matrix
- ![Eva Matrix](https://github.com/PurwadhikaDev/ScikitLearnGroup_JC_DS_12_FinalProject/blob/main/SS/Compare.png)

### Machine Learning Insight
Berdasarkan Evaluation Matrix di atas, Ditemukan 5 Model Machine Learning yang memenuhi kriteria Bike Sharing Prediction. Dengan basis scoring R-Squared, MAE, dan Residual Negative.
- `Base DecisionTree` Mempunyai nilai Residual Negative terbaik, tetapi model tersebut Overfitting. 
- `XGBoost Tuned Randomized` adalah model yang memiliki Residual Negative tertinggi setelah `Base DT`, dan memiliki nilai MAE dan R-Squared yg bagus.
- `Decision Tree Tuned Grid 2` memiliki Residual Negative yang cukup tinggi tetapi nilai MAE nya di atas rata-rata MAE semua model. 
- `Base RandomForest` dan `RandomForest Tuned Bayes` memiliki nilai Evaluation Matrix yang mirip.

### Conclusion
Best Model Machine Learning yang dipilih adalah **XGBoost Tuned Randomized**, karena memiliki nilai R-Squared yang tinggi sebesar 94,8 dan MAE lebih rendah di bandingkan dengan rata-rata MAE semua model dan Memiliki Nilai Residual Negative 54,68%.

- Untuk Jadwal Bike Maintenance bisa dengan beberapa opsi/sequnce :

    - Dilakukan Maintenance Ringan secara Harian pada pukul 4 Pagi.
        - Contoh: Pengecheckan Ban Bocor.
    - Dilakukan Maintenance Mingguan pada hari Minggu pada pukul 5 Pagi.
        - Contoh: Pelumasan Rantai & Pengecheckan Kabel Rem
    - Tidak disarankan untuk Bike Maintenancce secara Bulanan
        - Berakibat banyaknya sepeda yang harus di maintenance sekaligus.
    - Melakukan pengecheckan terlebih dahulu terhadap hari maintenance tersebut untuk menghindari Customer Lost.
        - Adanya Event pada hari Maintenance.
    - Menyamakan Jadwal Bike Maintenance dengan Jadwal Storing-Pickup Sepeda dimana stock sepeda yang berlebih di lapangan/station di-pickup untuk disimpan di Warehouse.
        - Contoh : Jadwal Storing-Pickup harian jam 5 dan jam 21, jadwal Bike Maintenance bisa disamakan.
    
- Perlu ada nya manajemen Stock Sepeda yang baik setiap hari nya :
    
     - Menyediakan Sepeda lebih banyak saat Work-day
     - Efisiensi Bike Storing
         - Menyimpan Sepeda pada saat minat penyewaan Sepeda Kecil, Untuk Menghindari Kerusakan

   
