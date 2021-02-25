импортировать  дату и время  как  dt
from  pathlib  import  Path
из  urllib . анализировать  импорт  urljoin
 запросы на импорт
импорт  bs4
импортное  пимонго


МЕСЯЦЕВ  = {
    "янв" : 1 ,
    "фев" : 2 ,
    "мар" : 3 ,
    «апр» : 4 , г.
    «май» : 5 ,
    «мая» : 5 ,
    «июн» : 6 ,
    "июл" : 7 ,
    «авг» : 8 ,
    «сен» : 9 ,
    «окт» : 10 ,
    «ноя» : 11 , г.
    «дек» : 12 ,
}


класс  MagnitParse :
    def  __init__ ( self , start_url , db_client ):
        я . start_url  =  начальный_url
        я . db  =  db_client [ "gb_data_mining_15_02_2021" ]
        я . collection  =  self . db [ "magnit_products" ]

    def  _get_response ( self , url ):
        # TODO: написать обработку ошибки
         запросы на возврат . получить ( URL )

    def  _get_soup ( self , url ):
        ответ  =  себя . _get_response ( URL )
        вернуть  bs4 . BeautifulSoup ( ответ . Текст , "LXML" )

    def  run ( self ):
        суп  =  сам . _get_soup ( собственный . start_url )
        каталог  =  суп . find ( "div" , attrs = { "class" : "сatalogue__main" })
        для  прод_а  в  каталоге . find_all ( "a" , рекурсивный = False ):
            product_data  =  self . _parse ( prod_a )
            я . _save ( product_data )

