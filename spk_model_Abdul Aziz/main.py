import sys

from colorama import Fore, Style
from models import Base, MotorSport
from engine import engine

from sqlalchemy import select
from sqlalchemy.orm import Session
from settings import SCALE_NAMA

session = Session(engine)

def create_table():
    Base.metadata.create_all(engine)
    print(f'{Fore.GREEN}[Success]: {Style.RESET_ALL}Database has created!')

class BaseMethod():

    def __init__(self):
        # 1-6
        self.raw_weight = {
            "nama": 5,
            "harga": 1,
            "cc": 6,
            "kapasitas bensin": 2,
            "daya maksimum": 3,
            "torsi maksimum": 4
        }

    @property
    def weight(self):
        total_weight = sum(self.raw_weight.values())
        return {k: round(v/total_weight, 2) for k,v in self.raw_weight.items()}

    @property
    def data(self):
        query = select(MotorSport)
        return [{
            'id': motor_sport.nama,
            'nama': SCALE_NAMA["".join([x for x in SCALE_NAMA.keys() if x.lower() == motor_sport.nama.lower()])],
            'harga': motor_sport.harga,
            'cc': motor_sport.cc,
            'kapasitas bensin': motor_sport.kapasitas_bensin,
            'daya maksimum': motor_sport.daya_maksimum,
            'torsi maksimum': motor_sport.torsi_maksimum
        } for motor_sport in session.scalars(query)]

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
            {   'id': data['nama'],
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
        return dict(sorted(result.items(), key=lambda x:x[1]))

class SimpleAdditiveWeighting(BaseMethod):
    
    @property
    def calculate(self):
        weight = self.weight
        # calculate data and weight
        result =  {row['id']:
            round(
                row['nama'] * weight['nama'] +
                row['harga'] * weight['harga'] +
                row['cc'] * weight['cc'] +
                row['kapasitas bensin'] * weight['kapasitas bensin'] +
                row['daya maksimum'] * weight['daya maksimum'] +
                row['torsi maksimum'] * weight['torsi maksimum']
                , 2
            )
            for row in self.normalized_data
        }
        # sorting
        return dict(sorted(result.items(), key=lambda x:x[1]))

def run_saw():
    saw = SimpleAdditiveWeighting()
    print('result:', saw.calculate)

def run_wp():
    wp = WeightedProduct()
    print('result:', wp.calculate)

if len(sys.argv)>1:
    arg = sys.argv[1]

    if arg == 'create_table':
        create_table()
    elif arg == 'saw':
        run_saw()
    elif arg =='wp':
        run_wp()
    else:
        print('command not found')
