import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { MetodosNumericosComponent } from './components/metodos-numericos/metodos-numericos.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [MetodosNumericosComponent],
  template: `<app-metodos-numericos></app-metodos-numericos>`,
})
export class AppComponent {
  title = 'frontend';
}
