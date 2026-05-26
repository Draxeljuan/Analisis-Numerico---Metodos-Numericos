# api.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import numpy as np

# Tus importaciones existentes
from conversor import ConvertirAFuncion
from Metodos.biseccion import biseccion
from Metodos.jacobi import jacobi
from Metodos.gauss_seidel import gauss_seidel
from Metodos.falsaposicion import falsa_posicion
from Metodos.newtonr import newton_raphson
from Metodos.puntofijo import punto_fijo
from Metodos.secante import secante



app = FastAPI(title="Metodos Numericos API")

# Habilitar CORS para Angular (puerto 4200) pueda conectar
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- MODELOS DE PETICIÓN ---
class RequestLineal(BaseModel):
    A: List[List[float]]
    b: List[float]
    tol: float
    max_iter: int = 100

class RequestNoLineal(BaseModel):
    funcion: str
    variable: str = "x"
    tol: float
    max_iter: int = 100
    a: Optional[float] = None
    b: Optional[float] = None
    x0: Optional[float] = None
    
    
    
# --- ENDPOINTS LINEALES ---
@app.post("/lineal/jacobi")
def api_jacobi(data: RequestLineal):
    try:
        A_np = np.array(data.A)
        b_np = np.array(data.b)
        
        solucion, total_it, historial, es_dominante = jacobi(
            A_np, b_np, data.tol, max_iter=data.max_iter
        )
        
        return {
            "solucion": solucion,
            "total_iteraciones": total_it,
            "es_dominante": es_dominante,
            "datos_tabla": historial
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@app.post("/lineal/gauss-seidel")
def api_gauss_seidel(data: RequestLineal):
    try:
        A_np = np.array(data.A)
        b_np = np.array(data.b)
        
        solucion, total_it, historial, es_dominante = gauss_seidel(
            A_np, b_np, data.tol, max_iter=data.max_iter
        )
        
        return {
            "solucion": solucion,
            "total_iteraciones": total_it,
            "es_dominante": es_dominante,
            "datos_tabla": historial
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# --- ENDPOINTS NO LINEALES ---
@app.post("/no-lineal/biseccion")
def api_biseccion(data: RequestNoLineal):
    try:
        conv = ConvertirAFuncion()
        f_ejecutable, _ = conv.preparar_funciones(data.funcion, data.variable)
        
        # Biseccion devuelve 3 valores
        raiz, total_it, historial = biseccion(
            f_ejecutable, data.a, data.b, data.tol, data.max_iter
        )
        
        if raiz is None:
            raise HTTPException(status_code=400, detail="El intervalo no cumple f(a)*f(b) < 0")

        return {
            "resultado": raiz,
            "total_iteraciones": total_it,
            "datos_tabla": historial  
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@app.post("/no-lineal/falsaposicion")
def api_falsaposicion(data: RequestNoLineal):
    try:
        conv = ConvertirAFuncion()
        f_ejecutable, _ = conv.preparar_funciones(data.funcion, data.variable)
        
        # Falsa Posicion nos retorna 3 valores
        raiz, total_it, historial = falsa_posicion(
            f_ejecutable, data.a, data.b, data.tol, data.max_iter
        )
        
        if raiz is None:
            raise HTTPException(status_code=400, detail="El intervalo no cumple f(a)*f(b) < 0")
        
        return {
            "resultado": raiz,
            "total_iteraciones": total_it,
            "datos_tabla": historial
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
        
@app.post("/no-lineal/newton-raphson")
def api_newtonraphon(data: RequestNoLineal):
    try:
        conv = ConvertirAFuncion()
        f_ejecutable, f_simbolica = conv.preparar_funciones(data.funcion, data.variable)
        
        # Newton Raphson nos retorna 3 valores
        raiz, total_it, historial = newton_raphson(
            f_ejecutable, f_simbolica, data.x0, data.tol, data.variable, data.max_iter
        )
        
        return {
            "resultado": raiz,
            "total_iteraciones": total_it,
            "datos_tabla": historial
        }
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@app.post("/no-lineal/puntofijo")
def api_punto_fijo(data: RequestNoLineal):
    try:
        conv = ConvertirAFuncion()
        f_ejecutable, _ = conv.preparar_funciones(data.funcion, data.variable)
        
        # Punto fijo nos retorna 3 valores
        raiz, total_it, historial = punto_fijo(
            f_ejecutable, data.x0, data.tol, data.max_iter
        )
        
        return {
            "resultado": raiz,
            "total_iteraciones": total_it,
            "datos_tabla": historial
        }
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@app.post("/no-lineal/secante")
def api_secante(data: RequestNoLineal):
    try:
        conv = ConvertirAFuncion()
        f_ejecutable, _ = conv.preparar_funciones(data.funcion, data.variable)
        
        # Secante nos retorna 3 valores
        raiz, total_it, historial = secante(
            f_ejecutable, data.a, data.b, data.tol, data.max_iter
        )
        
        return {
            "resultado": raiz,
            "total_iteraciones": total_it,
            "datos_tabla": historial
        }
        
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
        
        
        
        
    
    