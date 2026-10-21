import interface as iu


def automation_operation(orden_type,type_of_traders,market_type):
    iu.market_type()
    market_selection = input("Seleccione un Mercado 1/2:")
    if market_selection == "1":
        iu.orden_type_spot()
        selection_type = input("Seleccione el tipo de operacion")
        iu.buy_sell()
        buy_sell = int
    elif market_selection == "2":
        pass
    else:
        print("Seleccione un numero intente de nuevo")
    
          



            
            
