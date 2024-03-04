const axios = require('axios');
const fs = require('fs');

const proxies = [];
const output_file = 'proxy.txt';

if (fs.existsSync(output_file)) {
  fs.unlinkSync(output_file);
  console.log(`'${output_file}' telah dihapus.`);
}

const raw_proxy_sites = [
  'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt',
  'https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt',
  'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt',
'https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt',
'https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt',
'https://raw.githubusercontent.com/opsxcq/proxy-list/master/list.txt',
'https://raw.githubusercontent.com/saisuiu/Lionkings-Http-Proxys-Proxies/main/cnfree.txt',
'https://raw.githubusercontent.com/officialputuid/KangProxy/KangProxy/http/http.txt',
'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt',
'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies_anonymous/socks4.txt',
'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt',
'https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/socks5.txt',
'https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/socks5.txt',
'https://raw.githubusercontent.com/prxchk/proxy-list/main/socks5.txt',
'https://raw.githubusercontent.com/ALIILAPRO/Proxy/main/socks5.txt',
'https://spys.me/socks.txt',
'https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt',
'https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt',
'https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/HTTP.txt',
'https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt',
'https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt',
'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt',
'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt',
'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt',
'https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/http.txt',
'https://raw.githubusercontent.com/mallisc5/master/proxy-list-raw.txt',
'https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/http.txt',
'https://raw.githubusercontent.com/prxchk/proxy-list/main/http.txt',
'https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt',
'https://raw.githubusercontent.com/saisuiu/Lionkings-Http-Proxys-Proxies/main/free.txt',
'https://raw.githubusercontent.com/HyperBeats/proxy-list/main/https.txt',
'https://raw.githubusercontent.com/UptimerBot/proxy-list/main/proxies/http.txt',
'https://raw.githubusercontent.com/caliphdev/Proxy-List/master/http.txt',
'https://raw.githubusercontent.com/proxylist-to/proxy-list/main/http.txt',
'https://raw.githubusercontent.com/zloi-user/hideip.me/main/https.txt',
'https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt',
'https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/https.txt',
'https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt',
'https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/protocols/http/data.txt',
'https://raw.githubusercontent.com/tuanminpay/live-proxy/master/http.txt',
'https://raw.githubusercontent.com/casals-ar/proxy-list/main/https',
'https://raw.githubusercontent.com/casals-ar/proxy-list/main/http',
'https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/http.txt',
'https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/https.txt',
'https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt',
'https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt',
'https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/proxy_files/http_proxies.txt',
'https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/proxy_files/https_proxies.txt',
'https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt',
'https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt',
'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/proxy.txt',
'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt',
'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt',
'http://atomintersoft.com/proxy_list_port_80',
'http://atomintersoft.com/proxy_list_domain_org',
'http://atomintersoft.com/proxy_list_port_3128',
'https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/http.txt',
'https://raw.githubusercontent.com/mallisc5/master/proxy-list-raw.txt',
'https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/http.txt',
'https://raw.githubusercontent.com/prxchk/proxy-list/main/http.txt',
'https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt',
'https://raw.githubusercontent.com/saisuiu/Lionkings-Http-Proxys-Proxies/main/free.txt',
'https://raw.githubusercontent.com/HyperBeats/proxy-list/main/https.txt',
'https://raw.githubusercontent.com/UptimerBot/proxy-list/main/proxies/http.txt',
'https://raw.githubusercontent.com/caliphdev/Proxy-List/master/http.txt',
'https://raw.githubusercontent.com/proxylist-to/proxy-list/main/http.txt',
'https://raw.githubusercontent.com/zloi-user/hideip.me/main/https.txt',
'https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt',
'https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/https.txt',
'https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt',
'https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/protocols/http/data.txt',
'https://raw.githubusercontent.com/tuanminpay/live-proxy/master/http.txt',
'https://raw.githubusercontent.com/casals-ar/proxy-list/main/https',
'https://raw.githubusercontent.com/casals-ar/proxy-list/main/http',
'https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/http.txt',
'https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/https.txt',
'https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt',
'https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt',
'https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/proxy_files/http_proxies.txt',
'https://raw.githubusercontent.com/Anonym0usWork1221/Free-Proxies/main/proxy_files/https_proxies.txt',
'https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt',
'https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt',
'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/proxy.txt',
'https://openproxy.space/list/http',
'http://olaf4snow.com/public/proxy.txt',
'http://inav.chat.ru/ftp/proxy.txt',
'https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt',
'https://raw.githubusercontent.com/yuceltoluyag/GoodProxy/main/raw.txt',
'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt',
'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt',
'https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt',
'https://proxyspace.pro/http.txt',
'https://api.proxyscrape.com/?request=displayproxies&proxytype=http',
'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt',
'http://worm.rip/http.txt',
'http://worm.rip/https.txt',
'http://alexa.lr2b.com/proxylist.txt',
'https://api.openproxylist.xyz/http.txt',
'http://rootjazz.com/proxies/proxies.txt',
'https://multiproxy.org/txt_all/proxy.txt',
'https://proxy-spider.com/api/proxies.example.txt',
'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt',
'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies.txt',
'https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt',
'https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt',
'https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt',
'https://raw.githubusercontent.com/opsxcq/proxy-list/master/list.txt',
'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all',
'https://www.proxydocker.com/en/proxylist/download?email=noshare&country=all&city=all&port=all&type=all&anonymity=all&state=all&need=all',
'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=anonymous'
];

async function fetchProxies() {
  for (const site of raw_proxy_sites) {
    try {
      const response = await axios.get(site);
      const lines = response.data.split('\n');
      for (const line of lines) {
        if (line.includes(':')) {
          const [ip, port] = line.split(':', 2);
          proxies.push(`${ip}:${port}`);
        }
      }
    } catch (error) {
      console.error(`Gagal mengambil proxy dari ${site}: ${error.message}`);
    }
  }

  fs.writeFileSync(output_file, proxies.join('\n'));
  console.log(`Proxies berhasil diambil dan disimpan dalam ${output_file}`);
}

fetchProxies();
