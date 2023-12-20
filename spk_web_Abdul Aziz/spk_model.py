from settings import SCALE_NAMA

class BaseMethod():

    def __init__(self, data_dict, **setWeight):
        self.dataDict = data_dict

        # 1-7 (Kriteria)
        self.raw_weight = {
            "nama": 5,
            "harga": 1,
            "cc": 6,
            "kapasitas bensin": 2,
            "daya maksimum": 3,
            "torsi maksimum": 4
        }

        if setWeight:
            for item in setWeight.items():
                temp1 = setWeight[item[0]] # value int
                temp2 = {v: k for k, v in setWeight.items()}[item[1]] # key str

                setWeight[item[0]] = item[1]
                setWeight[temp2] = temp1

    @property
    def weight(self):
        total_weight = sum(self.raw_weight.values())
        return {c: round(w/total_weight, 2) for c,w in self.raw_weight.items()}

    @property
    def data(self):
        return [{
            'id': motor['nama'],
            "nama": SCALE_NAMA[motor['nama']],
            "harga": motor['harga'],
            "cc": motor['cc'],
            "kapasitas bensin": motor['kapasitas bensin'],
            "daya maksimum": motor['daya maksimum'],
            "torsi maksimum":motor['torsi maksimum'] 
        } for motor in self.dataDict]
    
    @property
    def normalized_data(self):
        # x/max [benefit]
        # min/x [cost]
        nama = [] # max
        harga = [] # min
        cc = [] # max
        kapasitas_bensin = [] # max
        daya_maksimum = [] # max
        torsi_maksimum = [] # max
        
        for data in self.data:
            nama.append(data['nama'])
            harga.append(data['harga'])
            cc.append(data['cc'])
            kapasitas_bensin.append(data['kapasitas bensin'])
            daya_maksimum.append(data['daya maksimum'])
            torsi_maksimum.append(data['torsi maksimum'])

        max_nama = max(nama)
        min_harga = min(harga)
        max_cc = max(cc)
        max_kapasitas_bensin = max(kapasitas_bensin)
        max_daya_maksimum = max(daya_maksimum)
        max_torsi_maksimum = max(torsi_maksimum)

        return [
            {   'id': data['id'],
                'nama': data['nama']/max_nama, # benefit
                'harga': min_harga/data['harga'], # cost
                'cc': data['cc']/max_cc, # benefit
                'kapasitas bensin': data['kapasitas bensin']/max_kapasitas_bensin, # benefit
                'daya maksimum': data['daya maksimum']/max_daya_maksimum, # benefit
                'torsi maksimum': max_torsi_maksimum/data['torsi maksimum'] # benefit
                }
            for data in self.data
        ]

class WeightedProduct(BaseMethod):
    def __init__(self, dataDict, setWeight:dict):
        super().__init__(data_dict=dataDict, **setWeight)
    @property
    def calculate(self):
        weight = self.weight
        result = {row['id']:
    round(
        row['nama'] ** weight['nama'] *
        row['harga'] ** weight['harga'] *
        row['cc'] ** weight['cc'] *
        row['kapasitas bensin'] ** weight['kapasitas bensin'] *
        row['daya maksimum'] ** weight['daya maksimum'] *
        row['torsi maksimum'] ** weight['torsi maksimum']
        , 2
    )
    for row in self.normalized_data}

        #sorting
        # return result
        return dict(sorted(result.items(), key=lambda x:x[1], reverse=True))