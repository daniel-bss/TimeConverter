def timeConverter(seconds):
    # Menguji apakah input adalah string
    try:
        #Jika input adalah float, maka keluar dari try/except
        float(seconds)
    except:
        #Jika input adalah string, maka program akan error
        print('Masukkan detik :',seconds)
        print('Invalid Input!')
        print()
        quit()

    if '.' in str(seconds): #Menguji apakah input adalah float
        print('Masukkan detik :',seconds)
        print('Invalid Input!')
        
    else:
        seconds = int(seconds) 
        if seconds > 359999 or seconds < 0: #Menguji apakah input lebih dari 359999 atau negatif
            print('Masukkan detik :',seconds)
            print('Invalid Input!')
            
        else:
            #Melakukan floor division untuk mengambil integer dari jam
            hour = seconds // 3600

            #Melakukan modulo untuk mengambil sisa dari detik jam
            #Melakukan floor division untuk mengambil integer dari menit
            minute = (seconds % 3600) // 60
            
            #Melakukan modulo untuk mengambil sisa detik dari menit
            second = (seconds % 3600) % 60
 
            #Berikut di bawah ini adalah membuat conditional statement
            #pada 6 kemungkinan kombinasi HH:MM:SS
            #Jika nilainya satuan, akan diberi angka '0'
            if hour < 10 and minute < 10 and second < 10:
                print('Masukkan detik :',seconds)
                print('Konversi : 0%s:0%s:0%s' %(hour,minute,second))

            elif hour < 10 and minute < 10 and second >= 10:
                print('Masukkan detik :',seconds)
                print('Konversi : 0%s:0%s:%s' %(hour,minute,second))

            elif hour < 10 and minute >= 10 and second < 10:
                print('Masukkan detik :',seconds)
                print('Konversi : 0%s:%s:0%s' %(hour,minute,second))

            elif hour < 10 and minute >= 10 and second >= 10:
                print('Masukkan detik :',seconds)
                print('Konversi : 0%s:%s:%s' %(hour,minute,second))

            elif hour >= 10 and minute < 10 and second < 10:
                print('Masukkan detik :',seconds)
                print('Konversi : %s:0%s:0%s' %(hour,minute,second))

            elif hour >= 10 and minute < 10 and second >= 10:
                print('Masukkan detik :',seconds)
                print('Konversi : %s:0%s:%s' %(hour,minute,second))

            elif hour >= 10 and minute >= 10 and second < 10:
                print('Masukkan detik :',seconds)
                print('Konversi : %s:%s:0%s' %(hour,minute,second))

            elif hour >= 10 and minute >= 10 and second >= 10:
                print('Masukkan detik :',seconds)
                print('Konversi : %s:%s:%s' %(hour,minute,second))                
            
    print() #Pemberian space kosong pada akhir function

#Mencoba pada beberapa nominal detik
timeConverter(3600) 
timeConverter(3665)
timeConverter(10000)
timeConverter(291723)

#Mencoba pada batas maksimum detik yaitu 359999
timeConverter(360000)

#Mencoba jika input adalah bilangan desimal
timeConverter(20.5)

#Mencoba jika input adalah bilangan negatif
timeConverter(-3600)

#Mencoba jika input adalah string
timeConverter('ujian')
