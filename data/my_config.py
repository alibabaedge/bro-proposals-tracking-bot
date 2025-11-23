NOTIFIER_FREQUENCY = 60 * 15 # seconds

SQL_PATH = './data/proposals.db'

TG_BOT_API_TOKEN = '6068988718:AAF2Pk8Y6KIB4kF98exfM3vu1ayO22ggqi4'
CHAT_ID = '-1001868672315'   # insert chat id, even if tarts with -
MESSAGE_THREAD_ID = '3474' # insert MESSAGE_THREAD id

NOTIFIER_REMINDER_MODES = {
        "SOFT": (range(345_600, 3_036_800), 86_400),
        "MEDIUM": (range(172_800, 345_600), 43_200),
        "HARD": (range(86_400, 172_800), 21_600),
        "EXTREME": (range(0, 86_400), 1800)
}

NETWORKS = [
    {
        "name": "cosmos",
        # Multiple endpoints for automatic fallback if one fails
        "lcd_endpoints": [
            "https://rest.lavenderfive.com:443/cosmoshub",
            "https://cosmos-rest.publicnode.com",
            "https://api.cosmos.citizenweb3.com"
        ],
        "validator": "cosmosvaloper1e859xaue4k2jzqw20cv6l7p3tmc378pc3k8g2u",
        "prefix": "cosmos",
        "explorer": "https://www.mintscan.io/cosmos/proposals/"
    },
    {
        "name": "bostrom",
        "lcd_api": "http://jupiter.cybernode.ai:36317",
        "validator": "bostromvaloper1f7nx65pmayfenpfwzwaamwas4ygmvalqj6dz5r",
        "prefix": "bostrom",
        "explorer": "https://cyb.ai/senate/"
    },
    {
        "name": "quicksilver",
        "lcd_api": "https://api.quicksilver.citizenweb3.com",
        "validator": "quickvaloper1m77eksxfz9q50qejnqf720sns7q0xtx8a7t9vq",
        "prefix": "quick",
        "explorer": "https://quicksilver.explorers.guru/proposals/"
    },
    {
        "name": "gravity",
        "lcd_api": "https://api.gravity.citizenweb3.com",
        "validator": "gravityvaloper1a00v3m5sthed82267gvdp2qt9czhjngg2djy8m",
        "prefix": "gravity",
        "explorer": "https://www.mintscan.io/gravity-bridge/proposals/"
    },
    {
        "name": "uptick",
        "lcd_api": "https://api.uptick.citizenweb3.com",
        "validator": "uptickvaloper1ke3qlvuhcn537m47l3y3hj0v7jm48ka47nkduu",
        "prefix": "uptick",
        "explorer": "https://uptick.explorers.guru/proposals/"
    },
    {
        "name": "stride",
        "lcd_api": "https://api.stride.citizenweb3.com",
        "validator": "stridevaloper1m77eksxfz9q50qejnqf720sns7q0xtx8gf36rj",
        "prefix": "stride",
        "explorer": "https://www.mintscan.io/stride/proposals/"
    },
    {
        "name": "althea",
        "lcd_api": "https://api.althea.citizenweb3.com",
        "validator": "altheavaloper1m77eksxfz9q50qejnqf720sns7q0xtx8c4r6fm",
        "prefix": "althea",
        "explorer": "https://www.mintscan.io/althea/proposals/"
    },
    {
        "name": "symphony",
        "lcd_endpoints": [
            "https://api.symphony.citizenweb3.com",
            "https://symphony-api.polkachu.com",
            "https://symphony.api.m.stavr.tech"
        ],
        "validator": "symphonyvaloper1m77eksxfz9q50qejnqf720sns7q0xtx8vdaj7d",
        "prefix": "symphony",
        "explorer": "https://www.mintscan.io/symphony/proposals/"
    },
    {
        "name": "axone",
        "lcd_endpoints": [
            "https://api.axone.citizenweb3.com",
            "https://rest.devnet.axone.xyz",
            "https://api-axone.mms.team"
        ],
        "validator": "axonevaloper1wnpak7sfawsfv9c8vqe7naxfa4g99lv7wd2wl6",
        "prefix": "axone",
        "explorer": "https://www.mintscan.io/axone/proposals/"
    },
    {
        "name": "atomone",
        "gov_prefix": "atomone",  # AtomOne uses /atomone/gov/ instead of /cosmos/gov/
        # Multiple endpoints for automatic fallback if one fails
        "lcd_endpoints": [
            "https://atomone-api.polkachu.com",
            "https://api.atomone.citizenweb3.com",
            "https://atomone-rest.publicnode.com"
        ],
        "validator": "atonevaloper1e859xaue4k2jzqw20cv6l7p3tmc378pcclyn60",
        "prefix": "atone",
        "explorer": "https://validatorinfo.com/networks/atomone/proposal/"
    },
    {
        "name": "namada",
        "provider": "namada",  # Required: specifies Namada provider usage
        "validator_address": "tnam1qx6k7xv66y58jw2jngtt98x0r9k3wtljxqd7qe2l",  # Namada validator address
        "indexers": [
            "https://indexer.namada.citizenweb3.com",  # Citizen Web3
            "https://indexer.namada.net",  # Heliax (official)
            "https://index-namada.5elementsnodes.com",  # 5ElementsNodes
            "https://namada-indexer.denodes.xyz",  # deNodes
            "https://namada-indexer.wavefive.xyz",  # Wavefive
            "https://namada-mainnet-indexer.mellifera.network"  # MELLIFERA
        ],
        "explorer": "https://validatorinfo.com/networks/namada/proposal/"
    }
]

PHRASES = {
        "SOFT": [
            'Hey 😀 Looks like its new proposal in the Cosmos ecosystem',
            'Take your time. But remember, you have to vote anyway! 😴',
            'Hello! Have a look to a new proposal! 😀',
            'Probably is there something interesting here? 🧐',
            'Yet another drama or not? 🤡',

        ],
        "MEDIUM": [
            'Tik-tok! The time has come! Your decision ❓',
            'I understand youre guys very busy 🥸🥸🥸, but one of the responsibilities of a validator is voting ‼️',
            'Just take a look on that, maybe is something interesting here...'
            'You havent voted yet? 😱😱😱'
        ],
        "HARD": [
            'Vote abstain if you have no idea 💩',
            'Yes? No? Abstain? No with veto? Hurry up, lets decide! 👊👊👊',
            'You have to vote. Please. 🤐',
            'There is no time for thinking! Decision! 👿'
        ],
        "EXTREME": [
            'You wanna die or what?',
            'I know a lot of irresponsible validators but you... 💩💩💩',
            'Wanna lose all of your delegators? You are close to.',
            'D E C I S I O N',
            'Hey 🤬. Get your butt up and vote!'
        ]
}