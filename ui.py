import streamlit as st

import requests
import ui_functions
import openai
from streamlit_lottie import st_lottie





API_KEY = "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"
API_KEY = "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"
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def find_true_positions(boolean_list):
    for a,i in enumerate(boolean_list[0]):
        if i == True:
            return a+1
################################################################################################################################################################
def main():
    with st.container():
        st.header(":red[Women's E-Commerce Clothing Reviews Predictor ] :wave:")
        left,rigth = st.columns(2)
        with left:
            lottie_url = "https://lottie.host/9b1d760a-d152-4817-9a7c-d5dce70d0f96/65tWrCArzp.json"
            lottie_json = load_lottieurl(lottie_url)
            st_lottie(lottie_json,height=400)
            lottie_url = "https://lottie.host/d27c410d-c34e-494c-826b-47d37805e1e1/VkSmAWhA8B.json"
            lottie_json = load_lottieurl(lottie_url)
            st_lottie(lottie_json,height=400)
        with rigth:
            st.title(":blue[NLP Reviews v1.0!]")
            
            st.write(""":red[Descripción del Proyecto]

¡Bienvenidos a nuestro increíble proyecto de NLP! Este proyecto se centra en las reseñas de ropa de comercio electrónico, permitiendo a los usuarios enviar sus opiniones y recibir calificaciones estimadas de estrellas del 1 al 5. El potente modelo de procesamiento de lenguaje natural que hemos desarrollado analiza el contenido y el sentimiento de las reseñas para generar predicciones precisas.

:red[FUNCIONALIDADES]

:green[Introduce tu Reseña:] Los usuarios pueden ingresar sus propias reseñas y nuestro modelo proporcionará rápidamente una calificación estimada de estrellas en función de la entrada.
                     
:green[Integración con ChatGPT:] Para mayor comodidad, hemos incorporado ChatGPT, lo que permite a los usuarios generar reseñas de ejemplo con calificaciones de estrellas específicas con un simple clic.
                     
:green[Predicciones Precisas:] Nuestro modelo entrenado garantiza predicciones de calificaciones de estrellas confiables y precisas, mejorando la confianza y la experiencia del usuario.
                """)
            
    st.write("---")

    with st.container():
        left , right = st.columns(2)
       
        with right:
                st.subheader(":green[Copy and paste the review provided by ChatGPT, do not copy the Score!!  😂]")
                st.subheader(":pink[Select the ⭐️ rating]")
                checkbox_states = [[st.checkbox("⭐️" * i) for i in range(1, 6)]]
                true_positions = find_true_positions(checkbox_states)
                
                
        with left:
            
            if true_positions == None:
                    true_positions= "Random"

            if st.button(f":red[Generate a :green[{true_positions}]-stars⭐️ review with ChatGPT]"):
                
                openai.api_key = API_KEY # cargo mi api_key OpenAI
                content = f"Dame tu reseña en inglés nueva de {true_positions} estrellas de un vestido comprado, donde 1 es pésimo y 5 excelente, 70 palabras  "
                messages =[{"role":"system","content":"Crea reseñas de ropa"}] # Pongo al bot en un contexto inicial
                messages.append({"role":"user","content":content})                      
                response = openai.ChatCompletion.create(
                                            model= "gpt-3.5-turbo",              
                                            messages = messages                        
                                            )
                response_content = response.choices[0].message.content                  
                messages.append({"role":"assistant","content":response_content})
                st.text_area(":green[gpt-3.5-turbo]",value=response.choices[0].message.content,height=300, key="text_area")
                #st.text(f"{response.choices[0].message.content}")
    
    
    ui_functions.load_model_and_textinput()
    

if __name__ == "__main__":
    main()