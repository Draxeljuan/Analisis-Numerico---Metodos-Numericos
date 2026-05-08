import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { RespuestaMetodo, RequestNoLineal, RequestLineal, FilaLineal, FilaNoLineal } from '../app/models/metodos.model';


@Injectable({
  providedIn: 'root'
})
export class MetodosNumericosService {

  private API_URL = 'http://127.0.0.1:8000';

  constructor(private http: HttpClient) { }

  // Biseccion
  resolverBiseccion(datos: RequestNoLineal): Observable<RespuestaMetodo<FilaNoLineal>> {
    return this.http.post<RespuestaMetodo<FilaNoLineal>>(`${this.API_URL}/no-lineal/biseccion`, datos);
  }

  // Falsa Posicion
  resolverFalsaPosicion(datos: RequestNoLineal): Observable<RespuestaMetodo<FilaNoLineal>> {
    return this.http.post<RespuestaMetodo<FilaNoLineal>>(`${this.API_URL}/no-lineal/falsaposicion`, datos);
  }

  // NewtonRaphson
  resolverNewtonRaphson(datos: RequestNoLineal): Observable<RespuestaMetodo<FilaNoLineal>> {
    return this.http.post<RespuestaMetodo<FilaNoLineal>>(`${this.API_URL}/no-lineal/newton-raphson`, datos);
  }

  // Punto Fijo
  resolverPuntoFijo(datos: RequestNoLineal): Observable<RespuestaMetodo<FilaNoLineal>> {
    return this.http.post<RespuestaMetodo<FilaNoLineal>>(`${this.API_URL}/no-lineal/puntofijo`, datos);
  }

  // Punto Secante
  resolverSecante(datos: RequestNoLineal): Observable<RespuestaMetodo<FilaNoLineal>> {
    return this.http.post<RespuestaMetodo<FilaNoLineal>>(`${this.API_URL}/no-lineal/secante`, datos);
  }

  // Jacobi
  resolverJacobi(datos: RequestLineal): Observable<RespuestaMetodo<FilaLineal>> {
    return this.http.post<RespuestaMetodo<FilaLineal>>(`${this.API_URL}/lineal/jacobi`, datos);
  }

  // Jacobi
  resolverGaussSeidel(datos: RequestLineal): Observable<RespuestaMetodo<FilaLineal>> {
    return this.http.post<RespuestaMetodo<FilaLineal>>(`${this.API_URL}/lineal/gauss-seidel`, datos);
  }

  



}
