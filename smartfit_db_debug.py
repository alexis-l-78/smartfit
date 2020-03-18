# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 09:43:21 2020

@author: jlalv
"""

#coding: utf-8

import sqlite3

def open_database():
      conn = sqlite3.connect('Smartfit_db')
      cursor = conn.cursor()
    
      cursor.execute("""SELECT id, nom_exercice, muscle_cibler, niveau_difficulte FROM exercices""")
      exercices = cursor.fetchall()
      print(exercices)
 
def clean_database():
    
      conn = sqlite3.connect('Smartfit_db')
      cursor = conn.cursor()
    
      cursor = conn.cursor()
      cursor.execute("""
      DROP TABLE profil
      """)
      conn.commit()
      
      cursor = conn.cursor()
      cursor.execute("""
      DROP TABLE compte
      """)
      conn.commit()
      
      cursor = conn.cursor()
      cursor.execute("""
      DROP TABLE corps
      """)
      conn.commit()
      
      cursor = conn.cursor()
      cursor.execute("""
      DROP TABLE exercices
      """)
      conn.commit()
      
      cursor = conn.cursor()
      cursor.execute("""
      DROP TABLE cardio
      """)
      conn.commit()
      
      cursor = conn.cursor()
      cursor.execute("""
      DROP TABLE nutrition
      """)
      conn.commit()
      
      cursor = conn.cursor()
      cursor.execute("""
      DROP TABLE suivi_perso
      """)
      conn.commit()

def create_table():
    

    conn = sqlite3.connect('Smartfit_db')
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS profil(
         id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
         name TEXT,
         age INTERGER,
         poid FLOAT,
         taille FLOAT
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS compte(
         id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
         email TEXT,
         mdp TEXT
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS corps(
         id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
         parti_corp TEXT
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS exercices(
         id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
         nom_exercice TEXT,
         muscle_cibler TEXT,  
         niveau_difficulte TEXT
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS cardio(
         id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
         nom_exercice TEXT, 
         objectif TEXT
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS nutrition(
         id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
         aliment_bon TEXT,  
         aliment_pasbon TEXT,
         conseil_general TEXT
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS suivi_perso(
         id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
         performances_exo TEXT,
         evaluation_exo INTERGER,
         commentaires_exo TEXT
    )
    """)
   
    conn.commit()



def insert_datas():
    """
    This function add test datas to the database
    """
    conn = sqlite3.connect('Smartfit_db')
    cursor = conn.cursor()
    
    cursor.execute("""
     INSERT INTO corps(parti_corp) VALUES(?)""", ("bras",))
    conn.commit()
    
    cursor.execute("""
     INSERT INTO corps(parti_corp) VALUES(?)""", ("abdomen",))
    conn.commit()
    
    cursor.execute("""
     INSERT INTO corps(parti_corp) VALUES(?)""", ("fesse",))
    conn.commit()
    
    cursor.execute("""
     INSERT INTO corps(parti_corp) VALUES(?)""", ("jambes",))
    conn.commit()
    
    cursor.execute("""
    INSERT INTO corps(parti_corp) VALUES(?)""", ("torse",))
    conn.commit()
    
    cursor.execute("""
    INSERT INTO corps(parti_corp) VALUES(?)""", ("dos",))
    conn.commit()
    
    cursor.execute("""
    INSERT INTO exercices(nom_exercice, muscle_cibler, niveau_difficulte) VALUES(?, ?, ?)""", ("curl", "biceps", "intermediaire"))
    conn.commit()
    
    cursor.execute("""
    INSERT INTO exercices(nom_exercice, muscle_cibler, niveau_difficulte) VALUES(?, ?, ?)""", ("dips", "pectoraux", "difficile"))
    conn.commit()
    
    cursor.execute("""
    INSERT INTO exercices(nom_exercice, muscle_cibler, niveau_difficulte) VALUES(?, ?, ?)""", ("traction", "dorsaux", "intermediaire"))
    conn.commit()
    

    
if __name__ == '__main__' :
    
    



    
    create_table()
    
    insert_datas()
    
    open_database()
    
    clean_database()
    

   

    
    
