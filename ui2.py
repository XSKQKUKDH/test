import streamlit as st
import random


def gen(Max):
   return random.randint(1,Max)

def param():
   if 'essaie' not in st.session_state:
      st.session_state['essaie'] = 0

   # Initialisation de la variable de difficulté
   if 'diff' not in st.session_state:
      st.session_state['diff'] = 100

   # Initialisation de la variable de victoire
   if 'victoire' not in st.session_state:
      st.session_state['victoire'] = 0

   # Initialisation de la variable de nombre secret
   if 'nombre' not in st.session_state:
      st.session_state['nombre'] = gen(st.session_state['diff'])
   
    

def main() :

   st.title("menu")


   st.image("https://media.tenor.com/XpXsPDTXhYQAAAAC/math-numbers.gif", width = 200)



   with st.expander("comment jouer"):
      st.write("")

   with st.expander("Bonus"):
      st.write("")


   # Initialisation à la difficulté 1
   if 'nombre' not in st.session_state:
      param()

   nouv_p , vict , conf = st.columns([1,1,1])

   # bouton nouvelle partie
   nouv_p.button("Nouvelle partie", on_click=param)

   # les victoires
   vict.button(f'Nb victoires : {st.session_state["victoire"]}')

   # la configuration d'une partie
   with conf.expander("Configuration"):
      st.selectbox('Difficulté', options=[100,500,1000],key='diff',on_change=param)
      st.slider('Nombre d\'essais', min_value=1, max_value=10,value=10, step=1,key='conf_essaie',on_change=param)
   
   # on initialise 2 variables pour le nombre entré par l'utilisateur et le message à afficher

   inp , mess = st.empty(), st.empty()

   guess = inp.number_input("Entrez un nombre", min_value=1, max_value=st.session_state['diff'], step=1, key='guess',format="%i")

   if guess :
      st.session_state['essaie'] += 1
      if guess == st.session_state['nombre']:
         st.session_state['victoire'] += 1
         mess.success(f'Bravo vous avez gagné en {st.session_state["essaie"]} essais')
         st.balloons()
      elif guess < st.session_state['nombre']:
         mess.warning('Le nombre est plus grand')
      else:
         mess.warning('Le nombre est plus petit')

      if st.session_state['essaie'] == st.session_state['conf_essaie']:
         mess.error(f'Vous avez perdu, le nombre était {st.session_state["nombre"]}')
         param()

   
      



      
         
   if st.button("Afficher les scores"):
         pass

if __name__ == "__main__":
    main()