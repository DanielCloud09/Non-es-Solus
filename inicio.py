#Linea para importar la biblioteca streamlit
import streamlit as st
#linea para escribir un titulo
st.title("TEST Non es Solus")
#linea de subtitulo
st.markdown("Proyecto inspirado en el universo del Mandela Catalogue, no apto para asustadisos, niños, tontitos, personas de bajo intelecto, enfermos cardiacos, enfermos terminales y loquitos, ademas de estar dirigido especialmente para las personas(especificamente danieles, matias, maximilianos y gonzalos) de la region metropólitana pero tambien para el resto de Chile como precaucion, ademas de tener un apartado de conocimiento sobre la grasa para los interesados que hayan pasado el test de alternos. ")

# Imagen de portada
st.image("mand.jpg", caption="**Ellos se ven como nosotros...**")

# Sección descriptiva
st.header("¿Qué es esta aplicación?")
st.write(
    """
    Esta aplicación es una **experiencia interactiva de terror psicológico**, inspirada en el universo del *Mandela Catalogue*.  
    Aquí pondremos a prueba tu **percepción**, tu **capacidad para distinguir la realidad**, y tu **resistencia mental** ante lo desconocido.

    El **Test de Alternos** no busca solo asustarte, sino **evaluar tu reacción** frente a estímulos ambiguos y señales de suplantación.

    *Advertencia: algunas imágenes, sonidos o decisiones podrían resultar perturbadoras.*
    """
)
st.image("visto2.png", caption="**Ellos observan, siempre al acecho...**")

# Presentación del objetivo
st.subheader("Objetivo del Proyecto")
st.write(
    """
    El objetivo de esta aplicación es simular un **entrenamiento del Departamento de Defensa** del Condado de Mandela,
    diseñado para identificar **Alternos**: entidades que **imitan la forma humana** pero carecen de empatía y racionalidad ademas de un apartado sobre la grasa para los que hayan pasado.

    En versiones futuras, podrás:
    - Realizar un **test visual** con fotografías de humanos y alternos.
    - Escuchar **grabaciones distorsionadas** y decidir si provienen de una persona o una entidad.
    - Participar en **simulaciones interactivas** donde tus decisiones determinarán tu destino.
    - Calcular tu porcentaje de grasa y aasegurar por las dudas de que no eres un alterno.
    """
)




