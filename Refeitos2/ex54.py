dias_da_semana  = [ "Domingo" , "Segunda" , "Terça" , "Quarta" , "Quinta" , "Sexta" , "Sabado" ]

def  seleciona_dias_da_semana_que_têm_a_letra_S ( Dias_com_S ):
    Lista_auxiliar  = []
    para  dias  em  Dias_com_S :
    se  "S"  em  dias :
    Lista_auxiliar . acrescentar ( dias )
    retornar  Lista_auxiliar

dias_da_semana_que_contêm_a_letra_S  =  selecione_dias_da_semana_que_têm_a_letra_S ( dias_da_semana )
imprimir ( dias_da_semana_que_contêm_a_letra_S )