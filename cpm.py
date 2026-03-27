import os, sys, time, json, requests
from colorama import Fore, init, Style
from datetime import datetime
init(); #colorama start
# Telegram @abdulazizruziboev

##########################################################################################################################################
# VERIFICAÇÃO DE LICENÇA
##########################################################################################################################################
DATA_EXPIRACAO = "2026-04-12 23:59:59"

def verificar_expiracao():
    try:
        agora = datetime.now()
        expira_em = datetime.strptime(DATA_EXPIRACAO, "%Y-%m-%d %H:%M:%S")

        if agora > expira_em:
            print("\033[38;2;255;0;0m╔════════════════════════════════════╗\033[0m")
            print("\033[38;2;255;0;0m║       LICENÇA EXPIRADA!            ║\033[0m")
            print("\033[38;2;255;0;0m║   Entre em contato com o suporte    ║\033[0m")
            print("\033[38;2;255;0;0m║        @abdulazizruziboev           ║\033[0m")
            print("\033[38;2;255;0;0m╚════════════════════════════════════╝\033[0m")
            return False

        dias_restantes = (expira_em - agora).days
        horas_restantes = (expira_em - agora).seconds // 3600
        
        print("\033[38;2;0;255;0m╔════════════════════════════════════╗\033[0m")
        print("\033[38;2;0;255;0m║        CPM NEGO VIP - ATIVO        ║\033[0m")
        print(f"\033[38;2;255;255;0m║   Dias restantes: {dias_restantes:3d} dias           ║\033[0m")
        print(f"\033[38;2;255;255;0m║   Horas restantes: {horas_restantes:3d} horas          ║\033[0m")
        print("\033[38;2;0;255;0m║      @abdulazizruziboev            ║\033[0m")
        print("\033[38;2;0;255;0m╚════════════════════════════════════╝\033[0m")
        print("")
        time.sleep(2)
        return True
    except Exception as e:
        print(f"\033[38;2;255;0;0mErro na verificação: {e}\033[0m")
        return True  # Permite continuar em caso de erro de formatação

##########################################################################################################################################
##########################################################################################################################################
def pt(text, hex_color):
    hex_color = hex_color.lstrip('#')
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    ansi_code = f"\033[38;2;{r};{g};{b}m{text}\033[0m"
    print(ansi_code)

def cs():
    os.system('cls' if os.name == 'nt' else 'clear')
##########################################################################################################################################
##########################################################################################################################################
def choice_exit():
    cs()
    pt("/ You exit?","#ff0000")
    pt("| 0 - No", "#fff700")
    pt("\ 1 - Yes", "#ff0000")
    ei = input("➤ Enter choice: ")
    if ei.lower()=="0":
        cs()
        choice()
    elif ei.lower()=="1":
        cs()
        pt("Goodbye, 👋", "#ff0000")
        time.sleep(0.5)
        cs()
        sys.exit()
    else: 
        pt("Invalid choice", "#ff0000")
        cs()
        time.sleep(0.5)
        choice_exit()
def choice():
    cs()
    pt("/- @abdulazizruziboev","#ff00ff")
    pt("\- Choice Game","#ff00ff")
    pt("|- 1 - CPM1", "#fff700")
    pt("|- 2 - CPM2", "#fff700")
    pt("|- 0 - Exit", "#ff0000")
    chp = input("\- Enter choice: ")
    if chp.lower() == "0":
        choice_exit()
    elif chp.lower() == "1":
        cpmOne()
    elif chp.lower() == "2":
        cpmTwo()
    else:
        pt("Invalid choice", "#ff0000")
        time.sleep(0.5)
        cs()
        choice()
##########################################################################################################################################
##########################################################################################################################################
CPM1_FB_KEY = "AIzaSyBW1ZbMiUeDZHYUO2bY8Bfnf5rRgrQGPTM"
CPM1_INFO_API = "https://us-central1-cp-multiplayer.cloudfunctions.net/GetPlayerRecords2"
CPM1_RANK_API = "https://us-central1-cp-multiplayer.cloudfunctions.net/SetUserRating4"
##########################################################################################################################################
##########################################################################################################################################
def cpmOneReg():
    cs()
    pt("/ CPM 1 - Register New Account", "#03fc1c")
    oneEmail = input("|- Email: ")
    onePassword = input("|- Password: ")    
    api = f"https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={CPM1_FB_KEY}"
    payload = {'email': oneEmail, 'password': onePassword, 'returnSecureToken':True}
    try:
        response = requests.post(api, json=payload)
        response_data = response.json()
        if response.status_code == 200 and "idToken" in response_data:
            print("✅ Account Created")
            time.sleep(1)
            cpmOne()
            return response_data.get('idToken', None)
        else:
            print(f"❌ Account Not created: {response_data.get('error', {}).get('message', '404')}")
            time.sleep(1)
            cpmOne()
            return None
    except requests.exceptions.RequestException as e:
        print(f"⚠️ Request error: {e}")
        time.sleep(1)
        cpmOne()
        return None 
def cpmOneLogin():
    cs()
    pt("/ CPM 1 - Login Account", "#03fc1c")
    pt("|- Please first Logout Account via game!", "#ff0000")
    oneEmail = input("|- Email: ")
    onePassword = input("|- Password: ")

    url = f"https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key={CPM1_FB_KEY}"
    payload = {
        'email': oneEmail,
        'password': onePassword,
        'returnSecureToken': True
    }

    try:
        response = requests.post(url, json=payload)
        data = response.json()

        if response.status_code == 200 and "idToken" in data:
            oneToken = data["idToken"]
            pt("Login Successful.", "#00ff00")
            time.sleep(1)
            cpmOneServices(oneEmail, onePassword, oneToken)
            return oneToken
        else:
            pt(f"Error: {data.get('error', {}).get('message', 'Unknown error')}", "#ff0000")
            time.sleep(1)
            cpmOne()
            return None

    except requests.exceptions.RequestException as e:
        pt(f"Request error: {e}", "#ff0000")
        time.sleep(1)
        cpmOne()
        return None
def cpmOneAccountInfo(oneToken):
    headers = {
        "accept": "*/*",
        "content-type": "application/json",
        "accept-language": "ru",
        "user-agent": "com.aidana.cardriving.ios/4.8.9 iPhone/16.7.6 hw/iPhone10_6",
        "authorization": f"Bearer {oneToken}",
        "accept-encoding": "gzip, deflate, br"
    } 
    xx = {"data": "null"}

    try:
        a = requests.post(CPM1_INFO_API, headers=headers, json=xx)
        if a.status_code == 200:
            data = a.json()
            result_data = json.loads(data["result"])
            name = result_data.get("Name", "Noma'lum")
            localID = result_data.get("localID", "Noma'lum")
            money = result_data.get("money", 0)
            coin = result_data.get("coin", 0)
            return name, localID, money, coin
    except:
        pass
    return "Noma'lum", "Noma'lum", 0, 0
def cpmOneGetKingRank(oneToken):
    headers = {
        "accept": "*/*",
        "content-type": "application/json",
        "accept-language": "ru",
        "user-agent": "com.aidana.cardriving.ios/4.8.9 iPhone/16.7.6 hw/iPhone10_6",
        "authorization": f"Bearer {oneToken}",
        "accept-encoding": "gzip, deflate, br"
    }
    ratingData = {
        "data": "{\"RatingData\" : {\"t_distance\" : 2000000000,\"time\" : 2000000000,\"speed_banner\" : 2000000000,\"gifts\" : 2000000000,\"treasure\" : 2000000000,\"cars\" : 2000000000,\"race_win\" : 2000000000,\"levels\" : 2000000000,\"drift\" : 2000000000,\"run\" : 2000000000,\"police\" : 2000000000,\"block_post\" : 2000000000,\"real_estate\" : 2000000000,\"fuel\" : 2000000000,\"car_trade\" : 2000000000,\"car_exchange\" : 2000000000,\"burnt_tire\" : 2000000000,\"car_fix\" : 2000000000,\"car_wash\" : 2000000000,\"offroad\" : 2000000000,\"passanger_distance\" : 2000000000,\"reactions\" : 2000000000,\"drift_max\" : 2000000000,\"taxi\" : 2000000000,\"delivery\" : 2000000000,\"cargo\" : 2000000000,\"push_ups\" : 2000000000,\"slicer_cut\" : 2000000000,\"car_collided\" : 2000000000,\"new_type\" : 2000000000}}"
    }
    cs()
    pt("/ Applying King Rank...", "#00ffff")
    try:
        a = requests.post(CPM1_RANK_API, headers=headers, json=ratingData)
        if a.status_code == 200:
            pt("King Rank Applied Successfully!", "#00ff00")
        else:
            pt(f"Error: {a.text}", "#ff0000")
        time.sleep(2)
    except requests.exceptions.RequestException as e:
        pt(f"Request error: {e}", "#ff0000")
        time.sleep(2)
def cpmOneChangeEmail(oneToken,onePassword):
    cs()
    pt("/ CPM 1 - Change Email", "#03fc1c")
    oneOldEmail = input("|- Current Email: ")
    oneNewEmail = input("|- New Email: ")
    if not oneOldEmail or not onePassword or not oneNewEmail:
        pt("❌ Fill all fields!", "#ff0000")
        time.sleep(1)
        return
    FIREBASE_LOGIN_URL = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={CPM1_FB_KEY}"
    FIREBASE_UPDATE_URL = f"https://identitytoolkit.googleapis.com/v1/accounts:update?key={CPM1_FB_KEY}"
    auth_res = requests.post(FIREBASE_LOGIN_URL, json={
        "email": oneOldEmail,
        "password": onePassword,
        "returnSecureToken": True
    })
    auth_data = auth_res.json()

    if "idToken" not in auth_data:
        pt(f"❌ Auth failed: {auth_data.get('error', {}).get('message', 'Unknown error')}", "#ff0000")
        time.sleep(1)
        return
    id_token = auth_data["idToken"]
    update_res = requests.post(FIREBASE_UPDATE_URL, json={ "idToken": id_token, "email": oneNewEmail, "returnSecureToken": True })
    update_data = update_res.json()
    if "email" in update_data:
        pt(f"✅ Email changed successfully! New Email: {update_data['email']}", "#00ff00")
        time.sleep(1)
    else:
        pt(f"❌ Error changing email: {update_data.get('error', {}).get('message', 'Unknown error')}", "#ff0000")
        time.sleep(1)
def cpmOneChangePassword(oneToken):
    cs()
    pt("/ CPM 1 - Change Password", "#03fc1c")
    oneOldPassword = input("|- Current Password: ")
    oneNewPassword = input("|- New Password: ")
    if not oneOldPassword or not oneNewPassword:
        pt("❌ Fill all fields!", "#ff0000")
        time.sleep(1)
        return

    FIREBASE_UPDATE_URL = f"https://identitytoolkit.googleapis.com/v1/accounts:update?key={CPM1_FB_KEY}"

    
    update_res = requests.post(FIREBASE_UPDATE_URL, json={
        "idToken": oneToken,
        "password": oneNewPassword,
        "returnSecureToken": True
    })
    update_data = update_res.json()

    if "passwordHash" in update_data:
        pt(f"Password changed successfully!", "#00ff00")
        time.sleep(1)
    else:
        pt(f"Error changing password: {update_data.get('error', {}).get('message', 'Unknown error')}", "#ff0000")
        time.sleep(1)
def cpmOneDeleteAccount(oneToken):
    cs()
    pt("/ CPM 1 - Delete Account", "#ff0000")
    confirm = input("|- Are you sure you want to DELETE this account? (yes/no): ").lower()
    if confirm != "yes":
        pt("Account deletion cancelled!", "#fff700")
        time.sleep(1)
        return

    FIREBASE_DELETE_URL = f"https://identitytoolkit.googleapis.com/v1/accounts:delete?key={CPM1_FB_KEY}"

    # delete account using idToken
    delete_res = requests.post(FIREBASE_DELETE_URL, json={
        "idToken": oneToken
    })
    delete_data = delete_res.json()

    if delete_res.status_code == 200:
        pt("Account deleted successfully!", "#00ff00")
        time.sleep(1)
        cs()
        cpmOne()
    else:
        pt(f"❌ Error deleting account: {delete_data.get('error', {}).get('message', 'Unknown error')}", "#ff0000")
        time.sleep(1)
def cpmOne():
    cs()
    pt("/ CPM 1 - Choice", "#03fc1c")
    pt("|- 1 - Login","#fcfc03")
    pt("|- 2 - Register","#fcfc03")
    pt("|- 0 - Exit","#fc0320")
    c1c = input("\- Enter choice: ")
    if c1c.lower() == "0":
        cs()
        choice()
    elif c1c.lower() == "1":
        cs()
        cpmOneLogin()
    elif c1c.lower() == "2":
        cs()
        cpmOneReg()
    else:
        pt("Invalid choice", "#ff0000")
        cs()
        time.sleep(0.5)
        cpmOne()
def cpmOneServices(oneEmail, onePassword, oneToken):
    while True:    
        try:
            name, localID, money, coin = cpmOneAccountInfo(oneToken)
        except:
            name, localID, money, coin = "Noma'lum", "Noma'lum", 0, 0
        
        cs()
        pt("__________________________________________", "#a200ff")
        pt("\      CPM 1 - by @abdulazizruziboev     /", "#a200ff")
        pt(" ----------------------------------------","#a200ff")
        pt("/ Account Info", "#fff700")
        pt(f"\_Email     | {oneEmail}","#00ff00")
        pt(f"\_Password  | {onePassword}","#00ff00")
        pt(f"\_Name      | {name}","#00ff00")
        pt(f"\_LocalID   | {localID}","#00ff00")
        pt(f"\_Money     | {money}","#00ff00")
        pt(f"\_Coin      | {coin}","#00ff00")
        pt("/--------------------------------------\\","#a200ff")
        pt("\--------------------------------------/","#a200ff")
        pt("/ Services","#fff700")
        pt("\_1 - King Rank","#00ff00")
        pt("\_2 - Change Email","#00ff00")
        pt("\_3 - Change Password","#00ff00")
        pt("\_4 - Delete Account","#00ff00")
        pt("\_0 - Exit Script","#ff0000")
        cpmOneCommand = input("\_Enter choice: ")
        if cpmOneCommand.lower()=="0":
            cs()
            sys.exit()
        if cpmOneCommand.lower()=="1":
            cs()
            cpmOneGetKingRank(oneToken)
        if cpmOneCommand.lower()=="2":
            cs()
            cpmOneChangeEmail(oneToken,onePassword)
        if cpmOneCommand.lower()=="3":
            cs()
            cpmOneChangePassword(oneToken)
        if cpmOneCommand.lower()=="4":
            cs()
            cpmOneDeleteAccount(oneToken)
##########################################################################################################################################
##########################################################################################################################################
CPM2_FB_KEY = "AIzaSyCQDz9rgjgmvmFkvVfmvr2-7fT4tfrzRRQ"
CPM2_RANK_API = "https://us-central1-cpm-2-7cea1.cloudfunctions.net/SetUserRating17"
##########################################################################################################################################
##########################################################################################################################################
def cpmTwoReg():
    cs()
    pt("/ CPM 2 - Register New Account", "#03fc1c")
    twoEmail = input("|- Email: ")
    twoPassword = input("|- Password: ")    
    api = f"https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={CPM2_FB_KEY}"
    payload = {'email': twoEmail, 'password': twoPassword, 'returnSecureToken':True}
    try:
        response = requests.post(api, json=payload)
        response_data = response.json()
        if response.status_code == 200 and "idToken" in response_data:
            print("✅ Account Created")
            time.sleep(1)
            cpmTwo()
            return response_data.get('idToken', None)
        else:
            print(f"❌ Account Not created: {response_data.get('error', {}).get('message', '404')}")
            time.sleep(1)
            cpmTwo()
            return None
    except requests.exceptions.RequestException as e:
        print(f"⚠️ Request error: {e}")
        time.sleep(1)
        cpmTwo()
        return None 
def cpmTwoLogin():
    cs()
    pt("/ CPM 2 - Login Account", "#03fc1c")
    pt("|- Please first Logout Account via game!", "#ff0000")
    twoEmail = input("|- Email: ")
    twoPassword = input("|- Password: ")

    url = f"https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key={CPM2_FB_KEY}"
    payload = {
        'email': twoEmail,
        'password': twoPassword,
        'returnSecureToken': True
    }

    try:
        response = requests.post(url, json=payload)
        data = response.json()

        if response.status_code == 200 and "idToken" in data:
            twoToken = data["idToken"]
            pt("Login Successful.", "#00ff00")
            time.sleep(1)
            cpmTwoServices(twoEmail, twoPassword, twoToken)
            return twoToken
        else:
            pt(f"Error: {data.get('error', {}).get('message', 'Unknown error')}", "#ff0000")
            time.sleep(1)
            cpmTwo()
            return None

    except requests.exceptions.RequestException as e:
        pt(f"Request error: {e}", "#ff0000")
        time.sleep(1)
        cpmTwo()
        return None

def cpmTwoGetKingRank(twoToken):
    headers = {
        "accept": "*/*",
        "content-type": "application/json",
        "accept-language": "ru",
        "user-agent": "com.aidana.cardriving.ios/4.8.9 iPhone/16.7.6 hw/iPhone10_6",
        "authorization": f"Bearer {twoToken}",
        "accept-encoding": "gzip, deflate, br"
    }
    ratingData = {
        "data": "{\"RatingData\" : {\"t_distance\" : 2000000000,\"time\" : 2000000000,\"speed_banner\" : 2000000000,\"gifts\" : 2000000000,\"treasure\" : 2000000000,\"cars\" : 2000000000,\"race_win\" : 2000000000,\"levels\" : 2000000000,\"drift\" : 2000000000,\"run\" : 2000000000,\"police\" : 2000000000,\"block_post\" : 2000000000,\"real_estate\" : 2000000000,\"fuel\" : 2000000000,\"car_trade\" : 2000000000,\"car_exchange\" : 2000000000,\"burnt_tire\" : 2000000000,\"car_fix\" : 2000000000,\"car_wash\" : 2000000000,\"offroad\" : 2000000000,\"passanger_distance\" : 2000000000,\"reactions\" : 2000000000,\"drift_max\" : 2000000000,\"taxi\" : 2000000000,\"delivery\" : 2000000000,\"cargo\" : 2000000000,\"push_ups\" : 2000000000,\"slicer_cut\" : 2000000000,\"car_collided\" : 2000000000,\"new_type\" : 2000000000}}"
    }
    cs()
    pt("/ Applying King Rank...", "#00ffff")
    try:
        a = requests.post(CPM2_RANK_API, headers=headers, json=ratingData)
        if a.status_code == 200:
            pt("King Rank Applied Successfully!", "#00ff00")
        else:
            pt(f"❌ Error: {a.text}", "#ff0000")
        time.sleep(2)
    except requests.exceptions.RequestException as e:
        pt(f"Request error: {e}", "#ff0000")
        time.sleep(2)
def cpmTwoChangeEmail(twoToken,twoPassword):
    cs()
    pt("/ CPM 2 - Change Email", "#03fc1c")
    twoOldEmail = input("|- Current Email: ")
    twoNewEmail = input("|- New Email: ")
    if not twoOldEmail or not twoPassword or not twoNewEmail:
        pt("❌ Fill all fields!", "#ff0000")
        time.sleep(1)
        return
    FIREBASE_LOGIN_URL = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={CPM2_FB_KEY}"
    FIREBASE_UPDATE_URL = f"https://identitytoolkit.googleapis.com/v1/accounts:update?key={CPM2_FB_KEY}"
    auth_res = requests.post(FIREBASE_LOGIN_URL, json={
        "email": twoOldEmail,
        "password": twoPassword,
        "returnSecureToken": True
    })
    auth_data = auth_res.json()

    if "idToken" not in auth_data:
        pt(f"❌ Auth failed: {auth_data.get('error', {}).get('message', 'Unknown error')}", "#ff0000")
        time.sleep(1)
        return
    id_token = auth_data["idToken"]
    update_res = requests.post(FIREBASE_UPDATE_URL, json={ "idToken": id_token, "email": twoNewEmail, "returnSecureToken": True })
    update_data = update_res.json()
    if "email" in update_data:
        pt(f"✅ Email changed successfully! New Email: {update_data['email']}", "#00ff00")
        time.sleep(1)
    else:
        pt(f"❌ Error changing email: {update_data.get('error', {}).get('message', 'Unknown error')}", "#ff0000")
        time.sleep(1)
def cpmTwoChangePassword(twoToken):
    cs()
    pt("/ CPM 2 - Change Password", "#03fc1c")
    twoOldPassword = input("|- Current Password: ")
    twoNewPassword = input("|- New Password: ")
    if not twoOldPassword or not twoNewPassword:
        pt("❌ Fill all fields!", "#ff0000")
        time.sleep(1)
        return

    FIREBASE_UPDATE_URL = f"https://identitytoolkit.googleapis.com/v1/accounts:update?key={CPM2_FB_KEY}"

    
    update_res = requests.post(FIREBASE_UPDATE_URL, json={
        "idToken": twoToken,
        "password": twoNewPassword,
        "returnSecureToken": True
    })
    update_data = update_res.json()

    if "passwordHash" in update_data:
        pt(f"Password changed successfully!", "#00ff00")
        time.sleep(1)
    else:
        pt(f"Error changing password: {update_data.get('error', {}).get('message', 'Unknown error')}", "#ff0000")
        time.sleep(1)
def cpmTwoDeleteAccount(twoToken):
    cs()
    pt("/ CPM 2 - Delete Account", "#ff0000")
    confirm = input("|- Are you sure you want to DELETE this account? (yes/no): ").lower()
    if confirm != "yes":
        pt("Account deletion cancelled!", "#fff700")
        time.sleep(1)
        return

    FIREBASE_DELETE_URL = f"https://identitytoolkit.googleapis.com/v1/accounts:delete?key={CPM2_FB_KEY}"

    # delete account using idToken
    delete_res = requests.post(FIREBASE_DELETE_URL, json={
        "idToken": twoToken
    })
    delete_data = delete_res.json()

    if delete_res.status_code == 200:
        pt("Account deleted successfully!", "#00ff00")
        time.sleep(1)
        cs()
        cpmTwo()
    else:
        pt(f"❌ Error deleting account: {delete_data.get('error', {}).get('message', 'Unknown error')}", "#ff0000")
        time.sleep(1)
def cpmTwo():
    cs()
    pt("/ CPM 2 - Choice", "#03fc1c")
    pt("|- 1 - Login","#fcfc03")
    pt("|- 2 - Register","#fcfc03")
    pt("|- 0 - Exit","#fc0320")
    c2c = input("\- Enter choice: ")
    if c2c.lower() == "0":
        cs()
        choice()
    elif c2c.lower() == "1":
        cs()
        cpmTwoLogin()
    elif c2c.lower() == "2":
        cs()
        cpmTwoReg()
    else:
        pt("Invalid choice", "#ff0000")
        cs()
        time.sleep(0.5)
        cpmTwo()
def cpmTwoServices(twoEmail, twoPassword, twoToken):
    while True:    
        cs()
        pt("__________________________________________", "#a200ff")
        pt("\      CPM 2 - by @abdulazizruziboev     /", "#a200ff")
        pt(" ----------------------------------------","#a200ff")
        pt("/ Account Info", "#fff700")
        pt(f"\_Email     | {twoEmail}","#00ff00")
        pt(f"\_Password  | {twoPassword}","#00ff00")
        pt("/--------------------------------------\\","#a200ff")
        pt("\--------------------------------------/","#a200ff")
        pt("/ Services","#fff700")
        pt("\_1 - King Rank","#00ff00")
        pt("\_2 - Change Email","#00ff00")
        pt("\_3 - Change Password","#00ff00")
        pt("\_4 - Delete Account","#00ff00")
        pt("\_0 - Exit Script","#ff0000")
        cpmTwoCommand = input("\_Enter choice: ")
        if cpmTwoCommand.lower()=="0":
            cs()
            sys.exit()
        if cpmTwoCommand.lower()=="1":
            cs()
            cpmTwoGetKingRank(twoToken)
        if cpmTwoCommand.lower()=="2":
            cs()
            cpmTwoChangeEmail(twoToken,twoPassword)
        if cpmTwoCommand.lower()=="3":
            cs()
            cpmTwoChangePassword(twoToken)
        if cpmTwoCommand.lower()=="4":
            cs()
            cpmTwoDeleteAccount(twoToken)
#loop_main
if __name__ == '__main__':
    if verificar_expiracao():
        choice()