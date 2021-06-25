import random

#Thanks to ichabod801 for the intial idea https://python-forum.io/thread-18779.html
 
FIRST = ['A', 'Ag', 'Ar', 'Ara', 'Anu', 'Bal', 'Bil', 'Boro', 'Bern', 'Bra', 'Cas', 'Cere', 'Co', 'Con',
    'Cor', 'Dag', 'Doo', 'Elen', 'El', 'En', 'Eo', 'Faf', 'Fan', 'Fara', 'Fre', 'Fro', 'Ga', 'Gala', 'Has', 
    'He', 'Heim', 'Ho', 'Isil', 'In', 'Ini', 'Is', 'Ka', 'Kuo', 'Lance', 'Lo', 'Ma', 'Mag', 'Mi', 'Mo', 
    'Moon', 'Mor', 'Mora', 'Nin', 'O', 'Obi', 'Og', 'Pelli', 'Por', 'Ran', 'Rud', 'Sam',  'She', 'Sheel', 
    'Shin', 'Shog', 'Son', 'Sur', 'Theo', 'Tho', 'Tris', 'U', 'Uh', 'Ul', 'Vap', 'Vish', 'Ya', 'Yo', 'Yyr']
 
SECOND = ['at', 'ar','an','ba', 'bis', 'bo', 'bus', 'da', 'dar' 'dal', 'dagz', 'den', 'di', 'dil', 'din', 'do', 'dor', 'dra', 
    'dur', 'gi', 'gauble', 'gen', 'glum', 'go', 'gorn', 'goth', 'had', 'hard', 'is', 'ki', 'koon', 'ku', 
    'lad', 'ler', 'li', 'lot', 'ma', 'man', 'mir', 'mus', 'nan', 'ni', 'nor', 'nu', 'nad' 'pian', 'ra', 'rak', 
    'ric', 'rin', 'rum', 'rus', 'rut', 'sek', 'sha', 'thos', 'thur', 'toa', 'tu', 'tur', 'tred', 'varl',
    'wain', 'wan', 'win', 'wise', 'ya']

THIRD = ['Beacon', 'God', 'Lord', 'Master', 'Saviour', 'Last', 'Brute', 'Echo', 'Apex'
         , 'Destiny', 'Protector', 'Hellion', 'Druid', 'Deciever', 'Tamer', 'Storm', 'Weaver'
         , 'Spitter', 'Fighter', 'Elite', 'Artificer', 'General', 'Capitan', 'Walker','Fallen',
        ]

FOURTH = ['of', 'becoming', 'of the', 'touched-by']

FIFTH = ['Destruction', 'Lies', 'Hope','Friendship', 'Planes', 'Aeons', 'Annihilation', 'Extinction'
         , 'Human', 'Beast', 'Snake', 'Death', 'Artifacts', 'Flames','Wall', 'Omen', 'Slayer', 'Merchants'
         , 'Fools', 'Emotions', 'Doom', 'Void', 'Field', 'Spacetime', 'Forest', 'Plains', 'Mountains', 'Swamps', 'Islands'
         , 'Ruins', 'Meek', 
        ]
SIX = [ 'Alara', 'Mirrodin', 'Ravnica','Theros', 'Innistrad','Zendikar', 'Kamigawa', 'Dominaria'
       , 'Lorwyn', 'Phyrexia', 'Wastelands', 'Bazaar', 'Alexandria', 'Strixhaven', 'Kaldhiem', 'Forgotten Realms'
       , 'Vast', 'Unknown', 'Dying Breath', 'Plague-wind', 'Shimmering-Coves', 'Yavimiya', 'Eternal Suffering'
      ]
    


def fantasy_name():
    
    n = random.randrange(0, 2)
    
    if n == 0:
        return random.choice(FIRST) + random.choice(SECOND) + ', ' + random.choice(THIRD) + ' ' + random.choice(FOURTH) +' ' + random.choice(FIFTH)
    else:
        return random.choice(THIRD) + ' '+ random.choice(FIRST) + random.choice(SECOND) + ' of ' + random.choice(SIX)
    
    
    
