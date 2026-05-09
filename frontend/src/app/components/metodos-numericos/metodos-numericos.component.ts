// src/app/components/metodos-numericos/metodos-numericos.component.ts
import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { MetodosNumericosService } from '../../services/metodos-numericos.service';
import {
  RequestNoLineal,
  RequestLineal,
  RespuestaMetodo,
  FilaNoLineal,
  FilaLineal,
} from '../../models/metodos.model';

type Categoria = 'no-lineal' | 'lineal';
type MetodoNoLineal = 'biseccion' | 'falsaposicion' | 'newton' | 'puntofijo' | 'secante';
type MetodoLineal = 'jacobi' | 'gauss-seidel';
type Metodo = MetodoNoLineal | MetodoLineal;



interface ConfigMetodo {
  label: string;
  categoria: Categoria;
  requiereA: boolean;
  requiereB: boolean;
  requiereX0: boolean;
  requiereFuncion: boolean;
  requiereMatriz: boolean;
}

@Component({
  selector: 'app-metodos-numericos',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './metodos-numericos.component.html',
  styleUrls: ['./metodos-numericos.component.scss'],
})
export class MetodosNumericosComponent implements OnInit {
  // ─── Tab activo ─────────────────────────────────────────────────────────────
  categoriaActiva: Categoria = 'no-lineal';
  metodoActivo: Metodo = 'biseccion';

  // ─── Config de métodos ───────────────────────────────────────────────────────
  readonly metodos: Record<Metodo, ConfigMetodo> = {
    biseccion: { label: 'Bisección', categoria: 'no-lineal', requiereA: true, requiereB: true, requiereX0: false, requiereFuncion: true, requiereMatriz: false },
    falsaposicion: { label: 'Falsa Posición', categoria: 'no-lineal', requiereA: true, requiereB: true, requiereX0: false, requiereFuncion: true, requiereMatriz: false },
    newton: { label: 'Newton-Raphson', categoria: 'no-lineal', requiereA: false, requiereB: false, requiereX0: true, requiereFuncion: true, requiereMatriz: false },
    puntofijo: { label: 'Punto Fijo', categoria: 'no-lineal', requiereA: false, requiereB: false, requiereX0: true, requiereFuncion: true, requiereMatriz: false },
    secante: { label: 'Secante', categoria: 'no-lineal', requiereA: true, requiereB: true, requiereX0: false, requiereFuncion: true, requiereMatriz: false },
    jacobi: { label: 'Jacobi', categoria: 'lineal', requiereA: false, requiereB: false, requiereX0: false, requiereFuncion: false, requiereMatriz: true },
    'gauss-seidel': { label: 'Gauss-Seidel', categoria: 'lineal', requiereA: false, requiereB: false, requiereX0: false, requiereFuncion: false, requiereMatriz: true },
  };

  get metodosNoLineales(): Metodo[] {
    return Object.keys(this.metodos).filter(k => this.metodos[k as Metodo].categoria === 'no-lineal') as Metodo[];
  }

  get metodosLineales(): Metodo[] {
    return Object.keys(this.metodos).filter(k => this.metodos[k as Metodo].categoria === 'lineal') as Metodo[];
  }

  get configActual(): ConfigMetodo {
    return this.metodos[this.metodoActivo];
  }


  // ─── Formulario No Lineal ────────────────────────────────────────────────────
  funcion: string = 'x**3 - x - 2';
  variable: string = 'x';
  a: number | null = 1;
  b: number | null = 2;
  x0: number | null = 1.5;
  tol: number = 0.0001;
  maxIter: number = 100;

  // ─── Formulario Lineal (matriz dinámica) ─────────────────────────────────────
  tamanoSistema: number = 3;
  matrizA: number[][] = [];
  vectorB: number[] = [];

  // ─── Estado ──────────────────────────────────────────────────────────────────
  cargando: boolean = false;
  error: string | null = null;
  respuestaNoLineal: RespuestaMetodo<FilaNoLineal> | null = null;
  respuestaLineal: RespuestaMetodo<FilaLineal> | null = null;

  // ─── Columnas de tabla dinámica ───────────────────────────────────────────────
  columnasNoLineal: string[] = [];

  constructor(private service: MetodosNumericosService) { }

  ngOnInit(): void {
    this.inicializarMatriz();
  }

  // ─── Cambio de categoría ──────────────────────────────────────────────────────
  seleccionarCategoria(cat: Categoria): void {
    this.categoriaActiva = cat;
    this.metodoActivo = cat === 'no-lineal' ? 'biseccion' : 'jacobi';
    this.limpiarResultados();
  }

  seleccionarMetodo(m: Metodo): void {
    this.metodoActivo = m;
    this.limpiarResultados();
  }

  limpiarResultados(): void {
    this.respuestaNoLineal = null;
    this.respuestaLineal = null;
    this.error = null;
  }

  // ─── Matriz dinámica ──────────────────────────────────────────────────────────
  inicializarMatriz(): void {
    const n = this.tamanoSistema;
    this.matrizA = Array.from({ length: n }, () => Array(n).fill(0));
    this.vectorB = Array(n).fill(0);
  }

  actualizarTamano(): void {
    const n = this.tamanoSistema;
    if (n < 2 || n > 6) return;
    this.inicializarMatriz();
    this.limpiarResultados();
  }

  trackByIndex(index: number): number {
    return index;
  }

  // ─── Resolver ────────────────────────────────────────────────────────────────
  resolver(): void {
    this.error = null;
    this.respuestaNoLineal = null;
    this.respuestaLineal = null;

    if (this.configActual.requiereMatriz) {
      this.resolverLineal();
    } else {
      this.resolverNoLineal();
    }
  }

  private resolverNoLineal(): void {
    const datos: RequestNoLineal = {
      funcion: this.funcion,
      variable: this.variable,
      tol: this.tol,
      max_iter: this.maxIter,
      a: this.a ?? undefined,
      b: this.b ?? undefined,
      x0: this.x0 ?? undefined,
    };

    this.cargando = true;

    const obs$ = (() => {
      switch (this.metodoActivo) {
        case 'biseccion': return this.service.resolverBiseccion(datos);
        case 'falsaposicion': return this.service.resolverFalsaPosicion(datos);
        case 'newton': return this.service.resolverNewtonRaphson(datos);
        case 'puntofijo': return this.service.resolverPuntoFijo(datos);
        case 'secante': return this.service.resolverSecante(datos);
        default: return this.service.resolverBiseccion(datos);
      }
    })();

    obs$.subscribe({
      next: (res) => {
        this.respuestaNoLineal = res;
        this.columnasNoLineal = this.inferirColumnas(res.datos_tabla);
        this.cargando = false;
      },
      error: (err) => {
        this.error = err?.error?.detail ?? 'Error al conectar con el servidor.';
        this.cargando = false;
      },
    });
  }

  private resolverLineal(): void {
    const datos: RequestLineal = {
      A: this.matrizA.map(fila => [...fila]),
      b: [...this.vectorB],
      tol: this.tol,
      max_iter: this.maxIter,
    };

    this.cargando = true;

    const obs$ = this.metodoActivo === 'jacobi'
      ? this.service.resolverJacobi(datos)
      : this.service.resolverGaussSeidel(datos);

    obs$.subscribe({
      next: (res) => {
        this.respuestaLineal = res;
        this.cargando = false;
      },
      error: (err) => {
        this.error = err?.error?.detail ?? 'Error al conectar con el servidor.';
        this.cargando = false;
      },
    });
  }

  // ─── Helpers de tabla ────────────────────────────────────────────────────────
  private inferirColumnas(tabla: FilaNoLineal[]): string[] {
    if (!tabla || tabla.length === 0) return [];
    return Object.keys(tabla[0]);
  }

  formatNum(val: unknown): string {
    if (val === undefined || val === null) return '—';
    if (typeof val === 'number') {
      return Math.abs(val) < 1e-10 ? val.toExponential(4) : val.toPrecision(8);
    }
    return String(val);
  }

  getFilaValue(fila: FilaNoLineal, col: string): unknown {
    return (fila as unknown as Record<string, unknown>)[col];
  }

  get solucionLineal(): string {
    if (!this.respuestaLineal?.solucion) return '';
    return this.respuestaLineal.solucion
      .map((v, i) => `x${i + 1} = ${v.toPrecision(8)}`)
      .join(',  ');
  }

  get variablesLineal(): string[] {
    if (!this.respuestaLineal?.solucion) return [];
    return this.respuestaLineal.solucion.map((_, i) => `x${i + 1}`);
  }

}
