import asyncio
import aiohttp
from bs4 import BeautifulSoup
import random
import json
import os
from colorama import Fore, init
import logging

# Инициализация colorama
init(autoreset=True)

# Настройка логирования
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

# Логотип и хелпа
print(f"""
{Fore.LIGHTRED_EX}
                   _____             _____      _   __  __  _____ _____                        
                  / ____|           / ____|    | | |  \/  |/ ____|  __ \                       
                 | |  __  ___ _ __ | |  __  ___| |_| \  / | |    | |__) |__ _ _ __   __ _  ___ 
                 | | |_ |/ _ \ '_ \| | |_ |/ _ \ __| |\/| | |    |  _  // _` | '_ \ / _` |/ _ \\
                 | |__| |  __/ | | | |__| |  __/ |_| |  | | |____| | \ \ (_| | | | | (_| |  __/
                  \_____|\___|_| |_|\_____|\___|\__|_|  |_|\_____|_|  \_\__,_|_| |_|\__, |\___|
                                                                                     __/ |     
                                                                                    |___/     
{Fore.LIGHTBLUE_EX}
                                        Парсер серверов Minecraft
                                       Использование: python {os.path.basename(__file__)}
              сканирует и показывает IP-адреса серверов Minecraft с сайта minecraft-mp.com
                                        Пример: python {os.path.basename(__file__)}
                                             {Fore.LIGHTYELLOW_EX}by geniuszly
""")

SUBDOMAINS = [
    "www", "build", "web", "dev", "staff", "mc", "play", "sys", "node1", "node2",
    "node3", "node4", "node5", "node6", "node7", "node8", "node9", "node10",
    "node11", "node12", "node13", "node14", "node15", "node16", "node17",
    "node18", "node19", "node20", "node001", "node002", "node01", "node02",
    "node003", "sys001", "sys002", "go", "admin", "eggwars", "bedwars", "lobby1",
    "hub", "builder", "developer", "test", "test1", "forum", "bans", "baneos",
    "ts", "ts3", "sys1", "sys2", "mods", "bungee", "bungeecord", "array", "spawn",
    "server", "help", "client", "api", "smtp", "s1", "s2", "s3", "s4", "server1",
    "server2", "jugar", "login", "mysql", "phpmyadmin", "demo", "na", "eu", "us",
    "es", "fr", "it", "ru", "support", "developing", "discord", "backup", "buy",
    "buycraft", "dedicado1", "dedi", "dedi1", "dedi2", "dedi3", "minecraft",
    "prueba", "pruebas", "ping", "register", "cdn", "stats", "store", "serie",
    "buildteam", "info", "host", "jogar", "proxy", "vps", "ovh", "partner",
    "partners", "appeals", "appeal", "store-assets", "builds", "testing",
    "server", "pvp", "skywars", "survival", "skyblock", "lobby", "hg", "games",
    "sys001", "sys002", "node001", "node002", "games001", "games002", "us1",
    "us2", "us3", "us4", "us5", "goliathdev", "staticassets", "rewards", "rpsrv",
    "ftp", "ssh", "web", "jobs", "render", "sadre"
]

def clean_domain(domain):
    """Очистка домена от нежелательных частей."""
    prefixes = ["play.", "mc.", "lobby.", "hub.", "eu.", "jogar.", "loja.", "fun.", "mp.", "oyna."]
    for prefix in prefixes:
        domain = domain.replace(prefix, "")
    return domain.replace("pixel", "").strip()

async def get_ip_data(session, domain):
    """Получение информации об IP из API асинхронно."""
    try:
        async with session.get(f'https://api.mcsrvstat.us/2/{domain}') as response:
            if response.headers['Content-Type'] != 'application/json':
                #logging.warning(f"Неверный тип содержимого для домена {domain}")
                return None, None
            data = await response.json()
            return data.get('ip'), data.get('players', {}).get('online', 0)
    except aiohttp.ClientError as e:
        logging.error(f"Ошибка при получении данных для домена {domain}: {e}")
        return None, None
    except json.JSONDecodeError as e:
        logging.error(f"Ошибка при декодировании JSON для домена {domain}: {e}")
        return None, None

async def main():
    visited_ips = set()
    async with aiohttp.ClientSession() as session:
        for _ in range(20):
            screen_id = random.randint(100000000, 999999999)
            txt_id = random.randint(100000000, 999999999)
            page_num = random.randint(1, 5)
            selected_server = random.randint(0, 24)

            # Получение списка серверов
            url = f"https://minecraft-mp.com/servers/list/{page_num}/"
            headers = {"User-Agent": "Mozilla/5.0"}
            try:
                async with session.get(url, headers=headers) as response:
                    if response.status != 200:
                        logging.warning(f"Не удалось получить данные со страницы {page_num}")
                        continue
                    soup = BeautifulSoup(await response.text(), 'html.parser')
            except aiohttp.ClientError as e:
                logging.error(f"Ошибка при подключении к {url}: {e}")
                continue

            server_rows = soup.find_all('tr', height='90')
            if not server_rows:
                logging.warning(f"Не найдено серверов на странице {page_num}")
                continue

            # Получение IP адреса выбранного сервера
            server_row = server_rows[selected_server]
            ip_address = server_row.find_all('td')[1].find('strong').text.split(':')[0].strip()
            cleaned_domain = clean_domain(ip_address.lower())

            tasks = []
            for subdomain in SUBDOMAINS:
                full_domain = f"{subdomain}.{cleaned_domain}"
                tasks.append(get_ip_data(session, full_domain))

            try:
                results = await asyncio.gather(*tasks)
            except asyncio.CancelledError:
                logging.warning("Выполнение было прервано")
                return

            for ip, _ in results:
                if ip and ip.split('.')[0] != "104":
                    masked_ip = '.'.join(ip.split('.')[:3]) + '.*'
                    if masked_ip not in visited_ips:
                        visited_ips.add(masked_ip)
                        kind = "OVH" if "1" in ip else "TBH" if "2" in ip else "CTB" if "0" in ip else "GDD"
                        print(f"{Fore.MAGENTA}[{Fore.BLUE}>>{Fore.MAGENTA}] [{Fore.YELLOW}{kind}{Fore.MAGENTA}] => {Fore.GREEN}{masked_ip}")
                        print(f"Команда: {Fore.BLUE}screen -S {screen_id} nmap -p 1-20,23-79,81-110,112-65535 -T5 -A -v -Pn --min-hostgroup 8 --max-hostgroup 8 --open -oN /root/{txt_id}.txt {masked_ip}\n")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Программа была прервана пользователем")
