// src/app/models/metodos.model.ts

// ─── REQUESTS ───────────────

export interface RequestNoLineal {
  funcion: string;
  variable?: string;
  tol: number;
  max_iter?: number;
  a?: number;
  b?: number;
  x0?: number;
}

export interface RequestLineal {
  A: number[][];
  b: number[];
  tol: number;
  max_iter?: number;
}

// ─── ROWS DE HISTORIAL ──────

// No lineal: bisección, falsa posición, secante, newton-raphson, punto fijo
export interface FilaNoLineal {
  iteracion: number;
  a?: number;
  b?: number;
  x?: number;
  x0?: number;
  x1?: number;
  xi?: number;
  fx?: number;
  error: number;
}

// Lineal: jacobi, gauss-seidel
export interface FilaLineal {
  iteracion: number;
  valores: number[];
  error: number;
}

// ─── RESPUESTA GENÉRICA ─────

export interface RespuestaMetodo<T> {
  // No lineal
  resultado?: number;
  // Lineal
  solucion?: number[];
  total_iteraciones: number;
  es_dominante?: boolean;
  datos_tabla: T[];
}