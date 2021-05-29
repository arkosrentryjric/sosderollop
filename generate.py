import requests, json, random

f = open("./README.md", "w")
pokemon_id = random.randint(1, 151)
res = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}')
result = json.loads(res.text)
f.write(f'''
<p align="center">
    <img src="{result['sprites']['front_default']}" width="150" height="150">
</p>
<h3 align="center">You have been greeted by a wild <b>{result['name'].title()}</b></h3>
<h3 align="center">Have a nice day!</h3>
<p align="center">
  <a href="https://github.com/HermanSoukup">
    <img alt="GitHub Stats" src="https://github-readme-stats.vercel.app/api?username=HermanSoukup&hide=issues&hide_title=true&include_all_commits=true&bg_color=30,e96443,904e95&title_color=fff&text_color=fff" />
    </a>
</p>
<p align="center">

[![GitHub release (latest by date)](https://img.shields.io/github/v/release/HermanSoukup/Nano-Openwrt?style=for-the-badge&label=Download)](https://github.com/HermanSoukup/Nano-Openwrt/releases)

</p>       
''')
f.close()
