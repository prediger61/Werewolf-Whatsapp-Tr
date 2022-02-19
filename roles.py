kurtAdam = """*KurtAdam* 
_Sen gözü dönmüş bir kurtsun. Her gün köylüleri kandırarak aralarına sızıp geceleri evlerinden kanlar içinde çıkarsın._
"""
alfaKurt = """*Alfa KurtAdam*
_Sen Alfa Kurt’sun, lanetin kaynağı, pisliğin tekisin.Kime saldırılacağını sen seçersin.Gözcü seni iyi biri olarak görür fakat asil gözcü senin rolünü görebilir._
"""
soytarı = """*Soytarı*
_Senin olayın linç yemek. Evet tam olarak bu.Kendini idam ettirmek için en iyi stratejiyi belirlemelisin.Gözcülere yakalanmamalısın yoksa silahşör tarafından öldürülüp oyunu kaybedersin._
"""
silahsor = """*Silahşör*
_Sen köyün RedKit’isin. Oyun başında 2 mermiye sahipsin. Her yeni gün başladığında istediğin kişiye sıkabilirsin, unutma 1 kez ateş ettiğinde rolün açığa çıkar._
"""
gozcu = """*Gözcü*
_Gözcüler her gece birinin rolünün iyi(Köylü,Silahşör,Alfa KurtAdam,) ya da kötü(Soytarı,KurtAdam) olarak  görebilir. Unutma eğer açığa çıkarsan kurtadamların hedefi olma ihtimalin yüksek._
"""
alfagozcu = """*Alfa Gözcü*
_AlfaGözcüler her gece birinin rolünü görebilir. Unutma eğer açığa çıkarsan kurtadamların hedefi olma ihtimalin yüksek._
"""
mayor = """*Belediye Başkanı (Mayor)*
_Sıradan bir köylü olarak başlarsın. Ta ki kendi isteğinle rolünü açıklayana kadar. Masaya yumruğunu vurarak linç sırasında 2 oy kullanırsın._
"""
doktor = """*Doktor*
_Sen köyün doktorusun. Her gece seçtiğin birini koruyabilirsin. Ancak kendini üst üste ancak 1 kere koruyabilirsin._
"""
koylu = """*Köylü*
_Sıradan bir köylüsün, oy kullanmak dışında başka bir işlevin yok. Diğer köylüleri bularak, kurtadam ve aykırıların linç edilip ölmesini sağla._
"""

roleList=[]
roleList.append(kurtAdam)
roleList.append(kurtAdam)
roleList.append(alfaKurt)
roleList.append(doktor)
roleList.append(mayor)
roleList.append(gozcu)
roleList.append(alfagozcu)
roleList.append(silahsor)
#roleList.append(kurtAdam)
#roleList.append(koylu)
#roleList.append(koylu)
#roleList.append(koylu)
#roleList.append(kurtAdam)