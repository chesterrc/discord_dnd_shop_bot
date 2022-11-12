import random
import item_library

def Common_Item_Gen():
    print('it went through to the common items!')
    Common = [] 
    #Reading Item and Money in library
    count = 0 
    #Rand generation of COmmon Item and Mon
    while count <= 35: 
        Common += [{'name': item_library.common_item[random.randrange(0, len(item_library.common_item))], 'Gold' : item_library.common_item_price[random.randrange(0, len(item_library.common_item_price))]}]
        count += 1
    true_common = list(Common)
    return true_common 

def Uncommon_Item_Gen():
    Uncommon = [] 
    #Reading Item and Money in library
    count = 0 
    #Rand generation of COmmon Item and Mon
    while count < 35: 
        Uncommon += [{'name': item_library.uncommon_item[random.randrange(0, len(item_library.uncommon_item))], 'Gold' : item_library.uncommon_item_price[random.randrange(0, len(item_library.uncommon_item_price))]}]
        count += 1
    true_uncommon = list(Uncommon)
    return true_uncommon 

def Rare_Item_Gen():
    Rare = [] 
    #Reading Item and Money in library
    count = 0 
    #Rand generation of COmmon Item and Mon
    while count < 35: 
        Rare += [{'name': item_library.rare_item[random.randrange(0, len(item_library.rare_item))], 'Gold' : item_library.rare_item_price[random.randrange(0, len(item_library.rare_item_price))]}]
        count += 1
    true_rare = list(Rare)
    return true_rare 

def cCommon_Item_Gen():
    cCommon = [] 
    #Reading Item and Money in library
    count = 0 
    #Rand generation of COmmon Item and Mon
    while count < 35: 
        cCommon += [{'name': item_library.common_consumable[random.randrange(0, len(item_library.common_consumable))], 'Gold' : item_library.common_consumable_price[random.randrange(0, len(item_library.common_consumable_price))]}]
        count += 1
    true_ccommon = list(cCommon)
    return true_ccommon

def cUncommon_Item_Gen():
    cUncommon = [] 
    #Reading Item and Money in library
    count = 0 
    #Rand generation of COmmon Item and Mon
    while count < 35: 
        cUncommon += [{'name': item_library.uncommon_consumable[random.randrange(0, len(item_library.uncommon_consumable))], 'Gold' : item_library.uncommon_consumable_price[random.randrange(0, len(item_library.uncommon_consumable_price))]}]
        count += 1
    true_cUncommon = list(cUncommon)
    return true_cUncommon 

def cRare_Item_Gen():
    cRare = [] 
    #Reading Item and Money in library
    count = 0 
    #Rand generation of COmmon Item and Mon
    while count < 35: 
        cRare += [{'name': item_library.rare_consumable[random.randrange(0, len(item_library.rare_consumable))], 'Gold' : item_library.rare_consumable_price[random.randrange(0, len(item_library.rare_consumable_price))]}]
        count += 1
    true_cRare = list(cRare)
    return true_cRare

class shop: 
    def __init__(self, True_Common, True_Uncommon, True_Rare, True_cCommon, True_cUncommon, True_cRare): 
        self.common_list = list(True_Common)
        self.uncommon_list = list(True_Uncommon)
        self.rare_list = list(True_Rare)
        self.ccommon_list = list(True_cCommon)
        self.cuncommon_list = list(True_cUncommon)
        self.crare_list = list(True_cRare)

    def get_shop_list(self):
        return self.common_list, self.uncommon_list, self.rare_list, self.ccommon_list, self.cuncommon_list, self.crare_list

Phauahevon_common = Common_Item_Gen() 
Phauahevon_uncommon = Uncommon_Item_Gen() 
Phauahevon_rare = Rare_Item_Gen()
Phauahevon_ccommon = cCommon_Item_Gen()
Phauahevon_cuncommon = cUncommon_Item_Gen()
Phauahevon_crare = cRare_Item_Gen()

Eaqoria_common = Common_Item_Gen() 
Eaqoria_uncommon = Uncommon_Item_Gen() 
Eaqoria_rare = Rare_Item_Gen()
Eaqoria_ccommon = cCommon_Item_Gen()
Eaqoria_cuncommon = cUncommon_Item_Gen()
Eaqoria_crare = cRare_Item_Gen()

Weastberia_common = Common_Item_Gen() 
Weastberia_uncommon = Uncommon_Item_Gen() 
Weastberia_rare = Rare_Item_Gen()
Weastberia_ccommon = cCommon_Item_Gen()
Weastberia_cuncommon = cUncommon_Item_Gen()
Weastberia_crare = cRare_Item_Gen()

def refresh():
    global Phauahevon_common, Phauahevon_uncommon,Phauahevon_rare, Phauahevon_ccommon, Phauahevon_cuncommon, Phauahevon_crare, Phauahevon
    global Eaqoria_common, Eaqoria_uncommon, Eaqoria_rare, Eaqoria_ccommon, Eaqoria_cuncommon, Eaqoria_rare, Eaqoria_crare, Eaqoria
    global Weastberia_common,Weastberia_cuncommon,Weastberia_crare, Weastberia_ccommon, Weastberia_rare, Weastberia_uncommon, Weastberia

    Phauahevon_common = Common_Item_Gen() 
    Phauahevon_uncommon = Uncommon_Item_Gen() 
    Phauahevon_rare = Rare_Item_Gen()
    Phauahevon_ccommon = cCommon_Item_Gen()
    Phauahevon_cuncommon = cUncommon_Item_Gen()
    Phauahevon_crare = cRare_Item_Gen()

    Eaqoria_common = Common_Item_Gen() 
    Eaqoria_uncommon = Uncommon_Item_Gen() 
    Eaqoria_rare = Rare_Item_Gen()
    Eaqoria_ccommon = cCommon_Item_Gen()
    Eaqoria_cuncommon = cUncommon_Item_Gen()
    Eaqoria_crare = cRare_Item_Gen()

    Weastberia_common = Common_Item_Gen() 
    Weastberia_uncommon = Uncommon_Item_Gen() 
    Weastberia_rare = Rare_Item_Gen()
    Weastberia_ccommon = cCommon_Item_Gen()
    Weastberia_cuncommon = cUncommon_Item_Gen()
    Weastberia_crare = cRare_Item_Gen()

    Phauahevon = shop(Phauahevon_common, Phauahevon_uncommon, Phauahevon_rare, Phauahevon_ccommon, Phauahevon_cuncommon, Phauahevon_crare)
    Weastberia = shop(Weastberia_common, Weastberia_uncommon, Weastberia_rare, Weastberia_ccommon, Weastberia_cuncommon, Weastberia_crare)
    Eaqoria = shop(Eaqoria_common, Eaqoria_uncommon, Eaqoria_rare, Eaqoria_ccommon, Eaqoria_cuncommon, Eaqoria_crare)

Phauahevon = shop(Phauahevon_common, Phauahevon_uncommon, Phauahevon_rare, Phauahevon_ccommon, Phauahevon_cuncommon, Phauahevon_crare)
Weastberia = shop(Weastberia_common, Weastberia_uncommon, Weastberia_rare, Weastberia_ccommon, Weastberia_cuncommon, Weastberia_crare)
Eaqoria = shop(Eaqoria_common, Eaqoria_uncommon, Eaqoria_rare, Eaqoria_ccommon, Eaqoria_cuncommon, Eaqoria_crare)

  