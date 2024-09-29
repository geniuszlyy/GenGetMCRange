# EN
**GenGetMCRange** - A simple and efficient minecraft server scanner that fetches and displays IP addresses of Minecraft servers listed on `minecraft-mp.com`. The script asynchronously scrapes the server information and performs scans on subdomains to find active IP addresses.

## Features

- **Async Scraping:** Uses `aiohttp` for non-blocking, asynchronous scraping of server data.
- **Server Scanning:** Gathers server information, including IP addresses, and checks subdomains for active servers.
- **Customizable Subdomain List:** The script comes with a pre-defined list of subdomains but can be customized as needed.

## Requirements

- Python 3.8+
- Libraries:
  - `aiohttp`
  - `beautifulsoup4`
  - `colorama`

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/geniuszly/GenGetMCRange
   ```
2. Navigate to the project directory:
   ```bash
   cd GenGetMCRange
   ```
3. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
    ```

## Usage
1. Run the script:
   ```bash
   python main.py
    ```
2. The script will start fetching and displaying Minecraft server information. It will output color-coded server IP addresses and other data to the console.
3. Example output:
   ```arduino
   >> [OVH] => 192.168.0.*
    Command: screen -S <session_id> nmap -p 1-20,23-79,81-110,112-65535 -T5 -A -v -Pn --min-hostgroup 8 --max-hostgroup 8 --open -oN /root/<output_file>.txt 192.168.0.*
    ```

![image](https://github.com/user-attachments/assets/e9f1f0a5-3036-4580-8c15-a95a8a1f36b4)


# RU
**GenGetMCRange** - Простой и эффективный сканер серверов minecraft, который получает и отображает IP-адреса серверов Minecraft, зарегистрированных на minecraft-mp.com. Скрипт асинхронно собирает информацию о серверах и выполняет сканирование поддоменов для поиска активных IP-адресов.

## Особенности

- **Асинхронный Парсинг:** Используется `aiohttp` для неблокирующего асинхронного парсинга данных о серверах.
- **Сканирование Серверов:** Получает информацию о серверах, включая IP-адреса, и проверяет поддомены на наличие активных серверов.
- **Настраиваемый Список Поддоменов:** Скрипт поставляется с предопределенным списком поддоменов, но может быть изменен по необходимости.

## Требования

- Python 3.8+
- Библиотеки:
  - `aiohttp`
  - `beautifulsoup4`
  - `colorama`

## Установка

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/geniuszly/GenGetMCRange
   ```
2. Перейдите в папку проекта:
   ```bash
   cd GenGetMCRange
   ```
3. Установите необходимые Python-пакеты:
   ```bash
   pip install -r requirements.txt
    ```

## Использование
1. Запустите скрипт:
   ```bash
   python main.py
    ```
2. Скрипт начнет собирать и отображать информацию о серверах Minecraft. В консоли будет выводиться цветная информация об IP-адресах серверов и другие данные.
3. Пример вывода:
   ```arduino
   >> [OVH] => 192.168.0.*
    Команда: screen -S <session_id> nmap -p 1-20,23-79,81-110,112-65535 -T5 -A -v -Pn --min-hostgroup 8 --max-hostgroup 8 --open -oN /root/<output_file>.txt 192.168.0.*
    ```

![image](https://github.com/user-attachments/assets/bacfa01d-c34d-47ce-9c0a-1e8551f8e246)
