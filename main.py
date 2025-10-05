import discord
from discord.ext import commands
from config import token
from logic import Pokemon,Fighter,Wizard
import random

# Bot için yetkileri/intents ayarlama
intents = discord.Intents.all()  # Varsayılan ayarların alınması

# Tanımlanmış bir komut önekine ve etkinleştirilmiş amaçlara sahip bir bot oluşturma
bot = commands.Bot(command_prefix='!', intents=intents)

# Bot çalışmaya hazır olduğunda tetiklenen bir olay
@bot.event
async def on_ready():
    print(f'Giriş yapıldı:  {bot.user.name}')  # Botun adını konsola çıktı olarak verir

# '!go' komutu
@bot.command()
async def go(ctx):
    author = ctx.author.name  # Mesaj yazarının adını alma
    # Kullanıcının zaten bir Pokémon'u olup olmadığını kontrol edin. Eğer yoksa, o zaman...
    if author not in Pokemon.pokemons.keys():
        psec=random.randint(1,3)
        if psec == 1:
            pokemon = Pokemon(author)  # Yeni bir Pokémon oluşturma
            await ctx.send('Size Sıradan Pokemon geldi')

        if psec == 2:
            pokemon = Fighter(author)  # Yeni bir Pokémon oluşturma
            await ctx.send('Size Fighter Pokemon geldi')

        if psec == 3:
            pokemon = Wizard(author)  # Yeni bir Pokémon oluşturma
            await ctx.send('Size Wizrad Pokemon geldi')

        await ctx.send(await pokemon.info())  # Pokémon hakkında bilgi gönderilmesi
        image_url = await pokemon.show_img()  # Pokémon resminin URL'sini alma
        if image_url:
            embed = discord.Embed()  # Gömülü mesajı oluşturma
            embed.set_image(url=image_url)  # Pokémon'un görüntüsünün ayarlanması
            await ctx.send(embed=embed)  # Görüntü içeren gömülü bir mesaj gönderme
        else:
            await ctx.send("Pokémonun görüntüsü yüklenemedi!")
    else:
        await ctx.send("Zaten kendi Pokémonunuzu oluşturdunuz!")  # Bir Pokémon'un daha önce oluşturulup oluşturulmadığını gösteren bir mesaj

@bot.command()
async def feed(ctx):
    author = ctx.author.name
    if author not in Pokemon.pokemons.keys():
        await ctx.send("😕 Pokémon'un yok!")
    else:
        poke = Pokemon.pokemons[author]
        await poke.feed()  # Eğer feed async ise await ile çağırılır
        await ctx.send(await poke.feed())  # Besleme sonucunu gönder


@bot.command()
async def sil(ctx):
    author = ctx.author.name
    if author not in Pokemon.pokemons.keys():
        await ctx.send ('Zaten sende Pokemon yok')
    else:
        del Pokemon.pokemons[author]
        await ctx.send('Pokemon Silindi Yeni Alabilirsin')

@bot.command()
async def attack(ctx):
    target = ctx.message.mentions[0] if ctx.message.mentions else None  # Mesajda belirtilen kullanıcıyı alırız
    if target:  # Kullanıcının belirtilip belirtilmediğini kontrol ederiz
        # Hem saldırganın hem de hedefin Pokémon sahibi olup olmadığını kontrol ederiz
        if target.name in Pokemon.pokemons and ctx.author.name in Pokemon.pokemons:
            enemy = Pokemon.pokemons[target.name]  # Hedefin Pokémon'unu alırız
            attacker = Pokemon.pokemons[ctx.author.name]  # Saldırganın Pokémon'unu alırız
            result = await attacker.saldir(enemy)  # Saldırıyı gerçekleştirir ve sonucu alırız
            await ctx.send(result)  # Saldırı sonucunu göndeririz
        else:
            await ctx.send("Savaş için her iki tarafın da Pokémon sahibi olması gerekir!")  # Katılımcılardan birinin Pokémon'u yoksa bilgilendiririz
    else:
        await ctx.send("Saldırmak istediğiniz kullanıcıyı etiketleyerek belirtin.")  # Saldırmak için kullanıcıyı etiketleyerek belirtmesini isteriz



bot.run(token)
