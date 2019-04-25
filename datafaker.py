from faker import Faker
import datetime
import random
import json
fake = Faker()




'''data = {}
data['Pembeli'] = []
path='./'
fileName = 'pembeli'
filePathNameWExt = './' + path + '/' + fileName + '.json'

for i in range(1, 100):
	data['Pembeli'].append({  
		'Idx' : str(i),
	    'Nama': fake.name(),
	    'Email':  fake.email(),
	    'NoTelepon': str(random.randint(6280000000000, 6289999999999)),
	    'Foto' : 'data/pembeli/foto' + str(i)+'.png',
	    'Wallet' : str(random.randint(1,999999)),
	    'JumlahPoin' : str(random.randint(10,99219))
	})
with open(filePathNameWExt, 'w') as fp:
	json.dump(data, fp, indent=4)'''

'''data = {}
data['Voucher'] = []
path='./'
fileName = 'voucher'
filePathNameWExt = './' + path + '/' + fileName + '.json'

for i in range(1, 100):
	data['Voucher'].append({  
		'Idx' : str(i),
	    'Nama': fake.name(),
	    'Email':  fake.email(),
	    'NoTelepon': str(random.randint(6280000000000, 6289999999999)),
	    'Foto' : 'data/pembeli/foto' + str(i)+'.png',
	    'Wallet' : str(random.randint(1,999999)),
	    'JumlahPoin' : str(random.randint(10,99219))
	})
'''

def getJSON(filePathAndName):
    with open(filePathAndName, 'r') as fp:
        return json.load(fp)

# Example of returning just JSON
# jsonFile = getJSON('./test.json') # Uncomment this line
# It gets returned as a dictionary.

# Example of getting a list from a JSON file
# test.json looks like:
# {
#   "photos" : [
#           "test1",
#           "test2"
#       ]
# }
'''
listofpenjual = getJSON('./penjual.json').get('Penjual',[])
for penjual in listofpenjual:
	penjual['Nama']

data = {}
data['Barang'] = []
path='./'
fileName = 'barang'
filePathNameWExt = './' + path + '/' + fileName + '.json'
namaBarang = ['Pensil', 'Pulpen', 'Buku', 'Kursi', 'Meja', 'Komputer', 'Pengserut', 'Speaker', 'Microphone', 'Diary', 'Susu', 'Kalkulator']
merk = ['Apple', 'HP', 'Pastel', 'Bjarne', 'Samsung', 'Stable', 'Exec', 'MOR', 'Joyko']

for i in range(1, 1000):
	data['Barang'].append({  
		'IdBarang' : str(i),
		'IdAkun' : str(random.randint(1,100)),
	    'Stok': str(random.randint(0,1000)),
	    'Harga':  str(random.randint(5,100) * 10000),
	    'Deskripsi': '-',
	    'NamaBarang' : random.choice(namaBarang) + ' ' + fake.color_name() + ' ' + random.choice(merk)
	})'''
'''
data = {}
data['Kurir'] = []
path='./'
fileName = 'kurir'
filePathNameWExt = './' + path + '/' + fileName + '.json'
kurirId = ['622', '625', '667', '379', '501']

for i in range(1, 10):
	data['Kurir'].append({  
		'IdKurir' : random.choice(kurirId) + str(i),
	    'NamaKurir' : fake.last_name_female()
	})
'''

'''
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

'''
data = {}
data['Pembayaran'] = []
path='./'
fileName = 'pembayaran'
filePathNameWExt = './' + path + '/' + fileName + '.json'
pembId = ['100', '200', '300', '400', '500']
metode = ['Kredit','Debit','Visa','Cash','GoPay','OVO','Dana',]

for i in range(1, 2000):
	data['Pembayaran'].append({  
		'IdPembayaran' : random.choice(pembId) + str(random.randint(10001,10999)) + str(i),
	    'IdAkun' : str(random.randint(1,100)),
	    'Nominal' : str(random.randint(5,100000) * 1000),
	    'Metode' : random.choice(metode)
	})
'''

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
'''
'''
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
'''
'''
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
'''
'''
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

'''
'''
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
'''
'''
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
'''
'''
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