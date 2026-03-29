world_champions = {
    2002: 'Бразилия',
    2006: 'Италия',
    2010: 'Испания',
    2014: 'Германия',
    2018: 'Франция',
}

world_champions[2022] = 'Аргентина'
country = 'Италия'
for year, champion in world_champions.items():
    print(f'{year} - {champion}')
if country in world_champions.values():
    for year, champion in world_champions.items():
      if champion == country:
        print(f'Италия стала чемпионом мира по футболу в 21 веке в {year} году.')
      else:
        print(f'Италия не выигрывала чемпионат мира по футболу в 21 веке.', year)


