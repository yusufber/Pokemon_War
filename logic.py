import aiohttp  # Eşzamansız HTTP istekleri için bir kütüphane
import random
import asyncio

class Pokemon:
    pokemons = {}
    # Nesne başlatma (kurucu)
    def __init__(self, pokemon_trainer):
        self.pokemon_trainer = pokemon_trainer
        self.pokemon_number = random.randint(1, 1000)
        self.name = None
        if pokemon_trainer not in Pokemon.pokemons:
            Pokemon.pokemons[pokemon_trainer] = self
        else:
            self = Pokemon.pokemons[pokemon_trainer]

    async def get_name(self):
        # PokeAPI aracılığıyla bir pokémonun adını almak için asenktron metot
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'  # İstek için URL API
        async with aiohttp.ClientSession() as session:  #  HTTP oturumu açma
            async with session.get(url) as response:  # GET isteği gönderme
                if response.status == 200:
                    data = await response.json()  # JSON yanıtının alınması ve çözümlenmesi
                    return data['forms'][0]['name']  #  Pokémon adını döndürme
                else:
                    return "Pikachu"  # İstek başarısız olursa varsayılan adı döndürür

    async def info(self):
        # Pokémon hakkında bilgi döndüren bir metot
        if not self.name:
            self.name = await self.get_name()# Henüz yüklenmemişse bir adın geri alınması
            self.attack=await self.get_attack()
            self.hp=await self.get_hp()
            self.defense=await self.get_defense()
            
        return f"Pokémonunuzun ismi: {self.name}"  # Pokémon adını içeren dizeyi döndürür

    async def show_img(self):
        # PokeAPI aracılığıyla bir pokémon görüntüsünün URL'sini almak için asenktron metot
        # PokeAPI aracılığıyla bir pokémonun adını almak için asenktron metot
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'  # İstek için URL API
        async with aiohttp.ClientSession() as session:  #  HTTP oturumu açma
            async with session.get(url) as response:  # GET isteği gönderme
                if response.status == 200:
                    data = await response.json()  # JSON yanıtının alınması ve çözümlenmesi
                    return data['sprites']['front_default']  #  Pokémon adını döndürme
                else:
                    return "Pikachu"  # İstek başarısız olursa varsayılan adı döndürür
                

    async def get_hp(self):
        # PokeAPI aracılığıyla bir pokémonun adını almak için asenktron metot
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'  # İstek için URL API
        async with aiohttp.ClientSession() as session:  #  HTTP oturumu açma
            async with session.get(url) as response:  # GET isteği gönderme
                if response.status == 200:
                    data = await response.json()  # JSON yanıtının alınması ve çözümlenmesi
                    return data['stats'][0]['base_stat']  #  Pokémon adını döndürme
                else:
                    return 50  # İstek başarısız olursa varsayılan adı döndürür
    



    async def get_attack(self):
        # PokeAPI aracılığıyla bir pokémonun adını almak için asenktron metot
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'  # İstek için URL API
        async with aiohttp.ClientSession() as session:  #  HTTP oturumu açma
            async with session.get(url) as response:  # GET isteği gönderme
                if response.status == 200:
                    data = await response.json()  # JSON yanıtının alınması ve çözümlenmesi
                    return data['stats'][1]['base_stat']  #  Pokémon adını döndürme
                else:
                    return 50  # İstek başarısız olursa varsayılan adı döndürür
                



    async def get_defense(self):
        # PokeAPI aracılığıyla bir pokémonun adını almak için asenktron metot
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'  # İstek için URL API
        async with aiohttp.ClientSession() as session:  #  HTTP oturumu açma
            async with session.get(url) as response:  # GET isteği gönderme
                if response.status == 200:
                    data = await response.json()  # JSON yanıtının alınması ve çözümlenmesi
                    return data['stats'][2]['base_stat']  #  Pokémon adını döndürme
                else:
                    return 50  # İstek başarısız olursa varsayılan adı döndürür
                


    async def saldir(self,enemy):
        if self.hp <= 0:
            return f'{self.name} dinleniyor'

        else:
            if isinstance(enemy , Wizard):  # Düşmanın Wizard veri tipi olup olmadığının kontrol edilmesi (Sihirbaz sınıfının bir örneği midir?) 
                sans = random.randint(1, 4) 
                if sans == 1:
                    return f"{enemy.name}, savaşta bir kalkan kullandı!"

            hasar=round(self.attack*(enemy.defense/(enemy.defense+100)),2)
            if enemy.hp <= hasar:
                enemy.hp=0
                return f'{self.name} {enemy.name}\'e saldırdı.\n {enemy.name} yenildi.'

            else:
                enemy.hp-=hasar
                return f'{self.name} {enemy.name}\'e saldırdı.{hasar} verdi.\n{enemy.name}\'in canı {enemy.hp} kaldı '
        


class Fighter(Pokemon):
    async def saldir(self, enemy):
        super_guc = random.randint(10 , 20)  
        self.attack += super_guc
        sonuc = await super().saldir(enemy)  
        self.attack -= super_guc
        return sonuc + f"\n{self.name} süper saldırı kullandı. Eklenen güç: {super_guc}"
    



class Wizard(Pokemon):
    pass




if __name__== '__main__':
    pokemon1=Wizard('Rüzgar')
    pokemon2=Fighter('Ege')
    async def deneme():
        print(await pokemon1.info())
        print(await pokemon2.info())
        print("----------------------------------------------------------------------------------------------------------")
        print(await pokemon1.saldir(pokemon2))
        print('------------------------------------------------------------------------------------------------------------')
        print(await pokemon2.saldir(pokemon1))




    asyncio.run(deneme())
