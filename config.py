from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("24755516"))
API_HASH = getenv("f06b275511fff3403ddd75e0534cd48c")

BOT_TOKEN = getenv("6037166517:AAFPkF1XS4A8YNUIANf33u7JNidmkB58wVU", None)
DURATION_LIMIT = int(getenv("90", "90"))

OWNER_ID = int(getenv("1083660482"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/6f99c49bdb4679acad717.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/f8ba75bdbb9931cbc8229.jpg")

SESSION = getenv("BQF5vTwAt6oKGDPHm4jTCF4iG0ZpqNKLb45n3vFfLRrlL15QPnujRUlykreUvpCYmIg70vkr1JZgfmYE5wAU8LOv5pNGLnyNolR-NrpATOykE6daKNI34WbVJ00glpVzCYOFMxZKNtnV4cYDglThad8xW367cCnCl9QCI-EdVGYxm5zUx4jsK0PKaihu0VyjKPZYO6jlE2njSfh9QzYxr1pyVSLFfGAi8fI_WdcvCqettS6veRkTp-llfGgDyexLdzUFN0SHKkzRjx06qGFOcxlGVcSNvQG-tHRGaxQ9EPDPAB6GG4z48ZfVrAxfOEYANtatdyyBg4Y_sAS4wvdfgQ2KG9EsNQAAAAB_nhrNAA", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/DevilsHeavenMF")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/FallenAssociation")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1356469075").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
