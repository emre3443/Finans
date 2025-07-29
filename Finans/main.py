import streamlit as st
import sqlite3

conn=sqlite3.connect('emre.db')
c=conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS arac(isim TEXT,kod TEXT")
conn.commit()

def aracEkle(isim,kod):
    conn=sqlite3.connect('emre.db')
    c = conn.cursor()
    c.execute('INSERT OR INGORE INTO arac VALUES(?,?)',(isim,kod))
    conn.commit()


def araclar()