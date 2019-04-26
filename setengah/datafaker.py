from faker import Faker
import datetime
import random
import json
fake = Faker()



'''
data = {}
data['Pembeli'] = []
path='./'
fileName = 'pembeli'
filePathNameWExt = './' + path + '/' + fileName + '.json'

for i in range(1, 10000):
	data['Pembeli'].append({  
		'id_akun' : i,
	    'nama': fake.name(),
	    'email':  fake.email(),
	    'no_telepon': str(random.randint(6280000000000, 6289999999999)),
	    'foto' : 'data/pembeli/foto' + str(i)+'.png',
	    'wallet' : random.randint(1,999999),
	    'jumlah_poin' : random.randint(10,99219)
	})
with open(filePathNameWExt, 'w') as fp:
	json.dump(data, fp, indent=4)
'''
'''
data = {}
data['Penjual'] = []
path='./'
fileName = 'penjual'
filePathNameWExt = './' + path + '/' + fileName + '.json'

for i in range(1, 1000):
	data['Penjual'].append({  
		'id_akun' : i,
	    'nama': fake.name(),
	    'email':  fake.email(),
	    'no_telepon': str(random.randint(6280000000000, 6289999999999)),
	    'foto' : 'data/pembeli/foto' + str(i)+'.png',
	    'wallet' : random.randint(1,999999),
	    'no_rekening' : str(random.randint(1013232,9992019))
	})
with open(filePathNameWExt, 'w') as fp:
	json.dump(data, fp, indent=4)
'''
'''
data = {}
data['Voucher'] = []
path='./'
fileName = 'voucher'
filePathNameWExt = './' + path + '/' + fileName + '.json'

for i in range(1, 30000):
	data['Voucher'].append({  
		'kode_voucher' : i,
		'masa_berlaku' :  str(fake.date_between_dates(date_start=(datetime.date(day = 2, year = 2018, month = 2)), date_end=(datetime.date(day = 2, year = 2028, month = 2)))),
		'potongan_harga' : random.randint(1, 50) * 1000
	})
'''


def getJSON(filePathAndName):
    with open(filePathAndName, 'r') as fp:
        return json.load(fp)


'''
data = {}
data['Barang'] = []
path='./'
fileName = 'barang'
filePathNameWExt = './' + path + '/' + fileName + '.json'
namaBarang = ['Pensil', 'Pulpen', 'Buku', 'Kursi', 'Meja', 'Komputer', 'Pengserut', 'Speaker', 'Microphone', 'Diary', 'Susu', 'Kalkulator']
merk = ['Apple', 'HP', 'Pastel', 'Bjarne', 'Samsung', 'Stable', 'Exec', 'MOR', 'Joyko']

for i in range(1, 5000):
	data['Barang'].append({  
		'id_barang' : i,
		'id_akun' : str(random.randint(1,100)),
	    'stok': random.randint(0,1000),
	    'harga':  random.randint(5,100) * 1000,
	    'deskripi': str(random.randint(1111111111, 11111111110)),
	    'nama_barang' : random.choice(namaBarang) + ' ' + fake.color_name() + ' ' + random.choice(merk)
	})
'''
'''
data = {}
data['Kurir'] = []
path='./'
fileName = 'kurir'
filePathNameWExt = './' + path + '/' + fileName + '.json'
kurirId = ['622', '625', '667', '379', '501']

for i in range(1, 10):
	data['Kurir'].append({  
		'id_kurir' : int(random.choice(kurirId) + str(i)),
	    'nama' : fake.last_name_female()
	})



data = {}
data['Voucher'] = []
path='./'
fileName = 'voucher'
filePathNameWExt = './' + path + '/' + fileName + '.json'
VoucherId1 = ['622', '625', '667', '379', '501']
VoucherId2 = ['111', '902', '1234', '332', '123']

for i in range(1, 1000):
	data['Voucher'].append({  
		'kodeVoucher' : random.choice(VoucherId1) + random.choice(VoucherId2) + str(i),
	    'masaBerlaku' : str(fake.date_between_dates(date_start=(datetime.date(day = 2, year = 2018, month = 2)), date_end=(datetime.date(day = 2, year = 2028, month = 2))))
	})
'''

data = {}
data['Pembayaran'] = []
path='./'
fileName = 'pembayaran'
filePathNameWExt = './' + path + '/' + fileName + '.json'
pembId = ['100', '200', '300', '400', '500']
metode = ['Kredit','Debit','Visa','Cash','GoPay','OVO','Dana',]

for i in range(1, 35000):
	data['Pembayaran'].append({  
		'id_pembayaran' : int(random.choice(pembId) + str(random.randint(10001,10999)) + str(i)),
	    'id_akun' : int(str(random.randint(1,100))),
	    'nominal' : str(random.randint(5,100000) * 1000),
	    'metode' : random.choice(metode)
	})

'''

data = {}
data['Alamat'] = []
path='./'
fileName = 'alamat'
filePathNameWExt = './' + path + '/' + fileName + '.json'
namaAlamat = ['Bisnis', 'Rumah'] 
namaAlamat2 = ['Kerja', 'Misc']

for i in range(1, 100):
	data['Alamat'].append({  
		'IdAkun' : str(i),
	    'NamaAlamat' : str(random.choice(namaAlamat)),
	    'Detail' : fake.address()
	})
	if(i % 4 == 3):
		data['Alamat'].append({  
			'IdAkun' : str(i),
		    'NamaAlamat' : str(random.choice(namaAlamat2)),
		    'Detail' : fake.address()
		})


kurirlist = []
temp = []
listofkurir = getJSON('./kurir.json').get('Kurir',[])
for kurir in listofkurir:
	temp = [(k,v) for k,v in kurir.items()]
	kurirlist.append(temp)

alamatlist = []
temp = []
listofalamat = getJSON('./alamat.json').get('Alamat',[])
for alamat in listofalamat:
	temp = [(k,v) for k,v in alamat.items()]
	alamatlist.append(temp)

print(alamatlist)

data = {}
data['Transaksi'] = []
path='./'
fileName = 'transaksi'
filePathNameWExt = './' + path + '/' + fileName + '.json'
VoucherId1 = ['153', '209']
VoucherId2 = ['332', '111', '009', '777']
idofkurir = []
for x in kurirlist:
	for k in x:
		if (k[0] == 'IdKurir'):
			idofkurir.append(k[1])

for i in range(1, 2000):

	namaAlamati = ''

	temp = []

	temp = random.choice(alamatlist)

	for x in temp:
		if x[0] == 'IdAkun':
			idAkuni = x[1]
		if x[0] == 'NamaAlamat':
			namaAlamati = x[1]
	
	idKurir = random.choice(idofkurir)
	
	data['Transaksi'].append({  
		'IdTransaksi' : random.choice(VoucherId1) + random.choice(VoucherId2) + str(i),
	    'IdAkun' : idAkuni,
	    'IdKurir' : idKurir,
	    'NamaAlamat' : namaAlamati,
	    'TanggalTransaksi' : str(fake.date_between_dates(date_start=(datetime.date(day = 2, year = 2012, month = 2)), date_end=(datetime.date(day = 2, year = 2019, month = 2))))
	})


transaksilist = []
temp = []
listoftran = getJSON('./transaksi.json').get('Transaksi',[])
for tran in listoftran:
	temp = [(k,v) for k,v in tran.items()]
	transaksilist.append(temp)

#print(transaksilist)


data = {}
data['TransaksiLine'] = []
path='./'
fileName = 'transaksiline'
filePathNameWExt = './' + path + '/' + fileName + '.json'

for i in transaksilist:
	for x in i:
		if (x[0] == 'IdTransaksi'):
			idtran = x[1]
	for j in range(1, random.randint(2, 10)):
		data['TransaksiLine'].append({  
			'IdTransaksi' : idtran,
		    'NoBaris' : j,
		    'IdBarang' : str(random.randint(1, 1000)),
		    'JumlahBarang' : str(random.randint(1, 100))
		})


voucherlist = []
temp = []
listofvou = getJSON('./voucher.json').get('Voucher',[])
for vouc in listofvou:
	temp = [(k,v) for k,v in vouc.items()]
	voucherlist.append(temp)

#print(transaksilist)


data = {}
data['Memiliki'] = []
path='./'
fileName = 'memiliki'
filePathNameWExt = './' + path + '/' + fileName + '.json'

for i in range(0, 10):
	for x in range(1, 100):
		if ((x * x + 4) % 3 == 1):
			idtran = x + i
			for j in range(1, random.randint(2, 10)):
				data['Memiliki'].append({  
					'IdAkun' : idtran,
				    'kodeVoucher' : random.choice(voucherlist)[1][1]
				})



voucherlist = []
temp = []
listofvou = getJSON('./voucher.json').get('Voucher',[])
for vouc in listofvou:
	temp = [(k,v) for k,v in vouc.items()]
	voucherlist.append(temp)

pembayaranlist = []
temp = []
listofvou = getJSON('./pembayaran.json').get('Pembayaran',[])
for vouc in listofvou:
	temp = [(k,v) for k,v in vouc.items()]
	pembayaranlist.append(temp)


data = {}
data['Menggunakan'] = []
path='./'
fileName = 'menggunakan'
filePathNameWExt = './' + path + '/' + fileName + '.json'

for x in pembayaranlist:
	for y in x:
		y[0] == 'IdPembayaran'
		idtran = y[1]
	if ((int(idtran) * int(idtran) + 4) % 3 == 1):
		for j in range(1, random.randint(1, 4)):
			data['Menggunakan'].append({  
				'IdPembayaran' : idtran,
			    'kodeVoucher' : random.choice(voucherlist)[1][1]
			})


kurirlist = []
temp = []
listofkurir = getJSON('./kurir.json').get('Kurir',[])
for kurir in listofkurir:
	temp = [(k,v) for k,v in kurir.items()]
	kurirlist.append(temp)
idofkurir = []
for x in kurirlist:
	for k in x:
		if (k[0] == 'IdKurir'):
			idofkurir.append(k[1])

data = {}
data['KerjaSama'] = []
path='./'
fileName = 'kerjasama'
filePathNameWExt = './' + path + '/' + fileName + '.json'

for x in range(0,100):
	temp =[]
	for p in range(0, random.randint(1, 7)):
		ran = random.choice(idofkurir)
		if(ran not in temp):
			temp.append(ran)
	for l in temp:
		data['KerjaSama'].append({  
			'IdAkun' : x,
		    'IdKurir' : l
		})


tlinelist = []
temp = []
listofvou = getJSON('./transaksiline.json').get('TransaksiLine',[])
for vouc in listofvou:
	temp = [(k,v) for k,v in vouc.items()]
	tlinelist.append(temp)


data = {}
data['Review'] = []
path='./'
fileName = 'review'
filePathNameWExt = './' + path + '/' + fileName + '.json'
cnt = 0
for x in tlinelist:
	cnt += 1;
	if(random.randint(1, 10) % 5 == 1):
		for y in x:
			if(y[0] == 'IdTransaksi'):
				idtran = y[1]
			if(y[0]	== 'NoBaris'):
				noBar = y[1]
		data['Review'].append({  
			'IdReview' : '12300' + str(cnt),
		    'IdTransaksi' : idtran,
		    'NoBaris' : noBar,
		    'Konten' : 'Warna barang saya terlalu ' + fake.color_name(),
		    'Rating' : str(random.randint(0, 5)),
		    'WaktuReview' :  str(fake.date_between_dates(date_start=(datetime.date(day = 2, year = 2012, month = 2)), date_end=(datetime.date(day = 2, year = 2019, month = 2))))
		})
'''

with open(filePathNameWExt, 'w') as fp:
	json.dump(data, fp, indent=4)