from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("24755516"))
API_HASH = getenv("f06b275511fff3403ddd75e0534cd48c")

BOT_TOKEN = getenv("6037166517:AAFPkF1XS4A8YNUIANf33u7JNidmkB58wVU", None)
DURATION_LIMIT = int(getenv("90", "90"))

OWNER_ID = int(getenv("1083660482"))

PING_IMG = getenv("PING_IMG", "https://daily.jstor.org/wp-content/uploads/2023/01/good_times_with_bad_music_1050x700.jpg")
START_IMG = getenv("START_IMG", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRZPoi5hp0YLqI5i6zY2HGXI5Bezabs2Xis6A&usqp=CAU")

SESSION = getenv("BQAjvNwGPR0k2fZ6EAQ_fWQeZmfnfjHA32gFk84pZ54wXSG_WjIgrhhP4wVW6Ifzqn2ZtCuoY6x4cW1EL2AYYFrG6o1w4YycmasifC5gYFHollX02Lslrxnq2RTlWljvICPAz86Xs_bJ0EokF48TAb-FLwTg788ovCUgasJonu-sPY2-_o0FItPyvhiI-naPgCVODCiiHA6XcR_qT3ytKL1mcVR6YB-fyTT_NfQ1irmJ-LVKyyLLRPFTN8vAlZ1EF9zmaE7j43Oh7vPxdV6uTyJzf6TaBPwVkqyabXgKDYRZmbdXJkf18gGg-IRbAK5h9y_NTvPo-_exQsv5QE2wNlinf54azQA", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/the_squaaad")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/about_faiz")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1083660482").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
