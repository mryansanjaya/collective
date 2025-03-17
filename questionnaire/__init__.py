from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'questionnaire'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    age = models.IntegerField(min=1, max=99, label='Usia (dalam tahun) saat ini: ')
    gender = models.StringField(
        choices=['Perempuan', 'Laki-laki'],
        widget=widgets.RadioSelect,
        label='Jenis kelamin: '
    )
    major = models.StringField(
        choices=['Ekonomi dan bisnis', 'Ilmu sosial/humaniora selain ekonomi dan bisnis', 'Lainnya', 'Tidak relevan (bukan mahasiswa)'],
        widget=widgets.RadioSelect,
        label='Rumpun ilmu tempat Anda belajar saat ini'
    )
    region = models.StringField(
        choices=['Daerah Istimewa Yogyakarta', 'Jawa Tengah', 'Jawa Barat/Banten', 'DKI Jakarta', 'Jawa Timur', 'Lainnya'],
        widget=widgets.RadioSelect,
        label='Daerah tempat Anda paling lama tinggal: '
    )
    income = models.StringField(
        choices=['Kurang dari Rp500.000', 'Rp500.000 - Rp1.000.000', 'Rp1.000.001 - Rp1.500.000', 'Rp1.500.001 - Rp2.000.000', 'Rp2.000.001 - Rp2.500.000', 'Rp2.500.001 - Rp3.000.000', 'Di atas Rp3.000.000'],
        widget=widgets.RadioSelect,
        label='Uang saku atau penghasilan yang Anda terima per bulan: '
    )
    experiment = models.IntegerField(min=0, label='Berapa kali Anda pernah mengikuti eksperimen/tugas pengambilan keputusan seperti ini?')
    comments = models.StringField(label='Komentar:')


class Questionnaire(Page):
    form_model = 'player'
    form_fields = [
    'age',
    'gender',
    'major',
    'region',
    'income',
    'experiment',
    'comments'
    ]

class PaymentInfo(Page):
    pass

page_sequence = [Questionnaire, PaymentInfo]
