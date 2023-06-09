
import math

def calcular_cantidades_cinematicas(posicion_final, posicion_inicial,
    velocidad_final, velocidad_inicial, aceleracion, tiempo,
    tipo_movimiento):
  
    """
    Esta función permite calcular las cantidades cinemáticas para los cuatro
    movimientos en una dimensión: movimiento uniforme, uniforme variado, caida
    libre, y tiro vertical.IMPORTANTE: Los datos de ingreso deben tener las
    unidades en el S.I. Para especificar los incognitas del ejercicio
    se deben ingresar como argumento las letras correspondientes a la mismas 
    como string. Ejemplo, si la incognita es la velocidad final  y la posición
    final entonces se debe ingresar "x" en el primer argumento y "v" en el tercer 
    argumento ademas se debe especificar el tipo de movimiento entre
    comillas en el último argumento de la función

    parámetros de entrada:
    posicion_final en metros
    posicion_inicial en metros
    velocidad_final  en metros/segundo
    velocidad_inicial en metros/segundo
    aceleracion en metros/seg^2
    tiempo en seg
    tipo_movimiento se especifica el tipo de movimiento para el ejercicio
  
    parámetros de salida:
    x_final = posición final en el m.u o m.r.u.v en metros
    y_final = altura o altura maxima en la caída libre o tiro vertical en metros
    v_final = velocidad final en metos/segundos
    t = tiempo en el cual sucede el movimento en segundos
    desplazamiento = diferencia entre el inicio y final del movimiento en metros

    """ 

    resultado = 0

    ## movimiento rectilineo uniforme => velocidad es una constante
    if tipo_movimiento == "MRU":

        # Cálculo del tiempo
        if tiempo == "t":
            t = (posicion_final - posicion_inicial) / velocidad_final
            resultado = "Tiempo final = " + str(t) + " seg"

        # Cálculo de la velocidad
        if velocidad_final == "v":
            v_final = (posicion_final - posicion_inicial) / tiempo
            resultado = "Velocidad final = " + str(v_final) + " m/seg"

        # Cálculo de la velocidad
        if velocidad_final != 0 and tiempo > 0 and posicion_final == "x":
            x_final = posicion_inicial + velocidad_final * tiempo
            resultado = "Posición final = " + str(x_final) + " m"

    # movimiento rectilineo uniforme variado => aceleracion es una cte
    elif tipo_movimiento == "MRUV":

        # Cálculo de la posición
        if posicion_final == "x" and tiempo > 0 and velocidad_final != "v":
            x_final = posicion_inicial + (velocidad_inicial * tiempo) + (aceleracion/2) * tiempo**2
            resultado = "Posición final = " + str(x_final) + " m"

        # Cálculo de la posición final y la velocidad final
        if velocidad_final == "v" and tiempo > 0 and posicion_final == "x":
            v_final = velocidad_inicial + (aceleracion * tiempo)
            x_final = posicion_inicial + ((v_final + velocidad_inicial) / 2) * tiempo
            resultado = "Posición final  = "+ str(x_final) +  " m" + "     "  +"Velocidad final = " + str(v_final) + " m/seg"

        # Cálculo de la velocidad sin tiempo, y el tiempo
        if velocidad_final == "v" and tiempo == "t":
            v_final= math.sqrt((velocidad_inicial**2) + 2 * aceleracion * (posicion_final - posicion_inicial))
            t= (v_final - velocidad_inicial) / aceleracion
            resultado = "Velocidad final = " + str(v_final) + " m/seg" +"     " + "Tiempo = " + str(t) + " seg"

        # Cálculo de la posición final, aceleración y el tiempo
        if posicion_final == "x" and aceleracion == "a":
            x_final = posicion_inicial + ((velocidad_final + velocidad_inicial) / 2) * tiempo
            a = (((velocidad_final**2) - (velocidad_inicial**2)) / 2) * (x_final - posicion_inicial)
            t = (velocidad_final - velocidad_inicial) / a
            resultado = "Posición final = " + str(x_final) + " m" +"      "+ " aceleración = " + str(
                a) + " m/seg^2 "+"      "+"Tiempo = " + str(t) + " seg"

  # tiro vertical con la aceleracion resultante : ar=a-ag
    elif tipo_movimiento=="tiro vertical":
        # Cálculo de la altura
        if aceleracion!=9.8:
        # calculo de la altura
          if posicion_final=="y":
              resultado = "altura  = " + str(round(posicion_inicial 
              + (velocidad_inicial * tiempo) + ((aceleracion-9.81)/2)*tiempo**2,3))+ " m"

        # Cálculo de la velocidad
          if velocidad_final=="v":
              resultado="velocidad final = " + str(round(math.sqrt((velocidad_inicial**2)
              +2*(aceleracion-9.81)*(posicion_final-posicion_inicial)),3)) + " m/seg"

          # Cálculo del tiempo
          if tiempo=="t":
              resultado="tiempo = " + str(round(((velocidad_final-velocidad_inicial)/(aceleracion-9.81)),3))+" seg"
          
          # Cálculo de la altura máxima
          if posicion_final=="altura maxima":
              resultado="tiempo vuelo = " + str(round((velocidad_inicial)/(aceleracion-9.8),3))
              + "altura maxima = " + str(round(((velocidad_inicial**2)/2*(aceleracion-9.81)),3)) 
              + " m"
      
            # Cálculo de la altura con la ausencia de la velocidad final
          if posicion_final=="y" and tiempo>0 and velocidad_final == "v":
                y_final = posicion_inicial + (velocidad_inicial * tiempo) + ((aceleracion-9.81)/2)*tiempo**2
                v_final = math.sqrt((velocidad_inicial**2)+2*(aceleracion-9.81)*(y_final-posicion_inicial))
                resultado= "altura final=" + str(round(y_final, 3)) + " m" + "     " + "velocidad final=" + str(round(v_final, 3)) + " m/seg"  
        
        # movimiento de tiro vertical donde la aceleración resultante es la de la gravedad
        elif aceleracion==9.8:
            # Cálculo de la posición
          if posicion_final == "y" and tiempo == "t" and velocidad_final != "v":
              t = (velocidad_final - velocidad_inicial)/(-1*aceleracion)
              y_final = posicion_inicial + (velocidad_inicial * t) - ((aceleracion/2) * t**2)
              resultado = "Posición final = " + str(round(y_final,3)) + " m     "   + "tiempo = " + str(round(t,3)) + " seg"

          # Cálculo de la posición final y la velocidad final
          if velocidad_final == "v" and tiempo > 0 and posicion_final == "y":
              v_final = velocidad_inicial + (aceleracion * tiempo)
              y_final = posicion_inicial + ((v_final + velocidad_inicial) / 2) * tiempo
              resultado = "Posición final  = "+ str(y_final) + " m" +"     "  
              +"Velocidad final = " + str(v_final) + " m/seg"

          # Cálculo de la velocidad sin tiempo, y el tiempo
          if velocidad_final == "v" and tiempo == "t":
              v_final= math.sqrt((velocidad_inicial**2) + 2 * aceleracion * (posicion_final - posicion_inicial))
              t= (v_final - velocidad_inicial) / aceleracion
              resultado = "Velocidad final = " + str(v_final) +  " m/seg" + "     " + "Tiempo = " + str(t) + " seg"

          # Cálculo de la posición final, aceleración y el tiempo
          if posicion_final == "y" and aceleracion == "a":
              y_final = posicion_inicial + ((velocidad_final + velocidad_inicial) / 2) * tiempo
              a = (((velocidad_final**2) - (velocidad_inicial**2)) / 2) * (y_final - posicion_inicial)
              t = (velocidad_final - velocidad_inicial) / a
              resultado = "Posición final = " + str(y_final) +  " m" +"      "+ " aceleración = " 
              + str(a) + " m/seg^2" + "      "+"Tiempo = " + str(t) +" seg"

   # MOvimiento de caída libre      
    elif tipo_movimiento=="caida libre":
   
   # Cálculo de la velocidad final
      if velocidad_final=="v"and tiempo!="t":
        resultado= "velocidad final = "  + str(round(aceleracion/tiempo,3)) + " seg"
    
    # Cálculo del tiempo de la caída
      if tiempo=="t" and velocidad_final!="v":
        resultado= "tiempo caida=" + str(round(velocidad_final/aceleracion,3)) + " m\seg"
 
    # Cálculo de la posicion final  
      if posicion_final=="y" and tiempo>0:
        v_final = -1*aceleracion*tiempo
        resultado="posicion final =" + str(round(posicion_inicial-((aceleracion/2)*(tiempo**2)), 3)) + " m      " + "velocidad = " + str(round(v_final, 3))+ " m/s"
     
      if velocidad_final=="v" and tiempo=="t": 
        v_final=math.sqrt(2*(posicion_final-posicion_inicial)*aceleracion)
        resultado= "velocidad final = "  + str(round(v_final,3)) + " m/s"+  "      tiempo = "+str(round(v_final/aceleracion,3))+ " seg"
    #
    else:
        resultado = "El tipo de movimiento ingresado no corresponde a MRU, MRUV, caída libre o  tiro vertical"

    return tipo_movimiento+" :"+ "  "+ resultado 


# parámetros de ingreso para la función deben estar en m, seg, m/seg, m/seg^2 respectivamente

#posicion_final,  posicion_inicial,  velocidad_final,   velocidad_inicial,    aceleración,    tiempo ,  tipo_movimiento 

print(calcular_cantidades_cinematicas("x",75, "v",5, -2, 7, "MRUV"))
